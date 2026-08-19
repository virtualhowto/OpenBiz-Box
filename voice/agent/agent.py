import os
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import openai

SYSTEM_PROMPT = """You are OpenBiz, a concise voice assistant for a small business.
Help the authenticated user understand and operate their business. Never claim a business action completed unless a tool confirms it. Sensitive external actions require explicit confirmation through the OpenBiz Tool Gateway. Keep spoken responses brief and natural."""

async def entrypoint(ctx: JobContext):
    await ctx.connect()

    # OpenAI-compatible endpoints keep the first worker useful with LiteLLM.
    # STT/TTS are provider abstractions and will gain local adapters next.
    session = AgentSession(
        stt=openai.STT(),
        llm=openai.LLM(
            model=os.getenv("OPENBIZ_VOICE_LLM_MODEL", "gpt-4o-mini"),
            base_url=os.getenv("OPENBIZ_LITELLM_URL", "http://litellm:4000/v1"),
            api_key=os.getenv("LITELLM_MASTER_KEY", ""),
        ),
        tts=openai.TTS(),
    )

    await session.start(
        room=ctx.room,
        agent=Agent(instructions=SYSTEM_PROMPT),
    )

    await session.generate_reply(
        instructions="Greet the user as OpenBiz and ask what they would like to know or do with their business."
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
