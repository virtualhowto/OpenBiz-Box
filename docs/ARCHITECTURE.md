# OpenBiz Box Architecture

## North Star

OpenBiz Box is a **human-governed autonomous business platform**. Open-source business applications remain the systems of record, while AI staff operate those systems through controlled tools, durable workflows and explicit human governance.

```text
                    HUMAN GOVERNANCE
              Goals · Policy · Approval · Exceptions
                             |
                             v
                       AI WORKFORCE
       Chief of Staff · Sales · Finance · Ops · Support · IT
                             |
                             v
                    GOVERNANCE ENGINE
       Identity · Delegation · Budgets · Approval · Audit
                             |
                             v
                  PROCESS ORCHESTRATION
                       Temporal + n8n
                             |
                             v
                    OPENBIZ TOOL GATEWAY
                             |
                             v
                     SYSTEMS OF RECORD
       ERPNext · Chatwoot · Nextcloud · Cal.com · Documenso
```

Humans retain authority. Agents can research, propose, prepare and execute only within their delegated permissions.

## Product Layers

### 1. Platform Core

- ingress and TLS
- identity and SSO
- secrets
- networking
- backup and restore
- monitoring and logging
- event/integration automation
- AI gateway and RAG
- LiveKit real-time voice
- Temporal durable workflow engine
- OpenBiz Tool Gateway

### 2. Governance Plane

The governance plane determines what a human, service or AI staff member may do.

Every governed action is assigned one of five modes:

- `auto` — execute without approval
- `notify` — execute and notify the relevant human
- `approve` — prepare/propose and wait for human approval
- `human` — human execution only
- `deny` — prohibited for the identity

Policies can additionally constrain:

- monetary amount
- discount percentage
- customer/account
- data sensitivity
- time window
- tool/application
- transaction type
- cumulative budget
- model/token spend
- approver role

Every action should produce an immutable audit event containing identity, tenant, capability, policy decision, arguments, approval state, execution result and correlation ID.

### 3. AI Workforce

Agents are first-class workforce identities, not one shared super-user.

Initial roles:

- `agent.chief-of-staff`
- `agent.sales`
- `agent.finance`
- `agent.operations`
- `agent.support`
- `agent.marketing`
- `agent.procurement`
- `agent.it-security`

Each agent has:

- service identity
- job description
- objectives
- tools
- data scope
- delegation policy
- human escalation path
- monthly AI budget
- preferred/fallback models
- memory/knowledge scope
- audit history
- business KPIs

The Agent Runtime interface should avoid hard coupling OpenBiz to one framework. LangGraph, CrewAI or future runtimes can be adapters behind the OpenBiz agent contract.

### 4. Process Orchestration

OpenBiz separates reasoning from durable business process state.

**Temporal** owns important, long-running workflows: approvals, waiting, retries, compensation, timers and process state.

**n8n** handles integrations, webhooks and straightforward automation.

An LLM should never be the database for a three-week business process.

Example:

```text
Lead qualified
   |
Sales Agent drafts proposal
   |
Human approval if policy requires
   |
Customer accepts
   |
Contract Agent prepares agreement
   |
WAIT for signature
   |
Finance creates account/invoice state
   |
Operations creates project
   |
Customer Success begins onboarding
```

### 5. Tool / Capability Layer

Applications register capabilities with the OpenBiz Tool Gateway. Agents never receive unrestricted application credentials simply because they need a function.

A capability definition should declare:

- capability ID
- read/write classification
- risk level
- required identity claims
- policy hooks
- application adapter
- argument schema
- audit schema
- idempotency behaviour
- rollback/compensation support

### 6. Systems of Record

Business applications remain modular and replaceable. Initial systems include ERPNext, Nextcloud, Chatwoot, BookStack, Cal.com, Documenso, Kimai, Snipe-IT and other Business Pack workloads.

### 7. Experience Layer

Humans interact through:

- OpenBiz Control Plane
- approval inbox
- management dashboard
- AI chat
- LiveKit real-time voice
- future SIP/telephone interface
- API and webhooks

## Human Oversight

Human oversight is a product feature, not an exception handler.

The Control Plane should provide a unified **Approval Inbox** containing:

- action requested
- requesting AI staff member
- business rationale
- supporting evidence
- financial/risk impact
- proposed tool call
- policy that triggered approval
- approve / reject / modify / delegate actions

Example:

```text
Finance Agent
Supplier payment INV-3941
Amount: $4,820
Policy: payments > $2,500 require approval
Status: WAITING FOR OWNER

[Approve] [Reject] [Modify] [Ask Agent]
```

## AI Staff Cost and Performance

OpenBiz should meter AI workforce cost and outcomes by agent.

Example dashboard:

```text
Sales Agent
AI cost this month       $37.82
Leads processed              483
Meetings booked               31
Quotes prepared               18
Approvals requested            4
Revenue influenced        $42,300
```

This provides both cost control and evidence that an AI role is delivering useful work.

## Voice Architecture

LiveKit Server and LiveKit Agents remain the real-time voice foundation. Voice calls the same governed tools as chat and workflow agents.

```text
Human voice
   |
LiveKit / STT
   |
Chief of Staff or specialist agent
   |
Governance Engine
   |
OpenBiz Tool Gateway
   |
Business systems / Temporal workflows
   |
TTS
   |
Spoken response
```

A management conversation can therefore surface approvals and delegate work without bypassing policy.

## Multi-Tenancy

The first release optimises for one business per OpenBiz deployment while retaining tenant IDs throughout the control-plane domain model. MSP deployments can manage isolated customer stacks from a higher-level control plane.

## Security Principles

- humans retain ultimate delegated authority
- no shared omnipotent AI identity
- least-privilege service identities per agent
- SSO/MFA for human users
- secrets never committed to Git
- tool access mediated through policy
- privileged actions audited
- approval required where policy dictates
- financial and AI-spend budgets enforced
- public exposure limited to required services
- encrypted backups and tested restore procedures

## Deployment Targets

Initial target: single Linux Docker host.

Planned targets include Docker Compose, multi-host Docker, remote GPU/AI workers, cloud VMs, on-prem appliances and MSP-managed customer nodes. Kubernetes is not required for a normal small-business deployment.
