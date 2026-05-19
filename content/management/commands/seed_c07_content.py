"""
Seeds Module 1-3 content for Course 7 (ניהול סיכונים בנדל"ן).
Usage: python manage.py seed_c07_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": 'זיהוי וסיווג סיכונים בנדל"ן',
        "slug": "zihuy-vsivug-sikuim",
        "estimated_minutes": 50,
    },
    {
        "module_number": 2,
        "title_he": "סיכון ריבית וסיכון מימון מחדש",
        "slug": "sikun-ribit-mimun-mehadash",
        "estimated_minutes": 55,
    },
    {
        "module_number": 3,
        "title_he": "סיכוני שוק, תפוסה ותזרים",
        "slug": "sikune-shuk-tefusa-tizrim",
        "estimated_minutes": 50,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (זיהוי וסיווג סיכונים בנדל"ן)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>זיהוי וסיווג סיכונים בנדל"ן — המפה המלאה</h2>

<p>
אנליסט אשראי בתחום הנדל"ן אינו פותח תיק הלוואה כדי לאשר — הוא פותחו כדי להבין מה יכול
להשתבש. ניהול סיכונים מקצועי מתחיל בזיהוי שיטתי של כל הסיכונים הרלוונטיים, המשך בסיווגם
לפי חומרה ולאחר מכן בניית מנגנוני מיתיגציה מתאימים. מודול זה מציג את מפת הסיכונים המלאה
של עסקאות מימון נדל"ן.
</p>

<h2>טקסונומיה של סיכוני נדל"ן — שש משפחות</h2>

<p>
הסיכונים בעסקאות מימון נדל"ן מתחלקים לשש משפחות עיקריות. כל משפחה כוללת מספר סיכונים
ספציפיים שעל האנליסט לשקול ולמדוד:
</p>

<h3>1. סיכון שוק (Market Risk)</h3>
<p>
סיכון שוק הוא הסיכון לירידת שווי הנכס או ירידת הכנסות הנכס בשל שינויים בסביבה הכלכלית.
הוא כולל: ירידת מחירי נכסים, ירידת שכר דירה בשוק, עלייה בשיעורי הריקנות הכלל-ענפיים
ושינויים בביקוש לסוגי נכסים שונים.
</p>

<h3>2. סיכון נזילות (Liquidity Risk)</h3>
<p>
הסיכון שהנכס לא ניתן למכירה במהירות סבירה במחיר שוק הוגן. נכסים ייחודיים (כגון מפעלים,
מחסנים ייעודיים), נכסים באזורי פריפריה, ונכסים גדולים מאוד סובלים מנזילות נמוכה יותר.
נזילות נמוכה מקשה על המלווה לממש בטחונות בתרחיש כשל.
</p>

<h3>3. סיכון ריבית (Interest Rate Risk)</h3>
<p>
הסיכון לעלייה בריבית שמגדילה את נטל שירות החוב ופוגעת ביכולת הפירעון של הלווה. בישראל,
עסקאות רבות צמודות לריבית הפריים — שינוי של 200 נקודות בסיס בפריים מגדיל עלות חוב של
10M₪ ב-200,000 ₪ לשנה.
</p>

<h3>4. סיכון מימון מחדש (Refinancing Risk)</h3>
<p>
הסיכון שבפקיעת הלוואת Bullet הלווה לא יצליח לגייס מימון חלופי — בשל הידוק אשראי בשוק,
ירידת שווי הנכס, או הרעה בפרופיל האשראי של הלווה. בלא מימון מחדש, הלווה חייב לפרוע
את מלוא הקרן ביום הפקיעה — לעיתים ללא יכולת לעשות כן.
</p>

<h3>5. סיכון בנייה והשלמה (Construction / Completion Risk)</h3>
<p>
רלוונטי בפרויקטי ייזום ובינוי: עיכוב בהשלמה, חריגה בתקציב, קבלן ראשי שקורס, שינוי
דרישות רגולטוריות או קשיים בקבלת היתרים. נכס שלא הושלם אינו מייצר הכנסות — כלומר,
שירות החוב חייב לבוא ממקורות חיצוניים עד להשלמה.
</p>

<h3>6. סיכון רגולטורי ומשפטי (Regulatory / Legal Risk)</h3>
<p>
שינויי חקיקה (מס שבח, מס רכישה, חוקי שכירות), שינוי תוכניות בניין עיר (תב"ע), ליטיגציה
(תביעות שוכרים, שכנים, ספקים), בעיות בעלות ורישום בטאבו, ושיעבודים לא גלויים על הנכס.
</p>

<h2>סיכון הלווה / אשראי (Borrower / Credit Risk)</h2>

<p>
מעבר לסיכוני הנכס, קיים <strong>סיכון הלווה</strong> — הסיכון שהלווה עצמו לא יוכל לעמוד
בתשלומים גם אם הנכס בריא. זה כולל: כישלון עסקי, מינוף יתר בשאר הפעילות, בעיות תזרים
בחברות אחרות, ניהול לקוי. בישראל, יזמים רבים מנהלים מספר פרויקטים בו-זמנית — כשל
בפרויקט אחד עלול "להדביק" אחרים.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — מיפוי סיכונים בפרויקט:</strong><br><br>
  פרויקט: מרכז מסחרי חדש, עלות 50M₪, מימון בנקאי 35M₪ (LTV 70%), אזור פריפריה.<br><br>
  מיפוי ראשוני:<br>
  • סיכון שוק — גבוה (ביקוש מסחרי בפריפריה לא ודאי)<br>
  • סיכון נזילות — גבוה (נכס ייעודי, שוק קטן)<br>
  • סיכון ריבית — בינוני (הלוואה צמודת פריים)<br>
  • סיכון בנייה — גבוה (פרויקט בשלב ייזום)<br>
  • סיכון רגולטורי — נמוך (היתרים קיימים)<br>
  • סיכון לווה — בינוני (יזם עם 2 פרויקטים נוספים)
</div>

<h2>מטריצת סיכונים — הסתברות × השפעה</h2>

<p>
לאחר זיהוי הסיכונים, האנליסט ממפה כל סיכון לפי שני ממדים: <strong>הסתברות להתממשות</strong>
ו<strong>השפעה על עסקה</strong> (אם יתממש). המכפלה נותנת את ה<strong>חשיפה המשוקללת</strong>
— הסיכון הכולל.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">סיכון</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הסתברות (1-5)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">השפעה (1-5)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ציון כולל (מכפלה)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">עדיפות</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון שוק</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">4</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">12</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גבוהה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון ריבית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">9</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בינונית</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון בנייה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גבוהה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון נזילות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">4</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">8</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בינונית</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון רגולטורי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נמוכה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון לווה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">4</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">8</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בינונית</td>
    </tr>
  </tbody>
</table>

<p>
<strong>שימוש במטריצה:</strong> סיכונים עם ציון כולל של 10 ומעלה דורשים מיתיגציה פעילה
(בטחונות נוספים, Covenant, תנאי מקדים). סיכונים בציון 5–9 נדרשים למעקב שוטף ו-Covenant
מדיד. סיכונים בציון מתחת ל-5 מספיק לתעד ב-Credit Memo.
</p>

<h2>כיצד אנליסט ממפה וממשקל סיכונים — תהליך עבודה</h2>

<ul>
  <li>
    <strong>שלב 1 — רשימה ראשונית:</strong> עבור כל עסקה, הכן רשימת "כל הסיכונים שיכולים
    לפגוע בפירעון" — ללא סינון. פרס מהרחב לצר.
  </li>
  <li>
    <strong>שלב 2 — ניקוד:</strong> לכל סיכון — הסתברות (1=נדיר, 5=כמעט ודאי) והשפעה
    (1=שולית, 5=קטלנית לעסקה). חשב מכפלה.
  </li>
  <li>
    <strong>שלב 3 — עדיפות:</strong> דרג את הסיכונים לפי ציון כולל. הצבע את 3-5 הסיכונים
    הגבוהים כ"סיכונים מהותיים" שדורשים טיפול ב-Credit Memo.
  </li>
  <li>
    <strong>שלב 4 — מיתיגציה:</strong> לכל סיכון מהותי — הגדר את מנגנון המיתיגציה המתאים:
    בטחון ספציפי, Covenant פיננסי, תנאי מקדים, ביטוח.
  </li>
  <li>
    <strong>שלב 5 — תיעוד:</strong> כלול את מטריצת הסיכונים ב-Credit Memo. ועדת האשראי
    רואה את הסיכונים — לא רק את נתוני הבסיס.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — סיכונים נסתרים:</strong><br>
  המסוכנים ביותר הם הסיכונים שלא ידועים מראש: בעיות בטאבו שלא נבדקו, חריגת בנייה
  לא מדווחת, שוכר עוגן שחוזה השכירות שלו עומד לפוג, זיהום קרקע שלא גולה. הכלל:
  <strong>תמיד כלול בתהליך ה-Due Diligence בדיקת טאבו מלאה, שמאות עצמאית, בדיקה
  הנדסית ואישור עורך דין על נקיון הבעלות.</strong> אל תסמוך על הצהרות הלווה בלבד.
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Comprehension HTML
# ---------------------------------------------------------------------------

M1_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על זיהוי וסיווג סיכונים בנדל"ן — בחן את הבנתך לפני שממשיכים.
השאלות בוחנות את שש משפחות הסיכון, שימוש במטריצת הסתברות × השפעה, תהליך מיפוי
סיכונים מעשי, וזיהוי סיכונים נסתרים בתרחישים נתונים.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Exercises HTML
# ---------------------------------------------------------------------------

M1_EXERCISES_HTML = """
<p>
5 תרגילים על מיפוי וסיווג סיכונים. התרגילים כוללים בניית מטריצת סיכונים לעסקה נתונה,
דירוג סיכונים לפי הסתברות והשפעה, זיהוי הסיכון הדומיננטי בתרחיש פרויקט ייזום,
השוואת פרופילי סיכון בין נכס מניב לנכס בייזום, ותכנון מנגנוני מיתיגציה לסיכונים מהותיים.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — זיהוי וסיווג סיכונים בנדל"ן</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>שש משפחות סיכון:</strong> שוק, נזילות, ריבית, מימון מחדש, בנייה/השלמה, רגולטורי/משפטי —
    בנוסף לסיכון הלווה. כל עסקה מתאפיינת בתמהיל שונה של סיכונים לפי סוג הנכס ושלב הפרויקט.
  </li>
  <li>
    <strong>מטריצת סיכונים:</strong> ניקוד הסתברות (1–5) × השפעה (1–5) = ציון כולל. ציון 10+
    = סיכון מהותי שדורש מיתיגציה פעילה ותיעוד ב-Credit Memo.
  </li>
  <li>
    <strong>תהליך מיפוי:</strong> רשימה רחבה → ניקוד → עדיפות → מיתיגציה → תיעוד. תהליך
    שיטתי מונע השמטת סיכונים חשובים ומבטיח שועדת האשראי רואה את התמונה המלאה.
  </li>
  <li>
    <strong>סיכון הלווה:</strong> נפרד מסיכוני הנכס — יזם עם מינוף יתר בפרויקטים אחרים עלול
    להכשיל עסקה בריאה. תמיד נתח את מצבו הכולל של הלווה, לא רק את הפרויקט הספציפי.
  </li>
  <li>
    <strong>סיכונים נסתרים:</strong> הסיכונים המסוכנים ביותר הם אלה שלא נחשפו בתהליך
    בדיקת הנאותות. Due Diligence מקיף — טאבו, שמאות, הנדסה, משפט — הוא הכלי הראשי.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
