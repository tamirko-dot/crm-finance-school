"""
Management command: seed_c06_content
Seeds Module 1-3 content for Course 6 (מבנה עסקאות מימון).

Usage:
    python manage.py seed_c06_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": 'אנטומיה של עסקת מימון נדל"ן',
        "slug": "anatomya-iskat-mimun",
        "estimated_minutes": 50,
    },
    {
        "module_number": 2,
        "title_he": "Senior Debt, Mezzanine ו-Equity",
        "slug": "senior-debt-mezzanine-equity",
        "estimated_minutes": 55,
    },
    {
        "module_number": 3,
        "title_he": "ערבויות ובטחונות",
        "slug": "aravuyot-uvitachonot",
        "estimated_minutes": 50,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (אנטומיה של עסקת מימון נדל"ן)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>אנטומיה של עסקת מימון נדל"ן</h2>

<p>
כל עסקת מימון נדל"ן — בין אם מדובר ברכישת בניין משרדים, פרויקט ייזום או מחזור הלוואה —
בנויה מרכיבים קבועים: שחקנים, שכבות הון, תהליך ומסמכים. הבנת האנטומיה הבסיסית של העסקה
היא תנאי הכרחי לכל אנליסט אשראי שרוצה לקרוא ולנתח מבנה מימון.
</p>

<h2>שחקני העסקה — מי עומד בכל צד?</h2>

<p>
בכל עסקת מימון נדל"ן פועלים מספר שחקנים בעלי אינטרסים שונים ולעיתים מנוגדים:
</p>

<h3>הלווה (Borrower)</h3>
<p>
בדרך כלל חברת SPV (Special Purpose Vehicle) שהוקמה ייעודית לפרויקט. הלווה הוא הבעלים
המשפטי של הנכס, המקבל את מימון המלווים ונושא בחובת ההחזר. שימוש ב-SPV מבודד את סיכוני
הפרויקט מיתר פעילות היזם.
</p>

<h3>המלווה הבכיר (Senior Lender)</h3>
<p>
בדרך כלל בנק מסחרי או גוף מוסדי (חברת ביטוח, קרן פנסיה). מחזיק בשיעבוד ראשון על הנכס,
בעדיפות מרבית בגבייה, ומציע את הריבית הנמוכה ביותר. ה-Senior Lender מממן לרוב עד 60%–65%
משווי הנכס.
</p>

<h3>מלווה המזנין (Mezzanine Lender)</h3>
<p>
גורם מימון ביניים — בין החוב הבכיר לבין ההון העצמי. מממן שכבת סיכון גבוהה יותר, בריבית גבוהה
יותר, ומחזיק בביטחונות משניים (לרוב שיעבוד מניות ה-SPV ולא שיעבוד ישיר על הנכס).
</p>

<h3>משקיעי ההון (Equity Investors)</h3>
<p>
היזם ושותפיו — מביאים את ההון העצמי לעסקה. נושאים בכל הסיכון הראשון, אך גם בפוטנציאל
התשואה הגבוה ביותר. ה-Equity הוא "הכרית" שמגינה על שכבות החוב.
</p>

<h3>מתווכים (Intermediaries)</h3>
<p>
כוללים: יועץ פיננסי (מסדיר בין לווה למלווים), עורכי דין (משפטי עסקה), שמאי (מעריך שווי נכס),
יועץ מס, חברת ניהול נכסים. המתווכים אינם צדדים להלוואה אך חיוניים לסגירתה.
</p>

<h2>מבנה ה-Capital Stack — שכבות סיכון ותשואה</h2>

<p>
ה-<strong>Capital Stack</strong> הוא המבנה ההיררכי של כל מקורות המימון בעסקה, מסודרים לפי
עדיפות בגבייה ורמת סיכון. ההיררכיה קריטית: כשעסקה "מפסידה" — מי מפסיד ראשון?
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Capital Stack (מלמטה למעלה — סיכון גובר, תשואה גבוהה יותר):<br><br>
  [שכבה 1 — תחתית] Equity (הון עצמי) — נושא ראשון בהפסדים<br>
  [שכבה 2]          Mezzanine — בין חוב לבין הון<br>
  [שכבה 3 — עליון]  Senior Debt — ראשון להיפרע, אחרון לספוג הפסד
</div>

<p>
<strong>הרציונל:</strong> ה-Equity הוא "הכרית" — אם שווי הנכס ירד ב-20%, ה-Equity ספג את
כל ה-20%. ה-Senior Debt טרם נפגע. לכן המלווה הבכיר יכול להציע ריבית נמוכה — הסיכון שלו מוגן
על ידי שכבות ה-Equity והמזנין שמתחתיו.
</p>

<h2>LTV לפי שכבה — כיצד כל שכבה תחומה</h2>

<p>
כל שכבה בCapital Stack מוגדרת על ידי תחום ה-LTV שלה. זה הבסיס להבנת הסיכון של כל שחקן:
</p>

<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">שכבה</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">תחום LTV</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ריבית טיפוסית</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ביטחון</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Senior Debt</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">0% עד 65%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">P+1.5%–3%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעבוד ראשון על נכס</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Mezzanine</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">65% עד 80%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">10%–15%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">שיעבוד מניות SPV</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">Equity</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">80% ומעלה (השאר)</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">IRR 15%–25%</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בעלות בנכס — ללא עדיפות חוב</td>
    </tr>
  </tbody>
</table>

<p>
<strong>דוגמה:</strong> נכס בשווי 100M₪ — Senior Debt 65M₪, Mezzanine 15M₪ (LTV 65%–80%),
Equity 20M₪ (LTV 80%–100%). אם שווי הנכס ירד ל-70M₪, ה-Equity (20M₪) נמחק לחלוטין,
ה-Mezzanine ספג הפסד של 10M₪, ורק ה-Senior Debt (65M₪) נפרע במלואו.
</p>

<h2>תהליך עסקה טיפוסי</h2>

<p>
כל עסקת מימון נדל"ן עוברת שלבים קבועים — מהרעיון ועד לסגירה. הכרת השלבים חיונית לאנליסט
שמעורב בתהליך האשראי:
</p>

<h3>שלב 1 — Term Sheet (מסמך עקרונות)</h3>
<p>
מסמך לא-מחייב (או מחייב חלקית) שמגדיר את עיקרי המימון המוצע: גובה הלוואה, ריבית, בטחונות,
אמות מידה פיננסיות (Covenants). ה-Term Sheet הוא בסיס למשא ומתן — לא החוזה הסופי.
</p>

<h3>שלב 2 — Due Diligence (בדיקת נאותות)</h3>
<p>
בדיקה מקיפה של: הנכס (שמאות, בדיקה הנדסית), הלווה (דוחות כספיים, ניתוח אשראי, בדיקת
רקע), המסמכים המשפטיים (בעלות נקייה, היתרים, חוזי שכירות). Due Diligence הוא שלב שאין
לדלג עליו — כאן מתגלות בעיות שיכולות להרוג עסקה.
</p>

<h3>שלב 3 — Credit Approval (אישור אשראי)</h3>
<p>
הצגת ניתוח האשראי לוועדת האשראי של הגוף המממן. הוועדה מאשרת, דוחה, או מאשרת בתנאים
(Approval with Conditions). ה-Credit Memo המוצג לוועדה הוא תוצר עבודת האנליסט.
</p>

<h3>שלב 4 — Closing (סגירת העסקה)</h3>
<p>
חתימת כל מסמכי ההלוואה, רישום השיעבודים, אסיפת תנאים מקדימים (Conditions Precedent)
ומשיכת הכסף. Closing מערב עורכי דין, נוטריונים, ולעיתים נאמן (Trustee).
</p>

<h2>מסמכי העסקה הבסיסיים</h2>

<p>
בכל עסקת מימון נדל"ן חתומים מסמכים משפטיים קבועים:
</p>

<ul>
  <li>
    <strong>הסכם הלוואה (Loan Agreement):</strong> המסמך המרכזי — מגדיר את כל תנאי ההלוואה:
    גובה, ריבית, לוח סילוקין, Covenants, אירועי ברירת מחדל, זכות פירעון מוקדם.
  </li>
  <li>
    <strong>שטר חוב (Promissory Note):</strong> מסמך ניתן להסבה שמתעד את חובת הפירעון.
    מאפשר למלווה להעביר את החוב לצד שלישי.
  </li>
  <li>
    <strong>שיעבוד (Mortgage / Hypothec):</strong> רישום זכות הבטוחה על הנכס בטאבו —
    מבטיח שהמלווה יכול לממש את הנכס אם הלווה אינו פורע.
  </li>
  <li>
    <strong>ערבות (Guarantee):</strong> התחייבות של צד שלישי (ערב אישי, חברת אם) לפרוע
    את החוב אם הלווה לא יכול. כלי בטוחה נוסף מעבר לשיעבוד הנכס.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — מבנה ה-Capital Stack קובע מי מפסיד ראשון:</strong><br>
  הון עצמי תמיד בתחתית ה-Capital Stack — ראשון לספוג הפסד, אחרון להיפרע. לכן, בניתוח
  אשראי, שאלת "כמה Equity יש בעסקה?" היא שאלת מפתח: Equity גבוה = כרית הגנה גדולה
  לשכבות החוב. Equity נמוך = סיכון גבוה יותר לכל המלווים. <strong>מבנה ה-Capital Stack הוא
  לא פרט טכני — זו ארכיטקטורת הסיכון של העסקה כולה.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Comprehension HTML
# ---------------------------------------------------------------------------

M1_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על אנטומיה של עסקת מימון — בחן את הבנתך לפני שממשיכים.
השאלות בוחנות את תפקידי השחקנים, מבנה ה-Capital Stack, LTV לפי שכבה ושלבי תהליך העסקה.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Exercises HTML
# ---------------------------------------------------------------------------

M1_EXERCISES_HTML = """
<p>
5 תרגילים על מבנה Capital Stack ועסקאות מימון. התרגילים כוללים מיפוי שחקנים לפי תפקיד,
בניית Capital Stack מנתוני עסקה, זיהוי מי ספג הפסד בתרחיש ירידת שווי, וניתוח מסמכי עסקה.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — אנטומיה של עסקת מימון נדל"ן</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>שחקני העסקה:</strong> לווה (SPV), מלווה בכיר, מלווה מזנין, משקיעי הון ומתווכים.
    לכל שחקן אינטרס שונה — הבנת מיקום כל שחקן ב-Capital Stack קריטית לניתוח אשראי.
  </li>
  <li>
    <strong>Capital Stack — שכבות:</strong> Senior Debt (0%–65% LTV) → Mezzanine (65%–80% LTV)
    → Equity (80% ומעלה). כל שכבה נושאת ברמת סיכון ותשואה שונה; ה-Equity ראשון להפסיד.
  </li>
  <li>
    <strong>LTV לפי שכבה:</strong> Senior עד 65%; Mezzanine עד 80%; Equity את היתרה.
    ירידת שווי נכס "מוחקת" את שכבות הסיכון מלמטה למעלה — Equity ראשון, Mezzanine שני.
  </li>
  <li>
    <strong>תהליך עסקה:</strong> Term Sheet → Due Diligence → Credit Approval → Closing.
    כל שלב הוא שער — עסקה יכולה ליפול בכל שלב. Due Diligence הוא שלב גילוי הסיכונים.
  </li>
  <li>
    <strong>מסמכי עסקה:</strong> הסכם הלוואה, שטר חוב, שיעבוד, ערבות. יחד הם יוצרים את
    מערך הבטחונות והזכויות שמגן על המלווה לאורך חיי ההלוואה.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
