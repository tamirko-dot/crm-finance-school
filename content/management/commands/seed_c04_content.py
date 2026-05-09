"""
Management command: seed_c04_content
Seeds Module 1-3 content for Course 4 (מדדים פיננסיים בנדל"ן).

Usage:
    python manage.py seed_c04_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": 'LTV ו-LTC — יחסי מינוף',
        "slug": "ltv-ltc-yahase-minuf",
        "estimated_minutes": 50,
    },
    {
        "module_number": 2,
        "title_he": "DSCR ו-ICR — כיסוי שירות חוב",
        "slug": "dscr-icr-kisuy-sherut-hov",
        "estimated_minutes": 55,
    },
    {
        "module_number": 3,
        "title_he": "NOI ו-Cap Rate",
        "slug": "noi-cap-rate",
        "estimated_minutes": 55,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (LTV ו-LTC)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>LTV ו-LTC — יחסי מינוף בנדל"ן</h2>

<p>
שני המדדים הנפוצים ביותר בהערכת מינוף בנדל"ן הם <strong>LTV (Loan-to-Value)</strong>
ו-<strong>LTC (Loan-to-Cost)</strong>. כל אנליסט אשראי חייב לדעת לחשב, לפרש ולהשוות אותם —
ולהבין מתי כל אחד מהם רלוונטי יותר.
</p>

<h2>הגדרת LTV — מדוע הוא המדד הראשון שבוחנים</h2>

<p>
<strong>LTV (Loan-to-Value Ratio)</strong> הוא היחס בין גובה ההלוואה לשווי הנכס המשמש
בטוחה לה. זהו המדד הבסיסי ביותר לבחינת כרית הביטחון של המלווה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
LTV = הלוואה ÷ שווי הנכס × 100%
</div>

<p>
הרציונל: אם הלווה אינו מחזיר את החוב, המלווה מממש את הנכס. ככל שה-LTV נמוך יותר,
כך גדולה ה<em>כרית</em> בין שווי הנכס לגובה החוב — וגדל הסיכוי שהמלווה יגבה את כל חובו
גם אם שווי הנכס ירד. ב-LTV של 70%, שווי הנכס יכול לרדת ב-30% לפני שהמלווה מתחיל
להפסיד קרן.
</p>

<p>
<strong>מתי נבחן LTV?</strong> בכל הלוואה כנגד נכס קיים: משכנתאות לדיור, הלוואות לנדל"ן
מניב, מימון רכישת קרקע, ומחזורי חוב. LTV הוא הנקודה הראשונה שמחלקות האשראי בוחנות
לפני כל אישור.
</p>

<h3>חישוב LTV — דוגמאות מספריות</h3>

<p>
הבנת ה-LTV מתחדדת עם דוגמאות קונקרטיות. נבחן מספר תרחישים:
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה 1 — נכס מניב בתל-אביב:</strong><br><br>
  שווי נכס (הערכת שמאי): 10,000,000 ₪<br>
  גובה הלוואה מבוקש: 7,000,000 ₪<br>
  <strong>LTV = 7,000,000 ÷ 10,000,000 = 70%</strong><br><br>
  פירוש: המלווה חשוף ל-70% משווי הנכס. כרית הביטחון: 30% = 3,000,000 ₪.
  שווי הנכס יכול לרדת ב-30% לפני שהמלווה מתחיל להפסיד.

  <br><br>
  <strong>דוגמה 2 — נכס עם LTV גבוה:</strong><br><br>
  שווי נכס: 5,000,000 ₪ | הלוואה: 4,250,000 ₪<br>
  <strong>LTV = 85%</strong> — כרית של 15% בלבד. ירידת שווי של 15% מוחקת את כל ההגנה.

  <br><br>
  <strong>דוגמה 3 — LTV נמוך:</strong><br><br>
  שווי נכס: 20,000,000 ₪ | הלוואה: 10,000,000 ₪<br>
  <strong>LTV = 50%</strong> — כרית של 50%. מינוף שמרני, הגנה גבוהה.
</div>

<h2>LTC — מדד השלמה לייזום</h2>

<p>
<strong>LTC (Loan-to-Cost Ratio)</strong> משמש בעיקר בפרויקטי ייזום — כשעדיין אין נכס גמור
לשמאות. במקרים אלה, שווי הנכס העתידי אינו ודאי, ולכן LTV פחות רלוונטי. LTC מודד את
ההלוואה כאחוז מ<em>עלות הפרויקט הכוללת</em>.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
LTC = הלוואה ÷ עלות הפרויקט הכוללת × 100%<br><br>
עלות הפרויקט = עלות קרקע + עלות בנייה + הוצאות פיתוח + עלויות מימון + שיווק
</div>

<p>
<strong>ההבדל המהותי מ-LTV:</strong> LTV מבוסס על שווי שוק (קדימה — אם יושלם נכון), בעוד
LTC מבוסס על עלויות ידועות (עסקה). LTC ניתן לחשב גם בשלב הראשוני של הפרויקט, לפני
שקיים נכס לשמאות.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — פרויקט ייזום:</strong><br><br>
  עלות קרקע: 8,000,000 ₪<br>
  עלות בנייה: 12,000,000 ₪<br>
  הוצאות פיתוח, רישוי ושיווק: 2,000,000 ₪<br>
  <strong>עלות פרויקט כוללת: 22,000,000 ₪</strong><br><br>
  הלוואת ייזום: 15,400,000 ₪<br>
  <strong>LTC = 15,400,000 ÷ 22,000,000 = 70%</strong><br><br>
  היזם מממן 30% מהפרויקט מהון עצמי (6,600,000 ₪).
</div>

<p>
<strong>מתי LTC עדיף על LTV?</strong> בשלב ייזום, השמאים מעריכים שווי עתידי (GDV — Gross
Development Value) שמכיל אי-ודאות גבוהה. LTC, לעומת זאת, מבוסס על תקציב בנייה
שנבדק ומאושר — ולכן מדויק יותר לשלב זה.
</p>

<h2>מגבלות ורגולציה בישראל</h2>

<p>
בנק ישראל מתווה מגבלות LTV לסוגי הלוואות שונות. המגבלות עודכנו מספר פעמים בשנים האחרונות
ומהוות כלי מרכזי של מדיניות מאקרו-פרודנציאלית:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">סוג הלווה / הנכס</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מגבלת LTV מרבית</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הערה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">דירה ראשונה למגורים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">75%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הוראת בנק ישראל</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">דירה שנייה ומעלה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">50%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מגבלה מחמירה למשקיעים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נדל"ן מסחרי / מניב</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">60%–70%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לפי מדיניות כל בנק</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הלוואות ייזום (LTC)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">65%–75%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">משתנה לפי בנק ורמת הפרויקט</td>
    </tr>
  </tbody>
</table>

<p>
בפועל, הבנקים הישראליים פועלים לרוב עם LTV של 60%–75% לנדל"ן מסחרי — מתחת למגבלות
הרשמיות — בהתאם לדירוג הלווה, איכות הנכס, ומצב השוק.
</p>

<h2>Dynamic LTV — שינוי לאורך חיי ההלוואה</h2>

<p>
LTV אינו קבוע לאורך חיי ההלוואה. הוא משתנה בשני כיוונים:
</p>

<h3>אמורטיזציה — הורדת ה-LTV עם הזמן</h3>
<p>
כאשר הלווה פורע קרן בכל תשלום (Amortizing Loan), יתרת ההלוואה יורדת בהדרגה. אם שווי
הנכס נותר יציב — ה-LTV יורד. לדוגמה: הלוואה של 7M₪ על נכס של 10M₪ (LTV=70%) לאחר
3 שנות פירעון קרן של 500K₪ לשנה: יתרת הלוואה = 5.5M₪, LTV = 55%.
</p>

<h3>שינויי שווי — השפעה על LTV</h3>
<p>
שינוי בשווי הנכס (עלייה או ירידה) משנה את ה-LTV גם ללא שינוי בגובה ההלוואה:
</p>
<ul>
  <li><strong>שווי עלה:</strong> LTV יורד — כרית הביטחון גדלה (חיובי למלווה).</li>
  <li><strong>שווי ירד:</strong> LTV עולה — כרית הביטחון נשחקת (סיכון למלווה).</li>
  <li><strong>ירידת שווי חדה:</strong> LTV עשוי לחצות את רף הברירת מחדל (Default Trigger) המוגדר
  בחוזה ההלוואה — ומחייב השלמת ביטחונות.</li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
LTV דינמי = יתרת הלוואה עדכנית ÷ שווי שוק עדכני × 100%
</div>

<p>
בהסכמי הלוואה מתקדמים, מוגדר <strong>LTV Covenant</strong>: רמת LTV שחציתה מהווה הפרת
אמות מידה פיננסיות ומאפשרת למלווה לדרוש פירעון מוקדם. לרוב מוגדר ב-80%–85%.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — LTV נמוך ≠ הלוואה בטוחה:</strong><br>
  LTV של 50% נשמע מצוין — אך אם הנכס אינו מייצר תזרים מספיק לשרת את החוב, הבנק עלול
  להיות תקוע עם נכס שקשה למכור, בשוק דל-נזילות, בלחץ זמן. גם בנכס עם LTV של 50%,
  אם אין תזרים לשרת את החוב — זו בעיה. <strong>LTV הוא מדד שיקום (Recovery Metric),
  לא מדד שירות חוב (Debt Service Metric).</strong> שניהם נחוצים.
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Comprehension HTML
# ---------------------------------------------------------------------------

M1_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על LTV ו-LTC — בחן את הבנתך לפני שממשיכים.
השאלות בוחנות את ההבחנה בין המדדים, חישובים מספריים, ויישום בשוק הישראלי.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Exercises HTML
# ---------------------------------------------------------------------------

M1_EXERCISES_HTML = """
<p>
6 תרגילי חישוב LTV ו-LTC על מקרי מבחן מהשוק הישראלי.
התרגילים כוללים חישוב LTV ראשוני, Dynamic LTV לאחר שינויי שווי, ומעבר בין LTC ל-LTV
עם השלמת פרויקט ייזום.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — LTV ו-LTC</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>LTV = הלוואה ÷ שווי נכס:</strong> מודד את כרית הביטחון של המלווה.
    LTV של 70% = שווי הנכס יכול לרדת ב-30% לפני שהמלווה מתחיל להפסיד קרן.
    המדד הבסיסי בכל הערכת אשראי נדל"ן.
  </li>
  <li>
    <strong>LTC = הלוואה ÷ עלות פרויקט:</strong> משמש בייזום כשאין נכס גמור לשמאות.
    מבוסס על תקציב בנייה ידוע ולא על שווי עתידי — מדויק יותר בשלב הבנייה.
  </li>
  <li>
    <strong>מגבלות בנק ישראל:</strong> דירה ראשונה — עד 75% LTV; דירה שנייה — עד 50%;
    נדל"ן מסחרי — 60%–70% לפי מדיניות הבנק. מגבלות אלה הן כלי מדיניות מאקרו-פרודנציאלי.
  </li>
  <li>
    <strong>Dynamic LTV:</strong> LTV משתנה לאורך חיי ההלוואה — יורד עם פירעון קרן,
    עולה כששווי הנכס יורד. LTV Covenant בחוזה ההלוואה מגדיר את רמת הסיכון המרבית.
  </li>
  <li>
    <strong>LTV נמוך ≠ הלוואה בטוחה:</strong> LTV הוא מדד שיקום בלבד. גם ב-LTV של 50%,
    אם אין תזרים לשרת את החוב — זוהי בעיה. יש לבחון LTV יחד עם DSCR — לא במקומו.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
