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
- voice gateway

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

### 4. Experience Layer

Users should not need to understand which underlying application implements a capability.

OpenBiz exposes capabilities through:

- Control Plane UI
- unified search
- AI chat
- Voice AI
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
      n8n                AI Gateway         Webhooks
       |                   |                   |
       +-------------------+-------------------+
                           |
              Business Capability Layer
                           |
  +----------+----------+---------+---------+----------+
  |          |          |         |         |          |
 CRM       Finance     Docs     Support   Projects    Assets
```

## AI and Voice

The agent runtime must not bypass application security simply because an LLM is calling a tool.

Each action should carry:

- authenticated user/service identity
- tenant/business context
- requested capability
- authorisation decision
- tool arguments
- audit ID
- result

Voice follows the same tool path as text chat:

```text
Microphone
   |
Streaming STT
   |
Conversation Runtime
   |
LLM / Agent Router
   |
OpenBiz Tool Gateway
   |
Business Applications
   |
Streaming TTS
   |
Speaker
```

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
- privileged AI actions require policy checks
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
