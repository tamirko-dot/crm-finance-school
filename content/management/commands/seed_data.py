from django.core.management.base import BaseCommand

from content.models import (
    Domain, Course, CoursePhase, Module, ModuleComponent, ComponentType,
    Question, QuestionOption, QuestionExplanation, QuestionType, QuestionDifficulty, QuestionUsage,
)


COURSES = [
    # (number, slug, title_he, phase, passing_score_pct, is_capstone)
    (1,  "c01-re-finance-basics",     "יסודות מימון נדל\"ן",          "A", 75, False),
    (2,  "c02-market-analysis",       "ניתוח שוק נדל\"ן",              "A", 75, False),
    (3,  "c03-property-valuation",    "הערכת שווי נכסים",              "B", 75, False),
    (4,  "c04-financial-metrics",     "מדדים פיננסיים בנדל\"ן",       "B", 75, False),
    (5,  "c05-cash-flow-analysis",    "ניתוח תזרים מזומנים",           "B", 80, False),
    (6,  "c06-deal-structure",        "מבנה עסקאות מימון",             "C", 75, False),
    (7,  "c07-risk-management",       "ניהול סיכונים בנדל\"ן",         "C", 75, False),
    (8,  "c08-legal-documents",       "ניתוח מסמכים משפטיים",          "C", 80, False),
    (9,  "c09-advanced-models",       "מודלים פיננסיים מתקדמים",       "D", 80, False),
    (10, "c10-risk-scenarios",        "ניתוח תרחישי סיכון",            "D", 80, False),
    (11, "c11-credit-memo",           "כתיבת מזכר אשראי",              "E", 80, False),
    (12, "c12-capstone",              "פרויקט גמר — מימון נדל\"ן",    "E", 80, True),
]

SAMPLE_READING = """
<h2>LTV ו-DSCR — מדדי הלב של ניתוח אשראי נדל"ן</h2>

<p>שני המדדים הפיננסיים החשובים ביותר בניתוח עסקאות מימון נדל"ן הם <strong>LTV (Loan-to-Value)</strong> ו-<strong>DSCR (Debt Service Coverage Ratio)</strong>. הבנה מעמיקה של שני מדדים אלה היא תנאי בסיסי לכל אנליסט אשראי.</p>

<div class="callout-rule">
  <strong>הגדרה — LTV:</strong><br>
  LTV = סכום ההלוואה ÷ שווי הנכס × 100<br>
  מדד ה-LTV מבטא את רמת המינוף של העסקה. ככל שה-LTV גבוה יותר, הסיכון למלווה גדול יותר.
</div>

<div class="callout-example">
  <strong>דוגמה:</strong><br>
  נכס מסחרי בשווי 10,000,000 ש"ח. מבקשים הלוואה של 7,000,000 ש"ח.<br>
  LTV = 7,000,000 ÷ 10,000,000 = 70%<br>
  מדיניות מוסד המימון: LTV מקסימלי 75%. העסקה עומדת בקריטריון.
</div>

<div class="callout-rule">
  <strong>הגדרה — DSCR:</strong><br>
  DSCR = הכנסה תפעולית נטו (NOI) ÷ שירות חוב שנתי<br>
  מדד ה-DSCR בוחן האם תזרים המזומנים מהנכס מספיק לכסות את תשלומי החוב. DSCR מינימלי מקובל: 1.20.
</div>

<div class="callout-warning">
  <strong>שים לב:</strong> DSCR מתחת ל-1.00 פירושו שהנכס אינו מייצר מספיק הכנסה לכיסוי שירות החוב — הלווה חייב להשלים ממקורות אחרים. ועדת האשראי תתקשה לאשר עסקה כזו ללא בטחונות נוספים משמעותיים.
</div>

<h3>חישוב NOI</h3>
<p>הכנסה תפעולית נטו (NOI) מחושבת כך:</p>
<pre>NOI = הכנסות שכירות ברוטו
    − שיעור פנויות (Vacancy)
    − הוצאות תפעוליות (ביטוח, ועד בית, תחזוקה, ניהול)</pre>
<p>חשוב: <strong>שירות חוב אינו נכלל בחישוב NOI</strong>. ה-DSCR משווה את ה-NOI לשירות החוב בנפרד.</p>
"""

