import markdown2
from weasyprint import HTML
from datetime import datetime
import os
import re

os.makedirs("output", exist_ok=True)

def save_report(query: str, summary: str):
    safe_title = re.sub(r'[^\w\s-]', '_', query)[:60].strip()

    urls = re.findall(r'https?://[^\s\]\)]+', summary)

    clean_text = re.split(r'\n\s*\n?(Sources?|References?):', summary, flags=re.IGNORECASE)[0]

    lines = [line.strip() for line in clean_text.split('\n') if line.strip()]
    final_lines = []
    for line in lines:
        lower = line.lower()
        if any(phrase in lower for phrase in [
            "here is a professional", "here is an executive", "below is", "summary:"
        ]):
            continue
        final_lines.append(line)

    body = "\n\n".join(final_lines).strip()

    sources_html = ""
    if urls:
        sources_html = "<h3 style='margin-top:40px; color:#1e40af; font-size:18px;'>Sources</h3><ul style='margin-left:20px; line-height:1.8;'>"
        seen = set()
        for i, url in enumerate(urls, 1):
            if url not in seen:
                seen.add(url)
                sources_html += f"<li><a href='{url}' style='color:#2563eb; text-decoration:none;'>{url}</a></li>"
        sources_html += "</ul>"

    html = f"""
    <h1 style="text-align:center; color:#1e40af; font-size:28px; margin-bottom:10px;">
        Executive Research Report
    </h1>
    <h2 style="text-align:center; color:#1e3a8a; font-size:22px; margin-bottom:20px;">
        {query}
    </h2>
    <p style="text-align:center; color:#6b7280; font-size:14px; margin-bottom:30px;">
        <strong>Generated on:</strong> {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
    </p>
    <hr style="border:1px solid #e5e7eb; margin:30px 0;">
    <div style="font-size:16px; line-height:1.8; color:#1f2937; text-align:justify;">
        {markdown2.markdown(body)}
    </div>
    {sources_html}
    """

    pdf_path = f"output/{safe_title}_report.pdf"
    HTML(string=html).write_pdf(pdf_path)
    print(f"Perfect PDF saved → {pdf_path}")