"""
Seeds Module 4-6 content for Course 11 (כתיבת מזכר אשראי).
Usage: python manage.py seed_c11_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — ניתוח סיכונים ומיתיגציה במזכר
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  ניתוח סיכונים ומיתיגציה במזכר האשראי
</h2>

<!-- ===== סעיף 1 — מבנה סעיף הסיכונים ===== -->
<h3 style="color:#1a2638;">1. מבנה סעיף הסיכונים במזכר</h3>

<p>
  סעיף הסיכונים הוא אחד הסעיפים הקריטיים ביותר במזכר האשראי. תפקידו
  אינו להסתיר סיכונים — אלא להציגם בצורה מובנית, לכמת אותם, ולהסביר
  כיצד הם מטופלים. ועדת האשראי מצפה לסעיף שמוכיח שהאנליסט הבין את
  הסיכונים ולא רק ציטט אותם.
</p>

<p>
  המבנה הסטנדרטי לכל סיכון הוא ארבעה אלמנטים:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.2;">
  <strong>סיכון:</strong> [תיאור ספציפי של הסיכון]<br>
  <strong>חומרה:</strong> גבוהה / בינונית / נמוכה — עם הסבר<br>
  <strong>מיתיגציה:</strong> [מנגנון ספציפי שמפחית את הסיכון]<br>
  <strong>סיכון שיורי:</strong> [הערכה של מה שנותר לאחר המיתיגציה]
</div>

<p>
  <strong>דוגמה:</strong><br>
  <em>סיכון: שוכר העוגן (60% מה-GRI) מסיים חוזה ב-2027 ועלול לא לחדש.
  חומרה: גבוהה — פינוי ישפיע מיידית על ה-NOI ב-38%. מיתיגציה: DSRA של
  6 חודשי שירות חוב, covenant לחידוש מקסימום 18 חודש לפני תפוגה, ו-Cash
  Sweep מעל DSCR 1.40x. סיכון שיורי: בינוני — שוק הלוגיסטיקה באזור
  מתוח, חלופות קיימות אך לאורך 12-18 חודש.</em>
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל זהב:</strong><br>
  כל סיכון שמוזכר חייב להיות מלווה במיתיגציה. סיכון ללא מיתיגציה
  הוא בעיה פתוחה — לא ניתוח. ועדת האשראי תשאל מיד: "ומה עושים עם זה?"
  — וטוב שהתשובה כבר כתובה במזכר.
</div>

<!-- ===== סעיף 2 — סיכוני שוק ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. סיכון שוק — Market Risk</h3>

<p>
  <strong>סיכון השוק</strong> הוא הסיכון שתנאי השוק יתדרדרו — שוק
  שכירות יחלש, ביקוש ירד, Cap Rate יעלה — ויפגעו בשווי הנכס וביכולת
  שירות החוב. כיצד כותבים אותו נכון:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>תיאור ספציפי:</strong> "שוק משרדים ב-X בצפי עודף היצע של
    Y אלף מ&quot;ר ב-2025–2026" — לא "שוק המשרדים תחרותי".
  </li>
  <li>
    <strong>כמות ההשפעה:</strong> כמה % ירידה בדמי השכירות יוריד את
    ה-DSCR מתחת לסף ה-Covenant? זהו ה-Break-Even Analysis.
  </li>
  <li>
    <strong>מיתיגציה:</strong> חוזי שכירות ארוכי-טווח הכוללים Escalation
    Clause; פיזור שוכרים; Covenant LTV שמגן על המלווה בירידת שווי.
  </li>
</ul>

<div style="background:#fce4ec;border-right:5px solid #c62828;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה:</strong><br>
  לכתוב "סיכון שוק: נמוך" ללא נימוק כמותי הוא אחד
  הדגלים האדומים הנפוצים ביותר שועדת אשראי מזהה. "נמוך" ללא הסבר
  אינו ניתוח — הוא משאלת לב. הציגו נתוני שוק, השוו לפרויקטים דומים,
  והסבירו מדוע הפרויקט הספציפי הזה עמיד יחסית.
</div>

<!-- ===== סעיף 3 — סיכון נזילות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. סיכון נזילות — Liquidity Risk</h3>

<p>
  <strong>סיכון נזילות</strong> הוא הסיכון שהלווה לא יוכל לשרת את
  החוב בעיתוי הנדרש — גם אם בטווח הארוך הנכס רווחי. סיכון נזילות
  הוא לרוב קצר-טווח: תחנה בהלוואה, פינוי שוכר, הוצאת Capex בלתי-צפויה.
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>מיתיגציה מרכזית — DSRA (Debt Service Reserve Account):</strong>
    חשבון ייעודי שבו הלווה מחזיק מראש 3-6 חודשי שירות חוב. במקרה של
    קושי נזילות זמני — המלווה שואב מה-DSRA לפני שהוא מכריז על ברירת מחדל.
    גודל ה-DSRA נקבע לפי רמת הסיכון של הנכס ועונתיות ההכנסות.
  </li>
  <li>
    <strong>מנגנון Cash Sweep:</strong> כל תזרים עודף מעל DSCR מוגדר
    (למשל 1.35x) מועבר אוטומטית לפירעון מוקדם או לחיזוק ה-DSRA.
    מונע מהלווה לחלק דיבידנד בתקופות שמחלישות את כרית הנזילות.
  </li>
</ul>

<!-- ===== סעיף 4 — ריכוז שוכרים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. סיכון ריכוז שוכרים — Tenant Concentration Risk</h3>

<p>
  ריכוז שוכרים הוא אחד הסיכונים הנפוצים ביותר בנכסים מסחריים —
  כאשר שוכר בודד מהווה אחוז גבוה מההכנסות הכוללות.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">רמת ריכוז</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דרישת מיתיגציה מינימלית</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נמוך</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אף שוכר מעל 25% מה-GRI</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSRA 3 חודשים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בינוני</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוכר בודד 25%–50% מה-GRI</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSRA 6 חודשים + Covenant חידוש חוזה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גבוה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוכר בודד מעל 50% מה-GRI</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSRA 9-12 חודשים + ערבות אישית + Cash Sweep</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 5 — סיכון בנייה / Capex ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. סיכון בנייה ו-Capex — Construction &amp; Capital Expenditure Risk</h3>

<p>
  אפילו בנכסים קיימים קיים סיכון Capex: גג שדורש החלפה, מערכות
  מיזוג, חניון — כולם הוצאות שאינן מתוכננות עלולות לפגוע בנזילות
  הלווה ולשחוק את ה-DSCR. כיצד מתמחרים זאת במזכר:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>Capex Reserve:</strong> מנגנון שבו סכום שנתי קבוע מוזרם
    לחשבון ייעודי לתחזוקה הונית. לרוב $X לשנה לכל יחידה / מ&quot;ר.
    מונע מצב שבו הוצאת Capex גדולה תפגע בתזרים שירות החוב.
  </li>
  <li>
    <strong>Technical Due Diligence:</strong> דוח מהנדס עצמאי שסוקר
    את מצב הנכס ומספק הערכה של Capex הנדרש ב-5 ו-10 שנים הקרובות.
    הוא הבסיס לקביעת גובה ה-Capex Reserve.
  </li>
</ul>

<!-- ===== סעיף 6 — סיכון ריבית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. סיכון ריבית — Interest Rate Risk</h3>

<p>
  הלוואות בריבית משתנה (Floating Rate) חשופות לעלייה בריבית.
  עלייה של 200 נקודות בסיס עלולה להכפיל את עלות ההלוואה ולהוריד
  את ה-DSCR מתחת לסף הקובנאנט.
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>מיתיגציה — הסכם Cap/Swap:</strong> רכישת ריבית מקסימום
    (Cap) — הלווה משלם פרמיה חד-פעמית ומוגן מעלייה בריבית מעל רמה
    מוגדרת. חלופה: Swap — המרת ריבית משתנה לקבועה לכל אורך ההלוואה.
    כתיבה נכונה: "הלווה מחויב לרכוש Cap על מלוא יתרת ההלוואה ב-SOFR + 3%
    לכל תקופת ההלוואה."
  </li>
  <li>
    <strong>ניתוח רגישות:</strong> הצגת DSCR בתרחיש ריבית +100bps,
    +200bps, +300bps — ומתי הוא מפר את הקובנאנט. זה חלק מ-Stress Test
    שמוכיח שהמבנה עמיד.
  </li>
</ul>

<!-- ===== סעיף 7 — סיכון לווה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">7. סיכון הלווה — Borrower Risk</h3>

<p>
  סיכון הלווה הוא הסיכון שהלווה עצמו — ולא רק הנכס — יכשל. גורמי
  סיכון עיקריים:
</p>

<ul style="line-height:1.9;">
  <li><strong>ריכוז עסקי:</strong> 80% מהכנסות הלווה ממקור בודד</li>
  <li><strong>מינוף יתר:</strong> חוב כולל גבוה ביחס להון העצמי</li>
  <li><strong>ניסיון מוגבל:</strong> לווה שלא ניהל נכס דומה בעבר</li>
  <li><strong>תביעות תלויות:</strong> ליטיגציה שעלולה לפגוע בנזילות</li>
</ul>

<p>
  <strong>מיתיגציות לסיכון לווה:</strong> ערבות אישית של בעל השליטה;
  Covenant Package שמגביל חלוקת דיבידנד ועסקאות עם צדדים קשורים;
  דרישה לביטוח חיי הלווה לטובת המלווה.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מנגנוני מיתיגציה — סיכום:</strong><br>
  <strong>DSRA</strong> — חשבון עתודה לשירות חוב; מגן על נזילות.<br>
  <strong>Cash Sweep</strong> — תזרים עודף מועבר לפירעון / DSRA; מגן על ריכוז רווחים.<br>
  <strong>Covenant Package</strong> — DSCR, LTV, דיווח, הגבלת חוב נוסף; מגן על מבנה.<br>
  <strong>ערבות אישית (Personal Guarantee)</strong> — בעל השליטה ערב אישית; מגן מסיכון לווה.
</div>

<!-- ===== סעיף 8 — סיכון שיורי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">8. סיכון שיורי — Residual Risk</h3>

<p>
  <strong>סיכון שיורי</strong> הוא הסיכון שנותר לאחר שכל מנגנוני
  המיתיגציה הופעלו. זהו החלק שהמלווה נוטל על עצמו במודע. הצגת
  הסיכון השיורי בצורה אמינה — לא "אין סיכון שיורי" — מעידה על ניתוח
  בוגר:
</p>

<ul style="line-height:1.9;">
  <li><strong>שיורי נמוך:</strong> הסיכון קטן, מוכר, ניתן לניטור רציף</li>
  <li><strong>שיורי בינוני:</strong> יש חשיפה, אך המבנה עמיד לרוב התרחישים</li>
  <li><strong>שיורי גבוה:</strong> עדיין מצדיק אישור? — דרוש הסבר מדוע ברווח / בטחון מכסה</li>
</ul>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מבנה סעיף הסיכונים, סוגי הסיכון העיקריים (שוק, נזילות, "
    "ריכוז שוכרים, Capex, ריבית, לווה), מנגנוני מיתיגציה (DSRA, Cash Sweep, Covenant, ערבות אישית), "
    "ומשמעות הסיכון השיורי. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים ניסוח סעיף סיכון מלא לפי המבנה (תיאור, חומרה, מיתיגציה, שיורי) "
    "לנכס נתון, זיהוי מנגנון המיתיגציה המתאים לכל סיכון מרשימה, "
    "ובניית ניתוח רגישות DSCR לתרחיש ריבית +200bps. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — ניתוח סיכונים ומיתיגציה במזכר
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>כל סיכון חייב ארבעה אלמנטים: תיאור, חומרה, מיתיגציה, שיורי.</strong>
    סיכון ללא מיתיגציה הוא בעיה פתוחה שועדת האשראי תדרוש לסגור.
  </li>
  <li>
    <strong>חומרת סיכון שוק חייבת להיות מגובה נתונים — לא תחושה.</strong>
    ציינו את אחוז ירידת דמי השכירות שיפר את הקובנאנט; זהו ה-Break-Even.
  </li>
  <li>
    <strong>DSRA ו-Cash Sweep הם מנגנוני ההגנה הנפוצים ביותר מסיכון נזילות.</strong>
    גודל ה-DSRA (3/6/9 חודשים) נקבע לפי רמת הריכוז ועונתיות ההכנסות.
  </li>
  <li>
    <strong>ריכוז שוכרים מעל 50% מה-GRI דורש DSRA 9-12 חודשים + ערבות אישית.</strong>
    המיתיגציה חייבת להיות פרופורציונלית לחומרת הריכוז.
  </li>
  <li>
    <strong>סיכון שיורי אמיתי הוא סימן לניתוח בוגר — לא לחולשת המזכר.</strong>
    ועדת האשראי מעדיפה "שיורי בינוני עם נימוק" על פני "אין סיכון שיורי" שמסתיר בעיות.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חשבון עתודה לשירות חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSRA — Debt Service Reserve Account</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חשבון ייעודי המחזיק X חודשי שירות חוב</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניגוף תזרים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cash Sweep</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">העברה אוטומטית של תזרים עודף לפירעון / DSRA</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ערבות אישית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Personal Guarantee</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">התחייבות אישית של בעל השליטה לפרוע את החוב</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סיכון שיורי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Residual Risk</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הסיכון הנותר לאחר הפעלת כל מנגנוני המיתיגציה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עתודת הוצאות הוניות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Capex Reserve</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חשבון ייעודי לתחזוקה הונית שנתית של הנכס</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הסכם גבול ריבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Interest Rate Cap</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הגנה מפני עלייה בריבית מעל רמה מוגדרת</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — תנאים, קובננטים והמלצה
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  תנאים, קובננטים והמלצה
</h2>

<!-- ===== סעיף 1 — תנאים מוצעים ===== -->
<h3 style="color:#1a2638;">1. סעיף התנאים המוצעים — Term Sheet במזכר</h3>

<p>
  סעיף התנאים המוצעים מציג את מבנה ההלוואה שהאנליסט ממליץ לאשר.
  הוא חייב להיות ספציפי ומדויק — כל מרכיב שמוצג "בערך" מעיד על
  ניתוח לא גמור. המרכיבים הסטנדרטיים:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מרכיב</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דוגמת ניסוח</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סכום הלוואה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">₪45,000,000 (ארבעים וחמישה מיליון ש&quot;ח)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">LTV בסגירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">62.5% מהשווי המשוערך של ₪72,000,000</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מועד פירעון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">5 שנים ממועד הסגירה, עם אופציית הארכה שנתית פעמיים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אמורטיזציה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">25 שנה Amortization Schedule; Balloon Payment במועד הפירעון</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ריבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Prime + 1.50% משתנה; או Swap לריבית קבועה לפי בחירת הלווה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עמלה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">0.75% Origination Fee; 0.25% Annual Commitment Fee על יתרה</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 2 — קובננטים פיננסיים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. קובננטים פיננסיים — Financial Covenants</h3>

<p>
  <strong>Covenant פיננסי</strong> הוא תנאי כמותי שהלווה מחויב לעמוד
  בו לאורך חיי ההלוואה. הפרת Covenant מהווה Event of Default שמאפשר
  למלווה לדרוש פירעון מוקדם. כיצד כותבים Covenant נכון:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.2;">
  <strong>שם הקובנאנט:</strong> DSCR מינימלי<br>
  <strong>סף:</strong> לא פחות מ-1.25x<br>
  <strong>תדירות בדיקה:</strong> רבעונית, על בסיס NOI TTM<br>
  <strong>Cure Period:</strong> 45 יום לתיקון ממועד ההפרה<br>
  <strong>השלכה:</strong> Sweep מלא של תזרים עודף; הפסקת אופציית הארכה
</div>

<p>
  <strong>שלושת הקובננטים הפיננסיים הנפוצים ביותר:</strong>
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>DSCR Covenant:</strong> NOI חלקי שירות חוב שנתי.
    נבדק רבעונית על בסיס 12 חודשים אחורה. סף מקובל: 1.20x–1.30x.
    הפרה מתמשכת: הפעלת Cash Sweep ואיסור על Distributions.
  </li>
  <li>
    <strong>LTV Covenant:</strong> יתרת הלוואה חלקי שווי שמאי עדכני.
    נבדק על בסיס הערכת שמאי שנתית. סף מקובל: לא יעלה על 70%–75%.
    הפרה: הלווה מחויב להזרים הון / לפרוע חלק מהקרן תוך 60 יום.
  </li>
  <li>
    <strong>DSRA Covenant:</strong> יתרת חשבון ה-DSRA תהיה לפחות
    שווה ל-6 חודשי שירות חוב בכל עת. נבדק חודשי. הפרה: Cure Period
    של 30 יום לחיזוק היתרה.
  </li>
</ul>

<!-- ===== סעיף 3 — קובננטים לא-פיננסיים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. קובננטים לא-פיננסיים — Non-Financial Covenants</h3>

<p>
  <strong>קובננטים לא-פיננסיים</strong> הם מגבלות התנהגותיות שאינן
  מוצגות כמספר — אך קריטיות להגנת המלווה:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>דרישות דיווח:</strong> דוחות כספיים מבוקרים תוך 120 יום מסוף
    שנה; דוחות עסקיים רבעוניים (NOI, Occupancy, Rent Roll) תוך 30 יום
    מסוף כל רבעון; הודעה מיידית על כל Event of Default פוטנציאלי.
  </li>
  <li>
    <strong>ביטוח:</strong> הלווה ישמור בכל עת ביטוח נכס בשווי כינון מלא,
    ביטוח אחריות צד שלישי של לא פחות מ-$X, ו-Business Interruption
    Insurance לתקופה של 12 חודשים. המלווה יהיה Named Insured.
  </li>
  <li>
    <strong>הגבלת חוב נוסף:</strong> הלווה לא יתקשר בהלוואה נוספת על
    הנכס הממושכן ללא הסכמה מפורשת ובכתב מהמלווה. כולל: Mezzanine,
    Preferred Equity, Sale-Leaseback, ומשכנתה שנייה.
  </li>
  <li>
    <strong>הגבלת עסקאות צדדים קשורים:</strong> כל עסקה בין הלווה לצד
    קשור (בעל שליטה, חברה בת) תהיה בתנאי שוק ותידרש לאישור מוקדם
    מהמלווה אם עולה על ₪X.
  </li>
</ul>

<!-- ===== סעיף 4 — ניסוח קובנאנט מדויק ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. ניסוח Covenant מדויק — ארבעה מרכיבים חובה</h3>

<p>
  Covenant ללא כל ארבעת המרכיבים הבאים אינו ניתן לאכיפה:
</p>

<ol style="line-height:1.9;">
  <li><strong>סף (Threshold):</strong> הערך המספרי המדויק — לא "סביר" ולא "מקובל בשוק"</li>
  <li><strong>תדירות בדיקה (Test Frequency):</strong> מתי ואיך נמדד — רבעוני / שנתי / ב-Drawdown</li>
  <li><strong>Cure Period:</strong> כמה זמן יש ללווה לתקן לאחר הפרה — לרוב 30–60 יום</li>
  <li><strong>השלכת הפרה (Breach Consequence):</strong> מה קורה אם ה-Cure Period פג — Event of Default, Sweep, עצירת אופציה</li>
</ol>

<div style="background:#fce4ec;border-right:5px solid #c62828;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה:</strong><br>
  תנאים מעורפלים כמו "תיעוד מספק" או "הסכמת הבנק לא תמנע
  שלא בסבירות" אינם ניתנים לאכיפה ומזמינים ויכוחים משפטיים.
  כל תנאי וכל Covenant חייב להיות ספציפי, מדיד, ומוגדר זמן.
</div>

<!-- ===== סעיף 5 — סעיף ההמלצה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. סעיף ההמלצה — The Recommendation</h3>

<p>
  סעיף ההמלצה הוא ה-Punchline של המזכר. הוא מסכם את הניתוח כולו
  ומביא החלטה ברורה. המבנה הסטנדרטי:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;">
  "בהסתמך על הניתוח לעיל, ובכפוף לתנאים המפורטים להלן, אני ממליץ על<br>
  [אישור / אישור מותנה / דחייה] של הלוואה בסך ₪X לטובת [שם הלווה]<br>
  לפי התנאים המוצגים בסעיף X לעיל."
</div>

<p>
  <strong>שלוש אפשרויות המלצה:</strong>
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>אישור (Approval):</strong> המזכר מספיק בסיס לאישור מלא.
    נדיר — רוב האישורים כוללים לפחות 2-3 תנאים מוקדמים.
  </li>
  <li>
    <strong>אישור מותנה (Conditional Approval):</strong> אישור כפוף
    לעמידה ברשימת תנאים מוקדמים (CPs). הנפוץ ביותר בפועל.
  </li>
  <li>
    <strong>דחייה (Decline):</strong> המזכר מסביר מדוע הסיכון אינו
    מוצדק. דחייה חייבת להיות מנומקת — לא רק "הסיכון גבוה מדי".
  </li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>עיקרון מפתח:</strong><br>
  המלצה ללא תנאים מוקדמים היא נדירה. רוב האישורים כוללים 3-7 תנאים
  מוקדמים. אל תהססו לכלול תנאים — הם מגנים גם על הלווה וגם על המלווה
  ומסמנים שהניתוח מעמיק.
</div>

<!-- ===== סעיף 6 — תנאים מוקדמים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. תנאים מוקדמים — Conditions Precedent (CPs)</h3>

<p>
  <strong>CPs — Conditions Precedent</strong> הם פריטים ספציפיים
  שחייבים להתקיים לפני ה-Drawdown הראשון. הם שונים מ-Covenants:
  Covenants נאכפים לאורך חיי ההלוואה; CPs חייבים להתקיים לפני
  השחרור הראשון של הכסף.
</p>

<p>
  <strong>דוגמאות ל-CPs נפוצים:</strong>
</p>

<ul style="line-height:1.9;">
  <li>הגשת הערכת שמאי מאושרת לא ישנה מ-90 יום</li>
  <li>אישור עורך-דין לנקיון הכותרת (Title Opinion)</li>
  <li>המצאת פוליסות ביטוח עם המלווה כ-Named Insured</li>
  <li>רישום משכנתה ראשונה לטובת המלווה בלשכת רישום המקרקעין</li>
  <li>חתימה על הסכם DSRA וויסות יתרה ראשונית של ₪X</li>
  <li>המצאת דוחות כספיים מבוקרים לשנת ____</li>
  <li>אישור כלל ה-Covenants בחוזה ההלוואה הסופי</li>
</ul>

<div style="background:#fce4ec;border-right:5px solid #c62828;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה:</strong><br>
  "תיעוד לשביעות רצון הבנק" הוא CP שאינו ניתן לאכיפה.
  כתבו במקום: "הגשת הסכם שכירות מקורי חתום עם [שם שוכר] ל-[X שנים]
  בדמי שכירות לא פחות מ-₪X לחודש." ספציפיות היא ההגנה.
</div>

<!-- ===== גשר למודול 6 ===== -->
<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:32px 0;border-radius:4px;">
  <strong>גשר למודול 6 — כתיבה מקצועית ושגיאות נפוצות:</strong><br>
  למדנו את המבנה — תנאים, קובננטים, והמלצה. אבל מבנה נכון לא מספיק
  אם הכתיבה עצמה אינה ברורה, עקבית ומקצועית. מודול 6 יעסוק בחמישה
  עקרונות הכתיבה המקצועית ובשגיאות הנפוצות ביותר שאנליסטים עושים —
  שגיאות שגורמות לועדת אשראי לדחות מזכרים טובים שנכתבו בצורה גרועה.
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מרכיבי ה-Term Sheet, קובננטים פיננסיים (DSCR, LTV, DSRA), "
    "קובננטים לא-פיננסיים (דיווח, ביטוח, הגבלת חוב), ניסוח Covenant מדויק, "
    "מבנה סעיף ההמלצה, ותנאים מוקדמים (CPs). "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים ניסוח Covenant DSCR מלא עם כל ארבעת מרכיביו, "
    "זיהוי CPs חסרים ברשימה נתונה, כתיבת סעיף המלצה מלא לעסקה נתונה, "
    "ותיקון Covenants מעורפלים לניסוח אכיף וספציפי. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — תנאים, קובננטים והמלצה
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>ה-Term Sheet חייב להיות מלא ומדויק — כל מרכיב שמוצג "בערך" מעיד על ניתוח לא גמור.</strong>
    LTV, ריבית, אמורטיזציה, ועמלות — כולם חייבים מספר ספציפי.
  </li>
  <li>
    <strong>Covenant פיננסי חייב ארבעה מרכיבים: סף, תדירות, Cure Period, והשלכת הפרה.</strong>
    Covenant חסר אחד מהם אינו ניתן לאכיפה ומסכן את המלווה.
  </li>
  <li>
    <strong>קובננטים לא-פיננסיים (דיווח, ביטוח, הגבלת חוב) חשובים לא פחות מהפיננסיים.</strong>
    הם מגנים מפני שינויים מבניים שלא ניתן לזהות רק ממספרים.
  </li>
  <li>
    <strong>אישור מותנה עם 3-7 CPs הוא הנורמה — לא החריג.</strong>
    CPs ספציפיים מגנים על שני הצדדים ומוכיחים שהניתוח מעמיק.
  </li>
  <li>
    <strong>תנאים מעורפלים כמו "תיעוד מספק" אינם ניתנים לאכיפה — כתבו ספציפי.</strong>
    כל CP חייב לציין מסמך מוגדר, מוציא מוגדר, וסכום / תאריך מוגדר.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תנאים מוקדמים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Conditions Precedent (CPs)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פריטים חובה לפני Drawdown ראשון</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קובנאנט</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תנאי שהלווה חייב לעמוד בו לאורך ההלוואה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תקופת תיקון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cure Period</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פרק זמן לתיקון הפרת Covenant לפני Event of Default</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אירוע ברירת מחדל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Event of Default</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אירוע המאפשר למלווה לדרוש פירעון מיידי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אמורטיזציה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Amortization</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">לוח פירעון קרן וריבית לאורך חיי ההלוואה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אישור מותנה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Conditional Approval</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אישור הכפוף לעמידה ברשימת תנאים מוקדמים</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — עקרונות כתיבה מקצועית ושגיאות נפוצות
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  עקרונות כתיבה מקצועית ושגיאות נפוצות במזכר האשראי
</h2>

<!-- ===== סעיף 1 — 5 עקרונות ===== -->
<h3 style="color:#1a2638;">1. חמשת עקרונות הכתיבה המקצועית</h3>

<p>
  מזכר אשראי מקצועי אינו רק מקיף — הוא כתוב לפי עקרונות שמאפשרים
  לוועדת האשראי לקבל החלטה מהירה, מושכלת ומנומקת. חמשת העקרונות:
</p>

<ol style="line-height:1.9;">
  <li>
    <strong>עובדתי (Factual) — כל טענה מגובה מקור.</strong>
    "שוק המשרדים באזור מחוזק" — מאיפה המידע? ציינו: "לפי דוח JLL
    Q1-2025, התפוסה באזור עלתה מ-78% ל-84%." טענה ללא מקור היא דעה
    — לא ניתוח.
  </li>
  <li>
    <strong>כמותי (Quantitative) — מספרים, לא תארים.</strong>
    "הלווה חזק פיננסית" — ומה זה אומר? במקום: "הלווה הציג יחס חוב
    להון של 1.8x, NOI שנתי של ₪4.2M וכיסוי שירות חוב של 1.38x ב-2024."
    מספרים ניתנים לאימות ולהשוואה — תארים לא.
  </li>
  <li>
    <strong>תמציתי (Concise) — אין ריפוד.</strong>
    כל משפט שאינו מוסיף מידע — נמחק. "כידוע לכל, שוק הנדל&quot;ן הוא
    מורכב ודינמי..." — זה ריפוד. המקצוען כותב: "הנכס ממוקם בשוק
    תחרותי עם Vacancy Rate של 12% — גבוה מהמצע ב-4%."
  </li>
  <li>
    <strong>מאוזן (Balanced) — מוכר חוזקות וחולשות.</strong>
    מזכר שמציג רק את החיובי נראה כמו מצגת שיווקית — לא כניתוח אשראי.
    ועדת האשראי תחפש לבד את הסיכונים. עדיף שהאנליסט יציג אותם ראשון
    ויסביר כיצד הם מנוהלים.
  </li>
  <li>
    <strong>מסכם (Conclusive) — המלצה ברורה.</strong>
    מזכר שמציג מידע ולא מגיע למסקנה נכשל בתפקידו. ועדת האשראי צריכה
    לדעת מה האנליסט ממליץ — לא "מצד אחד X, מצד שני Y". המלצה מפורשת
    היא חלק בלתי-נפרד מהמסמך.
  </li>
</ol>

<!-- ===== סעיף 2 — שגיאות נפוצות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. שגיאות הכתיבה הנפוצות ביותר</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שגיאה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דוגמה לניסוח שגוי</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">ניסוח נכון</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח שם-תואר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"לווה חזק עם ניסיון מוכח"</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"הלווה ניהל 4 פרויקטים דומים 2018-2024; IRR ממוצע 14.5%"</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">היגיון מעגלי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"העסקה עובדת כי ה-NOI מספיק לשירות החוב"</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"NOI ₪3.8M כולל Vacancy 10%; DSCR 1.32x לפי שירות חוב שנתי ₪2.88M"</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">היעדר ה-Bear Case</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מציג רק Base Case חיובי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מציג Base / Downside / Stress — ומסביר מה קורה בכל תרחיש</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שפת שיווק הלווה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"נכס פרימיום במיקום אסטרטגי עם פוטנציאל עצום"</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"נכס Grade B בשוק X; Vacancy 9%; Cap Rate 6.8%"</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חוסר עקביות במספרים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI ₪4M בסעיף 3, ₪3.8M בסעיף 6</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מספר אחד, מקור אחד — ועקביות מלאה בין כל הסעיפים</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 3 — ניסוח ההמלצה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. ניסוח ההמלצה — ההבדל בין עמדה לניתוח</h3>

<p>
  אנליסטים רבים מסיימים את המזכר במשפט כמו: "בעוד שקיימים סיכונים,
  על המאזן נראה שהעסקה הגיונית ויש לשקול אישורה." זהו ניסוח שנמנע
  מלקיחת עמדה — ושממש עצבן כל ועדת אשראי.
</p>

<p>
  <strong>מדוע אנליסטים מסתירים את המלצתם:</strong> חשש מלקבל אחריות
  אישית על ההחלטה. אבל — זו בדיוק העבודה. ועדת האשראי שכרה אתכם
  להביע עמדה מקצועית — לא לצטט נתונים ולהותיר את ההחלטה לה.
</p>

<p>
  <strong>ניסוח נכון של המלצה:</strong>
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;">
  "בהסתמך על ניתוח הנ&quot;ל, אני ממליץ על <strong>אישור מותנה</strong> של
  ההלוואה בסך ₪45M לטובת [לווה X], בכפוף לתנאים המוקדמים המפורטים
  בנספח א'. הסיכון הראשי — ריכוז שוכרים גבוה — מנוהל במנגנוני DSRA
  ו-Cash Sweep ומוצג בפירוט בסעיף 5. הסיכון השיורי אינו מצדיק דחייה."
</div>

<!-- ===== סעיף 4 — רשימת בדיקה עצמית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. רשימת בדיקה עצמית לפני הגשת המזכר — 10 נקודות</h3>

<ol style="line-height:1.9;">
  <li>כל הנתונים הפיננסיים עקביים בין כל סעיפי המזכר</li>
  <li>כל טענה עובדתית מגובה מקור מצוין</li>
  <li>כל סיכון מגובה מיתיגציה מוגדרת — ולא "כללית"</li>
  <li>כל Covenant כולל סף, תדירות, Cure Period, והשלכה</li>
  <li>כל CP ספציפי — מסמך מוגדר, מוציא מוגדר, תאריך / סכום</li>
  <li>ה-Bear Case מוצג — לא רק ה-Base Case</li>
  <li>אין שפת שיווק של הלווה שנשארה במזכר</li>
  <li>ההמלצה ברורה: אישור / אישור מותנה / דחייה</li>
  <li>אין משפטים מעגליים שמנמקים את עצמם</li>
  <li>המזכר אינו ארוך יותר מהנדרש — כל סעיף תורם ניתוח</li>
</ol>

<!-- ===== סעיף 5 — מבחן העט האדום ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. מבחן העט האדום — כיצד קורא אותו קצין האשראי הבכיר</h3>

<p>
  לפני שמזכר מגיע לועדת אשראי — הוא עובר לרוב דרך קצין אשראי בכיר
  שיש לו ניסיון של 10-20 שנה. הוא קורא את המזכר בעט אדום ביד. מה הוא
  מחפש?
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>עקביות פנימית:</strong> הוא בודק אם NOI בסעיף 3 = NOI
    ב-DSCR Calculation בסעיף 5. חוסר עקביות אחת — ועל המזכר כולו
    נשאלת שאלה.
  </li>
  <li>
    <strong>תשובה ל-Bear Case:</strong> הוא ישאל: "מה קורה אם שוכר
    העוגן יוצא?" — אם התשובה אינה במזכר, הוא יחזיר אותו לתיקון.
  </li>
  <li>
    <strong>מקור הנתונים:</strong> מספרים ללא מקור = מספרים שניתן
    לפקפק בהם. "לפי דוח X שהוגש ביום Y" — קביל. "בערך ₪3M" — לא.
  </li>
  <li>
    <strong>ספציפיות ה-CPs:</strong> CP מעורפל = פרצה. הוא ידאג
    שכל CP ניתן לאימות אובייקטיבי לפני Drawdown.
  </li>
  <li>
    <strong>האם האנליסט "מכר" את העסקה:</strong> אם המזכר נשמע
    כמו מצגת יזם — הוא ידחה אותו. ניטרליות אנליטית, לא התלהבות.
  </li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>עיקרון הסיום:</strong><br>
  אם לא הייתם מרגישים נוח להגן על כל משפט במזכר בפני ועדת האשראי —
  חיזרו לשולחן ותתקנו אותו. הגשת מזכר לועדה היא לקיחת עמדה מקצועית
  — וזו בדיוק העבודה.
</div>

<!-- ===== גשר לקורס 12 ===== -->
<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:32px 0;border-radius:4px;">
  <strong>גשר לקורס 12 — פרויקט גמר:</strong><br>
  מזכר האשראי הוא התוצר המרכזי של פרויקט הגמר. בקורס 12 תיישמו את כל
  מה שלמדתם בקורסים 1-11 — ניתוח שוק, הערכת שווי, מדדים פיננסיים,
  תזרים מזומנים, מבנה עסקה, ניהול סיכונים, בדיקת מסמכים משפטיים,
  מודלים פיננסיים, וכעת — כתיבה מקצועית — לכדי מזכר אשראי מלא על
  נכס נדל&quot;ן אמיתי. זה הרגע שכל הקורס הזה הוביל אליו.
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של חמשת עקרונות הכתיבה המקצועית, שגיאות הכתיבה הנפוצות, "
    "ניסוח המלצה מקצועי, רשימת הבדיקה העצמית, ומבחן העט האדום. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים תיקון קטעי מזכר שגויים לפי חמשת עקרונות הכתיבה, "
    "זיהוי שגיאות כתיבה מסוג ניתוח שם-תואר, היגיון מעגלי, ושפת שיווק בקטעים נתונים, "
    "ויישום רשימת הבדיקה העצמית על מזכר לדוגמה. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — עקרונות כתיבה מקצועית ושגיאות נפוצות
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>חמשת עקרונות הכתיבה: עובדתי, כמותי, תמציתי, מאוזן, מסכם.</strong>
    הפרת אחד מהם — והמזכר מחזיר אותך. שמרו על כולם בכל משפט.
  </li>
  <li>
    <strong>ניתוח שם-תואר ("לווה חזק", "נכס פרימיום") הוא שגיאה שמחזירה מזכרים.</strong>
    כל תואר חייב להתחלף במספר: "DSCR 1.38x", "IRR ממוצע 14.5%".
  </li>
  <li>
    <strong>הצגת Bear Case היא חובה — לא אופציה.</strong>
    אנליסט שמציג רק Base Case נראה כמי שמסתיר סיכונים. הציגו את כל שלושת התרחישים.
  </li>
  <li>
    <strong>המלצה ברורה עם עמדה — לא ניסוח גדר.</strong>
    "אישור מותנה ב-X תנאים" מקצועי יותר מ"יש לשקול לאשר בתנאים מסוימים".
  </li>
  <li>
    <strong>עקביות פנימית — מספר אחד, מקור אחד, לאורך כל המזכר.</strong>
    חוסר עקביות אחת שוחקת את האמינות של המזכר כולו.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח שם-תואר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Adjective Analysis</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שגיאה של שימוש בתארים במקום מספרים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח מעגלי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Circular Reasoning</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נימוק שמנמק את עצמו ללא עובדות חיצוניות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תרחיש שלילי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Bear Case / Downside Scenario</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תרחיש שמציג את ההשפעה בהנחות שמרניות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עקביות פנימית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Internal Consistency</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אחידות מספרים ועובדות בין כל סעיפי המזכר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מבחן העט האדום</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Red Pen Test</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סקירה ביקורתית של מזכר על-ידי קצין אשראי בכיר</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">רשימת בדיקה עצמית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Self-Review Checklist</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">10 נקודות לאימות לפני הגשת מזכר לועדה</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לפרויקט הגמר:</strong><br>
  מזכר האשראי הוא תוצר מרכזי של פרויקט הגמר. השלמתם את קורס 11 —
  כתיבת מזכר אשראי. כעת אתם יודעים לבנות מזכר מלא: מבוא, ניתוח
  שוק, ניתוח לווה, ניתוח פיננסי, ניתוח סיכונים, תנאים, קובננטים
  והמלצה — ולכתוב אותו בצורה מקצועית, מדויקת ואכיפה.<br><br>
  קורס 12 — פרויקט גמר — ייקח אתכם ליישום מלא על נכס אמיתי. הגיעו מוכנים.
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "ניתוח סיכונים ומיתיגציה במזכר",
        "slug": "nitur-sikuim-umitigation-bamezker",
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
        "title_he": "תנאים, קובננטים והמלצה",
        "slug": "tnaim-covenants-vehamlaza",
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
        "title_he": "עקרונות כתיבה מקצועית ושגיאות נפוצות",
        "slug": "ikronot-ktiva-mikzoit-veshgiot",
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
    help = "Seed Course 11, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=11)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 11 not found. Run 'python manage.py seed_data' first."
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
