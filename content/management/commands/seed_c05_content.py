"""
Management command: seed_c05_content
Seeds Module 1-3 content for Course 5 (ניתוח תזרים מזומנים).

Usage:
    python manage.py seed_c05_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": "מבוא לדוח תזרים מזומנים",
        "slug": "mavo-doch-tizrim",
        "estimated_minutes": 45,
    },
    {
        "module_number": 2,
        "title_he": "תזרים מפעילות שוטפת",
        "slug": "tizrim-peulot-shotevet",
        "estimated_minutes": 50,
    },
    {
        "module_number": 3,
        "title_he": "תזרים מהשקעות ומימון",
        "slug": "tizrim-hashkaot-umimun",
        "estimated_minutes": 50,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (מבוא לדוח תזרים מזומנים)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>מבוא לדוח תזרים מזומנים</h2>

<p>
דוח תזרים המזומנים הוא אחד משלושת הדוחות הכספיים המרכזיים — לצד מאזן ודוח רווח והפסד —
אך הוא לרוב המוזנח ביותר בקרב מי שאינם אנליסטים פיננסיים מנוסים. בניתוח אשראי נדל"ן,
הדוח הזה הוא לפעמים <strong>הדוח החשוב ביותר מבין השלושה</strong>: הוא מספר את הסיפור של
הכסף האמיתי שנכנס ויוצא מהחברה — ולא של ה"רווח" שיכול להיות מכשיר חשבונאי.
</p>

<h2>למה תזרים משלים רווח והפסד</h2>

<p>
מערכת החשבונאות המקובלת (Accrual Accounting — חשבונאות צבירה) מכירה בהכנסות ובהוצאות
לפי <em>זמן הצמיחה הכלכלית</em> שלהן, לא לפי זמן תנועת המזומן. זה יוצר פער — לפעמים
ענק — בין הרווח המדווח לבין המזומן בקופה.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">פרמטר</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">חשבונאות צבירה (Accrual)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">בסיס מזומן (Cash)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מתי מכירה מוכרת?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בעת אספקת השירות/מוצר</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בעת קבלת התשלום</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מתי הוצאה מוכרת?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בעת צמיחת ההתחייבות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בעת התשלום בפועל</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מה מוצג ברווח?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווח כלכלי-חשבונאי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תזרים מזומנים נטו</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פחת</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הוצאה מוכרת</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לא מוכר (לא תזרים)</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חייבים גדלים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הכנסה מוכרת</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מזומן עוד לא התקבל</td>
    </tr>
  </tbody>
</table>

<p>
המשפט המפורסם ביותר בניתוח פיננסי: <strong>"Profit is opinion, cash is fact."</strong>
הרווח הוא תוצאה של בחירות חשבונאיות, הערכות שמאיות, ומדיניות פחת. המזומן — לעומת זאת —
הוא עובדה בלתי-ניתנת לפרשנות. כסף נמצא בחשבון, או שהוא לא נמצא.
</p>

<h2>שלושת החלקים של דוח תזרים המזומנים</h2>

<p>
דוח התזרים מחולק לשלושה חלקים, כל אחד מספר חלק שונה של הסיפור:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">חלק</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מה כולל</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">שאלה שעונה עליה</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">סימן טוב / רע</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;"><strong>פעילות שוטפת (OCF)</strong></td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גביות לקוחות, תשלומי ספקים, שכר, מסים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">האם הפעילות השוטפת מניצת מזומן?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חיובי = בריא; שלילי = אזהרה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;"><strong>פעילות השקעה (ICF)</strong></td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רכישת/מכירת נכסים, CAPEX, רכישות עסקיות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">האם החברה משקיעה לצמיחה?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שלילי בד"כ = השקעה בצמיחה</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;"><strong>פעילות מימון (FCF-fin)</strong></td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גיוס/פירעון חוב, דיבידנדים, הנפקות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כיצד ממומנת הפעילות?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תלוי בשלב הפיתוח</td>
    </tr>
  </tbody>
</table>

<p>
<strong>הקשר בין שלושת החלקים:</strong>
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
שינוי נטו במזומן = OCF + ICF + FCF-fin<br>
יתרת מזומן סוף תקופה = יתרת מזומן תחילת תקופה + שינוי נטו
</div>

<h2>שיטת ישיר לעומת שיטת עקיף לתזרים שוטף</h2>

<p>
לתזרים מפעילות שוטפת (OCF) קיימות שתי שיטות הצגה מקובלות — חשוב להבין את ההבדל
ביניהן, גם אם ברוב הדוחות בישראל תפגשו את השיטה העקיפה:
</p>

<h3>שיטת ישיר (Direct Method)</h3>
<p>
מציגה את תנועות המזומן עצמן — כמה גבתה החברה מלקוחות, כמה שילמה לספקים, כמה שילמה שכר.
ברורה ואינטואיטיבית, אך דורשת מערכת דיווח פנימית שעוקבת אחר כל תנועה ספציפית.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
OCF (ישיר) =<br>
  + גביות ממלקוחות<br>
  − תשלומים לספקים<br>
  − תשלומי שכר<br>
  − תשלומי מסים<br>
  ─────────────────<br>
  = תזרים מפעילות שוטפת
</div>

<h3>שיטת עקיף (Indirect Method)</h3>
<p>
מתחילה מהרווח הנקי ומתאימה אותו לתזרים מזומנים בפועל על ידי ניכוי פריטים שאינם מזומן
(כגון פחת) ותיאום שינויי הון חוזר. זוהי השיטה הנפוצה ביותר בפועל.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
OCF (עקיף) =<br>
  + רווח נקי<br>
  + פחת והפחתות (Non-Cash)<br>
  +/− שינויים בהון חוזר:<br>
      − עלייה בחייבים (כסף שלא גבינו)<br>
      + ירידה בחייבים (גבינו יותר ממה שהכרנו)<br>
      + עלייה בזכאים (דחינו תשלומים)<br>
      − ירידה בזכאים (שילמנו יותר ממה שהתחייבנו)<br>
      − עלייה במלאי (הכספנו כסף במלאי)<br>
  ─────────────────────────────────────<br>
  = תזרים מפעילות שוטפת (OCF)
</div>

<h2>גישור בין רווח נקי לתזרים שוטף</h2>

<p>
ההבדל בין הרווח הנקי ל-OCF הוא אחד הנושאים הכי חשובים בניתוח פיננסי. ישנם שלושה
מקורות עיקריים לפער:
</p>

<h3>1. פריטים שאינם מזומן (Non-Cash Items)</h3>
<p>
<strong>פחת והפחתות</strong> הן ההוצאות הגדולות ביותר שאינן מזומן. חברה שמחזיקה נכסים גדולים
(כמו נדל"ן, ציוד, או זכויות) תדווח על הוצאת פחת שמקטינה את הרווח הנקי — אך לא
מוציאה שקל מהקופה. לכן, OCF = רווח נקי + פחת (בשיטה עקיפה).
</p>

<h3>2. שינויי הון חוזר (Working Capital Changes)</h3>
<p>
גידול בחייבים (כסף שמגיע לנו מלקוחות ועוד לא שולם) מגדיל את הרווח אך לא את המזומן.
גידול בזכאים (כסף שאנחנו חייבים לספקים ועוד לא שולם) מגדיל את המזומן ביחס לרווח.
שינויים אלה הם ה<em>עיכוב</em> בין הרישום החשבונאי לבין תזרים המזומנים.
</p>

<h3>3. שערוכים ורווחי/הפסדי שווי הוגן</h3>
<p>
בחברות נדל"ן הנדרשות לדווח לפי IAS 40 (Investment Property), שינוי שווי הוגן מוכר
כהכנסה/הוצאה בדוח רווח והפסד — אך אינו תזרים מזומנים. חברת נדל"ן יכולה לדווח על
רווח ענק של שערוכים בשנה שבה ה-OCF שלילי לחלוטין.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — גישור רווח לתזרים:</strong><br><br>
  רווח נקי מדווח: 8,500,000 ₪<br>
  מזה: שערוך שווי הוגן נכסים: (6,000,000) ₪<br>
  פחת: 1,200,000 ₪<br>
  עלייה בחייבים: (2,800,000) ₪<br>
  עלייה בזכאים: 400,000 ₪<br>
  <strong>OCF = 8,500,000 − 6,000,000 + 1,200,000 − 2,800,000 + 400,000 = 1,300,000 ₪</strong><br><br>
  רווח נקי של 8.5M₪ — אך OCF של 1.3M₪ בלבד. מי שקרא רק דוח רווח והפסד פספס
  את התמונה האמיתית.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — "רווח" ללא מזומן בנדל"ן:</strong><br>
  יזם נדל"ן יכול להראות רווח נקי חיובי <em>שנים</em> לפני שנכנס שקל אחד למזומן —
  הודות לשערוכי שווי הוגן, הכרה בהכנסות לפי אחוז ביצוע, ומינוף גבוה שמסתיר
  גירעון תזרימי שוטף. <strong>תמיד בדוק את התזרים לפני שאתה מסיק מסקנות מהרווח.</strong>
  חברות נדל"ן שקרסו בישראל ובעולם עשו זאת לרוב עם דוחות רווח "יפים" — אך OCF שלילי.
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Comprehension HTML
# ---------------------------------------------------------------------------

M1_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על מבנה דוח תזרים המזומנים — בחן את הבנתך לגבי ההבדל בין חשבונאות
צבירה למזומן, שלושת חלקי הדוח, ושיטת ישיר לעומת שיטת עקיף.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Exercises HTML
# ---------------------------------------------------------------------------

M1_EXERCISES_HTML = """
<p>
5 תרגילי גישור בין רווח נקי ל-OCF — כולל תיאום פחת, שינויי הון חוזר, ושערוכי שווי
הוגן על מקרי מבחן ישראליים מתחום הנדל"ן.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — מבוא לדוח תזרים מזומנים</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>"Profit is opinion, cash is fact":</strong> הרווח הנקי מושפע מבחירות חשבונאיות
    ושערוכים. המזומן הוא עובדה. בניתוח אשראי — תמיד בחן את התזרים, לא רק את הרווח.
  </li>
  <li>
    <strong>שלושה חלקים:</strong> OCF (פעילות שוטפת) — בריאות תפעולית; ICF (השקעה) —
    אסטרטגיית צמיחה; FCF-fin (מימון) — מבנה ההון. יחד מסבירים את כל שינויי המזומן.
  </li>
  <li>
    <strong>שיטת ישיר vs עקיף:</strong> ישיר מציג תנועות מזומן ישירות; עקיף מתחיל מרווח
    נקי ומתאים. בישראל נפוצה בעיקר השיטה העקיפה — חיוני לדעת לקרוא אותה.
  </li>
  <li>
    <strong>מקורות הפער רווח-תזרים:</strong> פחת (Non-Cash), שינויי הון חוזר, שערוכי
    שווי הוגן (IAS 40). הגישור בין הרווח ל-OCF חושף את איכות הרווח.
  </li>
  <li>
    <strong>נדל"ן — אזהרה ספציפית:</strong> חברות נדל"ן נוטות לדווח רווחים גבוהים עם
    OCF שלילי, בשל שערוכים ומינוף. ניתוח אשראי שאינו בוחן את ה-OCF הוא ניתוח חסר.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