מיפינו את כלל הסיכונים ולמדנו לדרגם. <em>מודול 2</em> יצלול לעומק לשני מהסיכונים
המשמעותיים ביותר בשוק הישראלי: <strong>סיכון ריבית וסיכון מימון מחדש</strong> —
כיצד הם נמדדים, מה כלי הגידור הנפוצים, וכיצד מבצעים Stress Test על DSCR.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (סיכון ריבית וסיכון מימון מחדש)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>סיכון ריבית וסיכון מימון מחדש — שני הסיכונים הפיננסיים המרכזיים</h2>

<p>
בעסקאות מימון נדל"ן בישראל, שני הסיכונים הפיננסיים שמשפיעים ישירות על יכולת שירות
החוב הם סיכון ריבית וסיכון מימון מחדש. אנליסט אשראי שאינו בוחן אותם ספציפית — מפספס
את החלק הדינמי של ניתוח ההלוואה.
</p>

<h2>סיכון ריבית — ריבית קבועה מול ריבית משתנה</h2>

<p>
<strong>הלוואה בריבית קבועה:</strong> הריבית נקבעת ביום ההלוואה ואינה משתנה לאורך חיי
ההלוואה. הלווה יודע מראש בדיוק מה עלות החוב שלו. המלווה נושא בסיכון ריבית — אם הריבית
עולה, הוא לא יכול לדרוש יותר.
</p>

