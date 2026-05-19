"""
Seeds Module 1-3 content for Course 8 (ניתוח מסמכים משפטיים).
Usage: python manage.py seed_c08_content
"""

from django.core.management.base import BaseCommand, CommandError

from content.models import Course, Module, ModuleComponent, ComponentType


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

MODULES = [
    {
        "module_number": 1,
        "title_he": "הסכם הלוואה — מבנה, רכיבים וסעיפים קריטיים",
        "slug": "heskem-halvaa-mivne-svivim",
        "estimated_minutes": 55,
    },
    {
        "module_number": 2,
        "title_he": "Covenants — אמות מידה פיננסיות וסעיפי הגבלה",
        "slug": "covenants-amot-mida-finanziot",
        "estimated_minutes": 55,
    },
    {
        "module_number": 3,
        "title_he": "מסמכי שיעבוד ובטחונות — קריאה ופרשנות",
        "slug": "mismche-shiabud-uvtachonot",
        "estimated_minutes": 50,
    },
]


# ---------------------------------------------------------------------------
# Module 1 — Reading HTML (הסכם הלוואה — מבנה, רכיבים וסעיפים קריטיים)
# ---------------------------------------------------------------------------

M1_READING_HTML = """
<h2>הסכם הלוואה — המסמך הראשי של כל עסקת מימון</h2>

<p>
הסכם ההלוואה (Loan Agreement) הוא לב ליבה של כל עסקת מימון נדל"ן. הוא אינו רק
"חוזה" — הוא המפה המשפטית השלמה של מערכת היחסים בין הלווה לבין המלווה: מה מותר ללווה
לעשות, מה אסור לו, מתי הכסף יוצא, מה קורה כשהוא אינו פורע, וכיצד המלווה גובה את חובו.
כל אנליסט אשראי שקורא מבנה עסקה חייב לדעת לנווט בהסכם ההלוואה ולזהות את הסעיפים הקריטיים.
</p>

<h2>מבנה הסכם הלוואה — ששת הפרקים הקריטיים</h2>

<h3>א. הגדרות (Definitions)</h3>
<p>
הפרק הראשון והשעמומי לכאורה — אך למעשה הכי חשוב. כל מונח מוגדר בדייקנות, ואותה הגדרה
תחול בכל מקום בהסכם. ארבע הגדרות שכל אנליסט חייב לזהות:
</p>
<ul>
  <li>
    <strong>לווה (Borrower):</strong> בדרך כלל חברת SPV — חברה ייעודית שהוקמה לפרויקט.
    ההגדרה קריטית: האם ה-Borrower כולל חברות קשורות? האם ל-Borrower יש מנגנון "נציג"?
  </li>
  <li>
    <strong>מלווה (Lender):</strong> מי עומד בצד המממן — בנק יחיד, קונסורציום, גוף מוסדי.
    הגדרת ה-Lender קובעת מי רשאי להמחות את ההלוואה לצד שלישי.
  </li>
  <li>
    <strong>מסגרת (Facility):</strong> סכום ההלוואה המאושרת — הקצאה מרבית. לא בהכרח הסכום
    שנמשך בפועל. מסגרת עשויה לכלול רכיב Term Loan ורכיב Revolving Credit.
  </li>
  <li>
    <strong>משיכה (Drawdown):</strong> הגדרת תנאי כל משיכה בפועל מתוך המסגרת — הודעת משיכה
    (Drawdown Notice), מועד, מינימום, ותנאים מקדימים לכל משיכה בנפרד.
  </li>
</ul>

<h3>ב. תנאים מקדימים (Conditions Precedent)</h3>
<p>
אלה הן "השערים" שחייבים להיפתח לפני שהמלווה מחויב לשחרר כספים. Conditions Precedent
מחולקים לשניים: תנאים לחתימה (Signing CPs) ותנאים למשיכה (Drawdown CPs).
</p>

<p>דוגמאות טיפוסיות לתנאים מקדימים בעסקאות נדל"ן ישראליות:</p>
<ul>
  <li>רישום שיעבוד בטאבו לטובת המלווה (ואישור עורך דין שאין שיעבוד קודם עליו).</li>
  <li>הצגת שומת שמאי מוסכם שאינה ישנה מ-90 ימים.</li>
  <li>אישור היתר בנייה תקף (בפרויקטי ייזום).</li>
  <li>חוזי שכירות חתומים המכסים לפחות X% מהשטח (בנכסים מניבים).</li>
  <li>ביטוח נכס בסכום מלא עם "ציון לטובת המלווה" כמוטב ראשון.</li>
  <li>אישורי בעלות נקיים — נסח טאבו עדכני ללא הערות מגבילות.</li>
  <li>ערבויות חתומות (אישיות / חברתיות) מאת הגורמים הנדרשים.</li>
</ul>

<p>
<strong>חשיבות לאנליסט:</strong> כאשר לווה מבקש "ויתור" (Waiver) על תנאי מקדים, זהו
אות אזהרה. תנאי מקדים שנמחל הוא "גדר" שהורדה — המלווה חשוף יותר.
</p>

<h3>ג. הצהרות ואחריות (Representations &amp; Warranties)</h3>
<p>
הלווה מצהיר בחתימה על ההסכם שעובדות מסוימות נכונות — ולעיתים מחדש אותן בכל משיכה
ובכל תקופה. אם הצהרה מתבררת כשקרית, זה אירוע ברירת מחדל (Event of Default).
</p>

<p>הצהרות טיפוסיות:</p>
<ul>
  <li>הלווה הוא חברה בת-קיימא (Going Concern), מאוגד כדין, ללא הליכי פשיטת רגל תלויים.</li>
  <li>כל המסמכים שהוצגו למלווה (דוחות, חוזים, שמאויות) הם מדויקים ומלאים.</li>
  <li>אין הליכים משפטיים תלויים ועומדים שעשויים להשפיע מהותית על הנכס.</li>
  <li>הנכס אינו משועבד לאף גורם אחר (ללא ידיעת המלווה).</li>
  <li>אין שינוי מהותי שלילי (Material Adverse Change) מיום הגשת הבקשה.</li>
</ul>

<h3>ד. אמות מידה פיננסיות (Financial Covenants)</h3>
<p>
Covenants הם המנגנון שמאפשר למלווה לעקוב אחר בריאותה הפיננסית של העסקה לאורך חיי
ההלוואה. שלושת ה-Covenants הנפוצים בנדל"ן ישראלי:
</p>
<ul>
  <li>
    <strong>LTV (Loan-to-Value):</strong> יחס הלוואה לשווי נכס — לרוב לא יעלה על 65%–70%.
    נבדק בכל שמאות חוזרת (לרוב שנתית).
  </li>
  <li>
    <strong>DSCR (Debt Service Coverage Ratio):</strong> יחס כיסוי שירות חוב — NOI חלקי
    שירות חוב שנתי. לרוב ≥ 1.20. נבדק רבעונית או חצי שנתי.
  </li>
  <li>
    <strong>ICR (Interest Coverage Ratio):</strong> יחס כיסוי ריבית — EBITDA חלקי הוצאות ריבית.
    פחות נפוץ מ-DSCR בנדל"ן, אך מופיע בעסקאות ייזום.
  </li>
</ul>

<h3>ה. אירועי ברירת מחדל (Events of Default)</h3>
<p>
זהו הפרק שאנליסט חכם קורא <em>ראשון</em>. אירועי ברירת המחדל מגדירים מתי המלווה רשאי
להכריז על ההלוואה כפרועה מיידית (Acceleration). הפרק הזה הוא "מנגנון ההדק" של ההלוואה.
</p>

<p>אירועי ברירת מחדל טיפוסיים:</p>
<ul>
  <li>אי-תשלום קרן או ריבית במועד (Payment Default) — לרוב עם חסד של 3–5 ימי עסקים.</li>
  <li>הפרת Covenant — לרוב עם תקופת ריפוי (Cure Period) של 30–60 ימים.</li>
  <li>הפרת Representation מהותית.</li>
  <li>Cross-Default — הפרת הלוואה אחרת של הלווה (בסכום מעל סף מוגדר) גוררת Default גם כאן.</li>
  <li>Insolvency — הליכי חדלות פירעון, כינוס נכסים, פשיטת רגל.</li>
  <li>שינוי שליטה (Change of Control) — ללא הסכמת המלווה.</li>
  <li>נזק מהותי לנכס שאינו מכוסה בביטוח.</li>
</ul>

<h3>ו. סעדים ומנגנוני ריפוי (Remedy Provisions)</h3>
<p>
לאחר הכרזת Default, מה המלווה יכול לעשות? הסעיף מגדיר:
</p>
<ul>
  <li>
    <strong>Acceleration:</strong> דרישת פירעון מיידי של כל יתרת הקרן, הריבית וכל עמלה
    תלויה — ביום אחד.
  </li>
  <li>
    <strong>Enforcement of Security:</strong> מימוש הבטוחות — כינוס נכסים, מינוי כונס,
    מכירה בבית המשפט.
  </li>
  <li>
    <strong>Cure Period:</strong> תקופה שניתנת ללווה לתקן את ההפרה לפני שהמלווה מפעיל
    את סעדיו — תנאי חיוני שיש לבדוק בכל הסכם.
  </li>
  <li>
    <strong>Waiver vs. Default:</strong> המלווה רשאי לוותר (Waive) על הפרה ספציפית — ויתור
    אינו מהווה תקדים לעתיד (לרוב ישנה הוראה מפורשת בהסכם על כך).
  </li>
</ul>

<h2>כיצד אנליסט קורא הסכם הלוואה — מתודולוגיה</h2>

<p>
אנליסטים מנוסים אינם קוראים הסכם הלוואה מהתחלה לסוף. הם קוראים בסדר אסטרטגי:
</p>
<ol>
  <li><strong>Events of Default ראשון</strong> — מה "מוריד" את ההלוואה? מה תקופות הריפוי?</li>
  <li><strong>Financial Covenants שני</strong> — מה הרף המספרי? איך מחושב? כמה "מרחב" יש ללווה?</li>
  <li><strong>Conditions Precedent שלישי</strong> — מה כבר מולא ומה עדיין תלוי?</li>
  <li><strong>Representations רביעי</strong> — האם יש הצהרות לא-ריאליסטיות שיוצרות Default טכני?</li>
  <li><strong>Definitions חמישי</strong> — לחזור לפרק ההגדרות כשצורך בדיוק.</li>
</ol>

<h2>סעיף לדוגמה — Event of Default עם ניתוח</h2>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:14px 18px;font-family:monospace;margin:16px 0;direction:rtl;">
<strong>סעיף 18.1(ג) — הפרת Covenant פיננסי</strong><br><br>
"יראו את הלווה כמי שנמצא באירוע ברירת מחדל אם, בתום רבעון כלשהו, יחס ה-DSCR
כמחושב בהתאם לנספח ד' יהיה נמוך מ-1.15, בתנאי שהמלווה שלח הודעה בכתב ללווה
ולווה לא ריפא את ההפרה תוך 45 יום ממועד קבלת ההודעה."<br><br>
<strong>ניתוח:</strong> ה-DSCR המינימלי הוא 1.15 (לא 1.20 הסטנדרטי — נוחות גדולה יותר ללווה).
תקופת ריפוי של 45 יום — זמן סביר. שים לב: ה"ריפוי" עשוי לכלול הזרמת הון, הגדלת
שכירויות או מחזור חוב — על הלווה להוכיח ריפוי בפועל, לא רק הבטחה.
</div>

<h2>רגולציה ישראלית — הוראות בנק ישראל</h2>

<p>
בנק ישראל מסדיר את תנאי האשראי הבנקאי לנדל"ן דרך מספר הוראות מרכזיות:
</p>
<ul>
  <li>
    <strong>הוראת ניהול בנקאי תקין 329:</strong> מגדירה את מדיניות האשראי לנדל"ן ומציבה
    רף LTV מרבי של 60%–70% לפי סוג הנכס והלווה.
  </li>
  <li>
    <strong>הוראת 311 (סיכוני שוק):</strong> מחייבת בנקים לבצע בדיקות לחץ (Stress Tests)
    על תיקי האשראי שלהם — כולל תרחישי ירידת שווי נכסים.
  </li>
  <li>
    <strong>דרישות DSCR בנקאיות:</strong> רוב הבנקים הגדולים בישראל דורשים DSCR ≥ 1.20
    בנכסים מניבים; בנכסים ייזום DSCR נבחן לאחר יציבות הנכס (Stabilized DSCR).
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>טיפ מקצועי — קרא Events of Default לפני הכל:</strong><br>
  כאשר מוסרים לך הסכם הלוואה לניתוח, עמוד ראשון לקרוא הוא Events of Default — לא
  הגדרות, לא ריביות. ה-Events of Default מגדירים את "הקווים האדומים" של הלווה.
  רק לאחר שהבנת מה מפיל את ההלוואה — תוכל להעריך את סיכון הכשל האמיתי של העסקה.
  <br><br>
  <strong>הסכם הלוואה אינו קריאת ספר — הוא מסמך ניתוח. זהה את הסעיפים הקריטיים ועבוד
  מהם לאחור.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 1 — Comprehension HTML
# ---------------------------------------------------------------------------

M1_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על הסכם הלוואה — בחן את הבנתך לפני שממשיכים.
השאלות בוחנות את שישת הפרקים המרכזיים בהסכם, את מתודולוגיית הקריאה האנליטית,
זיהוי Conditions Precedent ואירועי ברירת מחדל.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Exercises HTML
# ---------------------------------------------------------------------------

M1_EXERCISES_HTML = """
<p>
5 תרגילים על הסכם הלוואה. התרגילים כוללים זיהוי פרק ראשון לקריאה בתרחיש נתון,
ניתוח סעיף Event of Default עם תקופת ריפוי, בחינת Condition Precedent שטרם מולא,
השוואת הצהרה (Representation) לנתון שהסתבר כשקרי — וכיצד מופעל סעד ה-Acceleration.
</p>
"""


# ---------------------------------------------------------------------------
# Module 1 — Summary HTML
# ---------------------------------------------------------------------------

M1_SUMMARY_HTML = """
<h2>סיכום מודול 1 — הסכם הלוואה: מבנה, רכיבים וסעיפים קריטיים</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>ששת הפרקים:</strong> הגדרות → Conditions Precedent → Representations &amp; Warranties
    → Financial Covenants → Events of Default → Remedy Provisions. כל פרק "שומר" על שלב
    אחר במחזור חיי ההלוואה.
  </li>
  <li>
    <strong>Conditions Precedent:</strong> השערים שחייבים להיפתח לפני שחרור כסף. ויתור על
    תנאי מקדים (Waiver) הוא אות אזהרה — גדר שהורדה, חשיפה שגדלה.
  </li>
  <li>
    <strong>Representations &amp; Warranties:</strong> הצהרות עובדתיות של הלווה שאם יתבררו
    כשקריות — יוצרות Event of Default. מחודשות בכל משיכה ולרוב בכל רבעון.
  </li>
  <li>
    <strong>Events of Default:</strong> הפרק הראשון שאנליסט קורא. מגדיר את "הקווים האדומים"
    ואת תקופות הריפוי — המרחב שיש ללווה לתקן לפני הפעלת סעדים.
  </li>
  <li>
    <strong>מתודולוגיית קריאה:</strong> Events of Default → Covenants → CPs → Representations
    → Definitions. קריאה אסטרטגית, לא ליניארית — כך עובד אנליסט מנוסה.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