ראינו שה-Capital Stack כולל שלוש שכבות — Senior Debt, Mezzanine ו-Equity. <em>מודול 2</em>
יצלול לעומק לכל אחת מהן: מאפיינים, עלות הון, מבנה, וההסכמים שמסדירים את היחסים ביניהן.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (Senior Debt, Mezzanine ו-Equity)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>Senior Debt, Mezzanine ו-Equity — שלוש שכבות ה-Capital Stack</h2>

<p>
כל שכבה ב-Capital Stack היא עולם בפני עצמו: מבנה שונה, עלות שונה, מנגנוני הגנה שונים.
אנליסט אשראי שמבין את ההבדלים ביניהן יכול לנתח כל מבנה מימון — גם מורכב — ולזהות את
נקודות הסיכון.
</p>

<h2>Senior Debt — החוב הבכיר</h2>

<p>
<strong>Senior Debt</strong> הוא שכבת החוב הגבוהה בסדר העדיפויות — ראשון להיפרע בכל תרחיש,
אחרון לספוג הפסד. זהו המוצר שבנקים מסחריים וגופים מוסדיים מציעים לרוב.
</p>

<h3>מאפייני Senior Debt:</h3>
<ul>
  <li><strong>LTV:</strong> עד 60%–65% משווי הנכס.</li>
  <li><strong>ריבית:</strong> נמוכה יחסית — Prime + 1.5%–3% לפי איכות הלווה והנכס.</li>
  <li><strong>בטחונות:</strong> שיעבוד ראשון (First Charge) על הנכס — זכות מימוש ראשונה.</li>
  <li><strong>Covenants:</strong> אמות מידה פיננסיות קפדניות — LTV, DSCR, ICR.</li>
  <li><strong>פירעון:</strong> לרוב Bullet (קרן בסוף) עם תשלומי ריבית שוטפים, או Amortizing.</li>
  <li><strong>קדימות בגבייה:</strong> בפירוק או מימוש — Senior Debt מקבל ראשון, לפני כל גורם אחר.</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — Senior Debt:</strong><br><br>
  נכס: מרכז מסחרי בשווי 80,000,000 ₪<br>
  Senior Debt: 50,000,000 ₪ (LTV 62.5%)<br>
  ריבית: Prime + 2% = ~7.5% (ריבית Prime כיום ~5.5%)<br>
  מח"מ: 5 שנים Bullet + אפשרות הארכה<br>
  בטחון: שיעבוד ראשון בטאבו על הנכס<br>
  DSCR מינימלי בחוזה: 1.20<br><br>
  <strong>עלות שנתית:</strong> 50,000,000 × 7.5% = 3,750,000 ₪ ריבית.
