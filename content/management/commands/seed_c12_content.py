"""
Seeds Module 1-3 content for Course 12 (פרויקט גמר — מימון נדל"ן).
Usage: python manage.py seed_c12_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": 'מבוא לפרויקט הגמר — מה נדרש ממך',
        "slug": "mavo-leproekt-hagemar",
        "estimated_minutes": 45,
    },
    {
        "module_number": 2,
        "title_he": "בחירת נכס וליקוט נתונים",
        "slug": "bkhirat-nkhas-velikut-ntunim",
        "estimated_minutes": 50,
    },
    {
        "module_number": 3,
        "title_he": "ביצוע Due Diligence ואיסוף מסמכים",
        "slug": "bitsu-due-diligence-veisuf-mismakhim",
        "estimated_minutes": 55,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (מבוא לפרויקט הגמר — מה נדרש ממך)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>מבוא לפרויקט הגמר — מה נדרש ממך</h2>

<p>
פרויקט הגמר הוא שיאו של תהליך הלמידה בקורס ניתוח אשראי נדל"ן. בניגוד לבחינות מודול
הבוחנות ידע ספציפי, פרויקט הגמר דורש ממך לשלב את כל הכלים שרכשת — ניתוח שוק, הערכת
שווי, מדדים פיננסיים, תזרים מזומנים, מבנה עסקה, ניהול סיכונים וניתוח מסמכים — לכדי
<strong>מזכר אשראי (Credit Memo) מקצועי ומלא</strong> על עסקת נדל"ן ישראלית אמיתית
או ריאלית.
</p>

<p>
זוהי הפעם הראשונה שאתה ניצב מול דף ריק ומבנה עסקה לא מוכתבים. ועדת האשראי תקבל
את מזכרך ותחליט — על בסיס ניתוחך בלבד — אם לאשר את ההלוואה, לסרב, או לאשר בתנאים.
</p>

<h2>חמישה מסמכי הפלט הנדרשים</h2>

<p>
מזכר הגמר חייב לכלול את חמשת הפרקים הבאים — כל אחד הכרחי, ואי-הגשת אחד מהם גורר
פסילה אוטומטית:
</p>

<ol>
  <li>
    <strong>תקציר מנהלים (Executive Summary):</strong> פסקה של 10–15 שורות המסכמת את
    העסקה, ההמלצה ועיקרי הממצאים. הוועדה קוראת זאת ראשון — הוא חייב להיות ברור, מדויק
    ומבוסס מספרים. אם התקציר מעורפל, שאר המזכר יבחן בעין ביקורתית.
  </li>
  <li>
    <strong>ניתוח הלווה והנכס:</strong> פרופיל הלווה (ניסיון, מינוף, נכסים אחרים, מוניטין
    אשראי), תיאור הנכס (סוג, מיקום, גיל, שטח, תפוסה, שוכרים), ניתוח שוק המשנה (סאב-מרקט
    — שיעורי ריקנות, עסקאות השוואה, מגמות שכ"ד). פרק זה מבסס את הרקע — ללא פרק זה, אין
    בסיס לניתוח הפיננסי.
  </li>
  <li>
    <strong>המודל הפיננסי המלא (DCF + DSCR + LTV):</strong> זה לב המזכר. חייב לכלול:
    תחזית NOI ל-5 שנים לפחות (כולל הנחות שכ"ד, תפוסה ועלויות תפעול); DCF לתמחור שווי
    הנכס (שיעור היוון, שיעור הצמיחה, שווי שיורי); DSCR לכל שנה; LTV ביום ההלוואה
    ותרחיש יציאה; Stress Test (+200bps בריבית, -10% בתפוסה).
  </li>
  <li>
    <strong>ניתוח סיכונים עם מיתיגציה:</strong> מטריצת סיכונים (הסתברות × השפעה) לפחות
    5 סיכונים זוהו, דורגו ותועדו. לכל סיכון מהותי (ציון 8+) — הגדר מנגנון מיתיגציה ספציפי
    (Covenant, בטחון, ביטוח, תנאי מקדים).
  </li>
  <li>
    <strong>המלצה עם תנאים ותנאי מקדים:</strong> המלצה מפורשת — אישור, סירוב, או אישור
    מותנה. אם אישור: כלול Proposed Term Sheet מלא (קרן, ריבית, תקופה, LTV מקסימלי,
    DSCR מינימלי, Covenants, בטחונות, תנאי מקדים). אם סירוב: נמק במדויק ועם מספרים.
  </li>
</ol>

<h2>קריטריוני הערכה</h2>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">קריטריון</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">משקל</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מה נבדק</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">דיוק הניתוח הכמותי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">30%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חישובי DCF, DSCR, LTV — אריתמטיקה ולוגיקה נכונות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">איכות הכתיבה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">20%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בהירות, מבנה לוגי, שפה מקצועית, ניסוחים מדויקים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שלמות רשימת ה-DD</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">20%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כיסוי כל 6 מסמכי ה-DD הסטנדרטיים ותיעוד פערים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח תרחישים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">15%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Stress Tests מוגדרים היטב, מסקנות ברורות לכל תרחיש</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">איכות ההמלצה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">15%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">המלצה ברורה, מנומקת, עם Term Sheet מלא וסיבות לסירוב/אישור</td>
    </tr>
  </tbody>
</table>

<h2>לוח זמנים מוצע</h2>

<p>
הקורס מחולק לשישה מודולים. הנה תוכנית עבודה מוצעת לחלוקת זמן:
</p>

<ul>
  <li><strong>מודול 1–2 (שבועות 1–2):</strong> בחירת הנכס, ליקוט נתונים ראשוני, הכנת תיק מידע.</li>
  <li><strong>מודול 3 (שבוע 3):</strong> ביצוע Due Diligence ואיסוף מסמכים, תיעוד פערים.</li>
  <li><strong>מודול 4 (שבועות 4–5):</strong> בניית המודל הפיננסי — DCF, DSCR, LTV, Stress Tests.</li>
  <li><strong>מודול 5 (שבוע 6):</strong> כתיבת פרק הסיכונים, מטריצה, מיתיגציות.</li>
  <li><strong>מודול 6 (שבוע 7):</strong> כתיבת ההמלצה, Term Sheet, עריכה סופית והגשה.</li>
</ul>

<h2>מה מבחין בין מזכר עובר למזכר נכשל</h2>

<p>
אנליסטים רבים מגישים מזכרים שנראים מקצועיים — אך נכשלים. הנה ההבדל המהותי:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מזכר עובר</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מזכר נכשל</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כל טענה מגובה במספר ומקור</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">טענות כלליות ("הנכס במיקום טוב")</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">DSCR, LTV ו-DCF מחושבים ומוסברים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מספרים ללא הסבר הנחות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Stress Test עם מסקנות ברורות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חישוב בסיס בלבד, ללא Stress</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פערי DD מוכרים ומתועדים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פערים מוסתרים או מתעלמים מהם</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">המלצה ברורה עם Term Sheet</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">המלצה מעורפלת ("כנראה כדאי לאשר")</td>
    </tr>
  </tbody>
</table>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>נקודת מפתח:</strong><br>
  הפרויקט הוא הזדמנות להפגין את כל מה שלמדת — כל קורס הוא כלי שתצטרך כאן. DCF מקורס 3,
  DSCR מקורס 4, תזרים מקורס 5, מבנה עסקה מקורס 6, סיכונים מקורס 7, מסמכים מקורס 8 —
  כולם מתכנסים כאן למזכר אחד, מלא ומקצועי.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — כלל הזהב:</strong><br>
  מזכר גמר שמכיל "הלווה חזק" ללא נתונים — נכשל. כל טענה חייבת מספר. "הנכס ממוקם
  היטב" ללא נתוני שוק — לא מתקבל. "הסיכון נמוך" ללא ניתוח — לא מתקבל.
  <strong>כל טענה חייבת מספר, מקור, או חישוב שמגבה אותה.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Comprehension HTML
# ---------------------------------------------------------------------------

M1_COMPREHENSION_HTML = """
<p>ענה על שאלות ההבנה הבאות.</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Exercises HTML
# ---------------------------------------------------------------------------

