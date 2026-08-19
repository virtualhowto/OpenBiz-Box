# OpenBiz Identity — Authentik

Authentik is the identity provider for OpenBiz Box. It owns human authentication, MFA and application access; OpenBiz services consume identity rather than maintaining independent user passwords where practical.

## Bootstrap

OpenBiz pins an Authentik release through `AUTHENTIK_TAG` rather than using `latest`.

For unattended first-run deployment, generate a password hash with Authentik's `hash_password` command and place the complete hash in `AUTHENTIK_BOOTSTRAP_PASSWORD_HASH`. This value is consumed only on first startup.

## Planned OpenBiz objects

The bootstrap blueprint will create:

- OpenBiz application/provider
- OpenBiz Owners group
- OpenBiz Administrators group
- Finance, Sales, Support and User groups
- OIDC provider for the Control Plane
- standard claims for user ID, email, groups and business/tenant context

## Security boundary

The browser authenticates with Authentik. The Control Plane exchanges/validates OIDC identity and passes signed identity context to internal OpenBiz services. The Tool Gateway must validate that context before executing business capabilities.

Direct trust of arbitrary `X-OpenBiz-User` headers is development-only and will be removed before the MVP is marked production-capable.