<p>
<strong>הלוואה בריבית משתנה (Floating Rate):</strong> הריבית צמודה לריבית בסיס — בישראל
לרוב <strong>ריבית הפריים</strong> (Prime Rate), שקבועה על ידי בנק ישראל ועדכנית בכל
שינוי ריבית. הלווה נושא בסיכון ריבית — כאשר הפריים עולה, תשלום הריבית שלו עולה.
</p>

<h3>פריים בישראל — הבסיס לעסקאות נדל"ן:</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ריבית הפריים = ריבית בנק ישראל + 1.5%<br><br>
דוגמה (2024-2025):<br>
ריבית בנק ישראל: 4.5%<br>
ריבית הפריים:    4.5% + 1.5% = 6.0%<br><br>
הלוואה P+2%:     6.0% + 2.0% = 8.0% לשנה<br><br>
אם בנק ישראל מעלה ל-5.5%:<br>
פריים חדש:       5.5% + 1.5% = 7.0%<br>
הלוואה P+2%:     7.0% + 2.0% = 9.0% לשנה<br><br>
עלייה בעלות חוב של 10M₪: 10,000,000 × 1% = 100,000 ₪ נוספים לשנה
</div>

<h2>מח"מ ופער מח"מ (Duration Mismatch)</h2>

<p>
<strong>מח"מ (Duration)</strong> הוא משך החיים הממוצע המשוקלל של תזרימי המזומנים —
מושג מעולם האג"ח שמשמש גם לניתוח הלוואות. הסיכון מתממש כאשר יש <strong>פער מח"מ
(Duration Mismatch)</strong> בין הנכס לבין ההתחייבות שמממנת אותו:
</p>

