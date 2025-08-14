import asyncio
from fastmcp import Client, FastMCP

# HTTP server
client = Client("http://127.0.0.1:9100/mcp")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()

        print(tools)

asyncio.run(main())