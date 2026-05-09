"""
Management command: seed_c01_modules45
Seeds Course 1, Modules 4 and 5 with full reading, comprehension, exercises,
and summary ModuleComponent records.

Usage:
    python manage.py seed_c01_modules45
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — מדדי אשראי: LTV ו-DSCR
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  מדדי אשראי: LTV ו-DSCR
</h2>

<!-- ===== סעיף 1 — מבוא ===== -->
<h3 style="color:#1a2638;">1. מבוא — שני יחסים, שתי שאלות</h3>

<p>
  בכל עסקת מימון נדל&quot;ן ישנן <strong>שתי שאלות יסוד</strong> שוועדת האשראי חייבת לענות עליהן לפני שתאשר הלוואה:
</p>

<ol style="line-height:1.9;">
  <li><strong>שאלת הביטחונות:</strong> האם שווי הנכס מספיק כדי לכסות את ההלוואה אם הלווה לא יעמוד בתשלומים?</li>
  <li><strong>שאלת התזרים:</strong> האם הנכס מייצר מספיק הכנסה כדי לשלם את שירות החוב השוטף?</li>
</ol>

<p>
  לכל שאלה יש מדד ייעודי:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מדד</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שם מלא</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">השאלה שהוא עונה עליה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג בדיקה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">LTV</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Loan-to-Value Ratio</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">האם הנכס מספיק כבטוחה?</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדיקת ביטחונות (Collateral Test)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">DSCR</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Debt Service Coverage Ratio</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">האם התזרים מספיק לתשלום החוב?</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדיקת תזרים מזומנים (Cash Flow Test)</td>
    </tr>
  </tbody>
</table>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>כלל בסיסי:</strong> כל עסקת מימון נדל&quot;ן חייבת לעמוד <em>בשני</em> המדדים גם יחד.
  LTV תקין ו-DSCR נמוך מדי — העסקה עלולה להידחות. DSCR גבוה ו-LTV גבוה מדי — גם כן בעיה.
  שני המדדים משלימים זה את זה ואינם ניתנים להחלפה.
</div>

<!-- ===== סעיף 2 — LTV ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. LTV — יחס הלוואה לשווי</h3>

<h4 style="color:#1976d2;">2.1 הנוסחה הבסיסית</h4>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  LTV = הלוואה ÷ שווי הנכס × 100
</div>

<p>
  המדד מבטא את <strong>שיעור המינוף</strong>: כמה אחוז מסכום הרכישה (או השווי) ממומן בחוב.
  יתרת המימון — ה&quot;הון עצמי&quot; (Equity) — היא ההפרש: <code>100% − LTV</code>.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>דוגמה:</strong><br>
  נכס מסחרי בשווי שוק <strong>10,000,000 ש&quot;ח</strong>. מבקשים הלוואה של <strong>7,000,000 ש&quot;ח</strong>.<br>
  LTV = 7,000,000 ÷ 10,000,000 × 100 = <strong>70%</strong><br>
  הון עצמי = 30% = 3,000,000 ש&quot;ח.<br>
  אם מדיניות המוסד: LTV מקסימלי 75% — העסקה עומדת בקריטריון.
</div>

<h4 style="color:#1976d2;margin-top:20px;">2.2 שלושה מושגי &quot;שווי&quot;</h4>

<p>
  המכנה בנוסחת LTV אינו פשוט תמיד — ישנן שלוש הגדרות שימושיות לשווי, ולכל אחת שימוש שונה:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מושג</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מתי משתמשים?</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הערות</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שווי שוק (Market Value)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">המחיר הצפוי במכירה תקינה בין קונה מרצון למוכר מרצון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואות רגילות לנכסים מניבים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הבסיס הסטנדרטי; נקבע בשמאות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שווי כפוי (Forced Sale Value)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">המחיר בפינוי מהיר / מכירה כפויה תוך 90–180 יום</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חישוב הנחת &quot;מקרה גרוע&quot; (worst-case)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">70–85% מהשווי השוק בישראל 2025</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">LTC — Loan-to-Cost</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואה ÷ <em>עלות</em> הפרויקט (לא שווי)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואות בנייה ופיתוח</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שימוש בעלות ולא בשווי כי הנכס טרם קיים</td>
    </tr>
  </tbody>
</table>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>אזהרה — Forced Sale Value:</strong><br>
  בישראל, שמאי מקרקעין מחויבים לפרט בחוות הדעת גם את שווי הכפייה בנפרד.
  חלק ממוסדות המימון מחשבים LTV על בסיס שווי כפייה כדי להבטיח שגם בתרחיש קיצון
  הם יוכלו לממש את הבטוחה ולהחזיר את ההלוואה.
</div>

<h4 style="color:#1976d2;margin-top:20px;">2.3 נורמות LTV בישראל 2025–2026</h4>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג נכס / עסקה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">LTV מקסימלי מקובל</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הערות</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">מגורים — דירה ראשונה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">75%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רגולציה BDI של בנק ישראל</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">מגורים — דירה נוספת / משקיעים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">50%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הוראת בנק ישראל 2012 ועדכוניה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">מסחרי מניב (משרדים, קניון)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">60–65%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תלוי בסוג הנכס ורמת הפנויות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">תעשייה ולוגיסטיקה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">60%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוק פחות נזיל; LTV שמרני יותר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואת בנייה (LTC)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">75–85%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">על בסיס עלות הפרויקט; בהתאם ללו&quot;ז ומכירות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">קרקע חקלאית / לא מאושרת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">40–50%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכון תכנוני גבוה; LTV נמוך מאוד</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>נקודה לוועדת אשראי:</strong><br>
  ה-LTV אינו סטטי — הוא משתנה לאורך חיי ההלוואה. ככל שהיתרה קטנה ו/או שווי הנכס עולה,
  ה-LTV משתפר. מוסדות מימון רבים מתנים מחזור הלוואה או הגדלת אשראי בבחינה מחדש של ה-LTV.
</div>

<!-- ===== סעיף 3 — DSCR ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. DSCR — יחס כיסוי שירות החוב</h3>

<h4 style="color:#1976d2;">3.1 הנוסחה</h4>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  DSCR = NOI ÷ שירות חוב שנתי
</div>

<p>
  <strong>NOI (Net Operating Income — הכנסה תפעולית נטו)</strong> מחושב כך:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  NOI = הכנסות שכירות ברוטו<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&minus; שיעור פנויות (Vacancy Rate)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&minus; הוצאות תפעוליות (ביטוח, ועד בית, תחזוקה, ניהול נכס)<br>
  ──────────────────────────────────<br>
  = NOI
</div>

<p>
  <strong>שירות חוב שנתי</strong> = סך תשלומי קרן + ריבית במהלך שנה (Debt Service = P&amp;I).
  <em>שים לב: NOI חושב לפני ניכוי שירות חוב — לא לבלבל בין השניים.</em>
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>דוגמה מספרית:</strong><br>
  נכס מסחרי. הכנסות ברוטו: 1,200,000 ש&quot;ח. פנויות: 5% = 60,000 ש&quot;ח.
  הוצאות תפעוליות: 180,000 ש&quot;ח.<br>
  NOI = 1,200,000 − 60,000 − 180,000 = <strong>960,000 ש&quot;ח</strong><br><br>
  שירות חוב שנתי (קרן + ריבית): 720,000 ש&quot;ח.<br>
  DSCR = 960,000 ÷ 720,000 = <strong>1.33</strong><br>
  מעל ה-1.20 המינימלי — העסקה עומדת בקריטריון.
</div>

<h4 style="color:#1976d2;margin-top:20px;">3.2 שתי גישות לחישוב DSCR</h4>

<p>
  בשוק הישראלי נהוגות שתי גישות מרכזיות לחישוב DSCR, בהתאם לסוג הנכס ולגוף המממן:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">גישה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מונה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מכנה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שימוש נפוץ</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">NOI-based</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI = הכנסה תפעולית נטו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שירות חוב שנתי (P&amp;I)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נדל&quot;ן מניב, משרדים, מסחרי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">EBITDA-based</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">EBITDA של פעילות הלווה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שירות חוב מסה&quot;כ (כולל הלוואות אחרות)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">לווים תאגידיים; פרויקטים מעורבים</td>
    </tr>
  </tbody>
</table>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>זהירות — EBITDA vs NOI:</strong><br>
  EBITDA כולל הכנסות מפעילויות עסקיות שאינן קשורות לנכס הבטוחה.
  בניתוח אשראי נדל&quot;ן &quot;טהור&quot; — NOI הוא המדד המועדף כי הוא מבטא את כוח הרוויח של הנכס עצמו בלבד.
  שימוש ב-EBITDA מבלי להבדיל עלול ליצור אשליה של DSCR גבוה שאינה מייצגת את הנכס הבטוחה.
</div>

<h4 style="color:#1976d2;margin-top:20px;">3.3 נורמות DSCR בישראל</h4>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג עסקה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">DSCR מינימלי מקובל</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הערות</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">מסחרי מאוכלס (משרדים, קניון)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">≥ 1.20x</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סטנדרט בנקאי מינימלי; מוסדות מוסיפים 10–15% מרווח</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">דיור להשכרה (Build-to-Rent)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">≥ 1.15x</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכנסות יציבות; רגישות נמוכה יותר לפנויות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">לוגיסטיקה / תעשייה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">≥ 1.25x</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שוק פחות נזיל; מינימום גבוה יותר</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">בנייה / יזמי (תזרים שוטף)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">לא רלוונטי בשלב הבנייה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מחושב על בסיס תחזית לאחר אכלוס; כיסוי מוודא ממכירות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR &lt; 1.00</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;color:#c62828;">⚠ חסרון תזרים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הנכס אינו מכסה שירות חוב; נדרשת השלמה חיצונית</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 4 — יחסים משלימים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. יחסים משלימים — טבלת עזר מהירה</h3>

<p>
  בנוסף ל-LTV ו-DSCR, ועדות אשראי עוקבות אחרי מספר יחסים נוספים שמשלימים את התמונה:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מדד</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">נוסחה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מה הוא מודד</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">נורמה מקובלת</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ICR</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-family:monospace;">EBIT ÷ הוצאות ריבית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כיסוי ריבית בלבד (ללא קרן)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">≥ 2.0x בדרך כלל</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Debt / EBITDA</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-family:monospace;">יתרת חוב ÷ EBITDA שנתי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כמה שנים נדרשות לפירעון מלא</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">&lt; 5.0x (לווים תאגידיים)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Net Leverage</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-family:monospace;">(חוב − מזומן) ÷ EBITDA</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מינוף נטו (בניכוי נזילות)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">&lt; 4.0x</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Cap Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-family:monospace;">NOI ÷ שווי שוק</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשואה תפעולית על הנכס</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">5–7% בנדל&quot;ן מסחרי ישראל 2025</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>בפועל:</strong> בניתוח מזכר אשראי לנדל&quot;ן, ה-LTV וה-DSCR הם מרכזיים.
  ICR ו-Net Leverage באים לידי ביטוי בעיקר כשהלווה הוא חברה תאגידית
  עם פעילות רחבה יותר מנכס יחיד.
</div>

<!-- ===== סעיף 5 — מינוף, תשואה וסיכון ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. מינוף, תשואה וסיכון</h3>

<p>
  מינוף (Leverage) הוא הכוח שמאפשר למשקיע להגדיל את תשואת ההון העצמי — אך הוא גם מגדיל את הסיכון.
  הבנת אפקט המינוף חיונית לאנליסט אשראי כדי להעריך מה מניע את הלווה לבקש LTV גבוה.
</p>

<h4 style="color:#1976d2;">דוגמה — השפעת רמת המינוף על IRR הון עצמי</h4>

<p>
  נכס מניב. מחיר רכישה: <strong>10,000,000 ש&quot;ח</strong>. NOI שנתי: <strong>600,000 ש&quot;ח</strong>
  (Cap Rate = 6%). ריבית הלוואה: <strong>6.5%</strong> קבועה. תקופה: 10 שנים.
  שערוך נכס: +2% לשנה.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">LTV</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הלוואה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הון עצמי</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שירות חוב שנתי (קירוב)</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">תזרים חופשי שנתי</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">DSCR</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">Cash-on-Cash (שנה 1)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">0% (ללא הלוואה)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">10,000,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">600,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">6.0%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">50%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">5,000,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">5,000,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">~390,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">~210,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">1.54x</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">4.2%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">65%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">6,500,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">3,500,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">~507,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">~93,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">1.18x</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">2.7%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;color:#c62828;">75%</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">7,500,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">2,500,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">~585,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;">~15,000</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;color:#c62828;">1.03x</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;color:#c62828;">0.6%</td>
    </tr>
  </tbody>
</table>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>תצפית:</strong><br>
  בדוגמה זו, Cap Rate (6%) נמוך מהריבית (6.5%).
  כלומר, מינוף גבוה <em>פוגע</em> בתזרים השוטף — תופעה הנקראת <strong>Negative Leverage</strong>.
  הלווה עדיין יכול להרוויח מהשבחה (שערוך הנכס), אך בינתיים שירות החוב &quot;אוכל&quot; את הכנסות השכירות.
  DSCR של 1.03 בשורה הרביעית כמעט ואינו עומד בסף המינימלי — ועדת האשראי תדחה עסקה כזו.
</div>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>כלל אצבע — פוזיטיב/נגטיב לברג':</strong><br>
  אם <strong>Cap Rate &gt; ריבית ההלוואה</strong> → מינוף גבוה מגדיל תשואת הון (Positive Leverage).<br>
  אם <strong>Cap Rate &lt; ריבית ההלוואה</strong> → מינוף גבוה פוגע בתשואת הון (Negative Leverage).<br>
  האנליסט חייב לבדוק את הפער הזה כחלק מכל ניתוח.
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מושגי LTV ו-DSCR. יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים חישובים ישירים ושאלות שיפוט. "
    "יש לך שתי הזדמנויות לכל שאלה — השתמש בניסיון הראשון בזהירות."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — מדדי אשראי: LTV ו-DSCR
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>LTV בוחן ביטחונות; DSCR בוחן תזרים.</strong>
    שני המדדים נדרשים יחד — אין אחד שמחליף את השני.
  </li>
  <li>
    <strong>&quot;שווי&quot; אינו מספר אחד.</strong>
    שווי שוק, שווי כפייה (FSV, 70–85% בישראל), ועלות (LTC לבנייה) — לכל הקשר המדד הנכון.
  </li>
  <li>
    <strong>DSCR מינימלי 1.20x לנדל&quot;ן מסחרי מאוכלס.</strong>
    DSCR מתחת ל-1.00 = חסרון תזרים; הלווה חייב להשלים ממקורות חיצוניים.
  </li>
  <li>
    <strong>אפקט המינוף יכול לפעול לשני הכיוונים.</strong>
    כשה-Cap Rate גבוה מהריבית (Positive Leverage) — מינוף גבוה מגדיל תשואת הון.
    כשה-Cap Rate נמוך — מינוף גבוה פוגע בתזרים.
  </li>
  <li>
    <strong>נורמות LTV 2025–2026 בישראל:</strong>
    מגורים ראשונה 75%, מסחרי מניב 60–65%, בנייה (LTC) 75–85%.
    נורמות אלה מעוגנות בהנחיות בנק ישראל ובמדיניות הגופים המממנים.
  </li>
</ol>

<h3 style="color:#1a2638;margin-top:24px;">מילון מונחים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מונח בעברית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">English</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">יחס הלוואה לשווי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">LTV — Loan-to-Value</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואה ÷ שווי הנכס; מדד מינוף ובטוחה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">יחס כיסוי שירות חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR — Debt Service Coverage Ratio</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI ÷ שירות חוב שנתי; מדד כיסוי תזרים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הכנסה תפעולית נטו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI — Net Operating Income</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכנסות שכירות בניכוי פנויות והוצאות תפעוליות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שווי כפוי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Forced Sale Value (FSV)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שווי הנכס במכירה מהירה; 70–85% מהשוק בישראל</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הלוואה לעלות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">LTC — Loan-to-Cost</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואה ÷ עלות הפרויקט; משמש בהלוואות בנייה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיעור היוון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cap Rate — Capitalization Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">NOI ÷ שווי שוק; תשואה תפעולית על הנכס</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מינוף חיובי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Positive Leverage</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מצב שבו Cap Rate &gt; ריבית; מינוף מגדיל תשואת הון</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שירות חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Debt Service (P&amp;I)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סך תשלומי קרן וריבית בתקופה נתונה</td>
    </tr>
  </tbody>
</table>

<h3 style="color:#1a2638;margin-top:24px;">גשר למודול הבא</h3>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>מודול 5 — ניתוח רגישות וניתוח תרחישים:</strong><br>
  כעת שאתה שולט ב-LTV וב-DSCR, המודול הבא ילמד אותך <em>מה קורה לשני המדדים האלה</em>
  כאשר הנחות השוק משתנות — עליית ריבית, ירידת שכירויות, האטה במכירות.
  ניתוח רגישות הוא הכלי שהופך אנליסט טוב לאנליסט מצוין.
</div>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — ניתוח רגישות וניתוח תרחישים
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  ניתוח רגישות וניתוח תרחישים
</h2>

<!-- ===== סעיף 1 — מהו ניתוח רגישות? ===== -->
<h3 style="color:#1a2638;">1. מהו ניתוח רגישות?</h3>

<p>
  ניתוח רגישות (Sensitivity Analysis) הוא כלי אנליטי שבוחן <strong>כיצד תשתנה תוצאה מסוימת
  כאשר משתנה קלט אחד משתנה</strong> — בעוד שאר המשתנים נשארים קבועים (ceteris paribus).
  בשפת האנליסטים: &quot;What-if Analysis&quot; — מה יקרה אם...?
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>למה ניתוח רגישות חשוב בנדל&quot;ן?</strong><br>
  עסקאות נדל&quot;ן מתבססות על תחזיות ל-5–20 שנה. בשוק ישראלי עם תנודתיות גבוהה —
  שינויי ריבית בנק ישראל, מחירי דירות, קצב מכירות — הנחות הבסיס יכולות להתממש בצורה שונה מאוד.
  ניתוח רגישות מראה לוועדת האשראי עד כמה העסקה &quot;עמידה&quot; ואיפה נמצאות נקודות השבירה.
</div>

<p>
  <strong>ההבדל המרכזי בין ניתוח רגישות לניתוח תרחישים:</strong>
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">סוג ניתוח</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">כמה משתנים משתנים?</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פלט אופייני</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שאלה שעונה עליה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח רגישות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">משתנה אחד בכל פעם</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">טבלת רגישות / גרף טורנדו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מה ה&quot;שבריריות&quot; לכל פרמטר בנפרד?</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח תרחישים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מספר משתנים בו-זמנית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">3 תרחישים מלאים (בסיס / אופטימי / פסימי)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מה קורה בעולמות שלמים שונים?</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 2 — בניית טבלת רגישות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. בניית טבלת רגישות</h3>

<p>
  הפורמט הנפוץ ביותר הוא <strong>טבלה דו-ממדית</strong>: שורות מייצגות ערכים שונים של משתנה אחד,
  עמודות מייצגות ערכים שונים של משתנה שני. בתאי הטבלה: התוצאה (DSCR, IRR, NPV וכד').
</p>

<h4 style="color:#1976d2;">דוגמה — טבלת רגישות DSCR: שכירות × ריבית</h4>

<p>
  נכס מסחרי. NOI בסיס: 960,000 ש&quot;ח. הלוואה: 7,000,000 ש&quot;ח. שירות חוב בריבית 6.5%: ~712,000 ש&quot;ח.
  DSCR בסיס: 1.35x.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">DSCR → ריבית<br>NOI ↓</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:center;">5.5%</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:center;">6.0%</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:center;background:#1976d2;">6.5% (בסיס)</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:center;">7.0%</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:center;">7.5%</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#e8f5e9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">1,100,000 (+15%)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;font-weight:bold;">1.71</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;font-weight:bold;">1.62</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;font-weight:bold;">1.55</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;font-weight:bold;">1.48</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;font-weight:bold;">1.42</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">1,030,000 (+7%)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">1.60</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">1.52</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">1.45</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">1.38</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#1565c0;">1.33</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;background:#fff8e1;">960,000 (בסיס)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">1.49</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">1.41</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;font-weight:bold;background:#fff8e1;">1.35</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#1565c0;">1.29</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#1565c0;">1.24</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">864,000 (−10%)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#1565c0;">1.34</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#1565c0;">1.27</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#1565c0;">1.21</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#e65100;font-weight:bold;">1.16</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#c62828;font-weight:bold;">1.11</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">768,000 (−20%)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#1565c0;">1.19</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#e65100;font-weight:bold;">1.13</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#c62828;font-weight:bold;">1.08</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#c62828;font-weight:bold;">1.03</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#c62828;font-weight:bold;">0.99</td>
    </tr>
  </tbody>
</table>

<p style="font-size:12px;color:#555;">
  <span style="color:#2e7d32;font-weight:bold;">ירוק</span> = DSCR ≥ 1.20 (עומד בקריטריון) |
  <span style="color:#1565c0;">כחול</span> = 1.10–1.19 (אזור אזהרה) |
  <span style="color:#c62828;font-weight:bold;">אדום</span> = &lt;1.10 (חריגה; דחייה צפויה)
</p>

<h4 style="color:#1976d2;margin-top:20px;">מושג — גרף טורנדו (Tornado Chart)</h4>

<p>
  גרף הטורנדו (Tornado Chart) מדרג את המשתנים לפי מידת השפעתם על התוצאה.
  המשתנה שמשפיע הכי הרבה מופיע בראש (הפס הרחב ביותר), ולמטה המשתנים בעלי השפעה קטנה יותר.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  <strong>השפעה על DSCR (דוגמה — לפי רוחב תחום):</strong><br><br>
  שיעור פנויות:    ████████████████████  ±0.28 DSCR<br>
  ריבית הלוואה:   ████████████████      ±0.22 DSCR<br>
  הוצ' תפעוליות:  ██████████            ±0.14 DSCR<br>
  שיעור שכירות:   ████████              ±0.11 DSCR<br>
  מחזור הלוואה:   ████                  ±0.06 DSCR<br>
</div>

<p>
  מהגרף עולה: <strong>שיעור הפנויות הוא הגורם הרגיש ביותר</strong> ב-DSCR.
  ועדת אשראי תשאל: &quot;מה קצב הפנויות ההיסטורי באזור? האם יש חוזי שכירות ארוכי טווח?&quot;
</p>

<!-- ===== סעיף 3 — ניתוח תרחישים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. ניתוח תרחישים</h3>

<p>
  בעוד ניתוח רגישות משנה משתנה אחד בכל פעם, <strong>ניתוח תרחישים</strong> מגדיר שלושה &quot;עולמות&quot; שלמים
  עם ערכים עקביים זה עם זה לכל המשתנים הרלוונטיים: תרחיש בסיס, אופטימי, ופסימי.
</p>

<h4 style="color:#1976d2;">דוגמה מלאה — פרויקט 60 יחידות דיור, מרכז הארץ</h4>

<p>
  <strong>פרטי הפרויקט (בסיס):</strong> 60 יחידות × 1,800,000 ש&quot;ח ממוצע = הכנסה כוללת 108,000,000 ש&quot;ח.
  עלות בנייה: 4,200 ש&quot;ח/מ&quot;ר × 5,400 מ&quot;ר = 22,680,000 ש&quot;ח. עלות קרקע ועלויות עקיפות: 35,000,000 ש&quot;ח.
  סה&quot;כ עלות פרויקט: 57,680,000 ש&quot;ח. הלוואת בנייה: 43,260,000 ש&quot;ח (LTC=75%).
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:12px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:7px 10px;text-align:right;">פרמטר</th>
      <th style="border:1px solid #ccc;padding:7px 10px;text-align:center;background:#2e7d32;">תרחיש אופטימי</th>
      <th style="border:1px solid #ccc;padding:7px 10px;text-align:center;background:#1565c0;">תרחיש בסיס</th>
      <th style="border:1px solid #ccc;padding:7px 10px;text-align:center;background:#c62828;">תרחיש פסימי</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">מחיר ממוצע ליחידה</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">2,000,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">1,800,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">1,550,000 ₪</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">עלות בנייה למ&quot;ר</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">3,900 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">4,200 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">5,100 ₪</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">ריבית הלוואת בנייה</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">5.8%</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">6.5%</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">7.5%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">קצב ספיגה (יח'/חודש)</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">5</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">3</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">1.5</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">תקופת מכירות (חודשים)</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">12</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">20</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">40</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;background:#e8f5e9;color:#1b5e20;">הכנסות מכירות כוללות</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;color:#2e7d32;">120,000,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;">108,000,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;color:#c62828;">93,000,000 ₪</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">עלות בנייה כוללת</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">21,060,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">22,680,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">27,540,000 ₪</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">הוצ' מימון (קירוב)</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">2,800,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">5,100,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;">11,200,000 ₪</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">רווח יזמי (לפני מס)</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;color:#2e7d32;">61,140,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;">45,220,000 ₪</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;color:#c62828;">19,260,000 ₪</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">שולי רווח</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;color:#2e7d32;">51%</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;">42%</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;color:#c62828;">21%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:7px 10px;font-weight:bold;">כיסוי הלוואה מהכנסות</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;color:#2e7d32;">2.77x</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;">2.50x</td>
      <td style="border:1px solid #ccc;padding:7px 10px;text-align:center;font-weight:bold;color:#e65100;">2.15x</td>
    </tr>
  </tbody>
</table>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>מסקנה מהניתוח:</strong><br>
  גם בתרחיש הפסימי, כיסוי ההלוואה מהכנסות המכירות עומד על 2.15x — כלומר ההכנסות הכוללות
  עולות פי 2.15 על ההלוואה. הפרויקט עמיד. עם זאת, תקופת ה-40 חודשים בתרחיש הפסימי
  מייצרת עלויות מימון גבוהות משמעותית ומדללת את הרווח ל-21% בלבד — עדיין חיובי אך מוגבל.
</div>

<!-- ===== סעיף 4 — משתנים קריטיים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. משתנים קריטיים בנדל&quot;ן ישראלי</h3>

<p>
  מתוך ניסיון שוק, ארבעה משתנים הם <strong>הגורמים הרגישים ביותר</strong> ברוב עסקאות הנדל&quot;ן בישראל.
  האנליסט חייב לבצע ניתוח רגישות לכל אחד מהם בנפרד.
</p>

<h4 style="color:#1976d2;">1. ריבית בנק ישראל / ריבית ה-Prime</h4>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>השפעה:</strong> שינוי של 1% בריבית Prime משפיע ישירות על שירות חוב של הלוואות משתנות-ריבית.
  בישראל 2024–2025, עם ריבית Prime שירדה מ-6.5% לסביבות 5.5%, חלה הקלה משמעותית בשירות חוב.
  אך הלוואות לפרויקטים ארוכים (5–7 שנים) חייבות לתמחר תרחיש של עלייה חוזרת.<br><br>
  <strong>בדיקה מומלצת:</strong> הצג DSCR בריבית נוכחית, ריבית + 1%, ריבית + 2%.
</div>

<h4 style="color:#1976d2;">2. עלות בנייה למ&quot;ר</h4>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>השפעה:</strong> בישראל 2025, עלות בנייה ממוצעת נעה בין 3,800–5,500 ש&quot;ח/מ&quot;ר (בהתאם לאזור ולסוג).
  עלייה של 15% בעלויות (בגלל חומרי גלם, ביטוח ריסק מלחמה, מחסור בפועלים) משפיעה ישירות
  על ה-LTC ועל שולי הרווח.<br><br>
  <strong>בדיקה מומלצת:</strong> הצג Profit Margin בעלות בסיס, + 10%, + 20%.
</div>

<h4 style="color:#1976d2;">3. מחיר מכירה ליחידת דיור / מחיר שכירות</h4>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>השפעה:</strong> ירידה של 10% במחיר מכירה על 60 יחידות = הפסד הכנסה של ~10,800,000 ש&quot;ח.
  בנכסים מניבים — ירידה של 10% בשכירות מחלישה את ה-NOI ומשפיעה ישירות על ה-DSCR.<br><br>
  <strong>בדיקה מומלצת:</strong> הצג רווח יזמי / DSCR במחיר −10%, בסיס, +10%.
</div>

<h4 style="color:#1976d2;">4. קצב ספיגה (Absorption Rate)</h4>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>השפעה — לרוב הנדרת ביותר:</strong><br>
  קצב ספיגה נמוך = תקופת מכירות ארוכה = עלויות מימון גבוהות יותר = LTC גבוה יותר
  (כי הקרן + ריבית שנצברת גדלים).
  בשוק ישראלי, ספיגה של פחות מ-2 יחידות/חודש לפרויקט גדול מחייבת בחינה מחודשת של כדאיות ההלוואה.<br><br>
  <strong>בדיקה מומלצת:</strong> הצג עלות מימון בקצב 5, 3, 1.5 יח'/חודש.
</div>

<!-- ===== סעיף 5 — מסקנות לוועדת האשראי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. מסקנות לוועדת האשראי</h3>

<p>
  ניתוח רגישות ותרחישים אינו מסתיים בטבלה — הוא חייב להגיע לכדי <strong>המלצה ברורה לוועדת האשראי</strong>.
</p>

<h4 style="color:#1976d2;">מה מציגים לוועדה?</h4>

<ol style="line-height:2.0;">
  <li><strong>תרחיש הבסיס ותרחיש הפסימי בלבד</strong> (תרחיש אופטימי פחות מעניין — הבנק לא לוקח את הסיכון של ה-Upside).</li>
  <li><strong>נקודת השבירה (Break-Even)</strong>: מה הערך המינימלי של X (שכירות, מחיר, ספיגה) שמתחתיו העסקה פוגעת ב-DSCR?</li>
  <li><strong>גורמי הסיכון הדומיננטיים</strong> לפי Tornado Chart: 2–3 גורמים שצריכים &quot;כרית ביטחון&quot;.</li>
  <li><strong>התניות מוצעות</strong>: אם מאשרים, אילו תנאים יפחיתו סיכון (ביטוח שכירות, Holdback, בדיקות Covenant).</li>
</ol>

<h4 style="color:#1976d2;margin-top:16px;">מה מוביל לדחייה מיידית vs. לאישור בתנאים?</h4>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">ממצא</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">המלצה לוועדה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פעולה אפשרית</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#ffebee;">
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;font-weight:bold;">DSCR פסימי &lt; 1.00</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;font-weight:bold;">דחייה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הפחתת סכום ההלוואה; בטוחות נוספות</td>
    </tr>
    <tr style="background:#fff8e1;">
      <td style="border:1px solid #ccc;padding:8px 12px;color:#e65100;font-weight:bold;">DSCR פסימי 1.00–1.10</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#e65100;font-weight:bold;">אישור בתנאים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Holdback, Financial Covenant, בדיקת DSCR רבעונית</td>
    </tr>
    <tr style="background:#e8f5e9;">
      <td style="border:1px solid #ccc;padding:8px 12px;color:#2e7d32;font-weight:bold;">DSCR פסימי ≥ 1.20</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#2e7d32;font-weight:bold;">אישור רגיל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניתן לאשר; תנאים סטנדרטיים</td>
    </tr>
    <tr style="background:#ffebee;">
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;font-weight:bold;">LTV פסימי &gt; מדיניות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;font-weight:bold;">דחייה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הגדלת הון עצמי; בטוחה נוספת</td>
    </tr>
    <tr style="background:#fff8e1;">
      <td style="border:1px solid #ccc;padding:8px 12px;color:#e65100;font-weight:bold;">ספיגה פסימי &gt; 36 חודשים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#e65100;font-weight:bold;">אישור בתנאים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הקמת Reserve Fund; ערבות אישית</td>
    </tr>
  </tbody>
</table>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>כלל עבודה — &quot;מבחן הכרית&quot;:</strong><br>
  לאחר כל ניתוח רגישות, שאל: &quot;כמה רחוק צריך להתדרדר השוק כדי שהעסקה תפגע ב-DSCR?&quot;
  אם הפיחות הנדרש קטן מ-10% — &quot;הכרית&quot; דקה מדי.
  אם הפיחות הנדרש גדול מ-20% — העסקה עמידה.
  זו שאלה שכל חבר ועדה רוצה לשמוע שהאנליסט כבר ענה עליה.
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של ניתוח רגישות וניתוח תרחישים. יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים ניתוח טבלאות, פרשנות תרחישים ושיפוטי ועדת אשראי. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — ניתוח רגישות וניתוח תרחישים
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>ניתוח רגישות משנה משתנה אחד בכל פעם;</strong> ניתוח תרחישים בונה עולמות שלמים עם מספר משתנים בו-זמנית.
    שניהם נדרשים במזכר אשראי מקצועי.
  </li>
  <li>
    <strong>ארבעת המשתנים הקריטיים בנדל&quot;ן ישראלי:</strong>
    ריבית, עלות בנייה למ&quot;ר, מחיר מכירה/שכירות, וקצב ספיגה.
    ניתוח רגישות לכל אחד מהם — חובה.
  </li>
  <li>
    <strong>גרף הטורנדו</strong> מדרג את הגורמים לפי השפעתם — הגורם בראש הוא זה שהוועדה תתמקד בו.
    הצג אותו בכל מזכר אשראי.
  </li>
  <li>
    <strong>התרחיש הפסימי הוא הבדיקה המרכזית</strong> של הבנק.
    DSCR בתרחיש הפסימי מתחת ל-1.00 = דחייה. בין 1.00–1.10 = אישור בתנאים.
  </li>
  <li>
    <strong>&quot;מבחן הכרית&quot;:</strong> כמה פיחות בשוק נדרש כדי לפגוע בעסקה?
    פחות מ-10% = כרית דקה מדי. יותר מ-20% = עסקה עמידה.
  </li>
</ol>

<h3 style="color:#1a2638;margin-top:24px;">מילון מונחים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מונח בעברית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">English</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח רגישות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Sensitivity Analysis</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בחינת השפעת שינוי משתנה אחד על התוצאה, כשהשאר קבועים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניתוח תרחישים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Scenario Analysis</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הגדרת מספר &quot;עולמות&quot; עקביים עם שינוי מספר משתנים בו-זמנית</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גרף טורנדו</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Tornado Chart</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ויזואליזציה המדרגת גורמי סיכון לפי עוצמת השפעתם</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">קצב ספיגה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Absorption Rate</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מספר יחידות הנמכרות/מושכרות לחודש; קובע משך מכירות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נקודת שבירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Break-Even Point</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ערך המשתנה שמתחתיו העסקה אינה עומדת בדרישות האשראי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מינוף שלילי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Negative Leverage</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מצב שבו ריבית ההלוואה גבוהה מה-Cap Rate; מינוף פוגע בתשואה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תניית שמירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Financial Covenant</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תנאי חוזי מתמשך בהסכם ההלוואה (מינימום DSCR, מקסימום LTV)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שמירת עתודה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Holdback / Reserve Fund</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סכום הלוואה שנשמר אצל המלווה עד עמידה בתנאים</td>
    </tr>
  </tbody>
</table>

<h3 style="color:#1a2638;margin-top:24px;">סיום קורס 1</h3>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:3px;">
  <strong>סיימת את קורס 1 — יסודות מימון נדל&quot;ן!</strong><br><br>
  בחמשת המודולים של קורס זה למדת:
  <ul style="margin:10px 0 0 0;line-height:1.9;">
    <li>יסודות מימון נדל&quot;ן — סוגי נכסים ומבנה שוק</li>
    <li>מבנה עסקאות — שחקנים, מסמכים, תפקידי האנליסט</li>
    <li>חישובי ריבית וזמן — עמלות, מח&quot;מ, NPV</li>
    <li>מדדי אשראי מרכזיים — LTV ו-DSCR</li>
    <li>ניתוח רגישות ותרחישים — הכלים המקצועיים של האנליסט</li>
  </ul>
  <br>
  <strong>הצעד הבא:</strong> עמוד בהצלחה במבחן קורס 1 (75% ומעלה) כדי לפתוח את קורס 2 — ניתוח שוק נדל&quot;ן.
  בהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# Module definitions
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "מדדי אשראי: LTV ו-DSCR",
        "slug": "ltv-dscr",
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
        "title_he": "ניתוח רגישות וניתוח תרחישים",
        "slug": "nituach-reguishut-vetarkhishim",
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
]


class Command(BaseCommand):
    help = "Seed Course 1, Modules 4 and 5 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=1)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 1 not found. Run 'python manage.py seed_data' first."
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

        self.stdout.write(self.style.SUCCESS("\nDone. Modules 4 and 5 seeded successfully."))
