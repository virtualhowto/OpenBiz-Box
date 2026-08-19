# OpenBiz Box Architecture

## Product Layers

OpenBiz Box is organised into four primary layers.

### 1. Platform Core

Provides infrastructure shared by every business pack:

- ingress and TLS
- identity and SSO
- secrets
- networking
- backups
- monitoring
- logging
- automation/event bus
- AI gateway
- **LiveKit real-time voice infrastructure**
- OpenBiz Tool Gateway

### 2. Business Capability Modules

Applications are registered as modules providing capabilities such as CRM, finance, documents, support, projects, scheduling, signatures and assets.

A module should declare:

- capability IDs
- container/deployment definition
- dependencies
- SSO support
- backup requirements
- health checks
- API endpoints
- events/webhooks
- agent tools
- configuration schema

### 3. Business Packs

A pack selects modules and configures them for an operating model.

A pack can provide:

- required and optional workloads
- roles
- dashboards
- workflows
- templates
- AI agents
- knowledge collections
- policies
- default integrations
- voice intents and permissions

### 4. Experience Layer

Users should not need to understand which underlying application implements a capability.

OpenBiz exposes capabilities through:

- Control Plane UI
- unified search
- AI chat
- real-time Voice AI
- future SIP/telephone agent
- API
- event/webhook interface

## Core Logical Architecture

```text
                    OPENBIZ BOX

 Browser        Mobile        Voice        API Client
    |              |             |              |
    +--------------+-------------+--------------+
                           |
                    OpenBiz Gateway
                           |
                  Authentik Identity
                           |
                 OpenBiz Control Plane
                           |
       +-------------------+-------------------+
       |                   |                   |
 Automation Bus        Agent Runtime       Event Bus
      n8n             LiteLLM / RAG         Webhooks
       |                   |                   |
       +-------------------+-------------------+
                           |
                  OpenBiz Tool Gateway
                           |
              Business Capability Layer
                           |
  +----------+----------+---------+---------+----------+
  |          |          |         |         |          |
 CRM       Finance     Docs     Support   Projects    Assets
```

## AI and Agent Security

The agent runtime must not bypass application security simply because an LLM is calling a tool.

Each action should carry:

- authenticated user/service identity
- tenant/business context
- requested capability
- authorisation decision
- tool arguments
- audit ID
- result

The Tool Gateway is the policy boundary between AI/automation interfaces and business applications.

## Voice Architecture

**LiveKit Server and LiveKit Agents are the planned real-time voice foundation for OpenBiz Box.**

OpenBiz should not build its own WebRTC/media transport. LiveKit handles real-time media while the OpenBiz agent and Tool Gateway provide the business-specific intelligence and security model.

```text
Browser / Mobile microphone
          |
          | WebRTC
          v
 +-------------------+
 |  LiveKit Server   |
 +---------+---------+
           |
           v
 +-------------------+
 | LiveKit Agents    |
 | Turn / session    |
 | Barge-in          |
 | Tool invocation   |
 +---------+---------+
           |
     +-----+------+----------------+
     |            |                |
     v            v                v
    STT          LLM              TTS
faster-whisper  LiteLLM      Kokoro / Piper
 / provider      |            / provider
                 |
                 v
        OpenBiz Tool Gateway
                 |
        Identity + Policy
                 |
     +-----------+-----------+
     |           |           |
     v           v           v
   ERPNext     Chatwoot      n8n
```

### Voice requirements

The voice service should support:

- streaming speech-to-text
- streaming text-to-speech
- low-latency conversational turns
- voice activity / turn detection
- interruption and barge-in
- conversational context
- business tool calling
- identity propagation
- policy checks before privileged actions
- explicit confirmation policies
- audit trails
- local and cloud STT/TTS providers
- local and cloud LLM providers
- browser/mobile WebRTC
- future SIP telephone integration

### Voice deployment modes

**Local-first**

```text
LiveKit → faster-whisper → local LLM → Kokoro/Piper
```

**Hybrid**

```text
LiveKit → cloud/local STT → LiteLLM provider → cloud/local TTS
```

**Telephone agent (future)**

```text
PSTN / SIP provider
       |
       v
LiveKit SIP
       |
       v
OpenBiz Voice Agent
       |
       v
OpenBiz Tool Gateway
```

Business Packs define the voice capabilities exposed to users. For example, the General Business pack may expose invoices, appointments and customer communications while the MSP pack adds incidents, customer health, backup status and NOC briefings.

## Multi-Tenancy

The first release should optimise for one business per OpenBiz deployment while keeping tenant IDs in the control-plane domain model.

The MSP pack can then add management of many customer environments without requiring every third-party workload to be safely multi-tenant inside a single instance.

This favours isolation:

```text
MSP Control Plane
      |
 +----+----+----+
 |         |    |
Cust A   Cust B Cust C
Stack    Stack  Stack
```

## Security Principles

- zero implicit trust between workloads
- SSO wherever supported
- MFA at the identity layer
- secrets never committed to Git
- least-privilege service accounts
- agent actions audited
- privileged AI/voice actions require policy checks
- confirmation required where policy dictates
- public exposure kept to required services only
- encrypted backups
- tested restore procedures

## Deployment Targets

Initial target:

- single Linux Docker host

Planned targets:

- Docker Compose
- multi-host Docker
- remote GPU/AI worker
- cloud VM
- on-prem appliance
- MSP-managed customer node

Kubernetes should not be required for a normal small-business deployment.
