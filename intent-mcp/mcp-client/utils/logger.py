import logging
import sys
from pathlib import Path
import yaml


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


cfg = _load_config()
log_cfg = (cfg.get("client") or {}).get("logging") or {}

# Configure logging
logger = logging.getLogger(log_cfg.get("name", "MCPClient"))
logger.setLevel(getattr(logging, str(log_cfg.get("level", "DEBUG")).upper(), logging.DEBUG))

# File handler
file_handler = logging.FileHandler(log_cfg.get("file", "mcp_client.log"))
file_handler.setLevel(getattr(logging, str(log_cfg.get("level", "DEBUG")).upper(), logging.DEBUG))
file_handler.setFormatter(
    logging.Formatter(log_cfg.get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
)
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(getattr(logging, str(log_cfg.get("console_level", "INFO")).upper(), logging.INFO))
console_handler.setFormatter(
    logging.Formatter(log_cfg.get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
)
logger.addHandler(console_handler)