# tools/research.py
from tavily import TavilyClient
import httpx
from bs4 import BeautifulSoup
import asyncio

client = TavilyClient()

async def fetch_page(url: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=15) as ac:
            r = await ac.get(url, follow_redirects=True)
            soup = BeautifulSoup(r.text, "lxml")
            text = soup.get_text(separator=" ")[:15_000]
            return " ".join(text.split())
    except:
        return "Content unavailable."

async def research_agent(query: str, top_k: int = 7):
    results = client.search(query, num_results=top_k)
    urls = [r["url"] for r in results["results"]]
    contents = await asyncio.gather(*[fetch_page(u) for u in urls])

    sources = []
    for res, content in zip(results["results"], contents):
        sources.append({
            "title": res["title"],
            "url": res["url"],
            "snippet": res["content"][:600],
            "content": content
        })
    return sources