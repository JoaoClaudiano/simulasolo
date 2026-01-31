# =====================================================
# service/report_builder.py
# =====================================================

"""
Constrói relatório técnico estruturado
independente do formato final (PDF/HTML)
"""
from datetime import datetime


class ReportBuilder:

    def __init__(self, project_name):
        self.project_name = project_name
        self.sections = []

    def add_section(self, title, content):
        self.sections.append({
            "title": title,
            "content": content
        })

    def build(self):
        return {
            "project": self.project_name,
            "sections": self.sections
        }
