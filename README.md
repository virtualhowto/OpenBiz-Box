<div align="center">

# 📦 OpenBiz Box

### Open Business in a Box

**Run your business. Own your stack. Talk to your business.**

An open-source, self-hostable business operating platform that brings together the software a small business needs — with automation, AI and real-time voice built into the core.

**Web · CRM · Finance · Files · Projects · Support · Automation · AI · Voice · API**

> 🚧 OpenBiz Box is currently in early development. The architecture and first Business Packs are being defined before the runnable MVP lands.

</div>

---

## 💡 What is OpenBiz Box?

Small businesses shouldn't need dozens of disconnected SaaS subscriptions just to operate.

OpenBiz Box turns proven open-source applications into **one integrated business platform**. Identity, automation, observability, AI and voice form the common foundation; Business Packs then configure the platform for different kinds of organisations.

The goal is simple:

```text
Clone → Configure → Choose your Business Pack → Deploy → Run your business
```

OpenBiz is not intended to hide open source behind a new monolith. Applications remain modular and replaceable while the OpenBiz control plane provides the common operating experience.

## ✨ One business. Four interfaces.

| Interface | What it provides |
|---|---|
| 🖥️ **Web** | Control plane, dashboards and business applications |
| 💬 **Chat** | Conversational access to business information and agents |
| 🎙️ **Voice** | Real-time voice conversations that can query and operate the business |
| 🔌 **API** | Automation, integrations, events and external systems |

## 🧠 Talk to your business

Voice is not an afterthought in OpenBiz Box. **LiveKit + LiveKit Agents** are the planned real-time voice foundation, supporting browser/mobile WebRTC and a future SIP/telephone interface.

```text
                🎙️ YOU
                   │
                   ▼
          ┌─────────────────┐
          │     LiveKit     │
          │ Realtime Voice  │
          └────────┬────────┘
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
      STT         Agent        TTS
 faster-whisper  LiteLLM   Kokoro / Piper
                   │
                   ▼
          OpenBiz Tool Gateway
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
   ERP/CRM       Support    Automation
   ERPNext       Chatwoot       n8n
```

Ask things like:

> **“Give me my morning business briefing.”**
>
> **“Which invoices are more than 30 days overdue?”**
>
> **“Draft follow-up emails and read the first one to me.”**
>
> **“What support tickets need attention?”**
>
> **“Create a quote for this customer.”**
>
> **“Which customer backups failed overnight?”**

Read-only requests can be frictionless. Sensitive actions such as sending communications, deleting records or approving transactions can require explicit policy and confirmation before execution.

### Planned voice stack

- **LiveKit Server** — real-time WebRTC media infrastructure
- **LiveKit Agents** — conversational voice-agent runtime
- **faster-whisper** — local speech-to-text option
- **Kokoro / Piper** — local text-to-speech options
- **LiteLLM** — pluggable local/cloud LLM routing
- **OpenBiz Tool Gateway** — permission-aware business actions
- **SIP** — future inbound/outbound AI phone agents

Providers remain interchangeable so an organisation can favour fully local processing or selected cloud services.

## 🧩 OpenBiz Core

Every Business Pack builds on a common platform foundation.

| Area | Planned foundation |
|---|---|
| 🚪 Ingress | Traefik |
| 🔐 Identity | Authentik |
| 📦 Containers | Docker / Compose + Portainer |
| 🛡️ Security | CrowdSec |
| ⚡ Automation | n8n |
| 📈 Monitoring | Uptime Kuma + Prometheus + Grafana |
| 📜 Logging | Loki |
| 💾 Backup | Restic + Backrest |
| 🤖 AI Gateway | LiteLLM |
| 🧠 Knowledge / RAG | Qdrant |
| 🎙️ Voice | LiveKit + LiveKit Agents |
| 🧭 Experience | OpenBiz Control Plane |

## 🏢 Business capability catalogue

OpenBiz Business Packs select from a catalogue of replaceable capabilities rather than hard-coding one application for everything.

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

A Business Pack is more than a Compose profile. It defines the **applications, roles, workflows, dashboards, templates, policies and AI agents** needed for a particular operating model.

### 🏪 General Small Business

The baseline business operating environment: customers, CRM, finance, documents, knowledge, scheduling, signatures, communications, automation, AI and voice.