ראינו שה-Financial Covenants הם מנגנון מרכזי בהסכם ההלוואה. <em>מודול 2</em> יצלול
לעומק ל-Covenants: סוגיהם, חישובם, מה קורה בהפרה — וכיצד אנליסט מחשב "מרחב ראש"
(Headroom) לפני שמגיעים לקו האדום.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Reading HTML (Covenants — אמות מידה פיננסיות וסעיפי הגבלה)
# ---------------------------------------------------------------------------

M2_READING_HTML = """
<h2>Covenants — הגדר הפיננסית של ההלוואה</h2>

<p>
Covenants הם ההתחייבויות המתמשכות שהלווה לוקח על עצמו לאורך כל חיי ההלוואה — לא רק
בחתימה. הם מאפשרים למלווה לעקוב אחר בריאות העסקה ולהתרעם בשלב מוקדם — לפני שמגיעים
לכשל פירעון. הבנת ה-Covenants היא אחד הכישורים הקריטיים ביותר של אנליסט אשראי בנדל"ן.
</p>

<h2>שני סוגי Covenants — Maintenance vs. Incurrence</h2>

<h3>Maintenance Covenants — בדיקה תקופתית שוטפת</h3>
<p>
<strong>Maintenance Covenants</strong> נבדקים באופן קבוע — רבעוני, חצי-שנתי, או שנתי —
ללא קשר לאירוע ספציפי. הלווה חייב לעמוד בהם תמיד. אם יחס מסוים נפל מתחת לרף — זה
Covenant Breach, ללא קשר למה גרם לנפילה.
</p>
<p>
<strong>דוגמאות:</strong> LTV מקסימלי, DSCR מינימלי, ICR מינימלי — כולם Maintenance.
מנגנון בדיקה: הלווה מגיש Compliance Certificate בסוף כל תקופה, חתום על-ידי CFO.
</p>

<h3>Incurrence Covenants — מופעלים רק בעת פעולה ספציפית</h3>
<p>
<strong>Incurrence Covenants</strong> אינם נבדקים שוטף — הם מופעלים רק כאשר הלווה
מבצע פעולה מסוימת: לקיחת חוב נוסף, חלוקת דיבידנד, ביצוע השקעה גדולה, מכירת נכס.
לפני הפעולה, הלווה חייב להוכיח שהיחסים עדיין עומדים בדרישה.
</p>
<p>
<strong>דוגמה:</strong> "הלווה לא יחלק דיבידנד אלא אם DSCR (כמחושב Pro Forma לאחר החלוקה)
יעלה על 1.30." זה Incurrence — נבדק רק אם הלווה מבקש לחלק דיבידנד.
</p>

<h2>LTV Covenant — חישוב, הפרה וריפוי</h2>

<h3>חישוב LTV Covenant:</h3>
<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
LTV = יתרת הלוואה ÷ שווי נכס (לפי שמאות עדכנית)<br><br>
דוגמה:<br>
  יתרת הלוואה: 55,000,000 ₪<br>
  שמאות עדכנית: 85,000,000 ₪<br>
  LTV = 55M ÷ 85M = 64.7% — בתוך הרף (מקסימום 65%)<br><br>
  שנה הבאה — שמאות ירדה ל-78,000,000 ₪:<br>
  LTV = 55M ÷ 78M = 70.5% — הפרת Covenant!
</div>

<h3>מנגנוני ריפוי LTV Breach — שלוש אפשרויות:</h3>
<ul>
  <li>
    <strong>Cash Sweep:</strong> הלווה מפקיד סכום מזומן בחשבון עירבון (Escrow) שמנוהל על-ידי
    המלווה עד לשיפור שווי הנכס. המזומן "מוריד" את ה-LTV האפקטיבי.
  </li>
  <li>
    <strong>Partial Prepayment:</strong> הלווה פורע חלק מהקרן — מקטין את מונה ה-LTV.
    לרוב ללא קנס פירעון מוקדם (Prepayment Penalty) כאשר הוא נעשה כריפוי Covenant.
  </li>
  <li>
    <strong>Additional Security:</strong> הלווה מספק בטוחה נוספת (נכס אחר, ערבות) שמחזירה
    את ה-LTV האפקטיבי לרף. נדיר יחסית — מצריך הסכמת המלווה ובדיקת שמאות על הבטוחה הנוספת.
  </li>
</ul>

<h2>DSCR Covenant — חישוב מפורט</h2>

<h3>נוסחה בסיסית:</h3>
<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
DSCR = NOI שנתי ÷ שירות חוב שנתי (קרן + ריבית)<br><br>
NOI (Net Operating Income) כולל:<br>
  (+) הכנסות שכירות ברוטו<br>
  (+) הכנסות חנייה, אנטנות ושירותים<br>
  (−) שיעור פנויות (Vacancy Rate) — בדרך כלל מניחים 5%–10%<br>
  (−) הוצאות תפעול (ניהול, תחזוקה, ביטוח, ארנונה שאינה על השוכר)<br>
  (−) CapEx שוטף (Replacement Reserve) — בדרך כלל 1%–2% מה-NOI<br>
= NOI נקי המשמש לחישוב DSCR<br><br>
NOI אינו כולל:<br>
  (×) פחת ואמורטיזציה (לא תזרימי)<br>
  (×) הוצאות מימון (ריבית) — שהן המכנה<br>
  (×) מס הכנסה — נבחן לפני מס ברוב ההסכמים הישראליים
</div>

<h3>דוגמה — חישוב DSCR ותרחיש הפרה:</h3>
<div style="background:#f0f7ff;border-right:5px solid #1976d2;padding:14px 18px;margin:16px 0;border-radius:4px;">
<strong>נתוני הנכס:</strong><br>
שכירות ברוטו שנתית: 7,200,000 ₪<br>
שיעור פנויות: 8% → הפסד: 576,000 ₪<br>
הוצאות תפעול: 1,100,000 ₪<br>
Replacement Reserve: 90,000 ₪<br>
<strong>NOI נקי: 7,200,000 − 576,000 − 1,100,000 − 90,000 = 5,434,000 ₪</strong><br><br>
<strong>שירות חוב שנתי:</strong><br>
קרן (Amortization): 800,000 ₪<br>
ריבית (Prime+2% על 50M₪): 3,750,000 ₪<br>
<strong>שירות חוב: 4,550,000 ₪</strong><br><br>
<strong>DSCR = 5,434,000 ÷ 4,550,000 = 1.194</strong><br><br>
Covenant מינימלי: 1.20 → <strong>הפרת Covenant!</strong><br>
מרחק מהפרה (Headroom): 1.194 − 1.20 = −0.006 → Breach של 0.5%<br><br>
<strong>ריפוי אפשרי:</strong> הגדלת הכנסות שכירות ב-~35,000 ₪ (חדר נוסף, חנייה) תחזיר
את ה-DSCR מעל 1.20.
</div>

<h2>ICR — Interest Coverage Ratio</h2>

<p>
<strong>ICR (Interest Coverage Ratio)</strong> בוחן רק את יכולת הנכס לכסות את הריבית —
ללא הקרן. הוא פחות שמרני מ-DSCR אך שימושי בהלוואות Bullet שאין בהן החזר קרן שוטף.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
ICR = NOI ÷ הוצאות ריבית שנתיות<br><br>
דוגמה: NOI = 5,434,000 ₪; ריבית שנתית = 3,750,000 ₪<br>
ICR = 5,434,000 ÷ 3,750,000 = 1.449<br><br>
Covenant מינימלי: 1.30 → ICR עומד בדרישה (פחות קפדנית מ-DSCR).
</div>

<h2>Covenant Headroom — מרחב הביטחון</h2>

<p>
<strong>Headroom</strong> הוא המרחק בין ה-Covenant הנוכחי לבין הרף. הוא מדד הסיכון המוביל
של האנליסט: Headroom נמוך = קרוב לקצה = אות אזהרה.
</p>

<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;">
Headroom (DSCR) = DSCR בפועל − DSCR מינימלי<br><br>
דוגמה: DSCR בפועל 1.35; מינימום 1.20<br>
Headroom = 1.35 − 1.20 = 0.15 = 15 נקודות בסיס<br><br>
פרשנות:<br>
  Headroom > 0.20 = נוח (ירידת NOI של 15%+ לפני הפרה)<br>
  Headroom 0.10–0.20 = מוגבל — דורש מעקב<br>
  Headroom < 0.10 = אזהרה — עסקה על הקצה
</div>

<h2>מה קורה בהפרת Covenant — Waiver vs. Default</h2>

<p>
לא כל הפרת Covenant מסתיימת ב-Acceleration. בפועל, מלווים מעדיפים לעבוד עם הלווה
ולא לממש בטוחות — מימוש הוא הליך יקר, ארוך ולעיתים מניב פחות ממה שציפו.
</p>

<ul>
  <li>
    <strong>Waiver (ויתור):</strong> המלווה מוותר על הפרה ספציפית תמורת תנאים — לרוב
    Fee, שיפור בטחונות, תוכנית תיקון. Waiver ניתן בכתב ואינו יוצר תקדים לעתיד.
  </li>
  <li>
    <strong>Amendment (תיקון):</strong> שינוי קבוע ברף ה-Covenant — למשל הורדת DSCR
    מינימלי מ-1.20 ל-1.10. לרוב דורש Fee ולעיתים שיפור בטחונות.
  </li>
  <li>
    <strong>Default &amp; Acceleration:</strong> אם הלווה לא ריפא ולא קיבל Waiver — המלווה
    מכריז Default ודורש פירעון מיידי. משפעיל גם Cross-Default בהלוואות אחרות.
  </li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>אזהרה — Covenant Breach ≠ כשל מיידי:</strong><br>
  הפרת Covenant היא אות אזהרה מוקדמת — לא כשל מיידי. הפרה פותחת Cure Period שבמהלכה
  הלווה יכול לתקן. אנליסט טוב מזהה Headroom נמוך <em>לפני</em> ההפרה — ומסמן את העסקה
  למעקב הדוק. <strong>Covenant אינו סף מוות — הוא מנגנון התרעה מוקדמת. השתמש בו ככזה.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 2 — Comprehension HTML
# ---------------------------------------------------------------------------

M2_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על Covenants — בחן את יכולתך לחשב DSCR, לזהות הפרת Covenant,
להבחין בין Maintenance ל-Incurrence Covenants ולהסביר את אפשרויות ריפוי LTV Breach.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Exercises HTML
# ---------------------------------------------------------------------------

M2_EXERCISES_HTML = """
<p>
5 תרגילים על Covenants. התרגילים כוללים חישוב DSCR מנתוני NOI ושירות חוב,
זיהוי הפרת LTV Covenant לאחר ירידת שמאות, חישוב Headroom ופרשנותו,
הבחנה בין Maintenance ל-Incurrence בסעיף נתון, ובחינת תרחיש Waiver vs. Default.
</p>
"""


# ---------------------------------------------------------------------------
# Module 2 — Summary HTML
# ---------------------------------------------------------------------------

M2_SUMMARY_HTML = """
<h2>סיכום מודול 2 — Covenants: אמות מידה פיננסיות וסעיפי הגבלה</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>Maintenance vs. Incurrence:</strong> Maintenance נבדק שוטף — הלווה חייב לעמוד
    תמיד. Incurrence מופעל רק בפעולה ספציפית (דיבידנד, חוב נוסף). הבחנה קריטית לניתוח
    סיכון הפרה.
  </li>
  <li>
    <strong>LTV Covenant:</strong> יתרת הלוואה ÷ שמאות עדכנית. הפרה מאפשרת שלושה ריפויים:
    Cash Sweep, Partial Prepayment, Additional Security. ירידת שמאות היא טריגר הנפוץ ביותר.
  </li>
  <li>
    <strong>DSCR — החישוב:</strong> NOI נקי (כולל שיעור פנויות ו-CapEx) ÷ שירות חוב (קרן +
    ריבית). אינו כולל פחת, מס, או הוצאות מימון. הרף הסטנדרטי: DSCR ≥ 1.20.
  </li>
  <li>
    <strong>Covenant Headroom:</strong> המרחק בין הנוכחי לרף. Headroom מתחת ל-0.10 = אות
    אזהרה. אנליסט טוב מזהה Headroom נמוך לפני שהוא הופך להפרה — ומסמן מעקב.
  </li>
  <li>
    <strong>Waiver vs. Default:</strong> Waiver = המלווה מוותר על הפרה בכתב בתנאים;
    Default = הכרזה רשמית ו-Acceleration. מלווים מעדיפים Waiver — מימוש בטוחות יקר ומסוכן.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
