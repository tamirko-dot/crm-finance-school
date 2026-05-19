"""
Seeds Module 1-3 content for Course 9 (מודלים פיננסיים מתקדמים).
Usage: python manage.py seed_c09_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": "מודל DCF מתקדם לנכס מניב",
        "slug": "model-dcf-matakim-nkhas-maniv",
        "estimated_minutes": 60,
    },
    {
        "module_number": 2,
        "title_he": "ניתוח רגישות ותרחישים",
        "slug": "nitur-rigishut-vtarkhishim",
        "estimated_minutes": 55,
    },
    {
        "module_number": 3,
        "title_he": "מימון בנייה — מודל Construction Finance",
        "slug": "mimun-bniya-construction-finance",
        "estimated_minutes": 60,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (מודל DCF מתקדם לנכס מניב)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>מודל DCF מתקדם לנכס מניב — בנייה שלב אחר שלב</h2>

<p>
מודל DCF (Discounted Cash Flow) הוא הכלי המרכזי לתמחור נכסי נדל"ן מניבים. בניגוד
לשיטת ה-Cap Rate הפשוטה שמעריכה נכס על בסיס NOI שנה אחת, מודל DCF בונה תחזית מלאה
של תזרימי מזומנים לכל שנות ההחזקה — ומוסיף ערך מכירה (Exit Value) בסוף האופק. הוא
מאפשר לאנליסט לקחת בחשבון שינויים בשכ"ד, תפוסה, הוצאות ואפילו מבנה הון לאורך זמן.
</p>

<h2>שלב 1 — תחזית NOI שנתי</h2>

<p>
<strong>NOI (Net Operating Income)</strong> הוא ההכנסה התפעולית נטו של הנכס — לפני
מימון ומסים. חישובו:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
הכנסות פוטנציאליות מלאות (Gross Potential Rent)    = שטח × שכ"ד × 12<br>
פחות: אובדן תפוסה וחובות אבודים (Vacancy &amp; Credit Loss) = GPR × שיעור ריקנות<br>
= הכנסות אפקטיביות (Effective Gross Income)<br>
פחות: הוצאות תפעול (Operating Expenses)             = ניהול + תחזוקה + ביטוח + ארנונה<br>
= NOI
</div>

<p>
<strong>דוגמה — נכס משרדים, אופק 5 שנים:</strong>
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
שטח: 6,000 מ"ר | שכ"ד ראשוני: 120 ₪/מ"ר/חודש | עלייה שנתית בשכ"ד: 3%<br>
שיעור ריקנות: 5% | הוצאות תפעול: 25% מ-EGI<br><br>
שנה 1:<br>
  GPR  = 6,000 × 120 × 12 = 8,640,000 ₪<br>
  Vacancy = 8,640,000 × 5% = 432,000 ₪<br>
  EGI  = 8,208,000 ₪<br>
  OpEx = 8,208,000 × 25% = 2,052,000 ₪<br>
  NOI  = 6,156,000 ₪<br><br>
שנה 2 (שכ"ד עולה 3%):<br>
  GPR  = 6,000 × 123.6 × 12 = 8,899,200 ₪<br>
  NOI  ≈ 6,340,680 ₪<br><br>
שנה 3–5: חישוב דומה עם עלייה שנתית.
</div>

<h2>שלב 2 — הוצאות הון (CapEx) ורזרבה</h2>

<p>
נכסים מניבים דורשים <strong>הוצאות הון תקופתיות (Capital Expenditures)</strong> — שיפוצים,
החלפת מערכות, שדרוג כניסות, שיפורים לשוכרים (TI — Tenant Improvements). יש לתקצב
<strong>רזרבת CapEx שנתית</strong> ולהפחיתה מהתזרים החופשי.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל אצבע:</strong><br>
  רזרבת CapEx סטנדרטית: 15–25 ₪/מ"ר/שנה לנכסי משרדים ותעשייה.<br>
  50–80 ₪/מ"ר/שנה לנכסי מלונאות ופנוי-אכלוס גבוה.<br>
  תמיד בדוק את מצב הנכס — נכס ישן או מוזנח דורש רזרבה גבוהה יותר.
</div>

<h2>שלב 3 — Exit Value (שווי מכירה בסוף האופק)</h2>

<p>
<strong>Exit Value</strong> מחושב לפי שיטת ה-Cap Rate: מחלקים את NOI של שנת ה-Exit
ב<strong>Exit Cap Rate</strong> (שיעור ההיוון שמייחס השוק לנכס דומה באותו מועד עתידי).
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Exit Value = NOI שנת Exit ÷ Exit Cap Rate<br><br>
דוגמה:<br>
  NOI שנה 6 (שנה לאחר האופק): 7,100,000 ₪<br>
  Exit Cap Rate: 6.5%<br>
  Exit Value = 7,100,000 ÷ 0.065 = 109,230,769 ₪ ≈ 109.2M₪<br><br>
  פחות: עלויות מכירה (1.5%–2%): 109,230,769 × 1.5% = 1,638,462 ₪<br>
  Exit Value נטו = 107,592,307 ₪ ≈ 107.6M₪
</div>

<h2>שלב 4 — היוון תזרימים (NPV ו-IRR)</h2>

<p>
לאחר בניית תחזית NOI שנתי ו-Exit Value, מהוונים את כל התזרימים לערך נוכחי (NPV) ומחשבים
את ה-IRR. <strong>IRR (Internal Rate of Return)</strong> הוא שיעור ההיוון שמאפס את ה-NPV —
כלומר, התשואה השנתית הפנימית על ההשקעה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
תזרים מזומנים — אופק 5 שנים:<br>
  שנה 0 (השקעה):   -100,000,000 ₪<br>
  שנה 1 (NOI נטו):   5,900,000 ₪<br>
  שנה 2:             6,080,000 ₪<br>
  שנה 3:             6,265,000 ₪<br>
  שנה 4:             6,455,000 ₪<br>
  שנה 5:             6,650,000 ₪ + Exit Value 107,600,000 ₪ = 114,250,000 ₪<br><br>
NPV (בשיעור היוון 8%) = 5,815,000 ₪ — חיובי → השקעה כדאית<br>
IRR ≈ 8.6% לשנה<br>
Equity Multiple = (סה"כ תקבולים) / (השקעה ראשונית) = 145,350,000 / 100,000,000 = 1.45x
</div>

<h2>מדדי תשואה — NPV, IRR ו-Equity Multiple</h2>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מדד</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">פירוש</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">סף קבלה טיפוסי</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">NPV חיובי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ההשקעה מוסיפה ערך מעל שיעור ההיוון</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">NPV &gt; 0</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">IRR</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תשואה שנתית פנימית על ההון</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">8%–12% לנדל"ן מניב ישראל</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Equity Multiple</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כמה פעמים הוכפל ההון</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.5x–2.5x לאופק 5–7 שנים</td>
    </tr>
  </tbody>
</table>

<h2>רגישות ל-Exit Cap Rate — כמה זה משנה?</h2>

<p>
<strong>Exit Cap Rate</strong> הוא המשתנה הרגיש ביותר במודל DCF. עלייה של 1% ב-Exit Cap Rate
מפחיתה את ה-Exit Value באופן דרסטי ומשפיעה ישירות על ה-IRR:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
NOI שנת Exit: 7,100,000 ₪<br><br>
Exit Cap Rate 5.5% → Exit Value = 7,100,000 / 0.055 = 129.1M₪ → IRR ≈ 10.2%<br>
Exit Cap Rate 6.5% → Exit Value = 7,100,000 / 0.065 = 109.2M₪ → IRR ≈ 8.6%<br>
Exit Cap Rate 7.5% → Exit Value = 7,100,000 / 0.075 =  94.7M₪ → IRR ≈ 7.1%<br><br>
עלייה של 1% ב-Exit Cap Rate → ירידה של ~1.5% ב-IRR.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>שגיאות נפוצות במודלי DCF:</strong><br>
  (א) Exit Cap Rate זהה לכניסה — בפועל נכסים מזדקנים; Exit Cap Rate לרוב גבוה ב-25–50bps
  מ-Going-In Cap Rate.<br>
  (ב) עלייה קבועה של NOI בלי להתחשב בפקיעת חוזים — בפועל NOI יכול לרדת בשנות חידוש.<br>
  (ג) אי-תקצוב CapEx — מגדיל NOI באופן מלאכותי ומנפח IRR.<br>
  (ד) שימוש ב-NOI שנה 1 כבסיס ל-Exit Value (במקום NOI שנת Exit + 1).<br>
  (ה) שימוש בשיעור היוון נמוך מדי ביחס לסיכון האמיתי של הנכס.
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Comprehension HTML
# ---------------------------------------------------------------------------

M1_COMPREHENSION_HTML = """
<p>ענה על שאלות ההבנה הבאות.</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Exercises HTML
# ---------------------------------------------------------------------------

