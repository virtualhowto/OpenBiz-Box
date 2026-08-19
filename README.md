<div align="center">

# 📦 OpenBiz Box

### Open Business in a Box

**Run your business. Own your stack. Manage your AI staff.**

An open-source, self-hostable **human-governed autonomous business platform** where AI staff can operate the business while people retain control over goals, policy, approvals, money and exceptions.

**Human Governance · AI Workforce · Voice · CRM · Finance · Operations · Automation · API**

> 🚧 Early development. The platform architecture, governance model and first Business Packs are being built toward a runnable MVP.

</div>

---

## 💡 What is OpenBiz Box?

Small businesses shouldn't need dozens of disconnected SaaS subscriptions — or an ungoverned AI with master credentials to all of them.

OpenBiz Box combines proven open-source business applications with an **AI Workforce, Governance Engine, durable workflows, real-time voice and a permission-aware Tool Gateway**.

The operating principle is:

> **Agents operate the business. Humans govern the business.**

```text
                    👤 HUMAN GOVERNANCE
               Goals · Policy · Approvals
                          │
                          ▼
                    🧠 AI WORKFORCE
       Chief of Staff · Sales · Finance · Operations
          Support · Marketing · Procurement · IT
                          │
                          ▼
                    ⚖️ GOVERNANCE
          Identity · Delegation · Budgets · Audit
                          │
                          ▼
                    🔄 ORCHESTRATION
                      Temporal + n8n
                          │
                          ▼
                    🔌 TOOL GATEWAY
                          │
                          ▼
                    🗄️ BUSINESS SYSTEMS
       ERPNext · Chatwoot · Nextcloud · Cal.com · more
```

## 👥 AI staff, not one super-agent

OpenBiz gives specialist agents separate identities, jobs, permissions, budgets and audit histories.

Initial workforce:

| AI staff member | Role |
|---|---|
| 🧭 **Chief of Staff** | Management briefings, prioritisation and delegation |
| 💼 **Sales Agent** | Leads, CRM, quotes, scheduling and sales follow-up |
| 💰 **Finance Agent** | Receivables, finance monitoring and payment proposals |
| ⚙️ **Operations Agent** | Projects, delivery, workload and exceptions |
| 🎧 **Support Agent** | Customer triage, knowledge and routine support |
| 📣 **Marketing Agent** | Campaign and content preparation |
| 🛒 **Procurement Agent** | Supplier and purchasing preparation |
| 🛡️ **IT & Security Agent** | Platform health, security events and remediation proposals |

See [`agents/workforce.yaml`](agents/workforce.yaml) for the initial machine-readable workforce definition.

## 👤 Humans remain in control

Every governed action can be configured as:

| Mode | Behaviour |
|---|---|
| **AUTO** | Agent may execute |
| **NOTIFY** | Agent executes and informs a human |
| **APPROVE** | Agent prepares the action and waits for approval |
| **HUMAN** | Human must perform the action |
| **DENY** | Agent is prohibited from the capability |

Policies can include limits such as monetary value, discount percentage, customer, data sensitivity, cumulative budget and approver role.

```text
Finance Agent
────────────────────────────────────
Supplier payment INV-3941
Amount: $4,820
Reason: Approved supplier invoice due today
Policy: Payments > $2,500 require approval

        [Approve] [Reject] [Modify] [Ask Agent]
```

The initial policy model lives in [`governance/policies.yaml`](governance/policies.yaml).

## 🎙️ Manage the business by voice

**LiveKit + LiveKit Agents** are the planned real-time voice foundation.

> “OpenBiz, give me today's management briefing.”
>
> “There are four items requiring your approval. Sales has a proposal ready, Finance has two supplier payments, and Operations has flagged a project at risk.”
>
> “Let's deal with the project first.”

Voice, chat and workflow agents all call the **same governed OpenBiz tools**. Voice never becomes a shortcut around permissions.

Planned voice stack:

- LiveKit Server + LiveKit Agents
- faster-whisper local STT option
- Kokoro / Piper local TTS options
- LiteLLM model routing
- browser/mobile WebRTC
- future SIP AI phone agents

## 🔄 Durable business processes

OpenBiz separates AI reasoning from authoritative workflow state.

**Temporal** is planned for important long-running processes involving approvals, waits, retries, deadlines and compensation. **n8n** remains the integration and straightforward automation layer.

```text
Sales Agent prepares proposal
          ↓
Human approval if required
          ↓
Customer accepts
          ↓
Contract prepared
          ↓
WAIT for signature
          ↓
Finance setup
          ↓
Operations project
          ↓
Customer onboarding
```

An LLM conversation is never the database for a three-week business process.

## 📊 Measure your AI workforce

OpenBiz is designed to meter AI cost and business outcomes per agent.

```text
Sales Agent
────────────────────────
AI cost this month       $37.82
Leads processed              483
Meetings booked               31
Quotes prepared               18
Approvals requested            4
Revenue influenced        $42,300
```

Each agent can have a monthly AI budget, preferred/fallback models and workload limits.

