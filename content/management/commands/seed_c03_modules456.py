"""
Management command: seed_c03_modules456
Seeds Course 3 (ניתוח מתקדם של יזמי נדל"ן), Modules 4, 5, and 6 with full reading,
comprehension, exercises, and summary ModuleComponent records.

Usage:
    python manage.py seed_c03_modules456
"""

from django.core.management.base import BaseCommand

from content.models import (
    Course,
    ComponentType,
    Module,
    ModuleComponent,
)

# ---------------------------------------------------------------------------
# MODULE 4 — ניתוח קבוצת יזמות נדל"ן
# ---------------------------------------------------------------------------

M4_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  ניתוח קבוצת יזמות נדל&quot;ן
</h2>

<!-- ===== סעיף 1 — מבוא ===== -->
<h3 style="color:#1a2638;">1. מבוא — מדוע ניתוח קבוצתי שונה מניתוח חברה בודדת?</h3>

<p>
  ניתוח אשראי של יזם נדל&quot;ן בודד הוא יחסית פשוט: קוראים את הדוחות, מחשבים יחסים, מסיקים מסקנות.
  אך מרבית יזמי הנדל&quot;ן הגדולים בישראל אינם חברה אחת — הם <strong>קבוצה של חברות</strong>: חברת-אם,
  עשרות חברות-בנות, ומאות חברות ייעודיות (SPV) לפרויקטים שונים.
</p>

<p>
  אנליסט שמסתפק בדוחות חברת-האם בלבד עלול לקבל תמונה מעוותת לחלוטין. החוב הגדול
  מסתתר בחברות-הבנות. הרווח האמיתי — או ההפסד — מחולק בין עשרות ישויות.
  הערבויות זורמות בין כולן.
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל יסוד לאנליסט:</strong> אנליסט אשראי נדל&quot;ן חייב לעבוד תמיד עם <em>הדוחות המאוחדים</em>
  של הקבוצה. דוחות חברת-אם בלבד הם חסרי משמעות לצורך ניתוח סיכון.
</div>

<!-- ===== סעיף 2 — דוחות מאוחדים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. דוחות מאוחדים — מה הם ולמה הם קיימים?</h3>

<p>
  <strong>דוחות מאוחדים (Consolidated Financial Statements)</strong> הם דוחות כספיים המציגים את
  כלל חברות הקבוצה כאילו היו ישות אחת אחידה. תקן IFRS 10 קובע את הכללים לאיחוד.
</p>

<h4 style="color:#1976d2;">2.1 מה מתאחד — ומה מנוטרל?</h4>

<p>
  בתהליך האיחוד, רואי החשבון מבצעים שתי פעולות מרכזיות:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>סיכום:</strong> נכסי כל החברות, ההתחייבויות, ההכנסות וההוצאות — מסוכמים יחדיו.
  </li>
  <li>
    <strong>ניטרול (Elimination):</strong> עסקאות <em>בין</em> חברות הקבוצה מנוטרלות לחלוטין.
    אם חברת-אם מכרה נכס לחברת-בת ב-10 מיליון ₪ — הרווח מנוטרל. אם חברת-אם הלוותה לחברת-בת
    5 מיליון ₪ — ההלוואה וההתחייבות קיזזים זו את זו. תוצאה: הדוח המאוחד מציג רק עסקאות
    עם <em>גורמים חיצוניים</em> לקבוצה.
  </li>
</ul>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פריט</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">טיפול בדוח מאוחד</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הסיבה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הלוואה מחברת-אם לחברת-בת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מנוטרל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חוב "פנימי" — אין חוב כלפי חיצוניים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מכירת נכס בין חברות קבוצה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מנוטרל + רווח מנוטרל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הנכס לא עזב את הקבוצה כלכלית</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">דמי ניהול מחברת-בת לחברת-אם</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכנסה וההוצאה מנוטרלות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">העברה פנימית ללא השפעה חיצונית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חוב לבנק חיצוני של חברת-בת</td>
      <td style="border:1px solid #ccc;padding:8px 12px;"><strong>נכלל במלואו</strong></td>
      <td style="border:1px solid #ccc;padding:8px 12px;">התחייבות כלפי גורם חיצון לקבוצה</td>
    </tr>
  </tbody>
</table>

<h4 style="color:#1976d2;margin-top:20px;">2.2 זכויות מיעוט (Minority Interest)</h4>

<p>
  לעיתים חברת-אם שולטת בחברת-בת אך אינה מחזיקה ב-100% מהמניות. חלק המניות שבידי בעלים חיצוניים
  נקרא <strong>זכויות מיעוט</strong> (Non-Controlling Interest, NCI).
</p>

<p>
  בדוח המאוחד, זכויות מיעוט מופיעות:
</p>

<ul style="line-height:1.9;">
  <li><strong>במאזן:</strong> כחלק מההון העצמי, נפרד מהון בעלי המניות של החברה-האם</li>
  <li><strong>בדוח רווח והפסד:</strong> חלק הרווח/הפסד השייך לבעלי המיעוט מוצג בנפרד</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  הון עצמי בדוח מאוחד כולל זכויות מיעוט. לצורך חישוב יחסי מינוף אמיתיים,
  הפרד בין הון שמיוחס לבעלי מניות הקבוצה לבין הון המיעוט — שניהם לא שווים
  מבחינת גישת הנושה.
</div>

<!-- ===== סעיף 3 — SPV ואיחוד לפי IFRS 10 ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. SPV ואיחוד לפי IFRS 10</h3>

<p>
  יזמי נדל&quot;ן בישראל נוהגים להקים <strong>חברה ייעודית (Special Purpose Vehicle, SPV)</strong>
  לכל פרויקט. המטרות: הגנה משפטית, ניהול פיננסי נפרד, הסדרת שעבודים לטובת המלווה.
</p>

<p>
  השאלה המהותית לאנליסט: <strong>האם ה-SPV מאוחד בדוחות חברת-האם?</strong>
</p>

<p>
  <strong>IFRS 10</strong> קובע שחברה מאחדת SPV אם היא <em>שולטת</em> בו. שליטה קיימת כאשר:
</p>

<ul style="line-height:1.9;">
  <li>לחברה יש <strong>כוח</strong> לכוון את פעילויות ה-SPV הרלוונטיות</li>
  <li>לחברה יש <strong>חשיפה לתשואות משתנות</strong> מהפרויקט</li>
  <li>לחברה יש <strong>יכולת לנצל כוחה</strong> כדי להשפיע על אותן תשואות</li>
</ul>