M1_EXERCISES_HTML = """
<p>פתור את התרגילים הבאים.</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — מודל DCF מתקדם לנכס מניב</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>מבנה מודל DCF:</strong> GPR פחות ריקנות = EGI; פחות OpEx = NOI; פחות CapEx = תזרים
    חופשי. בנה את המודל שנה-שנה לכל אופק ההחזקה — אל תסתפק ב-NOI שנה אחת.
  </li>
  <li>
    <strong>Exit Value:</strong> חשב כ-NOI(n+1) ÷ Exit Cap Rate, פחות עלויות מכירה.
    ה-Exit Value מהווה בדרך כלל 60%–80% מסך ערך ה-DCF — הוא הגורם הדומיננטי.
  </li>
  <li>
    <strong>IRR ו-Equity Multiple:</strong> IRR מודד תשואה שנתית; Equity Multiple מודד
    כמה פעמים הוכפל ההון. השתמש בשניהם — IRR גבוה על אופק קצר מאוד עלול להיות מטעה.
  </li>
  <li>
    <strong>Exit Cap Rate — הגורם הקריטי:</strong> עלייה של 1% ב-Exit Cap Rate מורידה
    IRR בכ-1.5%. תמיד הנח Exit Cap Rate גבוה ב-25–50bps מ-Going-In — נכסים מזדקנים.
  </li>
  <li>
    <strong>שגיאות נפוצות:</strong> NOI ללא CapEx, Exit Cap Rate זהה לכניסה, עלייה קבועה
    ללא התחשבות בחידוש חוזים — כל אלה מנפחים IRR באופן מלאכותי.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
בנינו מודל DCF בסיסי — אך מודל אחד אינו מספיק. <em>מודול 2</em> מלמד כיצד לבחון
<strong>רגישות ותרחישים</strong>: מה קורה ל-IRR כשמשנים Exit Cap Rate, שיעור ריקנות
וגידול שכ"ד בו-זמנית? כיצד בונים Bull / Bear / Stress Case ומציגים אותם לוועדת האשראי?
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (ניתוח רגישות ותרחישים)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>ניתוח רגישות ותרחישים — מה קורה כשהנחות הבסיס מתממשות אחרת?</h2>

<p>
מודל DCF מבוסס על הנחות: שיעור עלייה שנתי בשכ"ד, שיעור ריקנות, Exit Cap Rate, אופק
החזקה. אף אחת מהנחות אלה אינה ודאית. <strong>ניתוח רגישות ותרחישים</strong> הוא הכלי
שמאפשר לאנליסט לכמת: "מה קורה אם אנחנו טועים?" — ולהציג לוועדת האשראי את הטווח הריאלי
של התוצאות, לא רק את מקרה הבסיס.
</p>

<h2>רגישות (Sensitivity Analysis) — שינוי משתנה אחד</h2>

<p>
ב<strong>ניתוח רגישות</strong> משנים <em>משתנה אחד בלבד</em> בכל פעם ובוחנים את השפעתו
על מדד התשואה (IRR, NPV). לדוגמה: "מה קורה ל-IRR אם Exit Cap Rate עולה מ-6.5% ל-7.5%?".
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
טבלת רגישות — IRR לפי Exit Cap Rate:<br><br>
  Exit Cap Rate  | IRR<br>
  ─────────────────────<br>
  5.5%           | 10.2%<br>
  6.0%           | 9.4%<br>
  6.5% (בסיס)   |  8.6%<br>
  7.0%           |  7.8%<br>
  7.5%           |  7.1%<br>
  8.0%           |  6.4%<br><br>
מסקנה: כל 0.5% עלייה ב-Exit Cap Rate מוריד IRR בכ-0.75%.
</div>

<h3>טבלת רגישות דו-ממדית (Two-Way Sensitivity Table)</h3>

<p>
אנליסטים מתקדמים בונים <strong>טבלאות רגישות דו-ממדיות</strong> שמשנות שני משתנים
בו-זמנית — למשל Exit Cap Rate ושיעור גידול NOI — ומראות IRR לכל צירוף.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">גידול NOI \ Exit Cap</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">5.5%</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">6.5%</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">7.5%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1% לשנה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">9.1%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">7.5%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">6.1%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3% לשנה (בסיס)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10.2%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;font-weight:bold;">8.6%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">7.1%</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5% לשנה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">11.4%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">9.7%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">8.2%</td>
    </tr>
  </tbody>
</table>

<h2>ניתוח תרחישים (Scenario Analysis) — שינוי מספר משתנים בו-זמנית</h2>

<p>
ב<strong>ניתוח תרחישים</strong> מגדירים מספר <em>תרחישים שלמים</em> — כל אחד מכיל קבוצת
הנחות שמשקפת מצב שוק שונה. הגישה הנפוצה ביותר כוללת ארבעה תרחישים:
</p>

<h3>מסגרת ארבעת התרחישים:</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">תרחיש</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">גידול שכ"ד</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ריקנות</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">Exit Cap</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">IRR</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#e8f5e9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Bull Case (שוק חזק)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5% לשנה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5.5%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">11.4%</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;font-weight:bold;">Base Case (ציפייה)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3% לשנה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">6.5%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;font-weight:bold;">8.6%</td>
    </tr>
    <tr style="background:#fff8e1;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Bear Case (שוק חלש)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1% לשנה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">7.5%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5.8%</td>
    </tr>
    <tr style="background:#ffebee;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Stress Case (קיצון)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">-2% לשנה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">20%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">9.0%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2.1%</td>
    </tr>
  </tbody>
</table>

<h2>כיצד לבחור את המשתנים לבחינת רגישות?</h2>

<p>
לא כל משתנה שווה — חלקם משפיעים דרמטית על ה-IRR, אחרים כמעט לא. קבוצת המשתנים
שתמיד כדאי לכלול בניתוח רגישות בנדל"ן מניב:
</p>

<ul>
  <li>
    <strong>Exit Cap Rate</strong> — הגורם הרגיש ביותר; שינוי קטן = השפעה גדולה על Exit Value.
  </li>
  <li>
    <strong>שיעור ריקנות</strong> — ירידת תפוסה ב-10% יכולה להוריד NOI ב-10%–15%.
  </li>
  <li>
    <strong>שיעור גידול שכ"ד</strong> — בנכסים עם חוזים ארוכים; פחות קריטי אם חוזים
    כוללים עדכון מדדי.
  </li>
  <li>
    <strong>אופק מכירה (Exit Timing)</strong> — מכירה בשנה 3 מול שנה 7 יכולה לשנות
    IRR ב-1%–2% בהתאם למחזור השוק.
  </li>
  <li>
    <strong>הוצאות CapEx</strong> — רלוונטי בנכסים ישנים שדורשים שיפוץ.
  </li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל — מה להציג לוועדת אשראי:</strong><br>
  הצג את ה-Base Case כתרחיש המרכזי — אך כלול תמיד את ה-Bear Case ו-Stress Case.
  ועדת האשראי לא מעוניינת רק "מה קורה אם הכול ילך כמתוכנן" — היא רוצה לדעת
  <strong>"מה ה-IRR בתרחיש הכי גרוע שיכול להתרחש, ועדיין לאשר את ההלוואה?"</strong>
  השאלה המרכזית: האם גם ב-Bear Case ה-DSCR נשאר מעל 1.0?
</div>

<h2>הצגת תוצאות לוועדת אשראי — עקרונות</h2>

<ul>
  <li>
    <strong>מפת חום (Heat Map):</strong> צבע תאי טבלת הרגישות — ירוק לאזורים שה-IRR מעל
    הסף הנדרש, אדום לאזורים מתחת.
  </li>
  <li>
    <strong>Probability Weighting:</strong> הקצה הסתברות לכל תרחיש (לדוגמה: Bull 20%,
    Base 50%, Bear 25%, Stress 5%) וחשב IRR ממוצע משוקלל — "Expected IRR".
  </li>
  <li>
    <strong>Downside Protection:</strong> הדגש את המרחק בין Base Case ל-Break-Even IRR
    (IRR שמכסה עלות הון). ככל שהמרחק גדול יותר — ההשקעה עמידה יותר.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — Stress Case אמיתי:</strong><br>
  Stress Case אינו רק "ריקנות גבוהה קצת". תרחיש Stress אמיתי משקף משבר שוק: ירידת
  שכ"ד של 15%–25%, ריקנות של 20%–30%, Exit Cap Rate שעולה 200–300bps — בו-זמנית.
  אם המודל לא נבדק בתרחיש כזה, לא ניתחת את הסיכון האמיתי.
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Comprehension HTML
# ---------------------------------------------------------------------------

M2_COMPREHENSION_HTML = """
<p>ענה על שאלות ההבנה הבאות.</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Exercises HTML
# ---------------------------------------------------------------------------

