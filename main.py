import asyncio
import sys
from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Annotated
import operator
from tools.research import research_agent
from tools.summary import summary_agent
from utils.report import save_report
from rich.console import Console
from rich.panel import Panel

console = Console()

from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()
console.print("[bold green]MemorySaver loaded — State persists across agents in-run[/bold green]")

class AgentState(TypedDict):
    query: str
    sources: List[dict]
    summary: str
    messages: Annotated[List[str], operator.add]

async def research_node(state: AgentState):
    console.print(Panel("[bold blue]Research Agent → Searching the web...[/bold blue]", style="blue"))
    sources = await research_agent(state["query"])
    return {"sources": sources, "messages": [f"Found {len(sources)} high-quality sources"]}

async def summary_node(state: AgentState):
    console.print(Panel("[bold green]Summary Agent → Writing executive report...[/bold green]", style="green"))
    summary = await summary_agent(state["query"], state["sources"])
    save_report(state["query"], summary)
    return {"summary": summary, "messages": ["Executive report generated → saved as PDF"]}

# Build workflow
workflow = StateGraph(AgentState)
workflow.add_node("research", research_node)
workflow.add_node("summary", summary_node)
workflow.add_edge(START, "research")
workflow.add_edge("research", "summary")
workflow.add_edge("summary", END)

app = workflow.compile(checkpointer=memory)  # No context manager needed

async def run():
    console.print(Panel(
        "[bold magenta]Multi-Agent Research Assistant[/bold magenta]\n"
        "LangGraph • In-Run Memory • Real Web Search • PDF Reports",
        style="magenta"
    ))
    
    query = input("\nAsk your research question → ").strip()
    if not query:
        query = "Latest AI agent frameworks in November 2025"

    config = {"configurable": {"thread_id": "research_session_2025"}}

    result = await app.ainvoke({
        "query": query,
        "sources": [],
        "summary": "",
        "messages": []
    }, config)

    console.print(Panel(f"[bold cyan]EXECUTIVE SUMMARY[/bold cyan]\n\n{result['summary']}", style="cyan"))
    console.print("[bold green]Full report saved → output/report.pdf[/bold green]")

if __name__ == "__main__":
    if "ipykernel" in sys.modules or sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run())