ראינו ש-LTV לבדו אינו מספיק — נחוץ גם מדד שמעריך את יכולת תזרים המזומנים לשרת את החוב.
<em>מודול 2</em> יציג את <strong>DSCR ו-ICR</strong> — שני המדדים המרכזיים לבחינת שירות החוב.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (DSCR ו-ICR)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>DSCR ו-ICR — כיסוי שירות חוב</h2>

<p>
בעוד LTV מודד את כרית הביטחון הנכסית, <strong>DSCR</strong> ו-<strong>ICR</strong> מודדים
משהו שונה לחלוטין: האם הנכס מייצר מספיק תזרים מזומנים כדי לשרת את ההלוואה שוטפת?
אלו הם מדדי שירות החוב — והם לא פחות חשובים מה-LTV.
</p>

<h2>DSCR — ההגדרה</h2>

<p>
<strong>DSCR (Debt Service Coverage Ratio)</strong> הוא היחס בין ה-NOI (הכנסה תפעולית נטו)
לבין שירות החוב השנתי הכולל — קרן וריבית יחד.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
DSCR = NOI ÷ שירות חוב שנתי<br><br>
שירות חוב שנתי = תשלומי קרן שנתיים + תשלומי ריבית שנתיים
</div>

<p>
<strong>פירוש המדד:</strong>
</p>
<ul>
  <li>DSCR = 1.0: ה-NOI בדיוק מכסה את שירות החוב — אין מרווח ביטחון.</li>
  <li>DSCR = 1.25: ה-NOI גבוה ב-25% משירות החוב — מרווח ביטחון בריא.</li>
  <li>DSCR = 0.90: ה-NOI מכסה רק 90% משירות החוב — גירעון תזרימי שוטף.</li>
