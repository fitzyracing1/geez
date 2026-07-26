"""Entry point for the geez MCP server."""

from __future__ import annotations

import logging
import sys

from .server import build_server


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )
    mcp = build_server()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
