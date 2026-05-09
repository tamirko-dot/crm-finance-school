"""
Management command: seed_c04_modules456
Seeds Course 4 (מדדים פיננסיים בנדל"ן), Modules 4, 5, and 6 with full reading,
comprehension, exercises, and summary ModuleComponent records.

Usage:
    python manage.py seed_c04_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — IRR ו-Equity Multiple
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  IRR ו-Equity Multiple — מדדי תשואה מתקדמים
</h2>

<!-- ===== סעיף 1 — IRR ===== -->
<h3 style="color:#1a2638;">1. IRR — הגדרה ומשמעות</h3>

<p>
  <strong>Internal Rate of Return (IRR)</strong> — שיעור התשואה הפנימי — הוא שיעור ההיוון
  המביא את ה-<strong>NPV (שווי נוכחי נקי)</strong> של כל תזרימי המזומנים להשקעה לאפס.
  במילים אחרות: IRR הוא ה"ריבית" שבה ההשקעה "מחזירה את עצמה" בהתחשב בזמן שבו
  מתקבלים התזרימים.
</p>

<p>
  <strong>נוסחה קונספטואלית:</strong>
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  0 = -השקעה ראשונית + CF₁/(1+IRR)¹ + CF₂/(1+IRR)² + ... + CFₙ/(1+IRR)ⁿ
</div>

<p>
  <strong>דוגמה מספרית — פרויקט מגורים:</strong>
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שנה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">אירוע</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תזרים (מ' ₪)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">0</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">השקעת הון עצמי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">-10</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">1–3</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שלב בנייה — אין תזרים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">0</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">4</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מכירת דירות + יתרת הכנסות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#2e7d32;">+18</td>
    </tr>
  </tbody>
</table>

<p>
  ב-IRR של כ-16%, NPV = 0. כלומר, המשקיע הרוויח שיעור שנתי מורכב של 16% על הונו.
</p>

<!-- ===== סעיף 2 — Equity Multiple ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. Equity Multiple — מכפיל ההון</h3>

<p>
  <strong>Equity Multiple</strong> הוא מדד פשוט ואינטואיטיבי: כמה פעמים קיבל המשקיע בחזרה
  את כספו?
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  Equity Multiple = סך חלוקות שהתקבלו ÷ הון עצמי שהושקע
</div>

<p>
  <strong>דוגמה:</strong> משקיע השקיע 10 מ' ₪ וקיבל בסך הכל 18 מ' ₪ (כולל החזר הקרן)
  לאחר 5 שנים:
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  Equity Multiple = 18 ÷ 10 = <strong>1.8x</strong><br><br>
  פרשנות: על כל שקל שהושקע, המשקיע קיבל בחזרה 1.80 ₪ — כולל הקרן.
  "רווח נקי" הוא 0.80 ₪ לכל שקל השקעה, כלומר 80%.
</div>

<p>
  <strong>טווחי ייחוס מקובלים בישראל:</strong>
</p>

<ul style="line-height:1.9;">
  <li><strong>Equity Multiple &lt; 1.2x</strong> — תשואה נמוכה; אינה מפצה על הסיכון</li>
  <li><strong>1.2x – 1.5x</strong> — סביר לפרויקטים מניבים עם סיכון נמוך</li>
  <li><strong>1.5x – 2.0x</strong> — טוב לפרויקטי יזמות ובינוי לתקופת החזקה ממוצעת</li>
  <li><strong>מעל 2.0x</strong> — מצוין; בדרך כלל מלווה בסיכון גבוה יותר</li>
</ul>

<!-- ===== סעיף 3 — Cash-on-Cash ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. Cash-on-Cash Return — תשואה שוטפת</h3>

<p>
  בניגוד ל-IRR ול-Equity Multiple שמודדים את מכלול ההשקעה, <strong>Cash-on-Cash Return</strong>
  מודד אך ורק את <em>התזרים השנתי</em> ביחס להון שהושקע:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  Cash-on-Cash Return = תזרים מזומנים שנתי נטו ÷ הון עצמי שהושקע
</div>

<p>
  <strong>דוגמה — נכס מניב:</strong> משקיע השקיע 5 מ' ₪ בבניין משרדים. ב-2023 קיבל
  400,000 ₪ תזרים נקי לאחר הוצאות ושירות חוב:
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  Cash-on-Cash = 400,000 ÷ 5,000,000 = <strong>8%</strong><br><br>
  מדד זה רלוונטי בעיקר לנכסים מניבים, שם המשקיע מצפה לתזרים שנתי רציף.
  בפרויקט יזמות (אין הכנסה שוטפת) — Cash-on-Cash אינו רלוונטי.
</div>

<!-- ===== סעיף 4 — היחס בין IRR ל-Equity Multiple ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. היחס בין IRR ל-Equity Multiple</h3>

<p>
  IRR ו-Equity Multiple מספרים סיפורים שונים על אותה השקעה. ההבדל הקריטי:
  <strong>IRR מושפע מאוד מתזמון</strong>; Equity Multiple מודד את הגודל המוחלט של הרווח.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תרחיש</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">IRR</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">Equity Multiple</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">משמעות</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">פרויקט א' — 2 שנים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">35%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">1.4x</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">IRR גבוה, מכפיל נמוך — תשואה מהירה אך קטנה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">פרויקט ב' — 7 שנים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">18%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">2.5x</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">IRR נמוך יותר, מכפיל גבוה — תשואה גדולה לאורך זמן</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>כלל האצבע:</strong>
</p>

<ul style="line-height:1.9;">
  <li><strong>IRR גבוה + Equity Multiple נמוך</strong> = החזקה קצרה; הכסף חוזר מהר, אך סכום הרווח קטן</li>
  <li><strong>IRR נמוך יותר + Equity Multiple גבוה</strong> = החזקה ארוכה; פחות תשואה שנתית אך יותר כסף בסוף</li>
</ul>

<p>
  ההחלטה בין שני הפרויקטים תלויה במטרת המשקיע: האם הוא צריך נזילות מהירה, או יכול
  "לנעול" כסף לאורך שנים?
</p>

<!-- ===== סעיף 5 — IRR Hurdle Rates בישראל ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. IRR Hurdle Rates בישראל</h3>

<p>
  <strong>Hurdle Rate</strong> הוא ה-IRR המינימלי שמשקיע דורש על מנת להיכנס לעסקה.
  הוא משקף את עלות ההון, פרמיית הסיכון, ועלויות ההזדמנות.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג פרויקט</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">טווח IRR נדרש (ישראל)</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הסבר</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נכסים מניבים — מסחרי/מגורים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">8%–12%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תזרים יציב, סיכון נמוך-בינוני</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פיתוח ויזמות (Greenfield)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">15%–20%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכון ביצוע ושוק גבוה יותר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פינוי-בינוי / תמ"א 38</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">18%–25%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכון תכנוני-משפטי גבוה מאוד, ציר זמן לא וודאי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קרנות נדל"ן (מוסדיים)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">7%–10%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עלות הון נמוכה, מינוף מאוזן</td>
    </tr>
  </tbody>
</table>

<p>
  חשוב: ה-Hurdle Rate נמדד לאחר מינוף (levered IRR). אנליסט חייב לשאול: האם ה-IRR
  המוצג הוא <em>before</em> או <em>after</em> מינוף? ה-IRR מהמינוף יכול להיות גבוה פי 2–3
  מה-IRR הלא-ממונף.
</p>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  IRR גבוה על תקופה קצרה עלול להיות מטעה — בחן תמיד גם את ה-Equity Multiple ואת הסיכון הממשי.
  IRR של 40% על פרויקט של שנה עם Equity Multiple של 1.33x פחות אטרקטיבי ממה שנראה
  לעומת IRR של 20% על 4 שנים עם Equity Multiple של 2.1x. השאלה האמיתית היא: <em>מה הרווח
  בשקלים, ובאיזה סיכון?</em>
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של IRR, Equity Multiple, Cash-on-Cash Return "
    "וה-Hurdle Rates המקובלים בשוק הנדל\"ן בישראל. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים חישוב Equity Multiple מתזרים נתון, "
    "השוואת שני פרויקטים לפי IRR ו-Equity Multiple, וקביעת ה-Hurdle Rate המתאים "
    "לפרויקט על פי פרופיל הסיכון שלו. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — IRR ו-Equity Multiple
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>IRR הוא שיעור ההיוון שמביא NPV לאפס.</strong>
    הוא מביא בחשבון את ערך הזמן של הכסף — תזרים מוקדם שווה יותר מאוחר.
  </li>
  <li>
    <strong>Equity Multiple מודד כמה פעמים הוחזר ההון.</strong>
    הוא פשוט ואינטואיטיבי, אך אינו מביא בחשבון את תזמון התקבולים.
  </li>
  <li>
    <strong>IRR גבוה על תקופה קצרה ≠ Equity Multiple גבוה.</strong>
    חייבים לבחון את שני המדדים יחד כדי לקבל תמונה שלמה.
  </li>
  <li>
    <strong>Cash-on-Cash Return רלוונטי רק לנכסים מניבים עם תזרים שוטף.</strong>
    בפרויקטי יזמות, מדד זה אינו רלוונטי.
  </li>
  <li>
    <strong>Hurdle Rates בישראל: 8–12% לנכסים מניבים, 15–20% ליזמות.</strong>
    בדוק תמיד אם ה-IRR המוצג הוא לפני או אחרי מינוף.
  </li>
</ol>

<h3 style="color:#1a2638;margin-top:24px;">מילון מונחים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">עברית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">אנגלית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיעור תשואה פנימי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">IRR</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שיעור ההיוון שבו NPV = 0</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מכפיל הון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Equity Multiple</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סך תקבולים ÷ הון מושקע</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תשואה שוטפת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cash-on-Cash Return</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תזרים שנתי נקי ÷ הון מושקע</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיעור תשואה מינימלי נדרש</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Hurdle Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ה-IRR המינימלי שמשקיע דורש לכניסה לעסקה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שווי נוכחי נקי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NPV</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סכום תזרימים מהוונים בניכוי ההשקעה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מינוף</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Leverage</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שימוש בחוב להגדלת תשואת ההון העצמי</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — ניתוח רגישות ומינוף
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  ניתוח רגישות ומינוף — כלים לאנליסט האשראי
</h2>

<!-- ===== סעיף 1 — מהו ניתוח רגישות ===== -->
<h3 style="color:#1a2638;">1. מהו ניתוח רגישות?</h3>

<p>
  <strong>ניתוח רגישות (Sensitivity Analysis)</strong> הוא תהליך שיטתי של בחינת השפעת
  שינויים בהנחות המפתח על מדד פיננסי נבחר — DSCR, IRR, LTV, או NPV.
  במקום לשאול "האם ה-DSCR עומד בתנאי?" — ניתוח רגישות שואל: <em>"מה צריך להשתנות
  כדי שה-DSCR ייפול מתחת לרף?"</em>
</p>

<p>
  ניתוח רגישות אינו ניחוש עתידות — הוא מיפוי המרחב שבו ההשקעה יכולה להיכשל.
  אנליסט שמבצע ניתוח זה מבין את <strong>שוליות הבטחון (Margin of Safety)</strong>
  של כל עסקה.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>למה ניתוח רגישות הוא חובה לאנליסט אשראי?</strong><br>
  כי הנחות המודל הפיננסי הן לא מציאות — הן הערכות. ניתוח רגישות מגלה
  עד כמה הנחה שגויה יכולה לשנות את המסקנה ממתן אשראי לדחייתו.
</div>

<!-- ===== סעיף 2 — משתני מפתח ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. משתני המפתח לרגישות בנדל"ן מניב</h3>

<p>
  בנדל&quot;ן מניב, ארבעת המשתנים הקריטיים לניתוח רגישות הם:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">משתנה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שינוי בסיסי לבדיקה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">השפעה אופיינית על DSCR</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיעור פנויות (Vacancy Rate)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">±5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כל 1% פנויות נוספות מפחית NOI ב-~1%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיעור שכירות (Rental Rate)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">±10%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ירידה של 10% בשכירות = ירידה דומה ב-NOI</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיעור היוון (Cap Rate)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">±0.5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עלייה של 0.5% ב-Cap Rate = ירידת שווי נכס של ~10%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ריבית הלוואה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">±1%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עלייה של 1% בריבית = עלייה משמעותית בשירות החוב</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>דוגמה מספרית — בניין משרדים:</strong>
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>בסיס:</strong> NOI = 3.6 מ' ₪ | שירות חוב = 2.7 מ' ₪ | DSCR = 1.33<br><br>
  <strong>תרחיש רגישות — שיעור פנויות עולה מ-5% ל-10%:</strong><br>
  NOI חדש ≈ 3.6 × 0.95 / 1.05 × 0.90 = 3.43 מ' ₪ (הפשטה: ירידה של ~5% ב-NOI)<br>
  DSCR חדש = 3.43 ÷ 2.7 = <strong>1.27</strong> — עדיין מעל אמת המידה של 1.20<br><br>
  <strong>מסקנה:</strong> הפרויקט עמיד לעלייה של 5% בפנויות, אך שוליית הבטחון אינה גדולה.
</div>

<!-- ===== סעיף 3 — Stress Testing ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. Stress Testing — תרחיש קיצון</h3>

<p>
  בניגוד לניתוח רגישות שמשנה משתנה אחד בכל פעם, <strong>Stress Test</strong> משלב
  מספר שינויים שליליים בו-זמנית — תרחיש הגרוע ביותר הסביר (<em>worst-case plausible</em>).
</p>

<ul style="line-height:1.9;">
  <li>פנויות עולות מ-5% ל-15%</li>
  <li>שיעור השכירות יורד ב-8%</li>
  <li>ריבית ההלוואה עולה ב-1.5% (במקרה של הלוואות משתנות)</li>
  <li>עלויות תפעול עולות ב-5%</li>
</ul>

<p>
  השאלה אינה "האם זה יקרה?" — אלא "אם זה יקרה, האם הלווה ישרוד?"
  בנק ישראל ודירוגי האשראי דורשים Stress Testing כחלק ממסגרת ניהול הסיכונים.
</p>

<!-- ===== סעיף 4 — Break-Even Analysis ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. Break-Even Analysis — נקודת האיזון</h3>

<p>
  <strong>Break-Even Analysis</strong> שואל: <em>מה שיעור הפנויות / ירידת השכירות
  שמביאה את DSCR בדיוק ל-1.0?</em> כלומר — מתי הנכס בדיוק מכסה את שירות החוב, ולא יותר.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  NOI_break-even = שירות חוב שנתי<br>
  שיעור פנויות_break-even = 1 - (NOI_break-even ÷ Potential Gross Income)
</div>

<p>
  <strong>דוגמה:</strong> שירות חוב = 2.7 מ' ₪ | Potential Gross Income = 4.0 מ' ₪ |
  הוצאות תפעול = 0.4 מ' ₪
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  NOI_break-even = 2.7 + 0.4 = 3.1 מ' ₪<br>
  שיעור פנויות_break-even = 1 - (3.1 ÷ 4.0) = <strong>22.5%</strong><br><br>
  פרשנות: הנכס יכול לספוג פנויות של עד 22.5% לפני שה-DSCR יירד מ-1.0.
  אם שיעור הפנויות הנוכחי הוא 5%, שוליית הבטחון היא 17.5 נקודות אחוז.
</div>

<!-- ===== סעיף 5 — מינוף ותשואה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. מינוף ותשואה — חרב פיפיות</h3>

<p>
  <strong>מינוף (Leverage)</strong> מגביר הן את רווחי המשקיע והן את הפסדיו.
  זוהי "חרב פיפיות": כאשר שווי הנכס עולה, המינוף מאיץ את התשואה על ההון;
  כאשר שווי הנכס יורד — המינוף מאיץ את שחיקת ההון.
</p>

<p>
  <strong>דוגמה מספרית:</strong>
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תרחיש</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">ללא מינוף (100% הון)</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">עם מינוף (60% חוב)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">שווי נכס</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">10 מ' ₪</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">10 מ' ₪</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">הון עצמי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">10 מ' ₪</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">4 מ' ₪</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">0</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">6 מ' ₪</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;color:#2e7d32;">שווי עולה ב-20% → 12 מ'</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשואת הון: 20%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תשואת הון: 50%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;color:#c62828;">שווי יורד ב-20% → 8 מ'</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הפסד הון: 20%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;color:#c62828;">הפסד הון: 50%</td>
    </tr>
  </tbody>
</table>

<p>
  לאנליסט האשראי: מינוף גבוה מגדיל את הסיכון ללווה <em>ולמלווה</em>. ירידת שווי
  קטנה יחסית עלולה למחוק את כל ההון העצמי של הלווה, ולהשאיר את המלווה
  עם נכס ששוויו מתחת לחוב (Negative Equity).
</p>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  אנליסט שלא מריץ ניתוח רגישות לפני המלצתו — לא סיים את עבודתו.
  מספר אחד (DSCR = 1.35) אינו ניתוח — הוא תמונה סטטית של נקודת זמן אחת.
  ניתוח רגישות מגלה את <em>עמידות</em> אותו DSCR תחת תנאי לחץ.
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של ניתוח רגישות, Stress Testing, Break-Even Analysis "
    "והשפעת המינוף על תשואת ההון. "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים בניית טבלת רגישות DSCR לפי שינויי פנויות ושכירות, "
    "חישוב נקודת Break-Even לנכס מניב נתון, והשוואת תשואת הון עם ובלי מינוף. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — ניתוח רגישות ומינוף
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>ניתוח רגישות בוחן מה קורה למדד פיננסי כאשר הנחה אחת משתנה.</strong>
    הוא חושף את שוליית הבטחון ומגלה אילו הנחות "שוברות" את העסקה.
  </li>
  <li>
    <strong>ארבעת המשתנים הקריטיים: פנויות, שכירות, Cap Rate, ריבית.</strong>
    בכל ניתוח נדל"ן מניב — יש לבדוק את ארבעתם.
  </li>
  <li>
    <strong>Stress Test משלב מספר שינויים שליליים בו-זמנית.</strong>
    השאלה אינה "האם זה יקרה?" אלא "האם הפרויקט שורד אם זה יקרה?"
  </li>
  <li>
    <strong>Break-Even Analysis מגלה את שיעור הפנויות / ירידת השכירות שמביאה DSCR ל-1.0.</strong>
    כל DSCR מוצג חייב להיות מלווה בנקודת האיזון שלו.
  </li>
  <li>
    <strong>מינוף מגביר תשואות — אך גם הפסדים.</strong>
    ירידת שווי של 20% עם LTV של 60% עלולה למחוק 50% מההון העצמי.
  </li>
</ol>

<h3 style="color:#1a2638;margin-top:24px;">מילון מונחים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">עברית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">אנגלית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח רגישות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Sensitivity Analysis</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בחינת שינוי במדד כאשר הנחה משתנה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תרחיש קיצון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Stress Test</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדיקת עמידות בתנאי שוק קשים ומשולבים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נקודת איזון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Break-Even Point</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הרמה שבה הכנסות = הוצאות (DSCR=1.0)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שוליית בטחון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Margin of Safety</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מרחק בין ביצועי הנכס לנקודת הכשל</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיעור פנויות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Vacancy Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אחוז שטח הנכס שאינו מושכר</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מינוף שלילי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Negative Leverage</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כאשר עלות החוב גבוהה מתשואת הנכס</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — אמות מידה פיננסיות — Covenants
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  אמות מידה פיננסיות — Covenants
</h2>

<!-- ===== סעיף 1 — מהן אמות מידה פיננסיות ===== -->
<h3 style="color:#1a2638;">1. מהן אמות מידה פיננסיות?</h3>

<p>
  <strong>אמות מידה פיננסיות (Financial Covenants)</strong> הן תנאים חוזיים מדידים
  הכלולים בהסכם ההלוואה, שהלווה מתחייב לעמוד בהם לאורך כל תקופת ההלוואה.
  הפרת Covenant היא <strong>אירוע כשל טכני (Technical Default)</strong> — ואם לא
  מטופל, הופך לאירוע כשל מלא המעניק למלווה זכות לדרוש פירעון מיידי.
</p>

<p>
  Covenants הם כלי בקרה: הם מאפשרים למלווה לזהות הרעה בביצועי הלווה
  <em>לפני</em> שהיא הופכת לבעיה בלתי ניתנת לפתרון. כאשר DSCR מתחיל לרדת,
  ה-Covenant "מתריע" מוקדם — ומאפשר שיחת ניהול.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אנלוגיה:</strong> Covenants הם כמו אזעקת אש — הם לא מונעים את השריפה,
  אך הם מתריעים על מנת לאפשר פינוי בטרם יהיה מאוחר מדי.
</div>

<!-- ===== סעיף 2 — סוגי Covenants ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. סוגי Covenants עיקריים בנדל"ן</h3>

<p>
  בהסכמי הלוואות נדל&quot;ן בישראל, ארבעה Covenants נפוצים במיוחד:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">Covenant</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סף מינימלי / מקסימלי טיפוסי</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">משמעות</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">DSCR Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">≥ 1.20</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI חייב לכסות שירות חוב פי 1.20 לפחות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">LTV Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">≤ 75%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">יחס ההלוואה לשווי הנכס לא יחרוג מ-75%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ICR (Interest Coverage Ratio)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">≥ 1.50</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">EBITDA חייב לכסות הוצאות ריבית פי 1.50 לפחות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">יתרת מזומן מינימלית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מוגדר בהסכם (לדוגמה: 2 מ' ₪)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלווה חייב לשמור על "כרית" נזילות מינימלית</td>
    </tr>
  </tbody>
</table>

<p>
  חשוב: הסף המוגדר בהסכם הוא לא בהכרח אותו סף שאנליסט האשראי מחשיב כ"בריא".
  DSCR Covenant של 1.20 פירושו שהמלווה <em>מתחיל לאכוף</em> בנקודה זו — אך
  בניתוח הפנימי, DSCR מתחת ל-1.35 כבר מדליק נורה כתומה.
</p>

<!-- ===== סעיף 3 — Maintenance vs Incurrence ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. Maintenance לעומת Incurrence Covenants</h3>

<p>
  שני סוגים עיקריים של Covenants, הנבדלים בזמן הפעלתם:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מתי נבדק?</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דוגמה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Maintenance Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תקופתית — רבעונית / חצי-שנתית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR ≥ 1.20 בכל תאריך דיווח</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Incurrence Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רק כאשר הלווה נוקט פעולה ספציפית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR ≥ 1.25 לפני נטילת חוב נוסף</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>Maintenance Covenants</strong> — נפוצים יותר בהלוואות נדל&quot;ן —
  מחייבים ציות <em>מתמיד</em>, ללא קשר לפעולות הלווה. הם מגנים על המלווה
  מפני הרעה אטית ומתמשכת בביצועי הנכס.
</p>

<p>
  <strong>Incurrence Covenants</strong> — נפוצים יותר בשוק אגרות החוב (High Yield Bonds) —
  מופעלים רק כאשר הלווה מבקש לבצע פעולה כמו גיוס חוב נוסף, חלוקת דיבידנד,
  או רכישת נכס חדש. הם מגבילים פעולות — לא מצבים.
</p>

<!-- ===== סעיף 4 — תהליך ניטור ודיווח ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. תהליך ניטור ודיווח</h3>

<p>
  מחזור הניטור של Covenants בהלוואות נדל&quot;ן ישראליות בנוי בדרך כלל כך:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>תדירות דיווח:</strong> רבעונית לגבי מדדי נזילות; חצי-שנתית לגבי DSCR ו-LTV.
    חלק מהבנקים דורשים בדיקת DSCR שנתית בלבד לנכסים מניבים יציבים.
  </li>
  <li>
    <strong>אישור הלווה (Compliance Certificate):</strong> הלווה מגיש מסמך חתום
    על-ידי מנכ"ל או CFO המצהיר על ציות. האנליסט בוחן ומאמת מול הדוחות.
  </li>
  <li>
    <strong>דוחות מבוקרים לעומת דוחות ניהוליים:</strong> לניטור רבעוני מאפשרים
    לעתים דוחות ניהוליים (Management Accounts); לבדיקה שנתית נדרשים דוחות מבוקרים.
  </li>
  <li>
    <strong>הערכת שמאי עצמאי:</strong> לבדיקת LTV — נדרשת הערכת שמאי מוסמך, בדרך כלל
    אחת לשנה או עם כל שינוי מהותי בנכס.
  </li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  לוח זמנים טיפוסי לבדיקת Covenants בהלוואת ליווי:<br><br>
  מרץ  — דיווח Q4 + שנתי (דוחות מבוקרים + הערכת שמאי)<br>
  יוני  — דיווח Q1 (דוחות ניהוליים)<br>
  ספטמבר — דיווח H1 (דוחות ביניים + שמאי אם נדרש)<br>
  דצמבר — דיווח Q3 (דוחות ניהוליים)
</div>

<!-- ===== סעיף 5 — Breach וה-Waiver Process ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. Breach וה-Waiver Process</h3>

<p>
  כאשר לווה מפר Covenant — מה קורה בפועל? בניגוד לדמיון הפופולרי, הבנק לא
  ממהר לממש את השעבוד. בפרקטיקה הישראלית מתנהל תהליך מובנה:
</p>

<ol style="line-height:1.9;">
  <li>
    <strong>Technical Default:</strong> הפרת ה-Covenant מוגדרת רשמית כאירוע כשל טכני.
    הלווה מקבל הודעה פורמלית מהבנק.
  </li>
  <li>
    <strong>Cure Period — תקופת ריפוי:</strong> בדרך כלל 30–60 יום בהם הלווה
    יכול לתקן את ההפרה (לדוגמה — הזרמת הון עצמי להחזרת DSCR מעל הסף).
  </li>
  <li>
    <strong>ניהול משא ומתן — Waiver:</strong> אם תיקון אינו אפשרי, הלווה מבקש
    <strong>Waiver</strong> — ויתור חד-פעמי של המלווה על ההפרה. זה כולל בדרך כלל
    עמלת Waiver (0.1%–0.5% מהחוב) ולעתים הידוק תנאי ה-Covenant קדימה.
  </li>
  <li>
    <strong>Covenant Reset / Amendment:</strong> אם ברור שהביצועים השתנו מבנית,
    מנהלים מחדש את כל ה-Covenants. זה דורש הסכמה כתובה ולעתים אישור ועדת האשראי.
  </li>
  <li>
    <strong>Acceleration (במקרה קיצון):</strong> אם המצב חמור ואין הסכמה —
    המלווה מפעיל סעיף האצה ודורש פירעון מוקדם מלא.
  </li>
</ol>

<p>
  בפרקטיקה הישראלית, Acceleration בשוק הנדל&quot;ן מתרחש לעתים נדירות יחסית —
  מכיוון שהוא מזיק לשני הצדדים. בדרך כלל מגיעים להסדר.
</p>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  הפרת Covenant היא אירוע אשראי — גם אם ההלוואה נפרעת בזמן.
  יש לעקוב אחר ציות בכל תקופת דיווח. אנליסט שמגלה הפרת Covenant
  באיחור של שני רבעונים — כשל בתפקידו. מעקב שיטתי אחר ציות הוא
  חלק בלתי נפרד מניהול התיק.
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של סוגי Covenants, תהליך הניטור, ה-Waiver Process "
    "וההבדל בין Maintenance ל-Incurrence Covenants. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים בדיקת ציות לפי נתוני נכס נתונים, "
    "זיהוי Covenant המופר בתרחיש נתון, וניסוח מכתב Waiver Request בסיסי. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — אמות מידה פיננסיות (Covenants)
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>Covenant הוא תנאי חוזי — הפרתו היא אירוע כשל, גם ללא אי-פירעון.</strong>
    DSCR מתחת לסף שהוסכם הוא כשל טכני, גם אם הלווה שילם כל תשלום בזמן.
  </li>
  <li>
    <strong>ארבעת ה-Covenants המרכזיים: DSCR ≥ 1.20, LTV ≤ 75%, ICR ≥ 1.50, יתרת מזומן מינימלית.</strong>
    בכל ניתוח נדל"ן — יש לזהות ולנטר את כולם.
  </li>
  <li>
    <strong>Maintenance Covenant נבדק תקופתית; Incurrence Covenant מופעל עם פעולה ספציפית.</strong>
    בהלוואות נדל"ן, Maintenance הוא הנפוץ — הוא מגן על המלווה מפני הרעה מתמשכת.
  </li>
  <li>
    <strong>Breach → Cure Period → Waiver → Amendment → Acceleration.</strong>
    הבנת שלבי ה-Waiver Process קריטית לאנליסט המנהל תיק הלוואות פעיל.
  </li>
  <li>
    <strong>מעקב אחר ציות הוא אחריות שוטפת — לא רק בעת מתן האשראי.</strong>
    אנליסט שמגלה הפרה באיחור של שני רבעונים כשל בתפקידו.
  </li>
</ol>

<h3 style="color:#1a2638;margin-top:24px;">מילון מונחים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">עברית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">אנגלית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אמת מידה פיננסית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Financial Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תנאי חוזי מדיד בהסכם הלוואה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">כשל טכני</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Technical Default</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הפרת תנאי חוזי שאינה אי-פירעון</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ויתור</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Waiver</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הסכמת המלווה לא לאכוף הפרה ספציפית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">האצת פירעון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Acceleration</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דרישת פירעון מיידי מלא בעקבות כשל</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תקופת ריפוי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cure Period</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פרק הזמן לתיקון ההפרה לפני אכיפה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תעודת ציות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Compliance Certificate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אישור חתום של הלווה על עמידה בתנאים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">יחס כיסוי ריבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ICR — Interest Coverage Ratio</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">EBITDA ÷ הוצאות ריבית</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לבחינה הסופית:</strong><br>
  השלמתם את שישת מודולי קורס 4 — מדדים פיננסיים בנדל&quot;ן. למדתם לחשב
  ולפרש NOI, Cap Rate ו-DSCR, לנתח IRR ו-Equity Multiple, לבצע ניתוח רגישות
  ולהבין את מנגנון ה-Covenants.<br><br>
  הבחינה הסופית תכלול שאלות חישוב על מדדי תשואה, ניתוח רגישות של DSCR,
  וזיהוי הפרות Covenant בתרחיש נתון. הגיעו עם הכלים שרכשתם — ובהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": 'IRR ו-Equity Multiple',
        "slug": "irr-equity-multiple",
        "estimated_minutes": 55,
        "components": [
            {
                "component_type": ComponentType.READING,
                "order": 1,
                "body_html_he": M4_READING_HTML,
                "instructions_he": "",
            },
            {
                "component_type": ComponentType.COMPREHENSION,
                "order": 2,
                "body_html_he": "",
                "instructions_he": M4_COMPREHENSION_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.EXERCISES,
                "order": 3,
                "body_html_he": "",
                "instructions_he": M4_EXERCISES_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.SUMMARY,
                "order": 4,
                "body_html_he": M4_SUMMARY_HTML,
                "instructions_he": "",
            },
        ],
    },
    {
        "module_number": 5,
        "title_he": "ניתוח רגישות ומינוף",
        "slug": "nituach-rigishut-minuf",
        "estimated_minutes": 50,
        "components": [
            {
                "component_type": ComponentType.READING,
                "order": 1,
                "body_html_he": M5_READING_HTML,
                "instructions_he": "",
            },
            {
                "component_type": ComponentType.COMPREHENSION,
                "order": 2,
                "body_html_he": "",
                "instructions_he": M5_COMPREHENSION_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.EXERCISES,
                "order": 3,
                "body_html_he": "",
                "instructions_he": M5_EXERCISES_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.SUMMARY,
                "order": 4,
                "body_html_he": M5_SUMMARY_HTML,
                "instructions_he": "",
            },
        ],
    },
    {
        "module_number": 6,
        "title_he": 'אמות מידה פיננסיות — Covenants',
        "slug": "amot-mida-finansiot",
        "estimated_minutes": 45,
        "components": [
            {
                "component_type": ComponentType.READING,
                "order": 1,
                "body_html_he": M6_READING_HTML,
                "instructions_he": "",
            },
            {
                "component_type": ComponentType.COMPREHENSION,
                "order": 2,
                "body_html_he": "",
                "instructions_he": M6_COMPREHENSION_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.EXERCISES,
                "order": 3,
                "body_html_he": "",
                "instructions_he": M6_EXERCISES_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.SUMMARY,
                "order": 4,
                "body_html_he": M6_SUMMARY_HTML,
                "instructions_he": "",
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed Course 4, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=4)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 4 not found. Run 'python manage.py seed_data' first."
                )
            )
            return

        self.stdout.write(
            self.style.HTTP_INFO(f"Seeding modules for: {course}")
        )

        for mod_data in MODULES:
            module, mod_created = Module.objects.update_or_create(
                course=course,
                module_number=mod_data["module_number"],
                defaults={
                    "title_he": mod_data["title_he"],
                    "slug": mod_data["slug"],
                    "estimated_minutes": mod_data["estimated_minutes"],
                },
            )
            action = "CREATED" if mod_created else "UPDATED"
            self.stdout.write(
                f"  [{action}] Module {mod_data['module_number']}: {mod_data['title_he']}"
            )

            for comp_data in mod_data["components"]:
                component, comp_created = ModuleComponent.objects.update_or_create(
                    module=module,
                    order=comp_data["order"],
                    defaults={
                        "component_type": comp_data["component_type"],
                        "body_html_he": comp_data["body_html_he"],
                        "instructions_he": comp_data["instructions_he"],
                    },
                )
                comp_action = "CREATED" if comp_created else "UPDATED"
                self.stdout.write(
                    f"    [{comp_action}] order={comp_data['order']} "
                    f"type={comp_data['component_type']}"
                )

        self.stdout.write(self.style.SUCCESS("\nDone. Modules 4, 5, and 6 seeded successfully."))