הכרנו את מבנה הדוח וההבדל בין רווח לתזרים. <em>מודול 2</em> יצלול לעומק
<strong>תזרים מפעילות שוטפת (OCF)</strong> — חישובו המלא, הקשר ל-EBITDA, ואיך
לזהות סימני אזהרה בנדל"ן.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (תזרים מפעילות שוטפת)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>תזרים מפעילות שוטפת (OCF)</h2>

<p>
תזרים מפעילות שוטפת — <strong>OCF (Operating Cash Flow)</strong> — הוא הבדיקה הראשונה
שאנליסט אשראי עורך על כל לווה: האם הפעילות השוטפת מייצרת מזומן? האם החברה יכולה
לשרת את חובותיה מהפעילות הרגילה שלה, ללא הסתמכות על מכירת נכסים או גיוס חוב חדש?
</p>

<h2>הגדרה ומה כולל OCF</h2>

<p>
OCF מייצג את כלל תנועות המזומן הנובעות <em>מפעילות הליבה</em> של העסק — כלומר
הפעילויות שמהן העסק אמור להרוויח לאורך זמן.
</p>

<h3>מה נכלל ב-OCF:</h3>
<ul>
  <li><strong>גביות ממלקוחות (Collections from Customers):</strong> מזומן שנכנס בפועל
  מלקוחות — לא ההכנסה המוכרת. אם גבינו פחות ממה שמכרנו, חייבים גדלו.</li>
  <li><strong>תשלומים לספקים (Payments to Suppliers):</strong> מזומן ששילמנו בפועל לספקים.
  אם שילמנו פחות ממה שצרכנו, זכאים גדלו.</li>
  <li><strong>תשלומי שכר לעובדים:</strong> כל תשלומי השכר, ההטבות ומענקים ששולמו בפועל.</li>
  <li><strong>מסי הכנסה ששולמו:</strong> מסים בפועל, לא הוצאת מס חשבונאית.</li>
  <li><strong>ריבית ששולמה (בחלק מהמקרים):</strong> לפי IFRS ניתן לסווג בפעילות שוטפת
  או מימון — יש לבחון בעקביות.</li>
