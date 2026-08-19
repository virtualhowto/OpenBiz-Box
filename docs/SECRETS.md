# Secrets Management

OpenBiz Box never stores production secrets in tracked configuration.

## GitHub Actions

GitHub Actions Secrets are used to transport deployment credentials and runtime secrets to the target host during CI/CD. GitHub is **not** treated as the runtime secret store.

Create a GitHub Environment named `production` and configure the following Environment Secrets:

- `DEPLOY_HOST`
- `DEPLOY_USER`
- `DEPLOY_SSH_PRIVATE_KEY`
- `DEPLOY_HOST_KEY`
- `POSTGRES_PASSWORD`
- `REDIS_PASSWORD`
- `N8N_ENCRYPTION_KEY`
- `LITELLM_MASTER_KEY`
- `QDRANT_API_KEY`
- `LIVEKIT_API_KEY`
- `LIVEKIT_API_SECRET`
- `OPENAI_API_KEY` (optional)
- `ANTHROPIC_API_KEY` (optional)

Environment Variables:

- `OPENBIZ_DOMAIN`
- `N8N_HOST`

The workflow creates a temporary `.env.runtime` with restrictive permissions, transfers it to the deployment host as `~/openbiz-box/.env`, sets mode `600`, deploys the Compose stack and removes the runner copy.

## LiveKit

`voice/livekit.yaml` deliberately contains no API key or secret.

At runtime Compose constructs LiveKit's `LIVEKIT_KEYS` environment value from:

```text
LIVEKIT_API_KEY
LIVEKIT_API_SECRET
```

This keeps the credentials out of Git history.

## Local/manual deployments

Copy `.env.example` to `.env`, generate strong random values, and keep `.env` local. `.gitignore` excludes it.

## Future production secret providers

The OpenBiz secret abstraction should support:

- Docker secrets / mounted secret files
- OpenBao
- HashiCorp Vault
- Azure Key Vault
- AWS Secrets Manager
- other provider adapters

The long-term model is:

```text
CI/CD identity → deployment host → runtime secret provider → workload
```

rather than passing secrets through application configuration wherever a workload supports secret-file/provider integration.

## Rules

1. Never commit populated `.env` files.
2. Never put real credentials in Business Pack YAML.
3. Never put API secrets in tracked LiveKit/LiteLLM configuration.
4. Prefer GitHub Environment Secrets over repository-wide secrets for production deployments.
5. Protect the production environment with reviewers where appropriate.
6. Rotate any credential that is accidentally committed, even if the commit is later deleted.
