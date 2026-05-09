"""
Management command: seed_c02_content
Seeds Module 1-3 content for Course 2 (יסודות החשבונאות).

Usage:
    python manage.py seed_c02_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": "משוואת החשבונאות וכללי היסוד",
        "slug": "mishvaat-haheshbonaut",
        "estimated_minutes": 45,
    },
    {
        "module_number": 2,
        "title_he": "קריאת דוח רווח והפסד",
        "slug": "kiat-doch-rav-vehefsd",
        "estimated_minutes": 50,
    },
    {
        "module_number": 3,
        "title_he": "קריאת מאזן (Balance Sheet)",
        "slug": "kiat-mazan",
        "estimated_minutes": 50,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>משוואת החשבונאות — הבסיס לכל</h2>

<p>
החשבונאות הפיננסית מבוססת על עיקרון פשוט אחד, שמשמש עמוד שדרה לכל הדוחות הכספיים:
<strong>נכסים = התחייבויות + הון עצמי</strong>. זוהי <em>משוואת החשבונאות (Accounting Equation)</em>,
והיא תמיד, בכל נקודת זמן, חייבת להיות מאוזנת. אם הצד השמאלי גדל, הצד הימני חייב לגדול
בדיוק באותו הסכום — ולהפך.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
נכסים (Assets) = התחייבויות (Liabilities) + הון עצמי (Equity)
</div>

<p>
כל עסקה עסקית — קנייה, מכירה, גיוס הלוואה, תשלום שכר — משפיעה על לפחות שני סעיפים
במשוואה, כך שהאיזון נשמר תמיד. שיטה זו נקראת <strong>שיטת הרישום הכפול (Double-Entry Bookkeeping)</strong>.
</p>

<h3>מה משתנה כאשר עסקאות מתרחשות?</h3>

<p>
בואו נעקוב אחר סדרת עסקאות של חברת נדל"ן ישראלית חדשה — "כוכב נדל"ן בע"מ" — ונראה כיצד
כל עסקה משפיעה על המשוואה:
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה מחושבת — בניית מאזן שלב-אחר-שלב:</strong><br><br>

  <strong>עסקה 1: הקמת החברה — השקעת הון עצמי של 5,000,000 ש"ח</strong><br>
  מזומן ↑ 5,000,000 | הון עצמי ↑ 5,000,000<br>
  <em>נכסים = 5,000,000 | התחייבויות = 0 | הון עצמי = 5,000,000</em><br><br>

  <strong>עסקה 2: נטילת הלוואה בנקאית של 15,000,000 ש"ח</strong><br>
  מזומן ↑ 15,000,000 | הלוואות לטווח ארוך ↑ 15,000,000<br>
  <em>נכסים = 20,000,000 | התחייבויות = 15,000,000 | הון עצמי = 5,000,000</em><br><br>

  <strong>עסקה 3: רכישת קרקע תמורת 12,000,000 ש"ח (במזומן)</strong><br>
  מזומן ↓ 12,000,000 | קרקע ↑ 12,000,000<br>
  <em>נכסים = 20,000,000 (= 8M מזומן + 12M קרקע) | התחייבויות = 15,000,000 | הון עצמי = 5,000,000</em><br><br>

  <strong>עסקה 4: הכנסות שכירות שהתקבלו מראש — 600,000 ש"ח</strong><br>
  מזומן ↑ 600,000 | הכנסות מראש (התחייבות) ↑ 600,000<br>
  <em>נכסים = 20,600,000 | התחייבויות = 15,600,000 | הון עצמי = 5,000,000</em><br><br>

  <strong>עסקה 5: תשלום שכר עובדים — 150,000 ש"ח</strong><br>
  מזומן ↓ 150,000 | יתרת רווחים ↓ 150,000 (הוצאה)<br>
  <em>נכסים = 20,450,000 | התחייבויות = 15,600,000 | הון עצמי = 4,850,000</em><br><br>

  בכל שלב — האיזון נשמר.
</div>

<h2>בסיס מזומן מול בסיס צבירה</h2>

<p>
אחת ההחלטות המהותיות ביותר בחשבונאות היא <em>מתי</em> לרשום הכנסה או הוצאה. שתי שיטות
עיקריות קיימות:
</p>

<h3>בסיס מזומן (Cash Basis)</h3>
<p>
לפי <strong>בסיס מזומן (Cash Basis)</strong>, הכנסות נרשמות כשהכסף מתקבל פיזית, והוצאות
נרשמות כשהכסף משולם בפועל. שיטה זו פשוטה ואינטואיטיבית, אך מעוותת לעיתים את התמונה
הכלכלית האמיתית — במיוחד כאשר קיים פער זמן בין ביצוע העסקה לתשלומה.
</p>

<h3>בסיס צבירה (Accrual Basis)</h3>
<p>
לפי <strong>בסיס צבירה (Accrual Basis)</strong>, הכנסות נרשמות כשהן נצברות — כלומר,
כאשר הזכות לקבל את התמורה נוצרת (גם אם הכסף טרם הגיע). הוצאות נרשמות כשהן מתרחשות
מבחינה כלכלית (גם אם טרם שולמו). זוהי השיטה הנדרשת על-פי IFRS ועל-פי כל תקן
חשבונאות מודרני לחברות ציבוריות ופרטיות גדולות.
</p>

<h3>דוגמה: שכירות מראש</h3>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>תרחיש:</strong> חברת נדל"ן גובה שכירות ל-6 חודשים מראש — 300,000 ש"ח — ב-1 בנובמבר.<br>
  השנה הכספית מסתיימת ב-31 בדצמבר.<br><br>

  <strong>בסיס מזומן:</strong><br>
  300,000 ש"ח נרשמים כהכנסה בנובמבר. הדוח לשנה השוטפת כולל 300,000 ש"ח הכנסה שכירות.<br><br>

  <strong>בסיס צבירה:</strong><br>
  מתוך 6 חודשים, רק 2 חודשים שייכים לשנה הנוכחית (נובמבר–דצמבר).<br>
  הכנסה בשנה הנוכחית: 300,000 × 2/6 = <strong>100,000 ש"ח</strong>.<br>
  200,000 ש"ח נרשמים כ"הכנסות שנגבו מראש" (הכנסות נדחות) — התחייבות שוטפת.<br><br>

  ההפרש אינו טכני — הוא משפיע ישירות על רווח החברה ועל יחסים פיננסיים שמנתחים כאנליסטים.
</div>

<h2>שלושת עקרונות היסוד בחשבונאות</h2>

<h3>1. עקרון ההתאמה (Matching Principle)</h3>
<p>
<strong>עקרון ההתאמה (Matching Principle)</strong> קובע שהוצאות יש לרשום באותה התקופה שבה
הן תרמו להכנסה — לא כשהן שולמו. לדוגמה: עמלת מכירה ששולמה לסוכן עבור מכירת דירה
תירשם כהוצאה בתקופה שבה נרשמה ההכנסה ממכירת הדירה, לא ביום תשלום העמלה.
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל חשוב — עקרון ההתאמה:</strong><br>
  "הכנסות מכוונות הוצאות, לא להיפך." אם נמכרת דירה בנובמבר אך עמלת הסוכן תשולם
  בינואר — ההוצאה עדיין שייכת לנובמבר. כך מבטיחים שהרווח המדווח משקף נאמנה את
  הפעילות הכלכלית של התקופה.
</div>

<h3>2. עקרון השמרנות (Conservatism Principle)</h3>
<p>
<strong>עקרון השמרנות (Conservatism / Prudence Principle)</strong> קובע שבמצב של אי-ודאות,
יש להכיר בהפסדים כאשר הם ידועים (גם אם טרם מומשו), אך לרשום רווחים רק כאשר הם מומשו.
הרעיון: עדיף להגיש דוחות שמרניים ו"תחתיתיים" מאשר אופטימיסטיים שעלולים להטעות משקיעים
ומלווים.
</p>

<p>
לדוגמה: חברת נדל"ן שרכשה קרקע ב-10 מיליון ש"ח, וכעת שווי השוק ירד ל-7 מיליון — תדרש
לרשום ירידת ערך של 3 מיליון ש"ח <em>מיד</em>. לעומת זאת, אם השוויי עלה ל-13 מיליון —
הרישום תלוי במודל החשבונאי שנבחר (שווי הוגן מול עלות).
</p>

<h3>3. הנחת העסק החי (Going Concern Assumption)</h3>
<p>
<strong>הנחת העסק החי (Going Concern)</strong> מניחה שהחברה תמשיך לפעול לעתיד הנראה לעין
(לפחות 12 חודשים קדימה) ואין כוונה לפירוקה. כאשר הנחה זו נשברת — למשל, חברה שנמצאת
על סף חדלות פירעון — הכללים החשבונאיים משתנים: נכסים מוצגים בשווי חיסול (לא בעלות),
והדוחות חייבים לכלול גילוי על הספק להמשכיות.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט — Going Concern:</strong><br>
  בביקורת שנתית, אם רואה החשבון מטיל ספק בהנחת העסק החי — הוא מוסיף הסתייגות
  ("עניין דגש") לחוות הדעת. אנליסט שמקבל דוח עם הסתייגות כזו חייב לסמן אלארם אדום
  לגבי כל הערכות שווי ויחסים פיננסיים. בנייה על הנחת המשכיות כשהחברה אינה עסק חי —
  שגיאה מקצועית חמורה.
</div>

<h2>IFRS מול Israeli GAAP — ההבדלים הרלוונטיים לנדל"ן</h2>

<p>
בישראל קיימים שני מסגרות חשבונאיות עיקריות:
</p>
<ul>
  <li>
    <strong>IFRS (International Financial Reporting Standards)</strong> — תקני הדיווח הבינלאומיים,
    מחייבים לחברות ציבוריות בישראל (הנסחרות בבורסה לניירות ערך). כוללים: IAS, IFRS, SIC, IFRIC.
  </li>
  <li>
    <strong>Israeli GAAP (עקרונות חשבונאות מקובלים בישראל)</strong> — פותחו על-ידי המוסד הישראלי
    לתקינה חשבונאית. חלות בעיקר על חברות פרטיות.
  </li>
</ul>

<h3>IAS 40 — נדל"ן להשקעה</h3>
<p>
<strong>IAS 40 (Investment Property)</strong> הוא התקן המרכזי עבור חברות נדל"ן. הוא מאפשר
שני מודלים לאחר ההכרה הראשונית:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מודל</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">עיקרון</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">השפעה על רווח/הפסד</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מודל שווי הוגן (Fair Value)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הנכס מוצג בשווי שוק נוכחי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שינויים ↑↓ דרך רווח והפסד</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מודל עלות (Cost)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הנכס מוצג בעלות בניכוי פחת</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רק פחת שנתי דרך רווח והפסד</td>
    </tr>
  </tbody>
</table>

<p>
רוב חברות הנדל"ן הציבוריות בישראל (אמות השקעות, גב-ים, מליסרון) בוחרות במודל שווי הוגן —
שמייצר רווחים "נייר" גדולים בשוק עולה, אך יכול להפוך להפסדים כאשר השוק יורד.
</p>

<h3>IFRS 15 — הכרה בהכנסה</h3>
<p>
<strong>IFRS 15 (Revenue from Contracts with Customers)</strong> קובע מתי ואיך לרשום הכנסות.
לחברות ייזום נדל"ן (שמוכרות דירות), IFRS 15 קובע שהכנסה תוכר <em>כשהשליטה עוברת לקונה</em>
— בדרך כלל במסירת הדירה, לא בחתימת חוזה. זה יוצר עיוות: יזם שחתם על מאות חוזי מכר אך
טרם סיים בנייה — מדווח על הכנסות נמוכות ביחס לפעילות הכלכלית האמיתית.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — IFRS בחברות נדל"ן ישראליות:</strong><br><br>
  חברת ייזום שחתמה על 200 חוזי מכר דירות ב-2024 (סך כולל: 400 מיליון ש"ח) תדווח על
  הכנסות אלה רק ב-2025–2026, עם מסירות הדירות. בינתיים, 400 מיליון ש"ח יופיעו כ"חוזים
  שטרם הושלמו" (Liabilities / Contract Liabilities). אנליסט שמסתכל רק על דוח הרווח
  יפספס לחלוטין את ה-backlog האמיתי של החברה.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט — רווח צבירה ≠ תזרים מזומנים:</strong><br><br>
  חברת נדל"ן יכולה לדווח על רווח נאה לפי עקרון הצבירה — הכנסות שנצברו אך טרם
  נגבו — ובמקביל להיות בלחץ תזרימי חמור. הבנק שמממן אותה מסתכל על <em>תזרים
  מזומנים מפעילות שוטפת (CFO)</em> ולא רק על שורת הרווח. תמיד השלם ניתוח רווח
  בניתוח תזרים.
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — משוואת החשבונאות וכללי היסוד</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>משוואת החשבונאות:</strong> נכסים = התחייבויות + הון עצמי. האיזון נשמר תמיד,
    בכל עסקה, בשיטת הרישום הכפול.
  </li>
  <li>
    <strong>בסיס מזומן מול בסיס צבירה:</strong> IFRS מחייב בסיס צבירה — הכנסות נרשמות
    לפי זכות כלכלית, לא לפי תזרים מזומנים. ההפרש בין השניים יכול להיות ענק בחברות נדל"ן.
  </li>
  <li>
    <strong>עקרון ההתאמה:</strong> הוצאות נרשמות בתקופה שבה הן תרמו להכנסה — מבטיח
    שהרווח משקף נאמנה את הפעילות הכלכלית.
  </li>
  <li>
    <strong>עקרון השמרנות:</strong> הפסדים — מוכרים מיד. רווחים — רק כשמומשו.
    מגן על משתמשי הדוחות מפני אופטימיות יתר.
  </li>
  <li>
    <strong>IFRS בנדל"ן:</strong> IAS 40 מאפשר מודל שווי הוגן (רווחים/הפסדי נייר דרך
    רווח והפסד) ו-IFRS 15 קובע הכרה בהכנסה רק עם מסירת הדירה.
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
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכסים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Assets</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">משאבים בשליטת העסק שיצרו הטבה כלכלית עתידית</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">התחייבויות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Liabilities</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חובות ועל-ידי צד שלישי — בנקים, ספקים, רשויות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הון עצמי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Equity</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">זכות הבעלים בנכסי החברה לאחר קיזוז ההתחייבויות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בסיס מזומן</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Cash Basis</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רישום הכנסות/הוצאות רק עם תנועת מזומן בפועל</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בסיס צבירה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Accrual Basis</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רישום לפי זכות/חובה כלכלית, ללא קשר לתזרים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עקרון ההתאמה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Matching Principle</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הוצאות בתקופה שבה תרמו להכנסה</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עקרון השמרנות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Conservatism</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הפסדים — מוכרים מיד; רווחים — רק עם מימוש</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עסק חי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Going Concern</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הנחה שהחברה תמשיך לפעול ל-12 חודשים לפחות</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
כעת, לאחר שביססנו את מסגרת החשבונאות — המשוואה הבסיסית, שיטת הצבירה, ועקרונות היסוד —
נוכל לעבור ל<em>מודול 2</em>: קריאת <strong>דוח רווח והפסד (P&L)</strong>. נבין כיצד
הכנסות, עלויות ורווחים מוצגים בדוח, ומדוע מדד ה-EBITDA כל-כך מרכזי בניתוח אשראי נדל"ני.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>מבנה דוח רווח והפסד (Income Statement / P&L)</h2>

<p>
<strong>דוח רווח והפסד (Profit and Loss Statement)</strong> מציג את כל ההכנסות וההוצאות
של חברה לתקופה מסוימת (רבעון, שנה), ומסכם בשורת הרווח הנקי. בניגוד למאזן — שהוא
"תצלום" של יום אחד — דוח הרווח מספר סיפור של <em>תהליך</em> לאורך זמן.
</p>

<h3>המבנה ההיררכי של דוח רווח והפסד</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
הכנסות (Revenue)<br>
— עלות המכר (COGS)<br>
= רווח גולמי (Gross Profit)<br>
— הוצאות תפעוליות (Operating Expenses: SG&amp;A, R&amp;D)<br>
= EBIT (Earnings Before Interest and Tax)<br>
— הוצאות מימון (Finance Costs)<br>
+ הכנסות מימון<br>
= EBT (Earnings Before Tax)<br>
— מס חברות (Income Tax)<br>
= רווח נקי (Net Income)
</div>

<h3>דוגמה מספרית — חברת נדל"ן ישראלית</h3>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוח רווח והפסד — "מגדל נדל"ן בע"מ" — שנת 2024 (באלפי ש"ח)</strong><br><br>

  <table style="border-collapse:collapse;width:100%;margin:12px 0;">
    <tbody>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;"><strong>הכנסות שכירות</strong></td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;">48,000</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">עלות שירותי ניהול ואחזקה</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;">(12,000)</td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;"><strong>רווח גולמי</strong></td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;"><strong>36,000</strong></td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">הוצאות הנהלה וכלליות</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;">(4,500)</td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">פחת והפחתות</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;">(3,200)</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;"><strong>EBIT (רווח תפעולי)</strong></td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;"><strong>28,300</strong></td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">הוצאות ריבית על הלוואות</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;">(8,700)</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;"><strong>EBT (לפני מס)</strong></td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;"><strong>19,600</strong></td>
      </tr>
      <tr>
        <td style="padding:7px;border:1px solid #ddd;text-align:right;">מס חברות (23%)</td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;">(4,508)</td>
      </tr>
      <tr style="background:#e8f5e9;">
        <td style="padding:7px;border:1px solid #ddd;text-align:right;"><strong>רווח נקי</strong></td>
        <td style="padding:7px;border:1px solid #ddd;text-align:left;"><strong>15,092</strong></td>
      </tr>
    </tbody>
  </table>

  EBITDA = EBIT + פחת = 28,300 + 3,200 = <strong>31,500 אלפי ש"ח</strong>
</div>

<h2>EBITDA — מדד ניתוח האשראי המרכזי</h2>

<p>
<strong>EBITDA (Earnings Before Interest, Taxes, Depreciation and Amortization)</strong>
הוא מדד הרווחיות שאנליסטי אשראי ובנקים משתמשים בו יותר מכל מדד אחר.
</p>

<h3>מדוע אנליסטים מעדיפים EBITDA?</h3>
<ul>
  <li>
    <strong>מבטל השפעת מבנה ההון:</strong> ריבית תלויה בכמה חוב לקחה החברה — ולא
    בביצועי הליבה. EBITDA מאפשר השוואה בין חברות עם מינוף שונה.
  </li>
  <li>
    <strong>מבטל השפעת שיטות ריבית ומדיניות מס:</strong> מאפשר השוואה בינלאומית.
  </li>
  <li>
    <strong>מבטל פחת — הוצאה שאינה תזרימית:</strong> פחת "עולה" ברווח והפסד אך לא
    "יוצא" מהבנק. EBITDA קרוב יותר לתזרים המזומנים מהפעילות.
  </li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
EBITDA = רווח נקי + ריבית + מסים + פחת + הפחתות<br>
 — או —<br>
EBITDA = EBIT + פחת + הפחתות
</div>

<h3>מכפיל EBITDA (EV/EBITDA)</h3>
<p>
יחס <strong>EV/EBITDA</strong> (ערך הארגון חלקי EBITDA) הוא יחס הערכת שווי סטנדרטי
לחברות נדל"ן מניב. מכפיל של 12–16 נחשב נורמלי בשוק הישראלי (תלוי ריבית ואיכות נכסים).
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — EBITDA אינו תזרים מזומנים!</strong><br><br>
  EBITDA מבטל פחת — אך לא כל הוצאות ההון (CAPEX). חברת נדל"ן שמשקיעה מיליונים
  בשיפוץ נכסים תציג EBITDA גבוה, בעוד שתזרים החופשי שלה שלילי. תמיד בדוק
  <em>Free Cash Flow = EBITDA − CAPEX − שינוי הון חוזר − ריבית</em> לפני קביעת
  עמידה בהתחייבויות פיננסיות (Debt Service Coverage).
</div>

<h2>הוצאות מימון (Finance Costs)</h2>

<p>
<strong>הוצאות מימון (Finance Costs)</strong> כוללות את עלות ה"כסף השאול" — ריבית על
הלוואות, הפרשי שער מטבע, ורכיבים נוספים. הן מופיעות <em>מתחת ל-EBIT</em> — לאחר
הרווח התפעולי — כי הן תוצאה של מבנה ההון, לא של הפעילות העסקית עצמה.
</p>

<h3>הפרשי שער (Exchange Rate Differences)</h3>
<p>
חברות נדל"ן ישראליות הלוות דולרים או אירו לרכישת נכסים בחו"ל — ושינויי שער שקל/דולר
מייצרים הוצאות/הכנסות מימון שעלולות להיות גדולות מהרווח התפעולי. אנליסט צריך
להפריד בין הוצאות מימון "קבועות" (ריבית) לבין "חד-פעמיות" (הפרשי שער).
</p>

<h2>מס חברות ומס נדחה (Deferred Tax)</h2>

<p>
שיעור <strong>מס חברות בישראל הוא 23%</strong> (החל מ-2018). אולם, הסכום שמשולם
בפועל לרשות המסים לרוב שונה מהמס המחושב לפי IFRS — עקב הבדלים בשיטות פחת, עיתוי
ההכרה בהכנסות, ורכיבים אחרים.
</p>

<p>
ההפרש נרשם כ<strong>מס נדחה (Deferred Tax)</strong>: אם ה-IFRS מכיר בהכנסה לפני שהמס
נדרש לשלמה, נוצרת <em>התחייבות מס נדחה</em>. אם ה-IFRS מכיר בהוצאה לפני שמס מאשר
אותה, נוצר <em>נכס מס נדחה</em>.
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל חשוב — מס נדחה בנדל"ן להשקעה (IAS 40):</strong><br><br>
  חברה שבחרה במודל שווי הוגן מכירה ברווחי שערוך בדוח הרווח — אך לא משלמת עליהם
  מס עד למימוש הנכס. לכן נוצרת <em>התחייבות מס נדחה</em> גדולה, שמופיעה במאזן
  כהתחייבות. בניתוח אשראי — יש לבחון האם בתרחיש מכירה עתידית, מס זה יהפוך לתשלום
  מזומן ממשי שיפגע בנזילות.
</div>

<h2>OCI — רווח כולל אחר (Other Comprehensive Income)</h2>

<p>
לא כל שינויי שווי עוברים דרך שורת הרווח הנקי. <strong>OCI (Other Comprehensive Income)</strong>
הוא "מגירה" חשבונאית שמאפשרת לרשום שינויי שווי מסוימים <em>ישירות להון עצמי</em>,
מבלי לעבור דרך דוח הרווח. הדוגמה הנפוצה בנדל"ן:
</p>
<ul>
  <li>
    שערוך נכסים שבחר החברה למדוד לפי <strong>מודל שערוך (Revaluation Model) תחת IAS 16</strong>
    (לרכוש קבוע) — עלייה בשווי עוברת ל-OCI כ"עודף שערוך", ירידה עוברת ישירות לרווח
    והפסד.
  </li>
  <li>
    שינויים בשווי הוגן של <strong>נגזרים לגידור (Hedging Instruments)</strong>.
  </li>
  <li>
    הפרשי תרגום של פעילויות חוץ.
  </li>
</ul>

<p>
בחברות נדל"ן שבחרו מודל שווי הוגן לפי <strong>IAS 40</strong> — שינויי שווי <em>כן</em>
עוברים דרך הרווח והפסד (לא OCI). זהו ייחוד של IAS 40 לעומת IAS 16.
</p>

<h2>הכנסות חוזרות לעומת חד-פעמיות</h2>

<p>
אחת המיומנויות המרכזיות של אנליסט אשראי היא להבחין בין <strong>הכנסות חוזרות
(Recurring Revenue)</strong> — שניתן לסמוך עליהן בשנים הבאות — לבין <strong>פריטים
חד-פעמיים (One-time Items)</strong> שאינם ישנן לאחר מכן.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — מכירת נכס להשקעה:</strong><br><br>
  חברת נדל"ן מניבה מוכרת בניין משרדים ב-80,000 אלפי ש"ח (שעלות בספרים שלו 60,000).
  רווח ממכירה: 20,000 אלפי ש"ח — מופיע בדוח הרווח כ"רווח ממימוש נכסים".<br><br>
  <strong>ה-EBITDA המדווח:</strong> 31,500 + 20,000 = 51,500 אלפי ש"ח.<br>
  <strong>ה-EBITDA המתואם (Adjusted EBITDA):</strong> 31,500 אלפי ש"ח — זו הנתון שמייצג את
  הרווחיות האמיתית החוזרת של החברה. הבנק ישתמש ב-Adjusted EBITDA בחישוב יחס כיסוי החוב.
</div>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — כיצד אנליסטים מתאמים EBITDA:</strong><br><br>
  בוועדת אשראי ישראלית, האנליסט מציג טבלת "EBITDA מתואם" שמנטרלת:<br>
  - רווחי/הפסדי שערוך נדל"ן (אם מודל שווי הוגן)<br>
  - רווחי מכירת נכסים<br>
  - הוצאות חד-פעמיות (פיצויים, הוצאות ייסוד)<br>
  - הפרשי שער חד-פעמיים<br><br>
  רק לאחר תיאום זה, מחשבים את יחס כיסוי שירות החוב (DSCR):
  DSCR = EBITDA מתואם ÷ (ריבית + קרן שנתית)
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — קריאת דוח רווח והפסד</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>מבנה P&L:</strong> הכנסות → רווח גולמי → EBIT → EBT → רווח נקי.
    כל שלב מנטרל רובד אחר של עלויות.
  </li>
  <li>
    <strong>EBITDA:</strong> מדד הרווחיות המרכזי לאנליסטים — מבטל פחת, ריבית ומס.
    מאפשר השוואה בין חברות. אינו תחליף לתזרים חופשי.
  </li>
  <li>
    <strong>הוצאות מימון:</strong> מופיעות מתחת ל-EBIT. כוללות ריבית והפרשי שער.
    יש להפריד בין קבועות לחד-פעמיות.
  </li>
  <li>
    <strong>מס חברות ומס נדחה:</strong> 23% בישראל; מס נדחה נוצר מהפרש עיתוי בין IFRS
    לפקיד השומה. בנדל"ן להשקעה — התחייבות מס נדחה גדולה עקב שערוכים.
  </li>
  <li>
    <strong>הכנסות חד-פעמיות:</strong> מכירת נכסים, שערוכים ופריטים חריגים מנפחים את
    הרווח המדווח. Adjusted EBITDA — הנתון שמשקף יכולת החזר חוב.
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
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">EBITDA</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">EBITDA</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווח לפני ריבית, מס, פחת והפחתות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">EBIT</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">EBIT</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווח תפעולי — לפני ריבית ומס (כולל פחת)</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווח גולמי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Gross Profit</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הכנסות פחות עלות המכר הישירה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הכנסות חזרתיות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Recurring Revenue</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הכנסה שניתן לצפות להמשכה גם בשנים הבאות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הכנסה חד-פעמית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">One-time Item</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הכנסה/הוצאה שאינה צפויה להישנות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">OCI</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">OCI</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווח כולל אחר — שינויי שווי ישירות להון, מחוץ ל-P&L</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מס נדחה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Deferred Tax</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הפרש עיתוי בין חשבונאות IFRS לדיווח מס</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעור מס</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Tax Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">23% מס חברות בישראל (2024)</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
דוח רווח והפסד מספר לנו על הביצועים לאורך תקופה. כעת נפנה ל<em>מודול 3</em>:
<strong>קריאת מאזן (Balance Sheet)</strong> — תצלום הנכסים, ההתחייבויות וההון העצמי
ביום מסוים. נבין את קטגוריות הנכסים הייחודיות לחברות נדל"ן (IAS 40 ו-IAS 2),
ונחשב יחסי נזילות ויחסי מינוף שהם לחם חוק של אנליסט אשראי.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>מבנה המאזן (Balance Sheet)</h2>

<p>
<strong>המאזן (Balance Sheet)</strong>, המכונה בשפה החשבונאית הבינלאומית גם
<em>Statement of Financial Position</em>, מציג "תצלום" של החברה ביום מסוים:
כל נכסיה, כל התחייבויותיה, וסך ההון העצמי של בעלי המניות. הוא מיישם את משוואת
החשבונאות שלמדנו במודול 1 — ותמיד מאוזן.
</p>

<h3>המבנה הסטנדרטי</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
נכסים שוטפים (Current Assets)<br>
  + מזומן ושווי מזומן<br>
  + לקוחות וחייבים<br>
  + מלאי (דירות בפיתוח)<br>
  + נכסים שוטפים אחרים<br>
נכסים לא-שוטפים (Non-Current Assets)<br>
  + רכוש קבוע (PP&amp;E)<br>
  + נדל"ן להשקעה (IAS 40)<br>
  + נכסים בלתי-מוחשיים<br>
= סך נכסים<br>
<br>
התחייבויות שוטפות (Current Liabilities)<br>
  + ספקים וזכאים<br>
  + חלויות שוטפות של הלוואות ארוכות-מועד<br>
  + הכנסות נדחות (שכירות מראש)<br>
התחייבויות לא-שוטפות (Non-Current Liabilities)<br>
  + הלוואות ארוכות-מועד<br>
  + אגרות חוב<br>
  + מס נדחה<br>
= סך התחייבויות<br>
<br>
הון עצמי (Equity)<br>
  + הון רשום<br>
  + פרמיית הנפקה<br>
  + יתרת רווחים<br>
  + עודפי שערוך (OCI)<br>
= סך הון עצמי<br>
<br>
סך התחייבויות + הון עצמי = סך נכסים ✓
</div>

<h2>הון חוזר ויחסי נזילות</h2>

<p>
<strong>הון חוזר (Working Capital)</strong> הוא ההפרש בין הנכסים השוטפים להתחייבויות
השוטפות, ומשקף את יכולת החברה לעמוד בהתחייבויותיה לטווח קצר.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
הון חוזר = נכסים שוטפים − התחייבויות שוטפות
</div>

<h3>יחס שוטף (Current Ratio)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
יחס שוטף = נכסים שוטפים ÷ התחייבויות שוטפות
</div>

<p>
ספים מקובלים: יחס שוטף <strong>מעל 1.5</strong> נחשב בריא; מתחת ל-1.0 — אלארם אדום.
בחברות נדל"ן ישראליות, יחס שוטף של 1.2–2.0 נפוץ בשוק עולה; בשוק יורד, יחסים
נמוכים מ-1.0 אינם נדירים.
</p>

<h3>יחס מהיר (Quick Ratio)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
יחס מהיר = (מזומן + השקעות לטווח קצר + לקוחות) ÷ התחייבויות שוטפות
</div>

<p>
היחס המהיר מנטרל את <strong>המלאי</strong> — שהוא הנכס הכי פחות נזיל מבין הנכסים השוטפים.
בחברות ייזום נדל"ן, המלאי (דירות בפיתוח) עשוי להוות 70%–85% מהנכסים השוטפים — ולכן
הפער בין יחס שוטף ליחס מהיר יכול להיות עצום.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — חברת ייזום ישראלית:</strong><br><br>
  נכסים שוטפים: 120,000 אלפי ש"ח<br>
  — מתוכם מלאי דירות בפיתוח: 95,000 אלפי ש"ח<br>
  — מזומן ולקוחות: 25,000 אלפי ש"ח<br>
  התחייבויות שוטפות: 80,000 אלפי ש"ח<br><br>
  יחס שוטף = 120,000 ÷ 80,000 = <strong>1.50</strong> (נראה בסדר)<br>
  יחס מהיר = 25,000 ÷ 80,000 = <strong>0.31</strong> (סכנה! ללא מכירת דירות — אין נזילות)
</div>

<h2>קטגוריות נכסים מרכזיות בחברות נדל"ן</h2>

<h3>נכסים שוטפים (Current Assets)</h3>
<p>
<strong>נכסים שוטפים</strong> הם נכסים שצפויים להפוך למזומן תוך 12 חודשים:
</p>
<ul>
  <li><strong>מזומן ושווי מזומן:</strong> פיקדונות בנקאיים עד 3 חודשים, ני"ע סחירים לטווח קצר.</li>
  <li><strong>לקוחות (Trade Receivables):</strong> שכירות שנצברה אך טרם נגבתה.</li>
  <li><strong>מלאי דירות בפיתוח:</strong> דירות שהחברה בונה למכירה — מוצגות לפי IAS 2 (עלות או שווי מימוש נטו, הנמוך).</li>
</ul>

<h3>רכוש קבוע — PP&E (Property, Plant and Equipment)</h3>
<p>
<strong>רכוש קבוע (PP&E)</strong> כולל מבנים תפעוליים, ציוד, כלי רכב. מוצג <em>בערך פנקסני
(NBV — Net Book Value)</em>: עלות מקורית בניכוי פחת מצטבר. הפחת נרשם כהוצאה שנתית בדוח
הרווח, אך לא יוצא כמזומן.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
NBV = עלות מקורית − פחת מצטבר<br>
הוצאת פחת שנתית = עלות ÷ אורך חיים שימושי (שנים)
</div>

<h3>נדל"ן להשקעה — IAS 40 (Investment Property)</h3>
<p>
<strong>נדל"ן להשקעה (Investment Property)</strong> הוא נכס נדל"ן שמוחזק לצורך <em>השכרה</em>
או <em>עליית ערך</em> — ולא לשימוש עצמי של החברה ולא לצורך מכירה בפעילות הרגילה.
לדוגמה: בניין משרדים שהחברה משכירה לדיירים חיצוניים.
</p>

<p>
תחת IAS 40, החברה בוחרת בין שני מודלים:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">קריטריון</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מודל שווי הוגן (Fair Value)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מודל עלות (Cost)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ערך הנכס במאזן</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שווי שוק עדכני</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עלות פחות פחת מצטבר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שינוי שווי → לאן?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">דרך רווח והפסד (P&L)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אין הכרה בעליית ערך</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פחת?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לא (אין פחת)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כן — פחת שנתי לפי אורך חיים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מס נדחה?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גדול — עקב עליות שווי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מוגבל יחסית</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נפוץ ב...</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חברות ציבוריות ישראליות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חברות פרטיות קטנות יותר</td>
    </tr>
  </tbody>
</table>

<h3>מלאי דירות בפיתוח — IAS 2 / IFRS 15</h3>
<p>
דירות שחברת ייזום בונה <em>למכירה</em> מסווגות כ<strong>מלאי (Inventory)</strong> לפי
<strong>IAS 2</strong>, לא כנדל"ן להשקעה. לא ניתן לבחור מודל שווי הוגן — הן מוצגות
בעלות (כולל עלויות בנייה, עלויות מימון ועלויות קרקע), ולא מעל שווי מימוש נטו (NRV).
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל חשוב — ההבחנה IAS 40 לעומת IAS 2:</strong><br><br>
  אם החברה תשכיר את הדירה — IAS 40 (נדל"ן להשקעה, אפשרות שווי הוגן).<br>
  אם החברה תמכור את הדירה — IAS 2 (מלאי, בעלות בלבד).<br><br>
  זוהי שאלה שמשפיעה דרמטית על ה"עושר" שמציג המאזן. בחברה שמציגה נדל"ן להשקעה
  בשווי הוגן — המאזן מצביע על שווי שוק עדכני. בחברה שמציגה מלאי — המאזן מציג
  עלות היסטורית שעשויה להיות נמוכה מהשווי הכלכלי.
</div>

<h2>מרכיבי ההון העצמי</h2>

<p>
<strong>הון עצמי (Shareholders' Equity)</strong> הוא מה שנשאר לבעלי המניות לאחר
קיזוז כל ההתחייבויות מהנכסים. הוא מורכב ממספר רכיבים:
</p>

<ul>
  <li>
    <strong>הון רשום (Share Capital / Registered Capital):</strong> ערך נקוב של המניות
    שהונפקו. בדרך כלל סכום קטן (1 אגורה למניה).
  </li>
  <li>
    <strong>פרמיית הנפקה (Share Premium):</strong> ההפרש בין מחיר ההנפקה לבין הערך הנקוב.
    כשחברה מנפיקה מניה בנקוב 1 אגורה במחיר של 10 ש"ח — 9.99 ש"ח הם פרמיית הנפקה.
  </li>
  <li>
    <strong>יתרת רווחים (Retained Earnings):</strong> רווחים מצטברים שלא חולקו כדיבידנד.
    המדד הטוב ביותר לצמיחת ערך כרונולוגי.
  </li>
  <li>
    <strong>עודפי שערוך (Revaluation Reserve / OCI):</strong> עליות שווי שעברו ישירות
    להון מבלי לעבור דרך רווח והפסד (לדוגמה: גידור, תרגום מטבע).
  </li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — חישוב הון עצמי:</strong><br><br>
  הון רשום: 1,000 אלפי ש"ח<br>
  פרמיית הנפקה: 49,000 אלפי ש"ח<br>
  יתרת רווחים: 85,000 אלפי ש"ח<br>
  עודף שערוך OCI: 12,000 אלפי ש"ח<br>
  <strong>סך הון עצמי: 147,000 אלפי ש"ח</strong><br><br>
  אם סך הנכסים = 420,000 אלפי ש"ח, סך ההתחייבויות = 273,000 אלפי ש"ח.<br>
  יחס מינוף = חוב ÷ הון = 273,000 ÷ 147,000 = <strong>1.86 — כלומר כ-65% מימון חוב</strong>.
</div>

<h2>אזהרת אנליסט — "הרווח אינו מזומן"</h2>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט — הון חיובי ≠ נזילות!</strong><br><br>
  חברת נדל"ן יכולה להציג:<br>
  ✓ הון עצמי חיובי (400 מיליון ש"ח)<br>
  ✓ רווח נקי חיובי (50 מיליון ש"ח — בעיקר מרווחי שערוך IAS 40)<br>
  ✗ תזרים מפעילות שוטפת שלילי (−30 מיליון ש"ח)<br><br>
  הסיבה: רווח השערוך הוא "נייר" — מוצג בדוח הרווח אך לא מגיע לבנק. החברה
  צריכה לשלם ריבית, שכר ומסים במזומן — ואם אין מזומן, קורסת גם עם מאזן "יפה".
  אנליסט אשראי שמסתכל רק על הון עצמי ורווח נקי ומתעלם מדוח תזרים המזומנים —
  מפסיד את התמונה האמיתית.
</div>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — קריאת מאזן (Balance Sheet)</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>מבנה המאזן:</strong> נכסים שוטפים + נכסים לא-שוטפים = התחייבויות שוטפות
    + התחייבויות לא-שוטפות + הון עצמי. תמיד מאוזן.
  </li>
  <li>
    <strong>הון חוזר ויחסי נזילות:</strong> יחס שוטף מעל 1.5 — בריא; יחס מהיר מתחת ל-0.5
    בחברת ייזום — אלארם. בחברות עם מלאי גבוה, שני היחסים יכולים להיות שונים בתהום.
  </li>
  <li>
    <strong>IAS 40 (נדל"ן להשקעה):</strong> מודל שווי הוגן מציג שווי שוק עדכני; שינויים
    דרך רווח והפסד. מגדיל רווחים "נייריים" ומייצר מס נדחה גדול.
  </li>
  <li>
    <strong>IAS 2 (מלאי דירות):</strong> דירות למכירה = מלאי בעלות. לא שווי הוגן.
    המאזן מציג עלות היסטורית שעשויה להיות שמרנית.
  </li>
  <li>
    <strong>הון חיובי ≠ נזילות:</strong> רווחי שערוך IAS 40 מנפחים הון עצמי ורווח
    ללא תזרים מזומנים. תמיד השלם ניתוח מאזן בניתוח דוח תזרים.
  </li>
</ol>

<h3>מילון מושגים — מודול 3</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מונח בעברית</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">English</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכסים שוטפים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Current Assets</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכסים שיהפכו למזומן תוך 12 חודשים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הון חוזר</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Working Capital</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכסים שוטפים פחות התחייבויות שוטפות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">יחס שוטף</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Current Ratio</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכסים שוטפים ÷ התחייבויות שוטפות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">יחס מהיר</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Quick Ratio</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">(מזומן + לקוחות) ÷ התחייבויות שוטפות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נדל"ן להשקעה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Investment Property (IAS 40)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכס המוחזק להשכרה/עליית ערך — לא למכירה שוטפת</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שווי הוגן</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Fair Value</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מחיר שהיה מתקבל במכירה בין צדדים מרצון</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מלאי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Inventory (IAS 2)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">דירות בפיתוח/מוכנות למכירה — בעלות, לא שווי הוגן</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">יתרת רווחים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Retained Earnings</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווחים מצטברים שלא חולקו — צמיחת ערך לאורך השנים</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
כעת יש בידינו את שלוש הרגליים של הדיווח הכספי: משוואת החשבונאות, דוח רווח והפסד,
ומאזן. <em>מודול 4</em> יסגור את המעגל עם <strong>דוח תזרים המזומנים (Cash Flow Statement)</strong> —
הדוח שמגלה מה קרה בפועל לכסף, ומדוע חברה רווחית יכולה להיכנס לקשיים תזרימיים.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = "Seeds Module 1-3 reading and summary content for Course 2 (יסודות החשבונאות)"

    def handle(self, *args, **options) -> None:
        # ── Locate Course 2 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=2)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=2 not found. "
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

        self.stdout.write(self.style.SUCCESS("\nAll done — Course 2 modules 1-3 seeded successfully."))

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