</ul>

<h2>מה כולל NOI לצורך DSCR?</h2>

<p>
ה-NOI ל-DSCR חייב להיות מחושב נכון — שגיאות בהגדרת ה-NOI מובילות ל-DSCR מוטעה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
NOI = הכנסות שכירות ברוטו<br>
     − אחוז פנויות נורמלי (Vacancy Allowance)<br>
     − הוצאות תפעוליות ישירות (ניהול, תחזוקה, ביטוח, ארנונה)<br>
     ────────────────────────────────────────<br>
     = NOI
</div>

<p>
<strong>מה לא נכלל ב-NOI:</strong>
</p>
<ul>
  <li><strong>שירות חוב</strong> (ריבית + קרן) — אלה הסעיף שכנגדו מחשבים את ה-DSCR.</li>
  <li><strong>פחת</strong> — הוצאה חשבונאית שאינה תזרים מזומנים.</li>
  <li><strong>מסי הכנסה</strong> — DSCR הוא מדד לפני מס.</li>
  <li><strong>CapEx (הוצאות הון)</strong> — השקעות הוניות. לעיתים מנוכות בחישוב DSCR מתקדם.</li>
  <li><strong>הכנסות חד-פעמיות</strong> — פרמיות יציאה, פיצויי ביטוח, מכירת נכסים.</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה מחושבת — בניין משרדים בגוש דן:</strong><br><br>
  הכנסות שכירות ברוטו שנתיות: 2,400,000 ₪<br>
  אחוז פנויות נורמלי (5%): (120,000) ₪<br>
  הוצאות ניהול ותחזוקה: (360,000) ₪<br>
  ביטוח וארנונה: (120,000) ₪<br>
  <strong>NOI: 1,800,000 ₪</strong><br><br>
  תשלומי ריבית שנתיים: 900,000 ₪<br>
  תשלומי קרן שנתיים: 500,000 ₪<br>
  <strong>שירות חוב שנתי: 1,400,000 ₪</strong><br><br>
  <strong>DSCR = 1,800,000 ÷ 1,400,000 = 1.29</strong><br>
  — מרווח ביטחון סביר; הנכס מייצר 29% יותר מהנדרש לשירות החוב.