דנו בהסכם ההלוואה ובה-Covenants שמגינים על המלווה לאורך חיי ההלוואה. <em>מודול 3</em>
יעסוק ב<strong>מסמכי הביטחונות הפיזיים</strong> — מסמכי השיעבוד, נסח הטאבו, שטר החוב
והערבות — כיצד קוראים אותם, ומה מחפשים בהם כדי לאמת שהמלווה אכן מוגן.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Reading HTML (מסמכי שיעבוד ובטחונות — קריאה ופרשנות)
# ---------------------------------------------------------------------------

M3_READING_HTML = """
<h2>מסמכי שיעבוד ובטחונות — הכלים המשפטיים של הגבייה</h2>

<p>
הסכם ההלוואה מגדיר את הזכויות — אך מסמכי הביטחונות הם שמאפשרים את אכיפתן. בלי שיעבוד
רשום, ערבות חתומה ושטר חוב תקף, המלווה אינו יותר מנושה כללי — ממתין בתור ארוך. מסמכי
הביטחונות הם הכוח שמבדל את המלווה המאובטח מן הנושה הרגיל.
</p>

<h2>סוגי מסמכי שיעבוד בישראל</h2>

<h3>א. משכון על מקרקעין — רישום בטאבו</h3>
<p>
<strong>משכון על מקרקעין</strong> (Mortgage / Hypothec) הוא השיעבוד הנפוץ ביותר בעסקאות
נדל"ן — זכות בטחון קניינית הרשומה בלשכת רישום המקרקעין (טאבו). הוא "עוקב" אחר הנכס
ללא קשר לזהות הבעלים.
</p>
<ul>
  <li><strong>רישום:</strong> בטאבו, בצו בית משפט או בהסכם שיש להגישו לרישום. ללא רישום —
  אין קדימות קניינית.</li>
  <li><strong>Follow the Asset:</strong> גם אם הנכס נמכר ללא מחיקת השיעבוד, הוא מחייב את
  הרוכש החדש.</li>
  <li><strong>מימוש:</strong> כינוס נכסים, מכירה בהוראת בית משפט, מינוי כונס.</li>
</ul>

<h3>ב. רחוב ראשונה / שנייה (First Charge / Second Charge)</h3>
<p>
<strong>שיעבוד ראשון (First Charge)</strong> קודם לכל שיעבוד אחר שנרשם מאוחר יותר. כלל
ה"נמו דאט" (Nemo Dat) חל — "אינך יכול להעניק יותר ממה שיש לך". המוכר/משעבד אינו יכול
לתת שיעבוד ראשון לשני גורמים שונים.
</p>
<p>
<strong>שיעבוד שני (Second Charge)</strong> נרשם לאחר הראשון — מקבל תמורת מימוש רק לאחר
שה-First Charge נפרע במלואו. סיכון גבוה יותר, ולכן נדיר בנדל"ן מניב (נפוץ יותר
ב-Mezzanine וב-Bridge Financing).
</p>

<h3>ג. שטר חוב (Shtar Hov / Promissory Note)</h3>
<p>
<strong>שטר חוב</strong> הוא מסמך ניתן להסבה (Negotiable Instrument) שבו הלווה מתחייב
לשלם סכום מסוים למלווה (או לכל מי שיהיה המחזיק). שטר חוב מוסיף לאמצעי הגבייה:
</p>
<ul>
  <li>
    <strong>הסבה (Negotiability):</strong> המלווה יכול להעביר ("להסב") את שטר החוב לצד
    שלישי — הצד השלישי נהיה נושה ישיר. מאפשר הסחרה של חוב.
  </li>
  <li>
    <strong>הוצאה לפועל מהירה:</strong> שטר חוב מאפשר גבייה ישירה בהוצאה לפועל ללא
    צורך בפסק דין נפרד — מהיר יותר מתביעה רגילה.
  </li>
  <li>
    <strong>פרטי שטר חוב:</strong> סכום, שם הלווה (עושה השטר), שם המלווה (הנפרע),
    מועד פירעון, חתימה. ללא פרטים מדויקים — השטר עשוי להיות בטל.
  </li>
</ul>

<h3>ד. ערבות (Aravut / Guarantee)</h3>
<p>
<strong>ערבות</strong> היא התחייבות של גורם שלישי (הערב) לפרוע את חוב הלווה אם הלווה
אינו מסוגל. בישראל מוסדרת בחוק הערבות, תשכ"ז-1967. שלושה סוגים עיקריים:
</p>
<ul>
  <li>
    <strong>ערבות פשוטה:</strong> המלווה חייב לתבוע תחילה את הלווה — רק אחרי כישלון
    הגבייה יכול לפנות לערב. מגנה יותר על הערב.
  </li>
  <li>
    <strong>ערבות עצמאית (Autonomous Guarantee):</strong> המלווה יכול לדרוש מהערב פירעון
    מיידי — ללא צורך לתבוע תחילה את הלווה. הגנה חזקה יותר למלווה.
  </li>
  <li>
    <strong>ערבות מוגבלת (Capped Guarantee):</strong> הערב אחראי רק עד סכום מוגדר —
    לרוב ב-Corporate Guarantees. מגבילה חשיפת חברת האם.
  </li>
</ul>

<h2>קריאת נסח טאבו — מדריך מעשי</h2>

<p>
<strong>נסח טאבו</strong> הוא תעודת זהות של הנכס — מציג את הבעלות, הזכויות, העיקולים
והשיעבודים הרשומים. כל אנליסט חייב לדעת לקרוא נסח טאבו.
</p>

<h3>חלקי נסח הטאבו:</h3>
<ul>
  <li>
    <strong>פרק א — זיהוי הנכס:</strong> גוש, חלקה, תת-חלקה (דירה בבניין). כתובת, שטח
    רשום, סוג הנכס. חשוב לאמת שמדובר בנכס הנכון!
  </li>
  <li>
    <strong>פרק ב — הבעלות:</strong> שם הבעלים הרשום, חלקו (100% / 50% / שליש וכו').
    אם יש בעלים משותפים — כולם חייבים לחתום על כל שיעבוד.
  </li>
  <li>
    <strong>פרק ג — זכויות אחרות:</strong> זיקות הנאה (Easements), שכירויות ארוכות טווח
    שנרשמו, זכויות קדימה רשומות. אלה עשויות להגביל את שווי הנכס ואת יכולת המימוש.
  </li>
  <li>
    <strong>פרק ד — משכנתאות ושיעבודים:</strong> כל שיעבוד רשום — שם המשעבד, שם
    המוטב (המלווה), סכום, תאריך רישום. זה הפרק הקריטי לאנליסט אשראי.
  </li>
  <li>
    <strong>הערות:</strong> עיקולים, צווי בית משפט, הגבלות רישום. הערה "אזהרת קונה"
    מאפשרת לגורם שלישי (כגון רוכש דירה על הנייר) לרשום את זכותו — חשוב לזהות!
  </li>
</ul>

<h3>כיצד לקרוא שיעבוד רשום בפרק ד:</h3>
<div style="background:#f4f6f8;border-right:4px solid #1a2638;padding:12px 16px;font-family:monospace;margin:12px 0;direction:rtl;">
<strong>דוגמה — נסח טאבו, פרק ד:</strong><br><br>
מספר רשומה: 15<br>
סוג הרישום: משכנתא<br>
לטובת: בנק הפועלים בע"מ<br>
סכום: 45,000,000 ₪<br>
מטבע: שקל<br>
תאריך רישום: 15/03/2022<br>
הערות: שעבוד דרגה ראשונה<br><br>
<strong>קריאה:</strong> בנק הפועלים רשום כמחזיק משכנתא ראשונה של 45M₪ מ-2022.
אם אנחנו המלווה השני — אנחנו Second Charge. לפני כל מימוש, 45M₪ + ריבית
ייגבו לטובת בנק הפועלים. רק מה שנותר מגיע אלינו.
</div>

<h2>כלל הקדימות — Prior Registered Interest Prevails</h2>

<p>
<strong>כלל יסוד:</strong> שיעבוד שנרשם קודם קודם בגבייה. תאריך הרישום, לא תאריך
ההסכם, הוא הקובע. מי שנרשם ראשון — גובה ראשון.
</p>

<p>
<strong>השלכה מעשית:</strong> אם בנק מסחרי רשם שיעבוד ב-2021 ואתה מלווה חדש ב-2024,
הבנק הוא First Charge ואתה Second Charge — גם אם לא ידעת על השיעבוד הישן. לכן
חובת האנליסט: לבדוק נסח טאבו עדכני לפני כל אישור הלוואה.
</p>

<h2>דגלים אדומים בנסח טאבו</h2>

<p>
אלה הממצאים שאמורים לעצור עסקה (או לפחות לדרוש הסבר מיידי):
</p>
<ul>
  <li><strong>שיעבוד לא ידוע:</strong> שיעבוד שהלווה לא גילה — סימן לחוסר גילוי מלא.</li>
  <li><strong>עיקול פעיל:</strong> צו עיקול מבית משפט — מצביע על הליכים משפטיים פעילים נגד הנכס.</li>
  <li><strong>הערת אזהרה לרוכש:</strong> רוכש על הנייר שרשם זכויות — מגביל את יכולת המכירה
  למימוש.</li>
  <li><strong>פגמי בעלות:</strong> בעלות חלקית לא-ידועה, ירושה שטרם הוסדרה, שותפות
  שאחד מחבריה חייב חובות.</li>
  <li><strong>זיקת הנאה מגבילה:</strong> זכות מעבר, זכות בנייה שניתנה לשכן — יכולה להפחית
  שווי שמאי ולהגביל מימוש.</li>
  <li><strong>שיעבוד ישן לא מחוק:</strong> שיעבוד שאמור היה להיות מחוק (ההלוואה נפרעה)
  אך עדיין מופיע. לדרוש אישור מחיקה בכתב.</li>
</ul>

<div style="background:#fff8e1;border-right:5px solid #f57c00;padding:14px 18px;margin:16px 0;border-radius:4px;">
  <strong>כלל זהב — בדוק נסח טאבו עדכני, לא ישן:</strong><br>
  נסח טאבו שמסר הלווה לפני שישה חודשים — חסר ערך. שיעבוד חדש יכול להירשם בין
  לילה. דרוש תמיד נסח טאבו שהופק לא יותר מ-14 ימים לפני תאריך הסגירה.
  <br><br>
  <strong>בדיקת נסח טאבו עדכני היא קו ההגנה הראשון של המלווה — אל תוותר עליה לעולם.</strong>
</div>
"""