M2_EXERCISES_HTML = """
<p>פתור את התרגילים הבאים.</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — ניתוח רגישות ותרחישים</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>הבדל בין רגישות לתרחישים:</strong> ניתוח רגישות משנה משתנה אחד בכל פעם ומודד
    השפעתו; ניתוח תרחישים משנה קבוצת משתנים שלמה שמגדירים "מצב שוק" מסוים.
  </li>
  <li>
    <strong>ארבעת התרחישים:</strong> Bull / Base / Bear / Stress. Base Case הוא הציפייה
    הריאלית; Bear Case הוא תרחיש חלש אך אפשרי; Stress Case הוא תרחיש קיצון לבחינת עמידות.
  </li>
  <li>
    <strong>משתנים לבחינת רגישות:</strong> Exit Cap Rate (הרגיש ביותר), שיעור ריקנות,
    גידול שכ"ד ואופק מכירה. CapEx בנכסים ישנים. בחר משתנים לפי חומר הספציפי של הנכס.
  </li>
  <li>
    <strong>הצגה לוועדת אשראי:</strong> מפת חום + Probability Weighting + Downside Protection.
    ועדה רוצה לראות את ה-IRR בתרחיש הגרוע ואת ה-DSCR ב-Bear Case — לא רק Base Case.
  </li>
  <li>
    <strong>Stress Case אמיתי:</strong> ירידת שכ"ד 15%–25% + ריקנות 20%–30% + Exit Cap
    גבוה ב-200–300bps — בו-זמנית. כל פחות מזה אינו Stress אמיתי.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
לימדנו לבנות DCF ולנתחו בתרחישים. <em>מודול 3</em> מרחיב לסוג נכסים שונה לגמרי —
<strong>מימון בנייה (Construction Finance)</strong>: כיצד ממנים פרויקט ייזום שעדיין
לא קיים, מה לוח השאיבות, כיצד מחשבים רזרבת ריבית וכיצד מנהלים סיכון השלמה?
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (מימון בנייה — Construction Finance)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>מימון בנייה (Construction Finance) — מאפיינים ייחודיים</h2>

<p>
מימון בנייה שונה מהותית ממימון נכסים מניבים. בנכס מניב קיים, הכנסות הנכס מכסות את
שירות החוב מהיום הראשון. בפרויקט בנייה, הנכס עדיין לא קיים — ייקח 18–36 חודשים עד
שיושלם, ייכבש ויייצר הכנסות. בכל תקופת הבנייה, הלווה חייב לשלם ריבית ולמן
עלויות בנייה — ממקורות אחרים. זוהי מהות <strong>Construction Finance</strong>.
</p>

<h2>ההבדלים המרכזיים בין Construction Finance לנכס מניב</h2>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">פרמטר</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">נכס מניב קיים</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מימון בנייה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מקור שירות חוב</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">NOI שוטף</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רזרבת ריבית / הון עצמי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בטחון עיקרי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעבוד נכס קיים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעבוד קרקע + ערבות + Takeout</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">DSCR בתקופת בנייה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בדרך כלל &gt; 1.2</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">N/A — אין הכנסות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">LTC (Loan-to-Cost)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לא רלוונטי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">60%–75% מסך עלות הפרויקט</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון מרכזי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריקנות, ריבית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אי-השלמה, חריגת עלויות</td>
    </tr>
  </tbody>
</table>

<h2>LTC — Loan to Cost</h2>

<p>
בנכסים קיימים מודדים LTV (Loan-to-Value). בפרויקטי בנייה מודדים <strong>LTC (Loan-to-Cost)</strong>
— יחס ההלוואה לעומת עלות הפרויקט הכוללת:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
LTC = סכום ההלוואה ÷ עלות הפרויקט הכוללת<br><br>
דוגמה:<br>
  עלות פרויקט כוללת (קרקע + בנייה + רזרבות): 80,000,000 ₪<br>
  הון עצמי יזם:                               24,000,000 ₪ (30%)<br>
  הלוואת בנייה:                               56,000,000 ₪ (70%)<br><br>
  LTC = 56,000,000 / 80,000,000 = 70%<br><br>
כלל: LTC מקסימלי מקובל בישראל: 70%–75%.
מעל 75% — המלווה נושא בחלק גדול מדי מסיכון הפרויקט.
</div>

<h2>לוח שאיבות (Draw Schedule)</h2>

<p>
בשונה מהלוואה רגילה בה מלוא הסכום מועבר ביום החתימה, ב-Construction Finance
ההלוואה <strong>נשאבת בשלבים (Draws)</strong> לפי התקדמות הבנייה. כל שאיבה דורשת
אישור של מפקח בנייה שמוודא שהעבודה בוצעה כנדרש.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
דוגמה — לוח שאיבות לפרויקט 24 חודש:<br><br>
  חודש 0  (סגירה):    10,000,000 ₪ — רכישת קרקע / הכנות<br>
  חודש 3  (יסודות):    8,000,000 ₪ — עבודות עפר ויסודות<br>
  חודש 6  (שלד):      12,000,000 ₪ — שלד קונקרט<br>
  חודש 12 (גמר חוץ):  10,000,000 ₪ — חיפויים, גג, חלונות<br>
  חודש 18 (גמר פנים):  8,000,000 ₪ — חשמל, אינסטלציה, גמר פנים<br>
  חודש 22 (השלמה):     8,000,000 ₪ — אחרי טופס 4 / רישיון אכלוס<br>
  ─────────────────────────────────────────<br>
  סה"כ:               56,000,000 ₪
</div>

<h2>רזרבת ריבית (Interest Reserve)</h2>

<p>
מכיוון שבתקופת הבנייה הנכס אינו מייצר הכנסות, הריבית על ההלוואה משולמת <strong>מרזרבת
ריבית (Interest Reserve)</strong> — סכום שמוכלל מראש בתקציב הפרויקט ומשולם לבנק
מהשאיבות השוטפות.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
חישוב רזרבת ריבית:<br><br>
  ריבית שנתית: 9% (פריים 7% + 2%)<br>
  אופק בנייה: 24 חודשים<br>
  קרן ממוצעת שאובה: ~28,000,000 ₪ (מחצית ה-56M₪ — שנאבת בהדרגה)<br><br>
  ריבית שנה 1: 28,000,000 × 9% = 2,520,000 ₪<br>
  ריבית שנה 2: 42,000,000 × 9% = 3,780,000 ₪ (קרן ממוצעת גדולה יותר)<br>
  סה"כ רזרבת ריבית: ≈ 6,300,000 ₪<br><br>
  רזרבת ריבית כאחוז מגודל הפרויקט: 6,300,000 / 80,000,000 = 7.9%<br>
  (כלל אצבע: 6%–10% מעלות הפרויקט לאופק 18–24 חודשים)
</div>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל — רזרבת ריבית חייבת להכיל "כרית" לחריגות:</strong><br>
  תמיד תקצב רזרבת ריבית ל-6 חודשים יותר מאופק הבנייה המתוכנן.
  עיכובים של 3–6 חודשים שכיחים בישראל (פיקוח בנייה, היתרים, בעיות קבלן).
  רזרבה שלא מספיקה = הלווה חייב להזרים הון נוסף באמצע הפרויקט.
</div>

<h2>סיכון השלמה (Completion Risk) וכלי מיתיגציה</h2>

<p>
<strong>סיכון השלמה</strong> הוא הסיכון שהפרויקט לא יושלם — בשל פשיטת רגל של קבלן ראשי,
חריגה תקציבית דרסטית, בעיות היתרים, סכסוכי שכנים, זיהום קרקע שנתגלה. נכס שלא
הושלם לא מייצר הכנסות ולא ניתן למכירה כנכס מניב — המלווה עלול להישאר עם קרקע
בלבד כבטחון.
</p>

<h3>כלי מיתיגציה לסיכון השלמה:</h3>

<ul>
  <li>
    <strong>ערבות השלמה (Completion Guarantee):</strong> בעל המניות / הספונסור חותם
    על ערבות אישית להשלמת הפרויקט על חשבונו — גם אם עלויות יחרגו מהתקציב.
  </li>
  <li>
    <strong>ביטוח קבלן (Performance Bond):</strong> הקבלן הראשי מספק ביטוח הוצאה
    (Performance Bond) שמבטיח שאם הוא לא ישלים — חברת הביטוח תסיים.
  </li>
  <li>
    <strong>ניכיון אחרון (Retention):</strong> 5%–10% מכל תשלום לקבלן מעוכבים
    ומשולמים רק לאחר קבלת טופס 4. מינוף לסיום עבודה.
  </li>
  <li>
    <strong>חשבון ביניים מאושר (Inspector Approvals):</strong> כל שאיבה מאושרת ע"י
    מפקח בנייה מטעם הבנק — מוודא שהעבודה בוצעה לפני שחרור כסף.
  </li>
  <li>
    <strong>Cost-to-Complete Analysis:</strong> בכל שאיבה — מה עלויות ה-To-Complete?
    האם הקרן הנותרת + ההון העצמי מספיקים לסיים?
  </li>
</ul>

<h2>Takeout Commitment (מחויבות מחזור)</h2>

<p>
<strong>Takeout Commitment</strong> הוא מחויבות מראש של מלווה קבע (לרוב בנק אחר) לתת
הלוואת מחזור (Permanent Loan) לאחר השלמת הבנייה ואכלוסה. ה-Takeout מבטיח את הלווה
שיהיה לו מימון קבע — ומאפשר למלווה הבנייה להשלים את פירעונו.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
מבנה עסקת Construction Finance עם Takeout:<br><br>
  שלב 1: הלוואת בנייה (Construction Loan)<br>
    → סכום: 56,000,000 ₪<br>
    → אופק: 24 חודשים<br>
    → ריבית: פריים + 2.5% (גבוה יותר — סיכון גבוה)<br>
    → פירעון: ב-Takeout<br><br>
  שלב 2: Takeout / Permanent Loan<br>
    → סכום: 50,000,000 ₪ (לפי LTV 65% על שווי הנכס המוגמר)<br>
    → אופק: 10–15 שנה<br>
    → ריבית: פריים + 1.5%<br>
    → תנאי: תפוסה מינימלית 80%, NOI מינימלי 4,500,000 ₪
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — Construction Finance ללא Takeout:</strong><br>
  אישור הלוואת בנייה ללא Takeout Commitment מראש חושף את המלווה לסיכון מימון מחדש
  בסיום הבנייה. אם שוק האשראי מתהדק בעת ההשלמה, הלווה לא יוכל לקבל Permanent Loan —
  וחייב לפרוע את הלוואת הבנייה. <strong>תמיד דרוש Pre-Commitment לפני אישור
  Construction Loan בסכומים מעל 20M₪.</strong>
</div>

<h3>גשר למודול הבא</h3>
<p>
למדנו את יסודות Construction Finance — LTC, לוח שאיבות, רזרבת ריבית, סיכון השלמה
ו-Takeout. <em>מודול 4</em> מעמיק במודלים פיננסיים מתקדמים יותר: <strong>מודלים
משותפים (Joint Venture Waterfalls)</strong> — כיצד מחלקים תשואות בין שותפים בפרויקט,
מהי Preferred Return, מהי Promote ומתי כל שותף "נכנס לכסף".
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Comprehension HTML
# ---------------------------------------------------------------------------

M3_COMPREHENSION_HTML = """
<p>ענה על שאלות ההבנה הבאות.</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Exercises HTML
# ---------------------------------------------------------------------------