</ul>

<h3>מה לא נכלל ב-OCF:</h3>
<ul>
  <li>רכישת ציוד ונכסים (CAPEX) — זה ICF.</li>
  <li>גיוסי חוב ופירעון הלוואות — זה FCF-fin.</li>
  <li>דיבידנדים ששולמו — לרוב FCF-fin.</li>
</ul>

<h2>שיטת עקיף — הנוסחה המלאה</h2>

<p>
ברוב הדוחות בישראל, OCF מוצג בשיטת עקיף. חשוב לדעת לפרק ולהבין כל שורה:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
OCF (שיטת עקיף) =<br><br>
  + רווח נקי (Net Income)<br>
  + פחת והפחתות (Depreciation &amp; Amortization)<br>
  + הפסדי שווי הוגן / − רווחי שווי הוגן<br>
  + הוצאות מניות (Share-Based Compensation, Non-Cash)<br>
  +/− שינויים בהון חוזר:<br>
      − עלייה בחייבים לקבל<br>
      + ירידה בחייבים לקבל<br>
      − עלייה במלאי<br>
      + ירידה במלאי<br>
      + עלייה בזכאים לשלם<br>
      − ירידה בזכאים לשלם<br>
      + עלייה בהכנסות מראש<br>
      − ירידה בהכנסות מראש<br>
  − מסי הכנסה ששולמו<br>
  − ריבית ששולמה (אם מסווגת בשוטפת)<br>
  ─────────────────────────────────────────────<br>
  = OCF