<p>
  בפועל: רוב יזמי הנדל&quot;ן בישראל <strong>מאחדים</strong> את ה-SPVים שלהם, כי הם שולטים בהם
  במלואם. אם SPV <em>אינו</em> מאוחד — חוב הפרויקט אינו מופיע בדוח המאוחד. זו יכולה להיות
  הטעיה חמורה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  IFRS 10 — בדיקת שליטה:<br>
  שליטה = כוח + חשיפה לתשואות משתנות + קשר בין כוח לתשואות<br>
  אם שלושת התנאים מתקיימים → חובה לאחד!
</div>

<!-- ===== סעיף 4 — חוב קבוצתי לעומת חוב פרויקטלי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. חוב קבוצתי לעומת חוב פרויקטלי</h3>

<p>
  אחד הטעויות הנפוצות ביותר בניתוח יזמי נדל&quot;ן: מסתכלים על חוב חברת-האם בלבד ומתעלמים
  מהחוב המוחזק ברמת ה-SPVים.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה מספרית — קבוצת "אלפא יזמות":</strong><br><br>
  <table style="border-collapse:collapse;width:100%;font-size:13px;">
    <thead>
      <tr style="background:#1a2638;color:#fff;">
        <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">ישות</th>
        <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">חוב (מ' ₪)</th>
        <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הון (מ' ₪)</th>
        <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">D/E</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:#f9f9f9;">
        <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חברת-אם (standalone)</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">150</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">100</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">1.5x</td>
      </tr>
      <tr>
        <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">SPV פרויקט א'</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">80</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">20</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">4.0x</td>
      </tr>
      <tr style="background:#f9f9f9;">
        <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">SPV פרויקט ב'</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">120</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">30</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">4.0x</td>
      </tr>
      <tr>
        <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">SPV פרויקט ג'</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">50</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">15</td>
        <td style="border:1px solid #ccc;padding:8px 12px;">3.3x</td>
      </tr>
      <tr style="background:#e8f5e9;font-weight:bold;">
        <td style="border:1px solid #ccc;padding:8px 12px;"><strong>קבוצה מאוחדת</strong></td>
        <td style="border:1px solid #ccc;padding:8px 12px;"><strong>400</strong></td>
        <td style="border:1px solid #ccc;padding:8px 12px;"><strong>100</strong></td>
        <td style="border:1px solid #ccc;padding:8px 12px;color:#c62828;"><strong>4.0x</strong></td>
      </tr>
    </tbody>
  </table>
  <br>
  אנליסט שראה רק D/E של 1.5x ברמת חברת-האם עשוי להמליץ על מתן אשראי.
  אנליסט שראה D/E מאוחד של 4.0x יבחן זאת בזהירות רבה הרבה יותר.
</div>

<!-- ===== סעיף 5 — ערבויות צולבות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. ערבויות צולבות (Cross-Guarantees) — סיכון ההדבקה</h3>

<p>
  <strong>ערבויות צולבות</strong> הן ערבויות שמעניקות חברות בקבוצה אחת לשנייה לטובת מלווים שונים.
  המנגנון נפוץ מאוד בישראל: כאשר בנק מלווה לפרויקט SPV, הוא לעיתים דורש ערבות של חברת-האם
  ו/או של SPVים אחרים בקבוצה.
</p>

<p>
  <strong>הבעיה הקריטית:</strong> אם פרויקט אחד נכשל ומופעלת הערבות — חברה אחרת בקבוצה,
  שעל הנייר נראית בריאה לחלוטין, עלולה להיות בבעיה קשה בן-רגע.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — סיכון ההדבקה (Contagion Risk):</strong><br>
  ערבויות צולבות יוצרות מצב שבו כשל בפרויקט אחד יכול "להדביק" פרויקטים אחרים. מלווה
  שנתן הלוואה ל-SPV ב' על בסיס ערבות SPV א' — צריך להכיר את מצב SPV א' לא פחות מ-SPV ב'.
  לא לעשות זאת זה עיוורון ניתוחי.
</div>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — כשערבות צולבת הפילה פרויקט בריא:</strong><br><br>
  קבוצת יזמות בינונית פעלה עם שלושה פרויקטים: א', ב', ו-ג'. פרויקט א' — פינוי-בינוי בחיפה —
  נקלע לקשיים בגלל ויכוחים עם הרשות המקומית ועיכובים בהיתרים. הבנק המלווה לפרויקט א'
  הפעיל ערבות שנתנה SPV של פרויקט ב' — מגדל מגורים בחולון שהיה בתהליך בנייה תקין
  ועם מכירות גבוהות מהממוצע.<br><br>
  הפעלת הערבות הציבה SPV ב' בפני קריסת נזילות. הוא נאלץ למכור דירות מוכנות בהנחה חדה
  כדי לעמוד בתשלום — מה שפגע בשווי הנכסים ובאמון הרוכשים. נזק של עשרות מיליונים לפרויקט
  שלכשעצמו היה רווחי.<br><br>
  <em>המסקנה: לפני מתן הלוואה, בדוק את מפת הערבויות של כלל הקבוצה — לא רק של ה-SPV הנדון.</em>
</div>

<!-- ===== סעיף 6 — עסקאות בינחברותיות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. עסקאות בינחברותיות ועסקאות צד קשור</h3>

<p>
  בתוך קבוצת חברות נדל&quot;ן, ישנן עסקאות רבות שנראות חיצוניות אך הן פנימיות:
</p>

<ul style="line-height:1.9;">
  <li>
    <strong>דיבידנדים ממעלה:</strong> SPV פרויקטלי מחלק דיבידנד לחברת-האם לאחר סיום המכירות.
    בדוחות מאוחדים — מנוטרל. אך בניתוח נזילות ברמת חברת-האם — חשוב.
  </li>
  <li>
    <strong>דמי ניהול:</strong> חברת-האם מוציאה חשבונית לכל SPV על "שירותי ניהול". מנוטרל באיחוד,
    אך מסייע לחברת-האם לגלגל הוצאות פנימיות.
  </li>
  <li>
    <strong>מכירת נכסים בין חברות הקבוצה:</strong> SPV א' מוכר קרקע ל-SPV ב'. גם אם נראה "רווח" ברמת
    SPV א' — ברמה מאוחדת הרווח מנוטרל עד לרגע שהנכס ייצא מהקבוצה.
  </li>
</ul>

<p>
  <strong>הסיכון:</strong> עסקאות בינחברותיות עלולות לשמש להסתרת בעיות. SPV בהפסד יכול
  "למכור" נכס לחברה קשורה במחיר מנופח, לייצר רווח נייר, ולהסתיר את מצבו האמיתי.
</p>

<!-- ===== סעיף 7 — ריכוזיות פרויקטלית ===== -->
<h3 style="color:#1a2638;margin-top:28px;">7. ריכוזיות פרויקטלית (Concentration Risk)</h3>

<p>
  גם קבוצת יזמות עם דוחות מאוחדים מרשימים עלולה להיות פגיעה קיצונית אם <strong>חלק גדול מהרווח
  מגיע ממקור אחד</strong>: פרויקט יחיד, אזור גיאוגרפי יחיד, או לקוח מוסדי יחיד.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  ריכוזיות = (הכנסות ממקור בודד) / (סך הכנסות הקבוצה) × 100<br>
  ריכוזיות מעל 40% = סיכון מוגבר; מעל 70% = סיכון גבוה מאוד
</div>

<p>
  יזם עם 80% מרווחיו הצפויים מפרויקט אחד הוא למעשה יזם עם פרויקט אחד — כל קושי בפרויקט זה
  ישפיע ישירות על יכולת הפירעון לכלל הנושים.
</p>

<!-- ===== סעיף 8 — מהשטח ===== -->
<h3 style="color:#1a2638;margin-top:28px;">8. מהשטח — "יזם שמציג רק דוח חברת-האם מסתיר משהו"</h3>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — ניסיון מכיר אשראי בכיר, תל-אביב 2022:</strong><br><br>
  יזם הגיש בקשת מימון של 35 מיליון ₪. הגיש דוחות של חברת-האם: הון עצמי של 45 מיליון ₪,
  חוב של 60 מיליון ₪ — D/E של 1.3x. נראה בסדר.<br><br>
  דרשנו את הדוחות המאוחדים של הקבוצה. גילינו 14 SPVים, עם חוב כולל של 280 מיליון ₪ ופרויקטים
  בשלבים שונים. D/E מאוחד: 6.2x. שניים מהפרויקטים היו בהפסד. ערבויות צולבות קישרו את כולם.<br><br>
  <em>הבקשה נדחתה. לקח: יזם שמציג רק דוחות חברת-האם — ורק אחרי לחץ מגיש מאוחדים — כנראה
  מסתיר את גודל החוב הקבוצתי.</em>
</div>
"""

M4_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מבנה קבוצתי, איחוד דוחות, ערבויות צולבות וריכוזיות פרויקטלית. "
    "יש לך ניסיון אחד לכל שאלה."
)

M4_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים חישוב D/E מאוחד לעומת standalone, "
    "זיהוי עסקאות בינחברותיות לניטרול, וניתוח מפת ערבויות צולבות. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M4_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — ניתוח קבוצת יזמות נדל&quot;ן
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>עבוד תמיד עם דוחות מאוחדים.</strong>
    דוחות חברת-האם בלבד אינם מציגים את מלוא תמונת החוב והסיכון.
    הדוח המאוחד — לאחר ניטרול עסקאות בינחברותיות — הוא הבסיס לניתוח.
  </li>
  <li>
    <strong>IFRS 10 קובע מי מאוחד — לא רצון הדירקטוריון.</strong>
    אם קיימת שליטה בפועל ב-SPV, האיחוד הוא חובה. SPV לא מאוחד בניגוד ל-IFRS 10
    הוא דגל אדום חשבונאי חמור.
  </li>
  <li>
    <strong>D/E מאוחד שונה לחלוטין מ-D/E standalone.</strong>
    הדוגמה המספרית הדגימה: 1.5x ברמת חברת-האם מול 4.0x ברמה מאוחדת —
    ההבדל עשוי להיות ההבדל בין אישור לדחייה.
  </li>
  <li>
    <strong>ערבויות צולבות יוצרות סיכון הדבקה.</strong>
    כשל בפרויקט אחד יכול לגרור פרויקטים בריאים. תמיד מפה את מלוא מבנה הערבויות
    לפני אישור מימון.
  </li>
  <li>
    <strong>ריכוזיות מעל 40% מחייבת בחינה מעמיקה.</strong>
    יזם שתלוי בפרויקט בודד לרוב רווחיו — חשוף לסיכון בלתי סביר.
    הגוון פרויקטלי וגיאוגרפי הוא גורם מפחית סיכון מהותי.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">דוחות מאוחדים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Consolidated Statements</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דוחות המציגים את כלל הקבוצה כישות אחת</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חברה ייעודית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">SPV</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חברה שהוקמה לצורך פרויקט ספציפי בלבד</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ערבויות צולבות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Cross-Guarantees</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ערבויות הדדיות בין חברות בקבוצה לנושים שונים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ריכוזיות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Concentration Risk</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תלות גבוהה בפרויקט, לקוח, או אזור גיאוגרפי יחיד</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">זכויות מיעוט</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Minority Interest / NCI</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חלק ההון בחברת-בת שאינו בבעלות חברת-האם</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חוב קבוצתי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Group Debt</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סך החוב של כל ישויות הקבוצה כולל SPVים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">IFRS 10</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">IFRS 10</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תקן הקובע את כללי האיחוד של דוחות קבוצת חברות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ניטרול בינחברות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Elimination</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ביטול עסקאות פנימיות בין חברות הקבוצה בדוח המאוחד</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר למודול 5:</strong><br>
  למדנו כיצד לראות את הקבוצה כמכלול — מבנה, חוב מאוחד, וערבויות. כעת נעבור לשלב הבא:
  איך <em>מזהים</em> שמשהו לא בסדר בדוחות עצמם? במודול 5 נלמד את הדגלים האדומים —
  הסימנים המוקדמים שמסמנים לאנליסט כי הסיכון גבוה הרבה יותר ממה שנראה על פני השטח.
</div>
"""

# ---------------------------------------------------------------------------
# MODULE 5 — דגלים אדומים (Red Flags)
# ---------------------------------------------------------------------------

M5_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  דגלים אדומים בניתוח נדל&quot;ן ישראלי
</h2>

<!-- ===== מבוא ===== -->
<h3 style="color:#1a2638;">מבוא — מהו "דגל אדום" ולמה לא מספיק דגל אחד?</h3>

<p>
  <strong>דגל אדום (Red Flag)</strong> הוא ממצא בדוחות הכספיים או בנתוני החברה שמצביע על סיכון מוגבר
  — חשבונאי, תפעולי, או אסטרטגי. הוא אינו בהכרח ראיה לתרמית או כישלון,
  אלא <em>אות אזהרה שדורש חקירה נוספת</em>.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה חשובה:</strong><br>
  דגל אדום בודד עשוי להיות בעל הסבר תמים. שניים במקביל דורשים חקירה מעמיקה.
  שלושה ומעלה — הסיכון גבוה מאוד ויש לדון ברמת ועדת האשראי.
  אנליסט טוב לא נבהל מדגל אחד — אבל גם לא מתעלם ממנו.
</div>

<p>
  להלן קטלוג שיטתי של שמונת הדגלים האדומים החשובים ביותר בניתוח יזמי נדל&quot;ן בישראל.
</p>

<!-- ===== דגל 1 ===== -->
<h3 style="color:#c62828;margin-top:28px;">1. הון חוזר שלילי מתמשך</h3>

<p>
  <strong>מה זה:</strong> במשך שנתיים או יותר, ההתחייבויות השוטפות (חוב לטווח קצר, ספקים, לקוחות ששילמו מראש)
  עולות על הנכסים השוטפים (מזומן, חייבים, מלאי לטווח קצר).
</p>

<p>
  <strong>מה זה מסמן:</strong> החברה ממנת פרויקטים ארוכי-טווח בחוב קצר-טווח — מצב בלתי ברות כלכלית.
  בכל עת עלול גורם חיצוני (בנק שלא מחדש קו אשראי, ספק שדורש תשלום מיידי)
  להכניס את החברה לחנק תזרימי.
</p>

<p>
  <strong>פעולת אנליסט:</strong> בקש תחזית תזרים מזומנים ל-12 חודשים קדימה. בחן את מח&quot;מ ההתחייבויות
  לעומת לוח הזמנים הצפוי של פרויקטים. בדוק האם יש קווי אשראי שאינם נוצלו.
</p>

<!-- ===== דגל 2 ===== -->
<h3 style="color:#c62828;margin-top:24px;">2. פערים גדולים בין רווח לתזרים שוטף</h3>

<p>
  <strong>מה זה:</strong> הדוח מציג רווח נקי חיובי, אך תזרים מזומנים שוטף (Operating Cash Flow)
  שלילי לאורך שנה או יותר.
</p>

<p>
  <strong>מה זה מסמן:</strong> הרווח הוא נייר — שערוכי IAS 40, הכרה בהכנסה לפני גבייה,
  או פחת נמוך מהמציאות. הכסף בפועל אינו נכנס לחברה. חברות כאלה קורסות לא מחוסר
  רווח, אלא מחוסר מזומן.
</p>

<p>
  <strong>פעולת אנליסט:</strong> חשב Operating Cash Flow מנוטרל — הוסף בחזרה: (א) שערוכי נכסים,
  (ב) הכנסות שטרם נגבו, (ג) רווחים מניטרול בינחברות. אם התוצאה עדיין שלילית — בעיה אמיתית.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  OCF מנוטרל = OCF מדווח + שערוכי IAS 40 + הכנסות לא גבויות + רווחי בינחברות<br>
  (כולם מוסיפים בחזרה כי כבר הוחסרו מהרווח וכעת נחסרים גם מהתזרים)
</div>

<!-- ===== דגל 3 ===== -->
<h3 style="color:#c62828;margin-top:24px;">3. גידול חריג בחייבים ללא גידול מקביל בהכנסות</h3>

<p>
  <strong>מה זה:</strong> יתרת חייבים (לקוחות) גדלה בשיעור גבוה בהרבה מהכנסות — לדוגמה,
  הכנסות גדלו ב-15% אך חייבים גדלו ב-60%.
</p>

<p>
  <strong>מה זה מסמן:</strong> חברה מכירה בהכנסה אך לא גובה. יתכן: (א) קונים שחתמו חוזים אך מתקשים
  לסגור עסקאות, (ב) הכרה בהכנסה אגרסיבית לפני שהעסקה בשלה, (ג) במקרים קיצוניים —
  עסקאות פיקטיביות.
</p>

<p>
  <strong>פעולת אנליסט:</strong> בקש דוח ישן חייבים (Aging Report) — כמה מהחייבים הם מעל 90 יום?
  בקש חוזים חתומים לפרויקטים הגדולים. בדוק אחוז ביטולי עסקאות בפרויקטים.
</p>

<!-- ===== דגל 4 ===== -->
<h3 style="color:#c62828;margin-top:24px;">4. שינוי מדיניות חשבונאית</h3>

<p>
  <strong>מה זה:</strong> חברה משנה מדיניות חשבונאית — למשל מעוברת ממודל עלות לשווי הוגן לנכסי השקעה,
  או משנה שיטת הכרה בהכנסה — ובתוצאה: רווחיה עולים חדות.
</p>

<p>
  <strong>מה זה מסמן:</strong> "מאפיינים" של ניהול רווחים (Earnings Management). שאלת המפתח: <em>למה עכשיו?</em>
  שינוי מדיניות לקראת גיוס חוב, דירוג אשראי, או הנפקה — חשוד מאוד.
</p>

<p>
  <strong>פעולת אנליסט:</strong> דרוש הצגה מחדש של הדוחות בשנים קודמות לפי המדיניות החדשה.
  השווה: כמה הרווח היה שונה בשנים הקודמות? האם ביאור המדיניות מסביר בצורה ברורה את הסיבה לשינוי?
</p>

<!-- ===== דגל 5 ===== -->
<h3 style="color:#c62828;margin-top:24px;">5. החלפת רואה חשבון</h3>

<p>
  <strong>מה זה:</strong> החברה מחליפה את רואה החשבון המבקר — במיוחד אם עוברת מבית Big 4 לחברה קטנה,
  או אם זו ההחלפה השלישית בחמש שנים.
</p>

<p>
  <strong>מה זה מסמן:</strong> עשוי להצביע על כך שרואה החשבון הקודם סירב לחתום על הדוחות כפי שהוגשו
  (Auditor Resignation). חברה שמחפשת "רואה חשבון גמיש" — דגל אדום קריטי.
</p>

<p>
  <strong>פעולת אנליסט:</strong> בדוק ב-SEC/EDGAR (לחברות ציבוריות) או בדוח שינויי רואה חשבון
  האם פורסמה גילוי על מחלוקות מהותיות. שאל ישירות את ההנהלה: מדוע הוחלף רואה החשבון?
</p>

<!-- ===== דגל 6 ===== -->
<h3 style="color:#c62828;margin-top:24px;">6. איחור בדיווח</h3>

<p>
  <strong>מה זה:</strong> חברה מגישה דוחות כספיים שנתיים מאוחר ממועד הגשה הקבוע בחוק
  (בדרך כלל 90 יום לאחר סוף שנת הכספים לחברות ציבוריות).
</p>

<p>
  <strong>מה זה מסמן:</strong> עשוי להצביע על: (א) מחלוקת בין ההנהלה לרואה החשבון, (ב) אירועים מהותיים
  שההנהלה מנסה להסתיר או לייפות, (ג) כשל בבקרה פנימית, (ד) אירועים פורנזיים פנימיים.
</p>

<p>
  <strong>פעולת אנליסט:</strong> בחן מדוע האיחור אירע. אם הסיבה אינה טכנית (שינוי מערכת, אסון טבע),
  ודא ש<em>מלוא</em> המידע שנגלה לאחר האיחור נבחן לעומק.
</p>

<!-- ===== דגל 7 ===== -->
<h3 style="color:#c62828;margin-top:24px;">7. גידול חריג בנכסים בלתי מוחשיים (Goodwill)</h3>

<p>
  <strong>מה זה:</strong> גידול מהיר בסעיף מוניטין (Goodwill) או נכסים בלתי מוחשיים אחרים.
</p>

<p>
  <strong>מה זה מסמן:</strong> החברה רכשה נכסים מחברות קשורות במחיר גבוה מהשווי ההוגן — ההפרש
  נרשם כמוניטין. עלול להצביע על מניפולציה: רכישת נכסים "דרך צד קשור" לצורך ניפוח המאזן.
  מוניטין שעלה בחדות ללא רכישה עסקית מוסברת — בעייתי מאוד.
</p>

<p>
  <strong>פעולת אנליסט:</strong> בדוק את ביאור המוניטין — מאיפה הגיע? האם בוצע מבחן ירידת ערך (Impairment Test)?
  האם יש שמאות עצמאית לנכסים שנרכשו?
</p>

<!-- ===== דגל 8 ===== -->
<h3 style="color:#c62828;margin-top:24px;">8. עסקאות צד קשור גדולות ללא שמאות עצמאית</h3>

<p>
  <strong>מה זה:</strong> מכירה או רכישה משמעותית של נכסים בין החברה לגורם קשור (בעל שליטה, קרוב משפחה,
  חברה קשורה) — ללא חוות דעת חיצונית ועצמאית שהמחיר הוא שוק.
</p>

<p>
  <strong>מה זה מסמן:</strong> עלול להצביע על הצגה לא נאותה של ערך הנכסים, tunneling, או
  ניגוד עניינים חמור בהנהלה. אחד הגורמים הנפוצים לדוחות מטעים בענף הנדל&quot;ן.
</p>

<p>
  <strong>פעולת אנליסט:</strong> בדוק אישור ועדת ביקורת, שמאות עצמאית (מי ביצע? מתי?),
  ותנאי העסקה לעומת עסקאות שוק דומות. אם אין שמאות — דרוש אחת לפני אישור.
</p>

<!-- ===== טבלת סיכום ===== -->
<h3 style="color:#1a2638;margin-top:32px;">טבלת סיכום — 8 הדגלים האדומים</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">#</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">שם הדגל</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">מה הוא מסמן?</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">פעולת אנליסט</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">1</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הון חוזר שלילי מתמשך</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מימון ארוך-טווח בחוב קצר-טווח</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תחזית תזרים 12 חודשים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">2</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">רווח חיובי, OCF שלילי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רווח נייר; מזומן אינו נכנס</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חשב OCF מנוטרל</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">3</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">חייבים גדלים מהכנסות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הכרה בהכנסה לפני גבייה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דוח ישן חייבים + חוזים</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">4</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">שינוי מדיניות חשבונאית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">ניהול רווחים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">דרוש הצגה מחדש לתקופות קודמות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">5</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">החלפת רואה חשבון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מחלוקת חשבונאית / חיפוש גמישות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדוק גילוי מחלוקות; שאל את ההנהלה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">6</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">איחור בדיווח</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מחלוקת או אירוע נסתר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדוק סיבת האיחור; קרא כל גילוי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">7</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גידול חריג בגודוויל</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">רכישות מנופחות / ניפוח מאזן</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בדוק מקור הגודוויל + Impairment Test</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">8</td>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">עסקאות צד קשור ללא שמאות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">tunneling / ניגוד עניינים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">בקש שמאות עצמאית לפני אישור</td>
    </tr>
  </tbody>
</table>

<!-- ===== מקרה בוחן ===== -->
<h3 style="color:#1a2638;margin-top:28px;">מקרה בוחן — "חברת גלעד יזמות" (פיקטיבי)</h3>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>פרטי המקרה:</strong><br><br>
  גלעד יזמות הגישה בקשת הלוואה של 28 מיליון ₪ לפרויקט בנייה בבאר-שבע. הדוחות הציגו
  רווח נקי גדל ב-40% משנה לשנה. הנהלה מנוסה, פרויקטים מוכרים. על פניו — עסקה אטרקטיבית.<br><br>
  <strong>מה מצא האנליסט:</strong>
  <ol style="line-height:2.0;margin-top:8px;">
    <li><strong>דגל 1:</strong> הון חוזר שלילי ב-3 שנים ברציפות — לא הוזכר בבקשה</li>
    <li><strong>דגל 2:</strong> OCF שלילי בכל 3 שנים — כל הרווח מגיע משערוכי IAS 40</li>
    <li><strong>דגל 4:</strong> שינוי מדיניות חשבונאית בשנה הנוכחית — מעלות לשווי הוגן</li>
    <li><strong>דגל 5:</strong> החלפת רואה חשבון — מ-Big 4 לחברה קטנה, השנה</li>
    <li><strong>דגל 8:</strong> רכישת קרקע מחברת בעל השליטה ב-12 מיליון ₪ — ללא שמאות עצמאית</li>
  </ol>
  <strong>תוצאה:</strong> הבקשה נדחתה. שמונה עשר חודשים לאחר מכן — חברת גלעד נקלעה להסדר חוב
  עם נושיה הקיימים. <em>אנליסט שהכיר את הדגלים הציל את הארגון מהפסד של עשרות מיליונים.</em>
</div>

<!-- ===== מהשטח ===== -->
<h3 style="color:#1a2638;margin-top:28px;">מהשטח — "הצ'קליסט שלי"</h3>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — כיר אשראי נדל&quot;ן בכיר, 20 שנות ניסיון:</strong><br><br>
  "פיתחתי צ'קליסט אישי של 8 דגלים אדומים. בעשר שנות עבודה בניתוח אשראי נדל&quot;ן,
  לא אישרתי מעולם הלוואה לחברה שהציגה שלושה דגלים או יותר — ולא הייתה עסקה אחת כזו
  שלא הסתיימה בבעיות. לא אחת, לא פעמיים — כל פעם. הסטטיסטיקה מדברת בעד עצמה."
</div>
"""

M5_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת זיהוי דגלים אדומים, פרשנותם, ופעולות האנליסט המתאימות. "
    "יש לך ניסיון אחד לכל שאלה."
)

M5_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים זיהוי דגלים אדומים בתרחישי דוחות מדומים, "
    "חישוב OCF מנוטרל, וניתוח מקרי בוחן של חברות עם מרובה דגלים. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M5_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — דגלים אדומים בניתוח נדל&quot;ן
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>דגל אחד דורש תשומת לב; שניים דורשים חקירה; שלושה — אסור לאשר ללא דיון מעמיק.</strong>
    אף דגל אדום אינו ראיה חד-משמעית לכשל, אך הצטברות דגלים מסמנת סיכון מערכתי.
  </li>
  <li>
    <strong>OCF הוא הדגל האדום הבסיסי ביותר.</strong>
    רווח נקי חיובי עם OCF שלילי מזה שנתיים הוא כמעט מזומן לבעיית נזילות עתידית.
    תמיד נטרל שערוכים ורווחי נייר מהתזרים.
  </li>
  <li>
    <strong>שינוי מדיניות חשבונאית לפני גיוס חוב — חשוד עד ראיה לסתור.</strong>
    דרוש תמיד הצגה מחדש של התקופות הקודמות תחת המדיניות החדשה.
  </li>
  <li>
    <strong>החלפת רואה חשבון היא הדגל האדום הקל ביותר לזיהוי ולעתים החמור ביותר.</strong>
    חברה שמחליפה Big 4 ב"רואה חשבון שמבין" — אות לכך שה-Big 4 סירב לחתום.
  </li>
  <li>
    <strong>עסקאות צד קשור ללא שמאות עצמאית — עצור הכל.</strong>
    ללא חוות דעת עצמאית, אין לאנליסט בסיס לאמת את שווי הנכסים.
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
      <td style="border:1px solid #ccc;padding:8px 12px;">ממצא המצביע על סיכון מוגבר הדורש חקירה</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הון חוזר</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Working Capital</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נכסים שוטפים פחות התחייבויות שוטפות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">הסתייגות רו&quot;ח</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Auditor Qualification</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">חוות דעת שאינה חלקה — מסמנת בעיה מהותית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גידול לא אורגני</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Inorganic Growth</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">צמיחה הנובעת מרכישות ולא מפעילות עצמית</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מדיניות חשבונאית</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Accounting Policy</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">כללים שבחרה החברה ליישם בהצגת הדוחות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">איחור דיווח</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Late Filing</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הגשת דוחות כספיים לאחר המועד הנדרש בחוק</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נכסים בלתי מוחשיים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Intangible Assets</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">נכסים ללא מהות פיזית: מוניטין, פטנטים, רישיונות</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">גילוי מהותי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Material Disclosure</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מידע שחשיפתו עשויה לשנות החלטת משקיע/נושה</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר למודול 6:</strong><br>
  עד כה למדנו לאסוף מידע, לנתח מבנה קבוצתי, ולזהות דגלים אדומים. עכשיו מגיע השלב שבו
  כל הניתוח צריך להפוך ל<em>מסמך</em> — מזכר אשראי מקצועי שיסייע לוועדת האשראי לקבל החלטה
  מושכלת. במודול 6 נלמד את מלאכת כתיבת סיכום ניתוח אשראי.
</div>
"""

# ---------------------------------------------------------------------------
# MODULE 6 — כתיבת סיכום ניתוח
# ---------------------------------------------------------------------------

M6_READING_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  כתיבת סיכום ניתוח — מזכר האשראי המקצועי
</h2>

<!-- ===== סעיף 1 — מבוא ===== -->
<h3 style="color:#1a2638;">1. מבוא — למה הכתיבה חשובה לא פחות מהניתוח</h3>

<p>
  אנליסט יכול לבצע את הניתוח המדויק ביותר בעולם — אך אם אינו יודע לתעד ולתקשר אותו,
  הניתוח לא יועיל לאיש. <strong>מזכר האשראי (Credit Memo)</strong> הוא המסמך שבאמצעותו
  ועדת האשראי מקבלת את ההחלטה. הוא גם מסמך משפטי שמתעד את שרשרת ההחלטות.
</p>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — כלל הזהב:</strong><br>
  "הממו הטוב ביותר שקראתי ניתן להבנה על ידי מנהל שאינו מומחה פיננסי — תוך 5 דקות.
  הממו הגרוע ביותר הסתיר את המסקנה בפסקה השמינית, מאחורי 40 עמודי נתונים.
  הממו הטוב שכנע. הגרוע — בזבז זמן של כולם ויצר סיכון מוסדי."
</div>

<!-- ===== סעיף 2 — מבנה מזכר האשראי ===== -->
<h3 style="color:#1a2638;margin-top:28px;">2. מבנה מזכר האשראי — שישה חלקים</h3>

<h4 style="color:#1976d2;">חלק 1: תמצית מנהלים (Executive Summary) — פסקה אחת</h4>

<p>
  פסקה אחת, לא יותר משלוש משפטים: שם החברה, בקשת המימון, וההמלצה.
  הקורא צריך לדעת בשניות האם ההמלצה היא לאשר, לדחות, או לאשר בתנאים.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  דוגמה:<br>
  "אלפא יזמות בע&quot;מ מבקשת הלוואת ליווי בסך 42 מיליון ₪ לפרויקט מגורים בחולון.
  לאחר ניתוח דוחות כספיים לשנים 2021–2023 ובדיקת מבנה הקבוצה, המלצתנו היא:
  אישור מותנה, בכפוף לשלושה תנאים שפורטו בסעיף ו'."
</div>

<h4 style="color:#1976d2;margin-top:20px;">חלק 2: רקע החברה</h4>

<ul style="line-height:1.9;">
  <li><strong>תעשייה וסגמנט:</strong> מגורים, מסחרי, מניב, מעורב?</li>
  <li><strong>בעלות ושליטה:</strong> מי בעל השליטה? מה מבנה החזקה?</li>
  <li><strong>היסטוריה:</strong> מתי הוקמה החברה? מה הפרויקטים הבולטים שהשלימה?</li>
  <li><strong>פרויקטים פעילים:</strong> כמה פרויקטים כעת? באיזה שלב? היכן?</li>
</ul>

<h4 style="color:#1976d2;margin-top:20px;">חלק 3: ממצאים פיננסיים</h4>

<p>
  טבלת יחסים לשלוש שנים, מגמות, והשוואה לבנצ'מרק תעשייתי:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">יחס</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">2021</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">2022</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">2023</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">בנצ'מרק</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">הערה</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">D/E (מאוחד)</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">≤3.5</td>
      <td style="border:1px solid #ccc;padding:8px 12px;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">DSCR</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">≥1.25</td>
      <td style="border:1px solid #ccc;padding:8px 12px;"></td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">יחס שוטף</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">≥1.0</td>
      <td style="border:1px solid #ccc;padding:8px 12px;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">OCF / חוב</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">[X.X]</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">≥0.15</td>
      <td style="border:1px solid #ccc;padding:8px 12px;"></td>
    </tr>
  </tbody>
</table>

<h4 style="color:#1976d2;margin-top:20px;">חלק 4: הערכת סיכונים</h4>

<p>
  רשימה של 3–5 סיכונים ספציפיים, עם <strong>כימות</strong> במידת האפשר:
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>לא לכתוב:</strong> "מינוף גבוה"<br>
  <strong>לכתוב:</strong> "Debt/EBITDA של 6.2x לעומת בנצ'מרק ענפי של 3.5x.
  בהנחה שה-EBITDA נשאר יציב, יידרשו 6.2 שנים של כלל ה-EBITDA להחזר החוב — סיכון
  מינוף גבוה מאוד. רגישות: ירידה של 20% ב-EBITDA תעלה ה-Debt/EBITDA ל-7.8x."
</div>

<h4 style="color:#1976d2;margin-top:20px;">חלק 5: נקודות בירור פתוחות (Open Questions)</h4>

<p>
  רשימה של המסמכים או הבהרות שנדרשות לפני קבלת החלטה סופית.
  שלב זה אינו חולשה — הוא מקצועיות:
</p>

<ul style="line-height:1.9;">
  <li>דוחות כספיים מבוקרים לשנת 2023 (הוגשו רק מאזניים ביניים)</li>
  <li>חוזי מכר חתומים לפרויקט X — כמה מ-120 הדירות נמכרו בפועל?</li>
  <li>שמאות עצמאית לקרקע שנרכשה מחברת בעל השליטה</li>
  <li>הסבר לאיחור הדיווח ברבעון ג' 2023</li>
</ul>

<h4 style="color:#1976d2;margin-top:20px;">חלק 6: המלצה</h4>

<p>
  ברורה ומנומקת: <strong>לאשר / לדחות / לאשר בתנאים</strong>.
  אם בתנאים — ציין בדיוק מה הם (שעבודים, אמות מידה פיננסיות, מסמכים חסרים).
</p>

<!-- ===== סעיף 3 — עקרונות שפה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">3. עקרונות שפה — כל טענה מגובה במספר</h3>

<p>
  המזכר המקצועי נכתב בעברית רשמית, ללא ז'רגון. כל טענה חייבת להיות מגובה בנתון מספרי.
  אסור לכתוב משפט הערכתי ללא נתון תומך.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;font-size:13px;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">כתיבה חלשה ❌</th>
      <th style="border:1px solid #ccc;padding:8px 12px;text-align:right;">כתיבה מקצועית ✓</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">"לחברה נזילות נמוכה"</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"יחס שוטף של 0.87 — מתחת לבנצ'מרק ענפי של 1.4, ובירידה משנת 2021 (1.12)"</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">"המינוף גבוה"</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"Debt/EBITDA של 6.2x לעומת 3.5x בענף — יידרשו 6+ שנות EBITDA לפירעון מלא"</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;">"חברה מרוויחה"</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"רווח נקי של 8.2 מ' ₪ — אך לאחר ניטרול שערוכי IAS 40 (6.1 מ' ₪), הרווח התפעולי המנוטרל הוא 2.1 מ' ₪"</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;">"מבנה חוב מסוכן"</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">"42% מהחוב קצר-טווח, לעומת 18% ממוצע ענפי; ריכוז פירעון של 28 מ' ₪ בקרוב"</td>
    </tr>
  </tbody>
</table>

<!-- ===== סעיף 4 — כימות סיכונים ===== -->
<h3 style="color:#1a2638;margin-top:28px;">4. כימות סיכונים — השיטה</h3>

<p>
  כל סיכון ניתן לכמת בשלושה שלבים:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
  שלב 1: מה הסיכון? ("ביקוש למגורים ירד בצפון הארץ ב-15% בשנה האחרונה")<br>
  שלב 2: מה ההשפעה הכמותית? ("ירידה של 15% במכירות תוריד הכנסות ב-12 מ' ₪ ותפחית DSCR מ-1.4 ל-0.9")<br>
  שלב 3: מה גורם המפחת? ("70% מהדירות נמכרו כבר; הסיכון מוגבל ל-30% הנותרים")
</div>

<!-- ===== סעיף 5 — שימוש בטבלאות ===== -->
<h3 style="color:#1a2638;margin-top:28px;">5. טבלאות וגרפים — מה כן, מה לא</h3>

<ul style="line-height:1.9;">
  <li>
    <strong>כן:</strong> טבלת מגמת יחסים (3 שנים) — מראה תמונה אמינה ומעובדת
  </li>
  <li>
    <strong>כן:</strong> טבלת רגישות DSCR — מה קורה אם שיעור פנוי עולה מ-5% ל-15%?
  </li>
  <li>
    <strong>כן:</strong> טבלת דגלים אדומים שזוהו — שם הדגל, חומרה, פעולה מוצעת
  </li>
  <li>
    <strong>לא:</strong> גרפי עוגה צבעוניים ומרשימים שאינם מוסיפים מידע
  </li>
  <li>
    <strong>לא:</strong> נתונים גולמיים ללא ניתוח — אנליסט צריך לספר סיפור, לא להעתיק דוחות
  </li>
</ul>

<!-- ===== שלד מזכר לדוגמה ===== -->
<h3 style="color:#1a2638;margin-top:28px;">6. שלד מזכר אשראי לדוגמה (1 עמוד)</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:16px 20px;font-family:monospace;margin:12px 0;font-size:12px;line-height:1.8;">
  <strong>מזכר אשראי — [שם החברה] | [תאריך]</strong><br><br>
  <strong>א. תמצית מנהלים:</strong><br>
  [שם החברה] מבקשת [סוג מימון] בסך [X מ' ₪] ל[תיאור הפרויקט].
  לאחר ניתוח דוחות מאוחדים לשנים [X–X] ובחינת מבנה הקבוצה, המלצתנו: [לאשר / לדחות / לאשר בתנאים].<br><br>
  <strong>ב. רקע החברה:</strong><br>
  [שם החברה] הוקמה ב-[שנה]; בעל שליטה: [שם], מחזיק [X]% מהמניות.
  פרויקטים פעילים: [X פרויקטים ב-X ערים]. פרויקטים שהושלמו: [X פרויקטים, X יחידות דיור].<br><br>
  <strong>ג. ממצאים פיננסיים:</strong><br>
  [טבלת יחסים — D/E, DSCR, שוטף, OCF/חוב — לשלוש שנים + בנצ'מרק]<br><br>
  <strong>ד. הערכת סיכונים:</strong><br>
  1. [סיכון 1 + כימות]<br>
  2. [סיכון 2 + כימות]<br>
  3. [סיכון 3 + כימות]<br><br>
  <strong>ה. נקודות בירור פתוחות:</strong><br>
  1. [מסמך/הבהרה נדרשת 1]<br>
  2. [מסמך/הבהרה נדרשת 2]<br><br>
  <strong>ו. המלצה:</strong><br>
  [לאשר / לדחות / לאשר בתנאים]<br>
  תנאים (אם רלוונטי): [תנאי 1], [תנאי 2], [תנאי 3]<br>
  [שם האנליסט] | [תאריך]
</div>
"""

M6_COMPREHENSION_INSTRUCTIONS = (
    "ענה על שאלות ההבנה הבאות לאחר קריאת חומר הקריאה. "
    "כל שאלה בוחנת הבנה של מבנה מזכר האשראי, עקרונות כתיבה מקצועית וכימות סיכונים. "
    "יש לך ניסיון אחד לכל שאלה."
)

M6_EXERCISES_INSTRUCTIONS = (
    "פתור את התרגילים הבאים. הם כוללים ניסוח מחדש של טענות חלשות לכתיבה מקצועית, "
    "בניית שלד מזכר אשראי על בסיס נתונים נתונים, וזיהוי חסרים בממו לדוגמה. "
    "יש לך שתי הזדמנויות לכל שאלה."
)

M6_SUMMARY_HTML = """\
<h2 style="color:#1a2638;border-bottom:2px solid #1976d2;padding-bottom:8px;">
  סיכום — כתיבת סיכום ניתוח
</h2>

<h3 style="color:#1a2638;">5 נקודות המפתח של המודול</h3>

<ol style="line-height:2.0;font-size:14px;">
  <li>
    <strong>מזכר אשראי חייב לענות על שאלה אחת: האם לאשר, לדחות, או לאשר בתנאים?</strong>
    התשובה צריכה להופיע בתמצית המנהלים — לא בסוף המסמך.
  </li>
  <li>
    <strong>כל טענה ללא מספר — אינה טענה.</strong>
    "מינוף גבוה" הוא דעה. "Debt/EBITDA של 6.2x לעומת 3.5x ענפי" — זה ניתוח.
  </li>
  <li>
    <strong>סעיף "נקודות בירור פתוחות" הוא סממן מקצועיות, לא חולשה.</strong>
    אנליסט שמזהה את מה שחסר — אמין יותר מאחד שמסיק מסקנות ממידע חלקי.
  </li>
  <li>
    <strong>טבלת רגישות DSCR היא כלי חובה.</strong>
    הראה מה קורה ל-DSCR ב-2–3 תרחישים שונים של פנויות / שכירות / עלויות.
    זה מה שמייצג ניתוח מקצועי לוועדת האשראי.
  </li>
  <li>
    <strong>מזכר טוב ניתן להבנה על ידי לא-מומחה תוך 5 דקות.</strong>
    אם צריך להסביר, המזכר לא מספיק ברור. כתוב מסקנות ראשה — ולאחריהן הנתונים.
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
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מזכר אשראי</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Credit Memo</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מסמך ניתוח פורמלי המגיע לוועדת האשראי</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">ממצאים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Findings</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תוצאות הניתוח הפיננסי המגובות בנתונים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">סיכון</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Risk</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">גורם שעלול לפגוע ביכולת פירעון החוב</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">המלצה</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Recommendation</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">עמדת האנליסט: לאשר, לדחות, או לאשר בתנאים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">נקודות בירור</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Open Questions</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">מסמכים או הבהרות נדרשות לפני החלטה סופית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">כימות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Quantification</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">הבעת סיכון במספרים מדידים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">תמצית מנהלים</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Executive Summary</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">סיכום קצר ופתיחת המסמך עם המסקנה הראשית</td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc;padding:8px 12px;font-weight:bold;">מגבלות</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">Covenants</td>
      <td style="border:1px solid #ccc;padding:8px 12px;">תנאים פיננסיים שהלווה מתחייב לעמוד בהם</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:24px 0;border-radius:4px;">
  <strong>גשר לבחינה הסופית:</strong><br>
  השלמתם את שישת מודולי קורס 3 — ניתוח מתקדם של יזמי נדל&quot;ן. למדתם לנתח
  מבנה קבוצתי, להשתמש ביחסים מתקדמים, לנתח פרויקט יזמי, לזהות דגלים אדומים,
  ולכתוב מזכר אשראי מקצועי.<br><br>
  הבחינה הסופית תכלול קטע מדוחות כספיים אמיתיים (מעובדים), ניתוח יחסים, זיהוי דגלים אדומים,
  ושאלה פתוחה על ניסוח המלצת אשראי. הגיעו עם הכלים שרכשתם — ובהצלחה!
</div>
"""

# ---------------------------------------------------------------------------
# MODULES DATA
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 4,
        "title_he": 'ניתוח קבוצת יזמות נדל"ן',
        "slug": "nituach-kvutsat-yazamut",
        "estimated_minutes": 50,
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
        "title_he": "דגלים אדומים",
        "slug": "dagalim-adumim",
        "estimated_minutes": 45,
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
        "title_he": "כתיבת סיכום ניתוח",
        "slug": "ktviat-sikum-nituach",
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
    help = "Seed Course 3, Modules 4, 5, and 6 — full reading, comprehension, exercises, and summary components"

    def handle(self, *args, **options) -> None:
        try:
            course = Course.objects.select_related("domain").get(course_number=3)
        except Course.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    "Course 3 not found. Run 'python manage.py seed_data' first."
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
