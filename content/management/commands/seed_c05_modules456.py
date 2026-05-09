"""
Management command: seed_c05_modules456
Seeds Course 5 (ניתוח תזרים מזומנים), Modules 4, 5, and 6 with full reading,
comprehension, exercises, and summary ModuleComponent records.

Usage:
    python manage.py seed_c05_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — Free Cash Flow בנדל"ן
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  Free Cash Flow בנדל&quot;ן
</h2>

<!-- ===== סעיף 1 — FCF = OCF - Maintenance CAPEX ===== -->
<h3 style="color:#1a2638;">1. FCF = OCF &minus; Maintenance CAPEX</h3>

<p>
  <strong>Free Cash Flow (FCF)</strong> — תזרים מזומנים חופשי — הוא הכסף שנותר
  לבעלים לאחר שמימנו את כל ההוצאות השוטפות <em>וגם</em> את ה-CAPEX הנדרש
  לשמירת הנכס במצב תפעולי. הנוסחה הבסיסית:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  FCF = OCF &minus; Maintenance CAPEX
</div>

<p>
  ההבדל הקריטי הוא בין שני סוגי ה-CAPEX:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג CAPEX</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דוגמה בנדל&quot;ן</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">השפעה על FCF</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Maintenance CAPEX</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">השקעה לשמירת הנכס על מצבו הקיים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">החלפת מעלית ישנה, שיפוץ גג, עדכון מיזוג אוויר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">מפחית FCF — הכרחי לשמירת ערך</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Growth CAPEX</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">השקעה להרחבת הנכס או יצירת ערך נוסף</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תוספת קומה, בניית חניון חדש, הרחבת שטח מסחר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#1976d2;">אינו מנוכה מ-FCF הנוכחי — מחושב כהשקעה נפרדת</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>דוגמה מספרית — בניין מסחרי בתל אביב:</strong>
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  הכנסות שכירות שנתיות: 4,800,000 ₪<br>
  הוצאות תפעול: (800,000) ₪<br>
  <strong>NOI: 4,000,000 ₪</strong><br>
  מיסים ואגרות: (200,000) ₪<br>
  <strong>OCF: 3,800,000 ₪</strong><br>
  Maintenance CAPEX (החלפת מערכות, שיפוצים שוטפים): (350,000) ₪<br>
  <strong>FCF: 3,450,000 ₪</strong>
</div>

<p>
  שימו לב: NOI = 4,000,000 ₪, אך FCF = 3,450,000 ₪ — פער של 550,000 ₪ שה-NOI
  "מתעלם" ממנו. זהו בדיוק הפגם של שימוש ב-NOI כ-proxy לתזרים האמיתי.
</p>

<!-- ===== סעיף 2 — FCFF vs FCFE ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. FCFF לעומת FCFE — מי מקבל את הכסף?</h3>

<p>
  קיימות שתי רמות של FCF, המשקפות שתי נקודות מבט שונות:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מדד</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שם מלא</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">נוסחה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מתאים ל...</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">FCFF</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Free Cash Flow to Firm</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-family:monospace;">OCF &minus; Maintenance CAPEX</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הערכת שווי החברה (Enterprise Value); תזרים לפני שירות חוב</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">FCFE</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Free Cash Flow to Equity</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-family:monospace;">FCFF &minus; תשלומי ריבית &minus; החזרי קרן + גיוס חוב חדש</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הערכת שווי ההון העצמי; מה נשאר לבעלים אחרי המלווים</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>המשך הדוגמה:</strong><br>
  FCFF = 3,450,000 ₪<br>
  תשלום ריבית שנתי: (600,000) ₪<br>
  החזר קרן שנתי: (400,000) ₪<br>
  <strong>FCFE = 2,450,000 ₪</strong> — זה מה שנשאר לבעלים בפועל
</div>

<p>
  <strong>מתי להשתמש בכל אחד?</strong>
</p>
<ul style="line-height:1.9;">
  <li><strong>FCFF</strong> — מתאים לניתוח DCF של הנכס כולו, ולהשוואה בין נכסים ממונפים שונה</li>
  <li><strong>FCFE</strong> — מתאים לבעל הנכס המעוניין לדעת כמה כסף הוא יכול לחלק לעצמו</li>
  <li><strong>לאנליסט האשראי</strong> — FCFF רלוונטי יותר: הוא בוחן את כושר ייצור מזומנים לפני שירות חוב</li>
</ul>

<!-- ===== סעיף 3 — FCF Yield ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. FCF Yield — מדד הערכת שווי</h3>

<p>
  <strong>FCF Yield</strong> מודד את ה-FCF כאחוז מ-Enterprise Value — כמה "תשואה חופשית"
  מייצר הנכס ביחס לשוויו:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  FCF Yield = FCF &divide; Enterprise Value
</div>

<p>
  <strong>דוגמה:</strong> בניין ששוויו 50 מ' ₪ ומייצר FCF שנתי של 3.45 מ' ₪:
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  FCF Yield = 3,450,000 &divide; 50,000,000 = <strong>6.9%</strong><br><br>
  פרשנות: על כל שקל שמושקע בנכס, מתקבלים 6.9 אגורות בתזרים חופשי שנתי.
  ב-FCF Yield גבוה מ-Cap Rate — הנכס "יעיל" מבחינת ניהולית (CAPEX נמוך).
</div>

<p>
  <strong>טווחי ייחוס (שוק ישראלי):</strong>
</p>
<ul style="line-height:1.9;">
  <li><strong>FCF Yield &lt; 4%</strong> — נמוך; ייתכן שה-CAPEX גבוה או הנכס מוערך גבוה</li>
  <li><strong>4%–7%</strong> — סביר לנכסים מניבים באיזורי ביקוש</li>
  <li><strong>מעל 7%</strong> — גבוה; ייתכן נכס בפריפריה, נכס ישן עם CAPEX נמוך זמנית, או הזדמנות</li>
</ul>

<!-- ===== סעיף 4 — NOI ≠ FCF ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. מדוע NOI &ne; FCF בנדל&quot;ן</h3>

<p>
  זהו אחד הפערים הנפוצים ביותר בניתוח נדל&quot;ן. <strong>NOI</strong> הוא כלי שימושי
  אך הוא <em>אינו</em> מייצג את המזומנים שבעל הנכס יכול לקחת הביתה:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מה NOI מתעלם ממנו</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">כיצד זה משפיע</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Maintenance CAPEX</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">השקעה שוטפת בנכס — מפחיתה את התזרים האמיתי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שירות חוב (קרן + ריבית)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשלומי משכנתא חודשיים — אינם בחישוב NOI</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מיסים על הכנסה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI הוא לפני מס — FCF אמיתי הוא לאחר מס</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שינויים בהון חוזר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פיקדונות שוכרים, הכנסות/הוצאות מצטברות</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>המסקנה לאנליסט:</strong> Cap Rate מבוסס על NOI הוא כלי השוואה מהיר —
  אך לא תחליף לניתוח FCF מלא. שני נכסים עם אותו Cap Rate עשויים להיות שונים
  מאוד ב-FCF Yield, בשל CAPEX שונה לגמרי.
</p>

<!-- ===== סעיף 5 — Cash-on-Cash vs FCF Yield ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. Cash-on-Cash Return לעומת FCF Yield</h3>

<p>
  שני מדדים דומים אך שונים — חשוב להבין מה כל אחד מודד:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מדד</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מונה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מכנה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">נקודת מבט</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Cash-on-Cash Return</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCFE (לאחר שירות חוב)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הון עצמי שהושקע</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מדד לבעלים — תשואה על ההון שלי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">FCF Yield</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCFF (לפני שירות חוב)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Enterprise Value (שווי נכס)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מדד לנכס — יעילות ייצור מזומן ביחס לשווי</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה:</strong> משקיע רכש בניין ב-50 מ' ₪, מהם 20 מ' הון עצמי ו-30 מ' חוב.<br>
  FCFF שנתי: 3,450,000 ₪ | שירות חוב: 1,000,000 ₪ | FCFE: 2,450,000 ₪<br><br>
  FCF Yield = 3,450,000 &divide; 50,000,000 = <strong>6.9%</strong> (מנקודת מבט הנכס)<br>
  Cash-on-Cash = 2,450,000 &divide; 20,000,000 = <strong>12.25%</strong> (מנקודת מבט הבעלים)
</div>

<p>
  המינוף מגדיל את Cash-on-Cash ביחס ל-FCF Yield. זה מדגיש מדוע השוואת
  Cash-on-Cash בין נכסים ממונפים שונה — מטעה: אנחנו משווים אפלים לתפוזים.
</p>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  יזם שמשתמש ב-NOI כ-proxy ל-FCF — מתעלם מכל הוצאות ההשקעה השוטפות.
  CAPEX אינו מופיע ב-NOI, אך הוא אמיתי לחלוטין: מי שלא משקיע בתחזוקה
  שוחק את הנכס — ועם הזמן גם את שוויו ואת תזרימו. ניתוח FCF אמיתי
  הוא הדרך היחידה לראות את התמונה המלאה.
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של FCF, ההבדל בין FCFF ל-FCFE, FCF Yield, "
    "ומדוע NOI אינו שווה ל-FCF בנדל\"ן. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים חישוב FCFF ו-FCFE מנתוני נכס נתונים, "
    "חישוב FCF Yield והשוואתו ל-Cap Rate, וזיהוי ההבדל בין Maintenance CAPEX "
    "ל-Growth CAPEX בתרחיש נתון. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — Free Cash Flow בנדל&quot;ן
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>FCF = OCF &minus; Maintenance CAPEX.</strong>
    יש להבחין בין Maintenance CAPEX (שוחק FCF) לבין Growth CAPEX (השקעה לצמיחה).
  </li>
  <li>
    <strong>FCFF הוא FCF לפני שירות חוב; FCFE הוא FCF לאחר שירות חוב.</strong>
    לאנליסט אשראי — FCFF רלוונטי יותר; לבעלים — FCFE מראה מה נשאר להם.
  </li>
  <li>
    <strong>FCF Yield = FCF &divide; Enterprise Value — מדד יעילות ייצור מזומן.</strong>
    שני נכסים עם Cap Rate זהה עשויים להיות שונים ב-FCF Yield בשל CAPEX שונה.
  </li>
  <li>
    <strong>NOI מתעלם מ-CAPEX, שירות חוב, מיסים ושינויי הון חוזר.</strong>
    שימוש ב-NOI כ-proxy ל-FCF מעלים את כל הוצאות ההשקעה השוטפות.
  </li>
  <li>
    <strong>Cash-on-Cash מחושב על ההון העצמי; FCF Yield מחושב על שווי הנכס.</strong>
    השוואת Cash-on-Cash בין נכסים ממונפים שונה היא מטעה.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תזרים מזומנים חופשי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Free Cash Flow (FCF)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">OCF בניכוי Maintenance CAPEX</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תזרים חופשי לחברה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCFF</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCF לפני שירות חוב — זמין לכלל נותני ההון</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תזרים חופשי להון עצמי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCFE</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCF לאחר שירות חוב — זמין לבעלים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תשואת תזרים חופשי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCF Yield</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCF &divide; Enterprise Value</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הוצאות הון לתחזוקה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Maintenance CAPEX</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">השקעה לשמירת הנכס במצבו הקיים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הוצאות הון לצמיחה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Growth CAPEX</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">השקעה ליצירת שווי או תזרים נוסף</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — תזרים של יזם נדל"ן — ניתוח מעשי
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  תזרים של יזם נדל&quot;ן &mdash; ניתוח מעשי
</h2>

<!-- ===== סעיף 1 — מאפיינים ייחודיים ===== -->
<h3 style="color:#1a2638;">1. מאפיינים ייחודיים של תזרים יזם נדל&quot;ן</h3>

<p>
  תזרים המזומנים של יזם נדל&quot;ן שונה מהותית מתזרים של חברה תפעולית רגילה.
  האנליסט חייב להבין את המאפיינים הייחודיים הבאים:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מאפיין</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תיאור</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">השלכה לאנליסט</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אי-סדירות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תזרים לא אחיד — שנים שליליות בבנייה ושנה חיובית במכירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתוח DSCR שנתי אינו מספיק — נדרש ניתוח חודשי/רבעוני</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פרויקטים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כל פרויקט הוא ישות בפני עצמה עם תזמון וסיכון ייחודיים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתוח Consolidated מסתיר בעיות בפרויקט ספציפי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מכירות חד-פעמיות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רוב הרווח מגיע ממכירה של הנכס — אירוע בלתי חוזר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכנסות ממכירה אינן תזרים חוזר — אין להסתמך עליהן לשירות חוב שוטף</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>הבדל יסודי:</strong> חברת נדל&quot;ן מניבה דומה לחברה עם הכנסות שנתיות
  צפויות; יזם נדל&quot;ן דומה לחברת פרויקטים — כל פרויקט הוא "עסק" נפרד עם
  מחזור חיים ייחודי.
</p>

<!-- ===== סעיף 2 — J-Curve ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. פרופיל תזרים J-Curve בפרויקט ייזום</h3>

<p>
  פרויקט ייזום נדל&quot;ן מציג <strong>פרופיל תזרים "J-Curve"</strong>: שנות בנייה
  שליליות (השקעה ללא הכנסה) ואז אירוע חיובי גדול בשלב המכירה או ההשכרה.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — פרויקט מגורים (100 יחידות):</strong><br><br>
  <table style="border-collapse:collapse;width:100%;font-size:12px;">
    <thead>
      <tr style="background:#1a2638;color:#fff;">
        <th style="border:1px solid #ccc;padding:6px 10px;text-align:right;">שנה</th>
        <th style="border:1px solid #ccc;padding:6px 10px;text-align:right;">פעילות</th>
        <th style="border:1px solid #ccc;padding:6px 10px;text-align:right;">תזרים (מ' ₪)</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:#fce4e4;">
        <td style="border:1px solid #ccc;padding:6px 10px;">0</td>
        <td style="border:1px solid #ccc;padding:6px 10px;">רכישת קרקע + עלויות</td>
        <td style="border:1px solid #ccc;padding:6px 10px;color:#c62828;font-weight:bold;">&minus;40</td>
      </tr>
      <tr style="background:#fce4e4;">
        <td style="border:1px solid #ccc;padding:6px 10px;">1</td>
        <td style="border:1px solid #ccc;padding:6px 10px;">בנייה — שלב א' + מכירות על הנייר</td>
        <td style="border:1px solid #ccc;padding:6px 10px;color:#c62828;font-weight:bold;">&minus;25</td>
      </tr>
      <tr style="background:#fce4e4;">
        <td style="border:1px solid #ccc;padding:6px 10px;">2</td>
        <td style="border:1px solid #ccc;padding:6px 10px;">בנייה — שלב ב' + קבלות מקדמות</td>
        <td style="border:1px solid #ccc;padding:6px 10px;color:#c62828;font-weight:bold;">&minus;15</td>
      </tr>
      <tr style="background:#e8f5e9;">
        <td style="border:1px solid #ccc;padding:6px 10px;">3</td>
        <td style="border:1px solid #ccc;padding:6px 10px;">גמר בנייה + מסירת דירות</td>
        <td style="border:1px solid #ccc;padding:6px 10px;color:#2e7d32;font-weight:bold;">+110</td>
      </tr>
    </tbody>
  </table>
</div>

<p>
  <strong>האתגר לאנליסט:</strong> בשנים 0–2 הפרויקט "שורף" מזומנים. היזם מממן
  זאת מהון עצמי, הלוואות ליווי, ומקדמות רוכשים. <em>כל עיכוב בבנייה</em> מאריך
  את התקופה השלילית ומגדיל את עלויות המימון.
</p>

<p>
  <strong>ניתוח J-Curve מצריך:</strong>
</p>
<ul style="line-height:1.9;">
  <li>בדיקת <strong>Break-Even Sales Rate</strong> — כמה אחוז מהיחידות צריך למכור כדי לכסות את ההלוואה</li>
  <li>ניתוח <strong>תזרים חודשי</strong> בשנות הבנייה — לא רק שנתי</li>
  <li>בחינת <strong>מקורות מימון לגשר</strong> בתקופה השלילית</li>
</ul>

<!-- ===== סעיף 3 — נכסים מניבים vs ייזום ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. נכסים מניבים לעומת ייזום — ניגוד מהותי</h3>

<p>
  שני מודלי עסקים שונים לחלוטין, עם פרופילי תזרים מנוגדים:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מאפיין</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">נכס מניב</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פרויקט ייזום</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תזרים שוטף</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#2e7d32;">יציב וחוזר — שכר דירה חודשי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">שלילי בבנייה, חיובי גדול במכירה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח DSCR</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רלוונטי ומשמעותי — NOI/שירות חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מוגבל — DSCR שנתי לא מספיק</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מקור ההחזר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכנסות שכירות שוטפות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מכירת הנכס / יחידות — Bullet Payment</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סיכון עיקרי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פנויות, ירידת שכירות, עליית ריבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עיכוב בנייה, ירידת מחירים, עיכוב היתרים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מודל מימון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואה לטווח ארוך — Amortizing Loan</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואת ליווי — נפרעת ממכירות</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 4 — Consolidated Cash Flow ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. Consolidated Cash Flow של קבוצת נדל&quot;ן</h3>

<p>
  קבוצות נדל&quot;ן גדולות בישראל מחזיקות בו-זמנית נכסים מניבים <em>ו</em>פרויקטי
  ייזום. הדוח האיחודי (Consolidated) מאחד את שני המודלים, מה שמצריך ניתוח
  מפוצל:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>פיצול בין תזרים תפעולי (מניב) לתזרים מפרויקטים (ייזום):</strong>
    קבוצה שרושמת תזרים תפעולי גבוה עשויה להסתיר תזרים שלילי עמוק בפרויקטי ייזום.
  </li>
  <li>
    <strong>ביטול עסקאות בין-חברתיות (Eliminations):</strong>
    הלוואות פנים-קבוצתיות, דמי ניהול, ואחריות צולבת — כולם מנוטרלים באיחוד.
  </li>
  <li>
    <strong>Minority Interest (זכויות מיעוט):</strong>
    חלק מהפרויקטים הוא בשותפות. התזרים האיחודי כולל 100% אך מחלק חלק
    לשותפים — הכסף לא שייך כולו לחברה האם.
  </li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל מעשי:</strong> בקש תמיד פירוט לפי פרויקט ולפי מגזר (מניב / ייזום).
  דוח איחוד ללא פירוט כזה — בלתי ניתן לניתוח אמיתי.
</div>

<!-- ===== סעיף 5 — Debt Maturity Wall ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. Debt Maturity Wall — קיר הפירעון</h3>

<p>
  <strong>Debt Maturity Wall</strong> הוא ריכוז פירעונות חוב גדולים בתקופה קצרה,
  שלא בהכרח מתואמת עם שיא תזרים הכנסות הצפוי. זהו אחד הסיכונים המרכזיים
  בניתוח יזם נדל&quot;ן.
</p>

<p>
  <strong>ניתוח Maturity Wall מצריך:</strong>
</p>
<ul style="line-height:1.9;">
  <li>מיפוי כל מועדי פירעון החוב לפי שנה — טבלת "מגדל חוב"</li>
  <li>השוואה לתחזית התזרים הצפוי באותה שנה (ממכירות ו/או הכנסות שכירות)</li>
  <li>בחינת <strong>Refinancing Risk</strong> — האם ניתן לגלגל את החוב בתנאי ריבית עתידיים?</li>
  <li>בדיקת <strong>Cross-Default Clauses</strong> — האם כשל בפרויקט אחד מפעיל חוב אחר?</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — קבוצת ייזום ישראלית:</strong><br>
  שנת 2026: פירעון אג&quot;ח 800 מ' ₪ | תזרים צפוי ממכירות: 600 מ' ₪<br>
  <strong>פער: 200 מ' ₪ שיש לממן ממקורות אחרים</strong> — מכירת נכסים, גיוס הון, refinancing<br>
  זהו Maturity Wall — לא בגלל שהפרויקט רע, אלא כי <em>התזמון</em> לא מתאים.
</div>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  60% מחדלות פירעון בנדל&quot;ן מתרחשות כשהפרויקט טוב אך התזמון גרוע —
  Liquidity Mismatch. פרויקט עם IRR מצוין יכול לקרוס לפני שמגיע לשלב
  המכירה אם אין מספיק נזילות לשרת את החוב בתקופת הבנייה. ניתוח נזילות
  לפי חודש — לא לפי שנה — הוא ההגנה האמיתית.
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של פרופיל J-Curve, ההבדל בין נכס מניב לייזום, "
    "ניתוח Consolidated Cash Flow, ו-Debt Maturity Wall. "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים ניתוח תזרים J-Curve לפרויקט ייזום נתון, "
    "זיהוי Maturity Wall בלוח פירעונות חוב, והשוואת פרופיל תזרים בין נכס מניב "
    "לפרויקט ייזום. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום &mdash; תזרים של יזם נדל&quot;ן
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>תזרים יזם הוא אי-סדיר, פרויקטלי, ומבוסס על מכירות חד-פעמיות.</strong>
    ניתוח DSCR שנתי אינו מספיק — נדרש ניתוח חודשי בשנות הבנייה.
  </li>
  <li>
    <strong>פרויקט ייזום מציג פרופיל J-Curve: שנות שליליות בבנייה, תזרים גדול במכירה.</strong>
    כל עיכוב בבנייה מאריך את התקופה השלילית ומגדיל עלויות מימון.
  </li>
  <li>
    <strong>נכסים מניבים מייצרים תזרים יציב; ייזום מייצר תזרים "Bullet" חד-פעמי.</strong>
    שני מודלי ניתוח שונים — אין להחיל את כלי הנכס המניב על פרויקט ייזום.
  </li>
  <li>
    <strong>Consolidated Cash Flow מסתיר בעיות פרויקטלי — תמיד דרוש פירוט לפי פרויקט.</strong>
    ביטולי עסקאות פנים-קבוצתיות ו-Minority Interest משנים את התמונה.
  </li>
  <li>
    <strong>Debt Maturity Wall — ריכוז פירעונות שלא בהכרח מתואם עם תזרים ההכנסות.</strong>
    60% מחדלות הפירעון בנדל&quot;ן הן Liquidity Mismatch — לא בעיה בפרויקט עצמו.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עקומת ג'יי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">J-Curve</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פרופיל תזרים שלילי בתחילה וחיובי בסיום</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קיר חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Debt Maturity Wall</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ריכוז פירעונות חוב גדולים בתקופה קצרה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אי-התאמת נזילות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Liquidity Mismatch</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פירעון חוב לפני הגעת תזרים ההכנסות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">איחוד דוחות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Consolidation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">איחוד דוחות כספיים של חברות קשורות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סיכון מחזור חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Refinancing Risk</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכון שחוב לא יוכל להתגלגל בתנאים מקובלים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">כשל צולב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cross-Default</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הפרת הלוואה אחת מפעילה כשל בהלוואה אחרת</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — תחזית תזרים ומודל DCF
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  תחזית תזרים ומודל DCF
</h2>

<!-- ===== סעיף 1 — מהו DCF ===== -->
<h3 style="color:#1a2638;">1. DCF &mdash; מהות ומתודולוגיה</h3>

<p>
  <strong>DCF (Discounted Cash Flow)</strong> — ניתוח תזרים מהוון — הוא שיטת הערכת
  שווי המבוססת על ה<em>ערך הנוכחי</em> של תזרימי מזומנים עתידיים צפויים.
  הרעיון הבסיסי: שקל שמגיע בעוד שנה שווה פחות מהיום, כי כסף עכשיו ניתן
  להשקיע וייצר תשואה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  DCF Value = &Sigma; [CF&#8321; &divide; (1+r)&sup1;] + [CF&#8322; &divide; (1+r)&sup2;] + ... + [CF&#8345; &divide; (1+r)&#8319;] + [Terminal Value &divide; (1+r)&#8319;]
</div>

<p>
  שלושת מרכיבי ה-DCF בנדל&quot;ן:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>תחזית תזרים (Explicit Forecast Period):</strong>
    בדרך כלל 5–10 שנים. עבור כל שנה: NOI &minus; CAPEX &minus; מיסים.
  </li>
  <li>
    <strong>Terminal Value (ערך שיורי):</strong>
    שווי המכירה הצפוי בסוף תקופת התחזית — המייצג את כל התזרימים
    שלאחר מכן. ב-DCF נדל&quot;ן, Terminal Value מהווה לרוב <strong>60%–80%</strong> מהשווי הכולל.
  </li>
  <li>
    <strong>ריבית היוון (Discount Rate):</strong>
    השיעור שמביא תזרימים עתידיים לערכם הנוכחי.
  </li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מדוע DCF חשוב לאנליסט אשראי?</strong><br>
  DCF מאפשר לאנליסט לבחון האם שווי הנכס המוצג על ידי הלווה מגובה בתזרימים
  ריאליסטיים, או מבוסס על הנחות אופטימיות מדי. שווי DCF נמוך משווי השוק
  הנוכחי — סיגנל לבדיקה מחמירה.
</div>

<!-- ===== סעיף 2 — בניית תחזית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. בניית תחזית — הנחות המפתח</h3>

<p>
  תחזית DCF לנכס נדל&quot;ן מניב מבוססת על ארבע הנחות מפתח:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הנחה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מה לבחון</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">ערך ייחוס</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תפוסה (Occupancy)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">האם ריאלי ביחס לשוק? היסטוריה? חוזים קיימים?</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בניינים מסחריים: 85%–95%; לוגיסטיקה: 90%–97%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שכר דירה (Rental Growth)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">האם הצמיחה הנחה מצדיקה את השוק? מדד מחירים?</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ישראל: CPI + 0%–2% לנכסים מניבים יציבים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">CAPEX שנתי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">האם הנחת CAPEX ריאלית לגיל ומצב הנכס?</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">0.5%–1.5% משווי הנכס לשנה לנכסים בינוניים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Exit Cap Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">האם Exit Cap Rate מגלם סיכון שוק עתידי?</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">לרוב 0.25%–0.5% מעל ה-Cap Rate הנוכחי (זהירות)</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — תחזית ל-5 שנים:</strong><br><br>
  NOI שנה 1: 4,000,000 ₪ | צמיחה: 2% לשנה<br>
  CAPEX שנתי: 300,000 ₪ (0.6% מ-50 מ')<br>
  FCF שנה 1: 3,700,000 ₪ | שנה 5: ~4,082,000 ₪ (לאחר צמיחה)
</div>

<!-- ===== סעיף 3 — Terminal Value ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. Terminal Value &mdash; הלב של DCF בנדל&quot;ן</h3>

<p>
  בנדל&quot;ן, Terminal Value מחושב לפי <strong>Exit Cap Rate</strong>:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  Terminal Value = NOI(n+1) &divide; Exit Cap Rate
</div>

<p>
  כאשר NOI(n+1) הוא ה-NOI הצפוי בשנה הראשונה <em>לאחר</em> תקופת התחזית.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה:</strong> NOI בסוף שנה 5 = 4,082,000 ₪<br>
  NOI(n+1) = 4,082,000 &times; 1.02 = 4,164,000 ₪<br>
  Exit Cap Rate = 6%<br>
  <strong>Terminal Value = 4,164,000 &divide; 0.06 = 69,400,000 ₪</strong><br><br>
  Terminal Value (מהוון) = 69,400,000 &divide; (1.09)&sup5; = <strong>45,100,000 ₪</strong>
</div>

<p>
  <strong>מדוע Terminal Value חשוב כל כך?</strong>
  ב-DCF של נכס מניב לתקופה של 5–10 שנים, Terminal Value מהווה
  לרוב <strong>60%–80% מהשווי הכולל</strong>. שינוי קטן ב-Exit Cap Rate
  מניב שינוי גדול בשווי — זה המפתח להבנת רגישות ה-DCF.
</p>

<!-- ===== סעיף 4 — Discount Rate ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. ריבית היוון &mdash; WACC, שיעור הון עצמי, ו-Cap Rate</h3>

<p>
  בחירת ריבית ההיוון היא אחת ההחלטות הקריטיות ב-DCF. קיימות שלוש גישות עיקריות:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">גישה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מתי להשתמש</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">WACC</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ממוצע משוקלל של עלות החוב ועלות ההון העצמי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCFF DCF — הערכת שווי הנכס כולו</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Equity Discount Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשואה נדרשת על ידי בעלי ההון העצמי בלבד</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">FCFE DCF — הערכת שווי ההון העצמי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Cap Rate כ-Proxy</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שימוש ב-Cap Rate שוק כריבית היוון פשוטה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הערכות מהירות; יש להוסיף פרמיית סיכון בנסיבות</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>בשוק הישראלי:</strong> ריביות היוון נפוצות לנדל&quot;ן מניב הן <strong>7%–10%</strong>
  (WACC). לנכסים בסיכון גבוה יותר (ייזום, פריפריה) — <strong>12%–16%</strong>.
</p>

<p>
  <strong>WACC — נוסחה מפושטת:</strong>
</p>
<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  WACC = (E/V &times; r&#8336;) + (D/V &times; r&#8336; &times; (1 &minus; T))<br><br>
  E = הון עצמי | D = חוב | V = E+D | r&#8336; = עלות הון עצמי | r&#8336; = עלות חוב | T = שיעור מס
</div>

<!-- ===== סעיף 5 — Sensitivity על DCF ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. ניתוח רגישות על DCF</h3>

<p>
  DCF הוא רגיש מאוד לשינויים בהנחות — במיוחד Exit Cap Rate וצמיחת NOI.
  ניתוח רגישות הוא חובה:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שינוי בהנחה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">אפקט צפוי על שווי DCF</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דוגמה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Exit Cap Rate +0.5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">ירידת שווי של ~8%–12%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">50 מ' ₪ &rarr; ~44 מ' ₪</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Exit Cap Rate &minus;0.5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#2e7d32;">עלייה בשווי של ~8%–12%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">50 מ' ₪ &rarr; ~56 מ' ₪</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">NOI &minus;10%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">ירידת שווי של ~10%–15%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">50 מ' ₪ &rarr; ~43 מ' ₪</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Discount Rate +1%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">ירידת שווי של ~5%–8%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">50 מ' ₪ &rarr; ~46 מ' ₪</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>טבלת רגישות מלאה (Exit Cap Rate × NOI Growth):</strong>
</p>

<div style="overflow-x:auto;margin:16px 0;">
<table style="border-collapse:collapse;font-size:12px;min-width:420px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:6px 10px;">Exit Cap \ NOI</th>
      <th style="border:1px solid #ccc;padding:6px 10px;">&minus;10%</th>
      <th style="border:1px solid #ccc;padding:6px 10px;">Base</th>
      <th style="border:1px solid #ccc;padding:6px 10px;">+10%</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fce4e4;">
      <td style="border:1px solid #ccc;padding:6px 10px;font-weight:bold;">5.5%</td>
      <td style="border:1px solid #ccc;padding:6px 10px;color:#c62828;">56.2 מ'</td>
      <td style="border:1px solid #ccc;padding:6px 10px;">62.4 מ'</td>
      <td style="border:1px solid #ccc;padding:6px 10px;color:#2e7d32;">68.7 מ'</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:6px 10px;font-weight:bold;">6.0% (Base)</td>
      <td style="border:1px solid #ccc;padding:6px 10px;color:#c62828;">51.5 מ'</td>
      <td style="border:1px solid #ccc;padding:6px 10px;font-weight:bold;">57.2 מ'</td>
      <td style="border:1px solid #ccc;padding:6px 10px;color:#2e7d32;">63.0 מ'</td>
    </tr>
    <tr style="background:#fce4e4;">
      <td style="border:1px solid #ccc;padding:6px 10px;font-weight:bold;">6.5%</td>
      <td style="border:1px solid #ccc;padding:6px 10px;color:#c62828;">47.5 מ'</td>
      <td style="border:1px solid #ccc;padding:6px 10px;">52.8 מ'</td>
      <td style="border:1px solid #ccc;padding:6px 10px;color:#2e7d32;">58.1 מ'</td>
    </tr>
  </tbody>
</table>
</div>

<p>
  טבלה כזו מספקת לאנליסט "מפה" של ערכי הנכס האפשריים — ומדגישה את השינוי
  הגדול הנגרם מתזוזה קטנה ב-Exit Cap Rate.
</p>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  DCF טוב כמו הנחותיו — שנה את Exit Cap ב-1% ותראה כמה ה-"ערך" משתנה.
  DCF אינו אמת — הוא כלי לבחינת הנחות. מי שמציג DCF ללא טבלת רגישות
  מסתיר מידע קריטי. בחן תמיד את <em>מגוון</em> הערכים האפשריים,
  לא רק את התרחיש הבסיסי. שאל: "מה Exit Cap Rate יעביר את הנכס מרווחי להפסדי
  מנקודת מבט ה-LTV?" — זאת השאלה שאנליסט אשראי חייב לשאול.
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מתודולוגיית DCF, חישוב Terminal Value, "
    "בחירת ריבית היוון, וניתוח רגישות על תוצאות ה-DCF. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים בניית תחזית DCF בסיסית לנכס מניב נתון, "
    "חישוב Terminal Value לפי Exit Cap Rate שונים, "
    "ובניית טבלת רגישות DCF לשינויים ב-Exit Cap Rate וב-NOI. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום &mdash; תחזית תזרים ומודל DCF
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>DCF = ערך נוכחי של תזרימי עתידיים + Terminal Value.</strong>
    שלושת מרכיביו: תחזית שנתית, Terminal Value, וריבית היוון.
  </li>
  <li>
    <strong>Terminal Value = NOI(n+1) &divide; Exit Cap Rate — ולרוב מהווה 60%–80% מהשווי.</strong>
    שינוי של 0.5% ב-Exit Cap Rate משפיע יותר על השווי מאשר שינויי NOI של 10%.
  </li>
  <li>
    <strong>ארבע הנחות המפתח: תפוסה, צמיחת שכירות, CAPEX, Exit Cap Rate.</strong>
    כל הנחה חייבת להיות מגובה בנתוני שוק — לא בציפיות אופטימיות בלבד.
  </li>
  <li>
    <strong>WACC משמש לשיוון FCFF; Equity Rate לשיוון FCFE.</strong>
    Cap Rate כ-proxy לריבית היוון הוא פישוט — יש להכיר במגבלותיו.
  </li>
  <li>
    <strong>DCF ללא טבלת רגישות אינו ניתוח שלם.</strong>
    שאלת האנליסט: "מה Exit Cap Rate מוביל את LTV מעל הסף?" &mdash; שאלה זו
    חייבת לקבל תשובה מספרית.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תזרים מהוון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DCF — Discounted Cash Flow</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הערכת שווי לפי ערך נוכחי של תזרימים עתידיים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ערך שיורי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Terminal Value</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שווי הנכס בסוף תקופת התחזית = NOI(n+1) &divide; Exit Cap</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיעור היוון יציאה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Exit Cap Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cap Rate שנשתמש בו להערכת שווי מכירה עתידית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עלות הון ממוצעת משוקללת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">WACC</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ממוצע משוקלל של עלות חוב ועלות הון עצמי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ריבית היוון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Discount Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">השיעור שמשמש להיוון תזרימים עתידיים לערכם הנוכחי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תקופת תחזית מפורשת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Explicit Forecast Period</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שנות התחזית הספציפיות לפני Terminal Value (5–10 שנים)</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לבחינה הסופית:</strong><br>
  השלמתם את שישת מודולי קורס 5 &mdash; ניתוח תזרים מזומנים. למדתם לבנות
  ולנתח תזרים מזומנים תפעולי, להבחין בין NOI ל-FCF, לנתח תזרים יזם בפרופיל
  J-Curve, ולהעריך שווי נכס באמצעות מודל DCF עם ניתוח רגישות.<br><br>
  הבחינה הסופית תכלול שאלות חישוב FCF מנתוני נכס, בניית Terminal Value,
  וניתוח רגישות DCF לשינויי Exit Cap Rate ו-NOI. הגיעו עם הכלים שרכשתם &mdash; ובהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": 'Free Cash Flow בנדל"ן',
        "slug": "free-cash-flow-nadlan",
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
        "title_he": 'תזרים של יזם נדל"ן — ניתוח מעשי',
        "slug": "tizrim-yazam-nituach",
        "estimated_minutes": 55,
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
        "title_he": "תחזית תזרים ומודל DCF",
        "slug": "tachazit-tizrim-dcf",
        "estimated_minutes": 50,
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
    help = "Seed Course 5, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=5)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 5 not found. Run 'python manage.py seed_data' first."
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