M1_EXERCISES_HTML = """
<p>פתור את התרגילים הבאים.</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — מבוא לפרויקט הגמר</h2>

<h3>נקודות מפתח</h3>
<ol>
  <li>
    <strong>פרויקט הגמר הוא מזכר אשראי מלא:</strong> לא סיכום תיאורטי — אלא ניתוח
    פיננסי עמוק על עסקה ספציפית, הכולל את כל הכלים שנרכשו לאורך 11 קורסים.
  </li>
  <li>
    <strong>חמישה פרקי חובה:</strong> תקציר מנהלים, ניתוח לווה ונכס, מודל פיננסי מלא,
    ניתוח סיכונים, והמלצה עם Term Sheet. כל פרק חסר — פסילה.
  </li>
  <li>
    <strong>קריטריוני הערכה ידועים מראש:</strong> דיוק כמותי (30%), איכות כתיבה (20%),
    שלמות DD (20%), ניתוח תרחישים (15%), איכות המלצה (15%). התכוון לכולם.
  </li>
  <li>
    <strong>לוח זמנים מובנה:</strong> 6 מודולים, 7 שבועות. מודול 1–2 לנתונים, מודול 3
    ל-DD, מודול 4 למודל, מודול 5 לסיכונים, מודול 6 להמלצה ועריכה.
  </li>
  <li>
    <strong>כלל הזהב:</strong> כל טענה — מספר. כל הנחה — מקור. כל סיכון — מיתיגציה.
    מזכר ללא נתונים הוא מזכר שנכשל, גם אם הוא ארוך ומנוסח יפה.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
הבנת מה נדרש ממך — עכשיו מגיע הצעד הראשון המעשי: <em>מודול 2</em> ילמד אותך
<strong>כיצד לבחור נכס מתאים לפרויקט וכיצד לבנות את תיק הנתונים המלא</strong>
שעליו יתבסס כל הניתוח הבא.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (בחירת נכס וליקוט נתונים)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>בחירת נכס וליקוט נתונים — הבסיס לכל הניתוח</h2>

<p>
מזכר אשראי טוב מתחיל בבחירת נכס נכונה. לא כל נכס מתאים לפרויקט הגמר — יש צורך
בנכס שעליו קיים מספיק מידע ציבורי ומסחרי לביצוע ניתוח מלא. בחירה בנכס עם נתונים
חסרים תחבל בפרויקט כולו, ללא קשר לאיכות הכתיבה.
</p>

<h2>סוגי עסקאות המתאימות לפרויקט הגמר</h2>

<p>
הפרויקט מיועד לנכסים <strong>מניבים</strong> — כלומר נכסים שמייצרים הכנסה שוטפת
משכר דירה. הנכס חייב להיות ברמת השלמה סבירה ועם פעילות שוכרים בפועל:
</p>

<ul>
  <li><strong>נכסי משרדים:</strong> בניין משרדים, קומה משרדית, מתחם טכנולוגיה — מתאים מאוד. שוק
  המשרדים בישראל (תל אביב, ר"ג, הרצליה) עשיר בנתונים ציבוריים.</li>
  <li><strong>נכסי מסחר (Retail):</strong> מרכז מסחרי, סטריפ-מול, חנויות רחוב — מתאים. שים לב
  לסיכון ריכוז שוכרים ולמגמת ה-E-commerce.</li>
  <li><strong>נכסי לוגיסטיקה ותעשייה:</strong> מחסן, מרכז הפצה, פארק תעשייתי — מתאים. ביקוש
  גבוה ב-2022–2025 בישראל, נתונים זמינים.</li>
  <li><strong>נכסי מגורים מניבים:</strong> בניין להשכרה (BTR — Build to Rent), מתחם דיור מוסדי
  — מתאים, אם יש נתונים על תפוסה ושכ"ד.</li>
</ul>

<p><strong>לא מתאים לפרויקט:</strong></p>
<ul>
  <li>קרקע חקלאית או מגרש פנוי (אין הכנסה שוטפת לניתוח DSCR)</li>
  <li>פרויקט ייזום שטרם הושלם (אין NOI היסטורי לנרמול)</li>
  <li>נכס עם ליטיגציה פעילה (נתוני בסיס לא אמינים)</li>
</ul>

<h2>מקורות מידע לעסקה ישראלית</h2>

<p>
הנה רשימת מקורות המידע הרלוונטיים לפרויקט גמר על נכס ישראלי:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מקור</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מה ניתן לקבל</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">שימוש במזכר</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רשות מקרקעי ישראל (רמ"י)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עסקאות קרקע, זכויות חכירה, הסכמי פיתוח</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח עסקאות השוואה, בדיקת זכויות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">טאבו (רישום מקרקעין)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נסח טאבו, שיעבודים, הערות אזהרה, בעלות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בדיקת בעלות ונקיון שיעבודים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אתרי עיריות ורשויות מקומיות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תב"ע, היתרי בנייה, ייעוד קרקע, ארנונה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח רגולטורי, אימות ייעוד</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מדלן, יד2 מסחרי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עסקאות מכר, שכ"ד שוק, הצעות פעילות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח Comparable Transactions, Market Rent</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">דוחות שנתיים של REITים ציבוריים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעורי תפוסה, NOI לנכסים דומים, שכ"ד ממוצע</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Benchmarking, נתוני שוק המשנה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שמאויות מפורסמות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעור היוון, שווי שוק, עסקאות השוואה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Cap Rate לניתוח DCF, Comparable Sales</td>
    </tr>
  </tbody>
</table>

<h2>בניית תיק הנתונים</h2>

<p>
לאחר בחירת הנכס, בנה "תיק נתונים" מסודר שיהיה הבסיס לכל פרקי המזכר. תיק הנתונים
חייב לכלול:
</p>

<ul>
  <li><strong>תיעוד פיזי:</strong> תמונות, מפות, תוכנית קומות, מספר קומות ושטח כולל.</li>
  <li><strong>ניתוח אזורי:</strong> מיקום מדויק, ניגישות תחבורתית, תיאור סביבת הנכס (מתחרים, שירותים).</li>
  <li><strong>רשימת שוכרים:</strong> שם, שטח, שכ"ד, תאריך תחילת חוזה, תאריך פקיעה, אופציות חידוש.</li>
  <li><strong>סיכומי חוזי שכירות:</strong> תנאי עיקריים — עדכון שכ"ד, אחריות תחזוקה, תנאי יציאה.</li>
  <li><strong>דוחות כספיים היסטוריים:</strong> NOI ל-3 שנים אחרונות לפחות (הכנסות, הוצאות, NOI נטו).</li>
  <li><strong>עסקאות השוואה:</strong> לפחות 3 עסקאות מכר של נכסים דומים ב-12 חודשים האחרונים.</li>
</ul>

<h2>ניתוח שוק המשנה (Sub-Market Analysis)</h2>

<p>
חלק קריטי של פרק ניתוח הנכס הוא ניתוח שוק המשנה — לא "השוק בכלל" אלא
<strong>הסאב-מרקט הספציפי</strong> שבו הנכס ממוקם:
</p>

<ul>
  <li>שיעורי ריקנות בסאב-מרקט (השנה ובשנים האחרונות — מגמה עולה? יורדת?)</li>
  <li>מגמות שכ"ד (עלה? ירד? יציב?) — נתונים ממדלן/דוחות REITs</li>
  <li>עסקאות מכר דומות (Comparable Sales) — Cap Rate שהתממש בפועל</li>
  <li>צינור אספקה חדש (New Supply Pipeline) — האם הולך להיבנות היצע משמעותי?</li>
</ul>

<h2>דגלים אדומים — נכסים שיש להימנע מהם</h2>

<p>
בחירה בנכס בעייתי תכשיל את הפרויקט בשלב מוקדם. הנה מה לחפש ולהימנע:
</p>

<ul>
  <li><strong>אין נתונים זמינים:</strong> נכס ללא שמאות, ללא היסטוריה כספית, ללא נסח טאבו — לא ניתן
  לבצע ניתוח אמין.</li>
  <li><strong>ליטיגציה פעילה:</strong> תביעות שוכרים, סכסוכי בעלות, עיקולים — המידע הקיים אינו
  אמין ועלול להשתנות.</li>
  <li><strong>פרויקט ייזום ללא דוחות כספיים מלאים:</strong> ללא NOI היסטורי, לא ניתן לנרמל
  ולבנות תחזית אמינה.</li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>עקרון הבחירה:</strong><br>
  בחר נכס שיש עליו מספיק נתונים — ניתוח על נתונים חסרים הוא ניתוח חסר.
  עדיף נכס "פשוט" עם נתונים מלאים על נכס "מרשים" שאין עליו מידע. הוועדה
  תעריך ניתוח עמוק על נכס פשוט — לא ניתוח שטחי על נכס גדול ומרשים.
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Comprehension HTML
# ---------------------------------------------------------------------------

M2_COMPREHENSION_HTML = """
<p>ענה על שאלות ההבנה הבאות.</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Exercises HTML
# ---------------------------------------------------------------------------

