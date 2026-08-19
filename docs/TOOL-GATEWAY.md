# OpenBiz Tool Gateway

The Tool Gateway is the policy boundary between AI/voice/automation and business applications.

## Rule

Agents do not receive unrestricted application credentials. They request named business capabilities through the Tool Gateway.

## Initial risk classes

- `read` — retrieves business information and may execute immediately when authorised.
- `write` — changes internal state and requires an authorised identity/role.
- `confirm` — externally consequential or sensitive action; requires explicit confirmation before execution.

Examples:

| Tool | Risk |
|---|---|
| `business.briefing` | read |
| `invoice.list_overdue` | read |
| `customer.search` | read |
| `ticket.create` | write |
| `communication.send` | confirm |

## Request context

Production requests will carry authenticated identity, tenant/business, roles/scopes, correlation/audit ID and tool arguments. The current MVP skeleton requires an identity header and implements the confirmation state while Authentik/JWT validation is added.

## Adapter model

Tool contracts remain stable while adapters translate them to ERPNext, Chatwoot, Nextcloud, n8n or other modules. This lets Business Packs swap underlying applications without changing every agent prompt.
