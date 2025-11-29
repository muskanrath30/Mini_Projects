Goal:  Multi-Agent Research Assistant
Build two agents: a research agent and a summary agent

○      Research agent queries the web given a user request

○      Summary agent converts findings into executive summary

LangGraph used to orchestrate two agents with shared memory & persistent state (true multi-agent collaboration)
Tavily for real-time web search with clean, citation-ready results
Groq for fast inference using meta-llama/llama-4-maverick-17b-128e-instruct for high-quality executive summaries
ReportLab for beautiful, clean PDFs
Gradio for instant web UI with live demo + PDF download
MemorySaver / SQLite helps agents remember past context across runs

Run the following commands to check demo make your own changes (don't forget to add your own API keys!):
 
git clone https://github.com/muskanrath30/Mini_Projects.git

pip install -r requirements.txt

python app.py

Please check the output in output folder
output/<report-name># Mini_Projects

You will find several projects in the open source but the below table shows how my project is different from their projects:

## Comparison with Existing Projects

| Repository / Source                          | Key Features & Comparison                                                                 | How My Project is Different                                                                                                                                                           |
|----------------------------------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [wassupjay/Research-Agent](https://github.com/wassupjay/Research-Agent) | LangGraph + Tavily + Groq, generates reports with citations                               | My project adds **PDF export (ReportLab)**, **Gradio web UI**, **source deduplication**, and **clean executive formatting** |
| [botextractai/ai-langgraph-multi-agent](https://github.com/botextractai/ai-langgraph-multi-agent) | 5-agent workflow with Tavily + OpenAI → easy swap to Groq                                 | Uses **Groq by default**, **2-agent simple flow**, **Gradio UI**, **downloadable PDF**, removes LLM junk text ("Here is a professional summary...") |
| [yasaminfn/LangGraph-RAG-Agent](https://github.com/yasaminfn/LangGraph-RAG-Agent) | Tavily + Groq + PDF handling + Streamlit UI                                               | Pure **web research** (no OCR), **Gradio instead of Streamlit**, **MemorySaver** (no PGVector), **clean bullet sources** |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) (LangGraph example) | Deep research + Tavily + 5–6 page reports (PDF/MD/Docx)                                    | **Groq instead of GPT**, **2-agent streamlined**, **Gradio live demo**, **clean 1-page executive PDF** |
| [tarun7r/deep-research-agent](https://github.com/tarun7r/deep-research-agent) | 4-agent system + credibility scoring                                                    | Uses **Tavily**, **Groq**, **simple 2-agent**, **PDF + source deduplication**, no Ollama/Gemini |
| [Fastpacer/Langgraph_Agent_App](https://github.com/Fastpacer/Langgraph_Agent_App) | Groq + Tavily + Streamlit UI                                                              | **Multi-agent handoff**, **Gradio**, **PDF download**, **clean sources** |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | LangGraph deep research + Tavily + report model                                           | **Groq + ReportLab PDF**, **Gradio UI**, **source cleaning**, **no OpenAI** |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | LangGraph tutorials with Tavily + Groq examples                                          | The given repository is a tutorial repo, with multiple Agentic AI projects. My repo is a **complete working app** for one project, includes **Gradio**, **PDF**, **source deduplication** |

**My project stands out with:**
- Professional **PDF executive reports** (clean, no junk text)
- **Gradio web interface** with public shareable link
- **Source deduplication & cleaning** (removes duplicate URLs and "Here is a summary...")
- **MemorySaver** for reliable memory (avoids SqliteSaver bugs)
- Full compatibility with **Python 3.13 + Windows**