</div>

<h2>הון חוזר בנדל"ן — מה זה אומר?</h2>

<p>
בחברת נדל"ן, ה"הון החוזר" שונה מהותית מחברת תעשייה. האנליסט חייב להבין מה כל סעיף
מייצג בהקשר הנדל"ני:
</p>

<h3>מלאי קרקעות ופרויקטים (Inventory)</h3>
<p>
בחברת ייזום נדל"ן, "מלאי" הוא הקרקעות והפרויקטים בשלבי בנייה שונים. עלייה גדולה
במלאי פירושה שהחברה <em>הוציאה מזומן לרכישת קרקע ובנייה</em> — ללא גביית הכנסות עדיין.
זה מסביר מדוע OCF של יזמים הוא לרוב שלילי עמוקות בשנות הבנייה.
</p>

<h3>חייבים מלקוחות (Receivables)</h3>
<p>
בנדל"ן מניב — שכר דירה שמגיע אך טרם שולם. בנדל"ן ייזום — תשלומי רוכשים שהוכרו
כהכנסה לפי שלב ביצוע, אך הכסף עוד לא הגיע. עלייה חדה בחייבים = סיכון גבייה.
</p>

<h3>ספקים וזכאים (Payables)</h3>
<p>
כסף שחברת הנדל"ן חייבת לקבלנים, ספקים ונותני שירותים. עלייה בזכאים תורמת ל-OCF
(דחינו תשלומים) — אך אם נובעת מקשיים, זוהי אזהרה ולא יתרון.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — OCF חברת ייזום בשלב בנייה:</strong><br><br>
  רווח נקי: 12,000,000 ₪<br>
  פחת: 800,000 ₪<br>
  רווח שווי הוגן (Non-Cash): (15,000,000) ₪<br>
  עלייה במלאי קרקע ובנייה: (25,000,000) ₪<br>
  עלייה בחייבים רוכשים: (8,000,000) ₪<br>
  עלייה בזכאים קבלנים: 6,000,000 ₪<br>
  <strong>OCF = 12,000,000 + 800,000 − 15,000,000 − 25,000,000 − 8,000,000 + 6,000,000<br>
  = (29,200,000) ₪ — OCF שלילי של כ-29M₪!</strong><br><br>
  חברה רווחית לכאורה (12M₪ רווח) — אך שורפת מזומן בקצב של 29M₪ בשנה.
  כיצד ממומן הגירעון? זהו אחד השאלות המרכזיות באנליזת אשראי.
</div>

<h2>OCF vs EBITDA — ההבדלים ומתי כל אחד מתאים</h2>