</div>

<h2>ICR — ריבית בלבד</h2>

<p>
<strong>ICR (Interest Coverage Ratio)</strong> הוא גרסה פחות שמרנית מ-DSCR — הוא מודד את
יכולת ה-NOI לכסות את הוצאות הריבית <em>בלבד</em>, ללא תשלומי הקרן.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ICR = NOI ÷ הוצאות ריבית שנתיות
</div>

<p>
<strong>מתי ICR רלוונטי?</strong> בהלוואות Bullet (ריבית בלבד עם פירעון קרן בסוף מועד), ה-ICR
הוא המדד הנכון לבחינת השירות השוטף — שכן אין תשלומי קרן שוטפים. שכיח בהלוואות לנדל"ן
מסחרי ומניב.
</p>

<p>
<strong>ההבדל בין ICR ל-DSCR:</strong> ICR תמיד גבוה יותר מ-DSCR (כשיש תשלומי קרן), כי הוא
מתעלם מהם. ICR של 2.0 יחד עם DSCR של 1.2 שניהם על אותו NOI — ייתכן בהחלט, ומחייב
חישוב נפרד לכל אחד.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>המשך הדוגמה — ICR לאותו נכס:</strong><br><br>
  NOI: 1,800,000 ₪<br>
  הוצאות ריבית שנתיות: 900,000 ₪<br>
  <strong>ICR = 1,800,000 ÷ 900,000 = 2.00</strong><br><br>
  DSCR היה 1.29 — ICR גבוה משמעותית כי הוא אינו כולל תשלומי קרן (500,000 ₪).
  שני המדדים נדרשים לתמונה מלאה.
</div>

<h2>DSCR מנורמל לעומת DSCR מדווח</h2>

<p>
ה-DSCR "מדווח" — כזה שמחושב ישירות מהדוחות הכספיים — עלול להיות מעוות על ידי פריטים
חד-פעמיים ושינויים בשווי הוגן. האנליסט חייב <strong>לנרמל</strong> את ה-NOI לפני החישוב.
</p>

