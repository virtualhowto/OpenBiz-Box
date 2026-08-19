# OpenBiz Voice Agent

This worker will connect LiveKit Agents to the OpenBiz AI and Tool Gateway.

## MVP flow

`Web microphone → LiveKit → Agent → STT → LLM → OpenBiz tools → TTS → LiveKit`

The worker must propagate authenticated OpenBiz identity to tool calls. Write/privileged actions are subject to Tool Gateway policy and explicit confirmation where required.

## Provider targets

- STT: faster-whisper/local first; cloud adapters optional
- LLM: LiteLLM gateway
- TTS: Kokoro/Piper local first; cloud adapters optional
- Transport: LiveKit WebRTC
- Telephony: LiveKit SIP in a later milestone

This directory is intentionally scaffolded before provider-specific implementation so the security/tool contract is established first.