# ---------------------------------------------------------------------------
# Module 3 — Comprehension HTML
# ---------------------------------------------------------------------------

M3_COMPREHENSION_HTML = """
<p>
4 שאלות הבנה על מסמכי שיעבוד ובטחונות — בחן את יכולתך לקרוא נסח טאבו,
לזהות סדר קדימות שיעבודים, להבחין בין סוגי הערבות ולאתר דגלים אדומים בפרק ד.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Exercises HTML
# ---------------------------------------------------------------------------

M3_EXERCISES_HTML = """
<p>
5 תרגילים על מסמכי ביטחונות. התרגילים כוללים קריאת נסח טאבו לדוגמה וזיהוי שיעבוד
קיים, קביעת סדר קדימות בין שני מלווים לפי תאריכי רישום, זיהוי דגלים אדומים
בנסח מובא, הבחנה בין ערבות פשוטה לעצמאית בתרחיש גבייה, ובחינת שטר חוב לאמות
בדיקה שהוא תקף וניתן לאכיפה.
</p>
"""


# ---------------------------------------------------------------------------
# Module 3 — Summary HTML
# ---------------------------------------------------------------------------

M3_SUMMARY_HTML = """
<h2>סיכום מודול 3 — מסמכי שיעבוד ובטחונות: קריאה ופרשנות</h2>

