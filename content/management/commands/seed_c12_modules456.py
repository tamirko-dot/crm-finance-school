"""
Seeds Module 4-6 content for Course 12 (פרויקט גמר — מימון נדל"ן).
Usage: python manage.py seed_c12_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — בניית המודל הפיננסי לפרויקט הגמר
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  בניית המודל הפיננסי לפרויקט הגמר
</h2>

<!-- ===== סעיף 1 — מבנה המודל הנדרש ===== -->
<h3 style="color:#1a2638;">1. מבנה המודל הפיננסי הנדרש בפרויקט הגמר</h3>

<p>
  מודל פיננסי תקין לפרויקט הגמר חייב לכלול חמישה רכיבים מוגדרים,
  מוצגים בפורמט טבלאי ברור ומתויג. כל רכיב בא בתוספת הנחות מפורשות
  ומקורות נתונים.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">רכיב</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תוכן נדרש</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">טווח זמן</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">טבלת NOI</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">GPR ← שיעור פנוי ← EGI ← הוצאות תפעול ← NOI, שנה-שנה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שנות הפרויקט המלאות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">טבלת DSCR</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI חלקי שירות חוב שנתי, 3 שנים + תרחיש לחץ</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שנים 1–3 + Stress</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חישוב LTV</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">יתרת הלוואה חלקי שווי שוק מוערך (Appraised Value)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נקודת הנפקה + שנה 3</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Debt Yield</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI שנתי חלקי יתרת קרן ההלוואה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Base Case + Bear Case</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שווי יציאה ותשואה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Exit Value (NOI/Cap Rate), IRR, ומכפיל ההון (Equity Multiple)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תאריך יציאה מתוכנן</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 2 — נירמול NOI ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. נירמול NOI — שלב-שלב מנתוני העסקה</h3>

<p>
  נירמול ה-NOI הוא הצעד הראשון והקריטי ביותר בבניית המודל.
  הנה רצף הצעדים לביצוע:
</p>

<ol style="line-height:1.9;">
  <li>
    <strong>קביעת GPR (Gross Potential Rent):</strong> כפל שטח מושכר
    במחיר שכירות שוק לפי מ"ר. השתמש בנתוני שוק עדכניים — לא בהצעת
    הלווה בלבד. תעד את מקור המחיר.
  </li>
  <li>
    <strong>הפחתת שיעור פנוי (Vacancy):</strong> הפחת את ה-GPR לפי
    שיעור פנוי מייצג של האזור והסוג. בדוק שיעור פנוי היסטורי 3–5
    שנים, לא רק הנוכחי. הפעל שיעור פנוי בגובה 5%–10% לפחות.
  </li>
  <li>
    <strong>חישוב EGI (Effective Gross Income):</strong> GPR פחות אובדן
    שכירות משיעור הפנוי, בתוספת הכנסות אחרות (חניה, שירותים, פרסום).
  </li>
  <li>
    <strong>הפחתת הוצאות תפעול (Operating Expenses):</strong> ארנונה,
    ביטוח, ניהול נכסים, תחזוקה, CapEx שוטף. <strong>אסור להזניח CapEx</strong>
    — השתמש ב-1%–2% משווי הנכס לשנה.
  </li>
  <li>
    <strong>NOI = EGI − Operating Expenses.</strong> זה המספר שישמש
    לחישוב DSCR, Debt Yield, ושווי הנכס. תעד כל הנחה.
  </li>
</ol>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה:</strong><br>
  מודל עם שורת NOI אחת ללא הנחות מפורטות — אינו מודל, הוא ניחוש
</div>

<!-- ===== סעיף 3 — ניתוח תרחישים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. דרישת ניתוח התרחישים — מינימום 3 תרחישים</h3>

<p>
  המודל הפיננסי חייב לכלול שלושה תרחישים לפחות, עם הנחות שונות
  לכל אחד:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תרחיש</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הנחות מרכזיות</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מטרה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Base Case</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוק נוכחי, תפוסה מייצגת, ריבית כפי שהוצעה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מקרה הבסיס הסביר — מה שאתה מצפה שיקרה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Bear Case</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שכירות ירדה 10%, פנוי עלה ל-15%, עלויות עלו 5%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תרחיש שוק שלילי — האם ה-DSCR עדיין מעל 1.0?</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Stress Case</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שכירות ירדה 20%, פנוי 25%, ריבית עלתה 200bps</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תרחיש קיצון — מתי נשברת ההלוואה?</td>
    </tr>
  </tbody>
</table>

<p>
  לכל תרחיש — הצג את ה-NOI, DSCR, ו-Debt Yield המחושבים.
  הסבר בגוף המזכר מה משמעות כל תוצאה מבחינת ועדת האשראי.
</p>

<!-- ===== סעיף 4 — מה המודל לא יעשה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. מה המודל חייב שלא לעשות</h3>

<ul style="line-height:1.9;">
  <li>
    <strong>לא להציג NOI שנה אחת בלבד ללא פריסה שנתית.</strong>
    NOI ללא תחזית שנתית אינו מאפשר לראות אם הפרויקט מייצב, גדל, או נשחק.
  </li>
  <li>
    <strong>לא להזניח שיעור פנוי.</strong>
    NOI שמניח תפוסה מלאה (100%) — לא מציאותי ופוסל את המודל.
  </li>
  <li>
    <strong>לא להניח CapEx אפס.</strong>
    כל נכס מייצר הוצאות תחזוקה שוטפות. מודל ללא CapEx מנפח את ה-NOI
    ומטעה את ועדת האשראי.
  </li>
</ul>

<!-- ===== סעיף 5 — הצגת המודל במזכר ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. הצגת המודל במזכר האשראי</h3>

<p>
  טבלאות המודל הפיננסי המופיעות במזכר חייבות לעמוד בארבעה קריטריונים:
</p>

<ol style="line-height:1.9;">
  <li>
    <strong>קריאות:</strong> פונט בגודל סביר, שורות מוגדרות, מספרים
    מיושרים. אין לצרף צילום מסך של Excel עמוס ובלתי-קריא.
  </li>
  <li>
    <strong>תיוג:</strong> כל שורה ועמודה מתוייגים בשמם המלא.
    אין "Row 1", "Col A" — רק שמות מדדים מפורשים.
  </li>
  <li>
    <strong>מקורות:</strong> כל הנחה מפנה למקור — דוחות כספיים, נתוני
    שוק, הצעת הלווה, הערכת שמאי.
  </li>
  <li>
    <strong>עקביות:</strong> המספרים בטבלאות המודל חייבים להתאים
    בדיוק למספרים בגוף המזכר. כל אי-התאמה היא כישלון אוטומטי.
  </li>
</ol>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>נקודת מפתח של הוועדה:</strong><br>
  ה-Debt Yield הוא המדד שהוועדה תתמקד בו — ודא שהוא מעל 7.5% ב-Base Case
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות. "
    "כל שאלה בוחנת הבנה של מבנה המודל הפיננסי הנדרש בפרויקט הגמר: "
    "טבלת NOI, טבלת DSCR, חישוב LTV, Debt Yield, שווי יציאה, "
    "נירמול NOI שלב-שלב, דרישת ניתוח התרחישים, ועקרונות הצגת המודל במזכר. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים בניית טבלת NOI שנתית מנתוני עסקה נתונים, "
    "חישוב DSCR ו-Debt Yield לשלושה תרחישים (Base / Bear / Stress), "
    "חישוב שווי יציאה ו-IRR בהינתן NOI ו-Cap Rate, "
    "וזיהוי שגיאות במודל פיננסי שהוצג. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — בניית המודל הפיננסי לפרויקט הגמר
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>המודל הפיננסי כולל חמישה רכיבים: טבלת NOI, טבלת DSCR, LTV, Debt Yield, ושווי יציאה + IRR.</strong>
    כל רכיב בא עם הנחות מפורשות ומקורות מתועדים.
  </li>
  <li>
    <strong>נירמול NOI עובר 5 שלבים: GPR → שיעור פנוי → EGI → הוצאות תפעול → NOI.</strong>
    CapEx אינו אופציונלי — השתמש ב-1%–2% משווי הנכס לשנה.
  </li>
  <li>
    <strong>ניתוח תרחישים כולל לפחות Base Case, Bear Case, ו-Stress Case.</strong>
    כל תרחיש מציג NOI, DSCR, ו-Debt Yield נפרדים עם הנחות שונות.
  </li>
  <li>
    <strong>המודל לא יכיל NOI חד-שנתי, שיעור פנוי אפס, או CapEx אפס.</strong>
    שלוש שגיאות אלה פוסלות את המודל בעיני ועדת האשראי.
  </li>
  <li>
    <strong>Debt Yield הוא המדד שהוועדה בוחנת ראשון — ודא שהוא מעל 7.5% ב-Base Case.</strong>
    טבלאות קריאות, מתוייגות ועקביות עם גוף המזכר הן תנאי סף — לא בונוס.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הכנסת שכירות ברוטו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">GPR — Gross Potential Rent</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכנסה פוטנציאלית בתפוסה מלאה לפי מחיר שוק</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הכנסה ברוטו אפקטיבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">EGI — Effective Gross Income</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">GPR פחות אובדן מפנוי בתוספת הכנסות אחרות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הכנסה תפעולית נטו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI — Net Operating Income</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">EGI פחות הוצאות תפעול (לפני חוב ומס)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">יחס כיסוי שירות חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR — Debt Service Coverage Ratio</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI חלקי תשלומי קרן + ריבית שנתיים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תשואת חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Debt Yield</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI שנתי חלקי יתרת קרן ההלוואה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מכפיל הון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Equity Multiple</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סך תקבולי ההון חלקי ההון המושקע</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — כתיבת מזכר האשראי המלא
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  כתיבת מזכר האשראי המלא
</h2>

<!-- ===== סעיף 1 — מבנה מזכר האשראי ===== -->
<h3 style="color:#1a2638;">1. מבנה מזכר האשראי המלא — 8 חלקים ונספחים</h3>

<p>
  מזכר האשראי המלא לפרויקט הגמר חייב לכלול את שמונת הסעיפים הבאים
  בסדר זה, בסך כולל של 12–18 עמודים (לא כולל נספחים):
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">#</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סעיף</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מגבלת אורך / הנחיה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">1</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכום מנהלי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מקסימום עמוד אחד</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">2</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רקע הלווה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניסיון, מינוף, מוניטין</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">3</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תיאור הנכס</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מיקום, שטח, מצב, שוכרים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">4</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתוח פיננסי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פלט המודל: NOI, DSCR, LTV, Debt Yield</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">5</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתוח סיכונים ומיטיגציה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכוני שוק, לווה, בטוחה, רגולציה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">6</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתוח תרחישים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Base / Bear / Stress — טבלה ופרשנות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">7</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תנאים והגבלות מוצעים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סכום, ריבית, תקופה, Covenants, בטחונות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">8</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">המלצה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אשר / דחה / תנאים לאישור — עם נימוק</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>נספחים נדרשים:</strong> (א) רשימת בדיקת נאותות (DD Checklist),
  (ב) הנחות המודל הפיננסי המלאות, (ג) מקורות נתוני שוק.
</p>

<!-- ===== סעיף 2 — אורך ונימה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. אורך המזכר וסטנדרט הנימה</h3>

<p>
  <strong>אורך:</strong> 12–18 עמודים לא כולל נספחים. מזכר קצר מדי (פחות
  מ-12 עמודים) מעיד על ניתוח חלקי. מזכר ארוך מדי (מעל 18 עמודים)
  מעיד על חוסר סינון — ועדת אשראי אינה קוראת עומרות.
</p>

<p>
  <strong>נימה ולשון:</strong>
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>גוף שלישי לאורך כל המזכר:</strong> "הלווה מציג...",
    "הנכס ממוקם...", "הניתוח מעלה...". לא "אני בדקתי" או "לדעתי".
  </li>
  <li>
    <strong>עבר להיסטוריה, הווה לנוכחות, עתיד לתחזיות:</strong>
    "ב-2023 הנכס הניב...", "הנכס מניב כיום...", "הפרויקטציה מניחה...".
  </li>
  <li>
    <strong>פסקאות ממוקדות:</strong> כל פסקה — טענה אחת ורלוונטית.
    אין מידע כללי שאינו קשור לעסקה הספציפית.
  </li>
</ul>

<!-- ===== סעיף 3 — ביקורת עצמית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. ביקורת עצמית לפני הגשה</h3>

<p>
  לפני הגשת המזכר, בצע שתי בדיקות ביקורת:
</p>

<ol style="line-height:1.9;">
  <li>
    <strong>בדיקת עקביות מספרים:</strong> האם כל מספר שמוזכר בגוף
    המזכר (DSCR, NOI, LTV) תואם בדיוק לטבלאות המודל? כל
    סטייה — גם של עשרות שקלים — היא אי-עקביות.
  </li>
  <li>
    <strong>בדיקת מקורות:</strong> האם כל טענה עובדתית — על שוק,
    על הנכס, על הלווה — מגובה במקור מתועד? טענה ללא מקור
    היא ספקולציה, לא ניתוח.
  </li>
</ol>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל הסיכום המנהלי:</strong><br>
  הסיכום המנהלי הוא הדף הראשון שהוועדה קוראת — ולעיתים האחרון. כתוב אותו כאילו הוא המסמך היחיד
</div>

<!-- ===== סעיף 4 — סיכום מנהלי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. הסיכום המנהלי — מה לכלול</h3>

<p>
  הסיכום המנהלי (עמוד אחד מקסימום) חייב לכלול:
</p>

<ul style="line-height:1.9;">
  <li>שם הלווה, סכום ההלוואה המבוקש, תקופה, וייעוד</li>
  <li>תיאור הנכס בשלושה משפטים — מיקום, סוג, מצב</li>
  <li>ה-NOI, DSCR, LTV, ו-Debt Yield של ה-Base Case</li>
  <li>שני הסיכונים המרכזיים ואיך הם ממותגים</li>
  <li>המלצה: אשר / דחה / תנאי-על לאישור</li>
</ul>

<p>
  ועדת האשראי מחליטה על בסיס הסיכום המנהלי — ורק אז פותחת
  פרקים לבדיקה עמוקה. סיכום מנהלי חלש = מזכר חלש.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>אזהרה:</strong><br>
  חוסר עקביות בין מספרים בגוף המזכר לבין המודל — כישלון אוטומטי בציון
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות. "
    "כל שאלה בוחנת הבנה של מבנה מזכר האשראי המלא (8 סעיפים + נספחים), "
    "אורך ונימה נדרשים, ביקורת עצמית לפני הגשה, ודרישות הסיכום המנהלי. "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים כתיבת סיכום מנהלי לעסקה נתונה, "
    "זיהוי אי-עקביות בין גוף מזכר לבין טבלאות מודל, "
    "סיווג תוכן לסעיף הנכון מתוך 8 סעיפי המזכר, "
    "ותיקון נימה ולשון שגויים בקטע נתון ממזכר. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — כתיבת מזכר האשראי המלא
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>מזכר האשראי המלא כולל 8 סעיפים: סיכום מנהלי, רקע לווה, תיאור נכס, ניתוח פיננסי,
    סיכונים, תרחישים, תנאים, והמלצה — פלוס שלושה נספחים.</strong>
    האורך הנדרש הוא 12–18 עמודים לא כולל נספחים.
  </li>
  <li>
    <strong>הסיכום המנהלי (עמוד אחד) הוא הדף הקריטי ביותר.</strong>
    הוא כולל NOI, DSCR, LTV, Debt Yield, שני הסיכונים המרכזיים, והמלצה.
  </li>
  <li>
    <strong>הנימה: גוף שלישי לאורך כל המזכר. עבר להיסטוריה, הווה לנוכחות, עתיד לתחזיות.</strong>
    פסקאות ממוקדות — טענה אחת רלוונטית לעסקה, לא תיאוריה כללית.
  </li>
  <li>
    <strong>ביקורת עצמית כוללת שתי בדיקות: עקביות מספרים ומקורות לכל טענה עובדתית.</strong>
    כל אי-התאמה בין גוף המזכר למודל — כישלון אוטומטי בציון.
  </li>
  <li>
    <strong>ועדת האשראי מחליטה על בסיס הסיכום המנהלי ופותחת פרקים לבחינה מעמיקה רק לאחר מכן.</strong>
    השקיעו את הזמן הארוך ביותר בסיכום המנהלי ובעקביות הפנימית.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סיכום מנהלי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Executive Summary</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תמצית העסקה, הניתוח, וההמלצה בעמוד אחד</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">בדיקת נאותות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Due Diligence (DD)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תהליך בדיקה מקיף של נתוני הלווה, הנכס, והשוק</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תנאי התראה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תנאי פיננסי שהלווה מחויב לעמוד בו לאורך ההלוואה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ממתן סיכון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Risk Mitigation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פעולות ותנאים המצמצמים את חשיפת המלווה לסיכון</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">המלצת אשראי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Credit Recommendation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עמדת האנליסט: אשר / דחה / תנאי-על לאישור</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נספח</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Appendix</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מסמך תומך המצורף למזכר אך אינו חלק מהגוף הראשי</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — הגשה, קריטריוני ציון ומשוב
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  הגשה, קריטריוני ציון ומשוב
</h2>

<!-- ===== סעיף 1 — דרישות הגשה ===== -->
<h3 style="color:#1a2638;">1. דרישות הגשה — פורמט, שמות קבצים, ועמוד שער</h3>

<p>
  הגשת פרויקט הגמר תכלול קובץ <strong>.docx בלבד</strong>.
  קבצי PDF, Google Docs, או כל פורמט אחר — לא יתקבלו.
</p>

<p>
  <strong>מוסכמת שמות קבצים:</strong>
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;">
  [שם_משפחה]_[שם_פרטי]_Capstone_C12.docx<br>
  דוגמה: כהן_דנה_Capstone_C12.docx
</div>

<p>
  <strong>עמוד שער חובה:</strong>
</p>

<ul style="line-height:1.9;">
  <li>שם מלא של המגיש</li>
  <li>תאריך הגשה</li>
  <li>שם העסקה / הנכס</li>
  <li>המשפט: "מוגש כפרויקט גמר לתוכנית האנליסטים — מימון נדל&quot;ן"</li>
</ul>

<!-- ===== סעיף 2 — מחוון הציון ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. מחוון הציון — 5 קריטריונים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">קריטריון</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">משקל</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מה נבחן</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">דיוק פיננסי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">30%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נכונות חישובי NOI, DSCR, LTV, Debt Yield, IRR; עקביות מספרית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">איכות כתיבה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">25%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בהירות, נימה מקצועית, גוף שלישי, מבנה פסקאות, מקורות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח סיכונים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">20%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">זיהוי וכימות הסיכונים המרכזיים, הצגת מיטיגציה מוצעת</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח תרחישים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">15%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שלושה תרחישים מלאים עם הנחות שונות ופרשנות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">איכות ההמלצה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">10%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עמדה ברורה (אשר/דחה), נימוק מבוסס ניתוח, תנאים מוצעים</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 3 — מה המעריכים מחפשים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. מה המעריכים מחפשים — וסיבות הציון הנמוך השכיחות</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">קריטריון</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מה מצוין נראה כך</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הסיבה השכיחה לציון נמוך</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">דיוק פיננסי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כל מספר בגוף תואם את המודל; הנחות מפורשות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI חד-שנתי, שיעור פנוי אפס, אי-עקביות בין מזכר למודל</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">איכות כתיבה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">גוף שלישי עקבי, פסקאות ממוקדות, ציטוטים מתועדים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">גוף ראשון, פסקאות כלליות, טענות ללא מקור</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח סיכונים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כל סיכון כומת; כל מיטיגציה מוצעת קשורה ספציפית לסיכון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רשימת סיכונים ללא כימות ומיטיגציה כוללנית וסתמית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח תרחישים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הנחות שונות ומפורשות לכל תרחיש; פרשנות ועדת האשראי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שינוי מספר אחד בין תרחישים ללא שינוי הנחות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">איכות ההמלצה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עמדה חד-משמעית; תנאים קונקרטיים; נימוק ממוקד</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">המלצה מותנית ועמומה; אין תנאים מפורשים</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 4 — פרשנות משוב ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. כיצד לפרש משוב — שגיאה עובדתית לעומת חולשה אנליטית</h3>

<p>
  המשוב שתקבל יסווג לאחת משתי קטגוריות:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>שגיאה עובדתית (Factual Error):</strong> מספר שגוי, נוסחה
    שגויה, נתון שאינו מתאים למקור. זוהי שגיאה אובייקטיבית שיש
    לתקן. דוגמה: "ה-DSCR בשנה 2 מחושב שגוי — השתמשת ב-NOI
    של שנה 1 במקום שנה 2."
  </li>
  <li>
    <strong>חולשה אנליטית (Analytical Weakness):</strong> ניתוח
    שהוא לא שגוי אלא חסר עומק, שיפוט, או פרספקטיבה. דוגמה:
    "הסיכון הזה זוהה אך לא כומת ולא הוצעה מיטיגציה ספציפית."
  </li>
</ul>

<p>
  <strong>שגיאה עובדתית</strong> דורשת תיקון מדויק.
  <strong>חולשה אנליטית</strong> דורשת העמקה ושיפוט — לא רק תיקון מכני.
</p>

<!-- ===== סעיף 5 — תהליך עיון חוזר ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. אם אינך מסכים עם המשוב — תהליך העיון החוזר</h3>

<p>
  אם אתה סבור שמשוב שקיבלת שגוי או שאינו מוצדק:
</p>

<ol style="line-height:1.9;">
  <li>
    <strong>קרא את המשוב שוב לאחר 24 שעות.</strong> לעיתים קרובות,
    ההתנגדות הראשונית נובעת מהתגובה הרגשית ולא מבדיקה אנליטית.
  </li>
  <li>
    <strong>הכן נימוק בכתב:</strong> פרט מדוע אתה חולק על המשוב,
    עם הפנייה ספציפית לחומר הלמידה, לנתוני העסקה, או לסטנדרד
    מקצועי מוכר.
  </li>
  <li>
    <strong>שלח את הנימוק למעריך</strong> בתוך 14 יום ממועד קבלת
    הציון. בקשות עיון לאחר מועד זה לא יטופלו.
  </li>
  <li>
    <strong>תשובת המעריך היא סופית.</strong> לא קיים ערעור נוסף
    מעבר לתהליך עיון חוזר אחד.
  </li>
</ol>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>הסטנדרט המקצועי:</strong><br>
  מזכר אשראי שהוועדה יכולה לאשר ישירות — זה התקן. לא פחות
</div>

<!-- ===== מסר סיום ===== -->
<div style="background:#1a2638;color:#fff;padding:20px 24px;margin:28px 0;border-radius:6px;text-align:center;">
  <p style="font-size:16px;font-weight:bold;margin:0 0 10px;">
    סיימת את תוכנית האנליסטים
  </p>
  <p style="font-size:14px;margin:0;">
    סיימת את תוכנית האנליסטים — אתה מוכן לניתוח עסקאות מימון נדל&quot;ן מקצועי
  </p>
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות. "
    "כל שאלה בוחנת הבנה של דרישות ההגשה, מחוון הציון (5 קריטריונים ומשקליהם), "
    "מה המעריכים מחפשים, ההבדל בין שגיאה עובדתית לחולשה אנליטית, "
    "ותהליך העיון החוזר. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים חישוב ציון משוקלל בהינתן ציונים לפי קריטריונים, "
    "סיווג פיסות משוב כ'שגיאה עובדתית' או 'חולשה אנליטית', "
    "זיהוי הפרות דרישות הגשה בתיאור קובץ נתון, "
    "ותרגול ניסוח נימוק לעיון חוזר על משוב נתון. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — הגשה, קריטריוני ציון ומשוב
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>הגשה היא קובץ .docx בלבד, עם שם קובץ תקני ועמוד שער מלא.</strong>
    קובץ שאינו עומד בדרישות הפורמט נפסל לפני קריאה.
  </li>
  <li>
    <strong>מחוון הציון: דיוק פיננסי 30%, כתיבה 25%, סיכונים 20%, תרחישים 15%, המלצה 10%.</strong>
    הדיוק הפיננסי הוא הקריטריון הכבד ביותר — ועקביות מספרית היא תנאי סף.
  </li>
  <li>
    <strong>הסיבות השכיחות לציון נמוך: NOI חד-שנתי, שיעור פנוי אפס, אי-עקביות בין מזכר למודל, וסיכונים ללא כימות.</strong>
    כל אחת מהשגיאות הללו ניתנת למניעה בביקורת עצמית לפני הגשה.
  </li>
  <li>
    <strong>שגיאה עובדתית דורשת תיקון מדויק; חולשה אנליטית דורשת העמקה ושיפוט.</strong>
    הבחנה זו קריטית לפרשנות נכונה של המשוב ולשיפור אמיתי.
  </li>
  <li>
    <strong>עיון חוזר אפשרי בתוך 14 יום עם נימוק בכתב — ותשובת המעריך סופית.</strong>
    ההתנגדות הראשונית לעיתים קרובות נובעת מתגובה רגשית — קרא שוב לאחר 24 שעות.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מחוון ציון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Rubric</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פירוט קריטריוני הערכה ומשקליהם</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שגיאה עובדתית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Factual Error</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מספר או נתון שגוי שניתן לאימות אובייקטיבי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חולשה אנליטית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Analytical Weakness</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתוח שאינו שגוי אלא חסר עומק, שיפוט, או פרספקטיבה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עיון חוזר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Grade Appeal / Review</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בקשה מנומקת לבחינה מחדש של ציון שהתקבל</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עמוד שער</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cover Page</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עמוד פתיחה עם פרטי המגיש, העסקה, והתאריך</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ציון משוקלל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Weighted Score</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ציון כולל המחושב לפי משקל כל קריטריון</td>
    </tr>
  </tbody>
</table>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "בניית המודל הפיננסי לפרויקט הגמר",
        "slug": "bniyat-hamodel-hapinantsi-lagamar",
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
        "title_he": "כתיבת מזכר האשראי המלא",
        "slug": "ktivat-mezker-hashrai-hamale",
        "estimated_minutes": 60,
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
        "title_he": "הגשה, קריטריוני ציון ומשוב",
        "slug": "hagasha-kriteryoney-tzion-umashov",
        "estimated_minutes": 40,
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
    help = "Seed Course 12, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=12)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 12 not found. Run 'python manage.py seed_data' first."
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
