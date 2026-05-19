"""
Management command: seed_c09_modules456
Seeds Module 4-6 content for Course 9 (מודלים פיננסיים מתקדמים).
Usage: python manage.py seed_c09_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — מבני Waterfall ועסקאות מורכבות
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  מבני Waterfall ועסקאות מורכבות
</h2>

<!-- ===== סעיף 1 — מהו Waterfall ===== -->
<h3 style="color:#1a2638;">1. מהו מבנה Waterfall במימון נדל&quot;ן?</h3>

<p>
  <strong>Waterfall</strong> — מפל חלוקה — הוא מנגנון המגדיר את סדר
  קדימויות חלוקת תזרים המזומנים (Cash Flow) בין משקיעים שונים בעסקת
  נדל&quot;ן. השם מגיע מהדימוי למפל מים: כל שכבה מתמלאת ראשון — ורק
  לאחר שהתמלאה, העודף זורם לשכבה הבאה.
</p>

<p>
  בעסקת נדל&quot;ן טיפוסית קיימים שני סוגי משקיעי הון (Equity):
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>LP — Limited Partners (שותפים מוגבלים):</strong> המשקיעים
    הפסיביים שמספקים את רוב ההון העצמי (לרוב 80%–95% מסך ההון). הם
    נהנים מהגנה ראשונית בחלוקת הרווחים, אך אינם מעורבים בניהול.
  </li>
  <li>
    <strong>GP — General Partner (שותף כללי):</strong> היזם / מנהל
    הפרויקט שמספק את המיומנות התפעולית ולרוב רק 5%–20% מההון. הוא
    מנהל את הנכס ומקבל בונוס ביצועים (Promote) אם יעמוד ביעדי תשואה.
  </li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>עיקרון מרכזי:</strong><br>
  מבנה ה-Waterfall מגן על ה-LP: הם מקבלים קודם את ההון שהשקיעו בחזרה
  בתוספת תשואה מינימלית מובטחת (Preferred Return), ורק לאחר מכן ה-GP
  מקבל את הבונוס שלו (Promote). האנליסט חייב להבין מבנה זה כדי
  להעריך את מה שנשאר לשירות חוב הבנק.
</div>

<!-- ===== סעיף 2 — Preferred Return ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. Preferred Return — תשואה מועדפת</h3>

<p>
  <strong>Preferred Return (Pref)</strong> הוא שיעור תשואה שנתי מינימלי
  שה-LP זכאי לקבל על השקעתו לפני שה-GP מקבל דבר מעבר לדמי ניהול בסיסיים.
  שיעורים מקובלים בשוק: 6%–10% לשנה, כאשר 8% הוא נפוץ מאוד.
</p>

<p>
  חשוב להבחין בין שני סוגים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>Cumulative Pref (מצטבר):</strong> אם שנה מסוימת לא הניבה
    מספיק Cash Flow לשלם את ה-Pref המלא — ה-Pref הלא-ששולם מצטבר
    לשנים הבאות. ה-GP לא יקבל Promote עד שה-LP קיבל את כל הצבירה.
  </li>
  <li>
    <strong>Non-Cumulative Pref:</strong> כל שנה מחושבת בנפרד. אם
    ה-Cash Flow לא הספיק — ה-LP הפסיד את ה-Pref לאותה שנה. זה פחות
    נפוץ ופחות מגן על ה-LP.
  </li>
</ul>

<!-- ===== סעיף 3 — IRR Hurdles ו-Promote ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. IRR Hurdles ו-Promote — מנגנון הבונוס ליזם</h3>

<p>
  <strong>IRR Hurdle</strong> הוא סף תשואה פנימית (Internal Rate of Return)
  שמעליו ה-GP מתחיל לקבל חלק גדול יותר מהרווחים — ה-<strong>Promote</strong>
  (הנקרא גם Carried Interest). הרעיון: ה-GP מרוויח יותר רק אם הביא
  תשואה גבוהה עבור המשקיעים.
</p>

<p>
  מבנה Waterfall עם שני IRR Hurdles נראה לרוב כך:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שכבה (Tier)</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תנאי</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">חלוקה LP / GP</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שכבה 1 — החזר הון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עד להשבת 100% מהון ה-LP</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">100% LP / 0% GP</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שכבה 2 — Preferred Return</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עד ל-8% IRR מצטבר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">100% LP / 0% GP</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שכבה 3 — Catch-Up</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">IRR 8%–12%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">80% LP / 20% GP</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שכבה 4 — Super-Promote</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מעל IRR 12%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">70% LP / 30% GP</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 4 — דוגמה מספרית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. דוגמה מספרית: עסקה של $10M</h3>

<p>
  נניח עסקת נדל&quot;ן מסחרי:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;font-size:13px;">
  שווי רכישה: $10,000,000<br>
  מימון בנקאי (Senior Debt): $7,000,000 (70% LTV)<br>
  הון עצמי כולל: $3,000,000<br>
  — LP משקיע 90%: $2,700,000<br>
  — GP משקיע 10%: $300,000<br>
  Preferred Return: 8% לשנה (Cumulative)<br>
  Promote מעל IRR 12%: 20% GP / 80% LP<br>
  <br>
  שנה 5 — תמורה ממכירה לאחר פירעון חוב: $4,500,000 לחלוקה בין LP ו-GP
</div>

<p>
  <strong>חישוב הWaterfall:</strong>
</p>

<ol style="line-height:1.9;font-size:13px;">
  <li>
    <strong>שכבה 1 — החזר הון LP:</strong> $2,700,000 → LP קיבל.
    נשאר לחלוקה: $4,500,000 − $2,700,000 = $1,800,000
  </li>
  <li>
    <strong>שכבה 2 — Preferred Return LP 8% × 5 שנים:</strong>
    $2,700,000 × 8% × 5 = $1,080,000 → LP קיבל.
    נשאר: $1,800,000 − $1,080,000 = $720,000
  </li>
  <li>
    <strong>שכבה 3 — רווח נוסף (IRR 8%–12%):</strong>
    80% LP / 20% GP: LP מקבל $576,000, GP מקבל $144,000.
    (נניח שה-$720,000 כולם ב-Tier 3 לצורך הפשטה.)
  </li>
  <li>
    <strong>GP מסכום כולל:</strong> $300,000 (הון עצמי) + $144,000 (Promote)
    = $444,000 — תשואה של ~48% על הון ה-GP.
  </li>
</ol>

<!-- ===== סעיף 5 — נקודת מבט המלווה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. נקודת מבט המלווה הבכיר מול משקיע ההון</h3>

<p>
  המלווה הבנקאי (Senior Lender) <em>אינו</em> חלק מה-Waterfall — הוא
  מקבל תשלומי ריבית וקרן לפי לוח הסילוקין, <strong>לפני</strong> כל
  חלוקה ל-LP או ל-GP. בטרם מתחילה חלוקת ה-Waterfall, שירות חוב הבנק
  כבר שולם מ-NOI הנכס.
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>הבנק מקדים את כולם:</strong> אם ה-NOI אינו מספיק לשירות
    החוב — לא LP ולא GP לא מקבלים דבר, והבנק פותח בהליכי אכיפה.
  </li>
  <li>
    <strong>ה-Promote לא מדאיג את הבנק ישירות:</strong> אולם מבנה
    Waterfall שמחייב הזרמת Cash Flow גדולה ל-GP מוקדם יכול לדלל
    את הרזרבות של הפרויקט — ולהגדיל סיכון אם ה-NOI ייחלש.
  </li>
  <li>
    <strong>אנליסט בנק צריך לשאול:</strong> האם לאחר שירות החוב
    ותשלומי ה-Pref ל-LP נשאר מספיק Cash Flow לתחזוקה, רזרבות
    ובלתי-צפוי? Waterfall שמנצל כל שקל של Cash Flow הוא דגל אדום.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה: Waterfall כמסך לסיכון אמיתי</strong><br>
  יזמים לעיתים מציגים עסקה עם &quot;Preferred Return גבוה ל-LP&quot; כסימן
  לבטיחות. אך אם ה-Pref מימון ממחזור חוב ולא מ-NOI אמיתי — המבנה
  כולו מרעוש. ה-Pref לא מחליף ניתוח NOI עצמאי.
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מבנה Waterfall, ההבחנה בין LP ל-GP, "
    "Preferred Return, IRR Hurdles, Promote, ונקודת מבט המלווה הבכיר. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים חישוב חלוקת תמורה לפי Waterfall נתון, "
    "זיהוי IRR Hurdles בהסכם שותפות, קריאת מבנה Promote ועריכת טבלת חלוקה, "
    "והערכת השפעת מבנה Waterfall על יכולת שירות חוב הבנק. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — מבני Waterfall ועסקאות מורכבות
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>Waterfall הוא מנגנון קדימויות חלוקת Cash Flow בין LP ל-GP.</strong>
    ה-LP מקבל ראשון — החזר הון + Preferred Return — ורק לאחר מכן ה-GP מקבל Promote.
  </li>
  <li>
    <strong>Preferred Return (8% מקובל) מגן על ה-LP, Cumulative Pref מגן יותר מ-Non-Cumulative.</strong>
    Pref צבירה מבטיחה שה-LP קיבל את כל תשואתו המינימלית לפני חלוקת Promote.
  </li>
  <li>
    <strong>IRR Hurdles קובעים מתי ה-GP מתחיל לקבל Promote גדול יותר.</strong>
    שני Hurdles נפוצים: Hurdle ראשון 8%–10%, Hurdle שני 12%–15%.
  </li>
  <li>
    <strong>המלווה הבנקאי קודם לכל שכבות ה-Waterfall — הוא מחוץ למשחק ה-Promote.</strong>
    שירות החוב שולם מ-NOI לפני כל חלוקה להון.
  </li>
  <li>
    <strong>Waterfall שמנצל 100% מהCash Flow ללא רזרבה הוא סיכון נסתר.</strong>
    בדוק שנשאר מרווח לתחזוקה, CAPEX בלתי-מתוכנן, ותרחיש פנוי גבוה.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מפל חלוקה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Waterfall</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סדר קדימויות חלוקת Cash Flow בין שכבות משקיעים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תשואה מועדפת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Preferred Return</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשואה שנתית מינימלית ל-LP לפני Promote</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בונוס יזם</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Promote / Carried Interest</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חלק ה-GP ברווחים מעל ה-Hurdle</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סף תשואה פנימית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">IRR Hurdle</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סף IRR המפעיל שכבת חלוקה גבוהה יותר ל-GP</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שותף מוגבל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">LP — Limited Partner</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">משקיע פסיבי המספק רוב הון העצמי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שותף כללי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">GP — General Partner</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">יזם / מנהל הפרויקט המקבל Promote</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — Stress Testing ותיק הלוואות
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  Stress Testing ותיק הלוואות
</h2>

<!-- ===== סעיף 1 — Stress Testing ברמת תיק ===== -->
<h3 style="color:#1a2638;">1. Stress Testing ברמת תיק — מעבר לעסקה הבודדת</h3>

<p>
  Stress Testing ברמת עסקה בודדת — שלמדנו בקורסים קודמים — בוחן מה
  קורה לנכס ספציפי אם ה-NOI יורד או הריבית עולה. אולם <strong>Stress Testing
  ברמת תיק (Portfolio-Level)</strong> שונה: הוא בוחן מה קורה לכלל תיק
  ההלוואות של הבנק כשמספר נכסים בו נפגעים <em>בו-זמנית</em> — כפי שקורה
  בזמן מיתון כלכלי.
</p>

<p>
  ברמת התיק, שני מושגים קריטיים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>קורלציה (Correlation):</strong> מידת ההתאמה בין ביצועי נכסים
    שונים. נכסים בעלי קורלציה גבוהה — למשל שני מרכזי קניות בתל אביב —
    יסבלו באותו זמן בזמן מיתון. נכסים עם קורלציה נמוכה — כלומר, מחסן
    לוגיסטי ביישוב פריפריאלי ודירות להשכרה במרכז — מגוונים את הסיכון.
  </li>
  <li>
    <strong>קורלציה בזמן משבר (Stress Correlation):</strong> גם נכסים
    שנראו בלתי-תלויים בתקופה נורמלית עלולים להתאם בחוזקה בזמן משבר.
    2008 לימד אותנו שכאשר שוק האשראי נעצר — גם נכסים "מגוונים" נופלים יחד.
  </li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל לאנליסט:</strong><br>
  גיוון תיק מגן ב&quot;יום רגיל&quot;. בזמן משבר — הגנת הגיוון נחלשת.
  Stress Test חייב להניח קורלציה גבוהה יותר מזו שנמדדה בעבר.
</div>

<!-- ===== סעיף 2 — סיכון ריכוז ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. סיכון ריכוז — גיאוגרפי, ענפי ולווה</h3>

<p>
  <strong>Concentration Risk</strong> — סיכון ריכוז — מתממש כאשר תיק
  ההלוואות מרוכז מדי בממד אחד, כך שזעזוע ספציפי פוגע בחלק גדול מהתיק
  בו-זמנית.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג ריכוז</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">דוגמה לסיכון</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סימן לריכוז מסוכן</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גיאוגרפי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">80% מהתיק בתל אביב — נפגע ממשבר מקומי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מעל 40% בעיר / אזור אחד</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ענפי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">70% משרדים — נפגע ממעבר לעבודה מהבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מעל 35% בסוג נכס אחד</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">לווה בודד</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">קבוצת לווים קשורים שמחזיקה 15% מהתיק</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מעל 10% מהתיק בקבוצה קשורה</td>
    </tr>
  </tbody>
</table>

<p>
  בנק ישראל מגדיר <strong>Large Exposure</strong> — חשיפה גדולה — כאשר
  סך ההלוואות ללווה בודד (או קבוצת לווים קשורים) עולה על 10% מהון הבנק.
  חריגה מ-25% מחייבת אישור מיוחד.
</p>

<!-- ===== סעיף 3 — מסגרות רגולטוריות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. מסגרות רגולטוריות — IFRS 9 ובאזל</h3>

<p>
  שני מסגרות רגולטוריות מרכזיות מחייבות ביצוע Stress Testing שיטתי:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>IFRS 9 — מודל הפסד צפוי (ECL — Expected Credit Loss):</strong>
    התקן החשבונאי הבינלאומי שנכנס לתוקף ב-2018. דורש מבנקים לחשב
    הפסד צפוי על כל הלוואה — לא רק על הלוואות שנפגעו בפועל. ה-ECL
    מחושב בשלושה שלבים (Stage 1/2/3) לפי רמת ירידה באיכות אשראי.
  </li>
  <li>
    <strong>Basel III / IV — Stress Testing הוני:</strong>
    מסגרת רגולטורית של ועדת באזל המחייבת בנקים לבצע Stress Test
    על הון הרגולטורי (Capital Adequacy). תרחישי קיצון נקבעים על-ידי
    הרגולטור — בישראל, בנק ישראל מפרסם תרחישים פעם בשנה.
  </li>
</ul>

<p>
  <strong>משמעות מעשית לאנליסט:</strong> הפרשות IFRS 9 בדוחות הבנק
  הן אינדיקטור לאיכות תיק ההלוואות. גידול חד בהפרשות Stage 2
  (ירידה באיכות אשראי, ללא כשל עדיין) הוא אות אזהרה מוקדם.
</p>

<!-- ===== סעיף 4 — בניית מודל Stress פשוט ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. בניית מודל Stress פשוט לתיק נדל&quot;ן</h3>

<p>
  נדגים Stress Test ברמת תיק על שלושה נכסים מייצגים:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;font-size:13px;">
  תיק לדוגמה (סכומי הלוואה, NOI שנתי, Cap Rate, שווי נכס, LTV):<br><br>
  נכס A — משרדים, תל אביב:<br>
  &nbsp;&nbsp;הלוואה: ₪8M | NOI: ₪600K | Cap Rate: 6% | שווי: ₪10M | LTV: 80%<br><br>
  נכס B — מגורים להשכרה, חיפה:<br>
  &nbsp;&nbsp;הלוואה: ₪4M | NOI: ₪300K | Cap Rate: 5% | שווי: ₪6M | LTV: 67%<br><br>
  נכס C — לוגיסטיקה, אשדוד:<br>
  &nbsp;&nbsp;הלוואה: ₪6M | NOI: ₪480K | Cap Rate: 6.5% | שווי: ₪7.4M | LTV: 81%
</div>

<p>
  <strong>תרחיש Stress:</strong> NOI יורד 20%, Cap Rate עולה 1% (נכסים
  נראים מסוכנים יותר בשוק).
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;font-size:13px;">
  נכס A לאחר Stress:<br>
  &nbsp;&nbsp;NOI חדש: ₪600K × 0.8 = ₪480K<br>
  &nbsp;&nbsp;שווי חדש: ₪480K / (6% + 1%) = ₪480K / 7% = ₪6.86M<br>
  &nbsp;&nbsp;LTV חדש: ₪8M / ₪6.86M = 116.6% — הפרת Covenant חמורה!<br><br>
  נכס B לאחר Stress:<br>
  &nbsp;&nbsp;NOI חדש: ₪300K × 0.8 = ₪240K<br>
  &nbsp;&nbsp;שווי חדש: ₪240K / (5% + 1%) = ₪4M<br>
  &nbsp;&nbsp;LTV חדש: ₪4M / ₪4M = 100% — הפרת Covenant<br><br>
  נכס C לאחר Stress:<br>
  &nbsp;&nbsp;NOI חדש: ₪480K × 0.8 = ₪384K<br>
  &nbsp;&nbsp;שווי חדש: ₪384K / 7.5% = ₪5.12M<br>
  &nbsp;&nbsp;LTV חדש: ₪6M / ₪5.12M = 117.2% — הפרת Covenant חמורה
</div>

<p>
  <strong>מסקנת ה-Stress Test:</strong> שלושת הנכסים יפרו Covenants
  תחת תרחיש הlמיתון. הבנק נדרש להגדיל הפרשות משמעותית ולפתוח בתהליכי
  Workout עם שלושת הלווים בו-זמנית — עומס תפעולי ורגולטורי כבד.
</p>

<!-- ===== סעיף 5 — תגובת הבנק לתוצאות Stress ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. תגובת הבנק לתוצאות Stress Test</h3>

<ul style="line-height:1.9;">
  <li>
    <strong>הגדלת הפרשה (Provisioning):</strong> נכסים שה-Stress Test
    מראה סיכון גבוה לכשל עוברים לסיווג Watchlist / Stage 2 עם
    הגדלת הפרשה מ-1% ל-10%–25%.
  </li>
  <li>
    <strong>הפחתת מגבלות ריכוז:</strong> אם התיק ריכוזי מדי — הנחיה
    לא לאשר הלוואות חדשות מאותו סוג נכס / אזור עד לאיזון.
  </li>
  <li>
    <strong>הגדלת רזרבות הון:</strong> תוצאות Stress רעות מחייבות
    גיוס הון נוסף (Capital Raise) לעמידה ב-Capital Adequacy Ratio.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>טעות נפוצה: Stress Test כ&quot;תרגיל לרגולטור&quot;</strong><br>
  Stress Test שמבוצע רק כי הרגולטור דורש — ובעל הנחות שמיוצרות
  לכשל — הוא חסר ערך. Stress Test אמיתי משתמש בתרחישים שמנהלי
  הסיכון מאמינים שיכולים להתרחש. תרחיש שנראה &quot;קיצוני&quot; ב-2006
  התממש ב-2008. תכנן למה שקשה לחשוב עליו — לא רק למה שנוח.
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של Stress Testing ברמת תיק, קורלציה בין נכסים, "
    "סיכון ריכוז, מסגרות IFRS 9 ובאזל, ובניית מודל Stress פשוט. "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים ביצוע Stress Test על תיק נכסים נתון "
    "לפי תרחיש NOI-20% ו-Cap Rate+1%, זיהוי ריכוז מסוכן בתיק, "
    "חישוב LTV לאחר Stress והשוואה ל-Covenant, "
    "וסיווג הלוואות ב-IFRS 9 Stage 1/2/3 לאחר תוצאות Stress. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — Stress Testing ותיק הלוואות
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>Stress Testing ברמת תיק בוחן את כל הנכסים בו-זמנית — לא כל עסקה בנפרד.</strong>
    בזמן משבר, גם נכסים שנראו מגוונים עלולים ליפול יחד עקב קורלציה גבוהה.
  </li>
  <li>
    <strong>Concentration Risk — גיאוגרפי, ענפי, ולווה בודד — מגביר נזק Stress.</strong>
    Large Exposure מעל 10% מהון הבנק מחייב ניטור מוגבר ואישור מיוחד.
  </li>
  <li>
    <strong>IFRS 9 מחייב הפרשת ECL על כל הלוואה — לא רק על נכשלות.</strong>
    Stage 2 (ירידה בדרוג) הוא אות אזהרה מוקדם שחשוב לעקוב אחריו.
  </li>
  <li>
    <strong>תרחיש מפתח: NOI -20% + Cap Rate +1% — בדוק מה קורה ל-LTV ול-DSCR.</strong>
    רוב הנכסים בעלי LTV מעל 70% יפרו Covenant בתרחיש זה.
  </li>
  <li>
    <strong>Stress Test אמיתי מוביל לפעולה — הגדלת הפרשה, הפחתת ריכוז, גיוס הון.</strong>
    תרגיל שלא מוביל לפעולה אינו Stress Test — הוא דיווח רגולטורי בלבד.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מבחן עמידות תיק</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Portfolio Stress Test</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתוח השפעת תרחיש קיצון על כלל תיק ההלוואות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קורלציה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Correlation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מידת ההתאמה בין ביצועי נכסים שונים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סיכון ריכוז</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Concentration Risk</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חשיפה גבוהה מדי לממד אחד בתיק</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הפסד צפוי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ECL — Expected Credit Loss</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הפרשה פרו-אקטיבית לפי IFRS 9</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חשיפה גדולה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Large Exposure</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חשיפה ללווה בודד מעל 10% מהון הבנק</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">יחס הלימות הון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Capital Adequacy Ratio</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">יחס ההון הרגולטורי לנכסי סיכון</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — בקרה ואימות מודלים פיננסיים
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  בקרה ואימות מודלים פיננסיים
</h2>

<!-- ===== סעיף 1 — מה זה אימות מודל ===== -->
<h3 style="color:#1a2638;">1. אימות מודל (Model Validation) — מה ולמה?</h3>

<p>
  <strong>Model Validation</strong> — אימות מודל — הוא תהליך סקירה
  עצמאית של מודל פיננסי, שמטרתו לוודא שהמודל:
</p>

<ul style="line-height:1.9;">
  <li>בנוי נכון מבחינה מתמטית ולוגית</li>
  <li>מבוסס על הנחות מציאותיות ומתועדות</li>
  <li>מייצג נאמנה את מה שהוא אמור לייצג</li>
  <li>מוביל להחלטות אשראי שניתן להגן עליהן</li>
</ul>

<p>
  מדוע סקירה <em>עצמאית</em>? כי מי שבנה את המודל "עיוור לשגיאות שלו".
  מחקרים מראים שכ-88% מגליונות Excel מסחריים מכילים שגיאה אחת לפחות.
  בהחלטות אשראי של עשרות מיליוני שקלים — שגיאה אחת עלולה להיות קטסטרופלית.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל הסקירה העצמאית:</strong><br>
  מודל פיננסי שמשמש להחלטת אשראי מעל סכום מסוים (בנקים רבים: מעל
  ₪5M) חייב לעבור אימות על-ידי אנליסט שלא השתתף בבנייתו.
  הסוקר חותם על גיליון אימות נפרד — ומגיש אותו לוועדת אשראי.
</div>

<!-- ===== סעיף 2 — שגיאות מודל נפוצות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. שגיאות מודל נפוצות — Excel, לוגיקה והפניות מעגליות</h3>

<p>
  קטגוריות השגיאות הנפוצות ביותר במודלים פיננסיים לנדל&quot;ן:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג שגיאה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תיאור</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">כיצד מזהים</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Hard-Coded Value</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ערך קבוע שנקלד בתוך נוסחה (למשל =A1*0.065)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Ctrl+` בExcel — מציג נוסחאות; חפש ספרות בתוך נוסחאות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הפניה מעגלית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תא A מחשב לפי תא B שמחשב לפי תא A — לולאה אינסופית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Excel מציג אזהרה; בדוק "Circular References" בFormulas</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">טעות יחידות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בלבול בין ₪ לאלפי ₪, בין חודשי לשנתי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדוק כותרות עמודות; sanity check עם ערכי שוק</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הנחות לא-מתועדות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cap Rate, שיעור פנוי — הנחה שנקלטה ללא הצדקה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דרוש גיליון Assumptions נפרד עם מקורות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שגיאת טווח (Range Error)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">SUM שמחשב טווח לא נכון — שורה חסרה או עודפת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הדגשת טווח כל SUM ובדיקה ויזואלית</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 3 — רשימת תיוג לאימות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. רשימת תיוג לאימות מודל — Model Audit Checklist</h3>

<p>
  אנליסט שמבצע אימות מודל צריך לעבור על הרשימה הבאה:
</p>

<ol style="line-height:1.9;">
  <li>
    <strong>גיליון הנחות (Assumptions Sheet):</strong> האם כל ההנחות
    מרוכזות בגיליון נפרד? האם יש מקורות ותאריכים לכל הנחה?
  </li>
  <li>
    <strong>בדיקת קצוות (Boundary Check):</strong> הזן NOI = 0 — האם
    המודל מתפקד? Cap Rate = 0.01%? ריבית = 20%? שגיאות בקצוות
    מגלות בעיות לוגיקה.
  </li>
  <li>
    <strong>בדיקת Audit Trail:</strong> האם ניתן לעקוב מכל ערך פלט
    חזרה להנחת הקלט? מודל שחישובי הביניים חבויים — לא עמיד לאימות.
  </li>
  <li>
    <strong>Sanity Check עם שוק:</strong> האם ה-NOI הסופי מתאים
    לנכסים דומים בשוק? Cap Rate מחושב — האם סביר לפי עסקאות שנמכרו?
  </li>
  <li>
    <strong>Sensitivity Analysis:</strong> שנה את ה-Cap Rate ב-+1%
    — האם השפעה על ה-LTV הגיונית? שנה ריבית — האם ה-DSCR מגיב כצפוי?
  </li>
  <li>
    <strong>רוויזיה מגרסה:</strong> האם הגרסה ש-Sign Off עליה היא
    הגרסה האחרונה? בדוק תאריך שמירה ומספר גרסה בשם הקובץ.
  </li>
</ol>

<!-- ===== סעיף 4 — "Hockey Stick" ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. זיהוי ואתגור תחזית &quot;Hockey Stick&quot;</h3>

<p>
  <strong>Hockey Stick Projection</strong> — תחזית מקל הוקי — היא
  תחזית שמציגה ביצועים נמוכים לתקופה הקרובה ואז עלייה חדה ופתאומית
  בעתיד. הגרף דומה למקל הוקי: ידית שטוחה, ואז קצה מעוקל חדה כלפי מעלה.
</p>

<p>
  תחזיות Hockey Stick נפוצות בתוכניות עסקיות של לווים שמנסים להצדיק
  מימון עבור פרויקטים בעייתיים. כיצד לאתגר:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>שאל "מה ישתנה בשנה X?"</strong> אם היזם מניח קפיצה
    בהכנסות בשנה 3 — מה הסיבה הספציפית? חתימת שוכר עוגן? סיום
    שיפוץ? חסם רגולטורי שיוסר? אם הסיבה מעורפלת — ספג אותה ב-Sensitivity.
  </li>
  <li>
    <strong>השווה לביצועים היסטוריים:</strong> אם הנכס ביצע X%
    צמיחה בשלוש השנים האחרונות — מדוע הוא יצמח 3X בשנים הבאות?
  </li>
  <li>
    <strong>הכנס תרחיש Base ו-Downside:</strong> מדל את תרחיש
    ה-Upside של הלווה, ולצדו תרחיש Base (ממוצע ענפי) ו-Downside
    (תרחיש שמרני). אם ה-DSCR נשאר מעל 1.0 רק ב-Upside — סיכון גבוה.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אמרת אצבע:</strong><br>
  &quot;אם מודל עובד רק בתרחיש האופטימי — הוא לא מודל, הוא משאלת לב.&quot;<br>
  מזכר האשראי חייב לנתח Base Case, לא רק Best Case.
</div>

<!-- ===== סעיף 5 — תיעוד מודלים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. תיעוד מודלים — סטנדרטים להחלטות אשראי</h3>

<p>
  מודל פיננסי שמשמש להחלטת אשראי חייב להיות מתועד כך שאנליסט חדש
  יוכל להבין ולאמת אותו תוך שעה. סטנדרטי תיעוד:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>שם קובץ עם גרסה ותאריך:</strong>
    למשל: <code>DEAL_A_Model_v3.2_2026-05-19.xlsx</code>
  </li>
  <li>
    <strong>גיליון Cover Sheet:</strong> שם עסקה, שם בונה המודל,
    שם מאמת, תאריך אחרון שנבדק, וסיכום ממצאי אימות.
  </li>
  <li>
    <strong>הנחות מקובצות (Assumptions Tab):</strong> כל הנחה
    בשורה נפרדת — עם מקור, ערך Base Case, ערך Downside.
  </li>
  <li>
    <strong>הפרדת קלט/פלט:</strong> תאי קלט (ניתנים לשינוי) —
    בצבע שונה (בדרך כלל כחול); תאי חישוב — לא לעריכה ישירה.
  </li>
  <li>
    <strong>Sensitivity Table מוכן:</strong> טבלת רגישות NOI × Cap
    Rate בגיליון נפרד — מאפשרת לוועדת האשראי לראות מגוון תרחישים
    ללא עריכת המודל עצמו.
  </li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לקורס 10 — ניתוח תרחישי סיכון:</strong><br>
  בקורס זה למדנו לבנות ולאמת מודלים פיננסיים מתקדמים — ממבני
  Waterfall ועסקאות מורכבות, דרך Stress Testing ברמת תיק, ועד
  סטנדרטי בקרה ואימות. קורס 10 ייקח את כלי הניתוח הללו צעד קדימה:
  נבנה מסגרת מלאה לניתוח תרחישי סיכון רב-ממדיים — Monte Carlo,
  רגישות רב-משתנית, ומודלים להערכת הסתברות כשל — הכלים שמשלימים את
  ארגז הכלים המקצועי של אנליסט אשראי בנדל&quot;ן בעולם האמיתי.
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של אימות מודל עצמאי, שגיאות נפוצות במודלים פיננסיים, "
    "רשימת תיוג לאימות, זיהוי תחזיות Hockey Stick, וסטנדרטי תיעוד מודלים. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים זיהוי שגיאות במודל Excel נתון, "
    "ביצוע Boundary Check על מודל NOI, אתגור תחזית Hockey Stick עם בניית "
    "תרחיש Base ו-Downside, ובדיקת מודל נגד רשימת תיוג האימות המלאה. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — בקרה ואימות מודלים פיננסיים
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>אימות מודל עצמאי הוא חובה — לא אופציה — בהחלטות אשראי.</strong>
    88% ממודלי Excel מסחריים מכילים שגיאה אחת לפחות; בסכומים גדולים שגיאה אחת = הפסד גדול.
  </li>
  <li>
    <strong>השגיאות הנפוצות: Hard-Coded Values, הפניות מעגליות, טעויות יחידות, הנחות לא-מתועדות.</strong>
    Ctrl+` ו-Boundary Check הם כלי האימות הבסיסיים שכל אנליסט חייב לשלוט בהם.
  </li>
  <li>
    <strong>Model Audit Checklist: גיליון הנחות, בדיקת קצוות, Audit Trail, Sanity Check, Sensitivity.</strong>
    מודל שלא עובר כל שלב ברשימה — לא מוכן לוועדת אשראי.
  </li>
  <li>
    <strong>תחזית Hockey Stick = דגל אדום. אתגר ב-Base Case ו-Downside.</strong>
    אם DSCR מעל 1.0 רק ב-Upside — הסיכון גבוה מדי לאשראי סטנדרטי.
  </li>
  <li>
    <strong>תיעוד מודל: שם קובץ עם גרסה, Cover Sheet, Assumptions Tab, הפרדת קלט/פלט, Sensitivity Table.</strong>
    מודל מתועד היטב מגן על האנליסט, על הבנק, ועל החלטת האשראי.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אימות מודל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Model Validation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סקירה עצמאית של מודל פיננסי לפני שימוש</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ערך קבוע מקולד</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Hard-Coded Value</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ספרה שנקלדה ישירות בנוסחה ולא מקושרת לתא הנחה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הפניה מעגלית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Circular Reference</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תא המתייחס לעצמו דרך שרשרת תלויות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תחזית מקל הוקי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Hockey Stick Projection</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תחזית עם עלייה פתאומית בלתי-מוצדקת בעתיד</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בדיקת קצוות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Boundary Check</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בחינת מודל עם ערכי קיצון לאיתור שגיאות לוגיקה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח רגישות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Sensitivity Analysis</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בחינת השפעת שינוי הנחה אחת על תוצאות המודל</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לקורס 10 — ניתוח תרחישי סיכון:</strong><br>
  השלמתם את שישת מודולי קורס 9 — מודלים פיננסיים מתקדמים. כלי
  הניתוח שרכשתם — Waterfall, Stress Testing ברמת תיק, ואימות מודלים
  — הם הבסיס לקורס 10: ניתוח תרחישי סיכון. שם תבנו מסגרות ניתוח
  רב-ממדיות ותלמדו להציג ממצאי סיכון לוועדת אשראי בצורה מקצועית
  ומבוססת-נתונים.
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "מבני Waterfall ועסקאות מורכבות",
        "slug": "mivney-waterfall-askayot-murkavot",
        "estimated_minutes": 60,
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
                "body_html_he": "<p>ענה על שאלות ההבנה הבאות.</p>",
                "instructions_he": M4_COMPREHENSION_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.EXERCISES,
                "order": 3,
                "body_html_he": "<p>פתור את התרגילים הבאים.</p>",
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
        "title_he": "Stress Testing ותיק הלוואות",
        "slug": "stress-testing-tik-halvahot",
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
                "body_html_he": "<p>ענה על שאלות ההבנה הבאות.</p>",
                "instructions_he": M5_COMPREHENSION_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.EXERCISES,
                "order": 3,
                "body_html_he": "<p>פתור את התרגילים הבאים.</p>",
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
        "title_he": "בקרה ואימות מודלים פיננסיים",
        "slug": "bikora-vaimut-modelim-pinansiim",
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
                "body_html_he": "<p>ענה על שאלות ההבנה הבאות.</p>",
                "instructions_he": M6_COMPREHENSION_INSTRUCTIONS,
            },
            {
                "component_type": ComponentType.EXERCISES,
                "order": 3,
                "body_html_he": "<p>פתור את התרגילים הבאים.</p>",
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
    help = "Seeds Module 4-6 content for Course 9 (מודלים פיננסיים מתקדמים)"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=9)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 9 not found. Run 'python manage.py seed_data' first."
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
