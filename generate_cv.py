"""
Generate CV PDF for Dr Benya Wang — AI Architect (tailored: Alcoa Req-36794).
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
            textColor=BODY, spaceAfter=2.6, leading=13.4,
            leftIndent=11, firstLineIndent=-11),
        'skill_cat': S('skill_cat',
            fontName='Helvetica-Bold', fontSize=10,
            textColor=NAVY, spaceAfter=2, leading=12),
        'skill_val': S('skill_val',
            fontName='Helvetica', fontSize=10,
            textColor=BODY, spaceAfter=3.6, leading=13.4),
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
        title='Dr Benya Wang — AI Architect',
        author='Benya Wang',
    )

    styles = build_styles()
    story  = []
    body_w = PAGE_W - 2 * MARGIN  # usable width

    # ── Header ────────────────────────────────────────────────────────────
    story.append(Paragraph('Dr Benya Wang', styles['name']))
    story.append(Paragraph(
        'Email: benya.wang@hotmail.com  ·  Personal website: <a href="https://wangbenya.github.io/cv-site" color="#2E6DA4">wangbenya.github.io/cv-site</a>  ·  Perth, WA',
        styles['contact']
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(hr(ACCENT, 1.0))

    # ── Career Profile ────────────────────────────────────────────────────
    story += section_title('Career Profile', styles)
    story.append(Paragraph(
        'AI Architect with a PhD and 8 years of experience designing, governing, and scaling '
        'enterprise-grade data science and AI platforms across mining and resources. Sets enterprise '
        'AI standards, '
        'reference architectures, and roadmaps, then guides delivery teams to build against them '
        'through platform patterns, solution design review, and mentoring across business units. '
        'Deep Azure specialisation (Azure AI Foundry, Azure OpenAI, Azure ML) alongside Databricks, '
        'LLMOps and MLOps tooling, with a track record of taking Generative AI, RAG knowledge bases, '
        'and agentic systems from proof of concept to secure production. Designs AI and security '
        'governance frameworks with Cyber and Enterprise Architecture, and translates AI '
        'capability into strategic priorities for business leaders.',
        styles['body']
    ))

    # ── Core Competencies ─────────────────────────────────────────────────
    story += section_title('Core Competencies', styles)

    skills = [
        ('AI Architecture & Governance',
         'AI governance framework design, secure-by-design patterns, '
         'data architecture and governance'),
        ('Generative AI & LLMs',
         'Azure OpenAI, Azure AI Foundry, Azure AI Search, Microsoft Copilot Studio, LangChain, '
         'LightRAG, GraphRAG, '
         'Claude Code, RAG pipeline design, vector stores, multi-agent orchestration, agentic platforms'),
        ('Azure & Data Platforms',
         'Azure (ACR, IoT Edge/Hub, VNet, Azure ML), '
         'Databricks (data warehouse, workflow orchestration), AWS'),
        ('LLMOps, MLOps & DevOps',
         'MLflow, Azure DevOps / Pipelines, Terraform, Bicep, Docker, AKS, ACI (containerised '
         'microservices), model endpoint deployment, CI/CD pipeline design'),
        ('ML & Data Engineering',
         'Python, PySpark, Pandas, SQL, XGBoost, LightGBM, predictive analytics'),
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
        'Led technical governance for the ML platform including authoring standards, engineering '
        'guides, and platform patterns; reviewing architectures; and mentoring data scientists '
        'across business units to drive consistent, production-quality delivery.',
        'Defined the technical strategy and built a unified AI platform (Azure AI Search, '
        'Azure OpenAI, Cosmos DB) with self-service patterns and reference implementations that '
        'reduced time-to-production for new LLM applications by ~60%, enabling multiple product '
        'teams to ship independently.',
        'Built a safety chatbot and GenAI knowledge base over safety and geoscience corpora '
        '(Azure AI Foundry, Azure AI Search, LightRAG, Azure Web App), giving operational teams '
        'conversational access to guidance previously locked in unstructured documents.',
        'Right-sized the container runtime for model inference endpoints — ACI for lightweight, '
        'single-service workloads and AKS where orchestration and scaling were required — '
        'packaging models as Docker microservices published through ACR.',
        'Pioneered an air-gapped edge ML deployment pattern (Azure IoT Edge, Databricks Apps) '
        'enabling model inference on isolated industrial sites with zero internet connectivity; '
        'adopted as the standard across all remote operations.',
        'Partnered with Cyber and Enterprise Architecture teams to design a Microsoft Copilot '
        'Studio governance framework and a GitHub / GitHub Copilot governance framework, '
        'establishing enterprise-wide standards for AI-assisted development, access controls, '
        'and compliant deployment; supported the organisational migration from Azure DevOps '
        'to GitHub at scale.',
        'Served as Acting Data Science Lead May–Jun 2026, maintaining delivery continuity '
        'across active AI platform workstreams; co-designed the platform production support '
        'model with the Operational Digital Technology team, defining ownership, escalation '
        'paths, and SLA structures.',
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
        'Delivered advanced process control solutions for operations in Australia, Africa, and '
        'South America, working with local technology teams at each site to improve recovery '
        'and energy efficiency.',
        'Built reusable PySpark feature pipelines into a Databricks Feature Store over large-scale '
        'industrial sensor data, replacing ad-hoc notebook preparation with versioned, '
        'model-ready features.',
        'Partnered with data governance teams to implement stewardship and metadata '
        'management aligned with enterprise compliance policies.',
        'Designed and deployed a Vision AI safety system (YOLO, Supervision) for automated '
        'stop-sign monitoring, directly improving operational safety compliance.',
        'Implemented production multi-agent LLM pipelines (GraphRAG, AutoGen) to extract '
        'structured insights from HR records, safety incident reports, and geoscience '
        'exploration corpora.',
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
        'Won an internal Hackathon for diamond image classification using TensorFlow '
        'and transfer learning.',
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