SAMPLE_QUESTIONS = [
    {
        "external_id": "C01-M04-Q01",
        "qtype": QuestionType.RETRIEVAL,
        "difficulty": QuestionDifficulty.BASIC,
        "usage": QuestionUsage.COMPREHENSION,
        "stem": "<p>מהי הנוסחה לחישוב LTV?</p>",
        "options": [
            ("סכום ההלוואה ÷ שווי הנכס × 100", True, ""),
            ("שווי הנכס ÷ סכום ההלוואה × 100", False, "זהו ההיפוך של LTV — ה-Loan-to-Value תמיד מחשב את ההלוואה כמונה ולא כמכנה."),
            ("הכנסה שנתית ÷ ערך ההלוואה", False, "זוהי נוסחה שונה לחלוטין — קרובה יותר ל-Cap Rate. LTV קשור למינוף, לא לתשואה."),
            ("שירות חוב שנתי ÷ NOI", False, "זוהי נוסחת ה-DSCR — מדד שונה לחלוטין שבוחן כיסוי חוב, לא מינוף."),
        ],
        "explanation": "<p>LTV — Loan-to-Value — הוא יחס בין סכום ההלוואה לשווי הנכס. מחושב: (הלוואה ÷ שווי) × 100. ה-LTV גבוה = מינוף גבוה = סיכון גבוה למלווה.</p>",
        "insight": "ועדת אשראי שרואה LTV שגוי בניתוח תפסול את המזכר על הסף — זהו המדד הבסיסי ביותר, ובלבלו עם DSCR מעיד על חוסר בסיסי בהבנה.",
    },
    {
        "external_id": "C01-M04-Q02",
        "qtype": QuestionType.SINGLE_CALC,
        "difficulty": QuestionDifficulty.INTERMEDIATE,
        "usage": QuestionUsage.PRACTICE,
        "stem": "<p>נכס בשווי <strong>8,000,000 ש\"ח</strong>. מבקשים הלוואה של <strong>5,600,000 ש\"ח</strong>. מה ה-LTV?</p>",
        "options": [
            ("70%", True, ""),
            ("56%", False, "56% הוא 5,600,000 ÷ 10,000,000 — בשגיאת הנחת שווי הנכס כ-10M. יש לחלק ב-8M."),
            ("142.8%", False, "זהו ה-VTL — ההפוך. חלקת שווי בהלוואה במקום הלוואה בשווי."),
            ("80%", False, "80% היה נכון לו ההלוואה הייתה 6,400,000 ש\"ח, לא 5,600,000."),
        ],
        "explanation": "<p>LTV = 5,600,000 ÷ 8,000,000 × 100 = 70%. מתחת לרף של 75% שהוגדר — העסקה עומדת בקריטריון.</p>",
        "insight": "בחישוב LTV שגוי בפגישת ועדת אשראי, כל הדיון על כיסוי חוב ותשואה נופל — המספר הזה הוא עוגן הניתוח.",
    },
]


class Command(BaseCommand):
    help = "Seed initial domain, courses, and sample module data"

    def handle(self, *args, **options):
        self.stdout.write("Seeding domain...")
        domain, _ = Domain.objects.get_or_create(
            slug="real-estate-finance-il",
            defaults={
                "name_he": "מימון נדל\"ן — ישראל",
                "name_en": "Real Estate Finance — Israel",
                "description_he": "תחום הכשרה לאנליסטים בחברות מימון נדל\"ן בישראל.",
                "display_order": 1,
            },
        )
        self.stdout.write(self.style.SUCCESS(f"  Domain: {domain.name_he}"))

        self.stdout.write("Seeding 12 courses...")
        for num, slug, title, phase, passing, capstone in COURSES:
            course, created = Course.objects.get_or_create(
                domain=domain,
                course_number=num,
                defaults={
                    "title_he": title,
                    "slug": slug,
                    "phase": phase,
                    "passing_score_pct": passing,
                    "is_capstone": capstone,
                    "exam_question_count": 20,
                    "exam_duration_minutes": 60,
                },
            )
            tag = "NEW" if created else "exists"
            self.stdout.write(f"  [{tag}] {slug}")

        self.stdout.write("Seeding Course 1, Module 4 (LTV & DSCR)...")
        c1 = Course.objects.get(domain=domain, course_number=1)
        module, _ = Module.objects.get_or_create(
            course=c1,
            module_number=4,
            defaults={
                "title_he": "מדדים מרכזיים: LTV ו-DSCR",
                "slug": "ltv-dscr",
                "estimated_minutes": 45,
            },
        )

        components = [
            (ComponentType.READING, 1, SAMPLE_READING, ""),
            (ComponentType.COMPREHENSION, 2, "", "ענה על שאלות ההבנה הבאות לאחר קריאת החומר."),
            (ComponentType.EXERCISES, 3, "", "פתור את התרגילים הבאים. יש לך שתי הזדמנויות לכל שאלה."),
            (ComponentType.SUMMARY, 4, "<p>בשיעור זה למדנו את שני מדדי הלב של ניתוח אשראי נדל\"ן: LTV ו-DSCR. שמור עליהם בזיכרון — הם יופיעו בכל ניתוח עסקה שתכתוב.</p>", ""),
        ]
        for ctype, order, body, instructions in components:
            ModuleComponent.objects.get_or_create(
                module=module, order=order,
                defaults={"component_type": ctype, "body_html_he": body, "instructions_he": instructions},
            )

        self.stdout.write("Seeding sample questions for C01-M04...")
        for q_data in SAMPLE_QUESTIONS:
            q, created = Question.objects.get_or_create(
                question_id_external=q_data["external_id"],
                defaults={
                    "course": c1,
                    "module": module,
                    "question_type": q_data["qtype"],
                    "difficulty": q_data["difficulty"],
                    "usage_context": q_data["usage"],
                    "stem_html_he": q_data["stem"],
                    "points": 1,
                    "senior_insight_he": q_data["insight"],
                },
            )
            if created:
                for idx, (text, correct, rationale) in enumerate(q_data["options"]):
                    QuestionOption.objects.create(
                        question=q, text_he=text, is_correct=correct,
                        display_order=idx, distractor_rationale_he=rationale,
                    )
                QuestionExplanation.objects.create(question=q, explanation_html_he=q_data["explanation"])
            self.stdout.write(f"  [{'NEW' if created else 'exists'}] {q_data['external_id']}")

        self.stdout.write(self.style.SUCCESS("\nSeed complete."))