M3_EXERCISES_HTML = """
<p>פתור את התרגילים הבאים.</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — מימון בנייה (Construction Finance)</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>ההבדל המהותי מנכס מניב:</strong> Construction Finance מממן נכס שטרם קיים.
    אין NOI שוטף — שירות החוב מגיע מרזרבת ריבית שנבנית לתוך תקציב הפרויקט. המדד
    המרכזי הוא LTC, לא LTV.
  </li>
  <li>
    <strong>LTC (Loan-to-Cost):</strong> יחס ההלוואה לעלות הפרויקט הכוללת. סטנדרט:
    LTC מקסימלי 70%–75%. מעל 75% — המלווה נושא בחלק גדול מדי מסיכון הפרויקט.
  </li>
  <li>
    <strong>לוח שאיבות ומפקח:</strong> ההלוואה נשאבת בשלבים לפי התקדמות הבנייה.
    כל שאיבה דורשת אישור מפקח בנייה עצמאי. שחרור כסף לפני אישור — הוא שגיאת ניהול.
  </li>
  <li>
    <strong>רזרבת ריבית:</strong> תקצב לפחות ל-6 חודשים מעבר לאופק הבנייה המתוכנן.
    עיכובים שכיחים — רזרבה שנגמרת לפני ההשלמה מכריחה את הלווה להזרים הון נוסף.
  </li>
  <li>
    <strong>Takeout Commitment:</strong> מחויבות מראש למחזור בהלוואת קבע לאחר השלמה.
    ללא Takeout — Construction Loan מעל 20M₪ חשוף לסיכון מימון מחדש חמור בסיום הבנייה.
  </li>
</ol>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 9 "
        "(מודלים פיננסיים מתקדמים)"
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 9 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=9)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=9 not found. "
                "Run 'python manage.py seed_data' first to create the course structure."
            )

        self.stdout.write(f"Found course: {course}")

        # Pair each module metadata with its component HTML strings
        module_content = [
            (MODULES[0], M1_READING_HTML, M1_COMPREHENSION_HTML, M1_EXERCISES_HTML, M1_SUMMARY_HTML),
            (MODULES[1], M2_READING_HTML, M2_COMPREHENSION_HTML, M2_EXERCISES_HTML, M2_SUMMARY_HTML),
            (MODULES[2], M3_READING_HTML, M3_COMPREHENSION_HTML, M3_EXERCISES_HTML, M3_SUMMARY_HTML),
        ]

        for module_meta, reading_html, comprehension_html, exercises_html, summary_html in module_content:
            self._seed_module(course, module_meta, reading_html, comprehension_html, exercises_html, summary_html)

        self.stdout.write(
            self.style.SUCCESS("\nAll done — Course 9 modules 1-3 seeded successfully.")
        )

    def _seed_module(
        self,
        course: Course,
        meta: dict,
        reading_html: str,
        comprehension_html: str,
        exercises_html: str,
        summary_html: str,
    ) -> None:
        # ── Module ────────────────────────────────────────────────────────
        module, created = Module.objects.get_or_create(
            course=course,
            module_number=meta["module_number"],
            defaults={
                "title_he": meta["title_he"],
                "slug": meta["slug"],
                "estimated_minutes": meta["estimated_minutes"],
            },
        )
        if not created:
            # Update mutable fields in case they changed
            module.title_he = meta["title_he"]
            module.slug = meta["slug"]
            module.estimated_minutes = meta["estimated_minutes"]
            module.save(update_fields=["title_he", "slug", "estimated_minutes", "updated_at"])

        verb = "Created" if created else "Updated"
        self.stdout.write(f"  {verb} module: {module}")

        # ── Components ────────────────────────────────────────────────────
        components = [
            # (order, component_type, body_html_he)
            (1, ComponentType.READING, reading_html),
            (2, ComponentType.COMPREHENSION, comprehension_html),
            (3, ComponentType.EXERCISES, exercises_html),
            (4, ComponentType.SUMMARY, summary_html),
        ]

        for order, comp_type, body_html in components:
            component, comp_created = ModuleComponent.objects.get_or_create(
                module=module,
                order=order,
                defaults={
                    "component_type": comp_type,
                    "body_html_he": body_html,
                },
            )
            if not comp_created:
                component.component_type = comp_type
                component.body_html_he = body_html
                component.save(update_fields=["component_type", "body_html_he", "updated_at"])

            comp_verb = "Created" if comp_created else "Updated"
            self.stdout.write(
                f"    {comp_verb} component order={order} type={comp_type}"
            )
