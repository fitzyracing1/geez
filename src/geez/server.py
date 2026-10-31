"""Minimal MCP server that only exposes call_grok."""

from __future__ import annotations

from typing import Any

try:  # mcp 2.x
    from mcp.server.mcpserver import MCPServer as FastMCP
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP

from . import grok as grok_tools


def build_server() -> FastMCP:
    mcp = FastMCP("geez")

    @mcp.tool()
    def call_grok(
        prompt: str,
        system: str | None = None,
        model: str = "grok-3",
        max_tokens: int = 1024,
        temperature: float = 0.7,
    ) -> dict[str, Any]:
        """Call Grok (xAI) from Claude or any MCP client.

        Phone-first: uses only requests. Set XAI_API_KEY (or GROK_API_KEY)
        in the environment before starting the server.
        """
        return grok_tools.call_grok(
            prompt,
            system=system,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
        )

    return mcp
