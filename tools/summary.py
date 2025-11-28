from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def summary_agent(query: str, sources: list):
    if not sources:
        return "No reliable sources found."

    source_text = "\n\n".join(
        f"[{i+1}] {s['title']}\n{s['snippet']}\nURL: {s['url']}"
        for i, s in enumerate(sources)
    )

    prompt = f"""
You are an expert executive research assistant.
Write a professional executive summary (400–600 words) answering:

{query}

Use ONLY these sources to construct your answer, citing them appropriately with URLs alongside.
When you write a report don't start with words like "Here is a professional..." or "Below is an executive summary..." or 
"In Conclusion,", "Concluding the discussion", "Overall", "Overally", "So to sum up" just get straight to the point
and summarize the findings from the sources.
Sources:
{source_text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=1800
    )

    text = response.choices[0].message.content
    citations = "\n\nSources:\n" + "\n".join(
        f"[{i+1}] {s['url']}" for i, s in enumerate(sources)
    )
    return text