M2_EXERCISES_HTML = """
<p>פתור את התרגילים הבאים.</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — בחירת נכס וליקוט נתונים</h2>

<h3>נקודות מפתח</h3>
<ol>
  <li>
    <strong>בחר נכס מניב עם נתונים:</strong> משרדים, מסחר, לוגיסטיקה או מגורים מוסדיים —
    עם NOI היסטורי, רשימת שוכרים ועסקאות השוואה זמינות. קרקע ופרויקטי ייזום לא מתאימים.
  </li>
  <li>
    <strong>שישה מקורות מידע ישראליים:</strong> רמ"י, טאבו, עיריות, מדלן/יד2, דוחות REITs,
    שמאויות — כל אחד תורם נדבך שונה לתיק הנתונים.
  </li>
  <li>
    <strong>תיק הנתונים חייב לכלול:</strong> תיעוד פיזי, ניתוח אזורי, רשימת שוכרים מלאה,
    סיכומי חוזים, דוחות כספיים ל-3 שנים, ו-3 עסקאות השוואה לפחות.
  </li>
  <li>
    <strong>ניתוח שוק המשנה:</strong> שיעורי ריקנות, מגמות שכ"ד, Comparable Sales ו-New
    Supply Pipeline — ברמת הסאב-מרקט הספציפי, לא "ישראל בכלל".
  </li>
  <li>
    <strong>דגלים אדומים:</strong> אין נתונים, ליטיגציה פעילה, ייזום ללא דוחות מלאים —
    נכסים אלו יכשילו את הפרויקט בשלב מוקדם.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
בחרת נכס ובנית תיק נתונים ראשוני. <em>מודול 3</em> ילמד אותך <strong>כיצד לבצע
Due Diligence מקיף ולאסוף את מסמכי הבסיס</strong> — הצעד שקובע אם הניתוח שלך
עומד על קרקע מוצקה או על נתונים לא מאומתים.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (ביצוע Due Diligence ואיסוף מסמכים)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>ביצוע Due Diligence ואיסוף מסמכים — מה חייבים לבדוק</h2>

<p>
Due Diligence (DD) הוא תהליך הבדיקה המקיף שמבצע המלווה (ובפרויקט — האנליסט) לפני
מתן ההלוואה. מטרת ה-DD: לאמת שהמידע שהציג הלווה מדויק, לחשוף בעיות שלא גולו,
ולהעריך את הסיכונים הנסתרים בנכס. מזכר אשראי ללא פרק DD מלא הוא מזכר חסר —
גם אם המספרים נכונים.
</p>

<h2>רשימת ה-DD לפרויקט הגמר — ששת המסמכים הסטנדרטיים</h2>

<p>
בכל עסקת נדל"ן מסחרית, קיימים ששה סוגי מסמכי DD שחייבים להיות מטופלים. לכל אחד —
הסבר מה נבדק, ומה לכלול במזכר:
</p>

<ol>
  <li>
    <strong>שמאות (Appraisal):</strong> שמאות מוסמכת ועצמאית של הנכס. חייבת להיות מ"שמאי
    מוסמך" שאינו מטעם הלווה. השמאות קובעת את שווי השוק (Market Value) ושווי הכינוס
    (Forced Sale Value) — שניהם רלוונטיים לחישוב LTV. כלול במזכר: שם השמאי, תאריך
    השמאות, המתודולוגיה (הכנסה, השוואה, עלות), שווי שוק, Cap Rate שנגזר, והנחות מרכזיות.
  </li>
  <li>
    <strong>בדיקה הנדסית (Engineering Survey):</strong> בדיקת מצב הנכס הפיזי — מבנה,
    חשמל, אינסטלציה, מערכות מיזוג, גג, חניה. מבצעה: מהנדס עצמאי. הפלט הוא דו"ח המפרט
    פגמים קיימים ועלות תיקונם. כלול במזכר: אם נמצאו ליקויים, מה עלות התיקון ומי נושא בה,
    והאם יש ליקויים קריטיים שמפחיתים את שווי הנכס.
  </li>
  <li>
    <strong>בדיקה סביבתית (Environmental Survey):</strong> בדיקת זיהום קרקע, חומרים
    מסוכנים (אסבסט, עופרת), מי תהום מזוהמים. קריטי לנכסי תעשייה ומחסנים. כלול במזכר:
    אם נמצא זיהום — מה עלות הניקוי, ומי אחראי משפטית (הלווה הנוכחי? הקודם?).
  </li>
  <li>
    <strong>בדיקת בעלות ורישום (Title Search):</strong> נסח טאבו מלא — רישום הבעלות,
    שיעבודים (משכנתאות), עיקולים, הערות אזהרה, זכויות עוברות. כלול במזכר: האם הבעלות
    ברורה? האם קיימים שיעבודים קיימים (First Lien, Second Lien)? האם קיימות הגבלות
    העברה?
  </li>
  <li>
    <strong>ביטוח (Insurance):</strong> כיסוי ביטוחי נאות — ביטוח מבנה, ביטוח אחריות,
    ביטוח אובדן שכר דירה. כלול במזכר: פירוט הכיסויים הקיימים, אם יש כיסוי נאות לאובדן
    שכ"ד, ואם המלווה מצוין כמוטב (Loss Payee) בפוליסה.
  </li>
  <li>
    <strong>דוחות כספיים (Financial Statements):</strong> דוחות מבוקרים או מסוקרים של
    הנכס לשלוש שנים אחרונות. כלול: הכנסות, הוצאות תפעול, NOI לפני שירות חוב. כלול
    במזכר: נרמול ה-NOI (הסרת הוצאות חד-פעמיות, התאמת עלויות ניהול לשיעור שוק), וה-NOI
    המנורמל ששימש בסיס לניתוח.
  </li>
</ol>

<h2>כיצד לטפל במסמכים חסרים בפרויקט</h2>

<p>
לא תמיד ניתן להשיג את כל ששת המסמכים לנכס שבחרת לפרויקט. זהו מצב תקין — אך
<strong>אסור להתעלם מהפערים</strong>. הדרך הנכונה לטפל בהם:
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>נוסחת הפער:</strong><br><br>
  לכל מסמך שאינו ברשותך, כלול במזכר:<br>
  (א) <em>מה חסר:</em> "שמאות עצמאית לא נמצאה ברשות הציבורית"<br>
  (ב) <em>מה הייתי מבקש בעסקה אמיתית:</em> "בעסקה ריאלית, הייתי מחייב הזמנת שמאות
  עצמאית כתנאי מקדים למתן הלוואה"<br>
  (ג) <em>כיצד הפער משפיע על הניתוח:</em> "בהיעדר שמאות, השתמשתי ב-Cap Rate של 7%
  בהתאם לממוצע שוק מדוחות ריט — עם אי-ודאות של ±10% בשווי"<br><br>
  <strong>מזכר שמסביר פערים מדויקים ומתאים אותם לניתוח — עדיף על מזכר שמעמיד פנים
  שכל המסמכים קיימים.</strong>
</div>

<h2>כתיבת פרק ה-DD במזכר</h2>

<p>
פרק ה-DD במזכר חייב לכלול שלושה חלקים:
</p>

<ul>
  <li>
    <strong>מה נסקר:</strong> רשימה של כל מסמך/בדיקה שבוצעה — מקור המסמך, תאריכו, ומבצעו.
    לדוגמה: "נסח טאבו — הוצא ב-03/2025 מרשם המקרקעין; שמאות — פורסמה בדו"ח שנתי REIT X
    ב-12/2024".
  </li>
  <li>
    <strong>פערים שזוהו:</strong> כל מסמך שחסר ומה הייתה הדרישה בעסקה אמיתית.
  </li>
  <li>
    <strong>השפעת הפערים על הניתוח:</strong> כיצד כל פער הוביל להנחת-עבודה, לאי-ודאות
    נוספת, או לדרישת מיתיגציה במסגרת ההמלצה.
  </li>
</ul>

<h2>קריאת נסח טאבו — מה לחפש</h2>

<p>
נסח הטאבו הוא "תעודת הזהות" של הנכס. בפרויקט הגמר, עליך לקרוא נסח ולהסביר את
ממצאיו. הנה מה לחפש:
</p>

<ul>
  <li><strong>בעלות:</strong> מי הבעלים הרשומים? יחיד, שותפות, חברה? האם יש בעלות משותפת?</li>
  <li><strong>שיעבודים:</strong> האם קיימות משכנתאות רשומות? מי המלווה? מה הסכום? First Lien
  או Second Lien?</li>
  <li><strong>הערות אזהרה:</strong> הגבלת העברה, עיקול, תביעה ממתינה — כל אחת מהן
  מסמנת בעיה שחייבת להיות מוסברת במזכר.</li>
  <li><strong>זכויות עוברות:</strong> זיקות הנאה (Easements) — זכות מעבר לנכס שכן, קו
  תשתית — עלולות להגביל שימוש עתידי.</li>
</ul>

<h2>נרמול NOI לצורך הפרויקט</h2>

<p>
הדוחות הכספיים ההיסטוריים של הנכס לעיתים כוללים פריטים חד-פעמיים או לא-שגרתיים
שמעוותים את ה-NOI. לפני שימוש ב-NOI בחישובי DSCR ו-DCF, יש לנרמל:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
דוגמה — נרמול NOI:<br><br>
NOI מדווח (שנת 2024): 2,800,000 ₪<br><br>
התאמות:<br>
(+) שכ"ד חסר ל-3 חודשים ריקנות חריגה (שוכר שעזב ממניע יחיד): +180,000 ₪<br>
(-) הכנסת פיצוי חד-פעמי מביטוח (לא חוזרת): -120,000 ₪<br>
(-) תוספת ניהול: מדווח ב-3%, שוק ב-5% → הוסף עלות: -56,000 ₪<br><br>
NOI מנורמל: 2,800,000 + 180,000 - 120,000 - 56,000 = 2,804,000 ₪<br><br>
NOI מנורמל ישמש בסיס לחישוב DSCR ו-DCF — לא NOI המדווח.
</div>

<p>
<strong>גשר למודול הבא:</strong> לאחר שאספת את כל הנתונים, ביצעת את ה-DD ונרמלת את
ה-NOI — עכשיו מגיע החלק הפיננסי: בניית המודל. מודול 4 ילמד אותך לבנות את מלוא
המודל הפיננסי — DCF, DSCR שנתי, LTV ו-Stress Tests — שיהיה לב המזכר.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Comprehension HTML
# ---------------------------------------------------------------------------

M3_COMPREHENSION_HTML = """
<p>ענה על שאלות ההבנה הבאות.</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Exercises HTML
# ---------------------------------------------------------------------------

