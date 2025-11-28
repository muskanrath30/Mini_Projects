import gradio as gr
import asyncio
from main import app as langgraph_app
from utils.report import save_report
import os

os.makedirs("output", exist_ok=True)

async def run_research(query: str):
    config = {"configurable": {"thread_id": "gradio_session_123"}}
    
    result = await langgraph_app.ainvoke({
        "query": query,
        "sources": [],
        "summary": "",
        "messages": []
    }, config)
    
    summary = result["summary"]
    
    safe_title = "".join(c if c.isalnum() or c in " _-" else "_" for c in query)[:60]
    pdf_path = f"output/{safe_title}_report.pdf"
    
    save_report(query, summary)  # Uses your clean report generator
    
    return summary, pdf_path

def gradio_research(query: str):
    return asyncio.run(run_research(query))

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Multi-Agent Research Assistant
        **Professional Executive Reports in Seconds using Research & Summary Agents**
        """
    )
    
    with gr.Row():
        textbox = gr.Textbox(
            label="Your Research Question",
            placeholder="e.g., Latest AI agent frameworks in November 2025",
            lines=3
        )
        submit_btn = gr.Button("Generate Report", variant="primary")
    
    output_text = gr.Markdown(label="Executive Summary")
    pdf_output = gr.File(label="Download PDF Report")
    
    submit_btn.click(
        fn=gradio_research,
        inputs=textbox,
        outputs=[output_text, pdf_output]
    )
    
    gr.Examples(
        examples=[
            ["Latest AI agent breakthroughs November 2025"],
            ["Smartphone sales forecast 2025"],
            ["Impact of generative AI on sales teams"],
        ],
        inputs=textbox
    )


demo.launch(
    share=True,
    server_port=8000,
    theme=gr.themes.Soft(),
    css="footer {display:none !important;}"
)