<h3>פריטים שיש לנטרל בנורמליזציה:</h3>
<ul>
  <li><strong>שערוכי נדל"ן (IAS 40):</strong> עלייה/ירידה בשווי הוגן נכסים — אינה תזרים.</li>
  <li><strong>פיצויי פינוי חד-פעמיים:</strong> תקבול שאינו חוזר.</li>
  <li><strong>הכנסות מכירת נכסים:</strong> מכירת נכס שאינו בליבת הפעילות.</li>
  <li><strong>הוצאות שיפוץ חריגות:</strong> CapEx שרשום כהוצאה תפעולית.</li>
  <li><strong>הכנסות מדמי ניהול חד-פעמיים</strong> שאינם חלק מהמודל העסקי הקבוע.</li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
NOI מנורמל = NOI מדווח<br>
           − הכנסות חד-פעמיות<br>
           + הוצאות חד-פעמיות (שנוטרלו בדיווח)<br>
           − שערוכים חיוביים<br>
           + שערוכים שליליים<br>
           ────────────────────────────────────────<br>
           = NOI מנורמל לחישוב DSCR
</div>

<h2>ספי DSCR בשוק הישראלי</h2>

<p>
הבנקים הישראליים עובדים עם ספי DSCR מינימליים. אלה אינם אחידים — משתנים לפי סוג הנכס,
משך ההלוואה, ודירוג הלווה:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">סוג נכס / עסקה</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">DSCR מינימלי מקובל</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הערה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נדל"ן מניב (Office, Retail)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">≥ 1.20–1.25</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מרווח של 20%–25% מעל שירות החוב</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לוגיסטיקה ותעשייה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">≥ 1.20</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חוזים ארוכים מפצים על אי-נזילות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פרויקט ייזום (בשלב הכנסות)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">≥ 1.30</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון גבוה יותר — מרווח גדול נדרש</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מגורים להשכרה (Build-to-Rent)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">≥ 1.15–1.20</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ביקוש יציב בישראל מאפשר שוליים נמוכים</td>
    </tr>
  </tbody>
</table>

<p>
<strong>שימוש אנליטי:</strong> כאשר ה-DSCR של עסקה מסוימת קרוב לסף המינימום, יש לבדוק את
<em>הרגישות</em>: כמה צריך ה-NOI לרדת (עלייה בפנויות, ירידת שכירויות) כדי לחצות את ה-1.0?
רגישות של 10% = הנכס יכול לאבד 10% מה-NOI לפני כניסה לגירעון. רגישות זו חשובה לא פחות
מהמדד עצמו.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — DSCR מתחת ל-1.0:</strong><br>
  DSCR נמוך מ-1.0 פירושו שה-NOI אינו מספיק לשרת את החוב. הנכס מפסיד תזרים שוטף —
  הלווה נדרש להזרים הון עצמי בכל תקופה כדי לעמוד בתשלומים. זוהי הגדרת אי-כדאיות
  תזרימית, ולרוב — הגדרת ברירת מחדל פוטנציאלית לפי תנאי ההלוואה.
  <strong>DSCR מתחת ל-1.0 = הנכס אינו עומד ברשות עצמו.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Comprehension HTML
# ---------------------------------------------------------------------------

M2_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על DSCR ו-ICR — בחן את יכולתך להבחין בין המדדים, לחשב NOI מנורמל,
ולפרש DSCR ביחס לספי השוק הישראלי.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Exercises HTML
# ---------------------------------------------------------------------------

