"""
Generate a placeholder CV PDF for a Machine Learning Engineer.
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
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# ── Colour palette (matches website sunset theme) ──────────────────────────
CORAL   = colors.HexColor('#FF6B35')
AMBER   = colors.HexColor('#FFB347')
DARK    = colors.HexColor('#2D1B00')
MID     = colors.HexColor('#6B4226')
SOFT    = colors.HexColor('#9E7050')
BG_ALT  = colors.HexColor('#FFF3E8')
WHITE   = colors.white

PAGE_W, PAGE_H = A4
MARGIN = 2 * cm


def build_styles():
    base = getSampleStyleSheet()

    def S(name, **kw):
        return ParagraphStyle(name, **kw)

    return {
        'name': S('name',
            fontName='Helvetica-Bold', fontSize=26,
            textColor=DARK, spaceAfter=2, leading=30),
        'tagline': S('tagline',
            fontName='Helvetica', fontSize=11,
            textColor=CORAL, spaceAfter=10, leading=16),
        'contact': S('contact',
            fontName='Helvetica', fontSize=9,
            textColor=MID, spaceAfter=4, leading=13, alignment=TA_LEFT),
        'section_head': S('section_head',
            fontName='Helvetica-Bold', fontSize=9,
            textColor=CORAL, spaceBefore=14, spaceAfter=4,
            leading=12, letterSpacing=1.5),
        'job_title': S('job_title',
            fontName='Helvetica-Bold', fontSize=11,
            textColor=DARK, spaceAfter=1, leading=15),
        'company': S('company',
            fontName='Helvetica', fontSize=10,
            textColor=MID, spaceAfter=2, leading=14),
        'body': S('body',
            fontName='Helvetica', fontSize=9.5,
            textColor=MID, spaceAfter=4, leading=15),
        'bullet': S('bullet',
            fontName='Helvetica', fontSize=9.5,
            textColor=MID, spaceAfter=3, leading=15,
            leftIndent=12, firstLineIndent=-12),
        'skill_cat': S('skill_cat',
            fontName='Helvetica-Bold', fontSize=9,
            textColor=DARK, spaceAfter=1, leading=13),
        'skill_val': S('skill_val',
            fontName='Helvetica', fontSize=9,
            textColor=MID, spaceAfter=4, leading=13),
    }


def hr(color=CORAL, thickness=0.8, opacity=0.4):
    return HRFlowable(width='100%', thickness=thickness,
                      color=color, spaceAfter=6, spaceBefore=0)


def section_title(text, styles):
    return [
        Paragraph(text.upper(), styles['section_head']),
        hr(CORAL, 0.6, 0.5),
    ]


def build_pdf(path='cv.pdf'):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title='Alex Chen — ML Engineer CV',
        author='Alex Chen',
    )

    styles = build_styles()
    story  = []

    # ── Header ────────────────────────────────────────────────────────────
    story.append(Paragraph('Alex Chen', styles['name']))
    story.append(Paragraph('Senior Machine Learning Engineer', styles['tagline']))

    contact_line = (
        'alex@example.com  ·  github.com/alexchen  ·  linkedin.com/in/alexchen  ·  Edinburgh, UK'
    )
    story.append(Paragraph(contact_line, styles['contact']))
    story.append(Spacer(1, 0.3 * cm))
    story.append(hr(CORAL, 1.2))

    # ── Summary ────────────────────────────────────────────────────────────
    story += section_title('Summary', styles)
    story.append(Paragraph(
        'Machine learning engineer with 6+ years of experience turning research ideas '
        'into production systems. Specialised in NLP, recommender systems, and MLOps. '
        'Passionate about the full ML lifecycle — from exploratory data analysis through '
        'model training to reliable, monitored deployment at scale.',
        styles['body']
    ))

    # ── Skills ─────────────────────────────────────────────────────────────
    story += section_title('Skills', styles)

    skill_data = [
        ('Languages',        'Python, SQL, R, Bash'),
        ('ML / DL',          'PyTorch, TensorFlow, scikit-learn, HuggingFace Transformers, XGBoost, LightGBM'),
        ('MLOps & Cloud',    'MLflow, Kubeflow, Docker, Kubernetes, GCP (Vertex AI, BigQuery), AWS SageMaker'),
        ('Data & Infra',     'Apache Spark, Airflow, dbt, Kafka, PostgreSQL'),
    ]

    for cat, val in skill_data:
        story.append(Paragraph(cat, styles['skill_cat']))
        story.append(Paragraph(val, styles['skill_val']))

    # ── Experience ─────────────────────────────────────────────────────────
    story += section_title('Experience', styles)

    jobs = [
        {
            'title':   'Senior Machine Learning Engineer',
            'company': 'Luminary AI — Edinburgh, UK',
            'period':  '2022 – Present',
            'bullets': [
                'Led design and deployment of a real-time personalisation engine (8M+ users), '
                'increasing engagement by 34% and reducing churn by 18%.',
                'Built an automated model-monitoring framework (data drift + performance) that '
                'caught three silent regressions before production release.',
                'Mentored three junior engineers; introduced weekly ML reading-group sessions.',
            ],
        },
        {
            'title':   'Machine Learning Engineer',
            'company': 'DataForge Inc. — London, UK',
            'period':  '2020 – 2022',
            'bullets': [
                'Developed an NLP contract-analysis pipeline using fine-tuned BERT, reducing '
                'manual legal-review time by 60%.',
                'Architected end-to-end MLOps platform on GCP (Vertex AI + MLflow) adopted '
                'across three product teams.',
                'Collaborated with legal, product, and engineering stakeholders to translate '
                'business requirements into model objectives.',
            ],
        },
        {
            'title':   'Data Science Intern',
            'company': 'FinEdge Analytics — Remote',
            'period':  '2019 (6 months)',
            'bullets': [
                'Built credit-risk scoring models (LightGBM) improving AUC from 0.78 to 0.86.',
                'Automated feature-engineering pipeline cutting data prep time by 40%.',
            ],
        },
    ]

    for job in jobs:
        # Title + period row
        title_para  = Paragraph(job['title'],   styles['job_title'])
        period_para = Paragraph(job['period'],   styles['contact'])
        t = Table([[title_para, period_para]], colWidths=[12 * cm, None])
        t.setStyle(TableStyle([
            ('VALIGN',  (0,0), (-1,-1), 'TOP'),
            ('ALIGN',   (1,0), (1,0),   'RIGHT'),
        ]))
        story.append(t)
        story.append(Paragraph(job['company'], styles['company']))
        for b in job['bullets']:
            story.append(Paragraph(f'• {b}', styles['bullet']))
        story.append(Spacer(1, 0.2 * cm))

    # ── Education ──────────────────────────────────────────────────────────
    story += section_title('Education', styles)

    story.append(Paragraph('MSc Artificial Intelligence — Distinction', styles['job_title']))
    story.append(Paragraph('University of Edinburgh  |  2018 – 2020', styles['company']))
    story.append(Paragraph(
        'Thesis: "Graph Neural Networks for Molecular Property Prediction". '
        'Co-authored paper published at NeurIPS 2020.',
        styles['body']
    ))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph('BSc Mathematics — First Class Honours', styles['job_title']))
    story.append(Paragraph('University of Bristol  |  2015 – 2018', styles['company']))

    # ── Projects ───────────────────────────────────────────────────────────
    story += section_title('Selected Projects', styles)

    projects = [
        ('SentimentStream',
         'Streaming sentiment analysis system (50k posts/min) using fine-tuned DistilBERT, '
         'FastAPI, and Kafka. Open-source on GitHub.'),
        ('ForecastKit',
         'Open-source time-series forecasting library with auto model selection and '
         'cross-validation. 1.2k GitHub stars.'),
        ('ML Monitoring Dashboard',
         'Lightweight Grafana dashboard for data-drift detection and model performance '
         'tracking in production.'),
    ]

    for title, desc in projects:
        story.append(Paragraph(title, styles['skill_cat']))
        story.append(Paragraph(desc,  styles['skill_val']))

    doc.build(story)
    print(f'✓  CV saved to {path}')


if __name__ == '__main__':
    build_pdf()
