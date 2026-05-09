"""
Management command: seed_c03_content
Seeds Module 1-3 content for Course 3 (ניתוח דוחות כספיים — יזמי נדל"ן וקבוצות יזמיות).

Usage:
    python manage.py seed_c03_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": "מתודולוגיה לניתוח דוחות",
        "slug": "metodologya-lnituach-dochot",
        "estimated_minutes": 50,
    },
    {
        "module_number": 2,
        "title_he": "יחסים פיננסיים",
        "slug": "yahasim-finansiim",
        "estimated_minutes": 55,
    },
    {
        "module_number": 3,
        "title_he": "ניתוח יזם נדל\"ן",
        "slug": "nituach-yazam-nadlan",
        "estimated_minutes": 55,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>מתודולוגיה לניתוח דוחות כספיים — 6 שלבים</h2>

<p>
ניתוח דוחות כספיים הוא מיומנות מבנית: יש לבצע אותה לפי סדר קבוע, שלב אחר שלב.
אנליסטים מנוסים שבנו שגרת עבודה עקבית לעולם אינם מדלגים על שלבים — ולו מכיוון
שכל שלב מספק ה<em>קשר</em> שמאפשר לפרש נכון את השלב הבא.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — לעולם אל תתחיל ביחסים!</strong><br>
  הטעות הנפוצה ביותר של אנליסטים מתחילים היא לפתוח את הדוח ישר בחישוב יחסים.
  יחס חוב-להון של 3.0 יכול להיות מצוין (חברת נדל"ן מניב מבוססת) או קטסטרופלי
  (סטארטאפ שירותים). ללא הקשר ענפי — כל יחס חסר משמעות.
</div>

<h3>שלב 1 — הקשר ענפי (Industry Context)</h3>
<p>
לפני שנוגעים במספר אחד, יש לשאול: <strong>באיזה ענף פועלת החברה?</strong> לכל ענף
מאפיינים ייחודיים: מרווחים, מבנה הון, מחזורי עסקים, רגישות לריבית ולאינפלציה.
בנדל"ן ישראלי, מבחינים בין מספר קטגוריות עיקריות:
</p>
<ul>
  <li><strong>נדל"ן מניב (Income-Producing Real Estate):</strong> הכנסות שכירות יציבות, מינוף גבוה, חשיפה לריבית.</li>
  <li><strong>ייזום (Real Estate Development):</strong> הכנסות תנודתיות, עונות, תלויות בהתקדמות פרויקטים.</li>
  <li><strong>קבוצות יזמיות (Developer Groups):</strong> שילוב של מניב וייזום, לעיתים עם פעילות בחו"ל.</li>
  <li><strong>תשתיות ולוגיסטיקה:</strong> מאפיינים שונים לחלוטין — חוזים ארוכים, תשואות נמוכות ויציבות.</li>
</ul>

<h3>שלב 2 — מבנה הדוחות ומודל עסקי</h3>
<p>
עיין בדוח השנתי כמסמך שלם: מכתב למשקיעים, תיאור פעילות, דוח הדירקטוריון, ביאורים.
<strong>הבן את מודל ההכנסות</strong>: כיצד החברה מרוויחה? האם ההכנסות חוזרות (שכירות)
או אירועיות (מכירות פרויקט)? האם יש מגוון? ריכוז לקוחות?
</p>

<p>
בדוק את <strong>מבנה הקבוצה</strong>: האם החברה פועלת דרך חברות בנות, SPV (חברות ייעודיות),
שותפויות? מבנה מסועף מחייב ניתוח מאוחד (Consolidated) — וגם ניתוח נפרד של מרכיבים.
</p>

<h3>שלב 3 — חישוב כל היחסים המרכזיים</h3>
<p>
לאחר שהקשר ברור, מחשבים את כל קטגוריות היחסים: נזילות, רווחיות, יעילות, מינוף
ושירות חוב. נפרט אותם לעומק במודול 2 — בשלב זה חשוב שלא לדלג על אף קטגוריה.
</p>

<h3>שלב 4 — ניתוח מגמות (Horizontal Analysis)</h3>
<p>
<strong>ניתוח אופקי (Horizontal Analysis)</strong> בוחן שינויים לאורך זמן — בדרך כלל
השוואה ל-3 שנים אחרונות. לכל שורה בדוח מחשבים שינוי אחוזי משנה לשנה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
שינוי % = (ערך שנה נוכחית − ערך שנה קודמת) ÷ ערך שנה קודמת × 100
</div>

<p>
מה נחשב "נורמלי"? תלוי בענף ובמצב השוק. בשוק עולה: צמיחת הכנסות שכירות של 3%-8%
לשנה — סביר. צמיחה של 40% — מחייבת הסבר (רכישת נכס? הצמדה למדד?). ירידה של
10% בהכנסות בשוק עולה — אלארם.
</p>

<h3>שלב 5 — זיהוי דגלים אדומים (Red Flags)</h3>
<p>
אנליסט טוב מחפש אנומליות: מה <em>אינו</em> מתאים לסיפור שהחברה מספרת? רשימת
הדגלים האדומים הנפוצים:
</p>
<ul>
  <li>הכנסות גדלות אך תזרים מפעילות שוטפת יורד — ניפוח הכנסות?</li>
  <li>ימי לקוחות (Days Receivable) גדלים — בעיית גבייה?</li>
  <li>חוב עולה מהר מ-EBITDA — ירידה ביכולת שירות חוב.</li>
  <li>רווח גבוה מ-EBITDA — חשד לרווחים לא-תפעוליים (שערוכים, מכירות נכסים).</li>
  <li>שינוי מדיניות חשבונאית — מחייב בדיקה של ההשפעה הכמותית.</li>
  <li>הסתייגות רואה חשבון — ראה פרק על איכות הביקורת בהמשך.</li>
</ul>

<h3>שלב 6 — סינתזה וכתיבת מסקנה</h3>
<p>
הסינתזה היא השלב שמבדיל בין אנליסט לבין מחשבון. לאחר שאספנו את כל הנתונים,
שאלות הסינתזה הן: <strong>מהי אוכלוסיית הסיכונים המרכזית? מהי יכולת ההחזר?
מה התרחיש שבו ההלוואה לא מוחזרת?</strong>
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — אנליסט שדילג על שלב 1:</strong><br><br>
  אנליסט ניתח חברת בנייה וחישב יחס חוב-להון של 2.8 — ומיד דאג. לאחר שמנהל הצוות
  שאל "באיזה ענף?" — התברר שמדובר בחברת נדל"ן מניב מבוססת עם 95% תפוסה וחוזי
  שכירות ל-7 שנים. יחס 2.8 ב-Income REIT הוא שגרתי לחלוטין. ללא הקשר ענפי,
  הניתוח כולו היה מוטעה.
</div>

<h2>ניתוח אנכי (Vertical Analysis)</h2>

<p>
<strong>ניתוח אנכי (Vertical Analysis)</strong> מציג כל סעיף בדוח כאחוז מבסיס קבוע:
</p>
<ul>
  <li>בדוח רווח והפסד — כל שורה מחולקת ב<strong>הכנסות הכוללות</strong>.</li>
  <li>במאזן — כל שורה מחולקת ב<strong>סך הנכסים</strong>.</li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ניתוח אנכי P&L: % שורה = ערך שורה ÷ הכנסות כוללות × 100<br>
ניתוח אנכי מאזן: % שורה = ערך שורה ÷ סך נכסים × 100
</div>

<h3>דוגמה — ניתוח אנכי של P&L ומאזן</h3>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוח רווח והפסד — "נהר נדל"ן בע"מ" — ניתוח אנכי (שנת 2024)</strong><br><br>

  <table style="border-collapse:collapse;width:100%;margin:12px 0;">
    <thead>
      <tr style="background:#1a2638;color:#fff;">
        <th style="padding:9px;text-align:right;border:1px solid #ccc;">סעיף</th>
        <th style="padding:9px;text-align:right;border:1px solid #ccc;">אלפי ש"ח</th>
        <th style="padding:9px;text-align:right;border:1px solid #ccc;">% מהכנסות</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>הכנסות</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>60,000</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>100.0%</strong></td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">עלות המכר / עלויות ישירות</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">(42,000)</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">70.0%</td>
      </tr>
      <tr>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>רווח גולמי</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>18,000</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>30.0%</strong></td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">הוצאות תפעוליות</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">(4,800)</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">8.0%</td>
      </tr>
      <tr>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">פחת והפחתות</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">(1,800)</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">3.0%</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>EBIT</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>11,400</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>19.0%</strong></td>
      </tr>
      <tr>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>EBITDA</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>13,200</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>22.0%</strong></td>
      </tr>
    </tbody>
  </table>

  <strong>מאזן — ניתוח אנכי (% מסך נכסים = 300,000 אלפי ש"ח)</strong><br><br>

  <table style="border-collapse:collapse;width:100%;margin:12px 0;">
    <thead>
      <tr style="background:#1a2638;color:#fff;">
        <th style="padding:9px;text-align:right;border:1px solid #ccc;">סעיף</th>
        <th style="padding:9px;text-align:right;border:1px solid #ccc;">אלפי ש"ח</th>
        <th style="padding:9px;text-align:right;border:1px solid #ccc;">% מסך נכסים</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">מזומן ושווי מזומן</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">15,000</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">5.0%</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">לקוחות וחייבים</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">9,000</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">3.0%</td>
      </tr>
      <tr>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">מלאי דירות בפיתוח</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">66,000</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">22.0%</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">נדל"ן להשקעה (IAS 40)</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">195,000</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">65.0%</td>
      </tr>
      <tr>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">נכסים אחרים</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">15,000</td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;">5.0%</td>
      </tr>
      <tr style="background:#e8f5e9;">
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>סך נכסים</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>300,000</strong></td>
        <td style="padding:8px;border:1px solid #ddd;text-align:right;"><strong>100.0%</strong></td>
      </tr>
    </tbody>
  </table>

  <strong>אנומליה שהניתוח האנכי חושף:</strong> 65% מהנכסים הם נדל"ן להשקעה — אם החברה
  מדווחת לפי מודל שווי הוגן (IAS 40), שינוי של 10% בשווי הנכסים יוצר תנועה של
  19,500 אלפי ש"ח בדוח הרווח — יותר מ-EBIT השנתי כולו!
</div>

<h2>ניתוח אופקי (Horizontal Analysis)</h2>

<p>
<strong>ניתוח אופקי (Horizontal Analysis)</strong> עוקב אחר שינויים לאורך זמן — ההשוואה
הקלאסית היא 3 שנים: T-2, T-1, T (השנה). לכל שורה:
</p>
<ul>
  <li>שינוי מוחלט: T − T-1</li>
  <li>שינוי יחסי: (T − T-1) ÷ T-1 × 100%</li>
</ul>

<p>
<strong>מה נורמלי, מה דגל אדום:</strong>
</p>
<ul>
  <li>צמיחת הכנסות של 5%–15% בשוק עולה: נורמלי.</li>
  <li>עלויות גדלות מהר מהכנסות 3 שנים ברציפות: דחיסת מרווחים — בדוק מדוע.</li>
  <li>קפיצה חד-פעמית ברווח (שנה אחת) שאינה חוזרת: סביר שיש פריט חד-פעמי.</li>
  <li>ירידת EBITDA בשנה שבה הכנסות גדלו: ניפוח הכנסות? עלויות נסתרות?</li>
</ul>

<h2>בחירת בנצ'מארק (Benchmark Selection)</h2>

<p>
יחס פיננסי חסר ערך ללא ייחוס — עם מה משווים? שלוש גישות:
</p>

<h3>(א) בנצ'מארק ענפי (Industry Benchmark)</h3>
<p>
השוואה לממוצע חברות דומות בענף. המקור: דוחות ציבוריים של חברות נסחרות, פרסומי
הבורסה, נתוני לשכת המסחר. <strong>מגבלה:</strong> הגדרת "ענף" רחבה מדי — חברת ייזום
ישראלית ממוצעת שונה מאוד מחברת מניב.
</p>

<h3>(ב) בנצ'מארק אסטרטגי (Aspirational Benchmark)</h3>
<p>
השוואה לחברה המובילה בענף שאליה מכוונים. בנדל"ן המניב הישראלי: אמות השקעות,
גב-ים, מליסרון. <strong>שאלת מפתח:</strong> האם הפער מוסבר ומצדיק עצמו — או שמדובר
בחברה שמנסה להתנהג כמו הגדולות מבלי שיש לה הבסיס?
</p>

<h3>(ג) בנצ'מארק עצמי (Self-Benchmark)</h3>
<p>
השוואת החברה לעצמה לאורך זמן — 3–5 שנים אחורה. הכי אמין לזיהוי מגמות.
<strong>שאלת מפתח:</strong> האם המרווחים משתפרים, יציבים, או נשחקים? האם מינוף עולה?
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל חשוב — שלב הבנצ'מארק:</strong><br>
  השתמשו בשלוש הגישות יחד. ענפי מספק הקשר; אסטרטגי מספק שאיפה; עצמי מספק מגמה.
  כשהשלושה מצביעים לאותה כיוון — הממצא חזק. כשהם סותרים — יש לחקור למה.
</div>

<h2>איכות הביקורת</h2>

<p>
לא כל חוות דעת רואה חשבון שוות ערך. אנליסט מקצועי בוחן:
</p>

<h3>Big 4 לעומת משרדים קטנים</h3>
<p>
חברות הנסחרות בבורסה הישראלית מבוקרות בדרך כלל על-ידי אחת מחברות ה-Big 4:
Deloitte, PwC, EY, KPMG (הנמצאות בישראל תחת שמות מקומיים). ביקורת Big 4 מוסיפה
אמינות אך אינה ערובה — גם Big 4 הוציאו חוות דעת נקיות על חברות שקרסו.
</p>

<h3>חוות דעת עם הסתייגות (Qualified Opinion)</h3>
<p>
<strong>הסתייגות (Qualified Opinion)</strong> מופיעה כאשר רואה החשבון מסכים עם רוב הדוח
אך יש נושאים מוגבלים שאינו יכול לאמת, או שאינו מסכים עם מדיניות חשבונאית ספציפית.
</p>

<h3>הערת עסק חי (Going Concern)</h3>
<p>
<strong>הערת עסק חי (Going Concern Note)</strong> היא הסתייגות הכי חמורה — רואה החשבון
מביע ספק ביכולת החברה להמשיך לפעול ל-12 חודשים. זוהי <strong>תקייה אדומה אוטומטית</strong>:
אנליסט שמקבל דוח עם הערת עסק חי לא יכול להמשיך בניתוח רגיל מבלי לשאול תחילה
"האם זה עדיין עסק חי, ומה השתנה?"
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — Going Concern:</strong><br>
  אל תמשיך בניתוח יחסים סטנדרטי לחברה שקיבלה הערת עסק חי. כל הנחות השווי שונות
  כשהחברה פועלת בתנאי חיסול. פנה קודם לנהל הצוות ודון בהיתכנות המשך הניתוח.
</div>

<h2>טבלת ביצועי P&L — יזמי נדל"ן ישראליים</h2>

<p>
כדי להעריך האם מרווחי החברה הנבחנת "נורמליים", הלן ספים מקובלים לניתוח אנכי:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מדד</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">טווח נורמלי — יזמי נדל"ן ישראלי</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הערה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מרווח גולמי (Gross Margin)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">20%–35%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תלוי מיקום, סוג פרויקט, שנת קרקע</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מרווח EBITDA</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">15%–25%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לאחר ניטרול שערוכי IAS 40</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מרווח EBIT</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">12%–20%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כולל פחת תפעולי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מרווח נקי (Net Margin)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">8%–15%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תנודתי בגלל מימון ושערוכים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הוצאות הנה"כ כ-% מהכנסות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3%–8%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מעל 10% — אות להוצאות נסתרות</td>
    </tr>
  </tbody>
</table>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — מתודולוגיה לניתוח דוחות</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>6 שלבי הניתוח:</strong> (1) הקשר ענפי, (2) מבנה הדוחות ומודל עסקי,
    (3) חישוב יחסים, (4) ניתוח מגמות, (5) זיהוי דגלים אדומים, (6) סינתזה ומסקנה.
    אין לדלג על שלבים — כל שלב מאפשר לפרש נכון את הבא.
  </li>
  <li>
    <strong>ניתוח אנכי:</strong> כל שורה כאחוז מהכנסות (P&L) או מסך נכסים (מאזן).
    חושף אנומליות מיידית — שורה שגדלה לא-פרופורציונלית ביחס לבסיס.
  </li>
  <li>
    <strong>ניתוח אופקי:</strong> שינוי % שנתי לכל שורה על פני 3 שנים. מגלה מגמות
    ארוכות-טווח שאינן גלויות בשנה בודדת.
  </li>
  <li>
    <strong>בנצ'מארק:</strong> ענפי (הקשר), אסטרטגי (שאיפה), עצמי (מגמה). השתמשו
    בשלושתם — כל אחד מוסיף ממד שונה.
  </li>
  <li>
    <strong>איכות ביקורת:</strong> הסתייגות רואה חשבון — דגל צהוב. הערת עסק חי —
    דגל אדום אוטומטי. לעולם אל תתחיל בניתוח יחסים לפני שעיינת בחוות הדעת.
  </li>
</ol>

<h3>מילון מושגים — מודול 1</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מונח בעברית</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">English Term</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח אנכי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Vertical Analysis</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כל שורה כאחוז מהכנסות / מסך נכסים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח אופקי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Horizontal Analysis</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שינוי % שנה-על-שנה לכל שורה</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בנצ'מארק</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Benchmark</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נקודת ייחוס להשוואת ביצועים (ענפי/אסטרטגי/עצמי)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הסתייגות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Qualified Opinion</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חוות דעת רואה חשבון עם סייגים ספציפיים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עסק חי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Going Concern</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הנחת המשכיות פעילות ל-12 חודשים לפחות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח דוחות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Financial Statement Analysis</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תהליך מובנה לחילוץ מסקנות מדוחות כספיים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מגמה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Trend</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כיוון שינוי עקבי לאורך מספר תקופות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סינתזה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Synthesis</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">איחוד כל הממצאים למסקנה מקצועית אחת</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
במודול זה בנינו את מסגרת המתודולוגיה — שלב 3 (חישוב יחסים) הוזכר אך לא פורט.
<em>מודול 2</em> ייצלל לעומק לתוך <strong>יחסים פיננסיים</strong>: נזילות, רווחיות,
יעילות, מינוף ושירות חוב — עם דוגמאות מחושבות מחברות נדל"ן ישראליות.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>יחסים פיננסיים — ארבע הקטגוריות המרכזיות</h2>

<p>
יחסים פיננסיים הם הכלי הכמותי של אנליסט האשראי. הם מאפשרים להפוך מספרים מוחלטים
לנקודות השוואה — בין חברות, בין תקופות, בין ענפים. ארבע קטגוריות עיקריות:
יחסי נזילות, רווחיות, יעילות, מינוף ושירות חוב.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — יחסים ללא הקשר הם חסרי ערך!</strong><br>
  D/E של 3.0 הוא שגרתי עבור חברת נדל"ן מניב ישראלית עם נכסים מניבים ויציבים.
  אותו יחס הוא אלארם אדום עבור חברת שירותים עם הכנסות תנודתיות. לעולם ציין
  לצד כל יחס: מהו הרף המקובל בענף ספציפי זה.
</div>

<h2>יחסי נזילות (Liquidity Ratios)</h2>

<p>
<strong>יחסי נזילות (Liquidity Ratios)</strong> מודדים את יכולת החברה לפרוע
התחייבויות קצרות-טווח מתוך הנכסים השוטפים שלה.
</p>

<h3>יחס שוטף (Current Ratio)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
יחס שוטף = נכסים שוטפים ÷ התחייבויות שוטפות<br>
ספים: מעל 1.5 — בריא; 1.0–1.5 — תשומת לב; מתחת ל-1.0 — אלארם
</div>

<h3>יחס מהיר (Quick Ratio)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
יחס מהיר = (מזומן + שווי מזומן + לקוחות) ÷ התחייבויות שוטפות<br>
מנטרל מלאי — הנכס הפחות נזיל בנכסים השוטפים
</div>

<h3>יחס מזומן (Cash Ratio)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
יחס מזומן = מזומן ושווי מזומן ÷ התחייבויות שוטפות<br>
המחמיר ביותר — רק מזומן אמיתי מול התחייבויות שוטפות
</div>

<h3>ימי הון חוזר</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ימי הון חוזר = הון חוזר ÷ (הכנסות יומיות)<br>
הכנסות יומיות = הכנסות שנתיות ÷ 365
</div>

<p>
ימי הון חוזר חיוביים — החברה מממנת את פעילותה מהון עצמי. שליליים — הספקים
מממנים את פעילות החברה (לעיתים אינדיקציה לכוח מיקוח, לעיתים לבעיית נזילות).
</p>

<h2>יחסי רווחיות (Profitability Ratios)</h2>

<h3>מרווח גולמי, תפעולי ונקי</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
מרווח גולמי = רווח גולמי ÷ הכנסות × 100%<br>
מרווח תפעולי (EBIT Margin) = EBIT ÷ הכנסות × 100%<br>
מרווח נקי = רווח נקי ÷ הכנסות × 100%
</div>

<h3>ROA — תשואה על נכסים</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ROA = רווח נקי ÷ סך נכסים ממוצע × 100%<br>
(ממוצע = (פתיחה + סגירה) ÷ 2)
</div>

<p>
ROA מודד כמה רווח מייצר כל שקל של נכסים. בחברות נדל"ן מניב, ROA נמוך (1%–3%)
הוא נורמלי בגלל בסיס נכסים ענק. בחברות שירות, ROA של 10%–20% נפוץ. ללא
הקשר ענפי — ROA של 2% יכול להיות מצוין או גרוע.
</p>

<h3>ROE — תשואה על הון עצמי</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ROE = רווח נקי ÷ הון עצמי ממוצע × 100%
</div>

<h3>ניתוח DuPont — פירוק ROE</h3>

<p>
<strong>ניתוח DuPont</strong> מפרק את ה-ROE לשלושה גורמים, כל אחד עם פירוש שונה:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ROE = מרווח נקי × מחזור נכסים × מינוף פיננסי<br><br>
ROE = (רווח נקי ÷ הכנסות) × (הכנסות ÷ סך נכסים) × (סך נכסים ÷ הון עצמי)
</div>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — DuPont של "שמר נדל"ן בע"מ":</strong><br><br>
  רווח נקי: 12,000 | הכנסות: 80,000 | סך נכסים: 400,000 | הון עצמי: 100,000<br><br>
  מרווח נקי = 12,000 ÷ 80,000 = <strong>15%</strong><br>
  מחזור נכסים = 80,000 ÷ 400,000 = <strong>0.20</strong><br>
  מינוף פיננסי = 400,000 ÷ 100,000 = <strong>4.0</strong><br><br>
  ROE = 15% × 0.20 × 4.0 = <strong>12%</strong><br><br>
  <strong>פרשנות:</strong> מרווח גבוה יחסית (15%) אך מחזור נכסים נמוך מאוד (0.20) —
  אופייני לנדל"ן עם נכסים ענקיים. ה-ROE של 12% מושג בעיקר בזכות המינוף (4.0).
</div>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — DuPont מגלה את האמת:</strong><br><br>
  חברת נדל"ן הציגה ROE של 18% — נראה מצוין. ניתוח DuPont חשף: מרווח נקי ירד
  מ-18% ל-12% (ירידה תפעולית), מחזור נכסים ירד מ-0.25 ל-0.20 (נכסים פחות יעילים),
  אך מינוף עלה מ-4.0 ל-7.5. ה-ROE "שמר על עצמו" רק כי הנהלה העמיסה חוב —
  לא כי הפעילות השתפרה. הבנק שראה רק את ROE פספס את הידרדרות האיכות התפעולית.
</div>

<h2>יחסי יעילות (Efficiency Ratios)</h2>

<p>
יחסי יעילות מודדים כמה מהר החברה "מסובבת" את נכסיה התפעוליים.
</p>

<h3>ימי לקוחות (Days Sales Outstanding)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ימי לקוחות = (לקוחות ÷ הכנסות) × 365
</div>

<p>
כמה ימים עוברים בממוצע עד שהחברה גובה את חובות לקוחותיה. בנדל"ן מניב, ימי לקוחות
של 15–30 יום — נורמלי. מעל 60 יום — בעיית גבייה. מגמת עלייה לאורך 3 שנים — אלארם.
</p>

<h3>ימי ספקים (Days Payable Outstanding)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ימי ספקים = (ספקים ÷ עלות המכר) × 365
</div>

<h3>ימי מלאי (Days Inventory Outstanding)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ימי מלאי = (מלאי ÷ עלות המכר) × 365
</div>

<p>
בחברות ייזום נדל"ן, ימי מלאי יכולים להיות 730–1460 יום (2–4 שנות בנייה) — זה נורמלי.
ירידה חדה בימי מלאי עשויה לאותת על סגירת פרויקטים ומסירות.
</p>

<h3>מחזור המזומן (Cash Conversion Cycle)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
מחזור מזומן = ימי מלאי + ימי לקוחות − ימי ספקים
</div>

<p>
מחזור מזומן חיובי גבוה — החברה צריכה מימון לפעילות השוטפת. בייזום נדל"ן, מחזור
של 1,000–1,800 יום הוא נורמלי בגלל אורך הפרויקטים.
</p>

<h2>מינוף וסולבנטיות (Leverage &amp; Solvency)</h2>

<h3>יחס חוב-להון (D/E Ratio)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
D/E = סך חוב נושא ריבית ÷ הון עצמי
</div>

<p>
בנדל"ן מניב ישראלי: D/E של 1.5–3.0 — שגרתי. מעל 4.0 — גבוה, מחייב בחינת כיסוי.
בחברות שירות: D/E מעל 1.5 — כבר גבוה.
</p>

<h3>חוב ל-EBITDA (Debt/EBITDA)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Debt/EBITDA = סך חוב נושא ריבית ÷ EBITDA שנתי<br>
פרשנות: כמה שנים של EBITDA נדרשות לפירעון מלא של החוב
</div>

<p>
בנדל"ן מניב: Debt/EBITDA של 8–12 — נורמלי. מעל 15 — סיכון גבוה. בייזום:
יחס זה פחות רלוונטי בגלל EBITDA תנודתי — עדיפים DSCR ו-LTV לרמת פרויקט.
</p>

<h3>חוב נטו ל-EBITDA (Net Debt/EBITDA)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
חוב נטו = סך חוב נושא ריבית − מזומן ושווי מזומן<br>
Net Debt/EBITDA = חוב נטו ÷ EBITDA
</div>

<h2>שירות חוב (Debt Service)</h2>

<h3>DSCR — יחס כיסוי שירות חוב</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
DSCR = EBITDA מתואם ÷ (תשלומי ריבית + החזרי קרן שנתיים)<br>
ספים: מעל 1.25 — נדרש לרוב ההלוואות הבנקאיות; מתחת ל-1.0 — הפסד שירות
</div>

<h3>ICR — יחס כיסוי ריבית (Interest Coverage Ratio)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ICR = EBIT ÷ הוצאות ריבית<br>
ספים: מעל 2.0 — נאות; מתחת ל-1.5 — סיכון ממשי
</div>

<h3>FCF/Debt — תזרים חופשי על חוב</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
FCF/Debt = תזרים חופשי שנתי ÷ סך חוב נושא ריבית
</div>

<h2>דוגמה מלאה — "הר כסף נדל"ן בע"מ"</h2>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>נתונים (אלפי ש"ח):</strong><br><br>
  הכנסות: 75,000 | עלות המכר: 48,000 | רווח גולמי: 27,000<br>
  EBIT: 14,000 | פחת: 2,500 | EBITDA: 16,500<br>
  הוצאות ריבית: 5,200 | רווח נקי: 6,300<br>
  נכסים שוטפים: 35,000 (מזומן 8,000, לקוחות 6,000, מלאי 21,000)<br>
  התחייבויות שוטפות: 22,000 | סך נכסים: 280,000 | הון עצמי: 85,000<br>
  סך חוב נושא ריבית: 160,000 | ספקים: 12,000 | החזרי קרן שנתיים: 8,000<br><br>

  <strong>חישוב יחסים:</strong><br><br>

  <table style="border-collapse:collapse;width:100%;margin:8px 0;">
    <thead>
      <tr style="background:#1a2638;color:#fff;">
        <th style="padding:8px;text-align:right;border:1px solid #ccc;">יחס</th>
        <th style="padding:8px;text-align:right;border:1px solid #ccc;">חישוב</th>
        <th style="padding:8px;text-align:right;border:1px solid #ccc;">ערך</th>
        <th style="padding:8px;text-align:right;border:1px solid #ccc;">הערכה</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">יחס שוטף</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">35,000 ÷ 22,000</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">1.59</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">סביר</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">יחס מהיר</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">(8K+6K) ÷ 22,000</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">0.64</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">נמוך — בדוק מלאי</td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">מרווח גולמי</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">27,000 ÷ 75,000</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">36%</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">טוב לייזום</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">EBITDA Margin</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">16,500 ÷ 75,000</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">22%</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">טוב</td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">ROA</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">6,300 ÷ 280,000</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">2.3%</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">נורמלי לנדל"ן</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">ROE</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">6,300 ÷ 85,000</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">7.4%</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">סביר</td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">D/E</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">160,000 ÷ 85,000</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">1.88</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">נורמלי לנדל"ן</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">Debt/EBITDA</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">160,000 ÷ 16,500</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">9.7x</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">גבוה — נטר</td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">ICR</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">14,000 ÷ 5,200</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">2.69x</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">נאות</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">DSCR</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">16,500 ÷ (5,200+8,000)</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">1.25x</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">בקצה המינימום</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>טבלת השוואה לממוצע ענפי — נדל"ן ישראלי</h2>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">יחס</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">נדל"ן מניב (ממוצע)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">יזמי נדל"ן (ממוצע)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הר כסף נדל"ן</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">יחס שוטף</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.2–1.8</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.5–2.5</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.59 ✓</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">EBITDA Margin</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">55%–70%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">15%–25%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">22% ✓</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">D/E</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.5–3.5</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.0–2.5</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.88 ✓</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Debt/EBITDA</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">8–14x</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5–10x</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">9.7x ⚠</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ICR</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2.0–4.0x</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2.0–5.0x</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2.69x ✓</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">DSCR</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.3–2.5x</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.2–2.0x</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.25x ⚠</td>
    </tr>
  </tbody>
</table>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — יחסים פיננסיים</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>יחסי נזילות:</strong> יחס שוטף, מהיר ומזומן. בחברות ייזום — יחס מהיר יכול
    להיות נמוך מ-0.5 (בגלל מלאי גבוה) בלי שזו בהכרח בעיה — צריך הקשר. ימי הון
    חוזר משלימים את הסיפור.
  </li>
  <li>
    <strong>יחסי רווחיות:</strong> מרווח גולמי, EBIT Margin, ROA, ROE. ניתוח DuPont
    מפרק ROE לשלושה גורמים — מרווח, יעילות, מינוף — ומגלה מאיפה מגיע השיפור
    (או הידרדרות).
  </li>
  <li>
    <strong>יחסי יעילות:</strong> ימי לקוחות, ספקים ומלאי. מחזור המזומן = ימי מלאי
    + ימי לקוחות − ימי ספקים. בייזום — מחזור של 1,000–1,800 יום הוא נורמלי.
  </li>
  <li>
    <strong>מינוף וסולבנטיות:</strong> D/E, Debt/EBITDA, Net Debt/EBITDA. ספים
    שונים לחלוטין בין נדל"ן מניב לייזום לשירותים — לעולם ציין ענף!
  </li>
  <li>
    <strong>שירות חוב:</strong> DSCR מעל 1.25 — נדרש בנקאי; ICR מעל 2.0 — נאות.
    DSCR מתחת ל-1.0 — החברה לא מכסה שירות חוב מהפעילות.
  </li>
</ol>

<h3>מילון מושגים — מודול 2</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מונח</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">English</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">יחס שוטף</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Current Ratio</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכסים שוטפים ÷ התחייבויות שוטפות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ROA</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Return on Assets</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווח נקי ÷ סך נכסים — יעילות שימוש בנכסים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ROE</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Return on Equity</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווח נקי ÷ הון עצמי — תשואה לבעלי מניות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">DuPont</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">DuPont Analysis</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פירוק ROE = מרווח × מחזור נכסים × מינוף</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ימי לקוחות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Days Receivable (DSO)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">(לקוחות ÷ הכנסות) × 365</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">D/E</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Debt-to-Equity Ratio</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חוב נושא ריבית ÷ הון עצמי</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Debt/EBITDA</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Leverage Ratio</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שנים לפירעון חוב מ-EBITDA</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ICR</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Interest Coverage Ratio</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">EBIT ÷ הוצאות ריבית</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
יחסים פיננסיים "סטנדרטיים" עובדים טוב על חברות שירות ותעשייה. יזמי נדל"ן הם
חיה שונה: הכרה בהכנסות עם מסירת הדירה, מלאי שמסתיר שווי אמיתי, SPV שמסתירים
חוב. <em>מודול 3</em> יתמקד ב<strong>ניתוח ייחודי ליזמי נדל"ן</strong> — עם כל
המכשולים שצריך לעקוף כאנליסט מקצועי.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>ניתוח יזם נדל"ן — מדוע יזמים שונים מכל חברה אחרת</h2>

<p>
יזם נדל"ן אינו חברה שירותים, אינו חברה תעשייתית, ואינו חברת נדל"ן מניב.
ניתוח יזם דורש הבנה עמוקה של שלושה נושאים ייחודיים: <em>הכרה בהכנסה</em>
(מתי נרשמת המכירה?), <em>מבנה חוב</em> (ברמת חברה מול ברמת פרויקט), ו<em>איכות
רווחים</em> (האם הרווח המדווח משקף פעילות אמיתית?). כל שלושה יחד קובעים את
יכולת ההחזר האמיתית.
</p>

<h2>הכרה בהכנסה לפי IFRS 15</h2>

<p>
<strong>IFRS 15 (Revenue from Contracts with Customers)</strong> קובע שיזם מכיר
בהכנסה כאשר <em>השליטה בנכס עוברת לקונה</em>. לדירות, קיימות שתי גישות עיקריות:
</p>

<h3>שיטה א: הכרה בנקודת זמן (Point in Time) — עם מסירת הדירה</h3>
<p>
הגישה השמרנית והנפוצה יותר בישראל: הכנסה נרשמת <strong>רק ביום מסירת הדירה
לקונה</strong>. עד לאותו רגע — כל תשלומי הקונה (לרוב 10%–20% בחתימת חוזה,
השאר לפי לוח תשלומים) מופיעים כ"הכנסות שטרם הוכרו" — <em>התחייבות</em>
במאזן היזם.
</p>

<h3>שיטה ב: הכרה לאורך זמן (Over Time) — לפי התקדמות הבנייה</h3>
<p>
גישה זו מאפשרת לרשום הכנסה באופן יחסי לאחוז הבנייה שהושלם — <em>אם</em> מתקיימים
תנאים ספציפיים של IFRS 15 (בעיקר: ליזם יש זכות לתשלום עבור העבודה שבוצעה
ולקונה אין דרך לבטל ולקחת את הנכס בלי פיצוי). בישראל, רוב יזמי הדיור אינם
עומדים בתנאים אלה — ומשתמשים בגישה א.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה מחושבת — 100 יחידות, 60% מכורות מראש:</strong><br><br>

  יזם בונה פרויקט של 100 דירות בעלות ממוצעת של 2,000 אלפי ש"ח לדירה.
  60 דירות נמכרו בחוזה טרם תחילת הבנייה במחיר ממוצע 2,800 אלפי ש"ח לדירה.<br><br>

  <strong>מצב ב-31.12.2024 (עת הבנייה 50% מושלמת):</strong><br><br>

  <table style="border-collapse:collapse;width:100%;margin:8px 0;">
    <thead>
      <tr style="background:#1a2638;color:#fff;">
        <th style="padding:8px;text-align:right;border:1px solid #ccc;">פריט</th>
        <th style="padding:8px;text-align:right;border:1px solid #ccc;">שיטה א (מסירה)</th>
        <th style="padding:8px;text-align:right;border:1px solid #ccc;">שיטה ב (התקדמות)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">הכנסות P&L 2024</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">0 ש"ח</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">84,000 אלפי ש"ח (60×2,800×50%)</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">רווח גולמי P&L 2024</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">0 ש"ח</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">24,000 אלפי ש"ח (מרווח 28.6%)</td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">מאזן — מלאי (IAS 2)</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">100,000 אלפי ש"ח (עלות 50%)</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">40,000 אלפי ש"ח (עלות 40 דירות)</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">מאזן — הכנסות נדחות</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">168,000 אלפי ש"ח (60×2,800)</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">84,000 אלפי ש"ח (50% נדחה)</td>
      </tr>
    </tbody>
  </table>

  <strong>מסקנה:</strong> שתי שיטות — P&L שונה לחלוטין, מאזן שונה. חברות שמשתמשות
  בשיטה ב יראו "רווחיות" גבוהה יותר בשלב הבנייה, אך ה-backlog האמיתי זהה.
  אנליסט חייב לבדוק <em>איזו שיטה</em> נוקטת החברה ולנרמל בהתאם.
</div>

<h2>מלאי דירות בפיתוח (IAS 2)</h2>

<p>
דירות שיזם בונה למכירה מסווגות כ<strong>מלאי (Inventory)</strong> לפי <strong>IAS 2</strong>.
המלאי נרשם <em>בעלות</em> — כולל:
</p>
<ul>
  <li>עלות הקרקע (כולל היטל השבחה)</li>
  <li>עלויות בנייה ישירות</li>
  <li>עלויות מימון שנצברו בתקופת הבנייה (Capitalized Borrowing Costs לפי IAS 23)</li>
  <li>עלויות תכנון, רישוי ופיתוח תשתיות</li>
</ul>

<p>
<strong>ההבחנה הקריטית מ-IAS 40:</strong> לא ניתן לבחור מודל שווי הוגן למלאי. המלאי
מוצג בעלות או בשווי מימוש נטו (NRV — Net Realizable Value) — <em>הנמוך מבין השניים</em>.
כלומר: אם עלות הדירה 2,000 אלפי ש"ח ומחיר השוק ירד ל-1,800 אלפי ש"ח — יש לרשום
ירידת ערך מלאי של 200 אלפי ש"ח. לעומת זאת, אם מחיר השוק עלה ל-2,500 אלפי ש"ח —
<strong>אין רישום עלייה</strong>; שיפור זה יוכר רק ביום המסירה.
</p>

<h3>מלאי מול נדל"ן להשקעה — השוואה</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">קריטריון</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מלאי דירות (IAS 2)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">נדל"ן להשקעה (IAS 40)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מטרת הנכס</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מכירה בפעילות רגילה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">השכרה / עליית ערך</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מודל מדידה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עלות או NRV (הנמוך)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שווי הוגן או עלות (לפי בחירה)</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עלייה בשווי שוק</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לא מוכרת עד מסירה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מוכרת ב-P&L (מודל שווי הוגן)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ירידה בשווי שוק</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ירידת ערך מיידית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מוכרת ב-P&L (מודל שווי הוגן)</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פחת</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אין</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רק במודל עלות</td>
    </tr>
  </tbody>
</table>

<h2>חוב נטו ברמת חברה מול רמת פרויקט</h2>

<p>
סוגיה קריטית בניתוח יזמי נדל"ן: <strong>מבנה ה-SPV (Special Purpose Vehicle)</strong>.
יזם גדול עשוי לפעול כך:
</p>
<ul>
  <li><strong>חברת האם:</strong> הון עצמי נמוך יחסית, חוב ברמת Corporate קטן.</li>
  <li><strong>SPV א (פרויקט X):</strong> מכיל הלוואת ליווי בנקאי של 120 מיליון ש"ח.</li>
  <li><strong>SPV ב (פרויקט Y):</strong> מכיל הלוואת ליווי בנקאי של 80 מיליון ש"ח.</li>
  <li><strong>SPV ג (נדל"ן מניב):</strong> מכיל הלוואה לטווח ארוך של 60 מיליון ש"ח.</li>
</ul>

<p>
על הנייר — חברת האם נראית "קלה". הניתוח המאוחד (Consolidated) חושף את האמת:
260 מיליון ש"ח חוב כולל. <strong>אנליסט חייב לעבוד על הדוח המאוחד</strong> — לא
על הדוח הסולו של חברת האם.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — SPV מסתיר חוב!</strong><br>
  כאשר כל SPV מממן את עצמו בנפרד, הלוואת הליווי של SPV כלשהו היא <em>ללא
  recourse</em> לחברת האם — כלומר, אם הפרויקט נכשל, הבנק תובע את ה-SPV לא
  את האם. אבל: (א) חברת האם לרוב ערבה, (ב) כישלון SPV פוגע בשם ובמימון עתידי,
  (ג) המימון המאוחד חשוף לכולם. בקש תמיד את הדוח המאוחד <em>ואת</em> הרשימה
  המלאה של חברות הבנות והשותפויות.
</div>

<h2>שערוכי שווי הוגן ואיכות רווחים (Earnings Quality)</h2>

<p>
יזמים רבים מחזיקים גם נדל"ן מניב (IAS 40 מודל שווי הוגן). בשוק עולה, שערוכים
אלה מנפחים את הרווח הנקי בסכומים עצומים — <strong>אך הם לא-מזומניים</strong>.
</p>

<h3>כיצד לנרמל EBITDA מול שערוכים</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
EBITDA מנורמל = EBITDA מדווח<br>
  − רווחי שערוך IAS 40 (נכסים להשקעה)<br>
  − רווחי מכירת נכסים (חד-פעמי)<br>
  − רווחי חברות כלולות (לא-מזומן לרוב)<br>
  + הפסדי שערוך (אם קיים)<br>
= EBITDA תפעולי אמיתי
</div>

<p>
הפער בין EBITDA מדווח ל-EBITDA מנורמל יכול להיות עצום. יזם ישראלי גדול עשוי
לדווח על רווח נקי של 300 מיליון ש"ח, מתוכם 250 מיליון ש"ח שערוכי IAS 40.
<strong>EBITDA תפעולי אמיתי: 50 מיליון ש"ח</strong> — שינוי שמשנה את כל ניתוח
יכולת שירות החוב.
</p>

<h2>ביקורת צלב — דוחות כספיים מול מצב פרויקט פיזי</h2>

<p>
אנליסט מנוסה לא מקבל את הדוחות כפשוטם — הוא <strong>מבקר צלב (Cross-Checks)</strong>:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מה שהיזם מדווח</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">כיצד לאמת</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">דגל אדום אפשרי</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">80% מהדירות נמכרו</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בקש רשימת חוזים חתומים (עם פרטי קונים)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מכירות גבוהות בלי הכנסות נדחות תואמות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פרויקט 70% מבנה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">השווה לשיחת שמאי / תצלום אוויר / ביקור אתר</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עלויות מלאי נמוכות מהצפוי לשלב זה</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תזרים מכירות לפי לוח</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בקש לוח משיכות הלוואת ליווי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פער בין לוח משיכות ללוח תשלומי קונים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הכנסות שכירות גדלות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בקש הסכמי שכירות מייצגים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גידול מרווחי שערוך, לא מגידול תפוסה/שכירות</td>
    </tr>
  </tbody>
</table>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — אנליסט שקיבל EBITDA לא-מנורמל:</strong><br><br>
  בנק מימן יזם נדל"ן גדול על בסיס EBITDA של 180 מיליון ש"ח שהיזם הציג.
  האנליסט לא ניתח את הרכב ה-EBITDA. רק לאחר שהיזם נקלע לקשיים, הבנק גילה:
  120 מיליון ש"ח היו שערוכי IAS 40 (לא מזומן). ה-EBITDA התפעולי האמיתי היה
  60 מיליון ש"ח — וה-Debt/EBITDA המנורמל היה 14x, לא 4.7x. ההלוואה אושרה
  על בסיס נתון שלא ייצג את יכולת שירות החוב. ההלוואה נמחקה חלקית שנתיים לאחר מכן.
</div>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — ניתוח יזם נדל"ן</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>הכרה בהכנסה (IFRS 15):</strong> רוב יזמי הדיור בישראל מכירים בהכנסה
    רק עם מסירת הדירה (Point in Time). עד לאותו רגע — תשלומי הקונים הם התחייבות
    במאזן. אנליסט חייב לבדוק איזו שיטה נוקטת החברה ולפרש את הדוחות בהתאם.
  </li>
  <li>
    <strong>מלאי דירות (IAS 2):</strong> נרשם בעלות (לא שווי הוגן). עלייה בשווי
    שוק לא מוכרת. ירידה בשווי שוק מחייבת ירידת ערך מיידית. מלאי גבוה לא בהכרח
    בעיה — אם אחוז המכירות מראש גבוה, המלאי כבר "מכור".
  </li>
  <li>
    <strong>SPV וחוב מאוחד:</strong> יזם עם מבנה SPV יכול לגרום לחברת האם להיראות
    "קלה מחוב". הניתוח חייב להיות על הדוח המאוחד. בקש רשימת חברות בנות ומצב
    הלוואות בכל אחת.
  </li>
  <li>
    <strong>שערוכי IAS 40 ואיכות רווחים:</strong> בשוק עולה, שערוכי שווי הוגן
    מנפחים רווחים — אך הם לא-מזומניים. EBITDA מנורמל חייב לנטרל שערוכים,
    מכירות נכסים ורכיבים חד-פעמיים לפני חישוב DSCR.
  </li>
  <li>
    <strong>ביקורת צלב:</strong> הצלב בין דוחות לבין מצב פרויקט פיזי (חוזי מכר,
    לוח משיכות, תצלום אוויר) הוא הבדיקה שמבדילה אנליסט מקצועי מאנליסט שמאמין
    לנתוני היזם באופן עיוור.
  </li>
</ol>

<h3>מילון מושגים — מודול 3</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מונח בעברית</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">English Term</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הכרה בהכנסה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Revenue Recognition (IFRS 15)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מתי ואיך לרשום הכנסה — עם מסירה או לאורך הבנייה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">IFRS 15</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">IFRS 15</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תקן הכרה בהכנסה מחוזים עם לקוחות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מלאי דירות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Apartment Inventory (IAS 2)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">דירות בפיתוח/מוכנות למכירה — נרשמות בעלות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">SPV</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Special Purpose Vehicle</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חברה ייעודית לפרויקט אחד — מסתירה חוב מרמת האם</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שערוך</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Revaluation / Fair Value Gain</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רישום עלייה בשווי הוגן — לא-מזומני, מנפח רווח</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">IAS 40</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">IAS 40 — Investment Property</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תקן נדל"ן להשקעה — מאפשר מודל שווי הוגן</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חוב נטו</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Net Debt</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סך חוב נושא ריבית פחות מזומן — החוב "האמיתי"</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ליווי בנקאי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Bank Escort (Construction Loan)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הלוואה לפרויקט בנייה — נמשכת לפי התקדמות</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
שלושת המודולים הראשונים בנו בסיס מוצק: מתודולוגיה כללית, יחסים פיננסיים, וניתוח
ייחודי ליזמי נדל"ן. <em>מודול 4</em> יעמיק ב<strong>ניתוח קבוצות יזמיות וחברות
מניב</strong> — ניתוח מאוחד, ביצועי תיק נכסים, והשוואה בין-חברתית מקצועית.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 3 "
        "(ניתוח דוחות כספיים — יזמי נדל\"ן וקבוצות יזמיות)"
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 3 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=3)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=3 not found. "
                "Run 'python manage.py seed_data' first to create the course structure."
            )

        self.stdout.write(f"Found course: {course}")

        # Pair each module metadata with its reading and summary HTML
        module_content = [
            (MODULES[0], M1_READING_HTML, M1_SUMMARY_HTML),
            (MODULES[1], M2_READING_HTML, M2_SUMMARY_HTML),
            (MODULES[2], M3_READING_HTML, M3_SUMMARY_HTML),
        ]

        for module_meta, reading_html, summary_html in module_content:
            self._seed_module(course, module_meta, reading_html, summary_html)

        self.stdout.write(
            self.style.SUCCESS("\nAll done — Course 3 modules 1-3 seeded successfully.")
        )

    def _seed_module(
        self,
        course: Course,
        meta: dict,
        reading_html: str,
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
            (2, ComponentType.COMPREHENSION, ""),
            (3, ComponentType.EXERCISES, ""),
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