M3_EXERCISES_HTML = """
<p>פתור את התרגילים הבאים.</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — ביצוע Due Diligence ואיסוף מסמכים</h2>

<h3>נקודות מפתח</h3>
<ol>
  <li>
    <strong>ששת מסמכי ה-DD הסטנדרטיים:</strong> שמאות, הנדסית, סביבתית, בעלות/טאבו,
    ביטוח, דוחות כספיים — כל אחד בודק היבט שונה של הנכס. כיסוי כולם (או תיעוד פערים)
    הוא חובה לציון מלא בפרק ה-DD.
  </li>
  <li>
    <strong>פערי מסמכים — מכירים ומתעדים:</strong> מסמך שחסר אינו "נעלם" — מציינים מה חסר,
    מה הייתם מבקשים בעסקה אמיתית, וכיצד הפער השפיע על הנחות הניתוח. שקיפות > שלמות מדומה.
  </li>
  <li>
    <strong>קריאת נסח טאבו:</strong> בעלות ברורה, שיעבודים קיימים, הערות אזהרה וזיקות הנאה —
    ארבעה ממצאים שחייבים להופיע בפרק ה-DD של כל מזכר.
  </li>
  <li>
    <strong>נרמול NOI:</strong> NOI מדווח אינו NOI לניתוח. הסר הכנסות חד-פעמיות, התאם
    עלויות ניהול לשיעור שוק, והוסף שכ"ד על ריקנות חריגה. NOI מנורמל בלבד ישמש בחישובי
    DSCR ו-DCF.
  </li>
  <li>
    <strong>פרק ה-DD במזכר — שלושה חלקים:</strong> מה נסקר, פערים שזוהו, השפעת הפערים
    על הניתוח. מבנה ברור זה מראה לוועדת האשראי שה-DD בוצע ביסודיות ובשקיפות.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
אספת נתונים, ביצעת DD ונרמלת את ה-NOI. <em>מודול 4</em> הוא לב הפרויקט:
<strong>בניית המודל הפיננסי המלא</strong> — DCF, DSCR שנתי לחמש שנים, LTV ו-Stress
Tests — שיהיו הגרעין המספרי של מזכר האשראי שלך.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 12 "
        '(פרויקט גמר — מימון נדל"ן)'
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 12 ──────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=12)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=12 not found. "
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
            self.style.SUCCESS("\nAll done — Course 12 modules 1-3 seeded successfully.")
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
