# =====================================================
# service/report_render_pdf.py
# =====================================================


from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class PDFReportRenderer:
@staticmethod
def render(report: dict, filename: str):
doc = SimpleDocTemplate(filename, pagesize=A4)
styles = getSampleStyleSheet()
story = []


story.append(Paragraph(f"<b>Relatório Técnico – {report['metadata']['projeto']}</b>", styles['Title']))
story.append(Paragraph(f"Data: {report['metadata']['data']}", styles['Normal']))


for sec in report['sections']:
story.append(Paragraph(f"<b>{sec['title']}</b>", styles['Heading2']))
story.append(Paragraph(sec['content'], styles['Normal']))


doc.build(story)
