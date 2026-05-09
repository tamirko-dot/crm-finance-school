"""
Management command: seed_c01_content
Seeds Module 1-3 content for Course 1 (יסודות מימון נדל"ן).

Usage:
    python manage.py seed_c01_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": "ערך הזמן של הכסף",
        "slug": "erech-hazman-shel-hakesef",
        "estimated_minutes": 45,
    },
    {
        "module_number": 2,
        "title_he": "ריבית, אינפלציה והצמדה בישראל",
        "slug": "ribit-inflazia-vehatzamada",
        "estimated_minutes": 40,
    },
    {
        "module_number": 3,
        "title_he": "מדדי כדאיות השקעה",
        "slug": "madei-kdaiyut-hashkaa",
        "estimated_minutes": 50,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>מהו ערך הזמן של הכסף?</h2>

<p>
אחד העקרונות הבסיסיים ביותר במימון הוא שלשקל שבידינו היום יש ערך גבוה יותר מאשר לשקל שנקבל
בעתיד. עיקרון זה, המכונה <strong>ערך הזמן של הכסף (Time Value of Money — TVM)</strong>, עומד
בבסיס כל ניתוח פיננסי מודרני: הערכת שווי נכסים, חישוב תשואות, תמחור הלוואות ועוד.
</p>

<p>
מדוע שקל היום עדיף על שקל מחר? שלוש סיבות מרכזיות:
</p>

<ol>
  <li>
    <strong>יכולת השקעה:</strong> שקל שבידינו כבר היום יכול לעבוד — ניתן להשקיעו ולהרוויח
    עליו ריבית. שקל שיגיע רק בעוד שנה מפסיד שנה שלמה של הזדמנויות.
  </li>
  <li>
    <strong>אינפלציה:</strong> עם הזמן עולים המחירים, ולכן כוח הקנייה של שקל עתידי נמוך יותר
    משל שקל עכשווי.
  </li>
  <li>
    <strong>אי-ודאות:</strong> תשלום עתידי אינו וודאי. ככל שהתשלום מרוחק יותר בזמן, גדלה
    הסכנה שלא יתקבל בפועל.
  </li>
</ol>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה מהשטח — מימון נדל"ן:</strong><br><br>
  יזם מציע לבנק לפרוע הלוואה בסך 5,000,000 ש"ח כיום, או לחלופין לשלם 5,500,000 ש"ח בעוד
  שנה. אם הבנק יכול להשקיע את הכסף בריבית שנתית של 8%, הוא יעדיף את התשלום המיידי: שכן
  5,000,000 × 1.08 = 5,400,000 ש"ח — פחות מ-5,500,000 ש"ח, ולכן ההצעה להמתין אטרקטיבית.
  אך אם הריבית היא 12%, הבנק יפיק 5,600,000 ש"ח — ויעדיף לקבל כסף מיד.
</div>

<h3>הנחות יסוד</h3>
<p>
בחישובי TVM אנחנו עובדים עם ארבעה משתנים מרכזיים:
</p>
<ul>
  <li><strong>PV (Present Value — ערך נוכחי):</strong> שווי תזרים עתידי בזמן הנוכחי.</li>
  <li><strong>FV (Future Value — ערך עתידי):</strong> שווי השקעה בנקודת זמן עתידית.</li>
  <li><strong>r (Rate — שיעור ריבית):</strong> שיעור ריבית לתקופה.</li>
  <li><strong>n (Number of periods — מספר תקופות):</strong> מספר תקופות הזמן.</li>
</ul>
<p>
כאשר שלושה מתוך ארבעת המשתנים ידועים, ניתן לגזור את הרביעי.
</p>


<h2>ריבית פשוטה וריבית דריבית</h2>

<h3>ריבית פשוטה (Simple Interest)</h3>

<p>
<strong>ריבית פשוטה (Simple Interest)</strong> מחושבת כאחוז קבוע מהקרן המקורית בלבד, ללא
צבירת ריבית על ריבית. הנוסחה:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
FV = PV × (1 + r × n)
</div>

<p>
ריבית פשוטה נפוצה בעיקר בהלוואות קצרות-מועד ובתאריכי ערך בין בנקים. בפועל, רוב הלוואות
המשכנתא והנדל"ן מעניקות <strong>ריבית דריבית (Compound Interest)</strong>.
</p>

<h3>ריבית דריבית (Compound Interest)</h3>

<p>
בריבית דריבית, הריבית המצטברת מוסיפה עצמה לקרן ומרוויחה בעצמה ריבית בתקופות הבאות. זוהי
הנוסחה המרכזית ב-TVM:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
FV = PV × (1 + r)^n
</div>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה מחושבת — ריבית פשוטה מול ריבית דריבית:</strong><br><br>
  השקעה של 100,000 ש"ח בריבית שנתית של 6% לתקופה של 5 שנים:<br><br>
  <em>ריבית פשוטה:</em> FV = 100,000 × (1 + 0.06 × 5) = 100,000 × 1.30 = <strong>130,000 ש"ח</strong><br>
  <em>ריבית דריבית:</em> FV = 100,000 × (1.06)^5 = 100,000 × 1.3382 = <strong>133,823 ש"ח</strong><br><br>
  ההפרש של 3,823 ש"ח נוצר כי ב"ריבית דריבית" הריבית מכל שנה מרוויחה ריבית בשנים הבאות.
  ככל שהתקופה ארוכה יותר, ההפרש גדל בצורה דרמטית.
</div>

<h3>עוצמת הדריבית לאורך זמן</h3>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">שנים</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ריבית פשוטה (6%)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ריבית דריבית (6%)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הפרש</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">106,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">106,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">0</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">130,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">133,823</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3,823</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">160,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">179,085</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">19,085</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">20</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">220,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">320,714</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">100,714</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">30</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">280,000</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">574,349</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">294,349</td>
    </tr>
  </tbody>
</table>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט:</strong><br>
  לעולם אל תשתמש בנוסחת ריבית פשוטה לחישוב ערך נוכחי או עתידי של הלוואות נדל"ן.
  כל הלוואת משכנתא מחושבת בשיטת "שפיצר" — ריבית דריבית חודשית. שימוש בנוסחה הפשוטה
  יניב תוצאות שגויות באופן מהותי.
</div>


<h2>ריבית נומינלית, אפקטיבית ורציפה</h2>

<h3>ריבית נומינלית (Nominal Rate)</h3>

<p>
<strong>ריבית נומינלית (Nominal Interest Rate)</strong> היא שיעור הריבית הרשמי שמפורסם —
לדוגמה, "ריבית שנתית של 5%". אולם, שיעור זה אינו מביא בחשבון את תדירות ההרכבה (החישוב).
אם הבנק מחשב ריבית חודשית, הריבית החודשית היא 5% ÷ 12 = 0.4167%, אך האפקט השנתי גדול יותר
בשל ה"ריבית על הריבית" הבין-חודשית.
</p>

<h3>ריבית אפקטיבית (Effective Annual Rate — EAR)</h3>

<p>
<strong>ריבית אפקטיבית (EAR — Effective Annual Rate)</strong> מבטאת את התשואה האמיתית השנתית
לאחר הבאת תדירות ההרכבה בחשבון. הנוסחה:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
EAR = (1 + r_nom / m)^m − 1
</div>

<p>
כאשר <em>r_nom</em> היא הריבית הנומינלית ו-<em>m</em> הוא מספר תקופות ההרכבה בשנה.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — משכנתא ישראלית:</strong><br><br>
  ריבית פריים נומינלית: 7.25% לשנה (חישוב חודשי).<br>
  m = 12 (חודשים בשנה)<br>
  EAR = (1 + 0.0725/12)^12 − 1 = (1.006042)^12 − 1 = 1.07499 − 1 = <strong>7.499%</strong><br><br>
  ההפרש בין 7.25% (נומינלי) לבין 7.499% (אפקטיבי) קטן, אך על הלוואה של 2,000,000 ש"ח
  לתקופה של 25 שנה — ההפרש עולה לעשרות אלפי שקלים.
</div>

<h3>ריבית נקייה ופריים בישראל</h3>

<p>
בישראל, ריבית <strong>הפריים (Prime Rate)</strong> היא ריבית הבנקים ללקוחות הקמעוניים. על-פי
מוסכמה יציבה, <strong>פריים = ריבית בנק ישראל + 1.5%</strong>. ריבית בנק ישראל נקבעת
על-ידי הוועדה המוניטרית, המתכנסת כ-8 פעמים בשנה. נכון לתחילת 2025, לאחר מחזור העלאות
הריבית שהחל ב-2022, ריבית בנק ישראל עומדת בטווח של 4.5%–4.75%, ובהתאם הפריים עומד
על 6.0%–6.25%.
</p>

<h3>ריבית רציפה (Continuous Compounding)</h3>

<p>
<strong>ריבית רציפה (Continuous Compounding)</strong> היא הגבול המתמטי כאשר מספר תקופות
ההרכבה שואף לאינסוף. משמשת בעיקר בתאוריה פיננסית ובתמחור אופציות (מודל Black-Scholes):
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
FV = PV × e^(r × t)
</div>

<p>
כאשר <em>e</em> הוא בסיס הלוגריתם הטבעי (≈ 2.71828).
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">תדירות הרכבה</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">m</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">EAR לריבית 10%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שנתית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10.000%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חציונית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">2</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10.250%</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רבעונית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">4</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10.381%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חודשית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">12</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10.471%</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">יומית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">365</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10.516%</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רציפה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">∞</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10.517%</td>
    </tr>
  </tbody>
</table>


<h2>ערך נוכחי של תזרים לא אחיד</h2>

<p>
בפועל, פרויקטי נדל"ן מניבים תזרים מזומנים שאינו אחיד: שכירות משתנה, עלויות שיפוץ
חד-פעמיות, הכנסות מיוחדות, ושחרור הון עצמי במימוש. חישוב <strong>הערך הנוכחי של תזרים
לא אחיד (Uneven Cash Flow PV)</strong> מבוצע על-ידי היוון כל תזרים בנפרד ואז סיכום:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
PV = CF₁/(1+r)¹ + CF₂/(1+r)² + CF₃/(1+r)³ + ... + CFₙ/(1+r)ⁿ
</div>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה מלאה — נכס מסחרי בתל-אביב:</strong><br><br>
  שיעור היוון: 8% לשנה. תזרים המזומנים הצפוי (בש"ח):<br><br>
  שנה 1: 180,000 (שכירות נמוכה — תקופת אכלוס)<br>
  שנה 2: 320,000<br>
  שנה 3: 340,000<br>
  שנה 4: 360,000<br>
  שנה 5: 4,200,000 (שכירות + מימוש הנכס)<br><br>
  חישוב:<br>
  PV₁ = 180,000 / 1.08¹ = 166,667<br>
  PV₂ = 320,000 / 1.08² = 274,057<br>
  PV₃ = 340,000 / 1.08³ = 269,919<br>
  PV₄ = 360,000 / 1.08⁴ = 264,609<br>
  PV₅ = 4,200,000 / 1.08⁵ = 2,857,875<br>
  <strong>PV כולל = 3,833,127 ש"ח</strong>
</div>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — שיח עם אנליסט בכיר:</strong><br><br>
  "כשאנחנו מנתחים בקשת אשראי לנכס מסחרי, לעולם אין לנו תזרים אחיד — תמיד יש שנה ראשונה
  של אכלוס, חידוש חוזים בשנה 3, ואולי שיפוץ גדול בשנה 5. לכן אנחנו תמיד בונים תחזית
  שנה אחר שנה ומהוונים כל תזרים בנפרד. מי שמשתמש בנוסחת אנואיטי בלבד לנכס מניב
  — כנראה לא מסתכל על הנכס הנכון."
</div>

<h3>כלל הזהב: כיוון התזרים</h3>
<p>
בהיוון תזרים לא אחיד, חשוב לשמור על קונבנציה עקבית:
<strong>תזרים נכנס (הכנסה) — חיובי; תזרים יוצא (השקעה, הוצאה) — שלילי.</strong>
בדרך זו, ניתן להשתמש ישירות בפונקציית NPV של Excel.
</p>


<h2>אנואיטי ופרפטואיטי</h2>

<h3>אנואיטי (Annuity)</h3>

<p>
<strong>אנואיטי (Annuity)</strong> הוא סדרה של תשלומים שווים ואחידים המבוצעים במרווחי
זמן שווים. לדוגמה: תשלומי משכנתא קבועים (שיטת שפיצר), דמי שכירות קבועים לאורך חוזה רב-שנתי.
</p>

<p>
<strong>ערך נוכחי של אנואיטי (PV Annuity):</strong>
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
PV = PMT × [1 − (1+r)^(−n)] / r
</div>

<p>
<strong>ערך עתידי של אנואיטי (FV Annuity):</strong>
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
FV = PMT × [(1+r)^n − 1] / r
</div>

<p>
<strong>תשלום חודשי של אנואיטי (PMT):</strong>
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
PMT = PV × r / [1 − (1+r)^(−n)]
</div>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — חישוב תשלום משכנתא:</strong><br><br>
  משכנתא של 1,500,000 ש"ח. ריבית שנתית: 5.5% (= 0.4583% לחודש). תקופה: 25 שנה (300 חודשים).<br><br>
  PMT = 1,500,000 × 0.004583 / [1 − (1.004583)^(−300)]<br>
  PMT = 6,875 / [1 − 0.2536]<br>
  PMT = 6,875 / 0.7464<br>
  <strong>PMT ≈ 9,212 ש"ח לחודש</strong><br><br>
  לאורך 25 שנה, הלווה ישלם סך 25 × 12 × 9,212 = 2,763,600 ש"ח — כלומר 1,263,600 ש"ח
  ריבית על קרן של 1,500,000 ש"ח.
</div>

<h3>אנואיטי מאוחר (Annuity Due)</h3>

<p>
באנואיטי רגיל (ordinary annuity), התשלום מבוצע בסוף כל תקופה. <strong>אנואיטי מאוחר
(Annuity Due)</strong> מניח תשלום בתחילת כל תקופה. ערכו הנוכחי גבוה ב-(1+r) מאשר
האנואיטי הרגיל — כי כל תשלום מגיע "מוקדם יותר" ולכן שוה יותר.
</p>

<h3>פרפטואיטי (Perpetuity)</h3>

<p>
<strong>פרפטואיטי (Perpetuity)</strong> הוא אנואיטי אינסופי — סדרת תשלומים שווים לנצח.
נוסחת הערך הנוכחי מפשטת לצורה אלגנטית ביותר:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
PV = C / r
</div>

<p>
כאשר <em>C</em> הוא התשלום השנתי הקבוע ו-<em>r</em> שיעור ההיוון.
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>עיקרון — שימוש בפרפטואיטי להערכת נדל"ן מניב:</strong><br><br>
  כאשר נכס מניב הכנסה שנתית נקייה קבועה של 600,000 ש"ח, ושיעור ההיוון בשוק הוא 6%
  (<em>cap rate</em>), שווי הנכס הוא:<br>
  PV = 600,000 / 0.06 = <strong>10,000,000 ש"ח</strong><br><br>
  זוהי בדיוק השיטה שבה מוערכים נכסים מסחריים — NOI חלקי ה-Cap Rate. כלומר, נוסחת
  הפרפטואיטי היא הבסיס התיאורטי להערכת שווי נכס מניב.
</div>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — Cap Rate בשוק הישראלי 2025-2026:</strong><br><br>
  נכסי משרדים בתל-אביב: 5.5%–7.5%<br>
  מרכזי מסחר איזוריים: 7%–9%<br>
  מחסנים ולוגיסטיקה: 6%–8%<br>
  מגורים (שכירות ארוכת טווח): 3%–4.5%<br><br>
  Cap Rate נמוך יותר = שווי גבוה יותר לאותה הכנסה. בשנים האחרונות, עלייה בריבית בנק
  ישראל הובילה ללחץ כלפי מעלה על ה-Cap Rate ולהתאמת שווי נכסים כלפי מטה.
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום — ערך הזמן של הכסף</h2>

<h3>חמש נקודות המפתח של המודול</h3>
<ol>
  <li>
    <strong>שקל היום שווה יותר:</strong> עקב יכולת השקעה, אינפלציה ואי-ודאות, לכסף
    שזמין היום יש ערך גדול יותר מאשר לכסף זהה שיגיע בעתיד. זהו יסוד כל ניתוח פיננסי.
  </li>
  <li>
    <strong>ריבית דריבית עדיפה על פשוטה:</strong> בחישוב הלוואות ונדל"ן תמיד מדובר
    בריבית דריבית. הנוסחה הבסיסית היא FV = PV × (1+r)^n. ריבית פשוטה שגויה לניתוחים
    אלה.
  </li>
  <li>
    <strong>ריבית נומינלית אינה הריבית האמיתית:</strong> הריבית האפקטיבית (EAR) גבוהה
    מהנומינלית בשל תדירות ההרכבה. בישראל, ריבית פריים מחושבת חודשית — יש להמיר לאפקטיבית
    לפני השוואות.
  </li>
  <li>
    <strong>תזרים לא אחיד — היוון נפרד:</strong> כאשר תזרים המזומנים אינו קבוע לאורך
    כל התקופה, יש להוון כל תשלום בנפרד ולסכם. אין קיצורי דרך.
  </li>
  <li>
    <strong>פרפטואיטי = ה-Cap Rate:</strong> נוסחת הפרפטואיטי (PV = C/r) היא הבסיס
    התיאורטי לשיטת ה-Cap Rate בהערכת נדל"ן מניב. הבנת הנוסחה מסבירה מדוע עלייה
    בריבית מוריד שווי נכסים.
  </li>
</ol>

<h3>מילון מונחים</h3>
<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מונח עברי</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">English Term</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ערך זמן של הכסף</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Time Value of Money (TVM)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">העיקרון שכסף זמין כיום שווה יותר מכסף זהה בעתיד</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ערך נוכחי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Present Value (PV)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שווי תזרים עתידי בהיוון לזמן הנוכחי</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ערך עתידי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Future Value (FV)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שווי השקעה בנקודת זמן עתידית לאחר הרכבת ריבית</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית נומינלית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Nominal Interest Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הריבית השנתית הרשמית לפני תיקון תדירות הרכבה</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית אפקטיבית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Effective Annual Rate (EAR)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הריבית השנתית האמיתית בהתחשב בתדירות ההרכבה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אנואיטי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Annuity</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סדרת תשלומים שווים באינטרוולים קבועים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פרפטואיטי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Perpetuity</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אנואיטי אינסופי; PV = C/r; בסיס לשיטת Cap Rate</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">היוון</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Discounting</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">המרת ערך עתידי לערך נוכחי על-ידי שיעור ריבית</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
המודול הבא — <em>ריבית, אינפלציה והצמדה בישראל</em> — יבנה ישירות על הכלים שלמדנו כאן.
נראה כיצד ריבית בנק ישראל ומדד המחירים לצרכן (CPI) משפיעים על שיעורי ההיוון שבהם
אנו משתמשים בחישובי TVM. נבחן גם את ההבדל בין הלוואה צמודת מדד לבין הלוואה שאינה
צמודה — הבדל שמשנה מהותית את תזרים המזומנים שצריך להוון.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>ריבית בנק ישראל וריבית פריים</h2>

<p>
השחקן המרכזי בשוק הריבית הישראלי הוא <strong>בנק ישראל (Bank of Israel)</strong> — הבנק
המרכזי של המדינה. הבנק קובע את <strong>ריבית בנק ישראל (BoI Rate)</strong> — הריבית שבה
הוא מלווה כסף לבנקים המסחריים ומקבל פיקדונות מהם. שינויים בריבית בנק ישראל מגלגלים
ישירות לכל שוק האשראי במשק.
</p>

<h3>מנגנון קביעת הריבית</h3>

<p>
הוועדה המוניטרית של בנק ישראל מתכנסת 8 פעמים בשנה ומחליטה על שיעור הריבית בהתבסס על:
</p>
<ul>
  <li>שיעור האינפלציה הנוכחי ביחס ליעד (1%–3% לשנה)</li>
  <li>קצב הצמיחה הכלכלית ורמת האבטלה</li>
  <li>שיעור השקל ביחס למטבעות חוץ</li>
  <li>מגמות בשוק הנדל"ן וסיכוני יציבות פיננסית</li>
</ul>

<h3>ריבית פריים (Prime Rate)</h3>

<p>
<strong>ריבית פריים (Prime Rate)</strong> היא הריבית הבסיסית שבה הבנקים המסחריים מלווים
ללקוחות הקמעוניים שלהם. על-פי מסורת עסקית ויציבה:
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל יסוד — ריבית פריים:</strong><br><br>
  ריבית פריים = ריבית בנק ישראל + 1.5%<br><br>
  מרווח של 1.5% זה משקף את עלויות הפעילות של הבנקים ורווח מינימלי. הוא נשמר כמעט
  ללא שינוי לאורך עשורים, גם כאשר ריבית בנק ישראל עצמה משתנה.
</div>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">תאריך</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ריבית בנק ישראל</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ריבית פריים</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הקשר</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ינואר 2022</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">0.10%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">1.60%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיא מדיניות מרחיבה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ינואר 2023</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">3.75%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">5.25%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מחזור העלאות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ינואר 2024</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">4.75%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">6.25%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיא מחזור עליות</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ינואר 2025</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">4.50%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">6.00%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">התחלת ירידה מתונה</td>
    </tr>
  </tbody>
</table>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — השפעת שינוי ריבית פריים על הלוואות נדל"ן:</strong><br><br>
  משכנתא בריבית פריים מינוס 0.9% לסך 2,000,000 ש"ח ל-20 שנה.<br>
  בינואר 2022: ריבית = 1.6% − 0.9% = 0.7% → תשלום חודשי ≈ 9,600 ש"ח<br>
  בינואר 2024: ריבית = 6.25% − 0.9% = 5.35% → תשלום חודשי ≈ 13,500 ש"ח<br><br>
  בתוך שנתיים, אותו לווה שילם 3,900 ש"ח יותר בחודש — עלייה של 40%. זהו הסיכון
  המרכזי של ריבית משתנה צמודת פריים.
</div>


<h2>אינפלציה ומדד המחירים לצרכן</h2>

<h3>מה זה CPI?</h3>

<p>
<strong>מדד המחירים לצרכן (CPI — Consumer Price Index)</strong> הוא מדד המפורסם מדי חודש
על-ידי הלשכה המרכזית לסטטיסטיקה (למ"ס). הוא עוקב אחר השינוי במחירי "סל" קבוע של מוצרים
ושירותים שמשפחה ממוצעת בישראל צורכת — מזון, דיור, תחבורה, חינוך, בריאות ועוד.
</p>

<p>
יעד האינפלציה של בנק ישראל: <strong>1%–3% לשנה</strong>. כאשר אינפלציה חורגת מיעד זה,
הבנק נוטה להעלות ריבית. אינפלציה מתחת ליעד — הבנק נוטה להוריד ריבית.
</p>

<h3>משוואת פישר (Fisher Equation)</h3>

<p>
הכלכלן <strong>אירווינג פישר (Irving Fisher)</strong> פיתח את הקשר הכלכלי בין ריבית נומינלית,
ריבית ריאלית ואינפלציה:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
(1 + r_real) = (1 + r_nominal) / (1 + inflation)
</div>

<p>
גרסה מקורבת פשוטה יותר (מדויקת כאשר הריביות נמוכות):
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
r_real ≈ r_nominal − inflation
</div>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — ריבית ריאלית בישראל 2024:</strong><br><br>
  ריבית פריים נומינלית: 6.25%<br>
  אינפלציה שנתית: 2.8%<br><br>
  גרסה מדויקת: r_real = (1.0625 / 1.028) − 1 = 1.0335 − 1 = <strong>3.35%</strong><br>
  גרסה מקורבת: r_real ≈ 6.25% − 2.8% = <strong>3.45%</strong><br><br>
  ההפרש קטן, אך בריביות גבוהות (כמו 2023) ההפרש גדל ומוצדק להשתמש בנוסחה המדויקת.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — אינפלציה ותשואת נדל"ן:</strong><br><br>
  לעתים יזמים טוענים שנדל"ן "מגן מפני אינפלציה". זה נכון רק חלקית: שכירות ומחירי נכסים
  עולים עם האינפלציה בטווח הארוך, אך לא בהכרח בכל שנה. בשנים שבהן ריבית עולה מהר
  (כמו 2022-2023), עלות המימון עלתה מהר יותר מהשכירות — ה"מגן" האינפלציוני לא פעל.
</div>


<h2>הלוואות צמודות מדד מול לא צמודות</h2>

<h3>הלוואה צמודת מדד (CPI-Linked Loan)</h3>

<p>
<strong>הלוואה צמודת מדד (CPI-Linked Loan)</strong> היא הלוואה שבה הקרן (ולעתים גם הריבית)
צמודים לשינויים ב-CPI. מדי חודש, יתרת ההלוואה מעודכנת בשיעור עליית המדד. בשל כך, הלווה
משלם ריבית ריאלית נמוכה יחסית — אך חשוף לסיכון שהקרן תגדל בתקופות של אינפלציה גבוהה.
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — הלוואה צמודת מדד:</strong><br><br>
  הלוואה של 1,000,000 ש"ח. ריבית ריאלית: 2.5%. אינפלציה בשנה הראשונה: 4%.<br><br>
  יתרת קרן בסוף שנה 1: 1,000,000 × 1.04 = <strong>1,040,000 ש"ח</strong><br>
  ריבית שנה 1: 1,000,000 × 0.025 = 25,000 ש"ח<br>
  תוספת הצמדה שנה 1: 40,000 ש"ח<br>
  <strong>עלות אפקטיבית שנה 1: 65,000 ש"ח = 6.5% על ההלוואה</strong><br><br>
  לעומת: הלוואה לא צמודה בריבית 6.5% — אותו תשלום בשנה 1, אך ללא גידול בקרן.
</div>

<h3>הלוואה שאינה צמודה (Unlinked / Nominal Loan)</h3>

<p>
<strong>הלוואה שאינה צמודה</strong> נושאת ריבית נומינלית קבועה (או משתנה לפי פריים).
הקרן אינה גדלה עם האינפלציה. בתקופות של אינפלציה גבוהה, הלווה נהנה: הוא משלם
"בשקלים קלים" — שקלים שכוח הקנייה שלהם ירד.
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מאפיין</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הלוואה צמודת מדד</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הלוואה שאינה צמודה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית רשומה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נמוכה (ריאלית)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גבוהה (נומינלית)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון אינפלציה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אצל הלווה (קרן גדלה)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אצל המלווה (ריאלית יורדת)</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תשלום חודשי ראשוני</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נמוך</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גבוה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בתרחיש אינפלציה גבוהה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">חיסרון — יתרה גדלה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">יתרון — ריאלית נשחקת</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מתאים ל</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אינפלציה נמוכה/יציבה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אינפלציה גבוהה/לא בטוחה</td>
    </tr>
  </tbody>
</table>


<h2>ריבית קבועה מול ריבית משתנה</h2>

<h3>ריבית קבועה (Fixed Rate)</h3>

<p>
<strong>ריבית קבועה (Fixed Rate)</strong> נקבעת לכל אורך תקופת ההלוואה ואינה משתנה בעקבות
שינויים בשוק. הלווה יודע מראש בדיוק כמה ישלם בכל חודש. המלווה לוקח על עצמו את
<strong>סיכון הריבית (Interest Rate Risk)</strong> — אם הריבית בשוק עולה, הוא "מפסיד"
כי קיבע בריבית נמוכה.
</p>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מתי להמליץ על ריבית קבועה?</strong><br><br>
  כאשר הלווה זקוק לוודאות תזרימית — למשל יזם שמימן פרויקט עם הכנסות צפויות קבועות.
  כאשר שיעורי הריבית בשוק נמוכים היסטורית — נעילה בריבית נמוכה עשויה להיות כדאית.
  כאשר תחזית בנק ישראל מעידה על עליית ריבית עתידית.
</div>

<h3>ריבית משתנה (Variable / Floating Rate)</h3>

<p>
<strong>ריבית משתנה (Variable Rate)</strong> מתעדכנת מעת לעת לפי מדד ייחוס — בדרך כלל
ריבית פריים. כאשר פריים עולה, עולה גם תשלום ההחזר. כאשר פריים יורד — ההחזר יורד.
הלווה נושא את סיכון הריבית.
</p>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — ניתוח כושר החזר:</strong><br><br>
  בנק ישראל (הוראה 329 ותיקוניה) מחייב בנקים לבדוק את כושר ההחזר של לווה גם בתרחיש
  של עלייה של 2%–3% בריבית — ה"מבחן הלחץ" (Stress Test). כאנליסט, עליך לכלול
  תרחיש כזה בכל ניתוח הלוואה עם מרכיב ריבית משתנה.
</div>

<h3>מבנה מומלץ — "תמהיל משכנתא"</h3>

<p>
בנק ישראל ממליץ ולעתים מחייב שמרכיב ריבית משתנה בהלוואת משכנתא לא יעלה על שני שלישים
מסך ההלוואה. בפועל, רוב הלוואות הנדל"ן המסחריות משלבות:
</p>
<ul>
  <li>חלק בריבית פריים (משתנה)</li>
  <li>חלק בריבית קבועה לא צמודה</li>
  <li>חלק בריבית קבועה צמודת מדד</li>
</ul>
<p>
שילוב זה מפזר את הסיכון בין שינויי ריבית ושינויי אינפלציה.
</p>


<h2>ריבית ראשית מול סוף תקופה</h2>

<h3>השפעת תזמון התשלום</h3>

<p>
<strong>ריבית ראשית תקופה (Annuity Due)</strong> מניחה שתשלומים מבוצעים <em>בתחילת</em>
כל תקופה. <strong>ריבית סוף תקופה (Ordinary Annuity)</strong> מניחה שתשלומים מבוצעים
<em>בסוף</em> כל תקופה. ברוב משכנתאות ישראל, התשלום מבוצע בתחילת החודש (ראשית תקופה).
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
PV (Annuity Due) = PV (Ordinary Annuity) × (1 + r)
</div>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — שכירות לעומת משכנתא:</strong><br><br>
  חוזה שכירות: 5,000 ש"ח לחודש, 12 חודשים, ריבית 6% לשנה (= 0.5% לחודש).<br><br>
  <em>Ordinary Annuity (תשלום בסוף חודש):</em><br>
  PV = 5,000 × [1 − (1.005)^(−12)] / 0.005 = 5,000 × 11.619 = 58,095 ש"ח<br><br>
  <em>Annuity Due (תשלום בתחילת חודש):</em><br>
  PV = 58,095 × 1.005 = <strong>58,385 ש"ח</strong><br><br>
  ההפרש של 290 ש"ח משקף את העובדה שתשלום מוקדם יותר שווה יותר.
</div>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — חוזי שכירות מסחריים:</strong><br><br>
  חוזי שכירות של נכסים מסחריים גדולים (קניונים, משרדים) לרוב קובעים תשלום ראשוני
  (ראשית חודש) ועדכון שנתי לפי CPI. כאשר מניחים לחישוב NPV של פרויקט, חשוב לדעת
  האם לדגמן את השכירות כ-Ordinary Annuity או Annuity Due — ההפרש יכול להגיע
  למאות אלפי שקלים בפרויקטים גדולים.
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום — ריבית, אינפלציה והצמדה בישראל</h2>

<h3>חמש נקודות המפתח של המודול</h3>
<ol>
  <li>
    <strong>פריים = BoI + 1.5%:</strong> ריבית הפריים הישראלית נגזרת ישירות מריבית
    בנק ישראל. שינוי בהחלטה מוניטרית מגולגל לכל הלוואות הנדל"ן בתוך ימים.
    מעקב אחר ישיבות הוועדה המוניטרית הוא חובה לכל אנליסט.
  </li>
  <li>
    <strong>ריאלי ≠ נומינלי:</strong> משוואת פישר מפרידה את מרכיב האינפלציה מהריבית
    הנומינלית. בניתוח הלוואות ובפרויקטים ריאליים, תמיד השתמש בריבית ריאלית להיוון
    תזרים ריאלי, ובריבית נומינלית להיוון תזרים נומינלי — אסור לערבב.
  </li>
  <li>
    <strong>הצמדה — הסיכון בשני הכיוונים:</strong> הלוואות צמודות מדד מגנות על המלווה
    מפני אינפלציה, אך מגדילות את קרן החוב של הלווה. בניתוח אשראי, חשב תמיד את
    יתרת הקרן הצפויה בסוף תקופה תחת תרחיש אינפלציה גבוהה.
  </li>
  <li>
    <strong>ריבית קבועה לעומת משתנה — תלוי בסיכון:</strong> ריבית קבועה מגינה על
    הלווה מפני עליות ריבית, ריבית משתנה נמוכה יותר בתחילה. ניתוח "מבחן לחץ" ריבית
    (+2%–3%) הוא דרישת בנק ישראל ועיקרון מקצועי מרכזי.
  </li>
  <li>
    <strong>תזמון תשלום משנה:</strong> Ordinary Annuity לעומת Annuity Due — ההפרש
    של (1+r) פעמים בערך הנוכחי עשוי להגיע לסכומים מהותיים בפרויקטים גדולים.
    יש לבדוק תמיד את תנאי חוזה השכירות.
  </li>
</ol>

<h3>מילון מונחים</h3>
<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מונח עברי</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">English Term</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית פריים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Prime Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית בנק ישראל + 1.5%; בסיס לרוב הלוואות המשכנתא</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מדד המחירים לצרכן</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Consumer Price Index (CPI)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מדד אינפלציה חודשי של למ"ס; בסיס להצמדת הלוואות</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית ריאלית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Real Interest Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית נומינלית בניכוי אינפלציה; נמדדת לפי משוואת פישר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">הצמדת מדד</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">CPI Linkage (Indexation)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עדכון יתרת הלוואה לפי שינוי CPI; מגן על המלווה מאינפלציה</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית קבועה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Fixed Interest Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית שאינה משתנה לאורך תקופת ההלוואה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית משתנה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Variable / Floating Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ריבית המתעדכנת לפי מדד ייחוס (פריים); חשיפת לווה לסיכון ריבית</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מבחן לחץ ריבית</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Interest Rate Stress Test</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בחינת כושר החזר בתרחיש עלייה של 2%–3% בריבית; דרישת בנק ישראל</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
במודול הבא — <em>מדדי כדאיות השקעה</em> — נרכיב את כל הכלים שלמדנו: היוון תזרים,
ריבית אפקטיבית, ומרכיבי הסיכון — לתוך שני המדדים הגדולים שבהם משתמשים אנליסטי
אשראי ומשקיעים בנדל"ן: NPV ו-IRR. נראה גם מדוע לפעמים IRR מטעה, ומהו ה-MIRR
שמתקן את הכשל.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>NPV — שווי נוכחי נקי</h2>

<p>
<strong>שווי נוכחי נקי (NPV — Net Present Value)</strong> הוא המדד הפיננסי החשוב ביותר
להערכת כדאיות השקעה. הוא מסכם — בשקל אחד — את הערך שפרויקט מוסיף למשקיע, לאחר
שחשבנו את עלות ההזדמנות של הכסף. NPV חיובי פירושו שהפרויקט יוצר ערך. NPV שלילי
פירושו שהפרויקט מפחית ערך.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
NPV = Σ [CF_t / (1 + r)^t] − Investment₀
</div>

<p>
כאשר:
</p>
<ul>
  <li><strong>CF_t:</strong> תזרים מזומנים בתקופה t</li>
  <li><strong>r:</strong> שיעור ההיוון (שיעור התשואה הנדרש)</li>
  <li><strong>t:</strong> מספר התקופה (1, 2, ..., n)</li>
  <li><strong>Investment₀:</strong> ההשקעה הראשונית (בתקופה 0, לרוב שלילית)</li>
</ul>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל ההחלטה של NPV:</strong><br><br>
  NPV &gt; 0: הפרויקט מוסיף ערך — כדאי להשקיע<br>
  NPV = 0: הפרויקט מכסה בדיוק את עלות ההזדמנות — אדיש<br>
  NPV &lt; 0: הפרויקט מפחית ערך — אין להשקיע<br><br>
  בניתוח אשראי נדל"ן, NPV חיובי מחזק את ההנחה שהפרויקט יפרע את החוב ויישאר עם ערך
  עודף. NPV שלילי מהווה דגל אדום שדורש בחינה מחמירה של הנחות הפרויקט.
</div>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה מלאה — פרויקט נדל"ן בחיפה:</strong><br><br>
  השקעה ראשונית: −8,000,000 ש"ח. שיעור היוון: 10%.<br>
  תזרים צפוי (ש"ח):<br>
  שנה 1: 1,500,000 | שנה 2: 1,800,000 | שנה 3: 2,000,000<br>
  שנה 4: 2,200,000 | שנה 5: 3,500,000 (כולל מכירה)<br><br>
  חישוב PV לכל שנה:<br>
  PV₁ = 1,500,000 / 1.10¹ = 1,363,636<br>
  PV₂ = 1,800,000 / 1.10² = 1,487,603<br>
  PV₃ = 2,000,000 / 1.10³ = 1,502,630<br>
  PV₄ = 2,200,000 / 1.10⁴ = 1,502,630<br>
  PV₅ = 3,500,000 / 1.10⁵ = 2,173,575<br>
  סכום PV = 8,030,074<br><br>
  <strong>NPV = 8,030,074 − 8,000,000 = +30,074 ש"ח</strong><br><br>
  NPV חיובי קטן מאוד — הפרויקט כדאי בקושי. שינוי קטן בהנחות (ירידה של 1% בתזרים,
  עלייה של 0.5% בשיעור ההיוון) עלול להפוך את ה-NPV לשלילי. אנליסט יסמן את הפרויקט
  כ"בסף".
</div>


<h2>בחירת שיעור ההיוון</h2>

<p>
הבחירה של שיעור ההיוון (r) היא ההחלטה הקריטית ביותר בחישוב NPV. שיעור גבוה מדי יפסל
פרויקטים כדאיים; שיעור נמוך מדי יאשר פרויקטים גרועים.
</p>

<h3>גישה 1 — ריבית חסרת סיכון + פרמיית סיכון</h3>

<p>
<strong>ריבית חסרת סיכון (Risk-Free Rate)</strong>: בישראל, אג"ח ממשלתי ל-10 שנים (שחר).
נכון ל-2025, תשואה של כ-4.5%–5.0% לשנה.
</p>
<p>
<strong>פרמיית סיכון (Risk Premium)</strong>: תוספת הנדרשת בגין הסיכונים הספציפיים של
הפרויקט — סיכון שוק, סיכון ביצוע, סיכון שוכר. בנדל"ן מסחרי בישראל: בדרך כלל 3%–6%.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
r = r_f + Risk Premium
</div>

<h3>גישה 2 — WACC (Weighted Average Cost of Capital)</h3>

<p>
<strong>WACC — עלות ממוצעת משוקללת של הון (Weighted Average Cost of Capital)</strong>
משמשת כשיעור ההיוון לפרויקטים הממומנים בשילוב של הון עצמי וחוב:
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
WACC = (E/V) × r_e + (D/V) × r_d × (1 − Tax)
</div>

<p>
כאשר E = הון עצמי, D = חוב, V = E + D, r_e = עלות הון עצמי, r_d = ריבית החוב,
Tax = שיעור מס חברות (23% בישראל).
</p>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — חישוב WACC לפרויקט נדל"ן:</strong><br><br>
  מימון: 30% הון עצמי (עלות 14%), 70% חוב (ריבית 6.5%), מס חברות 23%.<br><br>
  WACC = (0.30 × 14%) + (0.70 × 6.5% × (1 − 0.23))<br>
  WACC = 4.20% + (0.70 × 5.005%)<br>
  WACC = 4.20% + 3.50%<br>
  <strong>WACC = 7.70%</strong><br><br>
  שיעור היוון זה ישמש לחישוב NPV של הפרויקט. שימו לב: החוב "זול" יותר לאחר מגן המס.
</div>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">סוג פרויקט נדל"ן</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">שיעור היוון טיפוסי (2025)</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הנמקה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מגורים להשכרה, מרכז</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">6%–7%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון נמוך, ביקוש גבוה</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">משרדים, תל-אביב</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">7%–9%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תנודות בביקוש, Work-From-Home</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מסחר (קניון)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">8%–10%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תחרות מסחר אלקטרוני</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לוגיסטיקה ומחסנים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">7%–8%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ביקוש גבוה, e-commerce</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פרויקט יזמי (בנייה + מכירה)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">12%–18%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון ביצוע גבוה, לא מניב</td>
    </tr>
  </tbody>
</table>


<h2>IRR — שיעור תשואה פנימי</h2>

<p>
<strong>שיעור תשואה פנימי (IRR — Internal Rate of Return)</strong> הוא שיעור ההיוון שבו
NPV של הפרויקט שווה לאפס — כלומר, שיעור התשואה שבו ההשקעה "מחזירה את עצמה" בדיוק.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
NPV = 0 = Σ [CF_t / (1 + IRR)^t] − Investment₀
</div>

<div style="background:#f3e5f5;border-right:5px solid #7b1fa2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל ההחלטה של IRR:</strong><br><br>
  IRR &gt; שיעור הדחייה (Hurdle Rate): הפרויקט כדאי — IRR עולה על עלות ההון<br>
  IRR &lt; שיעור הדחייה: הפרויקט אינו כדאי<br>
  IRR = שיעור הדחייה: נקודת האדישות<br><br>
  שיעור הדחייה (Hurdle Rate) הוא ה-WACC, או מינימום תשואה שקבעה הנהלת החברה.
</div>

<p>
IRR אינו בעל נוסחה סגורה — חישובו מחייב גישה איטרטיבית (ניסוי-וטעייה). ב-Excel,
הפונקציה <strong>=IRR(values, guess)</strong> מחשבת את ה-IRR אוטומטית, כאשר:
</p>
<ul>
  <li><em>values</em>: טווח תזרים המזומנים (כולל ההשקעה הראשונית כמספר שלילי)</li>
  <li><em>guess</em>: ניחוש ראשוני (לרוב 0.1 = 10%)</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — חישוב IRR לפרויקט נדל"ן:</strong><br><br>
  השקעה: −5,000,000 ש"ח<br>
  תזרים: שנה 1: 800,000 | שנה 2: 1,000,000 | שנה 3: 1,200,000 | שנה 4: 3,500,000<br><br>
  ניסיון IRR = 15%:<br>
  NPV = 800,000/1.15 + 1,000,000/1.15² + 1,200,000/1.15³ + 3,500,000/1.15⁴ − 5,000,000<br>
  NPV = 695,652 + 756,144 + 788,593 + 2,001,749 − 5,000,000 = +242,138 (חיובי → IRR &gt; 15%)<br><br>
  ניסיון IRR = 18%:<br>
  NPV ≈ −82,000 (שלילי → IRR &lt; 18%)<br><br>
  <strong>IRR ≈ 17.2%</strong> (בין 15% ל-18%, קרוב יותר ל-18%)<br><br>
  אם שיעור הדחייה הוא 12% → IRR (17.2%) &gt; Hurdle Rate (12%) → הפרויקט כדאי.
</div>


<h2>MIRR — שיעור תשואה פנימי מתוקן</h2>

<h3>מתי IRR מטעה?</h3>

<p>
<strong>שיעור תשואה פנימי מתוקן (MIRR — Modified Internal Rate of Return)</strong>
פותח לתקן שני כשלים מוכרים של IRR:
</p>

<ol>
  <li>
    <strong>כשל 1 — שינויי סימן מרובים:</strong> כאשר תזרים המזומנים משנה סימן (מחיובי
    לשלילי ושוב לחיובי) יותר מפעם אחת, ייתכנו מספר פתרונות ל-IRR — תוצאות שונות
    ולא חד-משמעיות.
  </li>
  <li>
    <strong>כשל 2 — הנחת השקעה מחדש:</strong> IRR מניח שכל תזרים חיובי בינים מושקע
    מחדש בשיעור ה-IRR עצמו. בפרויקטי נדל"ן בישראל עם IRR של 20%, להניח השקעה
    מחדש ב-20% היא הנחה לא מציאותית.
  </li>
</ol>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
MIRR = [(FV תזרים חיובי / PV תזרים שלילי)^(1/n)] − 1
</div>

<p>
כאשר:
</p>
<ul>
  <li>תזרים חיובי מוכפל קדימה (FV) בשיעור השקעה מחדש ריאלי (לרוב WACC)</li>
  <li>תזרים שלילי מוכן לאחור (PV) בשיעור מימון</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — השוואת IRR ל-MIRR:</strong><br><br>
  פרויקט A: השקעה −1,000,000 | שנה 1: +3,000,000 | שנה 2: −1,500,000<br>
  (שינוי סימן כפול — IRR לא חד-משמעי)<br><br>
  IRR מחשב שני ערכים: ≈ 50% ו-≈ −200% — בלתי שמיש.<br><br>
  MIRR (שיעור מימון 8%, שיעור השקעה מחדש 10%):<br>
  FV תזרים חיובי שנה 1: 3,000,000 × 1.10 = 3,300,000<br>
  PV תזרים שלילי שנה 2: 1,500,000 / 1.08 = 1,388,889<br>
  PV השקעה ראשונית: 1,000,000 + 1,388,889 / 1.08 = 2,285,905<br>
  MIRR = (3,300,000 / 2,285,905)^(1/2) − 1 ≈ <strong>20.1%</strong><br><br>
  MIRR נותן תשובה אחת ברורה — הרבה יותר שימושי.
</div>

<div style="background:#e8f5e9;border-right:5px solid #2e7d32;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>מהשטח — MIRR בניתוח אשראי:</strong><br><br>
  "בוועדות אשראי שאני מלווה, כשמגיעים פרויקטים עם IRR של 30% ומעלה אני תמיד שואל:
  מה ה-MIRR? IRR גבוה מאוד לרוב מחייב השקעה מחדש בשיעור לא ריאלי. כשמחשבים MIRR
  עם שיעור השקעה מחדש של 8%–10%, המדד מתכנס לטווח הרבה יותר הגיוני ומחדד את
  הדיון על ריאליות הפרויקט." — אנליסט אשראי בכיר, בנק גדול בישראל
</div>


<h2>שימוש ב-NPV ו-IRR בניתוח נדל"ן — יישום מעשי</h2>

<h3>מתי NPV ומתי IRR?</h3>

<p>
בניתוח מקצועי, NPV ו-IRR משמשים יחד ומשלימים זה את זה:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מאפיין</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">NPV</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">IRR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מה הוא מודד?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ערך בש"ח</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תשואה באחוזים</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">דורש שיעור היוון?</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כן — חייב לבחור r</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">לא — IRR מחושב מהתזרים</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">השוואת פרויקטים בגדלים שונים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מקשה (סכומים שונים)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מאפשר (אחוז אחיד)</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כשלים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">רגיש מאוד לשיעור ההיוון</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כשל שינויי סימן; הנחת השקעה</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">כלל קבלת החלטה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">NPV &gt; 0 → השקע</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">IRR &gt; Hurdle Rate → השקע</td>
    </tr>
  </tbody>
</table>

<h3>ניתוח כדאיות — דוגמה אינטגרטיבית</h3>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — השוואת שני פרויקטים נדל"ן:</strong><br><br>
  <strong>פרויקט X — בניין משרדים בפתח-תקווה:</strong><br>
  השקעה: −12,000,000 ש"ח | תזרים שנות 1-5: 1,500,000/שנה | תזרים שנה 6: 9,000,000 (מכירה)<br><br>
  NPV (r=9%): +1,243,000 ש"ח | IRR: ≈ 11.8%<br><br>
  <strong>פרויקט Y — מחסן לוגיסטיקה באשדוד:</strong><br>
  השקעה: −6,000,000 ש"ח | תזרים שנות 1-5: 800,000/שנה | תזרים שנה 6: 5,000,000 (מכירה)<br><br>
  NPV (r=9%): +781,000 ש"ח | IRR: ≈ 12.3%<br><br>
  <strong>מסקנה:</strong> לפי IRR, פרויקט Y עדיף (12.3% &gt; 11.8%). אך לפי NPV, פרויקט X יוצר יותר ערך
  בשקלים (+1,243,000 לעומת +781,000). אם תקציב המשקיע מוגבל ל-6,000,000 ש"ח — Y הוא הבחירה.
  אם תקציב אינו מוגבל — X יוצר יותר ערך אבסולוטי.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה לאנליסט — רגישות ל"זבל נכנס = זבל יוצא":</strong><br><br>
  NPV ו-IRR כל כך רגישים להנחות התזרים שאנליסטים חסרי ניסיון יכולים ליצור כל תוצאה שרצויה
  על-ידי כוונון הנחות. בוועדות אשראי מקצועיות, הוצגת ניתוח כדאיות תמיד לוותה ב-<strong>ניתוח
  רגישות (Sensitivity Analysis)</strong> — מה קורה אם שיעור ההיוון עולה ב-2%? אם שכירות
  יורדת ב-10%? אם פרויקט מאחר בשנה? ייצוג ויזואלי של תרחישים אלה הוא ציפייה מקצועית.
</div>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום — מדדי כדאיות השקעה</h2>

<h3>חמש נקודות המפתח של המודול</h3>
<ol>
  <li>
    <strong>NPV = ערך בשקלים:</strong> NPV מציג כמה ערך, בשקלים נוכחיים, הפרויקט יוצר
    מעבר לעלות ההון. NPV חיובי = כדאי. NPV = 0 = אדיש. הוא המדד הכלכלי הנכון ביותר,
    אך רגיש מאוד לבחירת שיעור ההיוון.
  </li>
  <li>
    <strong>IRR = שיעור תשואה; אך לא מושלם:</strong> IRR מודד תשואה כאחוז ואינו דורש
    קביעת שיעור היוון. יתרון: ניתן להשוות בין פרויקטים בגדלים שונים. חיסרון: כשל
    שינויי סימן ו"הנחת השקעה מחדש" לא ריאלית.
  </li>
  <li>
    <strong>MIRR מתקן את כשלי IRR:</strong> MIRR מפריד בין שיעור מימון לשיעור השקעה
    מחדש, ותמיד נותן תשובה חד-משמעית אחת. בפרויקטי נדל"ן מורכבים עם תזרים משנה
    סימן — MIRR עדיף על IRR.
  </li>
  <li>
    <strong>WACC = שיעור ההיוון הנכון:</strong> לפרויקטים הממומנים בחוב והון עצמי,
    ה-WACC הוא שיעור ההיוון המתאים לחישוב NPV. זכרו: ריבית החוב מוזלת במגן המס
    (שיעור מס 23% בישראל).
  </li>
  <li>
    <strong>ניתוח רגישות הוא חובה מקצועית:</strong> NPV ו-IRR בנקודה אחת הם חסרי
    ערך ללא ניתוח רגישות. כל ניתוח כדאיות מקצועי כולל תרחישי "מה-אם" — שינויי ריבית,
    ירידת שכירות, עיכוב בנייה.
  </li>
</ol>

<h3>מילון מונחים</h3>
<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">מונח עברי</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">English Term</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">הגדרה קצרה</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שווי נוכחי נקי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Net Present Value (NPV)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סכום PV של כל תזרים פחות השקעה ראשונית; חיובי = כדאי</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעור תשואה פנימי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Internal Rate of Return (IRR)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעור ההיוון שבו NPV=0; משמש לפסיקה לפי Hurdle Rate</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעור תשואה פנימי מתוקן</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Modified IRR (MIRR)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">IRR עם שיעורי מימון והשקעה מחדש נפרדים; מונע כשל IRR</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">עלות ממוצעת משוקללת הון</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">WACC</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ממוצע משוקלל של עלות חוב ועלות הון עצמי; משמש כשיעור היוון</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעור דחייה / תשואת מינימום</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Hurdle Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תשואה מינימלית שהמשקיע דורש; IRR מושווה אליו</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">ניתוח רגישות</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Sensitivity Analysis</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בחינת השפעת שינויים בהנחות על NPV / IRR</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעור ריבית חסרת סיכון</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Risk-Free Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">תשואת אג"ח ממשלתי; בסיס לחישוב שיעור היוון</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Cap Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Capitalization Rate</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">NOI / שווי נכס; שיעור היוון לנכסים מניבים; בסיס פרפטואיטי</td>
    </tr>
  </tbody>
</table>

<h3>גשר למודול הבא</h3>
<p>
לאחר שרכשנו את יסודות TVM, ריבית ישראלית, ומדדי NPV ו-IRR — המודולים הבאים יצללו
לתוך ניתוח תזרים מזומנים מפורט (<em>מודול 4</em>) ומבנה עסקאות מימון (<em>מודול 5</em>).
נראה כיצד לבנות מודל פיננסי שלם לפרויקט נדל"ן, מ"ריק" ועד להחלטת ועדת האשראי.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = "Seeds Module 1-3 reading and summary content for Course 1 (יסודות מימון נדל\"ן)"

    def handle(self, *args, **options) -> None:
        # ── Locate Course 1 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=1)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=1 not found. "
                "Run 'python manage.py seed_data' first to create the course structure."
            )

        self.stdout.write(f"Found course: {course}")

        # Pair each module metadata with its reading and summary HTML
        module_content = [
            (MODULES[0], M1_READING_HTML, M1_SUMMARY_HTML),
            (MODULES[1], M2_READING_HTML, M2_SUMMARY_HTML),
            (MODULES[2], M3_READING_HTML, M3_SUMMARY_HTML),
        ]

        for module_meta, reading_html, summary_html in module_content:
            self._seed_module(course, module_meta, reading_html, summary_html)

        self.stdout.write(self.style.SUCCESS("\nAll done — Course 1 modules 1-3 seeded successfully."))

    def _seed_module(
        self,
        course: Course,
        meta: dict,
        reading_html: str,
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
            (2, ComponentType.COMPREHENSION, ""),
            (3, ComponentType.EXERCISES, ""),
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
