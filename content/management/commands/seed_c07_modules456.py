"""
Seeds Module 4-6 content for Course 7 (ניהול סיכונים בנדל"ן).
Usage: python manage.py seed_c07_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — סיכוני בנייה, ייזום והשלמה
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכוני בנייה, ייזום והשלמה
</h2>

<!-- ===== סעיף 1 — נכס לפני השלמה לעומת נכס מייצב ===== -->
<h3 style="color:#1a2638;">1. סיכון טרום-השלמה לעומת נכס מייצב</h3>

<p>
  בפרויקט בנייה קיים פער מהותי בין שני סוגי סיכון: <strong>סיכון טרום-השלמה
  (Pre-Completion Risk)</strong> — הסיכון שהפרויקט לא יושלם כתוכנית — לבין
  הסיכון הקיים בנכס מייצב (Stabilized Asset Risk) — כלומר נכס גמור ומושכר
  שמניב תזרים שוטף.
</p>

<p>
  הסיכון הגדול ביותר בנדל&quot;ן הוא בשלב הבנייה: עוד אין הכנסות, העלויות
  כבר זורמות, והמלווה לא יכול לממש בטחונות אפקטיבית על בניין שלא נגמר.
  ברגע שהנכס מייצב — יש שוכרים, תזרים ו-NOI — הסיכון יורד משמעותית
  ויכול להיות ממומן מחדש בריבית נמוכה יותר (Refinancing).
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מדוע חשוב ההבחנה?</strong><br>
  הלוואת ייזום (Construction Loan) מסוכנת יותר מהלוואה לנכס מייצב —
  ולכן נושאת ריבית גבוהה יותר, LTC נמוך יותר, ומנגנוני פיקוח הדוקים יותר.
  אנליסט שמייחס שיעור ריבית של נכס מייצב לפרויקט בנייה — טועה בהנחת יסוד.
</div>

<!-- ===== סעיף 2 — חריגות עלות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. חריגות עלות — קריאת תקציב בנייה</h3>

<p>
  <strong>Cost Overrun</strong> — חריגה מתקציב הבנייה — הוא אחד הגורמים השכיחים
  ביותר לכשל בפרויקטי נדל&quot;ן. כדי לזהות חשיפה לחריגות, על האנליסט לקרוא
  את תקציב הבנייה ולהבחין בין שני סוגי עלות:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג עלות</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דגל אדום</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עלויות קשות (Hard Costs)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חומרי גלם, עבודה, קבלן ראשי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רזרבה מתחת ל-5% מסך העלויות הקשות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עלויות רכות (Soft Costs)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אדריכל, עו&quot;ד, אגרות, שיווק, מימון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Soft Costs מנופחים עלולים להסתיר הוצאות קבוצה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עתודה לאי-ודאות (Contingency)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רזרבה תקציבית לאי-צפוי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Contingency נמוך מ-5%–10% — פרויקט פגיע לחריגות</td>
    </tr>
  </tbody>
</table>

<p>
  בנוסף, בדוק את <strong>חשיפת ה-Soft Costs</strong>: מה אחוז הייעוץ, הניהול
  והשיווק מסך הפרויקט? Soft Costs גבוהים חריגים עלולים להסתיר העברות
  בין-חברתיות לא שקופות.
</p>

<!-- ===== סעיף 3 — עיכוב בלוח זמנים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. עיכוב בלוח זמנים — ריבית עתודה ועלויות נשיאה</h3>

<p>
  כל עיכוב בבנייה פוגע ישירות בכדאיות הפרויקט דרך שני מנגנונים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>שחיקת ריבית עתודה (Interest Reserve):</strong> תקציב הפרויקט
    כולל עתודה מוגדרת לתשלום ריבית בתקופת הבנייה. עיכוב של 6 חודשים
    מעל הצפוי עלול לאמץ את העתודה במלואה — ולגרום ללווה לצורך בהון
    נוסף שלא תוכנן.
  </li>
  <li>
    <strong>עלויות נשיאה (Carry Costs):</strong> ארנונה, ביטוח, אחזקת
    אתר, עלויות מימון — ממשיכות לרוץ גם כשהבנייה מושהית. עיכוב
    גורר עליית עלות כוללת של הפרויקט.
  </li>
</ul>

<p>
  <strong>כלל אצבע:</strong> לכל חודש עיכוב מעבר לצפי — צפה לתוספת עלות
  של 1%–2% מהתקציב הכולל, בהתאם לגודל הפרויקט ורמת הריבית.
</p>

<!-- ===== סעיף 4 — ערבות השלמה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. מנגנוני ערבות השלמה</h3>

<p>
  <strong>ערבות השלמה (Completion Guarantee)</strong> היא מנגנון שמבטיח
  שהפרויקט יושלם גם אם הלווה נקלע לקשיים. סוגי ערבות השלמה עיקריים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>ערבות אישית של בעל השליטה:</strong> בעל המניות מתחייב
    אישית להשלים את הפרויקט או לפרוע את ההלוואה. מגן על המלווה אך
    תלוי בכושר הפירעון האישי של הבעלים.
  </li>
  <li>
    <strong>ערבות קבלן (Contractor Performance Bond):</strong> הקבלן
    הראשי מספק ערבות ביצוע לכך שישלים את העבודה. אם הקבלן ניגש —
    חברת הביטוח או מלווה אחר מסיים את הבנייה.
  </li>
  <li>
    <strong>הזרמת הון (Equity Injection Commitment):</strong> הלווה
    מתחייב להזרים הון נוסף עד לסכום מוגדר אם העלויות חורגות. מגן
    את המלווה מדיבורים על "נגמר לי הכסף".
  </li>
</ul>

<!-- ===== סעיף 5 — LTC לעומת LTV ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. LTC לעומת LTV — מתי משתמשים בכל אחד</h3>

<p>
  שני יחסים מרכזיים בהלוואות ייזום:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>LTC — Loan-to-Cost:</strong> יחס בין סכום ההלוואה לעלות
    הכוללת של הפרויקט. מדד רלוונטי בשלב הבנייה — כשאין עוד שווי
    שוק ברור לנכס גמור. LTC מקובל: 65%–75%.
  </li>
  <li>
    <strong>LTV — Loan-to-Value:</strong> יחס בין ההלוואה לשווי שוק
    של הנכס. רלוונטי לנכסים מייצבים — שבהם יש הערכת שמאי על בסיס
    הכנסות. LTV מקובל: 60%–70% בנכסים מסחריים.
  </li>
</ul>

<p>
  בפרויקט בנייה המלווה בודק את <em>שניהם</em>: LTC מוודא שהמלווה
  לא מממן את כל הפרויקט (הלווה חייב להביא הון עצמי); LTV "as-completed"
  מוודא שגם לאחר השלמה ה-LTV יהיה סביר.
</p>

<!-- ===== סעיף 6 — לוח משיכות ואבני דרך ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. לוח משיכות ואבני דרך</h3>

<p>
  בהלוואת ייזום, המלווה אינו מעביר את כל הסכום ביום הראשון.
  ה-Drawdowns מתבצעים לפי <strong>לוח משיכות (Draw Schedule)</strong>
  המשויך לאבני דרך ניהוליות ו/או לאישור מפקח בנייה:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;">
  משיכה 1: פינוי קרקע + יסודות → 15% מסכום ההלוואה<br>
  משיכה 2: שלד + גג → 25%<br>
  משיכה 3: גמר חיצוני + מערכות → 30%<br>
  משיכה 4: גמר פנימי + עמידה בתקן → 20%<br>
  משיכה 5: תעודת גמר + רישיון → 10%
</div>

<p>
  לפני כל משיכה: מפקח בנייה מטעם המלווה מאשר שהעבודה בוצעה.
  עיכוב ב-Milestone = עיכוב במשיכה = לחץ נזילות על הלווה.
</p>

<!-- ===== מקרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>מקרה: יזם שנגמר לו ההון עצמי באמצע הבנייה</strong><br>
  יזם קיבל הלוואת ייזום ב-LTC של 70%. מתחילת הבנייה נחלש
  שוק הנדל&quot;ן, עלויות הפלדה עלו ב-18%, והקבלן ביקש תוספת.
  הלווה משך 85% מהמסגרת — אך הפרויקט הושלם רק ב-60%.
  ה-30% הון עצמי הסתיים, וסכום ההלוואה שנותר לא הספיק לסיום.
  <strong>תוצאה:</strong> הפרויקט קפא — הבנק נאלץ להגדיל מסגרת שלא תוכננה
  או לנהל מכירה מאולצת של פרויקט חצי גמור בשווי נמוך משמעותית.
  <strong>לקח:</strong> Contingency נמוך + LTC גבוה + ללא ערבות השלמה = מתכון לכשל.
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של סיכון טרום-השלמה, חריגות עלות, עיכוב בלוח זמנים, "
    "מנגנוני ערבות השלמה, ההבדל בין LTC ל-LTV, ולוח משיכות. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים קריאת תקציב בנייה נתון וזיהוי חשיפות עלות, "
    "חישוב ריבית עתודה נדרשת בתרחיש עיכוב, זיהוי הבדלים בין LTC ל-LTV 'as-completed', "
    "והערכת התאמה בין ערבויות השלמה לגודל הסיכון. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — סיכוני בנייה, ייזום והשלמה
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>סיכון טרום-השלמה גבוה בהרבה מסיכון נכס מייצב.</strong>
    הלוואת ייזום דורשת ריבית גבוהה יותר, LTC נמוך יותר ומנגנוני פיקוח הדוקים יותר.
  </li>
  <li>
    <strong>תקציב בנייה חייב לכלול Contingency של לפחות 5%–10%.</strong>
    Soft Costs מנופחים וחשיפת עלויות קשות ללא עתודה הם דגלים אדומים מובהקים.
  </li>
  <li>
    <strong>כל חודש עיכוב שוחק ריבית עתודה ומוסיף עלויות נשיאה.</strong>
    בדוק שעתודת הריבית מספיקה לתרחיש של עיכוב ב-6 חודשים לפחות.
  </li>
  <li>
    <strong>LTC מודד מימון מול עלות; LTV מודד מימון מול שווי.</strong>
    בפרויקטי ייזום — בדוק את שניהם: LTC בשלב הבנייה, LTV "as-completed" לאחר ההשלמה.
  </li>
  <li>
    <strong>ערבות השלמה — אישית, קבלן, או הזרמת הון — מגנה על המלווה מקפיאה.</strong>
    ללא ערבות השלמה, פרויקט שנתקע הופך לבעיה של המלווה.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סיכון טרום-השלמה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Pre-Completion Risk</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכון שהפרויקט לא יושלם כתוכנית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חריגת עלות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cost Overrun</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חריגה מתקציב הבנייה המאושר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עתודה לאי-ודאות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Contingency</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רזרבה תקציבית לעלויות בלתי-צפויות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ריבית עתודה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Interest Reserve</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תקציב ייעודי לתשלום ריבית בתקופת הבנייה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">יחס הלוואה לעלות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">LTC — Loan-to-Cost</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואה חלקי עלות כוללת של הפרויקט</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ערבות השלמה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Completion Guarantee</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">התחייבות להשלים פרויקט גם בקשיים</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — סיכוני רגולציה, משפט וסביבה
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכוני רגולציה, משפט וסביבה
</h2>

<!-- ===== סעיף 1 — סיכון תכנון ורישוי ===== -->
<h3 style="color:#1a2638;">1. סיכון תכנוני — שינויי תב&quot;ע</h3>

<p>
  <strong>תב&quot;ע — תוכנית בניין עיר</strong> — קובעת את ייעוד הקרקע, זכויות
  הבנייה, גובה המבנה ומקסימום השטח המותר לבנייה. שינוי בתב&quot;ע עלול
  לשנות דרמטית את ערך הנכס:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>שדרוג תב&quot;ע (Upzoning):</strong> אישור זכויות בנייה נוספות
    — מגדיל את ערך הקרקע ויכול לשפר את ה-LTV. לרוב חיובי למלווה.
  </li>
  <li>
    <strong>הפחתת זכויות:</strong> צמצום שטחים מותרים לבנייה — פוגע
    ישירות בשווי הקרקע ובהיתכנות הכלכלית של הפרויקט.
  </li>
  <li>
    <strong>שינוי ייעוד:</strong> מייצוב למגורים, מסחרי לשימור — עלול
    להפוך פרויקט ריווחי לבלתי-כלכלי ולפגוע ב-LTV קשות.
  </li>
</ul>

<p>
  על האנליסט לוודא שהפרויקט מאושר תחת תב&quot;ע קיימת ומאושרת —
  ולא מותנה בתב&quot;ע עתידית שעדיין בהליך אישור. פרויקט "שסומך" על
  אישור עירוני עתידי הוא פרויקט בסיכון תכנוני גבוה.
</p>

<!-- ===== סעיף 2 — היתרי בנייה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. היתרי בנייה — מה קורה כשהיתר מותקף לאחר הבנייה</h3>

<p>
  גם כאשר הבנייה הסתיימה — היתר הבנייה עלול להיות מותקף.
  צד שלישי (שכן, ארגון סביבתי, רשות תכנון) יכול להגיש ערר
  שיבטל את ההיתר למפרע ויחייב הריסה או שינויים משמעותיים.
</p>

<div style="background:#fce4ec;border-right:5px solid #c62828;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>תרחיש קיצוני:</strong><br>
  בית דין לתכנון ובנייה ביטל היתר לפרויקט מגורים של 80 יחידות
  לאחר שכנים הגישו ערר. הקבלן כבר בנה 6 קומות. בפועל — צו עצור בנייה
  ל-18 חודשים, עלויות משפטיות, עיכוב ריבית עתודה, ולחץ אדיר על
  ה-Interest Reserve. שווי הפרויקט ירד ב-30% ב-Distressed Sale.
</div>

<p>
  <strong>כיצד מתגוננים?</strong> וודא שתקופת ההתיישנות להגשת ערר
  חלפה (ב-ישראל — 45 יום ממועד מתן ההיתר לרוב). רכוש
  ביטוח כנגד ביטול היתר (Title &amp; Permit Insurance) כאשר קיים סיכון.
</p>

<!-- ===== סעיף 3 — זיהום סביבתי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. אחריות לזיהום סביבתי — מי נושא בה בעסקת מכר</h3>

<p>
  <strong>זיהום קרקע (Soil Contamination)</strong> הוא אחד הסיכונים
  הנסתרים הגדולים בנכסי תעשייה, לוגיסטיקה ונדל&quot;ן לשעבר תעשייתי.
  שאלת האחריות — מי משלם על פינוי הזיהום — קריטית בעסקת מכר:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>עיקרון המזהם משלם:</strong> לפי חוק הישראלי — המזהם
    האחראי נושא בעלויות. אולם זיהוי המזהם עשוי להיות קשה וממושך.
  </li>
  <li>
    <strong>קונה שרכש נכס מזוהם:</strong> גם אם הוא לא גרם לזיהום,
    הוא עלול לשאת באחריות על פינויו כבעל הנכס. ייצוג "As-Is" בחוזה
    לא תמיד מספיק להגנה.
  </li>
  <li>
    <strong>השפעה על LTV:</strong> עלות פינוי זיהום (ניקוי קרקע)
    יכולה לעלות מיליוני שקלים — ולהפחית את שווי הנכס בצורה קיצונית.
    המלווה חשוף לירידת ערך הבטוחה.
  </li>
</ul>

<p>
  <strong>הכרחי לבצע:</strong> סקר סביבתי שלב 1 (Phase 1 Environmental
  Survey) לפני כל עסקה בנכס לשעבר תעשייתי. אם מתגלה חשד — סקר שלב 2
  הכולל קידוחי דגימה.
</p>

<!-- ===== סעיף 4 — סיכון כותרת ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. סיכון כותרת — שיעבודים, זיקות הנאה וזכויות לא-רשומות</h3>

<p>
  <strong>Title Risk</strong> — סיכון כותרת — הוא הסיכון שבעלות הלווה
  בנכס אינה נקייה לחלוטין. גורמי סיכון עיקריים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>שיעבודים קיימים:</strong> שיעבוד שלא מחוק בטאבו מקיים
    עדיפות על ההלוואה החדשה — פוגע בדרגת השיעבוד של המלווה.
  </li>
  <li>
    <strong>זיקת הנאה (Easement):</strong> זכות צד שלישי לשימוש בחלק
    מהנכס (דרך מעבר, צינור, קו חשמל). יכולה להגביל פיתוח עתידי
    ולהפחית שווי.
  </li>
  <li>
    <strong>זכויות לא-רשומות:</strong> במיוחד בנכסים ישנים — יתכנו
    זכויות שכירות ותיקות, זכויות ירושה, או הסדרים בלתי-רשומים.
  </li>
  <li>
    <strong>עיקולי מס:</strong> חוב מס שמונח על הנכס קודם לשיעבוד
    המלווה. עיקול מס ברשות מקרקעי ישראל שאינו רשום בטאבו עלול
    להיות מפתיע.
  </li>
</ul>

<!-- ===== סעיף 5 — קדימות שיעבוד לעומת עיקול מס ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. קדימות שיעבוד לעומת עיקול מס</h3>

<p>
  בישראל, <strong>עיקול מס שנרשם לפני שיעבוד המלווה</strong> קודם
  לשיעבוד במקרה של מימוש. זה אחד מהסיכונים הנסתרים הגדולים ביותר:
  הבנק בדק טאבו, לא מצא שיעבוד — אך עיקול מס ברשות המסים קיים
  ולא נרשם בטאבו בזמן. בעת מימוש — הרשות גובה ראשון.
</p>

<p>
  <strong>הגנה:</strong> חיפוש מקיף לא רק בטאבו — גם ברשות המסים
  ובהוצאה לפועל, לפני כל Drawdown.
</p>

<!-- ===== סעיף 6 — סיכון ליטיגציה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. ליטיגציה — תביעות תלויות ועומדות</h3>

<p>
  תביעה משפטית פתוחה נגד הלווה יכולה:
</p>

<ul style="line-height:1.9;">
  <li>לגרום לעיקול נכסים — כולל הנכס הממושכן</li>
  <li>לפגוע ביכולת פירעון החוב (Cash Flow at Risk)</li>
  <li>ליצור אי-ודאות רגולטורית שמקשה על קבלת היתרים נוספים</li>
  <li>להחמיר את דירוג האשראי של הלווה</li>
</ul>

<p>
  חובה לקרוא את הגילוי בדוחות הכספיים על תביעות תלויות ועומדות,
  לדרוש חוות-דעת משפטית על כל תביעה מהותית, ולהעריך את ההסתברות
  לפסיקה שלילית ואת גודל הנזק הפוטנציאלי.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  "אין לנו תביעות מהותיות" — בדוק בעצמך. חפש בפנקס בתי המשפט,
  בגילויים בדוחות הכספיים, ובמחאות שכנים בהליכי תכנון. הלווה לא
  תמיד מגלה הכל מיוזמתו. לא מה שהוא אמר — אלא מה שמצאת בבדיקה —
  הוא הבסיס למזכר האשראי.
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של סיכוני תב\"ע, היתרי בנייה, זיהום סביבתי, "
    "Title Risk, קדימות שיעבוד לעומת עיקול מס, וסיכון ליטיגציה. "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים זיהוי סיכון תכנוני מתיאור פרויקט נתון, "
    "הערכת חשיפה לזיהום סביבתי, בדיקת קדימות שיעבוד לעומת עיקול מס בתרחיש נתון, "
    "וניתוח השפעת תביעה תלויה על יכולת שירות החוב. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — סיכוני רגולציה, משפט וסביבה
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>שינוי תב&quot;ע — בכיוון שלילי — יכול לאמץ את שווי הנכס ואת ה-LTV בבת-אחת.</strong>
    פרויקט שמותנה באישור תב&quot;ע עתידי נושא סיכון תכנוני גבוה שלא לממן.
  </li>
  <li>
    <strong>היתר בנייה שמותקף לאחר הבנייה עלול לגרום לצו עצור ולנזק קיצוני.</strong>
    וודא שתקופת ההתיישנות לעררים חלפה לפני מימון פרויקט שנגמר.
  </li>
  <li>
    <strong>זיהום סביבתי גורר עלויות פינוי שיכולות לאמץ את שווי הנכס לחלוטין.</strong>
    סקר סביבתי שלב 1 הוא חובה בנכסי תעשייה ולוגיסטיקה.
  </li>
  <li>
    <strong>Title Risk — שיעבודים נסתרים, זיקות הנאה, עיקולי מס — חייבים לאתר לפני Drawdown.</strong>
    חיפוש טאבו בלבד אינו מספיק — חפש גם ברשות המסים ובהוצאה לפועל.
  </li>
  <li>
    <strong>תביעה מהותית תלויה ועומדת היא אירוע Material Adverse Effect — בדוק אותה.</strong>
    חוות-דעת עו&quot;ד עצמאי על הסיכון הליטיגציוני היא חלק מ-DD משפטי תקין.
  </li>
</ol>

<h3 style="color:#1a2638;margin-top:24px;">מילון מונחים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">עברית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">אנגלית / מונח</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תוכנית בניין עיר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תב&quot;ע</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מסמך תכנוני שקובע ייעוד וזכויות בנייה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">זיהום קרקע</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Soil Contamination</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נוכחות חומרים מזיקים בקרקע הנכס</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סיכון כותרת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Title Risk</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ספק בנקיות הבעלות על הנכס</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">זיקת הנאה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Easement</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">זכות שימוש בנכס לצד שלישי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עיקול מס</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Tax Lien</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עיקול ברשות המסים הקודם לשיעבוד</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סקר סביבתי שלב 1</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Phase 1 Environmental Survey</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדיקה ראשונית לזיהום קרקע ומים</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — מסגרת ניהול סיכונים — מ-EWS ועד Stress Test
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  מסגרת ניהול סיכונים — מ-EWS ועד Stress Test
</h2>

<!-- ===== סעיף 1 — EWS ===== -->
<h3 style="color:#1a2638;">1. Early Warning System (EWS) — מערכת התרעה מוקדמת</h3>

<p>
  <strong>EWS — Early Warning System</strong> היא מערכת מעקב פנימית של הבנק
  המזהה הלוואות הנמצאות בסיכון גובר לפני שהן הופכות לחוב בעייתי (NPL —
  Non-Performing Loan). ה-EWS מטריגר סיווג ה"לוואה למעקב" (Watchlist).
</p>

<p>
  <strong>טריגרים נפוצים לכניסה ל-Watchlist:</strong>
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">טריגר</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תיאור</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">ספים מקובלים</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הפרת DSCR</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR ירד מתחת לסף ה-Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR מתחת ל-1.10 במשך רבעון</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הפרת LTV Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שווי הנכס ירד וה-LTV עלה מעל הסף</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">LTV מעל 75% בנכס מסחרי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פיגור בתשלום</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשלום ריבית או קרן עיכוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פיגור מעל 30 יום</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שינוי שלילי מהותי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ירידה חדה בתפוסה, אובדן שוכר עוגן</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תפוסה ירדה מ-85% ל-70% תוך רבעון</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 2 — תהליך מעקב אשראי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. תהליך מעקב אשראי (Credit Watch Process)</h3>

<p>
  ברגע שהלוואה נכנסת ל-Watchlist, מתחיל תהליך מובנה:
</p>

<ol style="line-height:1.9;">
  <li>
    <strong>התראה ראשונית:</strong> הצוות המטפל מקבל התראה מהמערכת ופותח
    תיק מעקב ייעודי עם תדירות דיווח גבוהה יותר (חודשית במקום רבעונית).
  </li>
  <li>
    <strong>ניתוח עומק:</strong> ביקור בנכס, עדכון הערכת שמאי, עדכון מודל
    התזרים, ובחינה מחודשת של כל ה-Covenants.
  </li>
  <li>
    <strong>דיון בוועדת אשראי:</strong> הצגת סטטוס המעקב, המלצות לשיפור
    תנאים, Forbearance, או התחלת הליכי מימוש.
  </li>
  <li>
    <strong>תוכנית פעולה:</strong> הסכמה עם הלווה על לוח זמנים לתיקון
    (Cure Period), תוספת בטחונות, הורדת קרן, או מימוש מסודר.
  </li>
</ol>

<!-- ===== סעיף 3 — Stress Testing ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. Stress Testing — מבחן עמידות לתיק הנדל&quot;ן</h3>

<p>
  <strong>Stress Test</strong> הוא ניתוח של השפעת תרחישי קיצון על תיק ההלוואות.
  הוא נדרש לפי הנחיות בנק ישראל ומבוצע ברמת הבנק ולעיתים ברמת הסניף.
  תרחישי הקיצון הסטנדרטיים בנדל&quot;ן ישראלי:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>עלייה בריבית של +200 נקודות בסיס (bps):</strong>
    הלוואות בריבית משתנה מתייקרות מיידית — עלייה בעומס שירות החוב.
    הלוואות קבועות לא מושפעות ישירות — אך שווי הנכסים (על בסיס Cap Rate)
    יורד עם ירידת ביקוש.
  </li>
  <li>
    <strong>עלייה בשיעור פנוי (Vacancy) ב-+20%:</strong>
    נכס מסחרי שתפוסתו 90% יורד ל-70% — NOI ירד, DSCR יאמץ,
    ונכסים מסוימים יפרו Covenants.
  </li>
  <li>
    <strong>ירידת שווי נכסים של 15%-:</strong>
    LTV יעלה — הלוואות שעמדו ב-65% LTV יעלו ל-76% — מעל הסף.
    הבנק נדרש להגדיל הפרשה.
  </li>
</ul>

<p>
  ה-Stress Test מחשב את השפעת כל תרחיש על: DSCR, LTV, הכנסות ריבית
  לבנק, ורמת ההפרשה הנדרשת (Provision) — ובוחן אם הבנק עמיד לתרחיש
  כזה מבלי לפגוע ביציבותו.
</p>

<!-- ===== סעיף 4 — ריכוז סיכון ומגבלות ריכוז ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. ריכוז סיכון ומגבלות ריכוז (Concentration Limits)</h3>

<p>
  <strong>Concentration Risk</strong> — סיכון ריכוז — הוא הסיכון
  שתיק ההלוואות מרוכז מדי בסוג נכס, אזור גיאוגרפי, או לווה בודד.
  בנק ישראל מחייב הגבלות ריכוז:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>ריכוז ענפי:</strong> אחוז מקסימלי של האשראי שמותר לתת
    לענף מסוים (למשל — נדל&quot;ן מסחרי לא יעלה על X% מסך תיק הנדל&quot;ן).
  </li>
  <li>
    <strong>ריכוז גיאוגרפי:</strong> אחוז מקסימלי ממרכז הארץ, מהפריפריה,
    מסוג אחד של שוק (תל אביב לבדה, למשל).
  </li>
  <li>
    <strong>ריכוז ב-Single Borrower:</strong> מגבלת חשיפה ללווה בודד
    (Large Exposure — 10%–25% מהון הבנק בהתאם לתקנות).
  </li>
</ul>

<!-- ===== סעיף 5 — Watchlist לעומת NPL ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. Watchlist לעומת NPL — סיווג לפי הנחיות בנק ישראל</h3>

<p>
  <strong>הסיווג לפי הנחיות בנק ישראל (הוראה 314):</strong>
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סיווג</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הפרשה נדרשת</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">רגיל (Standard)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תיק תקין, ללא סימני אזהרה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">1%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Watchlist (בתשומת לב)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">טריגר EWS, פגיעה בביטחון, חשיפה גוברת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">10%–25%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נחות (Substandard)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חולשה ברורה, ספק בגביה מלאה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">25%–50%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ספק (Doubtful)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">גביה חלקית בלבד סבירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">50%–75%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אבוד (Loss / NPL)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">גביה בלתי-אפשרית למעשה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">75%–100%</td>
    </tr>
  </tbody>
</table>

<p>
  ברגע שהלוואה מסווגת כ-NPL — הבנק עובר מניהול שוטף לניהול גביה:
  תהליכי מימוש בטחונות, מינוי מנהל מיוחד, ומשא ומתן על Workout.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  הפרשה לא מספיקה היא בעיה רגולטורית — לא רק חשבונאית.
  בנק שמחזיק הלוואות בסיווג רגיל שצריכות להיות Watchlist חשוף
  לביקורת בנק ישראל, לחיוב הפרשות רטרואקטיבי, ולפגיעה בהון הרגולטורי.
  סיווג אמיתי הוא חובה מקצועית — לא שאלה של נוחות עבודה.
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של טריגרי EWS, תהליך מעקב אשראי, "
    "מבחני עמידות (Stress Test), מגבלות ריכוז, וסיווג Watchlist לעומת NPL לפי הנחיות בנק ישראל. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים זיהוי טריגר EWS מנתוני הלוואה נתונים, "
    "ביצוע Stress Test פשוט על תיק נדל\"ן לפי תרחיש ריבית +200bps ו-Vacancy +20%, "
    "וסיווג הלוואות ל-Watchlist / Substandard / NPL לפי קריטריוני בנק ישראל. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — מסגרת ניהול סיכונים — מ-EWS ועד Stress Test
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>EWS מזהה הלוואות בסיכון מוקדם — לפני שהן הופכות ל-NPL.</strong>
    טריגרים מרכזיים: הפרת DSCR, חריגת LTV, פיגור בתשלום, אובדן שוכר עוגן.
  </li>
  <li>
    <strong>Watchlist מפעיל תהליך מובנה: ניתוח עומק, דיון ועדה, תוכנית פעולה עם הלווה.</strong>
    הלוואה ב-Watchlist אינה בהכרח NPL — אך דורשת מעקב הדוק ותוכנית תיקון.
  </li>
  <li>
    <strong>Stress Test בוחן שלושה תרחישים עיקריים: ריבית +200bps, Vacancy +20%, שווי -15%.</strong>
    כל תרחיש משפיע אחרת על DSCR, LTV, ורמת ההפרשה הנדרשת.
  </li>
  <li>
    <strong>Concentration Limits מגנים על הבנק מחשיפה ריכוזית לענף, אזור, או לווה בודד.</strong>
    חריגה ממגבלת ריכוז מחייבת אישור בנק ישראל ותוספת הון.
  </li>
  <li>
    <strong>הסיווג לפי הוראה 314: רגיל → Watchlist → נחות → ספק → NPL — עם הפרשה עולה בכל שלב.</strong>
    סיווג שגוי הוא סיכון רגולטורי — לא רק חשבונאי.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מערכת התרעה מוקדמת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">EWS — Early Warning System</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מערכת זיהוי הלוואות בסיכון גובר</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הלוואה במעקב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Watchlist</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואה שמקבלת ניטור הדוק בגלל סיכון גובר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מבחן עמידות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Stress Test</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתוח השפעת תרחישי קיצון על תיק ההלוואות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מגבלת ריכוז</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Concentration Limit</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מקסימום חשיפה לענף / אזור / לווה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חוב לא-מניב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NPL — Non-Performing Loan</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואה שאינה מניבה תשלומים סדירים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הפרשה לחובות מסופקים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Loan Loss Provision</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הפרשה חשבונאית לכיסוי הפסד צפוי</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לבחינה הסופית:</strong><br>
  השלמתם את שישת מודולי קורס 7 — ניהול סיכונים בנדל&quot;ן. למדתם לזהות
  וכמת סיכוני שוק ותזרים, לנתח סיכוני לווה ובטוחה, להבין סיכוני
  בנייה וייזום, לתמחר סיכוני רגולציה ומשפט, ולהפעיל מסגרת EWS ו-Stress Test.<br><br>
  הבחינה הסופית תכלול שאלות על זיהוי טריגרי EWS, ביצוע Stress Test
  פשוט, סיווג הלוואות לפי הוראה 314, וניתוח השפעת סיכוני תב&quot;ע וזיהום
  על ה-LTV. הגיעו מוכנים — ובהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "סיכוני בנייה, ייזום והשלמה",
        "slug": "sikune-biniya-yizum-hashlama",
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
        "title_he": "סיכוני רגולציה, משפט וסביבה",
        "slug": "sikune-regulatzia-mishpat-sviva",
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
        "title_he": 'מסגרת ניהול סיכונים — מ-EWS ועד Stress Test',
        "slug": "misgeret-nihul-sikuim",
        "estimated_minutes": 55,
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
    help = "Seed Course 7, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=7)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 7 not found. Run 'python manage.py seed_data' first."
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