## ✨ Four human interfaces

| Interface | What it provides |
|---|---|
| 🖥️ **Web** | Control Plane, Approval Inbox, dashboards and apps |
| 💬 **Chat** | Management and specialist-agent conversations |
| 🎙️ **Voice** | Real-time conversations, briefings and governed actions |
| 🔌 **API** | Integrations, events and external systems |

## 🧩 OpenBiz Core

| Area | Planned foundation |
|---|---|
| 🚪 Ingress | Traefik |
| 🔐 Human Identity | Authentik |
| 👥 AI Workforce | OpenBiz Agent Runtime abstraction |
| ⚖️ Governance | OpenBiz Governance Engine |
| 🔌 Business Actions | OpenBiz Tool Gateway |
| 🔄 Durable Workflows | Temporal |
| ⚡ Integration Automation | n8n |
| 🤖 AI Gateway | LiteLLM |
| 🧠 Knowledge / RAG | Qdrant |
| 🎙️ Voice | LiveKit + LiveKit Agents |
| 📈 Operations | Uptime Kuma + Prometheus + Grafana + Loki |
| 💾 Backup | Restic + Backrest |
| 🧭 Experience | OpenBiz Control Plane |

## 🏢 Systems of record

The AI workforce operates modular business applications through governed adapters rather than receiving unrestricted credentials.

| Capability | Initial choice |
|---|---|
| ERP / CRM / Finance / Inventory | ERPNext |
| Files & Collaboration | Nextcloud |
| Browser Office | OnlyOffice |
| Knowledge & SOPs | BookStack |
| Customer Conversations | Chatwoot |
| Service Desk | Zammad |
| Time Tracking | Kimai |
| Scheduling | Cal.com |
| Digital Signatures | Documenso |
| Email Campaigns | Listmonk |
| PDF Toolkit | Stirling PDF |
| Asset Management | Snipe-IT |
| Network / IPAM | NetBox |

## 📦 Business Packs

Business Packs define applications, workflows, AI staff, permissions, dashboards, templates and policies for an operating model.

- 🏪 **General Small Business** — baseline commercial and operational environment
- 💼 **Professional Services** — projects, quotes, contracts, time and delivery
- 🛠️ **MSP / IT Provider** — service desk, RMM, security, SLAs and managed-service operations

Future packs can include Trades, Retail, E-commerce, Clubs/NFP and Manufacturing.

## 🔐 Safety by architecture

OpenBiz is designed around least privilege rather than hoping the model behaves correctly.

- separate service identity per AI staff member
- no universal agent credential
- capability-level permissions
- financial and AI-spend budgets
- policy checks before tools execute
- durable human approvals
- complete audit trail
- global and per-agent kill switches
- secrets outside source control

See [`docs/AI-WORKFORCE.md`](docs/AI-WORKFORCE.md), [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and [`docs/SECRETS.md`](docs/SECRETS.md).

## 🗂️ Repository direction

```text
openbiz-box/
├── control-plane/       # Dashboard, Approval Inbox, management UI/API
├── core/                # Shared platform services
├── governance/          # Delegation, approval and budget policies
├── agents/              # AI workforce definitions/runtime adapters
├── workflows/           # Temporal + n8n workflows
├── tools/               # Governed capability/tool adapters
├── voice/               # LiveKit voice runtime
├── workloads/           # Application/module definitions
├── packs/               # Business operating models
├── integrations/        # External connectors
├── templates/           # Business templates
├── docs/
└── deploy/
```

## 🗺️ MVP target

```text
Clone → Configure → Deploy → Select Business Pack
                     ↓
              Create AI Workforce
                     ↓
           Set Delegation & Budgets
                     ↓
               Start Business
                     ↓
         Human manages by exception
```

### MVP workstreams

- [ ] OpenBiz Control Plane
- [ ] Approval Inbox
- [ ] Governance Engine
- [ ] AI workforce identity/runtime
- [ ] Tool Gateway
- [ ] Temporal durable workflows
- [ ] n8n integration foundation
- [ ] Authentik SSO bootstrap
- [ ] LiteLLM + Qdrant AI foundation
- [ ] LiveKit voice agent
- [ ] Workload/module specification
- [ ] Business Pack installer
- [ ] AI budget/cost metering
- [ ] Audit/event ledger
- [ ] Kill switches
- [ ] General Business Pack
- [ ] MSP Pack
- [ ] Backup/restore and observability
- [ ] CI / validation / upgrade strategy

## 🌱 Status

**Early development / architecture bootstrap.** A runnable infrastructure scaffold now exists, but OpenBiz is not yet a production autonomous-business platform. The next implementation milestone is the Governance Engine + Approval Inbox + Tool Gateway + first AI staff runtime.

## ⚖️ Licensing

OpenBiz Box's own license is still to be selected. Third-party applications retain their respective licenses. Licensing will be reviewed before the first distributable release.

---

<div align="center">

### 📦 OpenBiz Box

**Agents operate the business. Humans govern the business.**

</div>