<ul>
  <li><strong>נכס בעל מח"מ ארוך:</strong> חוזי שכירות ל-10+ שנים, שווי שוק שיורד ממש
  רק בטווח ארוך.</li>
  <li><strong>הלוואה בריבית משתנה לטווח קצר:</strong> חשיפה לריבית מתחדשת תכופות.</li>
  <li><strong>הפער:</strong> הכנסות הנכס (שכירות) קבועות לפי חוזה; עלות החוב עולה עם
  הפריים — ה-DSCR נפגע.</li>
</ul>

<h2>כלי גידור סיכון ריבית</h2>

<h3>1. ריבית קבועה — הגידור הפשוט</h3>
<p>
הלווה לוקח הלוואה בריבית קבועה שנקבעת מראש. כל עלייה עתידית בפריים אינה משפיעה עליו.
החסרון: ריבית קבועה גבוהה יותר מריבית משתנה ביום ההלוואה (בגלל פרמיית הסיכון שהמלווה
גובה על אי-ודאות עתידית).
</p>

<h3>2. Interest Rate Swap (IRS) — החלפת ריבית</h3>
<p>
הלווה לוקח הלוואה בריבית משתנה (P+2%), ובמקביל כורת חוזה Swap עם בנק: הלווה משלם
לבנק ריבית קבועה (למשל 6.5%), ומקבל מהבנק ריבית משתנה (Pריים). התוצאה נטו: הלווה
עומד בריבית קבועה אפקטיבית בלי שנה ההלוואה עצמה.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — IRS:</strong><br><br>
  הלוואה: 20,000,000 ₪ בפריים + 2% (כיום = 8%)<br>
  IRS: הלווה משלם 7% קבוע לבנק ה-Swap, מקבל פריים (6%)<br><br>
  תשלום נטו של הלווה:<br>
  • לבנק המלווה: פריים + 2% = 8%<br>
  • ל-Swap: 7% - פריים (6%) = 1%<br>
  • סה"כ: 8% + 1% = 9% — ריבית אפקטיבית קבועה<br><br>
  אם פריים עולה ל-8%: הלווה משלם P+2%=10%, אך מקבל מה-Swap פריים=8% ומשלם 7%
  → נטו = 10% - (8%-7%) = 9%. הריבית האפקטיבית נשארת 9% — הגידור עבד.
</div>

<h3>3. CAP Agreement — רצפת הגנה</h3>
<p>
הלווה רוכש חוזה CAP מגוף פיננסי: אם ריבית הפריים תעלה מעל "רצפה" מוסכמת (CAP Level,
למשל 7%), הלווה יקבל פיצוי על ההפרש. הלווה משלם פרמיה חד-פעמית מראש תמורת ההגנה.
</p>

<ul>
  <li><strong>יתרון:</strong> הלווה נהנה מריבית נמוכה כשהפריים נמוך (לא כמו ב-IRS שנועל ריבית).</li>
  <li><strong>חיסרון:</strong> עלות הפרמיה — בתרחיש של ריבית שיורדת, שילמת על הגנה שלא הייתה
  נחוצה.</li>
  <li><strong>נפוץ ב:</strong> הלוואות עם ציפייה לירידת ריבית, הלוואות עם אופק קצר.</li>
</ul>

<h2>סיכון מימון מחדש (Refinancing Risk)</h2>

<p>
עסקאות נדל"ן רבות ממומנות ב<strong>הלוואות Bullet</strong> — הקרן כולה נפרעת ביום הפקיעה
(Maturity), ובמהלך ההלוואה משולמים רק ריבית (וחלק קטן מקרן, בתלות במבנה). ביום הפקיעה,
הלווה חייב לפרוע את כל הקרן — לרוב על ידי מחזור (Refinancing) ההלוואה אצל מלווה חדש
או בתנאים חדשים.
</p>