M2_EXERCISES_HTML = """
<p>
6 תרגילי חישוב DSCR ו-ICR על נכסי נדל"ן מניב ישראליים. התרגילים כוללים חישוב NOI מנורמל,
בדיקת רגישות DSCR לשינויי שכירות ופנויות, והשוואת DSCR מדווח למנורמל בנוכחות שערוכי IAS 40.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — DSCR ו-ICR</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>DSCR = NOI ÷ שירות חוב שנתי (קרן + ריבית):</strong> המדד הבסיסי לשירות חוב.
    DSCR ≥ 1.0 = הנכס מממן את עצמו. מתחת ל-1.0 = הנכס בגירעון תזרימי.
  </li>
  <li>
    <strong>NOI מחושב נכון:</strong> שכירות ברוטו פחות פנויות פחות הוצאות תפעוליות.
    לא כולל: פחת, ריבית, מסים, הכנסות חד-פעמיות. שגיאה בחישוב NOI = שגיאה ב-DSCR.
  </li>
  <li>
    <strong>ICR = NOI ÷ ריבית בלבד:</strong> פחות שמרני מ-DSCR; רלוונטי בהלוואות Bullet
    שבהן אין תשלומי קרן שוטפים. ICR תמיד גבוה מ-DSCR כשיש תשלומי קרן.
  </li>
  <li>
    <strong>DSCR מנורמל:</strong> יש לנטרל שערוכי IAS 40, פריטים חד-פעמיים, ומכירות נכסים
    לפני החישוב. DSCR מדווח ללא נורמליזציה עלול להטעות.
  </li>
  <li>
    <strong>ספי שוק ישראל:</strong> נדל"ן מניב — DSCR ≥ 1.20–1.25; ייזום — ≥ 1.30.
    בחן תמיד גם את הרגישות: כמה יכול ה-NOI לרדת לפני שחוצים את ה-1.0.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
DSCR הסתמך כבר על מושג ה-NOI — מבלי שהגדרנו אותו לעומק. <em>מודול 3</em> יפרט את
<strong>NOI ו-Cap Rate</strong>: כיצד מחשבים NOI נכון, וכיצד הוא הופך לשווי נכס באמצעות ה-Cap Rate.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (NOI ו-Cap Rate)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>NOI ו-Cap Rate — הערכת שווי נכסים מניבים</h2>

<p>
שני מושגים אלה הם עמוד השדרה של כל הערכת שווי נדל"ן מניב: <strong>NOI (Net Operating Income)</strong>
מייצג את הכנסת הנכס הנקייה, ו-<strong>Cap Rate (Capitalization Rate)</strong> הוא הכלי
שהופך את ה-NOI לשווי שוק. כל אנליסט אשראי בנדל"ן חייב לשלוט בחישובם ובפרשנותם.
</p>

<h2>NOI — מה כולל ומה לא?</h2>

<p>
<strong>NOI (Net Operating Income)</strong> הוא ההכנסה התפעולית הנקייה מהנכס — לפני מימון,
מסים ופחת. הוא מייצג את היכולת התפעולית הנקייה של הנכס לייצר הכנסה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
NOI = הכנסות שכירות ברוטו (Gross Rental Income)<br>
    − אחוז פנויות (Vacancy &amp; Credit Loss)<br>
    − הוצאות תפעוליות (Operating Expenses)<br>
    ──────────────────────────────────────────<br>
    = NOI (הכנסה תפעולית נקייה)
</div>

<h3>מה כולל — פירוט:</h3>
<ul>
  <li><strong>הכנסות שכירות ברוטו:</strong> כל הכנסות השכירות מהנכס לפי שיעור תפוסה מלאה.</li>
  <li><strong>אחוז פנויות:</strong> ניכוי נורמטיבי לפנויות ואי-גבייה (לרוב 3%–8% לפי סוג שוק).</li>
  <li><strong>הוצאות תפעוליות:</strong> ניהול נכס, תחזוקה שוטפת, ביטוח, ארנונה מחוסרת שוכר,
  שירותי ניקיון ואבטחה.</li>
</ul>

<h3>מה לא כולל — פירוט:</h3>
<ul>
  <li><strong>פחת (Depreciation):</strong> הוצאה חשבונאית — אינה תזרים מזומנים.</li>
  <li><strong>ריבית ותשלומי קרן (Debt Service):</strong> מימון הוא ספציפי ללווה, לא לנכס.</li>
  <li><strong>מסי הכנסה (Income Tax):</strong> NOI הוא מדד לפני מס — מאפשר השוואה בין-לווה.</li>
  <li><strong>CapEx (הוצאות הון):</strong> שיפוצים גדולים, החלפת ציוד — אלה אינן הוצאות תפעוליות.</li>
  <li><strong>שערוכים (Revaluations):</strong> שינויי שווי הוגן לפי IAS 40 — לא תזרים.</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — חישוב NOI לנכס לוגיסטי:</strong><br><br>
  הכנסות שכירות ברוטו (שנתי): 3,600,000 ₪<br>
  אחוז פנויות נורמלי (4%): (144,000) ₪<br>
  הוצאות ניהול ואחזקה: (252,000) ₪<br>
  ביטוח, ארנונה, שמירה: (144,000) ₪<br>
  <strong>NOI: 3,060,000 ₪</strong><br><br>
  שים לב: לא נוכה פחת (720,000 ₪), ריבית (1,200,000 ₪) ומסים — NOI הוא לפני כל אלה.
</div>

<h2>Cap Rate — כלי הערכת השווי</h2>

<p>
<strong>Cap Rate (שיעור היוון)</strong> הוא שיעור התשואה הנורמטיבי לסוג נכס מסוים בשוק נתון.
הוא מקשר בין ה-NOI לשווי השוק בנוסחה פשוטה ועוצמתית:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Cap Rate = NOI ÷ שווי שוק<br>
שווי שוק = NOI ÷ Cap Rate
</div>

<p>
הנוסחה השנייה היא המפתח לשמאות: נתון ה-NOI, וידוע שה-Cap Rate בשוק לנכס דומה הוא X%,
אפשר לגזור את שווי הנכס. זה הבסיס ל<em>Income Approach</em> בהערכת שווי נדל"ן.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — הערכת שווי לפי Cap Rate:</strong><br><br>
  NOI שנתי: 3,060,000 ₪<br>
  Cap Rate שוק ללוגיסטיקה בגוש דן: 7.5%<br>
  <strong>שווי נכס = 3,060,000 ÷ 0.075 = 40,800,000 ₪</strong><br><br>
  אם ה-Cap Rate עולה ל-8.0%: שווי = 3,060,000 ÷ 0.08 = 38,250,000 ₪ — ירידה של 2,550,000 ₪!
</div>

<h2>Yield-on-Cost — תשואה על עלות בייזום</h2>

<p>
<strong>Yield-on-Cost (YoC)</strong> הוא מדד ייחודי לפרויקטי ייזום — הוא מחשב את התשואה
על כלל עלות הפרויקט, ולא על שווי שוק קיים.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Yield-on-Cost = NOI צפוי ÷ עלות פרויקט כוללת × 100%
</div>

<p>
<strong>מדוע חשוב?</strong> היזם לוקח סיכון בנייה. ה-Yield-on-Cost חייב להיות גבוה מה-Cap Rate
בשוק — אחרת, למה לבנות? ההפרש נקרא <strong>Development Spread</strong>:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Development Spread = Yield-on-Cost − Cap Rate שוק
</div>

<p>
Development Spread חיובי = הפרויקט מצדיק את הסיכון. ספי מקובלים: 0.75%–1.5% מעל Cap Rate
שוק, לפי רמת הסיכון ומשך הבנייה.
</p>

<h2>Going-in Cap Rate לעומת Exit Cap Rate</h2>

<p>
בניתוח השקעה, מבחינים בין שני Cap Rates:
</p>

<h3>Going-in Cap Rate</h3>
<p>
ה-Cap Rate <strong>ביום הרכישה</strong> — NOI הנוכחי חלקי מחיר הרכישה. מייצג את התשואה
הנוכחית שמקבל הרוכש ביום ה-Day 1.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Going-in Cap Rate = NOI שנה 1 ÷ מחיר רכישה
</div>

<h3>Exit Cap Rate</h3>
<p>
ה-Cap Rate <strong>הצפוי ביום המכירה</strong> בסוף תקופת ההחזקה. משמש לחישוב שווי היציאה
(Exit Value) במודל DCF.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Exit Value = NOI שנה אחרי היציאה ÷ Exit Cap Rate
</div>

<p>
<strong>הנחת Exit Cap Rate:</strong> לרוב Exit Cap Rate מוגדר גבוה יותר מה-Going-in Cap Rate
ב-0.25%–0.50% — להתחשב בגיל הנכס, סיכון שוק, ואי-ודאות. הנחת Exit Cap Rate שמרנית =
פחות סיכון במודל.
</p>

<h2>Cap Rates בישראל לפי סקטור</h2>

<p>
Cap Rates אינם אחידים — הם משקפים את רמת הסיכון ורמת הנזילות לכל סוג נכס. ספים
עדכניים לשוק הישראלי (2024):
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">סוג נכס</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">Cap Rate טיפוסי</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הסבר</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">משרדים — גוש דן, א' (Prime)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">6.0%–7.0%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ביקוש גבוה, נזילות גבוהה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מסחר (Retail) — קניונים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">7.0%–8.0%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון גבוה יותר מ-E-Commerce</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לוגיסטיקה ותעשייה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">7.0%–8.0%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ביקוש גובר, נזילות בינונית</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מגורים להשכרה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3.0%–4.5%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שכירות נמוכה יחסית לשווי בישראל</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מלונאות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">7.5%–9.0%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תנודתיות גבוהה, ניהול אינטנסיבי</td>
    </tr>
  </tbody>
</table>

<p>
<strong>Cap Rate ומחזורי ריבית:</strong> Cap Rates נוטים לעלות כאשר ריבית הבנקים המרכזיים
עולה — כי המשקיעים דורשים פרמיה גבוהה יותר על השקעה לא-נזילה. בישראל, העלאות ריבית בנק
ישראל ב-2022–2023 הובילו לעלייה של 0.5%–1.0% ב-Cap Rates במרבית הסקטורים.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — Cap Rate עולה = שווי יורד:</strong><br>
  הקשר בין Cap Rate לשווי הוא <em>הפוך</em>. עלייה של 0.5% ב-Cap Rate על NOI של 2,000,000 ₪:<br><br>
  שווי בCap Rate 7.0%: 2,000,000 ÷ 0.07 = <strong>28,571,429 ₪</strong><br>
  שווי בCap Rate 7.5%: 2,000,000 ÷ 0.075 = <strong>26,666,667 ₪</strong><br>
  <strong>ירידת שווי: 1,904,762 ₪ — כמעט 2M₪ על כל שינוי של 0.5% ב-Cap Rate!</strong><br><br>
  זוהי הסיבה שאנליסטים תמיד בוחנים את רגישות ה-LTV לשינויי Cap Rate — עלייה קטנה
  בשיעור ההיוון מחקה חלק ניכר מהכרית.
</div>
"""


