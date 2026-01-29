# =====================================================
# service/report_builder.py
# =====================================================


from datetime import datetime


class ReportBuilder:
"""
Constrói relatório técnico estruturado
independente do formato final (PDF/HTML)
"""


def __init__(self, project_name: str):
self.project_name = project_name
self.sections = []
self.metadata = {
"projeto": project_name,
"data": datetime.now().strftime("%d/%m/%Y"),
"responsavel": "Eng. Civil"
}


def add_section(self, title: str, content: str):
self.sections.append({
"title": title,
"content": content
})


def build(self):
return {
"metadata": self.metadata,
"sections": self.sections
}
