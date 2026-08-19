# OpenBiz Box — Bootstrap Deployment

This is the first runnable infrastructure scaffold for OpenBiz Box. It is **development/bootstrap quality**, not a production release yet.

## Requirements

- Linux host recommended
- Docker Engine
- Docker Compose v2
- 4 GB RAM minimum for the basic core; more is strongly recommended
- considerably more memory/GPU capacity for useful local AI models

## Start

```bash
git clone https://github.com/virtualhowto/OpenBiz-Box.git
cd OpenBiz-Box
cp .env.example .env
```

Edit `.env` and replace every `CHANGE_ME` value.

Then start the core:

```bash
docker compose up -d
```

To include the local Ollama service:

```bash
docker compose --profile local-ai up -d
```

Check status:

```bash
docker compose ps
```

## Current bootstrap services

- Traefik
- PostgreSQL
- Redis
- Uptime Kuma
- n8n
- Qdrant
- LiteLLM
- LiveKit Server
- optional Ollama

## Not yet production ready

The current Compose file intentionally establishes the platform skeleton first. Before exposing it publicly, OpenBiz still needs:

- TLS/ACME or an external trusted ingress
- Authentik bootstrap and forward-auth/OIDC integration
- secrets management
- network/host hardening
- LiveKit production keys generated into configuration
- LiveKit Agent worker
- STT/TTS worker configuration
- Tool Gateway
- control plane
- backup/restore jobs
- full monitoring/logging
- workload installer
- Business Pack generator
- automated upgrades and rollback

Do not expose this bootstrap stack directly to the Internet as a production business platform.