<h3>מתי סיכון מימון מחדש מתממש?</h3>
<ul>
  <li><strong>הידוק אשראי בשוק:</strong> בנקים מצמצמים מתן הלוואות (כפי שקרה ב-2008,
  ב-COVID). גם לווים טובים מתקשים לגייס מימון.</li>
  <li><strong>ירידת שווי נכס:</strong> LTV בעת המחזור גבוה מדי — הבנק לא ייתן מימון
  חדש ב-70% LTV אם שווי הנכס ירד ב-20%.</li>
  <li><strong>הרעת פרופיל הלווה:</strong> דירוג אשראי נמוך יותר, הפרות Covenant בעבר,
  כשל בפרויקט אחר — פוגעים ביכולת גיוס מחדש.</li>
  <li><strong>עלייה בריבית:</strong> תנאי מחזור יקרים בהרבה מהמקור — DSCR יורד.</li>
</ul>

<h3>Extension Options — אפשרות הארכה</h3>
<p>
כלי להפחתת סיכון מימון מחדש: ב-Term Sheet ניתן לנהל משא ומתן על <strong>Extension Option</strong>
— זכות הלווה להאריך את ההלוואה ב-1–2 שנים נוספות בהתקיים תנאים מסוימים (DSCR מינימלי,
LTV מקסימלי, ללא הפרות Covenant).
</p>

<ul>
  <li><strong>מחיר ה-Extension:</strong> לרוב Extension Fee (0.25%–0.5% מהקרן) ועלייה
  בשולי הריבית.</li>
  <li><strong>מבחינת המלווה:</strong> Extension נוח — לא צריך לגבש מחזור חדש, לווה מוכר,
  הכנסה מהפרמיה.</li>
  <li><strong>מבחינת הלווה:</strong> Extension נותן "מרווח נשימה" כשתנאי השוק לא נוחים
  למחזור.</li>
</ul>

<h2>Stress Test — DSCR עם עלייה של 200bps בפריים</h2>

<p>
אחד הבדיקות הסטנדרטיות שמלווים דורשים היא <strong>Stress Test על ריבית</strong>:
מה קורה ל-DSCR אם הפריים עולה ב-200 נקודות בסיס (2%)?
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
נתוני בסיס:<br>
הלוואה: 30,000,000 ₪ בפריים + 2% (ריבית כיום: 8%)<br>
NOI נכס: 3,000,000 ₪ לשנה<br>
שירות חוב (ריבית בלבד, Bullet): 30,000,000 × 8% = 2,400,000 ₪<br>
DSCR בסיס = 3,000,000 / 2,400,000 = 1.25<br><br>
Stress Test +200bps:<br>
ריבית חדשה: 8% + 2% = 10%<br>
שירות חוב חדש: 30,000,000 × 10% = 3,000,000 ₪<br>
DSCR תחת Stress = 3,000,000 / 3,000,000 = 1.00<br><br>
מסקנה: ב-Stress, הנכס בקושי מכסה את הריבית — ללא כרית. אם NOI ירד גם הוא ב-5%,
DSCR יהיה 0.95 — מתחת ל-1.0, כלומר הנכס לא מכסה את שירות החוב.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — Stress Test הוא חובה, לא אופציה:</strong><br>
  כל Credit Memo על הלוואה בריבית משתנה חייב לכלול Stress Test של +200bps לפחות.
  הלווה שמציג DSCR של 1.25 בבסיס ו-1.00 תחת Stress — עומד בדרישה המינימלית, אך ללא
  כרית. <strong>הגדר Covenant שמחייב DSCR מינימלי של 1.10 גם תחת Stress — ואם לא
  עומד, זהו אות אדום לאישור ההלוואה.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Comprehension HTML
# ---------------------------------------------------------------------------

M2_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על סיכון ריבית ומימון מחדש — בחן את יכולתך לחשב את השפעת שינוי פריים
על DSCR, לפרש מנגנוני IRS ו-CAP, לזהות גורמי סיכון מימון מחדש ולהעריך ערך Extension Option.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Exercises HTML
# ---------------------------------------------------------------------------

