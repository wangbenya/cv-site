"""
Generate CV PDF for Dr Benya Wang - AI & ML Engineer (tailored: Alcoa Req-37776).
Usage: pip install reportlab && python generate_cv.py
Output: Benya_Wang_CV.pdf in the same directory.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

# ── Colour palette (professional neutral) ──────────────────────────────────
NAVY    = colors.HexColor('#1B2B4B')   # name, job titles
ACCENT  = colors.HexColor('#2E6DA4')   # section headers, top rule
BODY    = colors.HexColor('#444444')   # body text
SUBTLE  = colors.HexColor('#666666')   # company, dates, contact
RULE    = colors.HexColor('#CCCCCC')   # horizontal rules

PAGE_W, PAGE_H = A4
MARGIN = 1.4 * cm


def build_styles():
    def S(name, **kw):
        return ParagraphStyle(name, **kw)

    return {
        'name': S('name',
            fontName='Helvetica-Bold', fontSize=24,
            textColor=NAVY, spaceAfter=2, leading=28),
        'subtitle': S('subtitle',
            fontName='Helvetica', fontSize=12,
            textColor=ACCENT, spaceBefore=1, spaceAfter=4, leading=14),
        'contact': S('contact',
            fontName='Helvetica', fontSize=10,
            textColor=SUBTLE, spaceAfter=3, leading=13, alignment=TA_LEFT),
        'contact_right': S('contact_right',
            fontName='Helvetica', fontSize=10,
            textColor=SUBTLE, spaceAfter=3, leading=13, alignment=TA_RIGHT),
        'section_head': S('section_head',
            fontName='Helvetica-Bold', fontSize=10,
            textColor=ACCENT, spaceBefore=11, spaceAfter=3,
            leading=12, letterSpacing=1.2),
        'job_title': S('job_title',
            fontName='Helvetica-Bold', fontSize=10.5,
            textColor=NAVY, spaceAfter=2, leading=13),
        'company': S('company',
            fontName='Helvetica', fontSize=10,
            textColor=SUBTLE, spaceAfter=4, leading=12),
        'body': S('body',
            fontName='Helvetica', fontSize=10,
            textColor=BODY, spaceAfter=3, leading=13.4),
        'bullet': S('bullet',
            fontName='Helvetica', fontSize=10,
            textColor=BODY, spaceAfter=2.0, leading=13.4,
            leftIndent=11, firstLineIndent=-11),
        'skill_cat': S('skill_cat',
            fontName='Helvetica-Bold', fontSize=10,
            textColor=NAVY, spaceAfter=2, leading=12),
        'skill_val': S('skill_val',
            fontName='Helvetica', fontSize=10,
            textColor=BODY, spaceAfter=3.0, leading=13.4),
        'pub': S('pub',
            fontName='Helvetica', fontSize=10,
            textColor=BODY, spaceAfter=3, leading=13,
            leftIndent=11, firstLineIndent=-11),
    }


def hr(color=RULE, thickness=0.6):
    return HRFlowable(width='100%', thickness=thickness,
                      color=color, spaceAfter=4, spaceBefore=0)


def section_title(text, styles):
    return [
        Paragraph(text.upper(), styles['section_head']),
        hr(),
    ]


def job_row(title, company_period, styles, col_widths):
    """Returns a Table row with job title left and period right."""
    title_p  = Paragraph(title, styles['job_title'])
    period_p = Paragraph(company_period, styles['contact_right'])
    t = Table([[title_p, period_p]], colWidths=col_widths)
    t.setStyle(TableStyle([
        ('VALIGN',  (0, 0), (-1, -1), 'TOP'),
        ('ALIGN',   (1, 0), (1,  0),  'RIGHT'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
    ]))
    return t


def build_pdf(path='Benya_Wang_CV.pdf'):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title='Dr Benya Wang - AI & ML Engineer',
        author='Benya Wang',
    )

    styles = build_styles()
    story  = []
    body_w = PAGE_W - 2 * MARGIN  # usable width

    # ── Header ────────────────────────────────────────────────────────────
    story.append(Paragraph('Dr Benya Wang', styles['name']))
    story.append(Paragraph('AI &amp; ML Engineer  ·  PhD', styles['subtitle']))
    story.append(Paragraph(
        'Email: benya.wang@hotmail.com  ·  Personal website: <a href="https://wangbenya.github.io/cv-site" color="#2E6DA4">wangbenya.github.io/cv-site</a>  ·  Perth, WA',
        styles['contact']
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(hr(ACCENT, 1.0))

    # ── Career Profile ────────────────────────────────────────────────────
    story += section_title('Career Profile', styles)
    story.append(Paragraph(
        'AI and ML engineer with a PhD and 8 years taking AI from prototype to production '
        'across mining and resources. Strongest on the deployment half: model endpoints, '
        'containerised microservices, edge inference on disconnected sites, CI/CD, and the '
        'MLOps tooling that keeps models running. Delivers Generative AI at enterprise scale '
        'through RAG knowledge bases and agentic workflows on Azure (AI Foundry, Azure OpenAI, '
        'AI Search, Azure ML) with Databricks and MLflow. Sets the standards, reference '
        'architectures, and platform patterns that let delivery teams build the same way, and '
        'designs responsible AI governance with Cyber and Enterprise Architecture. Works with '
        'complex operational data (time-series, sensor, historian) across Australia, Africa, '
        'and South America.',
        styles['body']
    ))

    # ── Core Competencies ─────────────────────────────────────────────────
    story += section_title('Core Competencies', styles)

    skills = [
        ('MLOps, Deployment & Responsible AI',
         'Model endpoint deployment, AKS / ACI, Docker microservices, ACR, MLflow, '
         'Azure DevOps / Pipelines, CI/CD design, edge inference (Azure IoT Edge), '
         'documented AI workflows, AI governance frameworks'),
        ('Generative AI & Agentic Systems',
         'RAG pipeline design, agentic and multi-agent workflows, Azure OpenAI, Azure AI Foundry, '
         'Azure AI Search, LangChain, LightRAG, GraphRAG, AutoGen, vector stores, '
         'Microsoft Copilot Studio, Claude Code'),
        ('Azure & Data Platforms',
         'Azure (AI Foundry, Azure ML, AI Search, IoT Edge/Hub, ACR), '
         'Databricks (Feature Store, workflow orchestration, data warehouse), AWS'),
        ('Machine Learning & Modelling',
         'Predictive analytics, time-series and sensor data modelling, feature engineering, '
         'XGBoost, LightGBM, Random Forest, computer vision (YOLO), advanced process control'),
        ('Engineering & Delivery',
         'Python, PySpark, Pandas, SQL, stakeholder engagement, technical mentoring, '
         'cross-site delivery across multiple time zones'),
    ]
    for cat, val in skills:
        story.append(Paragraph(cat, styles['skill_cat']))
        story.append(Paragraph(val, styles['skill_val']))

    # ── Experience ────────────────────────────────────────────────────────
    story += section_title('Professional Experience', styles)

    col_w = [body_w * 0.68, body_w * 0.32]

    # South32 — Specialist ML Engineer
    story.append(job_row(
        'Specialist Machine Learning Engineer',
        'Apr 2023 – Present',
        styles, col_w
    ))
    story.append(Paragraph('South32  ·  Perth, WA', styles['company']))
    for b in [
        'Designed and implemented end to end an air-gapped edge ML deployment pattern '
        '(Azure IoT Edge, Databricks Apps), enabling model inference on isolated industrial '
        'sites with zero internet connectivity; adopted as the standard across all remote '
        'operations.',
        'Built a safety chatbot and GenAI knowledge base over safety and geoscience corpora '
        '(Azure AI Foundry, Azure AI Search, LightRAG), covering corpus exploration, chunking '
        'strategy, retrieval tuning, and production deployment, giving operational teams '
        'conversational access to guidance locked in unstructured documents.',
        'Owned model deployment and optimisation, right-sizing the container runtime for '
        'inference endpoints: ACI for lightweight, single-service workloads and AKS where '
        'orchestration and scaling were required, packaging models as Docker microservices '
        'published through ACR.',
        'Applied responsible AI in practice: partnered with Cyber and Enterprise Architecture '
        'to design a Microsoft Copilot Studio governance framework and a GitHub / GitHub Copilot '
        'governance framework, establishing enterprise-wide standards for AI-assisted '
        'development, access controls, and compliant deployment.',
        'Defined the technical strategy and built a unified AI platform (Azure AI Search, '
        'Azure OpenAI, Cosmos DB) with self-service patterns and reference implementations that '
        'reduced time-to-production for new LLM applications by ~60%, enabling multiple product '
        'teams to ship independently.',
        'Authored the standards, engineering guides, and platform patterns that made AI delivery '
        'repeatable and well documented across the business, and mentored data scientists across '
        'business units to drive consistent, production-quality outcomes.',
        'Served as Acting Data Science Lead May–Jun 2026, maintaining delivery continuity '
        'across active AI workstreams; co-designed the production support model with the '
        'Operational Digital Technology team, defining ownership, escalation paths, and '
        'SLA structures.',
    ]:
        story.append(Paragraph(f'• {b}', styles['bullet']))
    story.append(Spacer(1, 0.14 * cm))

    # South32 — Specialist Data Scientist
    story.append(job_row(
        'Specialist Data Scientist',
        'Jan 2022 – Apr 2023',
        styles, col_w
    ))
    story.append(Paragraph('South32  ·  Perth, WA', styles['company']))
    for b in [
        'Architected and led delivery of a centralised Data Science platform (Azure Databricks, '
        'MLflow, Azure Pipelines) that standardised MLOps workflows across 6+ business units, '
        'cutting the average model deployment cycle from ~3 weeks to under 5 days and eliminating '
        'ad-hoc deployment risk.',
        'Delivered advanced process control solutions over plant time-series and sensor data for '
        'operations in Australia, Africa, and South America, working with local technology teams '
        'in each region to improve recovery and energy efficiency, coordinating delivery across '
        'multiple time zones.',
        'Built reusable PySpark feature pipelines into a Databricks Feature Store over large-scale '
        'industrial sensor and historian data, replacing ad-hoc notebook preparation with '
        'versioned, model-ready features.',
        'Implemented production multi-agent LLM pipelines (GraphRAG, AutoGen) to extract '
        'structured insights from HR records, safety incident reports, and geoscience '
        'exploration corpora.',
        'Designed and deployed a Vision AI safety system (YOLO, Supervision) for automated '
        'stop-sign monitoring, directly improving operational safety compliance.',
    ]:
        story.append(Paragraph(f'• {b}', styles['bullet']))
    story.append(Spacer(1, 0.14 * cm))

    # Rio Tinto — Data Scientist
    story.append(job_row(
        'Data Scientist',
        'Jan 2021 – Jan 2022',
        styles, col_w
    ))
    story.append(Paragraph('Rio Tinto  ·  Perth, WA', styles['company']))
    for b in [
        'Engineered serverless data pipelines (AWS Lambda, Glue, Athena) for real-time '
        'production analytics supporting operational decision-making.',
        'Led ML-driven optimisation of ore blending strategies, improving resource '
        'utilisation and reducing annual operational costs.',
    ]:
        story.append(Paragraph(f'• {b}', styles['bullet']))
    story.append(Spacer(1, 0.14 * cm))

    # Rio Tinto — Graduate Data Scientist
    story.append(job_row(
        'Graduate Data Scientist',
        'Feb 2019 – Jan 2021',
        styles, col_w
    ))
    story.append(Paragraph('Rio Tinto  ·  Perth, WA', styles['company']))
    for b in [
        'Developed predictive maintenance models (LightGBM, Random Forest) for a '
        '1,700 km rail network, reducing unplanned downtime through early fault detection.',
        'Containerised models in Docker and deployed via AWS SageMaker, establishing '
        'repeatable deployment and rollback processes for the team.',
    ]:
        story.append(Paragraph(f'• {b}', styles['bullet']))
    story.append(Spacer(1, 0.14 * cm))

    # ── Education ─────────────────────────────────────────────────────────
    story += section_title('Education', styles)

    story.append(job_row('PhD in Environmental Engineering', 'Feb 2015 – Feb 2019', styles, col_w))
    story.append(Paragraph('University of Western Australia', styles['company']))
    story.append(Paragraph(
        'Thesis: Application of machine learning algorithms in urban catchments. '
        'Five peer-reviewed publications in <i>Geoscientific Model Development</i>, '
        '<i>Water Resources Research</i>, and other journals.',
        styles['body']
    ))

    story.append(job_row('Bachelor of Science', 'Sep 2010 – Jun 2014', styles, col_w))
    story.append(Paragraph('Zhejiang University, China', styles['company']))

    # ── Certifications ────────────────────────────────────────────────────
    story += section_title('Certifications', styles)

    cert_data = [
        ('Databricks Certified',
         'Machine Learning Professional  ·  Machine Learning Associate  ·  Data Engineer Associate'),
        ('Microsoft Certified',
         'DevOps Engineer Expert  ·  Azure Data Scientist Associate  ·  '
         'Azure Data Engineer Associate  ·  Azure Developer Associate'),
        ('AWS Certified',
         'Machine Learning – Specialty  ·  Solutions Architect – Associate'),
        ('Other',
         'HashiCorp Certified: Terraform Associate  ·  Anthropic: Claude Code in Action'),
    ]
    for cat, val in cert_data:
        story.append(Paragraph(cat, styles['skill_cat']))
        story.append(Paragraph(val, styles['skill_val']))


    doc.build(story)
    print(f'CV saved to {path}')


if __name__ == '__main__':
    build_pdf()
