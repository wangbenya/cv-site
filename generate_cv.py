"""
Generate CV PDF for Dr Benya Wang — Principal Machine Learning Engineer.
Usage: pip install reportlab && python generate_cv.py
Output: cv.pdf in the same directory.
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
MARGIN = 1.8 * cm


def build_styles():
    def S(name, **kw):
        return ParagraphStyle(name, **kw)

    return {
        'name': S('name',
            fontName='Helvetica-Bold', fontSize=24,
            textColor=NAVY, spaceAfter=2, leading=28),
        'contact': S('contact',
            fontName='Helvetica', fontSize=9,
            textColor=SUBTLE, spaceAfter=4, leading=13, alignment=TA_LEFT),
        'contact_right': S('contact_right',
            fontName='Helvetica', fontSize=9,
            textColor=SUBTLE, spaceAfter=4, leading=13, alignment=TA_RIGHT),
        'section_head': S('section_head',
            fontName='Helvetica-Bold', fontSize=9,
            textColor=ACCENT, spaceBefore=10, spaceAfter=3,
            leading=12, letterSpacing=1.2),
        'job_title': S('job_title',
            fontName='Helvetica-Bold', fontSize=10.5,
            textColor=NAVY, spaceAfter=1, leading=14),
        'company': S('company',
            fontName='Helvetica', fontSize=9.5,
            textColor=SUBTLE, spaceAfter=2, leading=13),
        'body': S('body',
            fontName='Helvetica', fontSize=10,
            textColor=BODY, spaceAfter=4, leading=14),
        'bullet': S('bullet',
            fontName='Helvetica', fontSize=10,
            textColor=BODY, spaceAfter=2, leading=14,
            leftIndent=11, firstLineIndent=-11),
        'skill_cat': S('skill_cat',
            fontName='Helvetica-Bold', fontSize=9,
            textColor=NAVY, spaceAfter=1, leading=12),
        'skill_val': S('skill_val',
            fontName='Helvetica', fontSize=9.5,
            textColor=BODY, spaceAfter=3, leading=13),
        'pub': S('pub',
            fontName='Helvetica', fontSize=9,
            textColor=BODY, spaceAfter=3, leading=13,
            leftIndent=11, firstLineIndent=-11),
    }


def hr(color=RULE, thickness=0.6):
    return HRFlowable(width='100%', thickness=thickness,
                      color=color, spaceAfter=5, spaceBefore=0)


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


def build_pdf(path='cv.pdf'):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title='Dr Benya Wang — Machine Learning Engineer',
        author='Benya Wang',
    )

    styles = build_styles()
    story  = []
    body_w = PAGE_W - 2 * MARGIN  # usable width

    # ── Header ────────────────────────────────────────────────────────────
    story.append(Paragraph('Dr Benya Wang', styles['name']))
    story.append(Paragraph(
        'email: benya.wang@hotmail.com  ·  personal website: <a href="https://wangbenya.github.io/cv-site" color="#2E6DA4">wangbenya.github.io/cv-site</a>  ·  Perth, WA',
        styles['contact']
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(hr(ACCENT, 1.0))

    # ── Career Profile ────────────────────────────────────────────────────
    story += section_title('Career Profile', styles)
    story.append(Paragraph(
        'Machine Learning Engineer with a PhD and 7+ years of experience '
        'defining technical strategy and delivering enterprise-grade AI platforms across '
        'mining and resources. Proven track record owning the full ML lifecycle — from '
        'architecture design through to production deployment and '
        'platform governance — at organisations operating at industrial scale. Deep expertise '
        'spanning MLOps, LLM / GenAI pipelines, Vision AI, and edge computing on Azure and '
        'Databricks. Consistently drives cross-functional adoption of reusable frameworks, '
        'reduces delivery risk through robust monitoring, and translates complex business '
        'problems into scalable AI solutions.',
        styles['body']
    ))

    # ── Core Competencies ─────────────────────────────────────────────────
    story += section_title('Core Competencies', styles)

    skills = [
        ('Cloud & Data Platforms',
         'Azure (AI Foundry, Azure ML, IoT Edge/Hub, AI Search, Azure OpenAI, DevOps), '
         'Databricks, AWS'),
        ('MLOps & DevOps',
         'MLflow, Azure Pipelines, Terraform, Bicep, Docker, CI/CD pipeline design'),
        ('LLMs & Generative AI',
         'Azure AI Foundry, Claude, LightRAG, GraphRAG, AutoGen, RAG pipeline design, '
         'multi-agent orchestration'),
        ('ML & Data Engineering',
         'XGBoost, LightGBM, YOLO, PySpark, Python, SQL'),
        ('Leadership & Architecture',
         'Enterprise platform strategy, reusable framework design, stakeholder engagement, '
         'data governance, technical mentoring'),
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
        'Pioneered an air-gapped edge ML deployment pattern (Azure IoT Edge, ACR, Databricks Apps) '
        'enabling model inference on isolated industrial sites with zero internet connectivity — '
        'adopted as the enterprise-wide standard across all remote operations.',
        'Architected and led delivery of a centralised Data Science platform (Azure Databricks, '
        'MLflow, Azure Pipelines) that standardised MLOps workflows across 6+ business units, '
        'cutting average model deployment cycle from ~3 weeks to under 5 days.',
        'Defined the technical strategy and built a unified AI platform (Azure AI Search, '
        'Azure OpenAI, Cosmos DB) that reduced time-to-production for new LLM applications '
        'by ~60%, enabling multiple product teams to ship independently.',
        'Led technical governance for the ML platform — authoring standards, reviewing '
        'architectures, and mentoring data scientists across business units to drive '
        'consistent, production-quality delivery.',
        'Delivered GenAI-powered document intelligence (LightRAG, Azure AI Foundry) across '
        'geoscience and safety corpora, surfacing actionable insights from previously '
        'unstructured data at enterprise scale.',
    ]:
        story.append(Paragraph(f'• {b}', styles['bullet']))
    story.append(Spacer(1, 0.15 * cm))

    # South32 — Specialist Data Scientist
    story.append(job_row(
        'Specialist Data Scientist',
        'Jan 2022 – Apr 2023',
        styles, col_w
    ))
    story.append(Paragraph('South32  ·  Perth, WA', styles['company']))
    for b in [
        'Designed CI/CD pipelines (Azure DevOps) to automate model training, validation, '
        'and deployment — reducing manual release effort by ~70% and eliminating '
        'ad-hoc deployment risk.',
        'Led advanced feature engineering and exploratory analysis at scale using PySpark '
        'and scikit-learn across large industrial datasets.',
        'Partnered with data governance teams to implement stewardship and metadata '
        'management aligned with enterprise compliance policies.',
        'Designed and deployed a Vision AI safety system (YOLO, Supervision) for automated '
        'stop-sign monitoring, directly improving operational safety compliance.',
        'Implemented production multi-agent LLM pipelines (GraphRAG, AutoGen) to extract '
        'structured insights from HR records, safety incident reports, and geoscience '
        'exploration corpora.',
    ]:
        story.append(Paragraph(f'• {b}', styles['bullet']))
    story.append(Spacer(1, 0.15 * cm))

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
    story.append(Spacer(1, 0.15 * cm))

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
        'Delivered spatial analytics dashboards (GIS maps, Plotly Dash) enabling '
        'operational teams to make data-driven decisions in real time.',
    ]:
        story.append(Paragraph(f'• {b}', styles['bullet']))
    story.append(Spacer(1, 0.15 * cm))

    # Rio Tinto — Intern
    story.append(job_row(
        'Data Science Intern',
        'Jan 2018 – Apr 2018',
        styles, col_w
    ))
    story.append(Paragraph('Rio Tinto  ·  Perth, WA', styles['company']))
    story.append(Paragraph(
        '• Contributed to early-stage predictive maintenance analytics and sensor data '
        'preprocessing pipelines.',
        styles['bullet']
    ))
    story.append(Spacer(1, 0.15 * cm))

    # ── Education ─────────────────────────────────────────────────────────
    story += section_title('Education', styles)

    story.append(job_row('PhD — Environmental Engineering', 'Feb 2015 – Feb 2019', styles, col_w))
    story.append(Paragraph('University of Western Australia', styles['company']))
    story.append(Paragraph(
        'Thesis: Application of machine learning algorithms in urban catchments. '
        '5 peer-reviewed publications in <i>Geoscientific Model Development</i>, '
        '<i>Water Resources Research</i>, and other journals (see Selected Publications).',
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
    print(f'✓  CV saved to {path}')


if __name__ == '__main__':
    build_pdf()
