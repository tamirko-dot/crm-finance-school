"""
Management command: seed_c06_modules456
Seeds Course 6 (מבנה עסקאות מימון), Modules 4, 5, and 6 with full reading,
comprehension, exercises, and summary ModuleComponent records.

Usage:
    python manage.py seed_c06_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — SPV — ישות ייעודית לפרויקט
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  SPV — ישות ייעודית לפרויקט
</h2>

<!-- ===== סעיף 1 — מהו SPV ===== -->
<h3 style="color:#1a2638;">1. מהו SPV? (Special Purpose Vehicle)</h3>

<p>
  <strong>SPV — Special Purpose Vehicle</strong> — הוא חברת בת ייעודית שהוקמה
  למטרה אחת ויחידה: להחזיק בנכס ספציפי או לנהל פרויקט מימוני בודד.
  ה-SPV הוא ישות משפטית נפרדת — בדרך כלל חברה בע&quot;מ — שאינה עוסקת
  בשום פעילות עסקית מעבר לאחזקה וניהול של אותו נכס או פרויקט.
</p>

<p>
  בשוק הנדל&quot;ן הישראלי, כמעט כל עסקת מימון מוסדית מבוצעת דרך SPV.
  הבנק מעמיד הלוואה ל-SPV — לא לקבוצת האם — ורושם שיעבוד ראשון על הנכס
  שבידי ה-SPV.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>למה SPV ולא ישירות לקבוצה?</strong><br>
  כאשר ה-SPV הוא הלווה, הבנק יודע בדיוק מה הוא ממן: נכס אחד, תזרים
  אחד, שיעבוד אחד. אין ערבוב עם פעילויות אחרות של הקבוצה, וקל יותר
  לנטר ולאכוף את תנאי ההלוואה.
</div>

<!-- ===== סעיף 2 — יתרונות ה-SPV ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. יתרונות ה-SPV</h3>

<p>
  שלושה יתרונות מרכזיים מאפיינים את מבנה ה-SPV:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">יתרון</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">משמעות מעשית</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בידוד סיכון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">
        בעיות פיננסיות בפרויקט לא נדבקות לשאר הקבוצה — ולהיפך
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שקיפות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">
        הדוחות הכספיים של ה-SPV משקפים נכס בודד; קל לנתח ולנטר
      </td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קלות מימוש בטחונות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">
        השיעבוד על מניות ה-SPV מאפשר למלווה להשתלט על הנכס ללא הליך
        מסובך של מימוש שיעבוד על נכס ישירות
      </td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 3 — מבנה טיפוסי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. מבנה טיפוסי</h3>

<p>
  מבנה ה-SPV הסטנדרטי בישראל נראה כך:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:1.9;">
  קבוצה (חברת האם)<br>
  &nbsp;&nbsp;↓ (בעלת מניות 100%)<br>
  SPV (חברה בע&quot;מ ייעודית)<br>
  &nbsp;&nbsp;↓ (בעלת הנכס)<br>
  נכס / פרויקט<br>
  &nbsp;&nbsp;↑ (שיעבוד ראשון)<br>
  הלוואת מימון מהבנק
</div>

<p>
  הבנק רושם שני שעבודים עיקריים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>שיעבוד ראשון על הנכס עצמו</strong> — על מנת שיוכל למכור
    את הנכס בהליך מימוש
  </li>
  <li>
    <strong>שיעבוד על מניות ה-SPV</strong> — על מנת שיוכל להשתלט
    על ה-SPV כולו (ועם זה — על הנכס) בלי הליך נפרד
  </li>
</ul>

<!-- ===== סעיף 4 — Bankruptcy Remoteness ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. Bankruptcy Remoteness — עצמאות מפשיטת רגל</h3>

<p>
  <strong>Bankruptcy Remoteness</strong> הוא עיקרון משפטי לפיו ה-SPV
  מחוזק לעמוד בפני הליכי חדלות פירעון של חברת האם.
  אם קבוצת האם נקלעת לקשיים פיננסיים — ה-SPV אמור לא להיסחף
  יחד איתה.
</p>

<p>
  למה זה חשוב למלווה? כי אם ה-SPV "נסחף" לפשיטת רגל של הקבוצה,
  הנכס ייכנס לקופת הנשייה הכוללת — ויהיה קשה הרבה יותר לממשו.
  Bankruptcy Remoteness אמור להבטיח שה-SPV ממשיך לפעול בנפרד.
</p>

<p>
  <strong>דרישות טיפוסיות ל-Bankruptcy Remoteness:</strong>
</p>

<ul style="line-height:1.9;">
  <li>הסכמי שירות ב-Arm's Length (מחירי שוק) בין ה-SPV לקבוצה</li>
  <li>ספרים ורישומים חשבונאיים נפרדים לחלוטין</li>
  <li>חשבון בנק נפרד ל-SPV</li>
  <li>דירקטורים עצמאיים לפחות חלקית</li>
  <li>אין הלוואות בין-חברתיות לא מתועדות</li>
</ul>

<!-- ===== סעיף 5 — Ring-Fencing ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. Ring-Fencing — הגבלת העברות כסף</h3>

<p>
  <strong>Ring-Fencing</strong> הוא מנגנון חוזי המגביל את יכולת ה-SPV
  להעביר כספים לחברת האם או לגופים קשורים אחרים.
  ללא Ring-Fencing, קבוצת האם עלולה "לנקז" מזומנים מה-SPV
  בדרכים שונות — הלוואות בין-חברתיות, דמי ניהול גבוהים, דיבידנדים —
  ולהשאיר את ה-SPV ריק מנכסים.
</p>

<p>
  <strong>מנגנוני Ring-Fencing מקובלים:</strong>
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>Distribution Lock-Up:</strong> חלוקת כספים לחברת האם
    מותרת רק אם DSCR עומד בסף מינימלי לאחר החלוקה
  </li>
  <li>
    <strong>Cash Sweep:</strong> עודף תזרים מעבר לרזרבה נקבעת
    מועבר ישירות לפירעון חוב — לא לקבוצה
  </li>
  <li>
    <strong>Restricted Payments Covenant:</strong> הגבלה חוזית על
    תשלומים לצדדים קשורים מעל סכום מוגדר
  </li>
</ul>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  SPV לא מגן אוטומטית מסיכון קבוצה — בדוק Cross-Default ו-Cross-Collateral
  בין SPVים שונים. אם הסכם ה-SPV כולל <strong>Cross-Default</strong> עם
  חברת האם, הפרה בגוף אחר בקבוצה יכולה "להדביק" את ה-SPV ולהפוך
  את ההלוואה שלך לפרויקט לחוב בכשל — גם אם הנכס עצמו עובד מצוין.
  <strong>Cross-Collateral</strong> עלול להפוך את נכס ה-SPV לבטוחה
  עבור חובות של גופים אחרים בקבוצה. קרא כל מסמך בטחון — לא רק את הסיכום.
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מבנה SPV, יתרונותיו, עיקרון Bankruptcy Remoteness, "
    "מנגנוני Ring-Fencing וסיכוני Cross-Default ו-Cross-Collateral. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים זיהוי מבנה SPV מתרשים נתון, "
    "הערכת עמידה בדרישות Bankruptcy Remoteness לפי מאפייני עסקה, "
    "וזיהוי מנגנון Ring-Fencing הנכון לתרחיש נתון. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — SPV — ישות ייעודית לפרויקט
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>SPV הוא חברה בת ייעודית לנכס/פרויקט בודד.</strong>
    כמעט כל עסקת מימון נדל&quot;ן מוסדית בישראל מבוצעת דרכו.
  </li>
  <li>
    <strong>שלושת היתרונות: בידוד סיכון, שקיפות, קלות מימוש בטחונות.</strong>
    הבנק מממן נכס בודד עם תזרים ברור — לא פעילות קבוצתית מעורבת.
  </li>
  <li>
    <strong>Bankruptcy Remoteness מבטיח ש-SPV לא נסחף בכשל קבוצת האם.</strong>
    הוא מחייב ספרים נפרדים, חשבון בנק עצמאי ומחירי Arm's Length.
  </li>
  <li>
    <strong>Ring-Fencing מונע ניקוז מזומנים מה-SPV לקבוצה.</strong>
    כלים: Distribution Lock-Up, Cash Sweep, Restricted Payments Covenant.
  </li>
  <li>
    <strong>Cross-Default ו-Cross-Collateral שוברים את ההגנה של ה-SPV.</strong>
    קרא את כל מסמכי הבטחון לפני מסקנה שה-SPV מבודד.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ישות ייעודית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">SPV — Special Purpose Vehicle</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חברה בת לנכס/פרויקט בודד</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עצמאות מפשיטת רגל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Bankruptcy Remoteness</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בידוד ה-SPV מהליכי חדלות של הקבוצה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גידור מזומנים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Ring-Fencing</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הגבלת העברת כסף מה-SPV לקבוצה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">כשל צולב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cross-Default</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כשל בגוף אחד מפעיל כשל בגוף אחר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בטחון צולב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cross-Collateral</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נכס ה-SPV כבטוחה לחובות גופים אחרים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נעילת חלוקה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Distribution Lock-Up</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חלוקה מותרת רק אם DSCR עומד בסף</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — Term Sheet — קריאה ואימות
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  Term Sheet — קריאה ואימות
</h2>

<!-- ===== סעיף 1 — מה זה Term Sheet ===== -->
<h3 style="color:#1a2638;">1. מה זה Term Sheet?</h3>

<p>
  <strong>Term Sheet</strong> הוא מסמך כוונות שאינו מחייב משפטית,
  המסכם את עיקרי תנאי העסקה שעליהם הסכימו הצדדים לפני עריכת
  הסכם ההלוואה הסופי והמלא.
  הוא משמש כ"מפת דרכים" לצוות המשפטי שיגבש את ההסכם הסופי,
  ולצוות האשראי שיבצע את ה-Due Diligence.
</p>

<p>
  Term Sheet אינו חוזה — אך הוא קובע ציפיות עסקיות חזקות.
  חזרה ממנו ללא סיבה טובה פוגעת באמינות ובמוניטין של הצד שחוזר.
  בפרקטיקה הישראלית, Term Sheet חתום מנהל משא ומתן ממוקד יותר
  ועלות שינויים גדלה ככל שמתקדמים בתהליך.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מי מוציא Term Sheet?</strong><br>
  בדרך כלל — המלווה. הוא מסמל שהבנק עבר בדיקת היתכנות ראשונית
  ומוכן להתקדם לשלב ה-DD המלא. קבלת Term Sheet היא אות חיובי — אך
  לא כניסה לתוקף של ההלוואה.
</div>

<!-- ===== סעיף 2 — סעיפים קריטיים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. סעיפים קריטיים ב-Term Sheet</h3>

<p>
  כל Term Sheet בנדל&quot;ן ישראלי אמור לכלול את הסעיפים הבאים:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סעיף</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תיאור</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דגל אדום אפשרי</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סכום ההלוואה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הסכום המרבי שהמלווה מוכן לספק</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פער ממה שהלווה מבקש</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ריבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שיעור, סוג (קבועה/משתנה), בסיס חישוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מרווח גבוה, PIK מובנה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">LTV</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">יחס ההלוואה לשווי הנכס המאושר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">LTV גבוה מ-70% לנכסים מסחריים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">DSCR Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הסף המינימלי המחייב לכל תקופת ההלוואה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סף נמוך מ-1.20</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בטחונות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סוגי השיעבודים, ערבויות, בטחונות נוספים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ערבות אישית לא הוגנת, Cross-Collateral</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עמלות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Arrangement Fee, Commitment Fee, Prepayment</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עמלה מקדימה גבוהה (מעל 1%)</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 3 — ריבית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. ריבית — קבועה, פריים ו-PIK</h3>

<p>
  שלושת סוגי הריבית הנפוצים בשוק הישראלי:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>ריבית קבועה:</strong> שיעור אחיד לכל תקופת ההלוואה.
    נותנת ללווה ודאות בתכנון תזרים, אך בדרך כלל גבוהה יותר מהריבית
    המשתנה ביום הלקיחה. מקובלת בנכסים מניבים ארוכי טווח.
  </li>
  <li>
    <strong>ריבית פריים + מרווח (Spread):</strong> הריבית משתנה עם
    שינויי פריים בנק ישראל. הלווה נהנה בירידות ריבית, אך חשוף לעלייה.
    דוגמה: פריים + 1.5% — אם פריים עולה ב-0.5%, גם עלות ההלוואה עולה.
  </li>
  <li>
    <strong>PIK — Payment-In-Kind:</strong> הריבית אינה משולמת במזומן
    אלא נצברת לקרן. הקרן גדלה בכל תקופה. פוגש בהלוואות גישור ובמימון
    Junior/Mezzanine. <em>מסוכן ללווה</em> — החוב צומח גם אם הפרויקט
    לא מניב הכנסות.
  </li>
</ul>

<p>
  <strong>ריבית עונשית (Default Interest):</strong> שיעור ריבית גבוה יותר
  הנכנס לתוקף עם כשל. בדרך כלל פריים + 5%–8%, או שיעור קבוע גבוה.
  סעיף זה חייב להיות ב-Term Sheet — אנליסט שלא קרא אותו לא הבין
  את עלות הכשל.
</p>

<!-- ===== סעיף 4 — עמלות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. עמלות — Arrangement, Commitment ו-Prepayment</h3>

<ul style="line-height:1.9;">
  <li>
    <strong>Arrangement Fee (עמלת הסדר):</strong> תשלום חד-פעמי
    בסגירת העסקה, בדרך כלל 0.5%–1.5% מסכום ההלוואה. מתמחרת את
    עבודת המלווה בבדיקה, ניסוח ואישור.
  </li>
  <li>
    <strong>Commitment Fee (עמלת התחייבות):</strong> עמלה שנתית
    (לרוב 0.3%–0.75%) על החלק שלא נמשך מהמסגרת. הלווה משלם גם אם
    לא משך את כל הסכום שהובטח לו. רלוונטי במיוחד בהלוואות ליווי שחלות
    במשך שנים ולא נמשכות בבת אחת.
  </li>
  <li>
    <strong>Prepayment Penalty (קנס פירעון מוקדם):</strong> תשלום
    שהלווה משלם אם פרע את ההלוואה לפני המועד. מגן על המלווה מאיבוד
    הכנסות ריבית צפויות. בד&quot;כ 1%–3% מהסכום הנפרע המוקדם, או
    Make-Whole Formula מורכבת יותר.
  </li>
</ul>

<!-- ===== סעיף 5 — Events of Default ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. Events of Default — אירועי חדלון</h3>

<p>
  ה-Term Sheet מציין בדרך כלל את קטגוריות אירועי הכשל. ה-Events of Default
  הטיפוסיים בהלוואות נדל&quot;ן ישראליות:
</p>

<ul style="line-height:1.9;">
  <li>אי-פירעון קרן או ריבית במועד</li>
  <li>הפרת Covenant פיננסי (DSCR, LTV, ICR)</li>
  <li>הפרת Covenant לא-פיננסי (הגשת דוחות, ביטוח, אחזקת נכס)</li>
  <li>חדלות פירעון של ה-SPV או חברת האם</li>
  <li>שינוי שליטה ב-SPV ללא הסכמת המלווה</li>
  <li>Cross-Default — כשל בהלוואה אחרת מעל סכום הסף</li>
  <li>פסק דין שלילי מעל סכום מהותי שלא בוצע בו ערעור</li>
  <li>מכירת/העברת הנכס ללא הסכמה</li>
</ul>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  Term Sheet לא מחייב משפטית — אך ברגע שסגרת את ה-Fee Structure,
  קשה לשנות. נהל משא ומתן על Term Sheet ברצינות מלאה. כל סעיף שלא
  תנהל משא ומתן עליו עכשיו — ייהפך ל"מוסכם" בהסכם הסופי. שים לב
  במיוחד לעמלת ה-Arrangement — היא משולמת גם אם העסקה נכשלת
  לאחר ה-DD, במקרים רבים.
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מבנה Term Sheet, סעיפיו הקריטיים, "
    "סוגי הריבית (קבועה, פריים, PIK), מבנה העמלות ו-Events of Default. "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים חישוב עלות אפקטיבית של הלוואה "
    "כולל Arrangement Fee ו-Commitment Fee, השוואת ריבית קבועה לפריים + מרווח "
    "בתרחישי ריבית שונים, וזיהוי Events of Default בתרחיש נתון. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — Term Sheet — קריאה ואימות
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>Term Sheet הוא מסמך כוונות לא מחייב — אך קובע ציפיות עסקיות חזקות.</strong>
    ניהול משא ומתן עליו ברצינות הוא חובה מקצועית.
  </li>
  <li>
    <strong>שישה הסעיפים הקריטיים: סכום, ריבית, LTV, DSCR Covenant, בטחונות, עמלות.</strong>
    כולם חייבים להיות ברורים לפני חתימה על Term Sheet.
  </li>
  <li>
    <strong>שלושה סוגי ריבית: קבועה, פריים + מרווח, PIK.</strong>
    PIK גורם לצמיחת הקרן — מסוכן בפרויקטים ללא תזרים שוטף.
  </li>
  <li>
    <strong>שלוש עמלות עיקריות: Arrangement, Commitment, Prepayment Penalty.</strong>
    הן חלק מעלות ההלוואה האפקטיבית ויש לחשב אותן לצד הריבית.
  </li>
  <li>
    <strong>Events of Default כוללים גם הפרות Covenant ו-Cross-Default — לא רק אי-פירעון.</strong>
    קרא את הרשימה במלואה — כל סעיף הוא אירוע שיכול להפוך הלוואה לבעיה.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מסמך כוונות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Term Sheet</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עיקרי תנאי עסקה — לא מחייב משפטית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ריבית בעין</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">PIK — Payment-In-Kind</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ריבית שנצברת לקרן במקום לשולם במזומן</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עמלת הסדר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Arrangement Fee</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשלום חד-פעמי בסגירת העסקה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עמלת התחייבות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Commitment Fee</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עמלה שנתית על חלק שלא נמשך מהמסגרת</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קנס פירעון מוקדם</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Prepayment Penalty</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשלום על פירעון לפני המועד</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אירועי חדלון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Events of Default</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רשימת אירועים המפעילים זכות אכיפה</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — Due Diligence וסגירת עסקה
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  Due Diligence וסגירת עסקה
</h2>

<!-- ===== סעיף 1 — DD פיננסי ===== -->
<h3 style="color:#1a2638;">1. DD פיננסי — בדיקת הנתונים הכספיים</h3>

<p>
  <strong>Due Diligence פיננסי (DD פיננסי)</strong> הוא הבדיקה המעמיקה
  של הנתונים הכספיים של הלווה, הנכס, והפרויקט.
  מטרתו לאמת שהמספרים ב-Term Sheet והמצגת של הלווה
  מייצגים את המציאות — ולא מספרים מנופחים.
</p>

<p>
  <strong>רכיבי ה-DD הפיננסי המרכזיים:</strong>
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>בדיקת דוחות כספיים:</strong> 3 שנים אחרונות מבוקרים,
    ניתוח מגמות, שינויים חשבונאיים, הערות רואה החשבון
  </li>
  <li>
    <strong>תזרים מזומנים היסטורי:</strong> אימות NOI בפועל לעומת
    הצהרת הלווה; זיהוי תשלומים חד-פעמיים שנכללו שלא כדין ב-NOI הרגיל
  </li>
  <li>
    <strong>LTV אמיתי:</strong> השוואת הערכת שמאי עצמאית לשווי שהלווה
    מצהיר; בדיקת נכסים אחרים ששועבדו כבר
  </li>
  <li>
    <strong>הסכמי שכירות:</strong> קריאת כל חוזי השכירות; בדיקת אורך
    חוזה, אפשרויות יציאה מוקדמת של שוכר (Break Clauses), הצמדות
  </li>
  <li>
    <strong>חובות קיימים:</strong> מפת חובות מלאה של ה-SPV וחברת האם;
    זיהוי כל השיעבודים הקיימים
  </li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דגל אדום — NOI מנופח:</strong><br>
  NOI שמוצג ב-Term Sheet גבוה ב-15% מה-NOI ב-3 שנים האחרונות?
  שאל: האם יש שוכר אנקר חדש שנכנס ממש לפני ה-DD? האם הוצאות תחזוקה
  חד-פעמיות הוצאו מה-NOI "כי הן לא ייחזרו"? אלה שאלות שכיחות.
</div>

<!-- ===== סעיף 2 — DD משפטי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. DD משפטי — בדיקת הזכויות והחבויות</h3>

<p>
  ה-DD המשפטי בוחן את הזכויות המשפטיות בנכס ואת כל ההתחייבויות הנסתרות.
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>בעלות ורישום:</strong> חיפוש בטאבו או ברשות מקרקעי ישראל;
    אימות שה-SPV הוא בעל הנכס / חוכר ללא עיכובים משפטיים
  </li>
  <li>
    <strong>שיעבודים קיימים:</strong> כל שיעבוד רשום — מה דרגתו?
    האם יש שיעבוד ראשון שקדם להלוואה הנדונה?
  </li>
  <li>
    <strong>חוזים מהותיים:</strong> חוזי שכירות, ניהול, בנייה,
    אחזקה — יש להבין מה ניתן לביטול ומה מחייב
  </li>
  <li>
    <strong>ליטיגציה:</strong> בדיקת הליכים משפטיים תלויים ועומדים
    נגד ה-SPV ונגד בעלי המניות המרכזיים
  </li>
  <li>
    <strong>היתרים ורישיונות:</strong> אימות קיום היתר בנייה, רישיון
    עסק, תעודת גמר — כל מה שדרוש לפעילות הנכס
  </li>
</ul>

<!-- ===== סעיף 3 — DD טכני ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. DD טכני — מצב פיזי של הנכס</h3>

<p>
  ה-DD הטכני מאמת את מצב הנכס הפיזי ואת שווייו הריאלי:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>הערכת שמאי:</strong> שמאי מוסמך עצמאי (שאינו של הלווה)
    מבצע הערכת שווי לפי שיטות: Cap Rate, DCF, השוואת עסקאות.
    הבנק מסתמך על הערכת שמאי זו — לא על הצהרת הלווה.
  </li>
  <li>
    <strong>בדיקת מהנדס (Building Survey):</strong> מהנדס בניין בוחן
    מצב מבני, מערכות, גיל הנכס, עלויות תחזוקה צפויות ותיקונים נדרשים
  </li>
  <li>
    <strong>סקר סביבתי (Environmental Survey):</strong> בדיקת קרקע
    וקרבה למקורות זיהום. חיוני במיוחד בנכסים תעשייתיים ולוגיסטיים.
    אם יש זיהום — ערך הנכס ו/או עלויות הפינוי עלולים להשפיע דרמטית על LTV.
  </li>
</ul>

<!-- ===== סעיף 4 — Conditions Precedent ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. Conditions Precedent (CPs) — תנאים לשחרור ראשון</h3>

<p>
  <strong>Conditions Precedent (CPs)</strong> — בעברית: "תנאים מתלים" —
  הם רשימת דרישות שעל הלווה לעמוד בהן <em>לפני</em> ש-המלווה
  ישחרר את ה-Drawdown הראשון של ההלוואה.
</p>

<p>
  <strong>CPs טיפוסיים:</strong>
</p>

<ul style="line-height:1.9;">
  <li>חתימה על כל מסמכי ההלוואה ורישום כל השיעבודים</li>
  <li>קבלת הערכת שמאי מאושרת על-ידי המלווה</li>
  <li>הגשת ביטוחים בסכומים ולטובת המלווה כמוטב</li>
  <li>פתיחת חשבון ה-SPV בבנק המלווה</li>
  <li>קבלת אישור משפטי (Legal Opinion) מעורך דין מוסכם</li>
  <li>הוכחת הון עצמי מושקע (כלומר — שהלווה הביא את חלקו)</li>
  <li>עמידה ב-DSCR Covenant בזמן הסגירה</li>
</ul>

<p>
  CPs לא מסופקים = הלוואה לא יוצאת לפועל. כל CP שנותר פתוח הוא
  מנגנון שמגן על המלווה.
</p>

<!-- ===== סעיף 5 — Financial Close ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. Financial Close וה-Drawdown הראשון</h3>

<p>
  <strong>Financial Close</strong> — "סגירה פיננסית" — הוא הרגע שבו:
</p>

<ol style="line-height:1.9;">
  <li>כל מסמכי ההלוואה חתומים</li>
  <li>כל ה-CPs מסופקים ומאומתים</li>
  <li>כל השיעבודים רשומים</li>
  <li>המלווה מכריז שהוא מוכן לשחרר כסף</li>
</ol>

<p>
  לאחר ה-Financial Close — ה-Drawdown הראשון הוא שחרור הסכום הראשון
  מהמסגרת. בהלוואות ליווי, ה-Drawdowns מתבצעים לפי אבני דרך ניהוליות
  ו/או לפי אישורי פיקוח בנייה. בנכסים מניבים — לרוב סכום אחד מלא.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:1.9;">
  ציר הזמן של סגירת עסקה:<br><br>
  Term Sheet חתום → DD מלא (4-8 שבועות) → הסכם הלוואה → CPs → Financial Close → Drawdown ראשון
</div>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  Due Diligence שנחתך בלוח זמנים הוא DD חלקי. לחץ זמן מלווה הוא גורם
  סיכון — לא סיבה לדלג. כאשר הלווה מציב לחץ זמן ("חייבים לסגור עד סוף
  הרבעון"), זה לא סיבה לקצר את ה-DD — זה <em>סיבה לחשוד</em> שמנסים
  למנוע ממך לגלות משהו. DD מקיף לוקח את הזמן שהוא לוקח. וועדת האשראי
  צריכה לדעת אם ה-DD בוצע בלחץ זמן — זה מידע רלוונטי לאישור.
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של שלושת סוגי ה-DD (פיננסי, משפטי, טכני), "
    "Conditions Precedent, Financial Close וסדר הפעולות לסגירת עסקה. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים זיהוי דגלים אדומים ב-DD פיננסי מנתונים נתונים, "
    "בדיקת רשימת CPs ואיתור CP חסר, וקביעת סדר הפעולות הנכון לסגירת עסקה. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — Due Diligence וסגירת עסקה
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>DD כולל שלושה ממדים: פיננסי, משפטי, טכני.</strong>
    כל ממד בלתי-תלוי — קיצור של אחד מהם לא מתוגמל בשני האחרים.
  </li>
  <li>
    <strong>DD פיננסי מאמת NOI, LTV, תזרים ומבנה חוב — לא מקבל אותם כמובן מאליו.</strong>
    NOI היסטורי הוא בסיס; NOI מוצהר הוא טענה שדורשת הוכחה.
  </li>
  <li>
    <strong>DD משפטי בוחן בעלות, שיעבודים, חוזים וליטיגציה.</strong>
    שיעבוד קיים שלא אותר הוא טיקטיק ידוע — חיפוש טאבו מלא הוא חובה.
  </li>
  <li>
    <strong>CPs הם מנגנון הגנה על המלווה — כל CP שנשאר פתוח הוא סיכון פתוח.</strong>
    Financial Close לא מתבצע עד שכל ה-CPs סגורים.
  </li>
  <li>
    <strong>לחץ זמן ב-DD הוא דגל אדום — לא צידוק לקיצור.</strong>
    וועדת האשראי חייבת לדעת אם ה-DD בוצע בלחץ זמן.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בדיקת נאותות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Due Diligence</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדיקה מעמיקה לפני סגירת עסקה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תנאים מתלים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Conditions Precedent (CPs)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דרישות לפני שחרור ה-Drawdown הראשון</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סגירה פיננסית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Financial Close</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הרגע שבו כל CPs סגורים וניתן לשחרר כסף</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">משיכה ראשונה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">First Drawdown</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שחרור הסכום הראשון מהמסגרת</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חוות דעת משפטית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Legal Opinion</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אישור עורך דין על תקינות ה-CP המשפטיים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סקר סביבתי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Environmental Survey</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדיקת זיהום קרקע וסביבה</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לבחינה הסופית:</strong><br>
  השלמתם את שישת מודולי קורס 6 — מבנה עסקאות מימון. למדתם את
  ארכיטקטורת ה-Senior/Junior, מימון ביניים, מבנה SPV ו-Bankruptcy
  Remoteness, קריאה וניהול משא ומתן על Term Sheet, וביצוע Due Diligence
  מלא עד Financial Close.<br><br>
  הבחינה הסופית תכלול שאלות על מבנה SPV ו-Ring-Fencing, זיהוי
  סעיפים קריטיים ב-Term Sheet, וזיהוי דגלים אדומים בתהליך ה-DD.
  הגיעו מוכנים — ובהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "SPV — ישות ייעודית לפרויקט",
        "slug": "spv-yishut-yiudit",
        "estimated_minutes": 45,
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
        "title_he": "Term Sheet — קריאה ואימות",
        "slug": "term-sheet-kriya",
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
        "title_he": "Due Diligence וסגירת עסקה",
        "slug": "due-diligence-sgira",
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
    help = "Seed Course 6, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=6)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 6 not found. Run 'python manage.py seed_data' first."
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