<h3>5 נקודות מפתח</h3>
<ol>
  <li>
    <strong>משכון על מקרקעין:</strong> השיעבוד הקנייני החזק ביותר — רשום בטאבו, עוקב אחר
    הנכס, מאפשר מימוש ישיר. First Charge קודם ל-Second Charge בגבייה תמיד.
  </li>
  <li>
    <strong>שטר חוב:</strong> מסמך ניתן להסבה המאפשר גבייה מהירה בהוצאה לפועל ללא
    פסק דין נפרד. סחיר — ניתן להעברה לצד שלישי. הפרטים חייבים להיות מדויקים.
  </li>
  <li>
    <strong>ערבות — שלושה סוגים:</strong> פשוטה (תחילה תבע לווה), עצמאית (תבע ערב ישירות),
    מוגבלת (עד סכום מוגדר). ערבות עצמאית היא הגנה חזקה יותר למלווה.
  </li>
  <li>
    <strong>קריאת נסח טאבו:</strong> פרק ד — שיעבודים ומשכנתאות — הוא הקריטי. שיעבוד
    שנרשם ראשון גובה ראשון. בדוק תאריך רישום, לא תאריך הסכם.
  </li>
  <li>
    <strong>דגלים אדומים:</strong> שיעבוד לא-גלוי, עיקול פעיל, הערת אזהרה לרוכש, בעלות
    חלקית ופגומה, שיעבוד ישן שלא נמחק. כל אחד מהם דורש הסבר מיידי — לא להתקדם בלעדיו.
  </li>
</ol>

<h3>גשר למודול הבא</h3>
<p>
סיימנו את שלושת המודולים הראשונים של קורס 8 — הסכם הלוואה, Covenants ומסמכי ביטחונות.
<em>מודול 4</em> ייקח את הידע הזה לשלב הבא: <strong>קריאת חוזי שכירות</strong> — כיצד
אנליסט בוחן הכנסות נכס מניב, מזהה שוכרים בסיכון, ומעריך יציבות תזרים לטווח ארוך.
</p>
"""


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = (
        "Seeds Module 1-3 reading and summary content for Course 8 "
        "(ניתוח מסמכים משפטיים)"
    )

    def handle(self, *args, **options) -> None:
        # ── Locate Course 8 ───────────────────────────────────────────────
        try:
            course = Course.objects.get(course_number=8)
        except Course.DoesNotExist:
            raise CommandError(
                "Course with course_number=8 not found. "
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
            self.style.SUCCESS("\nAll done — Course 8 modules 1-3 seeded successfully.")
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