M2_EXERCISES_HTML = """
<p>
5 תרגילים על סיכון ריבית ומימון מחדש. התרגילים כוללים חישוב DSCR בתרחיש Stress של
+150bps ו-+300bps, ניתוח עלות IRS מול ריבית קבועה ישירה, הערכת Extension Option
בתרחיש שוק מהודק, ניתוח Duration Mismatch בין חוזי שכירות לטווח ההלוואה.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — סיכון ריבית וסיכון מימון מחדש</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>ריבית קבועה מול פריים:</strong> הלוואות בפריים חושפות את הלווה לסיכון ריבית.
    כל עלייה של 100bps בפריים = 1% נוסף על קרן ההלוואה לשנה. בהלוואה של 20M₪ — 200,000 ₪
    נוספים לשנה שחייבים להגיע מ-NOI הנכס.
  </li>
  <li>
    <strong>Duration Mismatch:</strong> נכס עם חוזי שכירות ארוכים (הכנסה קבועה) וממומן
    בהלוואה קצרת-מח"מ בריבית משתנה — פגיע במיוחד לעלייה בריבית. הפער בין מח"מ הנכס
    למח"מ ההתחייבות הוא גורם סיכון ראשוני לניתוח.
  </li>
  <li>
    <strong>כלי גידור:</strong> IRS (ריבית קבועה נטו), CAP (הגנה חד-כיוונית). IRS מתאים
    ללווים שרוצים ודאות מלאה; CAP מתאים למי שמאמין שהריבית לא תעלה מעל רף מסוים.
  </li>
  <li>
    <strong>סיכון מימון מחדש:</strong> הלוואות Bullet מחייבות מחזור ביום הפקיעה.
    הידוק אשראי, ירידת שווי נכס או הרעת פרופיל לווה עלולים למנוע מחזור — ולהפוך
    הלוואה תקינה לחדלת פירעון ביום אחד.
  </li>
  <li>
    <strong>Stress Test:</strong> בדיקת DSCR תחת +200bps בפריים היא חובה בכל Credit Memo
    על הלוואה בריבית משתנה. DSCR מתחת ל-1.10 תחת Stress = אות אדום שדורש מיתיגציה.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
ניתחנו את הסיכונים הפיננסיים — ריבית ומימון מחדש. <em>מודול 3</em> ישלים את תמונת
הסיכון עם <strong>סיכוני השוק, התפוסה והתזרים</strong>: כיצד ריקנות משפיעה על NOI,
מה WALT אומר על יציבות ההכנסה, וכיצד מחשבים Break-Even Occupancy.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (סיכוני שוק, תפוסה ותזרים)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>סיכוני שוק, תפוסה ותזרים — הסיכונים התפעוליים של הנכס</h2>

<p>
גם כאשר הריבית יציבה ומימון מחדש אינו בסכנה, נכס יכול להכשיל הלוואה בשל סיבות תפעוליות:
ריקנות גבוהה, שוכר עוגן שעוזב, ירידת שכר הדירה בשוק. אלו הם סיכוני השוק, התפוסה
והתזרים — המשקפים את ביצועי הנכס בפועל.
</p>

<h2>סיכון ריקנות (Vacancy Risk)</h2>

<p>
<strong>ריקנות מבנית:</strong> נובעת ממאפייני הנכס עצמו — מיקום לקוי, מפרט ישן, גודל
שאינו מתאים לביקוש הקיים. ריקנות מבנית קשה לתיקון ללא השקעה הונית (שיפוץ, שדרוג).
</p>

<p>
<strong>ריקנות מחזורית:</strong> נובעת ממחזור הכלכלה — בעת מיתון ביקוש לשטחים מסחריים,
משרדים ומחסנים יורד. ריקנות מחזורית בדרך כלל הפיכה, אך תהליך מילוי שטחים לוקח 12–24 חודשים.
</p>

<h3>השפעת ריקנות על NOI:</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
נכס משרדים — 5,000 מ"ר, שכ"ד שוק 120 ₪/מ"ר/חודש:<br><br>
תרחיש 1 (תפוסה 95%): 5,000 × 0.95 × 120 × 12 = 6,840,000 ₪ לשנה<br>
תרחיש 2 (תפוסה 80%): 5,000 × 0.80 × 120 × 12 = 5,760,000 ₪ לשנה<br>
תרחיש 3 (תפוסה 70%): 5,000 × 0.70 × 120 × 12 = 5,040,000 ₪ לשנה<br><br>
ירידה מ-95% ל-70% תפוסה = ירידת NOI של 1,800,000 ₪ — 26% מהכנסות
</div>

<h2>WALT — Weighted Average Lease Term</h2>

<p>
<strong>WALT</strong> (Weighted Average Lease Term) הוא מדד לבשלות ממוצעת משוקללת של
חוזי השכירות בנכס, כשהמשקל הוא חלקו של כל שוכר מסך ה-NOI (או השטח). WALT גבוה =
הכנסה יציבה לטווח ארוך; WALT נמוך = סיכון מחזור שוכרים בטווח הקרוב.
</p>

<h3>חישוב WALT:</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
נכס עם 3 שוכרים:<br><br>
שוכר A: 2,000 מ"ר × 130 ₪/מ"ר/חודש = 260,000 ₪/חודש; 4 שנים לפקיעה<br>
שוכר B: 1,500 מ"ר × 110 ₪/מ"ר/חודש = 165,000 ₪/חודש; 2 שנים לפקיעה<br>
שוכר C: 1,000 מ"ר × 100 ₪/מ"ר/חודש = 100,000 ₪/חודש; 7 שנים לפקיעה<br>
סה"כ NOI חודשי: 525,000 ₪<br><br>
WALT = (260,000/525,000 × 4) + (165,000/525,000 × 2) + (100,000/525,000 × 7)<br>
WALT = (0.495 × 4) + (0.314 × 2) + (0.190 × 7)<br>
WALT = 1.98 + 0.629 + 1.333 = 3.94 שנים<br><br>
פרשנות: בממוצע, חוזי השכירות פוקעים עוד ~4 שנים. אם ההלוואה היא ל-5 שנים,
יש חשיפה לחידוש חוזים לפני פקיעת ההלוואה.
</div>

<h2>סיכון ריכוז שוכרים (Tenant Concentration Risk)</h2>

<p>
<strong>שוכר עוגן (Anchor Tenant)</strong> הוא שוכר שמהווה חלק גדול מ-NOI הנכס — לעיתים
30%–60% מסך ההכנסות. תלות גבוהה בשוכר עוגן יוצרת סיכון ריכוז: עזיבת שוכר העוגן עלולה
להפיל את ה-DSCR מתחת לסף המינימלי.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">סיכון ריכוז</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">אחוז מ-NOI</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הערכת סיכון</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מיתיגציה מומלצת</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שוכר אחד &gt; 50%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">50%+</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גבוה מאוד</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח יציבות שוכר, LTV נמוך</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שוכר אחד 30%–50%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">30%–50%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גבוה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Covenant DSCR קפדני</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שוכר מוביל 15%–30%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">15%–30%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בינוני</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מעקב שנתי על חידוש חוזה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פיזור רחב — כ"א &lt;15%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">&lt;15%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נמוך</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בדיקה שגרתית</td>
    </tr>
  </tbody>
</table>

<h2>פער בין שכ"ד שוק לשכ"ד בחוזה (Market Rent vs. Passing Rent)</h2>

<p>
<strong>Passing Rent</strong> הוא שכר הדירה שהשוכר משלם בפועל לפי החוזה הקיים.
<strong>Market Rent</strong> הוא שכר הדירה שניתן לקבל בשוק למ"ר דומה היום.
הפער ביניהם חשוב לניתוח:
</p>

<ul>
  <li>
    <strong>Passing Rent &lt; Market Rent (Under-Rented):</strong> השוכר שמח — שכ"ד שלו
    זול מהשוק. לחידוש חוזה תהיה עלייה — טוב לנכס. אך אם השוכר יעזוב, שוכר חדש ישלם יותר.
  </li>
  <li>
    <strong>Passing Rent &gt; Market Rent (Over-Rented):</strong> השוכר משלם מעל השוק —
    <strong>סיכון:</strong> בחידוש חוזה ידרוש הנחה, ובמקרה קיצוני יעזוב. NOI עשוי לרדת
    בחידוש. זהו "פצצה מתקתקת" בניתוח.
  </li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — Over-Rented:</strong><br><br>
  נכס: 3,000 מ"ר, Passing Rent 150 ₪/מ"ר/חודש (חוזה עד 2026)<br>
  Market Rent כיום: 110 ₪/מ"ר/חודש<br><br>
  NOI נוכחי: 3,000 × 150 × 12 = 5,400,000 ₪<br>
  NOI לאחר חידוש (לפי שוק): 3,000 × 110 × 12 = 3,960,000 ₪<br><br>
  ירידת NOI עם חידוש: 1,440,000 ₪ — 27%<br>
  אם שירות חוב = 4,200,000 ₪: DSCR עובר מ-1.29 ל-0.94 — <strong>מתחת ל-1!</strong>
</div>

<h2>Break-Even Occupancy — חישוב נקודת האיזון</h2>

<p>
<strong>Break-Even Occupancy</strong> הוא שיעור התפוסה המינימלי שמכסה את כל הוצאות
הנכס ושירות החוב. תפוסה בפועל מעל ה-Break-Even = הנכס מכסה חובותיו. מתחתיו — הנכס
גורר הפסד תפעולי.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
חישוב Break-Even Occupancy:<br><br>
נתונים:<br>
  שטח נכס: 4,000 מ"ר<br>
  שכ"ד שוק: 120 ₪/מ"ר/חודש<br>
  הוצאות תפעול שנתיות (ניהול, תחזוקה, ביטוח, ארנונה): 800,000 ₪<br>
  שירות חוב שנתי (ריבית + קרן): 3,200,000 ₪<br>
  סה"כ חובות שנתיים: 4,000,000 ₪<br><br>
  NOI נדרש לכיסוי = 4,000,000 ₪<br>
  הכנסה מלאה (100% תפוסה): 4,000 × 120 × 12 = 5,760,000 ₪<br><br>
Break-Even Occupancy = 4,000,000 / 5,760,000 = 69.4%<br><br>
פרשנות: כל עוד הנכס מושכר ב-70%+ — הוא מכסה את כל ההוצאות. אם תפוסה תרד מתחת
ל-69.4%, הנכס לא מכסה את שירות החוב — הלווה חייב להזרים הון מחוץ לנכס.
</div>

<p>
<strong>כרית מרווח:</strong> ה-Gap בין תפוסה בפועל ל-Break-Even הוא "כרית הסיכון".
נכס עם תפוסה 90% ו-Break-Even 70% = כרית של 20 נקודות אחוז. נכס עם תפוסה 80%
ו-Break-Even 75% = כרית של 5 נקודות בלבד — פגיע מאוד.
</p>

<h2>רגישות NOI לירידת תפוסה — ניתוח Sensitivity</h2>

<p>
כלי נוסף שאנליסטים משתמשים בו: <strong>Sensitivity Table</strong> — טבלת DSCR לפי
שיעורי תפוסה שונים. זה מראה לוועדת האשראי במהירות כמה ה-DSCR עמיד לירידות תפוסה.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — אל תסתמך על NOI הנוכחי בלבד:</strong><br>
  NOI שמוצג בניתוח הוא תמיד "רגע בזמן" — הוא משקף תפוסה, שכ"ד ועלויות נכון לתאריך
  הניתוח. שאל תמיד:<br>
  (א) האם חוזי שכירות פוקעים בתוך אופק ההלוואה? מה NOI אחרי חידוש בשוק?<br>
  (ב) האם יש שוכר עוגן? מה קורה ל-NOI אם הוא עוזב?<br>
  (ג) מה Break-Even Occupancy, וכמה כרית קיימת?<br>
  <strong>NOI "חי" — לא סטטי. ניתוח אשראי טוב מנתח את NOI בתרחישי עתיד, לא רק בהווה.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 3 — Comprehension HTML
# ---------------------------------------------------------------------------

M3_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על סיכוני שוק, תפוסה ותזרים — בחן את יכולתך לחשב WALT, לפרש
Over-Rented לעומת Under-Rented, לחשב Break-Even Occupancy ולאתר סיכון ריכוז שוכרים
בנכס נתון.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Exercises HTML
# ---------------------------------------------------------------------------

M3_EXERCISES_HTML = """
<p>
5 תרגילים על סיכוני תפוסה ותזרים. התרגילים כוללים חישוב WALT לנכס עם 4 שוכרים,
חישוב Break-Even Occupancy ממידע פיננסי של עסקה, ניתוח השפעת עזיבת שוכר עוגן
על DSCR, זיהוי Over-Rented ואמידת NOI לאחר חידוש חוזה בשוק.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — סיכוני שוק, תפוסה ותזרים</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>ריקנות מבנית מול מחזורית:</strong> ריקנות מבנית קשה לתיקון ודורשת השקעה הונית;
    ריקנות מחזורית הפיכה אך עם פיגור של 12–24 חודשים. סוג הריקנות קובע את מדיניות המיתיגציה.
  </li>
  <li>
    <strong>WALT — מדד יציבות ההכנסה:</strong> WALT גבוה (5+ שנים) = NOI יציב לטווח ארוך.
    WALT נמוך (&lt;2 שנים) = סיכון חידוש קרוב. תמיד השווה WALT לאופק ההלוואה — WALT קצר
    מתקופת ההלוואה פירושו חשיפה לחידוש תוך חיי ההלוואה.
  </li>
  <li>
    <strong>ריכוז שוכרים:</strong> שוכר אחד המהווה 50%+ מ-NOI = סיכון ריכוז קריטי. ניתוח
    יציבות השוכר (דוחות כספיים, אשראי, ענף) חיוני כחלק מ-Due Diligence.
  </li>
  <li>
    <strong>Over-Rented:</strong> Passing Rent מעל Market Rent = "פצצה מתקתקת". בחידוש
    חוזה NOI ירד, ועלול לפגוע ב-DSCR. תמיד חשב NOI פרו-פורמה גם לפי Market Rent.
  </li>
  <li>
    <strong>Break-Even Occupancy:</strong> שיעור התפוסה המינימלי לכיסוי שירות חוב ועלויות.
    כרית של &gt;15% = נכס עמיד. כרית &lt;5% = נכס פגיע לזעזועים. כלול חישוב זה בכל Credit Memo.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
מיפינו, מדדנו וניתחנו את שלושת קבוצות הסיכון המרכזיות: זיהוי וסיווג, סיכוני ריבית ומימון,
וסיכוני תפוסה ותזרים. <em>מודול 4</em> יציג את <strong>כלי המיתיגציה המתקדמים</strong> —
Covenant Packages, מנגנוני Cash Sweep, Debt Service Reserve ואסטרטגיות ניהול סיכון
שמגנות על המלווה לאורך חיי ההלוואה.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 7 "
        '(ניהול סיכונים בנדל"ן)'
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 7 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=7)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=7 not found. "
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
            self.style.SUCCESS("\nAll done — Course 7 modules 1-3 seeded successfully.")
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
