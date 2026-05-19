"""
Seeds Module 1-3 content for Course 10 (ניתוח תרחישי סיכון).
Usage: python manage.py seed_c10_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": 'מסגרת ניתוח תרחישים — Base, Bear, Stress',
        "slug": "misgeref-nitur-tarkhishim",
        "estimated_minutes": 55,
    },
    {
        "module_number": 2,
        "title_he": 'תרחישי ריבית ושוק הנדל"ן',
        "slug": "tarkhishe-ribit-veshuk-nadlan",
        "estimated_minutes": 55,
    },
    {
        "module_number": 3,
        "title_he": "תרחישי שוכר — יציאה ותפוסה",
        "slug": "tarkhishe-shocher-yetzia-vtefusa",
        "estimated_minutes": 50,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (מסגרת ניתוח תרחישים)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>מסגרת ניתוח תרחישים — Base, Bear, Stress</h2>

<p>
אנליסט אשראי שמגיש תחזית נקודתית אחת ל-NOI ול-DSCR טועה מראש — לא בכוונה, אלא
בהכרח. כלכלת נדל"ן מתאפיינת בתנודתיות, באי-ודאות ובמחזוריות. תחזית נקודתית אחת
("NOI שנה הבאה יהיה 2.5M ₪") מתעלמת ממגוון רחב של תוצאות אפשריות. ניתוח תרחישים
הוא הכלי שמחייב את האנליסט לחשוב ולתעד מספר מסלולי עתיד — ולבחון האם ההלוואה
עמידה גם בתרחישים שליליים.
</p>

<h2>מדוע תחזית נקודתית אינה מספיקה</h2>

<p>
כאשר אנליסט מציג תחזית בסיס בלבד, ועדת האשראי אינה יודעת:
</p>

<ul>
  <li>מה הסיכון לחריגה כלפי מטה — כמה ה-DSCR יירד בסביבה עויינת?</li>
  <li>האם ה-DSCR בתחזית הבסיס כולל כרית ביטחון ריאלית, או שהוא מחושב בתנאים אופטימיסטיים?</li>
  <li>מה נקודת השבירה — התרחיש שבו ההלוואה כושלת?</li>
  <li>כמה חמור תרחיש הסיכון הסביר?</li>
</ul>

<p>
ניתוח תרחישים ממיר שאלות אלו לנתונים כמותיים שוועדת האשראי יכולה לקבל בהם החלטה מושכלת.
</p>

<h2>ארבעה שכבות תרחיש — הגדרה ומטרה</h2>

<h3>1. Base Case — תרחיש הבסיס</h3>
<p>
<strong>הגדרה:</strong> ציפיית השוק הסבירה ביותר — לא אופטימיסטית, לא פסימיסטית. מבוסס
על נתוני שוק עדכניים, תחזיות מסלול ריבית, ביצועי הנכס בשנים האחרונות ונתוני השוכרים.
</p>
<p>
<strong>מטרה:</strong> לשמש כנקודת ייחוס — כל שאר התרחישים נמדדים ביחס אליו.
</p>

<h3>2. Bear Case — תרחיש דובי</h3>
<p>
<strong>הגדרה:</strong> תרחיש שלילי סביר — לא קטסטרופלי, אך מייצג הרעה משמעותית בתנאים.
בסטטיסטיקה, Bear Case שואף לייצג תרחיש של בערך סטיית תקן אחת (<strong>−1σ</strong>)
מתחת לציפייה.
</p>
<p>
<strong>מטרה:</strong> לבחון שהעסקה עמידה גם כאשר הנסיבות פחות טובות מהצפוי. Bear Case
הוא "תרחיש שכיח" — עסקה טובה חייבת לשרוד אותו ללא עזרה חיצונית.
</p>

<h3>3. Stress Case — תרחיש לחץ</h3>
<p>
<strong>הגדרה:</strong> תרחיש קשה מאוד — שתי סטיות תקן (<strong>−2σ</strong>) מתחת לציפייה.
הוא אינו ה"תרחיש הרגיל" — הוא קורה, אבל בתדירות נמוכה (10%–15% מהמקרים בתחזיות
מושכלות). הוא מחייב כאב: DSCR יורד, NOI נסחט, ייתכן שכרית הביטחון נשחקת.
</p>
<p>
<strong>מטרה:</strong> לאתר את נקודות השבירה — מה הדבר הראשון שיישבר? מה עוצמת ההפסד?
האם הביטחונות מכסים את החשיפה?
</p>

<h3>4. Extreme / Tail Case — תרחיש זנב קיצוני</h3>
<p>
<strong>הגדרה:</strong> תרחיש ה"גרוע מכל" — מבוסס על <strong>אירועים היסטוריים קיצוניים</strong>
(אסון פיננסי 2008, מגפת COVID, מלחמות, קריסות שוק). הסתברות נמוכה (1%–5%), אך השפעה
קטסטרופלית.
</p>
<p>
<strong>מטרה:</strong> לא לאמוד ציפיות, אלא לבדוק כמה ייגבה המלווה במצב כשל מוחלט —
האם ביטחונות מספיקים לכיסוי מלא של חוב.
</p>

<h2>תשומות מפתח לבחינה בכל תרחיש</h2>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">תשומה</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">Base Case</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">Bear Case</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">Stress Case</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">Extreme Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">NOI</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תחזית בסיס</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">−10% עד −15%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">−20% עד −30%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">−40%+</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעור ריקנות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5%–10%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">15%–20%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">25%–35%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">50%+</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Cap Rate יציאה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Cap Rate נוכחי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">+50 bps</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">+100–150 bps</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">+200–300 bps</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית קיימת</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">+100 bps</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">+200–300 bps</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">+400–500 bps</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אופק החזקה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כמתוכנן</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">+1–2 שנים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">+3 שנים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כפוי / מימוש מהיר</td>
    </tr>
  </tbody>
</table>

<h2>כיצד מכיילים את עוצמת התרחיש?</h2>

<p>
שאלה מרכזית היא: כמה חמור כל תרחיש צריך להיות? שלוש גישות נפוצות:
</p>

<h3>גישה 1 — סטטיסטית (σ-based)</h3>
<p>
Bear Case = −1σ מהממוצע ההיסטורי של NOI / ריבית / תפוסה; Stress Case = −2σ; Extreme = worst
observed. דורשת נתוני עבר עמוקים — מתאים לשווקים בוגרים עם סדרות זמן ארוכות.
</p>

<h3>גישה 2 — תרחישים נרטיביים</h3>
<p>
Bear Case = "מיתון קל — ריקנות עולה ב-10%, שכ"ד יורד ב-8%";
Stress Case = "מיתון עמוק — ריקנות 30%, שכ"ד ירד ב-20%, ריבית עלתה 200bps".
גישה זו שקופה יותר ומאפשרת לוועדת האשראי לבחון את ההנחות.
</p>

<h3>גישה 3 — תרחישים היסטוריים</h3>
<p>
Stress Case = שיחזור שנת 2008 על הנכס הנוכחי; Extreme = שיחזור COVID 2020.
אינפורמטיבי מאוד, אך מחייב נתוני שוק מפורטים.
</p>

<h2>תרחיש לעומת ניתוח רגישות — משלימים, לא מתחרים</h2>

<p>
<strong>ניתוח רגישות</strong> (Sensitivity Analysis) בוחן השפעת שינוי <em>תשומה אחת</em>
בכל פעם — למשל: "מה קורה ל-DSCR אם NOI יורד ב-10%?" הוא מדיד, פשוט וקל להצגה בטבלה.
</p>
<p>
<strong>ניתוח תרחישים</strong> בוחן שינוי <em>מספר תשומות בו-זמנית</em> — כי במציאות,
הרעה בשוק מביאה לירידת NOI <strong>ובמקביל</strong> לעלייה בריבית ולהרחבת Cap Rate.
התרחישים מייצגים את המציאות טוב יותר, כי הם לוכדים את הקורלציה בין משתנים.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>עיקרון יסוד — Stress DSCR:</strong><br><br>
  DSCR בתרחיש ה-Stress חייב לעלות על 1.0 — לא רק בתרחיש הבסיס. DSCR שיורד מתחת ל-1.0
  ב-Stress Case פירושו שהנכס לא מכסה את שירות החוב בתנאי לחץ — וזהו תנאי מינימלי
  שוועדות אשראי שמרניות לא יאשרו ללא מיתיגציה משמעותית (LTV נמוך יותר, בטחון נוסף,
  ערבות אישית חזקה).
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — Stress Test שאינו מכאיב אינו Stress Test:</strong><br>
  תרחיש "לחץ" שבו DSCR יורד מ-1.40 ל-1.35 אינו תרחיש לחץ — הוא תרחיש בסיס קצת
  גרוע יותר. Stress Case אמיתי חייב לגרום לכאב מדיד: ירידת DSCR לאזור 1.0–1.1,
  אירוסיה משמעותית בשווי הנכס, ועל האנליסט לתעד בדיוק מה שואב את כרית הביטחון.
  אם התרחיש "קל מדי" — ועדת האשראי לא מקבלת את המידע הנחוץ.
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
<h2>סיכום מודול 1 — מסגרת ניתוח תרחישים</h2>

<h3>נקודות מפתח</h3>
<ul>
  <li>
    <strong>תחזית נקודתית לעולם שגויה:</strong> ניתוח תרחישים מחייב את האנליסט לתעד מספר
    מסלולי עתיד ולבחון את עמידות ההלוואה בכולם — לא רק בתרחיש הבסיס.
  </li>
  <li>
    <strong>ארבע שכבות:</strong> Base Case (ציפיית שוק סבירה), Bear Case (−1σ, תרחיש שכיח),
    Stress Case (−2σ, תרחיש לחץ), Extreme/Tail Case (אסון היסטורי, בדיקת ביטחונות).
  </li>
  <li>
    <strong>תשומות לכיול:</strong> NOI, שיעור ריקנות, Cap Rate יציאה, ריבית ואופק החזקה —
    כל אחד מחמיר בהדרגה מ-Base ל-Extreme. הכיול מבוסס על σ, נרטיב או היסטוריה.
  </li>
  <li>
    <strong>תרחיש ≠ רגישות:</strong> רגישות מזיזה תשומה אחת; תרחיש מזיז מספר תשומות בו-זמנית
    ומייצג קורלציות ריאליות בין שינויי שוק — הכלי הנכון לניתוח אשראי.
  </li>
  <li>
    <strong>Stress DSCR מינימלי 1.0:</strong> DSCR בתרחיש Stress מתחת ל-1.0 הוא קו אדום.
    Stress Test שאינו מכאיב אינו בדיקה אמיתית — ועדת האשראי לא מקבלת את המידע הנחוץ.
  </li>
</ul>

<h3>גשר למודול הבא</h3>
<p>
הנחנו את מסגרת ארבעת השכבות ולמדנו לכייל תרחישים. <em>מודול 2</em> יתרגל את המסגרת
על <strong>תרחישי ריבית ושוק הנדל"ן</strong> — שוקי ריבית ישראלי כדוגמה חיה,
חישובי DSCR תחת הלם ריבית, והשפעת הרחבת Cap Rate על שווי הנכס.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (תרחישי ריבית ושוק הנדל"ן)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>תרחישי ריבית ושוק הנדל"ן</h2>

<p>
מודול זה מיישם את מסגרת ארבעת שכבות התרחיש על שני גורמי סיכון מאקרו-כלכליים:
<strong>עלייה בריבית</strong> ו<strong>ירידת שווי נכסים</strong>. אלו אינם גורמים
עצמאיים — הם מתואמים חזק ויוצרים "סערה מושלמת" כאשר מתממשים בו-זמנית.
</p>

<h2>תרחישי הלם ריבית — +100bps, +200bps, +300bps</h2>

<p>
ריבית היא הגורם הבודד בעל ההשפעה הישירה ביותר על שירות החוב בהלוואות פריים.
שלושה תרחישי הלם סטנדרטיים:
</p>

<h3>+100bps — Bear Case</h3>
<p>
עלייה צנועה בריבית, תואמת מחזור הידוק מוניטרי מתון. ב-Bear Case, הלוואה של 10M₪
בריבית בסיס 8% תעלה לריבית 9% — נטל ריבית עולה ב-100,000 ₪ לשנה.
</p>

<h3>+200bps — Stress Case</h3>
<p>
עלייה משמעותית, תואמת מחזור הידוק חריף. כמו שהיה בישראל 2022–2023 (תוך שנה וחצי).
אותה הלוואה של 10M₪ תשלם 200,000 ₪ ריבית נוספת לשנה — עלייה של 25% בעלות החוב.
</p>

<h3>+300bps — Extreme Case</h3>
<p>
עלייה קיצונית. בישראל 2022–2024, הפריים עלה 465bps — תרחיש +300bps היה שמרני
מהמציאות. אותה הלוואה תשלם 300,000 ₪ נוספים — עלייה של 37.5% בעלות החוב.
</p>

<h2>ירידת שווי נכסים — −10%, −20%, −30%</h2>

<p>
ירידת שווי נכס משפיעה ישירות על <strong>LTV (Loan-to-Value)</strong> וסיכון ה-Covenant.
כאשר LTV חוצה את רף ה-Covenant (בדרך כלל 70%–75%), הלווה חייב לפרוע חלק מהקרן
כדי להחזיר את ה-LTV לסף — או שהבנק רשאי לקרוא להלוואה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
תרחישי LTV — הלוואה 14M₪ על נכס ששוויו 20M₪ (LTV בסיס: 70%)<br><br>
תרחיש −10%: שווי נכס יורד ל-18M₪ → LTV = 14/18 = 77.8% ← הפרת Covenant LTV&lt;75%<br>
תרחיש −20%: שווי נכס יורד ל-16M₪ → LTV = 14/16 = 87.5% ← פגיעה קשה<br>
תרחיש −30%: שווי נכס יורד ל-14M₪ → LTV = 14/14 = 100% ← ביטחון מכסה חוב בדיוק<br><br>
מסקנה: בירידה של 10% בלבד כבר מופר ה-Covenant — ללא כרית ביטחון אמיתית.
הבנק יכול לדרוש פירעון מוקדם חלקי.
</div>

<h2>הרחבת Cap Rate — הנהג ואמידת השפעה</h2>

<p>
<strong>Cap Rate</strong> (שיעור ההיוון) הוא NOI / שווי נכס. Cap Rate גבוה יותר = שווי
נמוך יותר לאותו NOI. Cap Rate מורחב בשני מצבים:
</p>

<ul>
  <li>
    <strong>עלייה בפרמיית הסיכון:</strong> כאשר המשק תופס נדל"ן כסוכן (uncertainty rises),
    משקיעים דורשים תשואה גבוהה יותר — Cap Rate עולה.
  </li>
  <li>
    <strong>עלייה בתשואות האג"ח:</strong> Cap Rate שואף לסגור פרמיה מעל תשואות אג"ח ממשלתי
    ארוך. כאשר תשואות עולות בגלל העלאת ריבית, Cap Rate עולה בעקבות.
  </li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
הרחבת Cap Rate — נכס עם NOI שנתי 1,200,000 ₪:<br><br>
Cap Rate 6.0% (Base): שווי = 1,200,000 / 0.060 = 20,000,000 ₪<br>
Cap Rate 6.5% (Bear): שווי = 1,200,000 / 0.065 = 18,461,538 ₪ (−7.7%)<br>
Cap Rate 7.0% (Stress): שווי = 1,200,000 / 0.070 = 17,142,857 ₪ (−14.3%)<br>
Cap Rate 8.0% (Extreme): שווי = 1,200,000 / 0.080 = 15,000,000 ₪ (−25.0%)<br><br>
הרחבה של 200bps ב-Cap Rate שוקלת שווי ב-25% — ללא שינוי ב-NOI כלל.
</div>

<h2>קורלציה — הסערה המושלמת</h2>

<p>
הסכנה הגדולה ביותר היא שלושת הגורמים מתממשים <strong>בו-זמנית</strong>:
</p>
<ol>
  <li><strong>עלייה בריבית</strong> — נטל שירות חוב עולה → DSCR יורד</li>
  <li><strong>הרחבת Cap Rate</strong> (בגלל עלייה בריבית) — שווי נכס יורד → LTV עולה</li>
  <li><strong>כיווץ NOI</strong> (מחזור כלכלי עמוק) — גם הכנסות יורדות → DSCR נסחט עוד</li>
</ol>

<p>
שלושתם מתואמים חיובי — כאשר הריבית עולה חדות, כלכלה נוטה להאט, NOI יורד והשוק
תופס יותר סיכון (Cap Rate עולה). זהו תרחיש ה-Stress המשמעותי ביותר.
</p>

<h2>הקשר ישראלי — 2022–2024</h2>

<p>
ישראל חוותה בדיוק תרחיש זה:
</p>
<ul>
  <li>בנק ישראל העלה ריבית מ-0.1% ל-4.75% — עלייה של 465bps תוך 18 חודשים (2022–2023)</li>
  <li>תשואות אג"ח ממשלה עלו בהתאם, מה שלחץ Cap Rate כלפי מעלה</li>
  <li>שוק המשרדים חווה עלייה בריקנות (בחלקה בגלל מגמות hybrid work ובחלקה בגלל אי-ודאות כלכלית)</li>
  <li>עסקאות שנישומו על בסיס Cap Rate 5.5% הפכו בעייתיות כאשר Cap Rate שוק עלה לכיוון 6.5%–7%</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — לקחי 2022–2023 בישראל:</strong><br><br>
  מודלים שנבנו ב-2020–2021 עם תרחיש Stress של +200bps לא היו שמרניים מספיק — הריבית
  עלתה יותר מכך. בנק ישראל העלה ב-465bps. מודל ניתוח אשראי שלא בחן תרחיש +300bps
  לא היה מתאים לתנאי השוק שנוצרו. <strong>בסביבת ריבית נמוכה היסטורית (2015–2021),
  +300bps נראה קיצוני; לאחר 2022 — הוא תרחיש Stress סטנדרטי.</strong>
</div>

<h2>דוגמה מחושבת — הלוואת 10M ₪ עם הלם +200bps</h2>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
נתוני בסיס:<br>
  הלוואה:       10,000,000 ₪<br>
  ריבית בסיס:   פריים + 1.5% = 6.0% + 1.5% = 7.5%<br>
  שירות חוב:    10,000,000 × 7.5% = 750,000 ₪/שנה (ריבית בלבד, Bullet)<br>
  NOI שנתי:     800,000 ₪<br>
  DSCR בסיס:    800,000 / 750,000 = 1.07<br><br>
Stress Case +200bps:<br>
  ריבית חדשה:   7.5% + 2% = 9.5%<br>
  שירות חוב:    10,000,000 × 9.5% = 950,000 ₪/שנה<br>
  DSCR Stress:  800,000 / 950,000 = 0.84<br><br>
מסקנה: DSCR בתרחיש Stress = 0.84 — מתחת ל-1.0. הנכס לא מכסה ריבית בתנאי לחץ.
→ בתרחיש זה הבנק ייחשף להפסד; העסקה דורשת LTV נמוך יותר, ריבית קבועה, או NOI גדול יותר.
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
<h2>סיכום מודול 2 — תרחישי ריבית ושוק הנדל"ן</h2>

<h3>נקודות מפתח</h3>
<ul>
  <li>
    <strong>שלושה תרחישי הלם ריבית:</strong> +100bps (Bear), +200bps (Stress), +300bps (Extreme).
    בישראל 2022–2023 הפריים עלה 465bps — +300bps היה תרחיש שמרני ממה שקרה בפועל.
  </li>
  <li>
    <strong>LTV וירידת שווי:</strong> ירידה של 10% בשווי הנכס יכולה לשבור Covenant LTV
    כבר ב-LTV בסיס של 70%. כרית ביטחון של 30% (LTV=70%) נשחקת מהר בסביבת לחץ.
  </li>
  <li>
    <strong>Cap Rate — מנגנון ההעברה:</strong> עלייה בריבית → עלייה בתשואות אג"ח → הרחבת
    Cap Rate → ירידת שווי נכס. הרחבה של 200bps ב-Cap Rate שוחקת 25% מהשווי ללא שינוי ב-NOI.
  </li>
  <li>
    <strong>הסערה המושלמת:</strong> עלייה בריבית + הרחבת Cap Rate + כיווץ NOI — שלושתם
    מתואמים ומתרחשים ביחד. ניתוח תרחישים חייב ללכוד קורלציות אלו, לא לנתח כל גורם לבד.
  </li>
  <li>
    <strong>DSCR Stress &lt; 1.0 = אות אדום:</strong> הדוגמה המחושבת הראתה כיצד DSCR של
    1.07 בבסיס נופל ל-0.84 ב-Stress +200bps — עסקה שנראית תקינה בבסיס אינה עמידה בלחץ.
  </li>
</ul>

<h3>גשר למודול הבא</h3>
<p>
ניתחנו תרחישים מקרו-כלכליים — ריבית ושוק. <em>מודול 3</em> יעבור לתרחישים ברמת
הנכס עצמו: <strong>תרחישי שוכר — יציאה, ריקנות ותפוסה</strong> — כיצד בוחנים
שרידות ההלוואה כאשר שוכר עוגן עוזב, וכיצד מחשבים Break-Even Occupancy בתרחיש לחץ.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (תרחישי שוכר — יציאה ותפוסה)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>תרחישי שוכר — יציאה, ריקנות ותפוסה</h2>

<p>
גם כאשר הריבית יציבה ושוק הנדל"ן לא בלחץ, נכס יכול להכשיל הלוואה בגלל אירועים
ברמת הנכס עצמו: שוכר גדול שעוזב, עלייה בריקנות, ירידת שכ"ד בחידוש חוזים. מודול
זה בונה תרחישים שוכר-מוכווני ומחשב את השפעתם על NOI ו-DSCR.
</p>

<h2>תרחיש שוכר יחיד — עזיבה מלאה</h2>

<p>
<strong>נכס Single-Tenant</strong> (שוכר בודד) הוא הנכס הפגיע ביותר לתרחיש יציאה.
כאשר השוכר עוזב:
</p>

<ul>
  <li>NOI יורד <strong>מ-100% לאפס</strong> (או לכמעט-אפס אם יש תשלום מינימלי בתקופת הסגת-יד)</li>
  <li>שירות החוב ממשיך — הלווה מממן אותו מהון עצמי</li>
  <li>ציר הזמן לשכירת שוכר חלופי: <strong>12–36 חודשים</strong> טיפוסי (תלוי בסוג הנכס, מיקום וגודל)</li>
  <li>עלויות "חידוש": שיפוצים לדרישות השוכר החדש (Fit-Out), הנחות שכ"ד בתחילת חוזה (Rent-Free Period)</li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
תרחיש: מחסן לוגיסטי 8,000 מ"ר, שוכר בודד, NOI שנתי 2,400,000 ₪<br>
הלוואה: 18,000,000 ₪ בריבית 8% = שירות חוב שנתי 1,440,000 ₪<br>
DSCR בסיס: 2,400,000 / 1,440,000 = 1.67<br><br>
תרחיש יציאה:<br>
שוכר עוזב — NOI = 0 (חוזה פג, אין שוכר)<br>
ציר זמן לשוכר חלופי: 18 חודשים<br>
הוצאות Fit-Out לשוכר חדש: 1,600,000 ₪ (200 ₪/מ"ר)<br>
Rent-Free Period: 3 חודשים (NOI חסר עוד 600,000 ₪)<br><br>
עלות תקופת ריקנות: 1,440,000 × 1.5 שנים = 2,160,000 ₪ חוב בלי NOI<br>
+ Fit-Out: 1,600,000 ₪<br>
+ Rent-Free: 600,000 ₪<br>
סה"כ עלות אירוע: ~4,360,000 ₪ — 24% מגובה ההלוואה<br><br>
הלווה נדרש למממן סכום זה מהון עצמי — האם יש לו רזרבות?
</div>

<h2>שוכר עוגן — השפעות מדורגות (Cascading Effects)</h2>

<p>
בנכסי קמעונאות ולוגיסטיקה, שוכר עוגן מייצר <strong>ביקוש משני</strong> לשאר הנכס:
</p>

<ul>
  <li>קניון: שוכר עוגן (רשת אופנה גדולה, סופר) מושך תנועה לשאר הדיירים. עזיבתו פוגעת
  בתנועה — שוכרים משניים עלולים לדרוש הפחתות שכ"ד ואף לעזוב.</li>
  <li>פארק לוגיסטי: שוכר עוגן גדול (אמזון, IKEA) מאפשר למוביל לנהל שרשרת אספקה משותפת.
  עזיבתו מפחיתה את ערך ה"קלסטר" לשאר הדיירים.</li>
</ul>

<p>
<strong>השפעת Cascade:</strong> NOI שוכר עוגן (30%–50% מהסך) יורד לאפס, ובנוסף חלק
מהשוכרים המשניים מפחיתים שכ"ד ב-10%–20% בשל ירידת ערך הנכס. NOI הכולל עלול לרדת
ב-40%–60% — הרבה מעבר לחלקו של שוכר העוגן לבדו.
</p>

<h2>סיכון ה-Re-Leasing — מחיר ואופק</h2>

<p>
<strong>Re-Leasing Spread</strong> הוא הפרש בין שכ"ד הסכם החדש לשכ"ד הסכם שפקע.
ב-Bear/Stress Case, Re-Leasing Spread שלילי — השוכר החדש מקבל תנאים טובים יותר
מהשוכר שעזב.
</p>

<ul>
  <li><strong>Base Case:</strong> Re-Leasing Spread = 0% עד +5% (שוק תקין)</li>
  <li><strong>Bear Case:</strong> Re-Leasing Spread = −5% עד −10% (שוק רפה)</li>
  <li><strong>Stress Case:</strong> Re-Leasing Spread = −15% עד −20% + Rent-Free 6 חודשים</li>
</ul>

<h2>תרחיש עלייה בריקנות — 20% ל-40%</h2>

<p>
תרחיש שלא מבוסס על שוכר ספציפי אלא על הידרדרות שוק כללית:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
נכס משרדים — 6,000 מ"ר, שכ"ד 100 ₪/מ"ר/חודש<br>
שירות חוב שנתי: 3,600,000 ₪<br><br>
Base Case (ריקנות 20%):
  NOI = 6,000 × 0.80 × 100 × 12 = 5,760,000 ₪
  DSCR = 5,760,000 / 3,600,000 = 1.60<br><br>
Bear Case (ריקנות 30%):
  NOI = 6,000 × 0.70 × 100 × 12 = 5,040,000 ₪
  DSCR = 5,040,000 / 3,600,000 = 1.40<br><br>
Stress Case (ריקנות 40%):
  NOI = 6,000 × 0.60 × 100 × 12 = 4,320,000 ₪
  DSCR = 4,320,000 / 3,600,000 = 1.20<br><br>
Extreme Case (ריקנות 55%):
  NOI = 6,000 × 0.45 × 100 × 12 = 3,240,000 ₪
  DSCR = 3,240,000 / 3,600,000 = 0.90 ← מתחת ל-1.0
</div>

<h2>חישוב Break-Even Occupancy בתרחיש לחץ</h2>

<p>
ב-Stress Case, שירות החוב גם הוא עשוי לעלות (בגלל +200bps). Break-Even Occupancy
חייב להתחשב בשירות חוב מוגדל:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
נכס: 6,000 מ"ר, שכ"ד 100 ₪/מ"ר/חודש (הכנסה פוטנציאלית 100% = 7,200,000 ₪/שנה)<br>
הוצאות תפעול קבועות: 1,200,000 ₪/שנה<br><br>
Base Case — שירות חוב 3,600,000 ₪/שנה:<br>
  Break-Even NOI = 3,600,000 + 1,200,000 = 4,800,000 ₪<br>
  Break-Even Occupancy = 4,800,000 / 7,200,000 = 66.7%<br><br>
Stress Case — שירות חוב עולה ב-+200bps ← +400,000 ₪/שנה = 4,000,000 ₪/שנה:<br>
  Break-Even NOI = 4,000,000 + 1,200,000 = 5,200,000 ₪<br>
  Break-Even Occupancy = 5,200,000 / 7,200,000 = 72.2%<br><br>
מסקנה: ב-Stress, נקודת האיזון עולה מ-66.7% ל-72.2% — הכרית מצטמצמת.
נכס שעמד ב-Stress בתפוסה 75% (8.3% כרית) עכשיו עומד ב-75% עם 2.8% כרית בלבד.
</div>

<h2>סיכון Over-Rented — תרחיש היפוך שכ"ד</h2>

<p>
כאשר Passing Rent גבוה ממחיר השוק, חידוש החוזה יביא לירידת NOI — גם אם הנכס נשאר
מאוכלס במלואו. זהו תרחיש שצריך לבנות במפורש:
</p>

<ul>
  <li><strong>Base Case:</strong> Passing Rent = 130 ₪/מ"ר; Market Rent = 130 ₪/מ"ר → NOI ללא שינוי</li>
  <li><strong>Reversion Bear:</strong> Market Rent = 110 ₪/מ"ר → בחידוש, NOI ירד ב-15%</li>
  <li><strong>Reversion Stress:</strong> Market Rent = 90 ₪/מ"ר → בחידוש, NOI ירד ב-31%</li>
</ul>

<p>
הסיכון: המלווה מניח NOI נוכחי גבוה, נותן הלוואה בהתאם, ובמהלך חיי ההלוואה (בחידוש
חוזה) NOI נסחט ו-DSCR מתחת לסף — בלי שום אירוע "חיצוני" קרה.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>עיקרון — NOI פרו-פורמה לפי Market Rent:</strong><br><br>
  כאשר Passing Rent &gt; Market Rent ב-10%+, חשב תמיד <em>גם</em> DSCR לפי Market Rent
  הנוכחי — כאילו החוזה מתחדש היום. אם DSCR לפי Market Rent נמוך מ-1.20, קיים סיכון
  Over-Rented שמחייב Covenant Rent Review ותשקיף כלכלי של שוק השכירות הרלוונטי.
</div>

<h2>גשר למודול 4 — תרחישים ברמת הלווה</h2>

<p>
בנינו תרחישים ברמת הנכס (שוכר יוצא, ריקנות עולה, שכ"ד יורד). <em>מודול 4</em>
יעלה לרמה הבאה: <strong>תרחישים ברמת הלווה</strong> — ירידת הכנסות כוללות, לחץ
בפרויקטים מקבילים, ואותות אזהרה מוקדמים שמאפשרים לבנק לפעול לפני שההלוואה כושלת.
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
<h2>סיכום מודול 3 — תרחישי שוכר: יציאה ותפוסה</h2>

<h3>נקודות מפתח</h3>
<ul>
  <li>
    <strong>שוכר בודד — סיכון מרבי:</strong> יציאת שוכר Single-Tenant מאפסת NOI. ציר זמן
    של 12–36 חודשים לשכירות חלופית + עלויות Fit-Out ו-Rent-Free — הלווה נדרש לממן
    את שירות החוב כולו מהון עצמי בתקופת הביניים.
  </li>
  <li>
    <strong>אפקט Cascade בשוכר עוגן:</strong> שוכר עוגן שעוזב לא רק מוריד את חלקו ב-NOI
    — הוא פוגע בביקוש לשאר הנכס, ושוכרים משניים עלולים להפחית שכ"ד או לעזוב גם הם.
    NOI כולל עלול לרדת ב-40%–60%.
  </li>
  <li>
    <strong>Re-Leasing Spread:</strong> ב-Stress Case, שוכר חדש משלם פחות מהשוכר שעזב.
    −15%–20% ריאלי בסביבת לחץ + Rent-Free 6 חודשים. חייב להיכלל בחישוב NOI פרו-פורמה.
  </li>
  <li>
    <strong>Break-Even Occupancy עולה ב-Stress:</strong> כאשר גם שירות החוב עולה (+200bps),
    נקודת האיזון עולה — הכרית מצטמצמת משני הצדדים בו-זמנית.
  </li>
  <li>
    <strong>Over-Rented — פצצה שקטה:</strong> Passing Rent מעל Market Rent אינו בעיה היום —
    הוא בעיה ביום חידוש החוזה. חשב תמיד DSCR גם לפי Market Rent הנוכחי.
  </li>
</ul>

<h3>גשר למודול הבא</h3>
<p>
ניתחנו תרחישים ברמת הנכס (שוכר, ריקנות, שכ"ד). <em>מודול 4</em> מרחיב לרמת הלווה:
<strong>תרחישי לווה — ירידת הכנסות כוללות, אותות אזהרה מוקדמים ומנגנוני התערבות בנקאית</strong>
לפני שההלוואה מגיעה לכשל מוחלט.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 10 "
        "(ניתוח תרחישי סיכון)"
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 10 ──────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=10)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=10 not found. "
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
            self.style.SUCCESS("\nAll done — Course 10 modules 1-3 seeded successfully.")
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
