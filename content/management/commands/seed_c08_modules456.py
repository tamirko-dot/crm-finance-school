"""
Management command: seed_c08_modules456
Seeds Module 4-6 content for Course 8 (ניתוח מסמכים משפטיים).
Usage: python manage.py seed_c08_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — הסכמי שכירות — ניתוח מנקודת מבט אשראי
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  הסכמי שכירות — ניתוח מנקודת מבט אשראי
</h2>

<!-- ===== סעיף 1 — למה הסכם שכירות חשוב למלווה ===== -->
<h3 style="color:#1a2638;">1. למה הסכם שכירות חשוב למלווה?</h3>

<p>
  מלווה המממן נכס מניב — קניון, בניין משרדים, מחסן לוגיסטי — מסתמך
  על ה-NOI שהנכס מייצר לפירעון ההלוואה. ה-NOI מורכב בעיקרו מהכנסות שכר
  דירה בניכוי הוצאות תפעול.
  לכן: <strong>כל הסכם שכירות הוא מסמך אשראי</strong>.
  חוזה שכירות חלש — עם שוכר חלש, תקופה קצרה, אפשרות יציאה מוקדמת —
  הוא סיכון ישיר ל-DSCR ולאפשרות הפירעון.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל הבסיס:</strong><br>
  NOI = ∑ שכר דירה חוזי − הוצאות תפעול.<br>
  אם שוכר עיקרי עוזב, ה-NOI יכול לצנוח ב-30%–60% בבת אחת — ולהפיל את ה-DSCR
  מתחת לסף Covenant. לכן אנליסט אשראי חייב לקרוא כל חוזה, לא רק את
  הסיכום שמגיש הלווה.
</div>

<!-- ===== סעיף 2 — תקופת השכירות ו-WALT ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. תקופת שכירות ו-WALT</h3>

<p>
  <strong>WALT — Weighted Average Lease Term</strong> הוא משך החוזים הממוצע
  המשוקלל לפי שטח (או לפי הכנסה). ככל ש-WALT גבוה יותר — כך הכנסות השכירות
  מובטחות לאורך זמן רב יותר.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">WALT</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פרשנות אשראי</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מעל 7 שנים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">יציב; מתאים לתקופת הלוואה ארוכה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">5–7 שנים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מקובל; בדוק Break Clauses</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פחות מ-5 שנים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכון גבוה; דרוש Buffer ב-DSCR</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>Break Clauses</strong> — סעיפי יציאה מוקדמת — מאפשרים לשוכר
  לסיים את החוזה לפני המועד בהתראה מוגדרת (לרוב 6–12 חודשים).
  WALT גבוה עם Break Clauses אינו WALT אמיתי — האנליסט חייב לחשב את
  ה-<strong>WAULT (Weighted Average Unexpired Lease Term)</strong> לאחר הפעלת Break.
</p>

<!-- ===== סעיף 3 — שכ"ד שוק: Over-Rented ו-Under-Rented ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. שכר דירה שוק — Over-Rented ו-Under-Rented</h3>

<p>
  השוואת שכר הדירה החוזי לשכר הדירה ה<strong>שוקי</strong> (ERV — Estimated Rental Value)
  היא כלי אנליטי קריטי:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>Over-Rented:</strong> השוכר משלם מעל שכר השוק. הנכס רווחי
    כרגע — אך בחידוש החוזה, השוכר יש לו כוח מיקוח לדרוש הפחתה.
    הסיכון: NOI ייפול בחידוש. יש לבדוק כמה שנים עד לחידוש.
  </li>
  <li>
    <strong>Under-Rented:</strong> השוכר משלם פחות משכר השוק. הנכס פחות
    רווחי כרגע — אך יש פוטנציאל לעלייה. לרוב מצב זה עדיף מנקודת מבט אשראי,
    כי הסיכון לשחיקת NOI נמוך.
  </li>
  <li>
    <strong>שכ"ד שוק:</strong> הנכס מתומחר נכון — חידוש חוזה אמור להיות
    יציב.
  </li>
</ul>

<!-- ===== סעיף 4 — הצמדות שכר דירה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. סעיפי הצמדת שכר הדירה</h3>

<p>
  שני מנגנוני הצמדה עיקריים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>הצמדה למדד המחירים לצרכן (CPI):</strong> שכ"ד עולה עם
    האינפלציה. מגן על ערך ה-NOI הריאלי. שכיח בישראל בחוזים ארוכי טווח.
    יש לבדוק: האם ה-Cap (תקרה להצמדה) נמוך מהאינפלציה הצפויה?
  </li>
  <li>
    <strong>Fixed Steps:</strong> עלייה קבועה מוגדרת מראש (למשל 2% לשנה,
    ללא קשר לאינפלציה). מספקת ודאות לשני הצדדים — אך אם האינפלציה גבוהה,
    ערך ה-NOI הריאלי נשחק.
  </li>
</ul>

<p>
  מנקודת מבט אשראי: הצמדת NOI לאינפלציה עדיפה — מבטיחה שפרמטרי
  ה-DSCR לא ייגרעו ריאלית לאורך שנות ההלוואה.
</p>

<!-- ===== סעיף 5 — איכות שוכר ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. איכות שוכר — כיצד להעריך?</h3>

<p>
  שוכר חזק = NOI בטוח. שוכר חלש = סיכון אשראי נסתר. כיצד מעריכים?
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>עסק ציבורי:</strong> בדוק דירוג אשראי, רווחיות תפעולית,
    יחסי כיסוי ריבית, רמת מינוף. גוף ציבורי (ממשלה, עירייה) — סיכון
    נמוך מאוד.
  </li>
  <li>
    <strong>עסק פרטי:</strong> בקש דוחות כספיים מבוקרים 3 שנים.
    נתח: האם ההכנסות גדלות? האם יש תזרים מזומנים חיובי? מהי יכולת
    העסק לשרת את שכר הדירה גם בתרחיש שפל?
  </li>
  <li>
    <strong>יחס כיסוי שכ"ד (Rent Cover Ratio):</strong> EBITDA / שכ"ד שנתי.
    יחס מתחת ל-1.5× מעיד שהעסק מתוח מבחינת יכולת תשלום השכירות.
  </li>
  <li>
    <strong>ריכוזיות שוכרים:</strong> שוכר אחד = 60% מ-NOI? זהו
    סיכון ריכוזיות קריטי. השוואה: מבנה Multi-Tenant מפזר סיכון.
  </li>
</ul>

<!-- ===== סעיף 6 — הסבת שכירות ושיפורי נכס ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. הסבת שכירות, TI ותנאי NNN מול Gross Lease</h3>

<p>
  <strong>הסבת שכירות (Assignment) וסעיפי Subletting:</strong>
  האם מותר לשוכר להסב את החוזה לצד שלישי?
  מנקודת מבט אשראי — הסבה ללא הסכמת המשכיר עלולה להחליף שוכר חזק בחלש.
  בדוק: האם הסכם השכירות דורש הסכמת המשכיר להסבה?
</p>

<p>
  <strong>Tenant Improvement (TI) — מענק שיפורים:</strong>
  מקובל שהמשכיר נותן לשוכר מענק כספי לשיפוץ השטח. TI גבוה מצמצם את
  ה-NOI הנקי בשנות ההקמה, אך בדרך כלל מבטיח WALT ארוך יותר.
  בדוק: האם TI כלול בתחשיב ה-NOI? האם הוא מוחזר בהדרגה דרך שכ"ד גבוה?
</p>

<p>
  <strong>Triple Net (NNN) מול Gross Lease:</strong>
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג חוזה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מי נושא בהוצאות הנכס?</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">משמעות לאנליסט</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Triple Net (NNN)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">השוכר — ארנונה, ביטוח, תחזוקה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI יציב וצפוי; הוצאות לא מכרסמות ברווח</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Gross Lease</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">המשכיר — כל הוצאות הנכס</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI תלוי בשליטת עלויות; עליית מחירים שוחקת רווח</td>
    </tr>
  </tbody>
</table>

<!-- ===== דוגמה — קניון ===== -->
<h3 style="color:#1a2638;margin-top:28px;">7. דוגמה: ניתוח חוזה שכירות אנקר בקניון</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:14px 18px;margin:12px 0;border-radius:4px;">
  <strong>עסקה:</strong> בקשת מימון לקניון אזורי. שוכר אנקר — רשת מזון ידועה —
  תופס 40% מהשטח ומייצר 45% מה-NOI.<br><br>
  <strong>פרטי החוזה:</strong><br>
  • תקופה: 10 שנים (נחתם לפני 3 שנים) — נותרו 7 שנים<br>
  • Break Clause: לשוכר זכות יציאה בתום שנה 5 (בעוד שנתיים) עם התראה של 12 חודשים<br>
  • שכ"ד: 320 ₪/מ&quot;ר/חודש — ERV שוקי: 290 ₪/מ&quot;ר/חודש (Over-Rented)<br>
  • הצמדה: CPI בלבד, ללא Cap<br>
  • סוג: NNN<br><br>
  <strong>ניתוח האנליסט:</strong><br>
  ה-WAULT האפקטיבי הוא 2 שנים (עד ה-Break Clause) — לא 7. השוכר Over-Rented
  ב-10.3% — יש לו תמריץ לממש את ה-Break ולשכור מחדש בשוק. אם יממש,
  ה-NOI יצנח ב-45%. יש לדרוש: (א) Cash Reserve שנתיים שכ"ד מהאנקר
  כ-Buffer, (ב) DSCR Covenant מחמיר, (ג) Covenant אוטומטי להגבלת
  חלוקות אם ה-Break מממומש.
</div>

<!-- ===== אזהרה ===== -->
<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  אל תסמוך על סיכום חוזי השכירות שמגיש הלווה — קרא את החוזים עצמם.
  Break Clauses, סעיפי Subletting, וסעיפי TI מוסתרים לעיתים בנספחים.
  WALT מחושב בטבלה אחת — WAULT אפקטיבי הוא חישוב שתבצע בעצמך.
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של WALT ו-WAULT, Over-Rented ו-Under-Rented, "
    "מנגנוני הצמדת שכ\"ד, הערכת איכות שוכר, ו-Triple Net מול Gross Lease. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים חישוב WALT ו-WAULT מנתוני חוזים נתונים, "
    "זיהוי שוכר Over-Rented או Under-Rented לפי שכ\"ד חוזי מול ERV שוקי, "
    "ואנליזת סיכון Break Clause לפי נתוני עסקה. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — הסכמי שכירות — ניתוח מנקודת מבט אשראי
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>חוזה שכירות הוא מסמך אשראי — NOI תלוי ישירות בחוזק חוזי השכירות.</strong>
    אנליסט אשראי חייב לקרוא כל חוזה, לא רק את הסיכום שמגיש הלווה.
  </li>
  <li>
    <strong>WALT הוא אורך חוזים ממוצע משוקלל; WAULT הוא אורך החוזה האפקטיבי לאחר Break Clauses.</strong>
    WALT גבוה עם Break Clauses אינו ערובה ליציבות — חשב WAULT בעצמך.
  </li>
  <li>
    <strong>Over-Rented מסמן סיכון לירידת NOI בחידוש; Under-Rented מסמן יציבות.</strong>
    השוואת שכ"ד חוזי ל-ERV שוקי היא ניתוח בסיסי שלא ניתן לדלג עליו.
  </li>
  <li>
    <strong>שוכר חזק = NOI בטוח; שוכר חלש = סיכון אשראי נסתר.</strong>
    Rent Cover Ratio מתחת ל-1.5× מצריך בדיקה מעמיקה של יכולת תשלום השוכר.
  </li>
  <li>
    <strong>NNN עדיף על Gross Lease ממנקודת מבט אשראי — NOI יציב ולא תלוי בשליטת עלויות.</strong>
    בחוזה Gross, עליית ארנונה או ביטוח שוחקת NOI ישירות.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אורך חוזה ממוצע משוקלל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">WALT</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ממוצע תקופות חוזי שכירות, משוקלל לפי שטח/הכנסה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אורך חוזה אפקטיבי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">WAULT</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">WALT אחרי הפעלת Break Clauses</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שכ"ד שוקי מוערך</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ERV — Estimated Rental Value</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שכ"ד שוק שנכס דומה יכול להשיג כרגע</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שכ"ד מעל שוק</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Over-Rented</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שכ"ד חוזי גבוה מ-ERV; סיכון בחידוש</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חוזה שלוש נטו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Triple Net (NNN)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוכר נושא בארנונה, ביטוח ותחזוקה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מענק שיפורים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Tenant Improvement (TI)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשלום מהמשכיר לשוכר לשיפוץ השטח</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — מסמכי Due Diligence — מה לחפש ואיך לקרוא
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  מסמכי Due Diligence — מה לחפש ואיך לקרוא
</h2>

<!-- ===== סעיף 1 — תפקיד האנליסט בתיק DD ===== -->
<h3 style="color:#1a2638;">1. תיק ה-DD — אחריות האנליסט</h3>

<p>
  ה-Due Diligence הוא שלב בו האנליסט עובר ממצגת הלווה — למציאות.
  <strong>תיק ה-DD</strong> הוא אוסף מסמכים שמגיש הלווה לאימות עצמאי על-ידי
  הבנק. האנליסט לא מקבל את המסמכים, קורא אותם ומעביר הלאה — הוא חייב לנתח,
  לאמת, ולדגל פערים.
</p>

<p>
  <strong>עיקרון מפתח:</strong> מסמך שחסר מתיק ה-DD הוא לא "לא רלוונטי" —
  הוא <em>דגל אדום</em>. אנליסט שמוותר על מסמך חסר מוותר על הגנה.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>רשימת ה-DD המינימלית:</strong><br>
  (א) דוח שמאות, (ב) סקר הנדסי, (ג) דוח סביבתי, (ד) בדיקת בעלות — טאבו,
  (ה) תעודות ביטוח, (ו) דוחות כספיים מבוקרים של הלווה.
  חסר אחד — דרוש הסבר.
</div>

<!-- ===== סעיף 2 — דוח שמאות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. דוח שמאות (שמאות מקרקעין)</h3>

<p>
  <strong>מה לקרוא בדוח שמאות:</strong>
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>מתודולוגיה:</strong> האם השמאי השתמש בשיטת Cap Rate, DCF, או
    השוואת עסקאות? שיטה אחת בלבד — דרוש ממנו לפחות שתי שיטות כ-Sanity Check.
  </li>
  <li>
    <strong>הנחות מרכזיות:</strong> Cap Rate בשמאות — האם הוא ריאלי ביחס
    לנכסים דומים שנמכרו? NOI שמניח השמאי — האם תואם ל-NOI ההיסטורי?
    תפוסה מניחה השמאי — האם סבירה ביחס לשוק?
  </li>
  <li>
    <strong>ראיות שוק (Comparables):</strong> עסקאות דומות שנעשו עד 12
    חודשים לפני הדוח. עסקאות ישנות יותר — פחות רלוונטיות בשוק משתנה.
  </li>
  <li>
    <strong>ניתוח רגישות:</strong> האם הדוח כולל Sensitivity Analysis?
    מה קורה לשווי אם Cap Rate עולה ב-0.5%? אם תפוסה יורדת ב-10%?
  </li>
  <li>
    <strong>תאריך הדוח:</strong> שמאות שנכתבה מעל 12 חודשים — דרוש
    עדכון. שמאות שנכתבה לפני ירידת שוק — לא שווה.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דגל אדום — שמאות:</strong><br>
  שמאי שמונה על-ידי הלווה ושמאי שמונה על-ידי הבנק הגיעו לשווים שונים ב-15%?
  זהו פער מהותי. דרוש ישיבת יישוב — אל תפשר ב-Average. הבנק מממן את
  שווי הבנק — לא ממוצע.
</div>

<!-- ===== סעיף 3 — סקר הנדסי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. סקר הנדסי — מצב פיזי הנכס</h3>

<p>
  מהנדס בניין מוסמך בוחן את הנכס ומדווח על:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>מצב מבני:</strong> איתור סדקים, נזקי לחות, כשלי מערכות.
    "מצב טוב" הוא לא מספיק — בקש הערכת עלות תחזוקה דחויה (Deferred Maintenance).
  </li>
  <li>
    <strong>גיל הנכס ומחזור חיים:</strong> גג, מעליות, מיזוג — כל מערכת
    גדולה יש לה תוחלת חיים. מה הגיל הנוכחי ומתי נדרש החלפה?
  </li>
  <li>
    <strong>הערכת עלות תיקונים נדרשים:</strong> הבנק דורש לעיתים שהלווה
    יפקיד Capex Reserve — שווה לעלות התחזוקה הדחויה — כתנאי לסגירה.
  </li>
</ul>

<!-- ===== סעיף 4 — דוח סביבתי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. דוח סביבתי — Phase 1 ו-Phase 2</h3>

<p>
  <strong>Phase 1 — Environmental Site Assessment:</strong> ביקורת תיעוד
  ושטח לאיתור זיהום אפשרי. לא כולל דיגום קרקע. מתאים לנכסים מסחריים
  ולוגיסטיים שנבנו על קרקע עם שימוש קודם (מפעל ישן, תחנת דלק).
</p>

<p>
  <strong>Phase 2:</strong> דיגום פיזי של קרקע ומי תהום. מתבצע כאשר Phase 1
  מצא אינדיקציות לזיהום. אם Phase 2 מגלה זיהום — עלות הפינוי עלולה
  להיות בטווח מיליונים, להפחית שווי ולעכב עסקאות.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דגל אדום — סביבתי:</strong><br>
  נכס על קרקע ששימשה מפעל תעשייתי, תחנת דלק, או מכבסה כימית — Phase 1
  הוא חובה מוחלטת. בנק שדילג על דוח סביבתי מממן חבות סביבתית פוטנציאלית
  בלי לדעת. בישראל, בעלי קרקע חייבים לפי חוק בפינוי זיהום — גם אם
  הם לא גרמו אותו.
</div>

<!-- ===== סעיף 5 — בדיקת בעלות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. בדיקת בעלות — נסח טאבו ותכנון</h3>

<p>
  <strong>נסח טאבו (לשכת רישום מקרקעין):</strong>
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>זיהוי הבעלים:</strong> האם ה-SPV רשום כבעלים? אם הנכס
    בחכירה מרשות מקרקעי ישראל — מה תנאי החכירה ואורכה?
  </li>
  <li>
    <strong>שיעבודים קיימים:</strong> האם יש שיעבוד ראשון שקדם להלוואה
    הנדונה? הבנק חייב לוודא שהוא מקבל שיעבוד ראשון — לא שני.
  </li>
  <li>
    <strong>הגבלות וזיקות:</strong> זיקות הנאה, הגבלות בנייה,
    זיקות כניסה — עלולות להגביל פיתוח עתידי ולפגוע בשווי.
  </li>
</ul>

<p>
  <strong>תכנון (Building Permit):</strong>
  האם הנכס בנוי לפי היתר בנייה תקין? כל מ"ר שנבנה ללא היתר —
  חשוף לצו הריסה. יש לדרוש:
  (א) העתק היתר הבנייה, (ב) תעודת גמר (אם נכס חדש), (ג) בדיקת תוכנית
  עיר עתידית — האם יש שינוי ייעוד מתוכנן שישפיע על ערך הנכס?
</p>

<!-- ===== סעיף 6 — ביטוחים ודוחות כספיים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. ביטוחים ודוחות כספיים</h3>

<p>
  <strong>ביטוחים:</strong> הלווה חייב להוכיח ביטוח מלא לפני ה-Drawdown הראשון:
</p>

<ul style="line-height:1.9;">
  <li><strong>ביטוח מבנה:</strong> לכיסוי שווי שחזור מלא — לא שווי שוק</li>
  <li><strong>ביטוח אחריות כלפי צד שלישי</strong></li>
  <li><strong>ביטוח אובדן שכ"ד (Business Interruption):</strong> חיוני
    בנכסים מניבים — אם הנכס ניזוק ואינו פעיל, ה-NOI נפסק.</li>
</ul>

<p>
  בדוק: <strong>הבנק הוא המוטב הראשי (Loss Payee)</strong> — לא הלווה.
  ביטוח שבו הלווה הוא המוטב — כסף ביטוח יכול להגיע ללווה ולא לשחזור הנכס.
</p>

<p>
  <strong>דוחות כספיים של הלווה:</strong> שלוש שנים אחרונות, מבוקרות.
  נתח: מגמת הכנסות, עלויות ריבית, יחסי מינוף, הערות רואה החשבון.
  הערת Going Concern — עצרת מיידית לתהליך האשראי.
</p>

<!-- ===== סעיף 7 — פערים בתיק DD ===== -->
<h3 style="color:#1a2638;margin-top:28px;">7. זיהוי פערים בתיק DD ובקשת מסמכים חסרים</h3>

<p>
  בנה Checklist ממובנה ורשום מול כל מסמך: <em>התקבל / לא התקבל / קיים אך לא מספיק</em>.
  כל פריט "לא התקבל" מחייב בקשה מפורשת בכתב ללווה עם deadline.
  אם הלווה לא מגיש — תעד בקובץ האשראי ודגל בוועדת האשראי.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>דגלים אדומים שכיחים בתיק DD:</strong><br>
  • שמאות ישנה מעל 12 חודשים — ייתכן שהשוק השתנה<br>
  • ביטוח שפג תוקפו — הנכס לא מבוטח!<br>
  • תכנון לא מאושר — חשיפה לצו הריסה<br>
  • שמאות ותכנון אינם תואמים — שמאי העריך שטח שלא קיים בהיתר<br>
  • דוחות כספיים ישנים מעל 18 חודש — לא משקפים מצב עדכני
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של ששת רכיבי תיק ה-DD: שמאות, סקר הנדסי, "
    "דוח סביבתי Phase 1/2, בדיקת בעלות ורישום טאבו, ביטוחים ודוחות כספיים. "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים ניתוח נסח טאבו מדומה לאיתור שיעבודים, "
    "קריאת דוח שמאות ואיתור הנחות לא ריאליות, "
    "ובנייה של Checklist DD לעסקה נתונה ואיתור מסמכים חסרים. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — מסמכי Due Diligence — מה לחפש ואיך לקרוא
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>תיק DD מינימלי כולל שישה רכיבים: שמאות, סקר הנדסי, דוח סביבתי, בדיקת טאבו, ביטוחים ודוחות כספיים.</strong>
    מסמך חסר אינו "לא רלוונטי" — הוא דגל אדום שמחייב בקשה מיידית.
  </li>
  <li>
    <strong>דוח שמאות נבחן לפי מתודולוגיה, הנחות, Comparables ותאריך.</strong>
    שמאות ישנה מ-12 חודש או שמאות שנכתבה לפני ירידת שוק — דרוש עדכון לפני אישור.
  </li>
  <li>
    <strong>הסקר ההנדסי מכמת Deferred Maintenance; הדוח הסביבתי מגלה חבות זיהום.</strong>
    בנכסים תעשייתיים ולוגיסטיים — Phase 1 הוא חובה, Phase 2 נדרש אם Phase 1 מדגיל.
  </li>
  <li>
    <strong>נסח טאבו מאמת בעלות, שיעבודים, הגבלות ותכנון — קרא אותו בעצמך.</strong>
    שיעבוד ראשון שלא אותר הוא תרחיש שממנו הבנק לא מחלים בקלות.
  </li>
  <li>
    <strong>הבנק חייב להיות מוטב ראשי בביטוח — לא הלווה.</strong>
    ביטוח שפג תוקפו ביום ה-Drawdown הוא ברירת מחדל רגולטורית פוטנציאלית.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">דוח שמאות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Valuation Report</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הערכת שמאי מוסמך לשווי הנכס</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תחזוקה דחויה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Deferred Maintenance</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עלות תיקונים שנדחו ועתידים לחול</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סקר סביבתי שלב ראשון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Phase 1 ESA</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ביקורת תיעוד ושטח לאיתור זיהום אפשרי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נסח טאבו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Land Registry Extract</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מסמך רשמי המפרט בעלות ושיעבודים בנכס</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מוטב ראשי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Loss Payee / First Named Insured</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">המקבל הראשון של כספי הביטוח במקרה נזק</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ביטוח אובדן שכ"ד</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Business Interruption Insurance</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כיסוי לאובדן הכנסות שכ"ד בזמן נזק לנכס</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — Red Flags משפטיים ואיתות אזהרה בעסקה
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  Red Flags משפטיים ואיתות אזהרה בעסקה
</h2>

<!-- ===== סעיף 1 — מהם Red Flags? ===== -->
<h3 style="color:#1a2638;">1. מהם Red Flags משפטיים?</h3>

<p>
  <strong>Red Flag</strong> הוא ממצא או אינדיקציה שמעורר חשש מהותי
  לגבי שלמות העסקה, יכולת הפירעון, או הגינות הצדדים.
  Red Flags לא תמיד אומרים "לא לעסקה" — אך הם תמיד אומרים
  "עצור, חקור, ואם לא ניתן הסבר מספק — דגל בוועדת אשראי".
</p>

<p>
  אנליסט שמזהה Red Flag ולא מדגיל אותו — נושא באחריות מקצועית
  אישית. ה-Red Flag שלא תדגיל הוא הכשל שיצוטט בדיעבד.
</p>

<div style="background:#ffebee;border-right:5px solid #c62828;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל הברזל:</strong><br>
  Red Flag = מחייב תיעוד בכתב, הסבר מפורש מהלווה, ופסקת ניתוח בדוח האשראי.
  "לא שאלתי" אינה תשובה קבילה בוועדת אשראי.
</div>

<!-- ===== סעיף 2 — Red Flag א: מחלוקת בעלות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. מחלוקת בעלות ותביעות משפטיות על הנכס</h3>

<p>
  <strong>מחלוקת בעלות</strong> — כאשר יש תביעה משפטית תלויה ועומדת
  על בעלות בנכס, הנכס אינו ניתן לשיעבוד תקני.
  המלווה לא יכול לרשום שיעבוד ראשון תקין על נכס שבעלותו שנויה במחלוקת.
</p>

<ul style="line-height:1.9;">
  <li>בדוק: נסח טאבו ל<strong>הערות אזהרה</strong> — הערת אזהרה
    היא אינדיקציה לתביעה משפטית שהוגשה.</li>
  <li>בדוק: <strong>פנקס המקרקעין</strong> לתביעות עכבה ועיקולים.</li>
  <li>בדוק: פסיקת בתי משפט — האם יש פסק דין שלא בוצע נגד הלווה?</li>
</ul>

<p>
  <strong>המדיניות:</strong> עסקה עם מחלוקת בעלות פעילה — עצירה מוחלטת
  עד להכרעה משפטית. אין לאשר הלוואה על נכס ש"בדרך לסיים תביעה".
</p>

<!-- ===== סעיף 3 — Red Flag ב: בנייה ללא היתר ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. בנייה ללא היתר — סיכון צו הריסה</h3>

<p>
  <strong>בנייה ללא היתר (בנייה בלתי חוקית)</strong> היא אחד מה-Red Flags
  הקריטיים בנדל&quot;ן ישראלי. בישראל, רשויות מקומיות רשאיות להוציא
  <strong>צו הריסה</strong> על כל מבנה שנבנה ללא היתר — גם שנים לאחר הבנייה.
</p>

<p>
  <strong>כיצד לזהות:</strong>
</p>

<ul style="line-height:1.9;">
  <li>השווה שטחי הנכס לפי <strong>היתר הבנייה</strong> לשטחים
    לפי <strong>השמאות</strong> ולפי חוזי השכירות — פערים = בנייה לא מהוייתרת.</li>
  <li>בדוק <strong>תעודת גמר (טופס 4)</strong> — האם הונפקה? נכס ללא
    תעודת גמר חשוף לסנקציות.</li>
  <li>שאל: האם הוגשו בקשות להכשרת בנייה? האם יש הליכים ועדת ערר?</li>
</ul>

<p>
  <strong>ההשלכה האשראית:</strong> אם חלק מה-NOI מגיע משטח שנבנה ללא היתר,
  ה-NOI עלול להיות שלילי בין לילה אם צו הריסה מתממש.
  שמאות שמעריכה שטח לא מהוייתר — שמאות לא ריאלית.
</p>

<!-- ===== סעיף 4 — Red Flag ג: שיעבודים לא מגולים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. שיעבודים קיימים שלא גולו</h3>

<p>
  שיעבוד ראשון לא ידוע על הנכס הוא אולי ה-Red Flag הקריטי ביותר:
  המלווה סבור שהוא מחזיק בשיעבוד ראשון — אך בפועל יש מלווה בכיר ממנו.
</p>

<p>
  <strong>כיצד לאתר:</strong>
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>חיפוש טאבו מלא:</strong> רישום שיעבודים בלשכת רישום
    המקרקעין — כל שיעבוד חייב להיות רשום כאן. אל תסמוך על הצהרת הלווה.
  </li>
  <li>
    <strong>רשם החברות (חברות פרטיות):</strong> שיעבודים על חברות
    פרטיות רשומים ברשם החברות — בדוק גם שם.
  </li>
  <li>
    <strong>בדיקת הסכמי הלוואה קיימים:</strong> בקש מהלווה הצהרה
    מלאה של כל ההתחייבויות הפיננסיות — והשווה לנסח הטאבו ולרשם החברות.
    פערים = Red Flag.
  </li>
</ul>

<!-- ===== סעיף 5 — Red Flag ד: ערב ללא נכסים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. ערב ללא נכסים ריאליים</h3>

<p>
  <strong>ערבות אישית</strong> היא אמצעי אשראי — אך ערבות של אדם
  שאין לו נכסים ריאליים היא נייר חסר ערך.
</p>

<ul style="line-height:1.9;">
  <li>דרוש <strong>דוח נכסים מפורט</strong> של הערב — נדל&quot;ן,
    השקעות, פיקדונות, אחזקות עסקיות.</li>
  <li>בדוק: האם הנכסים שמצהיר הערב <strong>כבר משועבדים</strong>
    לאחרים? ערב עם נכסים אך עם שיעבודים ראשונים מכסים הכל — ערב חלש.</li>
  <li>בדוק: <strong>הכנסה שוטפת של הערב</strong> — ערב ללא הכנסה
    עצמאית לא יכול לשרת ערבות גדולה.</li>
</ul>

<!-- ===== סעיף 6 — Red Flag ה: מבנה SPV חשוד ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. מבנה SPV חריג — אופשור, שרשרת מורכבת</h3>

<p>
  SPV הוא כלי לגיטימי — אך SPV שמוחזק דרך שרשרת של חברות אוף-שור
  (BVI, Cayman Islands) מבלי הסבר עסקי ברור מעורר חשד.
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>Beneficial Ownership:</strong> מי הבעלים האמיתי בסוף השרשרת?
    ב-2024, ישראל ואירופה מחמירות בחשיפת Beneficial Ownership.
    אם הלווה לא מוכן לגלות — זה Red Flag.
  </li>
  <li>
    <strong>עסקאות Related Party:</strong> האם ה-SPV עושה עסקאות
    עם חברות בשליטת אותו בעלים? בדוק מחירים — האם הם Arm's Length?
    שירות ניהול שה-SPV משלם לחברת אם ב-200% מחיר שוק = ניקוז מסווה.
  </li>
  <li>
    <strong>דפוס Refinancing ללא פירעון:</strong> הלווה מגייס מחדש
    שוב ושוב על אותו נכס מבלי לפרוע — הנכס משמש כ-ATM. בדוק היסטוריית
    מימון ואם כל הלוואה חדשה שימשה רק לפירעון הישנה ללא שחרור הון.
  </li>
</ul>

<!-- ===== סעיף 7 — מסגרת Escalation ===== -->
<h3 style="color:#1a2638;margin-top:28px;">7. מסגרת Escalation — מתי להסלים ומתי לדחות?</h3>

<p>
  לא כל Red Flag מצדיק דחייה מיידית. יש לבחון לפי חומרה:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">חומרת Red Flag</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דוגמה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פעולה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#ffebee;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קריטי — דחה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מחלוקת בעלות פעילה, זיהום סביבתי חשוף</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דחייה מיידית עד הסרת Red Flag</td>
    </tr>
    <tr style="background:#fff8e1;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גבוה — הסלם לוועדה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בנייה חלקית ללא היתר, ערב חלש, SPV אוף-שור</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הצג לוועדת אשראי עם ניתוח; המלץ תנאים מחמירים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בינוני — תנאים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שמאות ישנה, פוליסת ביטוח חסרה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הוסף כ-Condition Precedent; אל תסגור בלעדיו</td>
    </tr>
  </tbody>
</table>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  לחץ מהלווה, מהמנהל, או מקציר זמן — לא מוריד את מחויבותך לדגל Red Flag.
  Red Flag שלא דוגל בכתב הוא Red Flag שלא קיים מנקודת המבט של ועדת האשראי.
  תעד, דגל, והמלץ — זו העבודה.
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של שבעת הקטגוריות של Red Flags משפטיים: "
    "מחלוקת בעלות, בנייה ללא היתר, שיעבודים לא מגולים, ערב חלש, "
    "מבנה SPV חשוד, עסקאות Related Party ודפוס Refinancing. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים זיהוי Red Flags מתרחיש עסקה נתון, "
    "סיווג Red Flag לפי חומרה (קריטי / גבוה / בינוני) והמלצת פעולה, "
    "וניסוח פסקת Escalation מקצועית לוועדת אשראי. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — Red Flags משפטיים ואיתות אזהרה בעסקה
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>Red Flag הוא ממצא שמחייב תיעוד, הסבר מהלווה, ופסקת ניתוח בדוח האשראי.</strong>
    "לא שאלתי" אינה תשובה קבילה — האנליסט נושא באחריות מקצועית אישית.
  </li>
  <li>
    <strong>מחלוקת בעלות ובנייה ללא היתר הם Red Flags קריטיים שעוצרים את העסקה.</strong>
    שיעבוד על נכס שבעלותו שנויה במחלוקת — אינו שיעבוד ריאלי.
  </li>
  <li>
    <strong>שיעבוד קיים שלא גולה מתגלה דרך חיפוש טאבו עצמאי ורשם החברות — לא דרך הלווה.</strong>
    אל תסמוך על הצהרת הלווה בלבד — אמת עם המרשם הרשמי.
  </li>
  <li>
    <strong>SPV אוף-שור, עסקאות Related Party ודפוס Refinancing הם Red Flags מבניים.</strong>
    הם לא בהכרח פסולים — אך דורשים חשיפת Beneficial Ownership וניתוח Arm's Length.
  </li>
  <li>
    <strong>מסגרת Escalation: קריטי = דחה, גבוה = הסלם לוועדה, בינוני = תנאים.</strong>
    הסלמה לוועדת אשראי אינה כישלון — היא מקצועיות.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">דגל אדום</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Red Flag</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ממצא המחייב בדיקה, תיעוד והסלמה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הערת אזהרה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Caveat (Land Registry Warning)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רישום טאבו המציין תביעה משפטית תלויה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בנייה לא מהוייתרת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Unauthorized Construction</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בנייה ללא היתר תכנוני תקין — חשופה לצו הריסה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בעלות אמיתית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Beneficial Ownership</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הבעלים האמיתי בסוף שרשרת ההחזקה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עסקת צד קשור</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Related Party Transaction</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עסקה בין גופים בשליטת אותם בעלים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הסלמה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Escalation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">העברת ממצא לוועדת אשראי לקבלת החלטה בכירה</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לבחינה הסופית:</strong><br>
  השלמתם את שישת מודולי קורס 8 — ניתוח מסמכים משפטיים. למדתם לזהות
  את המסמכים הקריטיים בעסקת נדל&quot;ן, לנתח חוזי שכירות מנקודת מבט
  אשראי, לקרוא תיק Due Diligence, ולזהות Red Flags משפטיים שמצדיקים
  עצירה, הסלמה, או תנאים מחמירים.<br><br>
  הבחינה הסופית תכלול שאלות על ניתוח WALT/WAULT, קריאת נסח טאבו,
  זיהוי Red Flags מתרחישים, ומסגרת הסלמה. הגיעו מוכנים — ובהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "הסכמי שכירות — ניתוח מנקודת מבט אשראי",
        "slug": "heskeme-skhirut-nihul-ashray",
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
        "title_he": "מסמכי Due Diligence — מה לחפש ואיך לקרוא",
        "slug": "due-diligence-mismahim",
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
        "title_he": "Red Flags משפטיים ואיתות אזהרה בעסקה",
        "slug": "red-flags-mishpatim-itra-azhara",
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
    help = "Seed Course 8, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=8)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 8 not found. Run 'python manage.py seed_data' first."
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
