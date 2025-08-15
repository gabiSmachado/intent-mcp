import asyncio
from pathlib import Path
import yaml
from fastmcp import Client, FastMCP


def _load_config():
    cfg = {}
    try:
        here = Path(__file__).resolve()
        for p in [here.parent, here.parent.parent, here.parent.parent.parent]:
            if (p / "config.yaml").exists():
                with (p / "config.yaml").open("r", encoding="utf-8") as f:
                    cfg = yaml.safe_load(f) or {}
                break
    except Exception:
        cfg = {}
    return cfg

CONFIG = _load_config()

base_url = ((CONFIG.get("client") or {}).get("base_url")) or "http://127.0.0.1:9100/mcp"
client = Client(base_url)

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()

        print(tools)

asyncio.run(main())