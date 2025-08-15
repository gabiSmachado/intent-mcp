# intent-mcp

## Configuration

Static parameters are centralized in `intent-mcp/config.yaml`:

- server: FastAPI metadata, logging, uvicorn and MCP host/port
- client: MCP client base URL and logging
- geocoding: Nominatim user agent

Update values there instead of hardcoding in code.

## Setup

Install dependencies:

```bash
pip install -r intent-mcp/requirements.txt
```

Run server (example):

```bash
python -m uvicorn intent-mcp.camara_api.main:app --host 127.0.0.1 --port 9100 --reload
```