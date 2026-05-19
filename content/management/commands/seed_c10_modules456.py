"""
Seeds Module 4-6 content for Course 10 (ניתוח תרחישי סיכון).
Usage: python manage.py seed_c10_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — תרחישי לווה — Early Warning Signals
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  תרחישי לווה — Early Warning Signals
</h2>

<!-- ===== סעיף 1 — סיכון עסקה לעומת סיכון לווה ===== -->
<h3 style="color:#1a2638;">1. סיכון ברמת העסקה לעומת סיכון ברמת הלווה</h3>

<p>
  בניתוח אשראי נדל&quot;ן קיימים שני מישורי סיכון שיש לנתח בנפרד:
  <strong>סיכון ברמת העסקה (Deal-Level Stress)</strong> —
  שאלה אם הנכס הספציפי יכול לשרת את חובו — לעומת
  <strong>סיכון ברמת הלווה (Borrower-Level Stress)</strong> —
  שאלה אם הלווה עצמו, כגוף עסקי ואנושי, יכול לעמוד בהתחייבויותיו.
</p>

<p>
  ניתן שנכס יצליח — תפוסה גבוהה, DSCR חיובי — אך הלווה יכשל בגלל
  חובות ממינופים אחרים, ערבויות אישיות שהופעלו, או חולשה עסקית כוללת.
  ניתן גם שהלווה חזק — אך הנכס הספציפי חלש, ועלולה להיווצר שאלה אם
  הוא יתמוך בנכס או ישאיר אותו לצלול. אנליסט מיומן בוחן את שניהם.
</p>

<!-- ===== סעיף 2 — Early Warning Signals ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. Early Warning Signals — מסגרת שלושת הסימנים</h3>

<p>
  <strong>Early Warning Signals (EWS)</strong> הם אינדיקטורים מוקדמים
  המאותתים על הרעה במצב הלווה לפני שמתחיל פיגור. ניתן לחלקם לשלוש קטגוריות:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">קטגוריה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">אות אזהרה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">משמעות</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;" rowspan="2">פיננסי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR במגמת ירידה רבעון אחר רבעון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI נשחק או שירות חוב עולה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">LTV בעלייה הדרגתית ("LTV Creep")</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שווי הנכס יורד יחסית ליתרת ההלוואה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;" rowspan="2">תפעולי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דחיית אחזקה נדחית (Deferred Maintenance)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלווה מצמצם הוצאות שוטפות — אות למצוקת מזומן</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוכר עוגן שלא חידש חוזה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI עלול לצנוח ברבעון הקרוב</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;" rowspan="2">התנהגותי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">איחור בהגשת דוחות כספיים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">לווה שמסתיר מידע או בלחץ</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">בקשה לוויתור על Covenant (Waiver Request)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלווה יודע שהוא יפר — מבקש הגנה מראש</td>
    </tr>
  </tbody>
</table>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>ביקורת שנתית של Covenants — לא פורמליות:</strong><br>
  ביקורת שנתית של Covenants אינה פורמליות — היא קו ההגנה הראשון.
  אנליסט שמציין "עמד בכל התנאים" מבלי לבדוק מגמות, מחמיץ את הסכנה
  הגדולה ביותר: לווה שעדיין עומד — אך בקושי, ומגמת ה-DSCR שלו יורדת.
</div>

<!-- ===== סעיף 3 — Watch List ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. קריטריוני Watchlist — מתי הלוואה עוברת מ"ביצוע" ל"מעקב"</h3>

<p>
  <strong>Watchlist</strong> הוא סיווג פנימי שמאותת שהלוואה מצריכה
  ניטור הדוק יותר — אך טרם הגיעה לסיווג NPL רשמי. קריטריונים מקובלים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>DSCR ירד מתחת ל-1.10</strong> ברבעון אחד, או מראה מגמת
    ירידה של 0.10+ בשני רבעונים רצופים.
  </li>
  <li>
    <strong>LTV עלה מעל 70%–75%</strong> בנכס מסחרי — בין אם בגלל
    ירידת שווי או עלייה בחוב.
  </li>
  <li>
    <strong>איחור בדיווח</strong> ברבעון אחד, או בקשת Waiver ל-Covenant
    כלשהו.
  </li>
  <li>
    <strong>שינוי מהותי בהרכב השוכרים</strong> — אובדן שוכר מעל 20%
    מה-NOI — ללא שוכר חלופי חתום.
  </li>
</ul>

<!-- ===== סעיף 4 — תרחיש פיננסי של לווה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. תרחיש פיננסי של לווה — ירידת הכנסות, הצטברות חוב, חולשת ערב</h3>

<p>
  ניתוח תרחיש לווה מבוצע ברמת הקבוצה העסקית — לא רק ברמת הנכס.
  שלושת הגורמים המסוכנים ביותר:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>ירידת הכנסות (Revenue Decline):</strong> חברת ניהול הנכס
    מאבדת שוכרים, או שוק השכירות מתמתן. NOI יורד, DSCR נשחק.
    בתרחיש קיצון — הנכס לא מכסה את שירות החוב, והלווה צריך להזרים
    הון עצמי כדי לשלם לבנק.
  </li>
  <li>
    <strong>הצטברות חוב (Debt Pile-Up):</strong> לווה שמינף מספר נכסים
    במקביל — אם נכס אחד "שובר" את מבנה ההחזר, הוא עלול לפגוע
    בנזילות שמשרתת גם את ההלוואה אצלנו.
  </li>
  <li>
    <strong>חולשת ערב (Guarantor Weakness):</strong> ערב אישי שחוסנו
    הפיננסי נשחק — עקב מינוף אישי, פסק-דין, או פשיטת רגל של גוף אחר
    שבו הוא מעורב — פוחת כבטוחה גם כשהנכס עצמו תקין.
  </li>
</ul>

<!-- ===== סעיף 5 — Red Flag Checklist ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. Red Flag Checklist לביקורת Covenant שנתית</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">#</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">בדיקה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דגל אדום</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">1</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מגמת DSCR השנתית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ירידה מצטברת מעל 0.15 בשנתיים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">2</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שינוי ב-LTV (עדכון שמאות)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">LTV עלה ב-5 נקודות+ מאז הלוואה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">3</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רשימת שוכרים + מועדי פקיעת חוזה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוכר עוגן מסתיים ב-12 חודש הקרוב ללא חידוש</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">4</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דוחות כספיים — תאריך הגשה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דוחות הוגשו באיחור של 30+ יום</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">5</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דוחות ערב אישי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נטו שווי ירד ב-20%+, חובות חדשים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">6</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בקשות Waiver / שינוי תנאים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כל בקשת Waiver — בצע ניתוח עומק</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">7</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אחזקת הנכס — ביקור פיזי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בעיות תחזוקה גלויות, חניות ריקות</td>
    </tr>
  </tbody>
</table>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  לווה שמאחר בהגשת דוח אחד בלבד — סטטיסטית פי 3 יותר סביר לאחר
  בתשלום בשנה הקרובה. איחור בדיווח הוא לא שאלה של ניהול זמן —
  הוא אות לכך שמשהו בלחץ.
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = "<p>ענה על שאלות ההבנה הבאות.</p>"

M4_EXERCISES_INSTRUCTIONS = "<p>פתור את התרגילים הבאים.</p>"

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — תרחישי לווה — Early Warning Signals
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>סיכון ברמת הלווה שונה מסיכון ברמת העסקה — יש לנתח את שניהם.</strong>
    נכס תקין לא מגן על לווה שקורס עסקית, וההיפך.
  </li>
  <li>
    <strong>EWS מחולק לשלוש קטגוריות: פיננסי, תפעולי, התנהגותי.</strong>
    סימנים התנהגותיים — איחור בדיווח, בקשת Waiver — לעיתים מקדימים את הפיננסיים.
  </li>
  <li>
    <strong>Watchlist מופעל כאשר DSCR יורד, LTV עולה, או מתרחש שינוי מהותי בלווה.</strong>
    כניסה ל-Watchlist מחייבת תוכנית מעקב ותדירות דיווח גבוהה יותר.
  </li>
  <li>
    <strong>תרחיש לווה: ירידת הכנסות + הצטברות חוב + חולשת ערב — כל אחד לבד מסוכן, השלושה יחד — קריטי.</strong>
    בדוק את הקבוצה הכוללת, לא רק את הנכס הממומן.
  </li>
  <li>
    <strong>ביקורת Covenant שנתית חייבת לכלול Red Flag Checklist — לא רק "עמד / לא עמד".</strong>
    מגמות חשובות לא פחות מנקודת הזמן.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אות אזהרה מוקדמת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Early Warning Signal</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אינדיקטור המאותת על הרעה לפני פיגור</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הלוואה במעקב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Watchlist</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיווג פנימי המחייב ניטור הדוק</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">LTV בעלייה הדרגתית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">LTV Creep</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עלייה הדרגתית ב-LTV עקב ירידת שווי / עלייה בחוב</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ויתור על תנאי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Covenant Waiver</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בקשת לווה לפטור זמני מעמידה ב-Covenant</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אחזקה דחויה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Deferred Maintenance</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">צמצום הוצאות אחזקה שוטפות — אות למצוקה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חולשת ערב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Guarantor Weakness</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שחיקה בחוסנו הפיננסי של הערב האישי</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — תרחישי מאקרו — מיתון ואינפלציה
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  תרחישי מאקרו — מיתון ואינפלציה
</h2>

<!-- ===== סעיף 1 — בניית תרחיש מאקרו ===== -->
<h3 style="color:#1a2638;">1. בניית תרחיש מאקרו — שלושת התרחישים הסטנדרטיים</h3>

<p>
  ניתוח תרחישי מאקרו בוחן כיצד סביבה כלכלית שלילית משפיעה על תיק ההלוואות
  כולו. בניגוד לניתוח ברמת עסקה — כאן כל העסקאות סובלות בו-זמנית.
  שלושת תרחישי הבסיס הסטנדרטיים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>מיתון (Recession Scenario):</strong> תמ&quot;ג שלילי, עלייה באבטלה,
    ירידת ביקוש לשטחי מסחר ומשרדים, עלייה בשיעורי פנוי.
  </li>
  <li>
    <strong>סטגפלציה (Stagflation Scenario):</strong> אינפלציה גבוהה
    בד-בבד עם צמיחה אפסית. עלויות תפעול עולות (OpEx), אך הכנסות
    לא עולות בהתאם כי שוכרים לא מסכימים לעדכון שכ&quot;ד. DSCR נשחק
    גם ללא ירידת תפוסה.
  </li>
  <li>
    <strong>נורמליזציית ריבית מהירה (Rapid Rate Normalization):</strong>
    בנק מרכזי מעלה ריבית בשיעורים גבוהים בטווח קצר. הלוואות בריבית
    משתנה מתייקרות מיידית; שווי נכסים יורד עקב התרחבות Cap Rate.
  </li>
</ul>

<!-- ===== סעיף 2 — סיכוני מאקרו ספציפיים לישראל ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. סיכוני מאקרו ספציפיים לכלכלה הישראלית</h3>

<p>
  מעבר לתרחישים הגלובליים, ישראל חשופה לסיכוני מאקרו ייחודיים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>זעזועים גיאופוליטיים (Geopolitical Shocks):</strong>
    מלחמה, סבב לחימה, או אי-ודאות ביטחונית — גורמים לירידה זמנית
    בביקוש לנדל&quot;ן, עצירת פרויקטים, ויציאת שוכרים זרים.
    ההשפעה בדרך כלל קצרת-טווח אך עלולה להיות קיצונית.
  </li>
  <li>
    <strong>פיחות השקל (Shekel Depreciation):</strong> חוזי שכ&quot;ד
    הצמודים לדולר מוגנים — אך ייקור עלויות ייבוא (חומרי בנייה, ציוד)
    פוגע בפרויקטים חדשים ובתחזוקת נכסים קיימים.
  </li>
  <li>
    <strong>אינפלציית עלויות בנייה (Construction Cost Inflation):</strong>
    עלייה חדה בעלות פלדה, בטון, ועבודה — מייקרת את עלות הפרויקטים
    החדשים ומשנה את ה-LTC הנדרש, ועלולה להפוך פרויקט "בר-ביצוע"
    לבלתי-כלכלי.
  </li>
</ul>

<!-- ===== סעיף 3 — תרגום תרחישי מאקרו לנכס ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. תרגום תרחישי מאקרו לקלטים ברמת הנכס</h3>

<p>
  המעבר ממאקרו לנכס בודד מחייב הנחות מפורשות:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מאקרו</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">השפעה על הנכס</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">כיול כמותי לדוגמה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">ירידת תמ&quot;ג -3%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שיעור פנוי עולה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תפוסה יורדת מ-90% ל-78%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">אינפלציה +5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">OpEx עולה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הוצאות תפעול עולות ב-7% (מינוף תפעולי)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">ריבית +200bps</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cap Rate מתרחב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cap Rate עולה מ-6% ל-7.5%; שווי יורד ~20%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">אבטלה +2%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ביקוש למשרדים יורד</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוכרים לא מחדשים, NOI ירד 10%–15%</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 4 — IFRS 9 ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. IFRS 9 — שכבת מאקרו על חישוב ECL</h3>

<p>
  תקן <strong>IFRS 9</strong> מחייב בנקים לחשב <strong>ECL — Expected Credit Loss</strong>
  על בסיס תרחישים מאקרו-כלכליים עתידיים — לא רק על ביצועי העבר.
  התקן דורש שלושה תרחישים משוקללים:
</p>

<ul style="line-height:1.9;">
  <li><strong>Base Case</strong> — התרחיש הסביר ביותר (משקל כ-50%–60%)</li>
  <li><strong>Upside</strong> — תרחיש חיובי (משקל כ-20%–25%)</li>
  <li><strong>Downside</strong> — תרחיש שלילי (משקל כ-20%–25%)</li>
</ul>

<p>
  ה-ECL המחושב הוא ממוצע משוקלל של שלושת התרחישים. בתקופות מיתון —
  משקל ה-Downside עולה, ה-ECL עולה, ורמת ההפרשה עולה. כך IFRS 9
  גורם להפרשות "מוקדמות" יותר לעומת שיטות ישנות שהמתינו לפיגור בפועל.
</p>

<!-- ===== סעיף 5 — קורלציה בתיק ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. קורלציה בתיק בזמן מאקרו-סטרס — הסכנה הנסתרת</h3>

<p>
  בתרחיש מאקרו, כל העסקאות בתיק סובלות <em>בו-זמנית</em>.
  הסנפיר המקביל (Portfolio Correlation) הופך לאחד הגורמים הקריטיים
  ביותר:
</p>

<ul style="line-height:1.9;">
  <li>
    תיק נדל&quot;ן מסחרי מרוכז בתל-אביב — בתרחיש של מיתון ישראלי,
    כל הנכסים מאבדים שוכרים במקביל. לא ניתן לפצות עם נכסים "חזקים".
  </li>
  <li>
    בנק שיחזיק נכסי תעשייה ומסחר יחד — בתרחיש אינפלציה, OpEx
    עולה לכולם בו-זמנית.
  </li>
  <li>
    גיוון גיאוגרפי ו-Product Mix הם ה"כרית" שמרחיקה מקורלציה מלאה.
  </li>
</ul>

<!-- ===== סעיף 6 — דוגמה עבודה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. דוגמה: תרחיש מיתון — חישוב השפעה על LTV תיק</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;font-size:13px;">
  הנחות תרחיש:<br>
  ירידת תמ&quot;ג: -3% | עלייה באבטלה: +2% | NOI ירד: -15% | Cap Rate: +100bps<br>
  <br>
  דוגמה לנכס A:<br>
  NOI Base Case: ₪2,000,000/שנה<br>
  NOI Stress:    ₪1,700,000/שנה (-15%)<br>
  <br>
  שווי Base Case (Cap 6.5%): ₪30,769,000<br>
  שווי Stress (Cap 7.5%):    ₪22,667,000 (-26.3%)<br>
  <br>
  הלוואה: ₪18,000,000<br>
  LTV Base: 18M / 30.8M = 58.5%<br>
  LTV Stress: 18M / 22.7M = 79.3% ← הפרת Covenant (סף 75%)
</div>

<p>
  הדוגמה מראה כיצד תרחיש מאקרו "מתון" של -15% NOI ו-+100bps Cap Rate
  יכול להוביל לקפיצת LTV של 21 נקודות — ולהכניס עסקה "בריאה" להפרת Covenant.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>עיקרון ניתוח מאקרו:</strong><br>
  מאקרו-סטרס אינו ניסיון לחזות את העתיד — הוא ניסיון לבדוק
  האם התיק שורד עתיד רע. השאלה אינה "האם זה יקרה?" — השאלה היא
  "אם זה יקרה, כמה הפסדים נספוג ומה הכלים שלנו להתמודד?"
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = "<p>ענה על שאלות ההבנה הבאות.</p>"

M5_EXERCISES_INSTRUCTIONS = "<p>פתור את התרגילים הבאים.</p>"

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — תרחישי מאקרו — מיתון ואינפלציה
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>שלושת תרחישי המאקרו הסטנדרטיים: מיתון, סטגפלציה, נורמליזציית ריבית.</strong>
    כל תרחיש פוגע בנכסים דרך מנגנון שונה — תפוסה, OpEx, או Cap Rate.
  </li>
  <li>
    <strong>ישראל חשופה לסיכוני מאקרו ייחודיים: גיאופוליטיקה, פיחות שקל, אינפלציית בנייה.</strong>
    יש לכלול לפחות תרחיש גיאופוליטי בניתוח כל תיק ישראלי.
  </li>
  <li>
    <strong>מאקרו מתורגם לנכס בודד דרך הנחות מפורשות: תפוסה, OpEx, Cap Rate.</strong>
    הנחות "מרחפות" ללא עיגון כמותי — פסולות בניתוח מקצועי.
  </li>
  <li>
    <strong>IFRS 9 מחייב ECL מבוסס תרחישים מאקרו — Downside, Base, Upside בממוצע משוקלל.</strong>
    בתקופת מיתון, ה-ECL עולה גם ללא פיגור בפועל — כי המשקל של Downside עולה.
  </li>
  <li>
    <strong>קורלציה גבוהה בתיק בזמן מאקרו-סטרס — הסכנה הנסתרת של ריכוז.</strong>
    גיוון גיאוגרפי ו-Product Mix הם ההגנה הטובה ביותר מפני קורלציה מלאה.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סטגפלציה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Stagflation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אינפלציה גבוהה + צמיחה אפסית בו-זמנית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הפסד אשראי צפוי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ECL — Expected Credit Loss</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הפסד אשראי מחושב לפי תרחישים (IFRS 9)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שכבת מאקרו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Macroeconomic Overlay</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">התאמת ECL בגין תחזית כלכלית עתידית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קורלציה בתיק</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Portfolio Correlation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מידת ההתנהגות המשותפת של נכסים בתיק</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נורמליזציית ריבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Rate Normalization</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עלייה מהירה של ריבית לרמת שיווי-משקל</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נקודת שבירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Break-Even Point</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הנקודה שבה הנכס כבר לא מכסה את שירות החוב</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — כתיבת ניתוח תרחישים בדוח אשראי
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  כתיבת ניתוח תרחישים בדוח אשראי
</h2>

<!-- ===== סעיף 1 — מבנה הסקציה ===== -->
<h3 style="color:#1a2638;">1. מבנה סקציית ניתוח תרחישים במזכר אשראי</h3>

<p>
  סקציית ניתוח התרחישים היא אחת הסקציות הקריטיות במזכר אשראי.
  היא מצויה בדרך כלל אחרי הניתוח הפיננסי הבסיסי (NOI, DSCR, LTV
  בתרחיש Base) ולפני המסקנה וההמלצה.
</p>

<p>
  <strong>מבנה סטנדרטי של הסקציה:</strong>
</p>

<ol style="line-height:1.9;">
  <li>כותרת ומטרה: "ניתוח תרחישים — בחינת עמידות העסקה בתנאים שליליים"</li>
  <li>הגדרת שלושת התרחישים בטבלה</li>
  <li>טבלת תוצאות (NOI / DSCR / LTV לפי תרחיש)</li>
  <li>פרשנות הממצאים — מה מתרחש בכל תרחיש, ומה נקודת השבירה</li>
  <li>מסקנה: האם העסקה עוברת את ה-Stress Test ובאיזה תנאים</li>
</ol>

<!-- ===== סעיף 2 — פורמט הטבלה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. פורמט טבלת תרחישים — Base / Bear / Stress</h3>

<p>
  הסטנדרט המקצועי הוא טבלה עם שורות = תרחישים, עמודות = מדדים:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תרחיש</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הנחות מרכזיות</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">NOI שנתי</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">DSCR</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">LTV</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">עמידה בתנאים?</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Base</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תפוסה 90%, OpEx +2%, Cap 6.5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">₪2,000,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">1.42×</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">58.5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:green;font-weight:bold;">כן</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Bear</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תפוסה 82%, OpEx +5%, Cap 7%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">₪1,650,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">1.17×</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">69.4%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:green;font-weight:bold;">כן (בקושי)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Stress</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תפוסה 72%, OpEx +8%, Cap 7.5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">₪1,300,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">0.92×</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">79.3%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:red;font-weight:bold;">הפרת LTV ו-DSCR</td>
    </tr>
  </tbody>
</table>

<p>
  הטבלה מאפשרת לוועדת האשראי לראות בבת-אחת: היכן נמצאת נקודת השבירה,
  ובאיזה תרחיש מופרים Covenants.
</p>

<!-- ===== סעיף 3 — סטנדרטי שפה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. סטנדרטי שפה לסקציית תרחישים</h3>

<p>
  ניתוח תרחישים במזכר אשראי חייב לעמוד בסטנדרטי שפה ברורים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>עובדתי וכמותי:</strong> "בתרחיש Stress, DSCR יורד ל-0.92x —
    מתחת לסף ה-Covenant של 1.10x" — לא "DSCR עשוי להיות נמוך".
  </li>
  <li>
    <strong>ללא גידורים (No Hedging):</strong> המנעות מניסוחים כמו
    "ייתכן ש-", "אין לדעת אם", "תלוי בנסיבות". ועדת האשראי מצפה
    לנתח ולא לגדר.
  </li>
  <li>
    <strong>ניקוד מספרי מלא:</strong> כל הנחה וכל תוצאה מלווה
    בנתון מספרי. ניסוחים כמו "NOI ירד משמעותית" — בלתי-מקצועיים.
  </li>
</ul>

<!-- ===== סעיף 4 — חולשות נפוצות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. חולשות נפוצות בסקציות תרחישים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">חולשה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תיאור</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תיקון</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הנחות מעגליות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תרחיש "Bear" שהוא Base-Case כמעט — רק ירידת 2% ב-NOI</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Bear צריך להיות ירידה משמעותית; Stress — קיצוני</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">העדר תרחיש קיצון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רק Base + Bear — ללא Stress</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תמיד שלושה תרחישים; Stress מחויב</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הנחות שחזור לא ריאליות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בתרחיש Stress, ה"מיטיגציה" מניחה שחזור מהיר שלא מוצדק</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שחזור חייב להיות מבוסס על נתוני שוק היסטוריים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">העדר נקודת שבירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הטבלה מראה תוצאות אך לא מזהה מתי מופרים Covenants</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פרט במפורש: "נקודת שבירה DSCR: תפוסה X%"</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 5 — ציפיות ועדת האשראי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. מה ועדת האשראי באמת מחפשת?</h3>

<p>
  ועדת האשראי לא רוצה לראות רק ש"Base Case עובד". היא מחפשת:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>נקודת השבירה:</strong> בדיוק באיזה רמת NOI / תפוסה /
    Cap Rate הנכס מפר Covenant. לא טווח — נקודה מדויקת.
  </li>
  <li>
    <strong>רגישות המודל:</strong> האם שינוי קטן (5% ב-NOI) שובר
    את העסקה, או שיש כרית? DSCR של 1.42x הרבה יותר בטוח מ-1.15x.
  </li>
  <li>
    <strong>מנגנוני מיטיגציה:</strong> בתרחיש Stress, מה הכלים
    שיש לבנק — הגדלת ביטחונות, הפחתת קרן, ערב אישי, מימוש?
  </li>
</ul>

<!-- ===== סעיף 6 — ניסוח מסקנה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. כיצד לנסח את המסקנה של סקציית התרחישים</h3>

<p>
  מסקנה מקצועית של סקציית תרחישים מבנויה כך:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;margin:12px 0;font-size:13px;line-height:2.0;">
  "בתרחיש Base, הנכס מניב DSCR של 1.42× ו-LTV של 58.5% — עמידה נוחה בכל Covenants.<br>
  בתרחיש Bear, DSCR מצטמצם ל-1.17× ו-LTV עולה ל-69.4% — עדיין בתחום המותר, אך עם שולי בטיחות מצומצמים.<br>
  בתרחיש Stress, העסקה מפרת את ה-DSCR Covenant (0.92× מול סף 1.10×) ואת ה-LTV Covenant (79.3× מול סף 75×).
  הפרה זו מטופלת ע&quot;י ערב אישי עם נכסים נזילים של ₪8M, ובהסכם לגיוס שוכר חלופי תוך 6 חודשים."
</div>

<p>
  שימו לב: המסקנה מציינת מה מתרחש בכל תרחיש, מאחזרת את ה-Covenant
  שמופר, ומפרטת את המיטיגציה — לא רק את הבעיה.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>טבלת התרחישים היא לב המזכר:</strong><br>
  הטבלה היא הדמות שמראה שחשבת על מה שיכול להשתבש.
  ועדת האשראי שמקבלת מזכר ללא טבלת תרחישים שואלת את עצמה:
  "האנליסט בדק רק את הצלחה — לא בדק את הכישלון."
  טבלת תרחישים מלאה ומדויקת היא ההוכחה שהניתוח מקיף.
</div>

<!-- ===== גשר לקורס 11 ===== -->
<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לקורס 11 — כתיבת מזכר אשראי (כתיבת מזכר אשראי):</strong><br>
  למדתם עד כה לנתח נכסים, לווים, מאקרו, ולכתוב ניתוח תרחישים.
  קורס 11 ייקח את כל הכלים האלה וישלב אותם למוצר שלם: כתיבת מזכר
  אשראי מקצועי מתחילתו ועד סופו — מהמבוא ועד ההמלצה לועדה.
  כל מה שלמדתם בקורסים 1–10 ישמש בסיס לכתיבה.
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = "<p>ענה על שאלות ההבנה הבאות.</p>"

M6_EXERCISES_INSTRUCTIONS = "<p>פתור את התרגילים הבאים.</p>"

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — כתיבת ניתוח תרחישים בדוח אשראי
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>סקציית תרחישים במזכר אשראי חייבת לכלול שלושה תרחישים: Base, Bear, Stress.</strong>
    מזכר עם Base Case בלבד לא עובר ועדת אשראי מקצועית.
  </li>
  <li>
    <strong>פורמט הטבלה הוא הסטנדרט: שורות = תרחישים, עמודות = NOI / DSCR / LTV / עמידה ב-Covenants.</strong>
    הטבלה חייבת להיות ברורה, עם נתונים מדויקים בכל תא.
  </li>
  <li>
    <strong>שפה עובדתית, כמותית, וללא גידורים — זה הסטנדרט.</strong>
    כל הנחה וכל תוצאה מלווה בנתון מספרי — לא בניסוחים "עשויים לרדת".
  </li>
  <li>
    <strong>החולשות הנפוצות: הנחות מעגליות, העדר Stress, שחזור לא ריאלי, היעדר נקודת שבירה.</strong>
    בדוק את כל ארבעת אלה לפני הגשת מזכר.
  </li>
  <li>
    <strong>ועדת האשראי מחפשת את נקודת השבירה — לא רק ש-Base Case עובד.</strong>
    מסקנה מקצועית מציינת מה מופר בתרחיש Stress, ומה מנגנוני המיטיגציה.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תרחיש בסיס</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Base Case</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תרחיש ההנחות הסבירות ביותר</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תרחיש שלילי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Bear Case</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תרחיש שלילי — סביר אך לא קיצוני</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תרחיש קיצון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Stress Case</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תרחיש קיצוני שבוחן את גבולות העסקה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נקודת שבירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Break Point / Break-Even</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הרמה שבה מופר Covenant לראשונה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הפחתת סיכון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Mitigation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מנגנון שמקטין את ההשפעה של הפרת Covenant</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גידור בשפה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Hedging Language</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניסוחים מעורפלים שנמנעים ממסקנה — פסולים במזכר</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לבחינה הסופית:</strong><br>
  השלמתם את שישת מודולי קורס 10 — ניתוח תרחישי סיכון. למדתם לבנות
  תרחישי לווה ומאקרו, לתרגם תרחישים לקלטים ברמת הנכס, ולכתוב
  ניתוח תרחישים מקצועי במזכר האשראי.<br><br>
  הבחינה הסופית תכלול בניית טבלת תרחישים מנתונים נתונים, זיהוי
  Early Warning Signals, חישוב LTV בתרחיש מאקרו, וניסוח מסקנת
  תרחישים לפי הסטנדרט המקצועי. הגיעו מוכנים — ובהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "תרחישי לווה — Early Warning Signals",
        "slug": "tarkhishe-loveh-early-warning",
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
        "title_he": "תרחישי מאקרו — מיתון ואינפלציה",
        "slug": "tarkhishe-makro-miton-veinflazia",
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
        "title_he": "כתיבת ניתוח תרחישים בדוח אשראי",
        "slug": "ktivat-nitur-tarkhishim-bdoah-ashrai",
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
    help = "Seed Course 10, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=10)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 10 not found. Run 'python manage.py seed_data' first."
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