### 💼 Professional Services

Projects, customers, quotations, contracts, time, delivery workflows, invoicing and knowledge — designed for consulting and service businesses.

### 🛠️ MSP / IT Provider

Extends OpenBiz into an MSP operating platform with service desk, RMM, remote access, security monitoring, infrastructure inventory, customer environments, SLAs and managed-service reporting.

Future packs can include **Trades · Retail · E-commerce · Clubs/NFP · Manufacturing** and others.

## 🤖 AI is infrastructure, not a plugin

OpenBiz agents will use the same business capability layer whether the request comes from chat, voice, an automation or an API call.

```text
                 OpenBiz Agent Layer
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
      Chat             Voice          Automation
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                OpenBiz Tool Gateway
                         │
                Identity + Policy
                         │
       ┌─────────┬───────┼───────┬─────────┐
       ▼         ▼       ▼       ▼         ▼
      CRM      Finance  Docs   Support   Projects
```

Every privileged action should be attributable to an authenticated user or service identity and recorded for audit.

## 🏗️ Architecture

```text
 Users · Customers · Administrators
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
     Web        Chat       Voice
      └──────────┼──────────┘
                 ▼
       OpenBiz Control Plane
                 │
    ┌────────────┼────────────┐
    ▼            ▼            ▼
 Identity    Automation    AI / Agents
 Authentik       n8n      LiteLLM / RAG
    └────────────┼────────────┘
                 ▼
       Business Capabilities
                 │
   CRM · Finance · Docs · Support
   Projects · Assets · Scheduling
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the deeper architecture direction.

## 🗂️ Repository direction

```text
openbiz-box/
├── control-plane/       # Unified OpenBiz UI/API
├── core/                # Shared platform services
├── workloads/           # Application/module definitions
├── packs/
│   ├── general-business/
│   ├── professional-services/
│   └── msp/
├── agents/              # Business agents and tools
├── voice/               # LiveKit voice runtime
├── workflows/           # n8n/OpenBiz workflows
├── integrations/        # External connectors
├── templates/           # Business templates
├── docs/
└── deploy/              # Compose/deployment assets
```

## 🔐 Design principles

1. **Open-source first** — favour software businesses can inspect and operate.
2. **Self-hostable by default** — cloud services are options, not requirements.
3. **Modular** — business applications remain replaceable.
4. **Identity first** — central SSO and MFA wherever applications support it.
5. **API/event driven** — avoid fragile point-to-point integration.
6. **AI with boundaries** — agents inherit identity, policy and audit requirements.
7. **Voice = Chat = API** — all interfaces use the same capability and security layer.
8. **Operations included** — monitoring, backup and restore are part of the product.
9. **Business outcomes over containers** — users select what their business needs, not Docker images.
10. **Keep SMB deployment understandable** — Kubernetes is not a prerequisite.

## 🗺️ MVP target

The first meaningful release should deliver this experience:

```bash
git clone <openbiz-box>
cd OpenBiz-Box
cp .env.example .env
docker compose up -d
```

Then:

**Open setup wizard → configure business → select Business Pack → provision workloads → sign in → talk to OpenBiz.**

### MVP workstreams

- [ ] OpenBiz Control Plane
- [ ] Setup wizard
- [ ] Workload/module manifest specification
- [ ] Compose generator
- [ ] Authentik SSO bootstrap
- [ ] Core observability
- [ ] Backup/restore framework
- [ ] n8n automation foundation
- [ ] LiteLLM + Qdrant AI foundation
- [ ] LiveKit voice foundation
- [ ] Permission-aware Tool Gateway
- [ ] General Business Pack deployment
- [ ] MSP Pack foundation
- [ ] CI / validation / upgrade strategy

## 🌱 Project status

**Early development / architecture bootstrap.**

The repository currently contains the product direction, architecture and initial Business Pack definitions. The next milestone is the first runnable OpenBiz Core.

Contributions, architecture discussion and experimentation will become increasingly useful as the workload specification stabilises.

## ⚖️ Licensing

OpenBiz Box's own license is still to be selected. Third-party applications retain their respective licenses. The licensing model will be reviewed before the first distributable release.

---

<div align="center">

### 📦 OpenBiz Box

**Run your business. Own your stack. Talk to your business.**

</div>