<p>
שני המדדים נפוצים בניתוח פיננסי, אך מייצגים דברים שונים:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">פרמטר</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">EBITDA</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">OCF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בסיס חישוב</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רווח + ריבית + מסים + פחת</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תזרים מזומנים מפעילות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שינויי הון חוזר</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לא כולל</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כולל</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מסים ששולמו</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לא כולל</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כולל</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שערוכי IAS 40</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לרוב מנוטרל ידנית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מנוטרל מבנייתית</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מתי מתאים?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">השוואות בין-חברתיות, DSCR גס</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בחינת נזילות ותזרים אמיתי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חסרון עיקרי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אינו מייצג מזומן בפועל</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מושפע מעיתוי תזרים הון חוזר</td>
    </tr>
  </tbody>
</table>

<p>
<strong>הנחיה מעשית:</strong> EBITDA הוא כלי נוח להשוואות ראשוניות ולחישוב מהיר של
כושר שירות חוב גס. OCF הוא כלי המדויק יותר לבחינת הנזילות בפועל. <em>בניתוח אשראי
נדל"ן, השתמש בשניהם — וציין במפורש כשיש פער גדול ביניהם.</em>
</p>

<h2>אינדיקטורים אדומים ב-OCF</h2>

<p>
הדגלים האדומים הבאים, כשמופיעים יחד, מחייבים בדיקה מעמיקה:
</p>

<ul>
  <li><strong>OCF שלילי לאורך זמן + רווח חיובי:</strong> הרווח "נאכל" על ידי צמיחת
  הון חוזר, שערוכים, או הכנסות שלא גבו. זהו הסיכון המרכזי לניפוח רווחים (Earnings
  Manipulation Risk).</li>
  <li><strong>OCF יורד בעוד הכנסות עולות:</strong> שמירה על גדילה בהכנסות על חשבון
  חייבים גדלים — לקוחות לא משלמים, או החברה מקצרת תנאי תשלום כדי לגדול.</li>
  <li><strong>OCF נמוך מ-Net Income לאורך 3+ שנים:</strong> רמה גבוהה של הכנסות
  שאינן מזומן — חשד לאיכות רווח נמוכה.</li>
  <li><strong>שינויים חדים בזכאים ללא הסבר:</strong> עלייה חדה בזכאים ספקים עלולה
  לרמז על קשיי נזילות.</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — EBITDA גבוה ≠ מזומן:</strong><br>
  יזם שמציג EBITDA גבוה אך OCF שלילי הוא אחד הדפוסים המדאיגים ביותר בניתוח
  אשראי נדל"ן. <strong>חייבים לבדוק לאן הולך המזומן</strong> — האם לצמיחה מתוכננת
  ומבוקרת, או לכיסוי גירעון תפעולי שמוסתר מאחורי EBITDA חיובי? בדוק תמיד את
  הגישור בין EBITDA ל-OCF כחלק סטנדרטי מניתוח האשראי.
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Comprehension HTML
# ---------------------------------------------------------------------------

M2_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על OCF — בחן את יכולתך להבחין בין OCF ל-EBITDA, לפרש שינויי הון
חוזר בנדל"ן, ולזהות אינדיקטורים אדומים בדוחות תזרים.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Exercises HTML
# ---------------------------------------------------------------------------

