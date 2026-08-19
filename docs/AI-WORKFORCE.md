# AI Workforce Operating Model

OpenBiz Box is designed so a business can delegate substantial operational work to AI staff while humans retain authority over policy, risk, money and exceptions.

## Operating principle

**Agents operate the business. Humans govern the business.**

This does not mean every task should be autonomous. The goal is to automate routine work while making consequential decisions visible, explainable and easy for a human to approve or reject.

## Management model

The default organisation begins with a Chief of Staff agent and specialist roles for Sales, Finance, Operations, Support, Marketing, Procurement and IT/Security.

The owner can interact with the organisation through the Control Plane, chat or LiveKit voice. The Chief of Staff produces briefings, coordinates work and surfaces decisions that require human attention.

## Approval Inbox

The Control Plane should implement one queue for all governed decisions.

Each approval includes:

- requesting agent
- requested action
- rationale
- supporting evidence
- customer/supplier/project context
- monetary or risk impact
- proposed tool arguments
- triggering policy
- expiry/SLA where relevant
- approve, reject, modify and ask-agent controls

Approvals are durable workflow states, not chat messages. Temporal is the planned workflow engine for waiting and resuming safely.

## Agent identities

Agents must never share one universal business credential. Each role receives its own identity and capability grants.

This enables statements such as:

```text
14:32 agent.finance proposed payment INV-3941
14:41 business-owner approved approval/APR-884
14:42 agent.finance executed payment workflow
```

## Agent budgets

Each agent can have a monthly AI spend ceiling and workload limits. The governance engine should reject or escalate activity when a budget is exhausted.

Future reporting should compare cost with business outcomes such as leads processed, tickets resolved, quotes prepared, overdue invoices recovered and hours of human work avoided.

## Kill switch

The business owner must have a global emergency control that prevents autonomous write actions while preserving read-only visibility and the approval queue.

Additional kill switches should exist per agent and per capability.

## Agent runtime abstraction

OpenBiz should define its own agent contract. Agent implementations may use LangGraph, CrewAI or another framework, but Business Packs and tool permissions should not depend on one vendor/framework.

## Durable workflow boundary

Use Temporal for important business processes involving waits, retries, approvals, deadlines or compensation. Use n8n for integration automation and simpler event-driven flows.

Never depend on LLM conversation memory as authoritative workflow state.

## Minimum safe MVP

The AI-workforce MVP should initially allow agents to:

1. read business information;
2. prepare/draft actions;
3. submit governed actions to the Approval Inbox;
4. execute only low-risk capabilities explicitly configured as `auto` or `notify`;
5. resume approved Temporal workflows;
6. write complete audit events.

Broader autonomy can then be enabled capability by capability.
