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