</div>

<h2>Mezzanine Finance — מימון הביניים</h2>

<p>
<strong>Mezzanine</strong> הוא שכבת המימון שנמצאת בין ה-Senior Debt לבין ה-Equity — לכן שמה "מזנין"
(קומת ביניים בארכיטקטורה). מאפשר ליזם לממן עסקאות עם LTV כולל של עד 80% תוך שהוא שומר
על פחות הון עצמי.
</p>

<h3>מאפייני Mezzanine:</h3>
<ul>
  <li><strong>LTV:</strong> בדרך כלל LTV כולל 65%–80% (השכבה בין Senior ל-Equity).</li>
  <li>
    <strong>ריבית:</strong> גבוהה — 10%–15% בשנה. משקפת סיכון גבוה יותר ממקומו ב-Stack.
  </li>
  <li>
    <strong>PIK vs Cash:</strong> חלק מהמזנין משולם כ-PIK (Payment-in-Kind) — הריבית מצטברת
    לקרן ולא משולמת במזומן שוטף. מאפשר שמירת מזומן בעסקה, אך מגדיל את הקרן לאורך זמן.
  </li>
  <li><strong>בטחונות:</strong> לרוב שיעבוד מניות ה-SPV — לא שיעבוד ישיר על הנכס (שכבר
  נתפס ע"י ה-Senior).</li>
  <li><strong>Intercreditor:</strong> כפוף להסכם בין-מלווים (Intercreditor Agreement) שמגדיר
  יחסיו עם ה-Senior Lender.</li>
</ul>

<h3>PIK vs Cash Interest — ההבדל המעשי:</h3>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
דוגמה — הלוואת Mezzanine: 10,000,000 ₪, ריבית שנתית 12%:<br><br>
Cash Interest: 10,000,000 × 12% = 1,200,000 ₪ שמשולמים שוטף<br><br>
PIK Interest:  ריבית מצטברת לקרן:<br>
  שנה 1: קרן = 10,000,000 + (10,000,000 × 12%) = 11,200,000 ₪<br>
  שנה 2: קרן = 11,200,000 + (11,200,000 × 12%) = 12,544,000 ₪<br>
  שנה 3: קרן = 12,544,000 + (12,544,000 × 12%) = 14,049,280 ₪<br><br>
עם PIK מלא: הלווה אינו משלם שוטף, אך בסיום — חייב 40% יותר!
</div>

<h2>Equity — הון עצמי</h2>

<p>
ה-<strong>Equity</strong> הוא ההשקעה של היזם ושותפיו — ההון שאין לו עדיפות פירעון על פני שכבות
החוב. ה-Equity נושא בכל הסיכון הראשון, אבל גם מקבל את כל העודף אחרי פירעון החובות.
</p>

<h3>מאפייני Equity:</h3>
<ul>
  <li><strong>שכבת LTV:</strong> כל מה שמעל ה-80% (כלומר, ה-20% התחתונים של שווי הנכס).</li>
  <li><strong>תשואה מטרה:</strong> IRR של 15%–25% — פרמיית סיכון על נשיאה בהפסד הראשוני.</li>
  <li><strong>ראשון לספוג הפסד:</strong> ירידת שווי מוחקת את ה-Equity לפני כל שכבת חוב.</li>
  <li><strong>אחרון להיפרע:</strong> ב-Waterfall תשלומים — Equity מקבל רק אחרי שכל החובות
  נפרעו במלואם.</li>
  <li><strong>Upside לא מוגבל:</strong> אם העסקה מצליחה, כל עודף השווי שייך ל-Equity.</li>
</ul>

<h2>Blended Cost of Capital — עלות ההון המשוקללת</h2>

<p>
כל שכבה נושאת עלות שונה. השאלה הכלכלית המרכזית: מה עלות ההון הכוללת של העסקה — בהתחשב
בכל השכבות?
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
דוגמה — נכס 100M₪:<br><br>
Senior Debt:  65M₪ × 7.5%   = 4,875,000 ₪<br>
Mezzanine:    15M₪ × 12.0%  = 1,800,000 ₪<br>
Equity:       20M₪ × 20.0%* = 4,000,000 ₪ (*IRR target)<br>
                                ───────────────────────────<br>
סה"כ עלות:   100M₪          = 10,675,000 ₪ לשנה<br><br>
Blended Cost of Capital = 10,675,000 ÷ 100,000,000 = 10.675%
</div>

<p>
ה-Blended Cost of Capital הוא הרף המינימלי שה-NOI של הנכס חייב לייצר כדי שהעסקה תהיה
כלכלית לכל השחקנים. נכס שמייצר NOI של 10.675% × 100M₪ = 10.675M₪ בדיוק מכסה את
עלות ההון הכוללת — ללא עודף.
</p>

<h2>Intercreditor Agreement — הסכם בין-מלווים</h2>

<p>
כאשר יש מספר מלווים (Senior + Mezzanine), חייב להיות הסכם שמסדיר את סדר העדיפויות ביניהם.
ה-<strong>Intercreditor Agreement</strong> קובע:
</p>

<ul>
  <li><strong>Waterfall תשלומים:</strong> Senior מקבל ראשון; Mezzanine מקבל לאחר מכן.</li>
  <li><strong>Standstill Period:</strong> תקופה שבה ה-Mezzanine מנוע מלנקוט צעדי אכיפה
  גם אם הלווה הפר — כדי לאפשר ל-Senior לפתור את הבעיה ראשון.</li>
  <li><strong>Purchase Option:</strong> זכות ה-Mezzanine לרכוש את חוב ה-Senior (לפני מימוש)
  ולתפוס את מקומו.</li>
  <li><strong>Consent Rights:</strong> סוגיות שדורשות הסכמת שני המלווים — מחזור חוב,
  שינוי מהותי בנכס, מכירת הנכס.</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — מזנין הוא לא "הון עצמי בתחפושת":</strong><br>
  תפיסה שגויה נפוצה: מזנין הוא "כמו Equity" כי הוא נושא סיכון גבוה. <strong>זו טעות.</strong><br>
  למלווה המזנין יש זכויות חוב ממשיות: הוא יכול לאכוף פירעון בהפרת חוזה, להגיש לפשיטת
  רגל, להפעיל שיעבוד מניות. ה-Equity אינו יכול לעשות אף אחד מאלה — הוא שותף בעסק,
  לא נושה. <strong>ה-Mezzanine גובר על ה-Equity בכל תרחיש כשל — ולכן חוב, לא הון.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Comprehension HTML
# ---------------------------------------------------------------------------

M2_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על Senior Debt, Mezzanine ו-Equity — בחן את יכולתך להבחין בין השכבות,
לחשב Blended Cost of Capital, ולהסביר את ההבדל בין Mezzanine ל-Equity.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Exercises HTML
# ---------------------------------------------------------------------------

M2_EXERCISES_HTML = """
<p>
5 תרגילים על Capital Stack ועלות הון. התרגילים כוללים בניית Capital Stack מנתוני עסקה,
חישוב Blended Cost of Capital, ניתוח תשלומי PIK לעומת Cash Interest לאורך 3 שנים,
וניתוח Waterfall בתרחיש מימוש נכס.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — Senior Debt, Mezzanine ו-Equity</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>Senior Debt:</strong> LTV עד 65%, ריבית נמוכה (Prime+1.5%–3%), שיעבוד ראשון על נכס,
    ראשון להיפרע. העדיפות הגבוהה ביותר בגבייה מוצדקת על ידי הביטחון החזק ביותר.
  </li>
  <li>
    <strong>Mezzanine:</strong> LTV 65%–80%, ריבית 10%–15%, שיעבוד מניות SPV. PIK מאפשר
    שמירת מזומן שוטף אך מגדיל קרן. כפוף ל-Intercreditor Agreement עם ה-Senior.
  </li>
  <li>
    <strong>Equity:</strong> שכבת LTV 80%+, IRR target 15%–25%, ראשון לספוג הפסד ואחרון
    להיפרע. Upside לא מוגבל — כל עודף שווי שייך לשכבת ה-Equity.
  </li>
  <li>
    <strong>Blended Cost of Capital:</strong> ממוצע משוקלל של עלויות כל השכבות. NOI הנכס
    חייב לעלות על ה-Blended Cost כדי שהעסקה תהיה כלכלית לכלל השחקנים.
  </li>
  <li>
    <strong>Intercreditor Agreement:</strong> מסדיר Waterfall, Standstill, Purchase Option
    וזכויות הסכמה. חיוני בכל עסקה עם מספר מלווים — קובע מי שולט בתרחיש כשל.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
ראינו שמלווים מגנים על עצמם בשיעבודים, Intercreditor Agreements, ושיעבוד מניות. <em>מודול 3</em>
יצלול לעומק לעולם <strong>הערבויות והבטחונות</strong> — כל הכלים שמלווים משתמשים בהם להבטחת
גבייה כשהלווה אינו פורע.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (ערבויות ובטחונות)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>ערבויות ובטחונות — הגנות המלווה</h2>

<p>
מלווה אינו יכול להסתמך רק על אמונתו שהלווה יפרע. כל הלוואה מגובה במערך בטחונות וערבויות —
כלים משפטיים שמאפשרים גבייה גם כאשר הלווה חדל לשלם. הכרת כלי הגבייה הנפוצים היא
חיונית לכל אנליסט אשראי.
</p>

<h2>שיעבוד ראשון על נכס — Mortgage / Hypothec</h2>

<p>
<strong>שיעבוד ראשון (First Mortgage / Hypothec)</strong> הוא הבטוחה הכי חזקה שמלווה יכול לדרוש:
זכות רשומה בטאבו שמאפשרת לו לממש את הנכס אם הלווה לא פורע.
</p>

<h3>מהות השיעבוד:</h3>
<ul>
  <li><strong>רישום בטאבו:</strong> השיעבוד רשום בלשכת רישום המקרקעין ומחייב כל רוכש עתידי.</li>
  <li><strong>עדיפות:</strong> "ראשון" — קדם לכל שיעבוד אחר שיירשם לאחר מכן.</li>
  <li><strong>מימוש:</strong> בהפרת חוזה, המלווה יכול לפנות לבית המשפט ולדרוש מכירת הנכס
  בכינוס נכסים ולגבות את חובו מהתמורה.</li>
  <li><strong>Follow the Asset:</strong> השיעבוד "עוקב" אחר הנכס — גם אם הנכס נמכר
  (בלא הסרת השיעבוד) הוא מחייב את הרוכש החדש.</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה:</strong><br><br>
  בנק אוחז שיעבוד ראשון על מחסן בשווי 20M₪ עבור הלוואה של 12M₪ (LTV 60%).<br>
  הלווה חדל תשלומים. הבנק מגיש בקשה לכינוס נכסים. המחסן נמכר ב-18M₪.<br><br>
  <strong>גבייה:</strong> הבנק גובה ראשון — 12M₪ + ריבית + הוצאות = ~13M₪. יתרת 5M₪
  לבעל הנכס (לאחר כיסוי כל החובות). הבנק גבה במלואו.
</div>

<h2>שיעבוד שלילי — Negative Pledge</h2>

<p>
<strong>Negative Pledge</strong> אינו שיעבוד פעיל — זוהי התחייבות חוזית של הלווה <em>שלא</em>
לשעבד את הנכס לגורם נוסף ללא הסכמת המלווה.
</p>

<h3>מדוע Negative Pledge חשוב?</h3>
<p>
ללא Negative Pledge, לווה יכול לשעבד את הנכס גם למלווה שני, ולשלש, ולדלל את הכרית של
המלווה הראשון. עם Negative Pledge, כל שיעבוד נוסף ללא הסכמה הוא הפרת חוזה — ומאפשר
למלווה לדרוש פירעון מיידי.
</p>

<h3>מגבלות Negative Pledge:</h3>
<ul>
  <li>אינו רשום בטאבו — <strong>אינו בר-תוקף כלפי צד שלישי</strong> שרכש שיעבוד בתום לב.</li>
  <li>הוא זכות חוזית בין המלווה ללווה — לא קניינית.</li>
  <li>הגנתו היא דרך הפרת חוזה, לא דרך מימוש ישיר של הנכס.</li>
</ul>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Negative Pledge טיפוסי בהסכם הלוואה:<br><br>
"הלווה מתחייב שלא לשעבד, לממשן, להטיל עיקול או כל שעבוד אחר על נכסי הפרויקט,
 כולם או חלקם, ללא קבלת אישור מראש ובכתב מהמלווה."
</div>

<h2>ערבות אישית — Personal Guarantee</h2>

<p>
<strong>ערבות אישית</strong> היא התחייבות של אדם פרטי (בדרך כלל בעל המניות או המנכ"ל)
לפרוע את חוב הלווה אם הלווה אינו יכול. היא "מרחיבה" את האחריות מעבר לנכס הספציפי —
לנכסים האישיים של הערב.
</p>

<h3>מתי מלווה ידרוש ערבות אישית?</h3>
<ul>
  <li>כאשר הלווה הוא SPV ללא היסטוריה — הבנק רוצה "נשמה" מאחורי העסקה.</li>
  <li>כאשר ה-LTV גבוה מהרגיל — ערבות אישית מוסיפה "כרית" נוספת.</li>
  <li>כאשר הלווה הוא ישות חדשה ללא Track Record מוכח.</li>
  <li>כאשר הפרויקט נמצא בשלב ייזום — לפני שיש נכס גמור לשמאות.</li>
</ul>

<h3>מגבלות ערבות אישית:</h3>
<ul>
  <li><strong>ערך תלוי בנכסי הערב:</strong> ערב ללא נכסים ממשיים = ערבות חסרת שווי.</li>
  <li><strong>קיפול חברות:</strong> יזם יכול להעביר נכסים מראש כדי לרוקן את הערבות.</li>
  <li><strong>עדיפות בפשיטת רגל:</strong> בפשיטת רגל של הערב, נושים אחרים מתחרים על אותם נכסים.</li>
  <li><strong>בית האישי:</strong> לרוב מוגן בחוק — מלווה יתקשה לממש את בית הערב.</li>
</ul>

<h2>ערבות חברתית — Corporate Guarantee</h2>

<p>
<strong>Corporate Guarantee</strong> (ערבות חברה אם / Parent Guarantee) היא ערבות של חברה
אחרת בקבוצה — לרוב חברת האם — לפירעון חוב ה-SPV.
</p>

<h3>יתרונות ומגבלות לעומת ערבות אישית:</h3>
<table style="border-collapse:collapse;width:100%;margin:12px 0;">
  <thead>
    <tr style="background:#1a2638;color:#fff;">
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">פרמטר</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ערבות אישית</th>
      <th style="padding:10px;text-align:right;border:1px solid #ccc;">ערבות חברתית</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">בסיס הנכסים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכסי הפרט — לעיתים מוגנים</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נכסי חברה — בד"כ גדולים יותר</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">אכיפה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מורכבת — תלויה בבית אישי ועוד</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">פשוטה יותר — תביעה מסחרית</td>
    </tr>
    <tr>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון מוניטין</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">גבוה — נוגע לאדם ספציפי</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">נוגע לכל הקבוצה העסקית</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון בקבוצה</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">מוגבל לפרט</td>
      <td style="padding:9px;border:1px solid #ddd;text-align:right;">סיכון הידבקות (Contagion) בקבוצה</td>
    </tr>
  </tbody>
</table>

<h2>שיעבוד מניות SPV — Pledge over Shares</h2>

<p>
<strong>שיעבוד מניות</strong> (Pledge over Shares) הוא שיעבוד על מניות ה-SPV שמחזיק את הנכס —
לא שיעבוד ישיר על הנכס עצמו. הוא נפוץ בהלוואות מזנין ובמקרים שבהם לא ניתן לרשום שיעבוד
ישיר (כגון שיעבוד שני על נכס שכבר שועבד ל-Senior).
</p>

<h3>כיצד עובד שיעבוד מניות:</h3>
<ul>
  <li><strong>שיעבוד על מניות ה-SPV:</strong> אם הלווה מפר חוזה, המלווה תופס שליטה ב-SPV
  על ידי מימוש השיעבוד על המניות.</li>
  <li><strong>השפעה:</strong> ברגע שהמלווה שולט ב-SPV, הוא שולט בנכס — ויכול למכרו, לנהלו
  או להעביר בעלות.</li>
  <li><strong>מהירות:</strong> לרוב מהיר יותר ממימוש שיעבוד ישיר על נכס (שדורש הליך בית משפט).</li>
  <li><strong>מגבלות:</strong> SPV עשוי לשאת חובות נוספים שלא ידועים למלווה ביום הגבייה.</li>
</ul>

<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>דוגמה — שיעבוד מניות:</strong><br><br>
  חברת SPV מחזיקה מחסן בשווי 20M₪. Mezzanine Lender העניק 4M₪ בשיעבוד מניות ה-SPV.<br>
  הלווה מפר תשלומים. הבנק הבכיר ממש את שיעבוד הנכס (20M₪) — אחרי פירעון Senior 12M₪,
  נותרת יתרה של ~8M₪. ה-Mezzanine מממש שיעבוד מניות ה-SPV הריק (לאחר הנכס כבר מומש)<br><br>
  <strong>לקח:</strong> שיעבוד מניות שימושי כשה-Senior לא ממש, אך לאחר מימוש ה-Senior
  ה-SPV עלול להיות קליפה ריקה. חשוב לאמת שה-SPV מחזיק בנכס ממשי גם אחרי מימוש Senior.
</div>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — ערבות אישית ללא כיסוי ממשי:</strong><br>
  יזמים רבים נותנים ערבות אישית שמבחינה פורמלית תקפה — אך שווה מעט בפועל. לפני קבלת
  ערבות אישית, חובה לבדוק:<br>
  (א) מה נכסי הערב? האם יש נכסים ממשיים או רק נכסים ממונפים עמוק?<br>
  (ב) האם הנכסים חופשיים משיעבוד? נכס משועבד אינו תורם לכושר הגבייה.<br>
  (ג) האם יש ערבויות נוספות על אותם נכסים לגורמים אחרים?<br><br>
  <strong>ערבות אישית ללא כיסוי ממשי — שווה פחות מהניר עליו כתובה.
  תמיד בדוק את שווי נכסי הערב.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 3 — Comprehension HTML
# ---------------------------------------------------------------------------

M3_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על ערבויות ובטחונות — בחן את יכולתך להבחין בין סוגי הבטחונות, לזהות מתי
ערבות אישית חסרת שווי, ולהסביר את ההבדל בין שיעבוד נכס לשיעבוד מניות SPV.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Exercises HTML
# ---------------------------------------------------------------------------

M3_EXERCISES_HTML = """
<p>
5 תרגילים על ערבויות ובטחונות. התרגילים כוללים ניתוח מערך הבטחונות בעסקה נתונה,
הערכת שווי ערבות אישית לפי נכסי הערב, ניתוח תרחיש גבייה לפי סדר עדיפויות,
השוואת שיעבוד נכס לשיעבוד מניות ובחינת Negative Pledge כנגד שיעבוד שני.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — ערבויות ובטחונות</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>שיעבוד ראשון על נכס:</strong> הבטוחה החזקה ביותר — רשום בטאבו, עוקב אחר הנכס,
    מאפשר מימוש ישיר. "ראשון" = עדיפות על כל שיעבוד שיירשם לאחר מכן.
  </li>
  <li>
    <strong>Negative Pledge:</strong> התחייבות חוזית שלא לשעבד ללא הסכמה — אינו רשום בטאבו,
    אינו קנייני. מגן על המלווה מפני דילול ביטחונות, אך אכיפתו דרך הפרת חוזה בלבד.
  </li>
  <li>
    <strong>ערבות אישית:</strong> מרחיבה אחריות לנכסים האישיים של הערב. שווה רק כמו
    הנכסים החופשיים של הערב — לפני קבלה, חובה לבדוק שווי נכסי הערב וכיסוי שיעבודים קיימים.
  </li>
  <li>
    <strong>ערבות חברתית:</strong> Parent Guarantee — חברת האם מערבת כולה. בסיס נכסים
    גדול יותר, אך סיכון Contagion — כשל בפרויקט עלול להדביק את כל הקבוצה.
  </li>
  <li>
    <strong>שיעבוד מניות SPV:</strong> כלי גבייה חלופי — תפיסת שליטה ב-SPV במקום מימוש ישיר
    של הנכס. מהיר יותר לעיתים, אך ה-SPV עשוי לשאת חובות נסתרים. נפוץ ב-Mezzanine.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
למדנו את שלושת המרכיבים הבסיסיים של מבנה עסקת מימון: אנטומיית העסקה, שכבות ה-Capital Stack,
וכלי הבטחונות. <em>מודול 4</em> יישם את כל אלה ב<strong>ניתוח עסקת מימון מלאה</strong> —
מ-Term Sheet ועד ל-Credit Memo, ויציג כיצד אנליסט אשראי בונה המלצת מימון מקצועית.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 6 "
        "(מבנה עסקאות מימון)"
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 6 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=6)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=6 not found. "
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
            self.style.SUCCESS("\nAll done — Course 6 modules 1-3 seeded successfully.")
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
