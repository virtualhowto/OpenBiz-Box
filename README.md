# OpenBiz Box

**Open Business in a Box** — an open-source, modular business operating platform designed to deploy and operate the core technology a small business needs.

> Run your business. Own your stack.

## Vision

OpenBiz Box turns a curated collection of open-source services into an integrated business platform rather than a collection of unrelated containers.

The platform is built around four interfaces:

- **Web** — unified control plane and business dashboard
- **Chat** — conversational AI interface
- **Voice** — real-time voice AI for operating and querying the business
- **API** — automation and third-party integration

## Architecture

```text
Users / Customers / Administrators
              |
     +--------+--------+
     |        |        |
    Web      Chat     Voice
     |        |        |
     +--------+--------+
              |
       OpenBiz Control Plane
              |
 +------------+-------------+
 |            |             |
Identity   Automation      AI/Agents
Authentik     n8n       LLM / RAG / Voice
 |            |             |
 +------------+-------------+
              |
      Business Applications
              |
 +------+-----+------+-------+
 |      |     |      |       |
CRM  Finance Docs Support Projects
```

## OpenBiz Core

Core services are intended to include:

- Docker / Compose
- Traefik
- Authentik
- Portainer
- CrowdSec
- Uptime Kuma
- Prometheus / Grafana / Loki
- Restic / Backrest
- n8n
- OpenBiz Control Plane
- AI Gateway
- Voice AI Gateway

## Business Applications

Initial application catalogue:

- ERPNext — ERP / CRM / finance / inventory
- Nextcloud — files and collaboration
- OnlyOffice — browser office suite
- BookStack — knowledge and SOPs
- Chatwoot — customer communications
- Zammad — service desk option
- Kimai — time tracking
- Cal.com — scheduling
- Documenso — digital signatures
- Listmonk — mailing lists and campaigns
- Stirling PDF — PDF tools
- Snipe-IT — asset management
- NetBox — infrastructure/IPAM option

## AI Core

OpenBiz Box treats AI as platform infrastructure.

Planned components:

- LiteLLM-compatible AI gateway
- local and cloud LLM providers
- Ollama / vLLM support
- Open WebUI or OpenBiz-native chat
- Qdrant-backed knowledge/RAG
- business-aware agents
- tool calling into OpenBiz services
- permission-aware agent actions

## Voice AI

Voice is a first-class OpenBiz interface.

The voice layer will support:

- streaming speech-to-text
- streaming text-to-speech
- local and cloud providers
- interruption / barge-in
- conversational sessions
- agent tool calling
- Authentik-derived identity and permissions
- business queries and actions

Example requests:

- “What invoices are overdue?”
- “Give me my business briefing.”
- “Create a quote for this customer.”
- “What support tickets need attention?”
- “Book a meeting next Tuesday.”
- “Which customer backups failed overnight?”

## Business Packs

OpenBiz will configure workloads, workflows, dashboards and agents using industry packs.

Initial packs:

1. General Small Business
2. Professional Services
3. MSP / IT Provider

Future candidates:

- Trades
- Retail
- E-commerce
- Clubs / NFP
- Consulting
- Manufacturing

## Repository Direction

```text
openbiz-box/
├── control-plane/
├── core/
├── workloads/
├── packs/
│   ├── general-business/
│   ├── professional-services/
│   └── msp/
├── agents/
├── voice/
├── workflows/
├── integrations/
├── templates/
├── docs/
└── deploy/
```

## Design Principles

1. Open-source first.
2. Self-hostable by default.
3. SaaS integrations remain optional.
4. Applications are replaceable modules.
5. Identity is centralised.
6. APIs and events connect everything.
7. AI agents use the same permissions as users.
8. Voice, chat and web expose the same business capabilities.
9. Backups and observability are platform requirements, not add-ons.
10. Business packs deliver outcomes rather than lists of software.

## Status

🚧 **Early architecture / bootstrap stage**

The first milestone is a working OpenBiz Core deployment plus the General Business pack and the foundations of the MSP pack.

## License

License selection is pending while the project architecture and third-party component licensing model are reviewed.
