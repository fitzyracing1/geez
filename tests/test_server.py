import asyncio, sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

def test_server_starts_and_lists_call_grok():
    async def run():
        p = StdioServerParameters(command=sys.executable, args=["-m", "geez"], env={})
        async with stdio_client(p) as (r, w):
            async with ClientSession(r, w) as s:
                await s.initialize()
                names = [t.name for t in (await s.list_tools()).tools]
                assert names == ["call_grok"]
                res = await s.call_tool("call_grok", {"prompt": "hi"})
                assert "XAI_API_KEY" in res.content[0].text
    asyncio.run(run())