# ---------------------------------------------------------------------------
# Module 3 — Comprehension HTML
# ---------------------------------------------------------------------------

M3_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על NOI ו-Cap Rate — בחן את יכולתך לחשב NOI נכון, לגזור שווי נכס מ-Cap Rate,
ולפרש את הקשר בין שינויי ריבית לשינויי שווי.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Exercises HTML
# ---------------------------------------------------------------------------

M3_EXERCISES_HTML = """
<p>
6 תרגילי חישוב NOI ו-Cap Rate על נכסים מסחריים ולוגיסטיים ישראליים. התרגילים כוללים
חישוב NOI מפירוט הוצאות, הערכת שווי לפי Cap Rate שוק, ניתוח Development Spread לפרויקט ייזום,
וניתוח רגישות שווי לשינויי Cap Rate.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — NOI ו-Cap Rate</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>NOI = שכירות ברוטו − פנויות − הוצאות תפעוליות:</strong> לא כולל פחת, ריבית,
    מסים ו-CapEx. NOI הוא מדד תפעולי טהור של הנכס — ללא השפעת מבנה המימון.
  </li>
  <li>
    <strong>Cap Rate = NOI ÷ שווי שוק:</strong> ושווי שוק = NOI ÷ Cap Rate. זוהי נוסחת
    ה-Income Approach לשמאות. Cap Rate נמוך = שווי גבוה; Cap Rate גבוה = שווי נמוך.
  </li>
  <li>
    <strong>Yield-on-Cost לייזום:</strong> NOI צפוי ÷ עלות פרויקט. חייב להיות גבוה מה-Cap Rate
    בשוק (Development Spread חיובי) — אחרת אין הצדקה כלכלית לסיכון הבנייה.
  </li>
  <li>
    <strong>Going-in vs Exit Cap Rate:</strong> Going-in = תשואה ביום הרכישה; Exit = Cap Rate
    הצפוי ביום המכירה. Exit Cap Rate לרוב גבוה יותר ב-0.25%–0.5% — לשמרנות ולגיל הנכס.
  </li>
  <li>
    <strong>Cap Rates ישראל 2024:</strong> משרדים Prime ~6%–7%; מסחר ולוגיסטיקה ~7%–8%;
    מגורים ~3%–4.5%. Cap Rates עולים עם ריבית — עלייה של 0.5% מורידה שווי נכס ב-~7%.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
שלושת המודולים הראשונים בנו את בסיס המדדים: LTV/LTC למינוף, DSCR/ICR לשירות חוב,
NOI/Cap Rate לשווי. <em>מודול 4</em> יישם את כולם יחד ב<strong>ניתוח עסקת נדל"ן מניב מלאה</strong> —
מבחינת אשראי לצורך קבלת החלטת מימון.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 4 "
        '(מדדים פיננסיים בנדל"ן)'
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 4 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=4)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=4 not found. "
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
            self.style.SUCCESS("\nAll done — Course 4 modules 1-3 seeded successfully.")
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