M2_EXERCISES_HTML = """
<p>
6 תרגילי חישוב OCF בשיטת עקיף על חברות נדל"ן ישראליות — כולל ניטרול שערוכי IAS 40,
ניתוח שינויי הון חוזר ביזמות, והשוואת OCF ל-EBITDA לאותה חברה.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — תזרים מפעילות שוטפת</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>OCF = מזומן בפועל מפעילות הליבה:</strong> כולל גביות, תשלומי ספקים, שכר
    ומסים. אינו כולל CAPEX, גיוסי חוב, ודיבידנדים.
  </li>
  <li>
    <strong>שיטת עקיף — נוסחה מלאה:</strong> רווח נקי + פחת + הפסדי שווי הוגן +/−
    שינויי הון חוזר − מסים ששולמו. כל שורה בגישור חשובה ומעידה על משהו.
  </li>
  <li>
    <strong>הון חוזר בנדל"ן:</strong> מלאי קרקע = שריפת מזומן ביזמות; חייבים גדלים =
    סיכון גביה; זכאים גדלים = דחיית תשלומים (תורם ל-OCF — לא תמיד סימן חיובי).
  </li>
  <li>
    <strong>OCF vs EBITDA:</strong> EBITDA נוח להשוואות, OCF מדויק לנזילות בפועל.
    פער גדול ביניהם — חייבים להסביר. OCF שלילי עם EBITDA חיובי = דגל אדום.
  </li>
  <li>
    <strong>OCF שלילי + רווח חיובי לאורך זמן:</strong> הסיכון המרכזי לניפוח רווחים.
    בדוק את הגישור — אל תסתמך על הרווח הנקי בלבד לשיפוט כושר שירות חוב.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
ראינו שהפעילות השוטפת היא רק חלק אחד מהסיפור. <em>מודול 3</em> יציג את
<strong>תזרים ההשקעות ותזרים המימון</strong> — הכיצד הם משלימים את OCF לתמונה
מלאה, ואיך מחשבים Free Cash Flow ו-FCFE לניתוח מלא.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (תזרים מהשקעות ומימון)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>תזרים מהשקעות ומימון</h2>

<p>
לאחר שהבנו את OCF, נבחן את שני הסעיפים הנותרים בדוח תזרים המזומנים:
<strong>תזרים מפעילות השקעה (ICF)</strong> ו<strong>תזרים מפעילות מימון (FCF-fin)</strong>.
יחד עם OCF, הם מרכיבים את "מפל המזומנים" (Cash Waterfall) — הכלי המרכזי לניתוח
תמונת הנזילות של חברת נדל"ן.
</p>

<h2>תזרים מפעילות השקעה (ICF)</h2>

<p>
<strong>ICF (Investing Cash Flow)</strong> מייצג תנועות מזומן הקשורות לנכסים ארוכי-טווח:
רכישת נכסים, השקעות הוניות, ומכירות נכסים.
</p>

<h3>מה כולל ICF:</h3>
<ul>
  <li><strong>CAPEX — Capital Expenditure:</strong> רכישת מקרקעין, ציוד, שיפוצים גדולים,
  ופיתוח פרויקטים. אלו הם הוצאות ההון שמניחות את הבסיס לפעילות עתידית.</li>
  <li><strong>Acquisitions — רכישת עסקים:</strong> מזומן ששולם בעסקאות M&amp;A — רכישת
  חברות, תיקי נכסים, או שותפויות.</li>
  <li><strong>Disposals — מכירת נכסים:</strong> תמורות ממכירת נדל"ן, ציוד, או חלקי
  עסק. אלו הן תקבולים חד-פעמיים שיש לבחון בנפרד.</li>
  <li><strong>השקעות פיננסיות:</strong> רכישת/מכירת ניירות ערך, הלוואות לצדדים קשורים,
  פיקדונות ארוכי-טווח.</li>
</ul>

<h3>CAPEX בנדל"ן — שני סוגים</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
CAPEX תחזוקה (Maintenance CAPEX):<br>
השקעה הנדרשת לשמירת יכולת הייצור הנוכחית.<br>
לדוגמה: שיפוץ גג, החלפת מעלית, צביעה שוטפת.<br><br>
CAPEX צמיחה (Growth CAPEX):<br>
השקעה המרחיבה את הפעילות או הנכסים.<br>
לדוגמה: בנייה על קרקע חדשה, הוספת קומות, רכישת נכס חדש.
</div>

<p>
<strong>חשיבות ההבחנה:</strong> CAPEX תחזוקה הוא הוצאה "כמעט בלתי-נמנעת" — אם לא
מוציאים אותה, הנכס מתדרדר. CAPEX צמיחה הוא בחירה אסטרטגית. בחינת ה-FCF הנכונה
מנכה בעיקר את ה-CAPEX תחזוקה.
</p>

<h2>מינוס בתזרים השקעות — לא בהכרח רע</h2>

<p>
ICF שלילי הוא תמרור שכיח שמפחיד משקיעים חסרי ניסיון — אך בהקשר הנכון הוא מבשר
דווקא על בריאות:
</p>

<ul>
  <li><strong>ICF שלילי + OCF חיובי ויציב:</strong> החברה משקיעה מהתזרים השוטף שלה.
  כל שקל שנכנס מהפעילות משמש לצמיחה. זהו הדפוס הבריא ביותר.</li>
  <li><strong>ICF שלילי + OCF שלילי:</strong> הן השוטף והן ההשקעות שורפות מזומן. הכל
  ממומן מחוב חדש. זה בסדר בשלב ייזום — אך מצריך הסבר ברור.</li>
  <li><strong>ICF חיובי:</strong> החברה מוכרת נכסים. לפעמים זה אסטרטגי (מחזור תיק),
  לפעמים זה פעולת הצלה (מוכרת כדי לשרת חוב). חשוב לדעת מה הסיבה.</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — קריאת ICF:</strong><br><br>
  חברת נדל"ן מדווחת:<br>
  OCF: +18,000,000 ₪<br>
  ICF: (45,000,000) ₪<br>
  מתוכם: רכישת קרקע חדשה: (30,000,000) ₪, CAPEX תחזוקה: (5,000,000) ₪,
  השקעות בפרויקט בנייה: (10,000,000) ₪<br><br>
  <strong>פירוש:</strong> החברה בצמיחה אגרסיבית — משקיעה פי 2.5 מה-OCF שלה בנכסים חדשים.
  הגירעון (27M₪) ממומן מחוב. שאלת האנליסט: האם החוב בר-קיימא? מה ה-LTV לאחר הרכישות?
</div>

<h2>תזרים מפעילות מימון (FCF-fin)</h2>

<p>
<strong>תזרים מימון</strong> מייצג את כל תנועות המזומן בין החברה לבין ספקי ההון שלה —
בנקים, משקיעים, בעלי מניות:
</p>

<ul>
  <li><strong>גיוסי חוב חדש:</strong> הלוואות חדשות שנלקחו, אגרות חוב שהונפקו.</li>
  <li><strong>פירעון חוב:</strong> החזרי קרן על הלוואות קיימות.</li>
  <li><strong>תשלומי ריבית</strong> (אם מסווגת בפעילות מימון לפי IFRS).</li>
  <li><strong>דיבידנדים ששולמו לבעלי המניות.</strong></li>
  <li><strong>הנפקות הון חדש (IPO, הנפקות זכויות):</strong> גיוס כסף ממשקיעים חדשים.</li>
  <li><strong>רכישה עצמית של מניות (Buybacks).</strong></li>
</ul>

<h2>Free Cash Flow (FCF) ו-FCFE</h2>

<p>
שני מדדי תזרים מרכזיים לניתוח מתקדם שמבוססים על OCF:
</p>

<h3>Free Cash Flow (FCF)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
FCF = OCF − CAPEX
</div>

<p>
FCF הוא התזרים שנותר לאחר ש"שמרנו" על הנכסים הקיימים ו/או השקענו בצמיחה. הוא
מייצג את המזומן ה<em>חופשי</em> — הזמין לשירות חוב, דיבידנדים, השקעות נוספות, או
בניית יתרות.
</p>

<p>
<strong>FCF חיובי</strong> = החברה מייצרת מזומן מעבר לצרכי ה-CAPEX שלה — בסיס בריא לשירות חוב.<br>
<strong>FCF שלילי</strong> = החברה "שורפת" מזומן על CAPEX מעבר ל-OCF. ניתן לפרוד בין צמיחה לבעיה.
</p>

<h3>FCFE — Free Cash Flow to Equity</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
FCFE = FCF + גיוסי חוב נטו<br>
     = OCF − CAPEX + (הלוואות חדשות − פירעון הלוואות)
</div>

<p>
FCFE מייצג את התזרים שנותר <em>לבעלי המניות</em> לאחר שהחברה כבר עמדה בהתחייבויות
החוב. אם FCFE שלילי — בעלי המניות אינם מקבלים ערך מזומן מהחברה; אם חיובי — יש
תזרים לחלוקה כדיבידנד או לצמיחה נוספת.
</p>

<h2>ניתוח Combined: Cash Waterfall לנדל"ן</h2>

<p>
ה-"Cash Waterfall" הוא הכלי הכי שימושי לאנליסט אשראי נדל"ן — הוא מרכז את כל
תזרימי המזומנים לתמונה אחת:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
OCF (תזרים שוטף)<br>
  + ICF (תזרים השקעות, בד"כ שלילי בצמיחה)<br>
  ─────────────────────────────────────────<br>
  = FCF (Free Cash Flow)<br>
  + FCF-fin (גיוסי חוב נטו / פירעונות נטו)<br>
  ─────────────────────────────────────────<br>
  = שינוי נטו במזומן<br>
  + יתרת מזומן פתיחה<br>
  ─────────────────────────────────────────<br>
  = יתרת מזומן סגירה
</div>

<p>
<strong>שאלות שה-Cash Waterfall עונה עליהן:</strong>
</p>
<ul>
  <li>האם הפעילות השוטפת עומדת ברשות עצמה?</li>
  <li>כמה מימון חיצוני נדרש לתמיכה בצמיחה?</li>
  <li>האם יתרת המזומן גדלה, יציבה, או נשחקת?</li>
  <li>האם הדיבידנדים ממומנים מ-OCF חיובי או מגיוסי חוב?</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — Cash Waterfall שנתי:</strong><br><br>
  OCF: +22,000,000 ₪<br>
  ICF: (18,000,000) ₪<br>
  <strong>FCF: +4,000,000 ₪</strong><br><br>
  FCF-fin:<br>
  גיוסי הלוואות: +30,000,000 ₪<br>
  פירעון הלוואות: (15,000,000) ₪<br>
  דיבידנדים: (8,000,000) ₪<br>
  <strong>FCF-fin נטו: +7,000,000 ₪</strong><br><br>
  <strong>שינוי נטו במזומן: +4,000,000 + 7,000,000 = +11,000,000 ₪</strong><br><br>
  פירוש: יתרת מזומן גדלה ב-11M₪ — אך 8M₪ מתשלום הדיבידנד מומן מחוב חדש, לא מ-FCF.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — דיבידנדים ממומנים מחוב:</strong><br>
  חברה שמממנת תשלומי דיבידנד מגיוסי חוב — כלומר, שולמת לבעלי המניות כסף שלווה
  מהבנק — היא <strong>דגל אדום קריטי לקיימות</strong>. זה אומר שה-FCF אינו מספיק
  לכסות הן את ה-CAPEX והן את הדיבידנד. בשלב מסוים, כאשר המלווים יגבילו גיוסים
  נוספים, הדיבידנד ייפסק — ולעיתים קרובות, זה הסימן הראשון לתחילת משבר.
  <strong>בדוק תמיד: מהיכן מומנו הדיבידנדים? מ-FCF חיובי — תקין. מחוב חדש — בעיה.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 3 — Comprehension HTML
# ---------------------------------------------------------------------------

M3_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על ICF, FCF ו-Cash Waterfall — בחן את יכולתך לפרש תזרים השקעות,
לחשב FCF ו-FCFE, ולזהות דפוסי מימון לא-בר-קיימא.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Exercises HTML
# ---------------------------------------------------------------------------

M3_EXERCISES_HTML = """
<p>
6 תרגילי ניתוח Cash Waterfall מלא על חברות נדל"ן ישראליות — כולל חישוב FCF ו-FCFE,
ניתוח מקורות מימון דיבידנד, וזיהוי דפוסי ICF אסטרטגי לעומת ICF מאולץ.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — תזרים מהשקעות ומימון</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>ICF = תזרים ההשקעות:</strong> כולל CAPEX, רכישות ומכירות נכסים. ICF שלילי
    בחברה צומחת הוא נורמלי — המפתח הוא להבין אם הוא ממומן מ-OCF חיובי או מחוב.
  </li>
  <li>
    <strong>CAPEX תחזוקה vs צמיחה:</strong> הבחנה קריטית לחישוב FCF מדויק. CAPEX
    תחזוקה הוא "כמעט הכרחי" — יש לנכותו תמיד מה-OCF בחישוב FCF מנורמל.
  </li>
  <li>
    <strong>FCF = OCF − CAPEX:</strong> התזרים ה"חופשי" לאחר ההשקעות ההוניות.
    FCFE = FCF + גיוסי חוב נטו — מה שנותר לבעלי המניות.
  </li>
  <li>
    <strong>Cash Waterfall לנדל"ן:</strong> OCF + ICF = FCF; FCF + FCF-fin = שינוי
    במזומן. הכלי המרכזי לאנליסט — מחבר את כל שלושת חלקי הדוח לתמונה שלמה.
  </li>
  <li>
    <strong>דיבידנדים ממומנים מחוב = דגל אדום:</strong> בדוק תמיד את מקור הדיבידנד.
    אם FCF-fin הוא חיובי (גיוסים עודפים) אך FCF שלילי — הדיבידנד מכספי הלוואות.
    זהו הסיכון הקיימותי החמור ביותר בניתוח אשראי.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
שלושת המודולים הראשונים של קורס 5 בנו את מיומנות קריאת דוח תזרים המזומנים — מהמבנה
הבסיסי, דרך OCF, ועד ל-Cash Waterfall המלא. <em>המודולים הבאים</em> ייישמו את הכלים האלה
ב<strong>ניתוח עסקאות נדל"ן ספציפיות</strong> — ייזום, נדל"ן מניב, ומיחזורי חוב.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 5 "
        "(ניתוח תזרים מזומנים)"
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 5 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=5)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=5 not found. "
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
            self.style.SUCCESS("\nAll done — Course 5 modules 1-3 seeded successfully.")
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
