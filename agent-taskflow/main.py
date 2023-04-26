import os
import asyncio
import pinecone
from dotenv import load_dotenv

from .config.pinecone import init_pinecone
from .agents import BabyAGIAgent

# Load default environment variables (.env)
load_dotenv()

async def main():
    # Create the BabyAGI agent
    babyagi_agent = BabyAGIAgent(memory_backend=pinecone)
    await babyagi_agent.run()

if __name__ == "__main__":
    asyncio.run(main())
