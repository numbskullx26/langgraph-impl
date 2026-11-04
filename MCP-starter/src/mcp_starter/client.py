import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()


async def main():
    mcp_client = MultiServerMCPClient(
        {
            "math": {
                "command": sys.executable,
                "args": [str(Path(__file__).with_name("mathserver.py"))],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
        },
    )

    tools = await mcp_client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-20b")

    agent = create_agent(model=model, tools=tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the (3 + 5) x 12?"}]}
    )

    print("Math Response:", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather in New York City?"}]}
    )
    print("Weather Response:", weather_response["messages"][-1].content)

asyncio.run(main())
