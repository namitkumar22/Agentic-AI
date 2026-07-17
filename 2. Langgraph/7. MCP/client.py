from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import asyncio
from dotenv import load_dotenv
load_dotenv()

import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY, streaming=True)

async def main():
    client = MultiServerMCPClient(
        {
            "MathServer" : { # Name of the server
                "command" : "python", # Can also use uvicorn here
                "args" : ["mathserver.py"], # Correct absolute path of the file in a list
                "transport" : "stdio" # Transport we are using for this particular server
            },
            "WeatherServer" : {
                "url" : "http://localhost:8000/mcp", # URL of the server running, this is just a demo url of local server, you can see the localhost URL but its "/mcp" also after it, that is where we will find the entire MCP running
                "transport" : "streamable-http"
            }
        }
    )

    tools = await client.get_tools() # This will get all the tools present in all the servers we mentioned and create a list of them. Also "await" is used in asynchronous programming which allows the execution of other tasks while waiting for a specific task like here while its waiting for tools list the other task can be processed, and this is only allowed in a "async def" function and it works on the client side.

    
    agent = create_agent(
        model = model,
        tools = tools,
        system_prompt="Provide answers accordingly and strictly with tool calls, no need to add information from your own"
    )

    #Make sure the tools we created are served as asynchronous tools, so we have to call them asynchronously. ainvoke()is used for asynchronous calling and we use await keyword with it

    
    response = await agent.ainvoke({"messages" : [{
        "role" : "user",
        "content" : "What is weather in california. Add 2 + 2 then multiply it by 4"
    }]})

    print(response["messages"][-1].content)


asyncio.run(main())
