

# =====================================================
# service/report_render_html.py
# =====================================================


class HTMLReportRenderer:
@staticmethod
def render(report: dict) -> str:
html = f"<h1>Relatório Técnico – {report['metadata']['projeto']}</h1>"
html += f"<p>Data: {report['metadata']['data']}</p>"
html += f"<hr>"


for sec in report['sections']:
html += f"<h2>{sec['title']}</h2>"
html += f"<p>{sec['content']}</p>"


return html
