"""
Management command: seed_c02_modules45
Seeds Course 2 (יסודות החשבונאות), Modules 4 and 5 with full reading,
comprehension, exercises, and summary ModuleComponent records.

Usage:
    python manage.py seed_c02_modules45
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — דוח תזרים מזומנים
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  דוח תזרים מזומנים
</h2>

<!-- ===== סעיף 1 — מבוא ===== -->
<h3 style="color:#1a2638;">1. מבוא — למה דוח התזרים קריטי לאנליסט אשראי?</h3>

<p>
  דוח רווח והפסד יכול לשקר. לא בכוונה — אלא בגלל שהוא מבוסס על עקרון הצבירה (Accrual Basis):
  הכנסות נרשמות כשהן נצמחות, לא כשהכסף נכנס לחשבון. פחת, שערוכים, הכנסות עתידיות מוכרות מראש —
  כל אלה יוצרים פער בין הרווח החשבונאי לבין המציאות התזרימית.
</p>

<p>
  <strong>דוח תזרים המזומנים (Cash Flow Statement)</strong> מציג את <em>התנועה בפועל</em> של כסף —
  מה נכנס לחשבון הבנק של החברה ומה יצא ממנו. זהו הדוח שאינו ניתן לעיוות בקלות: כסף נכנס או לא נכנס.
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל בסיסי לאנליסט:</strong> אנליסט אשראי נדל&quot;ן חייב לקרוא את דוח תזרים המזומנים
  <em>לפני</em> שהוא מגיע למסקנות על רווחיות. חברה יכולה לדווח על רווח של מיליונים ובמקביל
  להיות בחנק תזרימי — מצב שמאותת על פשיטת רגל אפשרית.
</div>

<p>
  הדוח מחולק לשלושה חלקים, המשקפים את שלושת פעילויות החברה:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">חלק</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שם בעברית</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מה מופיע בו?</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שאלת מפתח</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Operating CF</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פעילות שוטפת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">גביית שכירות, תשלום לספקים, שכר עובדים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">האם ליבת העסק מייצרת כסף?</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Investing CF</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פעילות השקעה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רכישת/מכירת נכסים, השקעות הון, הלוואות לצדדים קשורים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">האם החברה מרחיבה את נכסיה?</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">Financing CF</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פעילות מימון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הלוואות שנלקחו/הוחזרו, גיוס מניות, דיבידנדים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כיצד ממומנת הצמיחה?</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 2 — פעילות שוטפת ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. פעילות שוטפת (Operating Activities)</h3>

<p>
  פעילות שוטפת מציגה את תזרים המזומנים שנוצר מ<strong>ליבת הפעילות העסקית</strong>.
  עבור חברת נדל&quot;ן מניב, המשמעות היא:
</p>

<ul style="line-height:1.9;">
  <li><strong>כניסת כסף:</strong> גביית שכירות מדיירים, קבלת דמי ניהול, גביית ריבית על הלוואות שניתנו</li>
  <li><strong>יציאת כסף:</strong> תשלום לספקי שירותים (ניקיון, אבטחה, תחזוקה), תשלום שכר עובדים,
    תשלום מסים, תשלומי ריבית על הלוואות (לפי IFRS)</li>
</ul>

<p>
  זהו החלק <strong>הקריטי ביותר</strong> לאנליסט אשראי. תזרים שוטף שלילי לאורך זמן הוא אות אדום —
  גם אם הדוחות מציגים רווח חשבונאי גבוה.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — תזרים שוטף שלילי הוא דגל אדום:</strong><br>
  בשוק הנדל&quot;ן הישראלי נפוץ התרחיש הבא: חברת נדל&quot;ן מדווחת על &quot;רווח&quot; גדול בשל שערוך נכסים
  לפי שווי הוגן (IFRS). אך שערוך הוא רווח נייר — אין כסף שנכנס. אם בפועל הגבייה מהדיירים
  נמוכה, ההוצאות השוטפות גבוהות, ואין כסף לשלם חשבונות — החברה בבעיה קשה
  למרות ה&quot;רווח&quot; שמוצג.
</div>

<!-- ===== סעיף 3 — פעילות השקעה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. פעילות השקעה (Investing Activities)</h3>

<p>
  פעילות ההשקעה מתעדת תזרימים הקשורים ל<strong>נכסים לטווח ארוך</strong>:
</p>

<ul style="line-height:1.9;">
  <li><strong>תזרים שלילי (יציאה):</strong> רכישת נכסי נדל&quot;ן, בנייה והשבחה (CAPEX),
    מתן הלוואות לחברות בנות, רכישת ניירות ערך לטווח ארוך</li>
  <li><strong>תזרים חיובי (כניסה):</strong> מכירת נכסים, פירעון הלוואות שניתנו, מכירת השקעות</li>
</ul>

<p>
  תזרים השקעה שלילי <em>אינו בהכרח רע</em> — הוא לעתים קרובות מעיד על צמיחה, השקעה בעתיד.
  השאלה היא: <strong>כיצד מימנו את ההשקעה?</strong> מתזרים שוטף בריא — מצוין.
  בחוב חדש בלבד — דורש בדיקה מעמיקה.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — חברת נדל&quot;ן ישראלית:</strong><br>
  חברה רכשה בניין משרדים בתל אביב ב-80,000,000 ₪ והשקיעה 5,000,000 ₪ נוספים בשיפוצים.
  בסעיף פעילות השקעה יופיע: <strong>(85,000,000) ₪</strong> — כלומר יציאת מזומן.
  במקביל, מכרה חניון ישן ב-12,000,000 ₪ — שיופיע כ<strong>+12,000,000 ₪</strong>.
  סך פעילות השקעה: (73,000,000) ₪.
</div>

<!-- ===== סעיף 4 — פעילות מימון ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. פעילות מימון (Financing Activities)</h3>

<p>
  פעילות המימון מראה כיצד <strong>ממנת החברה את פעילותה</strong> — מחוב או מהון עצמי:
</p>

<ul style="line-height:1.9;">
  <li><strong>תזרים חיובי:</strong> קבלת הלוואות חדשות מבנקים/גופים חוץ-בנקאיים, גיוס מניות (IPO, הנפקת זכויות)</li>
  <li><strong>תזרים שלילי:</strong> פירעון הלוואות (קרן), תשלום דיבידנד לבעלי מניות, רכישה עצמית של מניות</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה קריטית — הלוואה היא לא הכנסה:</strong><br>
  תזרים מימון חיובי גבוה (כלומר חוב חדש) <strong>אינו הצלחה</strong> — זהו כסף שחייבים להחזיר.
  חברה שמממנת את פעילותה השוטפת בהלוואות חדשות נמצאת בסיכון: ברגע שאשראי זה לא יתחדש,
  היא עלולה לקרוס. אנליסט טוב תמיד שואל: "מאיפה בא הכסף לשלם את שכר הדירה?"
  אם התשובה היא "מהלוואה" — זוהי בעיה קשה.
</div>

<!-- ===== סעיף 5 — שיטה ישירה מול שיטה עקיפה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. שיטה ישירה מול שיטה עקיפה</h3>

<p>
  סעיף פעילות שוטפת יכול להיות מוצג בשתי שיטות — ההבדל מהותי להבנת הנתונים:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">קריטריון</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שיטה ישירה (Direct)</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שיטה עקיפה (Indirect)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נקודת פתיחה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מפרטת כל זרם מזומן ישיר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מתחילה ברווח הנקי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אופן הצגה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">גביות מלקוחות, תשלומים לספקים, שכר — בנפרד</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מתאמת את הרווח לתזרים (הוסף פחת, הפחת שינוי חייבים וכו')</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נפיצות בישראל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נדירה — מחייבת תיעוד פרטני</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שכיחה מאוד — קלה יותר להכנה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">העדפת אנליסטים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מועדפת — שקיפות גבוהה יותר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מקובלת אך מחייבת ניתוח נוסף</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תוצאה סופית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">זהה — שתי השיטות מגיעות לאותה תוצאה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">זהה</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>מדוע השיטה העקיפה שכיחה יותר?</strong> כי קל יותר לתת דיווח חשבונאי על רווח ולהתאים אותו,
  מאשר לפרט כל תנועת מזומן בנפרד. IFRS מאפשר שתי השיטות, אך מעודד את הישירה.
</p>

<!-- ===== סעיף 6 — ההתאמות בשיטה עקיפה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. התאמות עיקריות בשיטה העקיפה</h3>

<p>
  כשמשתמשים בשיטה העקיפה, מתחילים מהרווח הנקי ומבצעים התאמות:
</p>

<h4 style="color:#1976d2;">6.1 הוספה חזרה של הוצאות לא-מזומניות</h4>

<ul style="line-height:1.9;">
  <li>
    <strong>פחת ופחת רכוש בלתי מוחשי (Depreciation &amp; Amortization):</strong>
    הפחת הוא הוצאה בדוח רווח והפסד, אך <em>אין תשלום כסף בפועל</em> בתקופה.
    לכן מוסיפים אותו חזרה לרווח הנקי.
  </li>
  <li>
    <strong>הפסדים/רווחים מהשקעות ונכסים:</strong>
    רווח ממכירת נכס מועבר לסעיף פעילות השקעה — מנטרלים אותו מהפעילות השוטפת.
  </li>
  <li>
    <strong>שינויים בשווי הוגן של נכסים (IFRS):</strong>
    עלייה בשווי נכס השקעה נרשמת כרווח אך אינה מזומן — מנטרלים אותה.
  </li>
</ul>

<h4 style="color:#1976d2;margin-top:20px;">6.2 שינויים בהון החוזר</h4>

<p>
  <strong>הון חוזר (Working Capital)</strong> = נכסים שוטפים פחות התחייבויות שוטפות.
  שינויים בו משפיעים על תזרים המזומנים השוטף:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פריט</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">עלייה → השפעה על תזרים</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הסבר</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">חייבים (Receivables)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;font-weight:bold;">שלילית (−)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מכרנו יותר אך גבינו פחות — כסף תקוע אצל הלקוח</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">זכאים (Payables)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#2e7d32;font-weight:bold;">חיובית (+)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">קנינו יותר אך שילמנו פחות — כסף נשאר אצלנו</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">מלאי (Inventory)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;font-weight:bold;">שלילית (−)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">קנינו יותר מלאי — שילמנו כסף</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">מקדמות מלקוחות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;color:#2e7d32;font-weight:bold;">חיובית (+)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">קיבלנו כסף מראש לפני מסירת שירות</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 7 — דוגמה מספרית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">7. דוגמה מספרית — גישור רווח נקי לתזרים שוטף (שיטה עקיפה)</h3>

<p>
  <strong>חברת גלבוע נכסים בע&quot;מ</strong> — חברת נדל&quot;ן מניב ישראלית, שנת 2025:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;">
  <strong>נקודת פתיחה:</strong><br>
  רווח נקי לפי דוח רווח והפסד&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5,000,000 ₪<br>
  <br>
  <strong>התאמות — הוצאות לא-מזומניות:</strong><br>
  (+) פחת על נכסי השקעה&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+800,000 ₪<br>
  (−) רווח משערוך נכסים (IFRS)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2,500,000) ₪<br>
  (−) רווח ממכירת נכס מניב (הועבר להשקעה)&nbsp;(300,000) ₪<br>
  <br>
  <strong>התאמות — שינויים בהון חוזר:</strong><br>
  (−) עלייה בחייבים&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1,200,000) ₪<br>
  (+) עלייה בזכאים&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+400,000 ₪<br>
  (−) ירידה במקדמות מדיירים&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(150,000) ₪<br>
  (+) עלייה בהתחייבויות מסים שוטפות&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+250,000 ₪<br>
  ─────────────────────────────────────────────<br>
  <strong>תזרים מזומנים מפעילות שוטפת:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2,300,000 ₪</strong>
</div>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>ניתוח הדוגמה:</strong><br>
  שימו לב: הרווח הנקי היה 5,000,000 ₪ — נראה מרשים. אבל לאחר ניטרול שערוך הנכסים
  (2,500,000 ₪ שהוא רווח נייר בלבד) והתאמות הון חוזר, התזרים השוטף בפועל עמד על
  2,300,000 ₪ בלבד — פחות ממחצית הרווח המדווח. ללא הניתוח הזה, אנליסט עלול להגזים
  בהערכת החוסן הפיננסי של החברה.
</div>

<!-- ===== סעיף 8 — FCF ===== -->
<h3 style="color:#1a2638;margin-top:28px;">8. תזרים חופשי — Free Cash Flow (FCF)</h3>

<p>
  <strong>תזרים חופשי</strong> הוא הסכום שנותר לחברה לאחר שהיא משקיעה בשמירת נכסיה ובצמיחה.
  זהו אחד המדדים החשובים ביותר לניתוח אשראי:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  FCF = תזרים מפעילות שוטפת − CAPEX (הוצאות השקעה בנכסים)
</div>

<p>
  <strong>CAPEX</strong> (Capital Expenditure) הם ההוצאות על נכסים לטווח ארוך — שיפוצים, ציוד, בנייה.
  חברה שה-FCF שלה חיובי ועקבי מסוגלת:
</p>

<ul style="line-height:1.9;">
  <li>לשלם חוב מתוך תפעול — ולא מהלוואות חדשות</li>
  <li>לחלק דיבידנד ולצמוח — ללא תלות מוחלטת בשוק ההון</li>
  <li>לעמוד בהתחייבויות בעת האטה כלכלית</li>
</ul>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — המשך חברת גלבוע נכסים:</strong><br>
  תזרים שוטף: 2,300,000 ₪<br>
  CAPEX (שיפוצים שנתיים + החלפת מערכות): (900,000) ₪<br>
  <strong>FCF = 1,400,000 ₪</strong><br><br>
  FCF חיובי ומהותי — החברה מממנת את שמירת הנכסים ועדיין נותרת לה יתרה.
  לאנליסט אשראי: זהו סימן טוב ליכולת פירעון.
</div>

<!-- ===== סעיף 9 — טבלת השוואה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">9. מה מופיע בכל חלק — טבלת השוואה מלאה</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פריט</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פעילות שוטפת</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פעילות השקעה</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פעילות מימון</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">גביית שכירות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">תשלום שכר עובדים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">רכישת נכס מניב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">מכירת בניין ישן</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">קבלת הלוואה בנקאית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">פירעון הלוואה (קרן)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">תשלום ריבית על הלוואה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓ (IFRS)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#888;">אפשרי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">דיבידנד לבעלי מניות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">גיוס הון ממניות חדשות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">CAPEX (שיפוצים, ציוד)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;color:#2e7d32;">✓</td>
      <td style="border:1px solid #ccc;padding:8px 12px;text-align:center;">—</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 10 — מהשטח ===== -->
<h3 style="color:#1a2638;margin-top:28px;">10. מהשטח — כשרווח חשבונאי הפיל את האנליסט</h3>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — תיק אמיתי (ספטמבר 2023):</strong><br><br>
  ועדת אשראי של מוסד מימון חוץ-בנקאי בישראל דנה בבקשת הלוואה של 15,000,000 ₪
  לחברת נדל&quot;ן מסחרי בראשון לציון. דוח הרווח והפסד הציג רווח נקי של 8,200,000 ₪ —
  תוצאה מרשימה. שניים מחברי הוועדה הסכימו לאשר מיידית.<br><br>
  אנליסט בכיר עצר את הדיון ודרש לראות את דוח התזרים. הנתונים גילו:
  <ul style="margin-top:8px;">
    <li>תזרים שוטף: <strong>(1,800,000) ₪</strong> — שלילי!</li>
    <li>6,500,000 ₪ מתוך הרווח הנקי היו שערוך נכסים לפי שווי הוגן — ללא כסף אמיתי</li>
    <li>החברה גבתה שכירות בפועל בסך 3,200,000 ₪ אך שילמה 5,000,000 ₪ הוצאות שוטפות</li>
    <li>הפער מומן מהלוואה גישור שנלקחה ב-2022</li>
  </ul>
  הבקשה נדחתה. שלושה חודשים לאחר מכן פתחה החברה בהליכי פשרה עם הנושים.<br><br>
  <em>המסקנה: רווח חשבונאי ללא תזרים שוטף חיובי הוא לא רווח — הוא אשליה.</em>
</div>

<!-- ===== סעיף 11 — אינטגרציה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">11. שלושת הדוחות — מבט משולב</h3>

<p>
  דוח תזרים המזומנים קשור ישירות לשני הדוחות האחרים:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>קישור לדוח רווח והפסד:</strong>
    הרווח הנקי הוא נקודת הפתיחה בשיטה העקיפה. ההתאמות מסבירות את הפער בין הרווח החשבונאי לתזרים האמיתי.
  </li>
  <li>
    <strong>קישור למאזן:</strong>
    התזרים המצטבר של שלושת הסעיפים מסביר את השינוי ביתרת המזומנים בין שתי שנות המאזן.
    אם פתחנו עם 5,000,000 ₪ ביתרת מזומנים, וסיכום כל שלושת הסעיפים הוא +2,000,000 ₪ —
    נצפה לראות 7,000,000 ₪ במזומן בסוף השנה.
  </li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  מזומן סגירה = מזומן פתיחה + תזרים שוטף + תזרים השקעה + תזרים מימון
</div>

<p>
  בדיקת הסוגרים הזו היא בדיקת אינטגריטי בסיסית — אם הסכומים אינם מסתדרים, יש טעות או מניפולציה.
</p>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של דוח תזרים המזומנים ושלושת סעיפיו. יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים סיווג תזרימים, חישוב FCF ופרשנות תרחישים. "
    "יש לך שתי הזדמנויות לכל שאלה — השתמש בניסיון הראשון בזהירות."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — דוח תזרים מזומנים
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>דוח התזרים מחולק לשלושה סעיפים:</strong>
    פעילות שוטפת (ליבת העסק), פעילות השקעה (נכסים לטווח ארוך), ופעילות מימון (חוב והון).
    כל סעיף עונה על שאלה שונה.
  </li>
  <li>
    <strong>תזרים שוטף שלילי = דגל אדום.</strong>
    גם אם הרווח הנקי חיובי — אם הפעילות השוטפת שורפת מזומן, הלווה תלוי בגורמים חיצוניים.
    זהו אחד הסיכונים הגדולים באשראי נדל&quot;ן.
  </li>
  <li>
    <strong>השיטה העקיפה מגשרת בין רווח לתזרים.</strong>
    ההתאמות העיקריות: חיבור חזרה של פחת (הוצאה לא מזומנית), ניטרול שערוכים,
    ושינויים בהון חוזר (חייבים, זכאים).
  </li>
  <li>
    <strong>FCF = תזרים שוטף פחות CAPEX.</strong>
    זהו ה&quot;כסף האמיתי&quot; שהחברה מייצרת לאחר שמירת נכסיה. FCF חיובי ועקבי — חברה חזקה.
  </li>
  <li>
    <strong>הלוואה היא לא הכנסה.</strong>
    תזרים מימון חיובי גבוה מעיד שהחברה לוקחת חוב — לא שהיא מרוויחה. יש להחזיר את הכסף הזה.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פעילות שוטפת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Operating Activities</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תזרים מזומנים מליבת הפעילות העסקית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פעילות השקעה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Investing Activities</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תזרים מרכישה ומכירה של נכסים לטווח ארוך</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פעילות מימון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Financing Activities</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תזרים מגיוס וממחזור חוב והון עצמי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיטה עקיפה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Indirect Method</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הצגת תזרים שוטף ע&quot;י התאמת הרווח הנקי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שיטה ישירה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Direct Method</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">פירוט כל זרם מזומן בנפרד (גבייה, תשלומים)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">פחת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Depreciation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הוצאה חשבונאית לא מזומנית על שחיקת ערך נכס</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תזרים חופשי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Free Cash Flow (FCF)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תזרים שוטף פחות CAPEX — ה&quot;כסף האמיתי&quot;</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הון חוזר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Working Capital</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נכסים שוטפים פחות התחייבויות שוטפות</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר למודול 5:</strong><br>
  הבנו כעת שלושה דוחות — מאזן, רווח והפסד, ותזרים מזומנים.
  אך המספרים בדוחות הם רק ה&quot;כותרת&quot;. הפרטים הקריטיים — המדיניות החשבונאית, התחייבויות נסתרות,
  עסקאות עם צדדים קשורים, ואירועים אחרי המאזן — כל אלה מסתתרים ב<strong>ביאורים</strong>.
  במודול הבא נלמד כיצד לקרוא ביאורים כמו מקצוען.
</div>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — ביאורים ומדיניות חשבונאית
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  ביאורים ומדיניות חשבונאית
</h2>

<!-- ===== סעיף 1 — מבוא ===== -->
<h3 style="color:#1a2638;">1. מבוא — מדוע הביאורים חשובים יותר מהמספרים?</h3>

<p>
  רוב הקוראים של דוחות כספיים עוצרים בדף הראשון: הרווח הנקי, הנכסים הכוללים, ההון העצמי.
  הם מחשבים יחסים פיננסיים, בונים אקסל — ועוברים הלאה.
  אנליסט מיומן יודע ש<strong>הסיפור האמיתי נמצא בביאורים</strong>.
</p>

<p>
  <strong>ביאורים (Notes to Financial Statements)</strong> הם חלק בלתי נפרד מהדוחות הכספיים.
  תקני IFRS מחייבים חברות לפרט בביאורים:
</p>

<ul style="line-height:1.9;">
  <li>את <strong>המדיניות החשבונאית</strong> שבחרו ויישמו</li>
  <li>את ה<strong>הנחות הניהוליות</strong> שעמדו בבסיס הערכות חשובות</li>
  <li>את ה<strong>סיכונים וההתחייבויות</strong> שאינן מופיעות ישירות בדוחות</li>
  <li><strong>מידע נוסף</strong> ומפורט על עסקאות ומצבים מהותיים</li>
</ul>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל מקצועי:</strong> אנליסט שדילג על הביאורים ראה רק חצי מהתמונה.
  הביאורים יכולים לחשוף ערבויות בשווי מאות מיליונים שאינן מופיעות במאזן,
  תביעות משפטיות מהותיות, הנחות ניהוליות שמנופחות שווי נכסים, ועסקאות עם בעלי שליטה
  שמוצגות בתנאים לא שיוויוניים.
</div>

<!-- ===== סעיף 2 — מדיניות חשבונאית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. ביאור מדיניות חשבונאית (Accounting Policy Note)</h3>

<p>
  ביאור המדיניות החשבונאית הוא בדרך כלל <strong>הביאור הראשון</strong> בדוחות.
  הוא מסביר את הכללים שהחברה בחרה להחיל על הדוחות שלה.
  מדוע זה חשוב? כי IFRS מאפשרת לחברות <em>לבחור</em> בין גישות שונות — והבחירה משפיעה משמעותית על המספרים.
</p>

<h4 style="color:#1976d2;">2.1 הכרה בהכנסות — IFRS 15</h4>

<p>
  <strong>IFRS 15</strong> קובע מתי ואיך חברה מכירה בהכנסה. לחברות נדל&quot;ן הכלל הרלוונטי:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>שכירות שוטפת:</strong> מוכרת לאורך תקופת החוזה — חשבונאות פשוטה.
  </li>
  <li>
    <strong>מכירת דירות (יזמות):</strong> ניתן להכיר לפי אחוז השלמה (over time) אם עומדים בתנאים,
    או רק עם מסירת הדירה (point in time). ההבדל יכול להיות ענק: חברה שמכירה 500 דירות
    ב-2 מיליארד ₪ תדווח על הכנסות שונות לחלוטין בהתאם לגישה שתבחר.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  בהשוואת שתי חברות יזמיות — ודא תחילה שהן משתמשות באותה מדיניות הכרה בהכנסה.
  אם אחת מכירה over time ואחרת point in time — ההשוואה ישירה בין ההכנסות שלהן מוטעית.
</div>

<h4 style="color:#1976d2;margin-top:20px;">2.2 שיטת הפחת ושיעורי פחת</h4>

<p>
  חברה חייבת לפרט בביאור:
</p>

<ul style="line-height:1.9;">
  <li><strong>שיטת הפחת:</strong> קו ישר (Straight-Line, הנפוץ ביותר), יורד (Declining Balance), או לפי ייצור</li>
  <li><strong>שיעורי הפחת:</strong> לדוגמה — מבנים 2–4%, ציוד 10–20%, רכב 15–25%</li>
  <li><strong>ערך שיורי:</strong> כמה מניחים שהנכס יהיה שווה בסוף חייו הכלכליים</li>
</ul>

<p>
  שינוי שיטת פחת או הארכת אורך חיים שימושי — <strong>משפיע על הרווח הנקי</strong>
  ומצריך גילוי מפורש. חברה שמאריכה את חיי הנכס מ-25 שנה ל-40 שנה — הפחת השנתי ירד
  וה&quot;רווח&quot; יעלה, אך זה אינו שיפור אמיתי.
</p>

<h4 style="color:#1976d2;margin-top:20px;">2.3 שיטת הערכת נכסי השקעה</h4>

<p>
  זהו <strong>אחד הביאורים המשמעותיים ביותר</strong> לחברות נדל&quot;ן. IFRS מאפשר שתי גישות:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">קריטריון</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מודל שווי הוגן (Fair Value)</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מודל עלות (Cost Model)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ערך במאזן</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שווי שוק לפי שמאות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עלות מקורית פחות פחת</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">השפעה על רווח</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">שינוי בשווי → לדוח רווח והפסד (רווח/הפסד נייר)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ללא השפעה (פחת בלבד)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תנודתיות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">גבוהה — תלוי בשוק</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נמוכה — יציב וצפוי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שימוש בישראל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רוב חברות הנדל&quot;ן המניב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חלק מחברות הבנייה/יזמות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">השלכה לאנליסט</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">יש לנטרל שערוכים מהרווח לצורך ניתוח תזרים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הנכסים עשויים להיות מוערכים בחסר</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 3 — אירועים לאחר תאריך המאזן ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. אירועים לאחר תאריך המאזן</h3>

<p>
  הדוחות הכספיים מוצגים לתאריך המאזן (לרוב 31.12). אך בין תאריך המאזן לבין מועד פרסום
  הדוחות עוברים בדרך כלל 2–4 חודשים. <strong>מה קורה בתקופה הזו?</strong>
</p>

<p>
  IAS 10 מגדיר שני סוגי אירועים לאחר תאריך המאזן:
</p>

<h4 style="color:#1976d2;">3.1 אירועים מתאימים (Adjusting Events)</h4>

<p>
  אירועים שמספקים ראיות לגבי <em>מצב שהתקיים</em> בתאריך המאזן — ולכן <strong>מחייבים תיקון</strong>
  של הדוחות:
</p>

<ul style="line-height:1.9;">
  <li>לקוח שהגיש בקשת פשיטת רגל לאחר המאזן — מעיד שהיה בקשיים כבר בתאריך המאזן → יש לבצע הפרשת חובות מסופקים</li>
  <li>נכס שנמכר אחרי תאריך המאזן במחיר שונה בהרבה מהשווי המאזני — מעיד שהשמאות בתאריך המאזן לא דייקה → ייתכן ויש לתקן</li>
  <li>גילוי של עוולה/מרמה שהתרחשה לפני המאזן</li>
</ul>

<h4 style="color:#1976d2;margin-top:20px;">3.2 אירועים לא מתאימים (Non-Adjusting Events)</h4>

<p>
  אירועים שהתרחשו <em>לאחר</em> תאריך המאזן ואינם קשורים למצב שהיה קיים בו —
  <strong>לא מתוקנים בדוחות, אך חייבים בגילוי:</strong>
</p>

<ul style="line-height:1.9;">
  <li>הלוואה גדולה שנחתמה לאחר המאזן</li>
  <li>רכישת חברה לאחר המאזן</li>
  <li>אסון טבע (שריפה, רעידת אדמה) שפגע בנכסים לאחר המאזן</li>
  <li>שינוי רגולטורי מהותי שנכנס לתוקף לאחר המאזן</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — אנליסט אשראי בפעולה:</strong><br>
  חברת נדל&quot;ן דיווחה על שווי נכס בשיעור 45,000,000 ₪ בתאריך המאזן (31.12.2024).
  בביאורים: &quot;ביאור 18 — אירועים לאחר תאריך המאזן: ביום 15.2.2025 נחתם חוזה מכירת הנכס בסך
  38,500,000 ₪.&quot;<br><br>
  זהו אירוע מתאים: המכירה חשפה שהשמאות הייתה גבוהה ב-6,500,000 ₪.
  האנליסט חייב לקחת זאת בחשבון בחישוב LTV האמיתי.
</div>

<!-- ===== סעיף 4 — התחייבויות תלויות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. התחייבויות תלויות (Contingent Liabilities)</h3>

<p>
  <strong>התחייבות תלויה</strong> היא חוב פוטנציאלי שתלוי בהתממשות אירוע עתידי לא ודאי.
  היא אינה מוכרת כהתחייבות במאזן — אך חייבת בגילוי אם ההסתברות אינה רחוקה.
</p>

<h4 style="color:#1976d2;">סוגים נפוצים בנדל&quot;ן ישראלי:</h4>

<ul style="line-height:1.9;">
  <li>
    <strong>ערבויות (Guarantees):</strong>
    חברה שנתנה ערבות לחברה בת — אם הבת לא תעמוד בהלוואה, האם תחויב לשלם.
    ערבות אינה מופיעה כהתחייבות במאזן, אך מופיעה בביאורים. סכומים של מאות מיליונים
    עשויים להתחבא שם.
  </li>
  <li>
    <strong>תביעות משפטיות תלויות (Pending Lawsuits):</strong>
    תביעות של שוכרים, ספקים, רשויות. חברה מחויבת לגלות את הסכום הנטען ואת
    הערכת ההנהלה לגבי תוצאת התביעה.
  </li>
  <li>
    <strong>מחלוקות מס:</strong>
    ביקורת מס תלויה ועומדת; תביעת מע&quot;מ; מחלוקת עם רשות מקרקעי ישראל על מס רכישה.
  </li>
  <li>
    <strong>התחייבויות תכנוניות:</strong>
    כתנאי לאישור תב&quot;ע, החברה התחייבה לבנות תשתיות ציבוריות בשווי עשרות מיליונים.
  </li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;line-height:2.0;">
  <strong>דוגמה — הערכת התחייבות תלויה:</strong><br>
  תביעה: 8,000,000 ₪ (מחיר מקרקעין שנטען כי לא שולם)<br>
  הסתברות לפי עורך הדין: 40% שהחברה תחויב<br>
  ערך צפוי (Expected Loss) = 8,000,000 × 40% = 3,200,000 ₪<br>
  <br>
  האנליסט: מוסיף 3,200,000 ₪ ל&quot;חוב מותאם&quot; בחישוב יחסי המינוף.
</div>

<p>
  <strong>ההבדל בין גילוי להכרה:</strong>
</p>

<ul style="line-height:1.9;">
  <li><strong>הכרה (Recognition):</strong> ההתחייבות מוכנסת למאזן — כאשר ההסתברות גבוהה (&gt;50%) וניתן לאמוד את הסכום</li>
  <li><strong>גילוי (Disclosure):</strong> מוזכרת בביאורים בלבד — כאשר ההסתברות אפשרית (possible) אך לא סבירה</li>
</ul>

<!-- ===== סעיף 5 — עסקאות צד קשור ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. עסקאות צד קשור (Related Party Transactions)</h3>

<p>
  <strong>צד קשור</strong> הוא ישות שיש לה יכולת להשפיע על החברה — או שהחברה יכולה להשפיע עליה.
  בהגדרה הישראלית (לפי IAS 24 ודיני החברות): בעלי שליטה, דירקטורים, מנהלים בכירים,
  חברות בנות ואחיות, וקרובי משפחה של אלה.
</p>

<h4 style="color:#1976d2;">עסקאות נפוצות בנדל&quot;ן ישראלי:</h4>

<ul style="line-height:1.9;">
  <li><strong>הלוואות לבעלי שליטה:</strong> חברה מלווה כסף לאחד מבעלי המניות הגדולים שלה — לעתים ללא ריבית או בתנאים נוחים</li>
  <li><strong>דמי ניהול:</strong> החברה משלמת דמי ניהול לחברה של בעל השליטה — האם הסכומים סבירים?</li>
  <li><strong>מכירת/רכישת נכסים בין חברות קשורות:</strong> האם המחיר היה שוק? מי ביצע שמאות?</li>
  <li><strong>ערבויות הדדיות:</strong> חברה-אם ערבה לחוב של חברה-בת — ולהפך</li>
</ul>

<h4 style="color:#1976d2;margin-top:20px;">סיכון Tunneling:</h4>

<p>
  <strong>Tunneling</strong> הוא העברה של ערך מחברה ציבורית לבעל שליטה — באמצעות עסקאות שאינן בתנאי שוק.
  בניתוח אשראי, זהו סיכון קריטי: בעל שליטה שמוציא עושר מהחברה מקשה על יכולתה לעמוד בחובותיה.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>שאלות שאנליסט חייב לשאול:</strong><br>
  <ul style="margin-top:8px;line-height:2.0;">
    <li>האם עסקאות הצד הקשור אושרו על ידי ועדת הביקורת?</li>
    <li>האם הוצגה חוות דעת של יועץ עצמאי שהמחיר שוק?</li>
    <li>מה הסכום המצטבר של עסקאות אלה — גדול ביחס לרווח החברה?</li>
    <li>האם ישנן הלוואות לבעלי שליטה שאינן מוחזרות?</li>
  </ul>
</div>

<!-- ===== סעיף 6 — צ'קליסט 5 ביאורים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. 5 ביאורים שאנליסט חייב לקרוא תמיד</h3>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>צ'קליסט לניתוח ביאורים — חמישה ביאורים מחייבים:</strong><br><br>

  <strong>1. ביאור מדיניות חשבונאית</strong><br>
  בדוק: שיטת הערכת נכסי השקעה (שווי הוגן/עלות), שיטת פחת, מדיניות הכרה בהכנסה.
  האם המדיניות שמרנית או אגרסיבית? האם שונתה השנה?<br><br>

  <strong>2. ביאור נכסי השקעה</strong><br>
  בדוק: הנחות הערכה (discount rate, yield rate), שם המעריך (שמאי חיצוני/פנימי), תאריך השמאות.
  האם ה-cap rate שהשתמשו בו סביר לשוק הנוכחי?<br><br>

  <strong>3. ביאור התחייבויות ועסקאות עם צדדים קשורים</strong><br>
  בדוק: גובה הלוואות לבעלי שליטה, דמי ניהול, עסקאות בין-חברתיות.
  חשב את שיעורם מסך הנכסים/רווח — האם מהותי?<br><br>

  <strong>4. ביאור התחייבויות תלויות וערבויות</strong><br>
  בדוק: סכומי ערבויות שנתנה החברה, תביעות משפטיות תלויות, מחלוקות מס.
  הוסף את הסכומים המהותיים לחוב המותאם בחישוב יחסי מינוף.<br><br>

  <strong>5. ביאור אירועים לאחר תאריך המאזן</strong><br>
  בדוק: עסקאות מהותיות שנחתמו לאחר המאזן, שינויים בהסכמי הלוואה, התפתחויות בתביעות.
  עדכן את הניתוח שלך בהתאם.
</div>

<!-- ===== סעיף 7 — מהשטח ===== -->
<h3 style="color:#1a2638;margin-top:28px;">7. מהשטח — כשעסקאות צד קשור הסתירו חולשה פיננסית</h3>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — מקרה ישראלי (2021):</strong><br><br>
  חברת נדל&quot;ן משפחתית ניהלה שמונה בניינים מסחריים בגוש דן.
  הדוחות הציגו הכנסות שוטפות של 9,000,000 ₪ ורווח נקי של 3,500,000 ₪.
  מוסד מימון חוץ-בנקאי שקל לתת לה הלוואה של 22,000,000 ₪.<br><br>
  האנליסט שיירה קרה קראה את ביאורי עסקאות הצד הקשור וגילתה:
  <ul style="margin-top:8px;line-height:2.0;">
    <li>דמי ניהול לחברת האחזקות של בעל השליטה: 2,800,000 ₪ לשנה</li>
    <li>הלוואות שניתנו לבעל השליטה באופן אישי: 4,500,000 ₪ — ללא ריבית, ללא מועד פירעון</li>
    <li>נכס שנמכר לאשתו של בעל השליטה ב-6,000,000 ₪ — שמאות עצמאית העריכה ב-9,200,000 ₪</li>
  </ul>
  תמונה שונה לחלוטין: בנטרול דמי הניהול — הרווח האמיתי היה 700,000 ₪ בלבד.
  ה&quot;הלוואה&quot; לבעל השליטה היא בפועל כסף שיצא מהחברה ולא יחזור.
  ושווי הנכסים מנופח ב-3,200,000 ₪.<br><br>
  הבקשה נדחתה. <em>המסקנה: ביאורי צד קשור הם לעתים המסמך החשוב ביותר בדוחות.</em>
</div>

<!-- ===== סעיף 8 — ביקורת חשבונאית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">8. ביקורת חשבונאית ודוח רואה החשבון המבקר</h3>

<p>
  דוחות כספיים של חברות ציבוריות וחברות גדולות מבוקרות על ידי <strong>רואה חשבון מבקר (Auditor)</strong>
  חיצוני ועצמאי. דוח המבקר מקדים את הדוחות ומציין:
</p>

<ul style="line-height:1.9;">
  <li><strong>חוות דעת חלקה (Unqualified/Clean Opinion):</strong> הדוחות מציגים בצורה נאותה את המצב הפיננסי</li>
  <li><strong>חוות דעת עם הסתייגות (Qualified Opinion):</strong> קיימת בעיה מהותית בסעיף מסוים</li>
  <li><strong>חוות דעת שלילית (Adverse Opinion):</strong> הדוחות אינם מציגים נאותה — מצב חמור מאוד</li>
  <li><strong>הימנעות מחוות דעת (Disclaimer):</strong> המבקר לא הצליח לבסס דעה — מצב חמור</li>
  <li><strong>דגש עניין (Emphasis of Matter):</strong> המבקר מפנה תשומת לב לנושא מסוים מבלי לפגוע בחוות הדעת</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — פסקאות הסתייגות ודגש:</strong><br>
  כל חריגה מחוות דעת חלקה מחייבת עצירה מיידית ובחינה מעמיקה.
  &quot;ספק לגבי עסק חי&quot; (Going Concern) — כלומר המבקר מטיל ספק ביכולת החברה להמשיך לפעול —
  הוא כנראה הנורה האדומה החמורה ביותר שאנליסט אשראי יכול לפגוש בדוחות.
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של ביאורים, מדיניות חשבונאית וסיכוני צד קשור. יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים זיהוי סוגי אירועים, הערכת התחייבויות תלויות וניתוח עסקאות צד קשור. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — ביאורים ומדיניות חשבונאית
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>הביאורים הם ה&quot;דוח האמיתי&quot;.</strong>
    המספרים בדוחות הם סיכום — הביאורים הם ההסבר. אנליסט שדילג על הביאורים ראה רק
    חצי מהתמונה הפיננסית.
  </li>
  <li>
    <strong>מדיניות חשבונאית שונה = מספרים שונים, גם עם אותה מציאות עסקית.</strong>
    שיטת ערכת נכסים, שיטת פחת, ומועד הכרה בהכנסה — כולן משפיעות על הרווח המדווח.
    השווה חברות רק לאחר שנוודאת שהמדיניות זהה.
  </li>
  <li>
    <strong>אירועים מתאימים מחייבים תיקון הדוחות; לא מתאימים — גילוי בלבד.</strong>
    אנליסט אשראי חייב לקרוא ביאור אירועים לאחר תאריך המאזן ולהפחית את השפעתם
    מהנתונים שבבסיס החלטתו.
  </li>
  <li>
    <strong>התחייבויות תלויות וערבויות הן &quot;חוב מוסתר&quot;.</strong>
    יש לחשב ערך צפוי (הסתברות × סכום) ולהוסיפו לחוב המותאם בניתוח המינוף.
  </li>
  <li>
    <strong>עסקאות צד קשור — בדוק תמיד האם הן בתנאי שוק.</strong>
    דמי ניהול מנופחים, הלוואות לבעל שליטה, ומכירות נכסים בתנאים בלתי שיוויוניים
    עלולים להסתיר tunneling ולהחליש את יכולת פירעון החוב.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ביאורים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Notes to Financial Statements</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הסברים ופירוטים הנלווים לדוחות הכספיים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מדיניות חשבונאית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Accounting Policy</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכללים שבחרה החברה ליישם בהצגת הדוחות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">אירוע מתאים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Adjusting Event</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">אירוע לאחר המאזן המחייב תיקון הדוחות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">התחייבות תלויה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Contingent Liability</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חוב פוטנציאלי התלוי בהתממשות אירוע עתידי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ערבות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Guarantee</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">התחייבות לשלם חוב של אחר אם הוא לא ישלם</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">צד קשור</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Related Party</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ישות שיש לה השפעה על החברה או שהחברה משפיעה עליה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הכרה בהכנסה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Revenue Recognition</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכלל הקובע מתי ואיך הכנסה נרשמת בדוחות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ביקורת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Audit</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בחינה עצמאית של הדוחות ע&quot;י רואה חשבון מבקר</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לבחינה הסופית:</strong><br>
  השלמתם את כל חמשת מודולי קורס 2 — יסודות החשבונאות.
  עברתם ממאזן בסיסי, דרך דוח רווח והפסד, נכסי השקעה בשיטות הערכה שונות, דוח תזרים מזומנים,
  ועכשיו ביאורים ומדיניות חשבונאית.<br><br>
  הבחינה הסופית תבחן את כלל החומר: קריאת קטעי דוחות אמיתיים, זיהוי בעיות,
  חישוב מדדים ואיתור דגלים אדומים. הגיעו מוכנים — ובהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": "דוח תזרים מזומנים",
        "slug": "doch-tizrim-mezumanim",
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
        "title_he": "ביאורים ומדיניות חשבונאית",
        "slug": "beurim-umediniut-heshbonaut",
        "estimated_minutes": 40,
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
    help = "Seed Course 2, Modules 4 and 5 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=2)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 2 not found. Run 'python manage.py seed_data' first."
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
