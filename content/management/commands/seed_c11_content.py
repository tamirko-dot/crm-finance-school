"""
Seeds Module 1-3 content for Course 11 (כתיבת מזכר אשראי).
Usage: python manage.py seed_c11_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": "מבנה מזכר האשראי — פרקים ורציונל",
        "slug": "mivne-mezker-ashrai-prakim",
        "estimated_minutes": 55,
    },
    {
        "module_number": 2,
        "title_he": "כתיבת תיאור הלווה והנכס",
        "slug": "ktivat-teur-haloveh-vehanakhas",
        "estimated_minutes": 55,
    },
    {
        "module_number": 3,
        "title_he": "ניתוח פיננסי במזכר — NOI, DSCR, LTV",
        "slug": "nitur-pinansi-bamezker-noi-dscr-ltv",
        "estimated_minutes": 60,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (מבנה מזכר האשראי — פרקים ורציונל)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>מזכר האשראי — מהו ומי קורא אותו</h2>

<p>
מזכר האשראי (Credit Memo) הוא המסמך המרכזי שבו אנליסט האשראי מסכם את ניתוחו ומגיש
המלצה לוועדת האשראי. זהו מסמך <strong>הערכת סיכון עצמאית</strong> — לא מצגת שיווקית
ולא תיאור של רצון הלווה, אלא ניתוח מאוזן ומבוסס נתונים של העסקה המוצעת.
</p>

<p>
מי קורא את מזכר האשראי? בדרך כלל שלושה גורמים:
</p>

<ul>
  <li>
    <strong>ועדת האשראי (Credit Committee):</strong> מקבלת ההחלטה הסופית. חבריה עשויים
    לבחון עשרות עסקאות בישיבה אחת — הם מצפים למזכר ממוקד, קצר, ועם מסקנות ברורות.
  </li>
  <li>
    <strong>קצין האשראי הבכיר (Senior Credit Officer):</strong> בודק לפני הוועדה. בוחן
    את איכות הניתוח, את שלמות המידע, ואת ההיגיון הפנימי של ההמלצה.
  </li>
  <li>
    <strong>ציות ורגולציה (Compliance):</strong> מוודא שהמזכר עומד בדרישות ועדת באזל,
    הנחיות בנק ישראל, ומדיניות ניהול הסיכונים של המוסד.
  </li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #388e3c;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>עקרון יסוד:</strong><br>
  מזכר האשראי אינו מסמך מכירה — הוא הערכת סיכון עצמאית. המלצה חיובית ניתנת כי הניתוח
  מראה שהעסקה סבירה, לא כי הלווה רוצה את ההלוואה.
</div>

<h2>פרקי מזכר האשראי הסטנדרטי</h2>

<p>
מזכר אשראי מקצועי בתחום הנדל"ן מכיל שמונה פרקים עיקריים, כל אחד עם תפקיד ייחודי:
</p>

<h3>1. תמצית מנהלים (Executive Summary)</h3>
<p>
סיכום עצמאי של כל העסקה — לווה, נכס, סכום מבוקש, הנמקה עיקרית לאישור או דחייה,
וגורמי הסיכון המרכזיים. הפרק חייב לעמוד בפני עצמו: קורא שיקרא רק את התמצית חייב
להבין את מהות העסקה, את הסיכון, ואת ההמלצה.
</p>

<h3>2. רקע הלווה (Borrower Background)</h3>
<p>
תיאור מקיף של הלווה: מבנה משפטי, בעלות, ניסיון בתחום, עמידה בהתחייבויות עבר,
חוזק פיננסי (שווי נקי, נזילות), ערבים אישיים או תאגידיים.
</p>

<h3>3. תיאור הנכס (Property Description)</h3>
<p>
פרטי הנכס המשמש כבטוחה: מיקום, שטח, גיל, סוג (מסחרי/משרדי/מגורים/תעשייה),
שוכרים נוכחיים, תפוסה, תנאי חוזי שכירות, CapEx שבוצע לאחרונה.
</p>

<h3>4. ניתוח פיננסי (Financial Analysis)</h3>
<p>
הניתוח הכמותי: NOI נורמלי, DSCR לפי שנים, LTV, Debt Yield, ניתוח רגישות.
זהו הפרק הטכני ביותר במזכר.
</p>

<h3>5. ניתוח סיכונים ומיתיגציה (Risk Analysis &amp; Mitigation)</h3>
<p>
מיפוי הסיכונים המהותיים (שוק, ריבית, לווה, נזילות) ומנגנוני המיתיגציה המוצעים
(Covenant, בטחונות, Stress Test, Extension Option).
</p>

<h3>6. ניתוח תרחישים (Scenario Analysis)</h3>
<p>
תרחיש בסיס, תרחיש שמרני (Downside) ותרחיש Stress. לכל תרחיש — DSCR ו-LTV.
</p>

<h3>7. תנאים ועקרונות ההלוואה המוצעים (Proposed Terms &amp; Conditions)</h3>
<p>
סכום, ריבית, מח"מ, שיטת פירעון, Covenants מרכזיים, בטחונות, תנאים מקדימים.
</p>

<h3>8. המלצה (Recommendation)</h3>
<p>
"מאשר" / "מאשר בתנאים" / "דוחה" — עם נימוקים תמציתיים. הפרק האחרון, אך קוראים
רבים קוראים אותו ראשון.
</p>

<h2>התמצית המנהלים — הפרק הקריטי</h2>

<p>
ועדת האשראי קוראת עשרות מזכרים. לעיתים קרובות, הדיון מתחיל ומסתיים בתמצית המנהלים.
תמצית טובה מציגה:
</p>

<ul>
  <li>שם הלווה ומהות הבקשה (מה, כמה, לאיזו מטרה)</li>
  <li>הנכס — סוג, מיקום, שווי</li>
  <li>מדדים פיננסיים מרכזיים — NOI, DSCR, LTV</li>
  <li>גורמי הסיכון המהותיים (1–3 בלבד)</li>
  <li>ההמלצה ותנאים עיקריים</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כשל נפוץ בתמצית המנהלים:</strong><br>
  תמצית שמחייבת את הקורא לעבור לסעיף 4 כדי להבין את העסקה — נכשלה. אם ה-NOI, ה-DSCR
  וה-LTV לא מופיעים בתמצית עצמה, הקורא חסר את המידע הקריטי להחלטה.
</div>

<h2>אורך ופורמט — סטנדרטים מקצועיים</h2>

<p>
מזכר אשראי מקצועי עבור עסקת נדל"ן מסחרי סטנדרטית: <strong>8–15 עמודים</strong>,
כולל טבלאות. מזכר של 30 עמוד על עסקה בינונית הוא בעיה — לא סימן לעומק.
</p>

<ul>
  <li><strong>כמותי, לא שיווקי:</strong> "DSCR 1.32 בשנה 1" — לא "נכס איכותי".</li>
  <li><strong>מבוסס מקורות:</strong> כל נתון מוצמד למסמך בתיק ה-Due Diligence.</li>
  <li><strong>ניטרלי:</strong> לא מתאים את הניתוח לרצוי — מציג את המציאות כפי שהיא.</li>
  <li><strong>קצר ואיכותי:</strong> כל פסקה תורמת — אין חזרות, אין מילוי.</li>
</ul>

<h2>מזכר פנימי מול חיצוני</h2>

<p>
<strong>מזכר פנימי (Internal Credit Memo):</strong> לשימוש פנימי בלבד — ועדת אשראי,
קצין אשראי בכיר, ציות. כולל ניתוח מלא, סיכונים, חולשות. שפה מקצועית אנליטית.
</p>

<p>
<strong>מזכר חיצוני (External Credit Memo / Term Sheet):</strong> לעיתים משותף עם
הלווה. גרסה מצומצמת — מציג את העסקה המוצעת ותנאים עיקריים, ללא חשיפת כל ניתוח
הסיכונים הפנימי של המוסד הפיננסי.
</p>

<p>
<strong>ההבדל המהותי:</strong> המזכר הפנימי הוא מסמך הערכת סיכון; המסמך החיצוני הוא
מסמך תנאים. אנליסט צריך לדעת לכתוב שניהם, ולהבין את ההבדל.
</p>
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
<h2>סיכום מודול 1 — מבנה מזכר האשראי</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>מזכר האשראי הוא הערכת סיכון עצמאית:</strong> לא מסמך שיווקי. מטרתו לאפשר
    לוועדת האשראי לקבל החלטה מושכלת על בסיס ניתוח מאוזן ומבוסס נתונים.
  </li>
  <li>
    <strong>קהל היעד — שלושה גורמים:</strong> ועדת האשראי, קצין האשראי הבכיר, ציות.
    כל אחד מחפש דברים שונים — מזכר טוב עונה לכולם.
  </li>
  <li>
    <strong>שמונה פרקים סטנדרטיים:</strong> תמצית מנהלים, רקע לווה, תיאור נכס, ניתוח
    פיננסי, סיכונים ומיתיגציה, ניתוח תרחישים, תנאים מוצעים, המלצה. הסדר אינו מקרי —
    הוא משקף זרימה הגיונית של ניתוח.
  </li>
  <li>
    <strong>התמצית חייבת לעמוד בפני עצמה:</strong> NOI, DSCR, LTV, גורמי הסיכון המרכזיים
    וההמלצה — כולם בתמצית. קורא שקרא רק אותה חייב להבין את העסקה.
  </li>
  <li>
    <strong>קצר, כמותי, ניטרלי:</strong> מזכר 8–15 עמוד. כל נתון מקושר למקור. שפה
    אנליטית, לא שיווקית. מציגים מציאות, לא מה שרוצים שיהיה.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
הכרנו את מבנה מזכר האשראי ואת הרציונל לכל פרק. <em>מודול 2</em> יצלול לכתיבה
בפועל של שני הפרקים הנרטיביים הראשונים: <strong>רקע הלווה ותיאור הנכס</strong> —
כיצד כותבים תיאורים מבוססי נתונים, מה נדרש, ומה הטעויות הנפוצות.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (כתיבת תיאור הלווה והנכס)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>פרק רקע הלווה — מה לכלול וכיצד לכתוב</h2>

<p>
פרק רקע הלווה אינו ביוגרפיה — הוא הערכה ממוקדת של יכולת הלווה לעמוד בהתחייבויות
ההלוואה. הקורא רוצה לדעת: מי הלווה, מה עמידתו בעבר בהתחייבויות, ומה מצבו הפיננסי כיום.
</p>

<h3>מרכיבי פרק רקע הלווה:</h3>

<h3>1. מבנה משפטי ובעלות</h3>
<p>
תאר את הישות המשפטית הלווה: חברה בע"מ, שותפות, נאמנות, יחיד. מי הבעלים (ישיר ועקיף)
ובאיזה אחוז. בעסקאות מסחריות — הצג את מבנה הקבוצה אם הלווה הוא חברת SPV.
</p>

<h3>2. ניסיון ורקע (Track Record)</h3>
<p>
זהו הסעיף הקריטי ביותר ברקע הלווה. האנליסט חייב לתאר ניסיון <strong>ספציפי וכמותי</strong>,
לא כללי:
</p>

<ul>
  <li>מספר הפרויקטים שבוצעו (ולא "יזם מנוסה")</li>
  <li>סוגי הנכסים (מגורים, מסחרי, לוגיסטיקה, מלונאות)</li>
  <li>גודל פרויקטים (עלויות, שטחים)</li>
  <li>תוצאות — האם הושלמו בזמן ובתקציב?</li>
  <li>כשלים — האם הייתה חדלות פירעון, הסדר חוב, הפרת Covenant בעבר?</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כשל נפוץ — תיאור ללא נתונים:</strong><br>
  כתיבת "יזם מנוסה עם רקורד חזק" ללא מספרים אינה ניתוח — זוהי שיווק. ועדת האשראי
  צריכה מספרים: "ביצע 7 פרויקטי מגורים בשנים 2015–2024, סך עלות 280M₪, כולם הושלמו
  בזמן. ללא הפרות Covenant ביחסי אשראי קיימים."
</div>

<h3>3. חוזק פיננסי</h3>
<p>
הצג שלושה מדדים מרכזיים:
</p>

<ul>
  <li><strong>שווי נקי (Net Worth):</strong> סך נכסים פחות סך התחייבויות של הלווה/הערב.</li>
  <li><strong>נזילות (Liquidity):</strong> מזומנים ושקולי מזומנים זמינים ללא מכירת נכסים.</li>
  <li><strong>מינוף כולל (Overall Leverage):</strong> סך חוב / סך נכסים — מה רמת המינוף
  הכוללת של הלווה, לא רק בפרויקט הנוכחי.</li>
</ul>

<h3>4. ערבים</h3>
<p>
פרט ערבים אישיים ותאגידיים. לכל ערב — שווי נקי מוצהר, נזילות, ואם הוערך על ידי
שמאי עצמאי או לפי הצהרה עצמית בלבד (הצהרה עצמית = אמינות נמוכה יותר).
</p>

<h2>פרק תיאור הנכס — כיצד לתאר נכס בצורה מקצועית</h2>

<p>
פרק תיאור הנכס מספק לוועדה את הבסיס להבנת הבטוחה. הוא חייב להיות <strong>ספציפי,
ניתן לאימות, ומחובר לנתוני שוק</strong>.
</p>

<h3>מרכיבי תיאור הנכס:</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מרכיב</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מה לכלול</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מה לא לכלול</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מיקום</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כתובת, רחוב, עיר, קרבה לתחבורה/מרכזי מסחר</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">"מיקום מצוין" ללא נימוק</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גודל ומפרט</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שטח מ"ר, מספר קומות, גיל הנכס, שנת שיפוץ אחרונה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">"מבנה מרשים"</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שוכרים ותפוסה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רשימת שוכרים עיקריים, % מ-NOI, תאריכי פקיעת חוזה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">"שוכרים איכותיים"</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">CapEx אחרון</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מה בוצע, מתי, בכמה — הוצאות הון בשלוש השנים האחרונות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">"תחזוקה שוטפת"</td>
    </tr>
  </tbody>
</table>

<h2>כיצד לכמת איכות נכס — Class A/B/C, WALT, אשראי שוכרים</h2>

<p>
"נכס Class A" — מה זה אומר? אנליסטים מנוסים מגדירים Class לפי מאפיינים מדידים:
</p>

<ul>
  <li>
    <strong>Class A:</strong> בנוי לאחר 2010, תשתיות מתקדמות (מיזוג, חשמל), מיקום פריים
    (מרכזי מסחר/עסקים ראשיים), שוכרים ברמת S&amp;P BBB+ ומעלה, תפוסה 95%+.
  </li>
  <li>
    <strong>Class B:</strong> בנוי 1990–2010, תחזוקה טובה, מיקום משני, שוכרים בינוניים,
    תפוסה 85%–95%.
  </li>
  <li>
    <strong>Class C:</strong> בנוי לפני 1990, CapEx נדרש, מיקום פריפריה, שוכרים עם
    סיכון אשראי גבוה יותר, תפוסה מתחת ל-85%.
  </li>
</ul>

<p>
<strong>WALT (Weighted Average Lease Term)</strong> — ציין WALT בפרק תיאור הנכס ופרש
אותו בהקשר לאופק ההלוואה. WALT של 3 שנים בהלוואה של 5 שנים = חידוש חוזים בתוך חיי
ההלוואה = סיכון שיש לנתח.
</p>

<p>
<strong>אשראי השוכר (Tenant Credit Quality):</strong> ציין אם לשוכרים העיקריים יש
דירוג אשראי פורמלי, דוחות כספיים ציבוריים, או שהם עסקים פרטיים לא מדורגים. שוכר
עם דירוג A- מהווה בטוחה חזקה הרבה יותר משוכר SME לא מדורג.
</p>

<h2>חולשות נפוצות בפרקי הלווה והנכס</h2>

<p>
להלן השגיאות שחוזרות שוב ושוב במזכרי אשראי:
</p>

<ul>
  <li><strong>שפה שיווקית:</strong> "נכס מצוין במיקום מבוקש" — ללא נתונים.</li>
  <li><strong>נתונים חסרים:</strong> אין WALT, אין פירוט שוכרים, אין CapEx.</li>
  <li><strong>ניסיון כללי:</strong> "יזם עם ניסיון של 20 שנה" — כמה פרויקטים? אילו
  סוגים? מה התוצאות?</li>
  <li><strong>אין השוואה לשוק:</strong> שכ"ד מוצג ללא השוואה ל-Market Rent. שווי מוצג
  ללא השוואת עסקאות דומות (Comparables).</li>
  <li><strong>מקורות לא מצוינים:</strong> מהיכן הגיע כל נתון? אם לא מצוין — קורא לא
  יכול לאמת.</li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #388e3c;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל מפתח — תיעוד מקורות:</strong><br>
  כל טענה עובדתית במזכר האשראי חייבת להיות מקושרת למסמך בתיק ה-Due Diligence.
  "שכ"ד 120 ₪/מ"ר/חודש (לפי חוזה שכירות עם חברה X, מצורף כנספח 3)." כך ניתן לאמת,
  וכך ועדת האשראי יודעת שהאנליסט לא המציא נתונים.
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
<h2>סיכום מודול 2 — כתיבת תיאור הלווה והנכס</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>רקע לווה = הערכת יכולת, לא ביוגרפיה:</strong> המטרה היא לענות על שאלה אחת:
    האם הלווה יעמוד בהתחייבויות? מבנה משפטי, ניסיון כמותי, חוזק פיננסי, ערבים —
    כולם צריכים לתמוך בתשובה.
  </li>
  <li>
    <strong>Track Record חייב להיות ספציפי:</strong> מספר פרויקטים, סוגים, עלויות,
    תוצאות, כשלים. "יזם מנוסה" ללא נתונים אינו ניתוח — הוא שיווק.
  </li>
  <li>
    <strong>תיאור נכס = בטוחה בכתב:</strong> מיקום, גודל, גיל, שוכרים עם % NOI ותאריכי
    פקיעה, CapEx אחרון. הנכס הוא מקור הפירעון הראשוני — תאורו חייב לאפשר הערכת שווי
    ונזילות.
  </li>
  <li>
    <strong>Class + WALT + אשראי שוכר = איכות נכס כמותית:</strong> Class A/B/C על פי
    מאפיינים מדידים. WALT ביחס לאופק ההלוואה. דירוג/יציבות שוכרים עיקריים.
  </li>
  <li>
    <strong>כל נתון — מקור:</strong> כל טענה עובדתית מקושרת למסמך בתיק ה-DD. ועדת
    האשראי יכולה לאמת. אנליסט שלא מצטט מקורות מוריד את אמינות המזכר כולו.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
תיארנו את הלווה ואת הנכס בצורה מקצועית ומבוססת נתונים. <em>מודול 3</em> יבנה
את הפרק הכמותי-טכני של המזכר: <strong>הניתוח הפיננסי</strong> — כיצד מציגים NOI
נורמלי, טבלת DSCR לאורך השנים, LTV, Debt Yield, ומה כל מדד אומר לוועדת האשראי.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (ניתוח פיננסי במזכר — NOI, DSCR, LTV)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>מבנה פרק הניתוח הפיננסי במזכר</h2>

<p>
פרק הניתוח הפיננסי הוא הליבה הטכנית של מזכר האשראי. הוא חייב להציג את הנתונים
בצורה מובנית, עקבית, וניתנת לאימות. הסדר הסטנדרטי:
</p>

<ol>
  <li>דוחות כספיים היסטוריים של הנכס (2–3 שנים אחורה)</li>
  <li>NOI מנורמל (Normalized NOI) — השנה הנוכחית</li>
  <li>DSCR — שנה נוכחית, שנה 1, שנה 2, שנה 3, תרחיש Stress</li>
  <li>LTV — לפי שומת הבנק</li>
  <li>Debt Yield — מדד בנקאי עצמאי</li>
  <li>ניתוח רגישות</li>
</ol>

<h2>נורמליזציה של NOI — מדוע ואיך</h2>

<p>
NOI "גולמי" מהדוחות הכספיים לעיתים קרובות מכיל פריטים חד-פעמיים, תשלומים חריגים
או הכנסות שאינן בנות-קיימא. <strong>NOI מנורמל</strong> הוא הנתון שמשקף את כוח הרווח
היציב של הנכס בנסיבות נורמליות.
</p>

<h3>התאמות נורמליזציה נפוצות:</h3>

<ul>
  <li>
    <strong>הסרת פריטים חד-פעמיים:</strong> פיצוי ביטוחי, תשלום עונש-יציאה מחד-פעמי
    מגורם שעזב — אלה אינם חוזרים.
  </li>
  <li>
    <strong>התאמת ריקנות:</strong> נכס שבוצע בו שיפוץ ועמד ריק 6 חודשים — ה-NOI של
    אותה שנה אינו מייצג. מנרמלים לתפוסה ייצוגית (לרוב שיעור ריקנות שוק אזורי).
  </li>
  <li>
    <strong>התאמת שכ"ד לשוק:</strong> אם שוכר עוגן משלם Over-Rented — ה-NOI הנוכחי
    גבוה מהמייצג. יש לחשב NOI פרו-פורמה לפי Market Rent.
  </li>
  <li>
    <strong>הוצאות חריגות:</strong> תיקון חירום חד-פעמי, הוצאה משפטית — מוסרים מ-NOI
    מנורמל (ומסבירים בפרק).
  </li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
דוגמה — נורמליזציה:<br><br>
NOI מדווח (2024): 4,200,000 ₪<br><br>
התאמות:<br>
  פיצוי ביטוחי חד-פעמי:    (-350,000 ₪)<br>
  שכ"ד Over-Rented שוכר A: (-280,000 ₪)  [Market Rent נמוך ב-280K]<br>
  ריקנות חריגה (Q1 שיפוץ): (+120,000 ₪)  [שנה עם ריקנות גבוהה מהרגיל]<br><br>
NOI מנורמל:                3,690,000 ₪<br><br>
הפרש: 510,000 ₪ — 12% מהנתון המדווח.<br>
אנליסט שמשתמש ב-NOI גולמי מגזים ב-DSCR ב-14%.
</div>

<h2>טבלת DSCR — איך מציגים בצורה נכונה</h2>

<p>
ועדת האשראי לא רוצה DSCR אחד — היא רוצה לראות את <strong>מסלול ה-DSCR לאורך זמן</strong>
וגם את ביצועיו תחת Stress. הצגה סטנדרטית:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">שנה</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">NOI (₪)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">שירות חוב (₪)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">DSCR</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הערות</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שנה נוכחית (מנורמל)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3,690,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2,800,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.32</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בסיס מנורמל</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שנה 1</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3,760,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2,800,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.34</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הצמדה +2% NOI</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שנה 2</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3,835,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2,800,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.37</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הצמדה +2% NOI</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שנה 3</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3,910,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2,800,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.40</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הצמדה +2% NOI</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;font-weight:bold;">Stress (+200bps)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;font-weight:bold;">3,320,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;font-weight:bold;">3,360,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;font-weight:bold;color:#c62828;">0.99</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;font-weight:bold;">NOI -10%, ריבית +200bps</td>
    </tr>
  </tbody>
</table>

<p>
<strong>פרשנות הטבלה:</strong> בתרחיש הבסיס, ה-DSCR עולה עם הזמן — בריא. אך תחת Stress
הוא יורד מתחת ל-1.0 — אות אדום. ועדת האשראי רואה את זה בשנייה אחת.
</p>

<h2>LTV — איזו שומה להשתמש</h2>

<p>
<strong>LTV (Loan to Value)</strong> = סכום ההלוואה / שווי הנכס.
</p>

<p>
נקודה קריטית: <strong>הלווה מגיש שומה משלו</strong> — שמאי שהלווה שכר, ולעיתים
עם תוצאה "נוחה" לעסקה. הבנק חייב להשתמש ב<strong>שומה עצמאית שהבנק הזמין</strong>,
לא בשומת הלווה. אם יש פער בין השניים — ציין את שתיהן במזכר ונמק.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
דוגמה — חישוב LTV:<br><br>
סכום הלוואה מבוקש: 28,000,000 ₪<br><br>
שומת הלווה:     42,000,000 ₪  →  LTV = 28/42 = 66.7%<br>
שומת הבנק:      38,000,000 ₪  →  LTV = 28/38 = 73.7%<br><br>
פער: 7.0 נקודות אחוז — משמעותי.<br>
מדיניות מקסימום LTV בבנק: 70%.<br><br>
מסקנה: לפי שומת הלווה — תוך המגבלה. לפי שומת הבנק — חריגה.<br>
במזכר: יש לדווח על שתי השומות ולציין את החריגה.
</div>

<h2>Debt Yield — מדד עצמאי מ-Cap Rate</h2>

<p>
<strong>Debt Yield = NOI / סכום ההלוואה</strong>
</p>

<p>
זהו מדד שמדוד את <strong>כוח הכנסה של הנכס ביחס לחוב</strong>, ללא תלות בהנחות שווי.
בניגוד ל-LTV שמושפע מ-Cap Rate (שינוי הנחת ה-Cap Rate משנה LTV ללא שינוי בנכס
עצמו), Debt Yield מבוסס על NOI בלבד — שניתן לאמת ממישהו עצמאי.
</p>

<div style="background:#e8f5e9;border-right:5px solid #388e3c;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>Debt Yield = NOI / סכום ההלוואה</strong><br><br>
  המדד אינו מושפע מהנחת ה-Cap Rate. אם מישהו "מניח" Cap Rate נמוך כדי להעלות שווי
  ולהוריד LTV — Debt Yield לא משתנה. לכן בנקים רבים קובעים רף מינימלי ל-Debt Yield
  (לרוב 8%–10% בשוק הישראלי) כתנאי עצמאי לאישור.
</div>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
דוגמה — Debt Yield:<br><br>
NOI מנורמל: 3,690,000 ₪<br>
הלוואה: 28,000,000 ₪<br><br>
Debt Yield = 3,690,000 / 28,000,000 = 13.2%<br><br>
פרשנות: כל שקל שהבנק הלווה מייצר 13.2 אגורות NOI לשנה.<br>
Debt Yield &gt; 10% = טוב. Debt Yield &lt; 8% = אות אזהרה.
</div>

<h2>כיצד להציג מספרים בצורה נכונה</h2>

<p>
עקרונות הצגה של נתונים פיננסיים במזכר:
</p>

<ul>
  <li>
    <strong>עיגול לאלפים:</strong> "3,690,000 ₪" — לא "3,692,847 ₪". דיוק מדומה מוריד
    אמינות, לא מעלה אותה.
  </li>
  <li>
    <strong>שינויים באחוזים:</strong> כל שינוי NOI בין שנים מוצג גם בערך מוחלט וגם באחוז.
    "+70,000 ₪ (+1.9%)" — ברור.
  </li>
  <li>
    <strong>ספי Covenant:</strong> מסמן בטבלה את רף ה-DSCR המינימלי (למשל 1.20). קורא
    רואה מיד מתי הנכס מתקרב לסף.
  </li>
  <li>
    <strong>עמודת "הערות":</strong> כל שורה בטבלת DSCR מוסברת. לא מספיק רק מספרים —
    הקורא צריך לדעת מה הניע את השינוי.
  </li>
</ul>

<h2>גשר לניתוח הסיכונים</h2>

<p>
הניתוח הפיננסי שבנינו — NOI מנורמל, DSCR לאורך שנים, LTV, Debt Yield — מהווה את
הבסיס הכמותי לפרק הסיכונים. פרק הסיכונים ישאל: מה יכול לפגוע ב-DSCR? מה יכול
לשנות את ה-LTV? ולכל גורם כזה — מה מנגנון המיתיגציה? מודול 4 יבנה את פרק ניתוח
הסיכונים ומנגנוני המיתיגציה במלואו.
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
<h2>סיכום מודול 3 — ניתוח פיננסי במזכר: NOI, DSCR, LTV</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>NOI מנורמל — לא NOI גולמי:</strong> הסרת פריטים חד-פעמיים, התאמת ריקנות
    חריגה ושכ"ד Over-Rented נותנת את NOI המייצג. שימוש ב-NOI גולמי עלול להגזים ב-DSCR
    ב-10%–15%.
  </li>
  <li>
    <strong>טבלת DSCR רב-שנתית + Stress:</strong> ועדת האשראי רוצה לראות את מסלול ה-DSCR
    לאורך זמן וגם תחת תרחיש Stress (+200bps ריבית, -10% NOI). טבלה אחת עם חמש שורות
    אומרת יותר מעמוד של טקסט.
  </li>
  <li>
    <strong>LTV — שומת הבנק, לא שומת הלווה:</strong> הלווה תמיד ינסה למקסם שווי. הבנק
    חייב שומה עצמאית. אם יש פער — מדווחים על שניהם ומסבירים. מדיניות ה-LTV נבדקת
    מול שומת הבנק, לא שומת הלווה.
  </li>
  <li>
    <strong>Debt Yield — מדד עצמאי מ-Cap Rate:</strong> NOI חלקי סכום ההלוואה. לא מושפע
    מהנחות שווי. רף 8%–10% כתנאי מינימלי עצמאי לאישור. Debt Yield נמוך מ-8% = נכס
    שמייצר מעט מאוד הכנסה ביחס לחוב.
  </li>
  <li>
    <strong>הצגת מספרים:</strong> עיגול לאלפים, שינויים באחוזים, ספי Covenant מסומנים
    בטבלה, עמודת "הערות" לכל שורה. המספרים חייבים לספר סיפור — לא להיות מטריצה של
    ספרות.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
בנינו את שלד המזכר: מבנה כללי (מודול 1), פרקי הלווה והנכס (מודול 2), וניתוח פיננסי
מלא (מודול 3). <em>מודול 4</em> ישלים את המזכר עם <strong>פרק ניתוח הסיכונים
ומיתיגציה</strong> — כיצד מציגים את מטריצת הסיכונים, מנסחים Covenant Packages
ומבנים את סעיף ההמלצה הסופי.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = "Seeds Module 1-3 reading and summary content for Course 11 (כתיבת מזכר אשראי)"

    def handle(self, *args, **options) -> None:
        # ── Locate Course 11 ──────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=11)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=11 not found. "
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
            self.style.SUCCESS("\nAll done — Course 11 modules 1-3 seeded successfully.")
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
