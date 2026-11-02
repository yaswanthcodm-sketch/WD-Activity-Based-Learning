import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = "/Users/yaswanth/.gemini/antigravity/scratch/WD-Activity-Based-Learning"
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Load fonts
font_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 20)
font_h2 = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 16)
font_h3 = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 13)
font_body = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 12)
font_sub = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 11)
font_bold_sm = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 11)
font_tab = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 12)
font_mono = ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 11)

def draw_browser_chrome(draw, w, h, title, url):
    # Header chrome background
    draw.rectangle([0, 0, w, 70], fill='#e2e8f0')
    # Window action buttons (red, yellow, green)
    draw.ellipse([16, 14, 28, 26], fill='#ef4444')
    draw.ellipse([36, 14, 48, 26], fill='#f59e0b')
    draw.ellipse([56, 14, 68, 26], fill='#10b981')
    
    # Active Tab
    draw.rectangle([85, 8, 380, 40], fill='#ffffff')
    draw.text((105, 17), title, fill='#1e293b', font=font_tab)
    draw.text((360, 16), "✕", fill='#94a3b8', font=font_tab)
    
    # Address bar
    draw.rectangle([0, 40, w, 70], fill='#ffffff')
    draw.line([0, 70, w, 70], fill='#cbd5e1', width=1)
    draw.text((20, 48), "🔒", fill='#10b981', font=font_body)
    draw.rectangle([50, 44, w - 30, 66], fill='#f1f5f9')
    draw.text((65, 48), url, fill='#334155', font=font_body)

# ==========================================
# 1. Academic Dashboard Preview
# ==========================================
def render_academic_dashboard():
    w, h = 1200, 760
    img = Image.new('RGB', (w, h), color='#f8fafc')
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, h, "Student Academic Dashboard - Dr. RVR NRIIT", "http://localhost:5500/academic-dashboard/")
    
    # Sidebar
    draw.rectangle([0, 71, 260, h], fill='#0f172a')
    draw.text((25, 95), "🎓  NRIIT ACADEMICS", fill='#ffffff', font=font_h2)
    draw.text((25, 120), "Deemed to be University", fill='#94a3b8', font=font_sub)
    
    # User Profile card in sidebar
    draw.rectangle([15, 145, 245, 215], fill='#1e293b', outline='#334155')
    draw.ellipse([28, 157, 68, 197], fill='#3b82f6')
    draw.text((38, 168), "YA", fill='#ffffff', font=font_h3)
    draw.text((78, 156), "Yaswanth Avirneni", fill='#ffffff', font=font_bold_sm)
    draw.text((78, 172), "Roll No: 26000918", fill='#94a3b8', font=font_sub)
    draw.rectangle([78, 188, 170, 204], fill='#065f46')
    draw.text((85, 190), "Active • CSM-1", fill='#34d399', font=font_sub)
    
    # Nav items
    navs = ["📊  Overview", "📈  Attendance Tracker", "📝  Semester Results", "📅  Exam Schedule", "📢  Notice Board"]
    y_nav = 235
    for i, n in enumerate(navs):
        if i == 0:
            draw.rectangle([15, y_nav - 4, 245, y_nav + 26], fill='#2563eb')
            draw.text((30, y_nav), n, fill='#ffffff', font=font_bold_sm)
        else:
            draw.text((30, y_nav), n, fill='#94a3b8', font=font_body)
        y_nav += 36

    # Main area banner
    draw.rectangle([285, 95, w - 25, 200], fill='#1e3a8a')
    draw.text((315, 115), "STUDENT ACADEMIC PORTAL • CASE STUDY 4", fill='#93c5fd', font=font_bold_sm)
    draw.text((315, 135), "Welcome back, Yaswanth Avirneni!", fill='#ffffff', font=font_title)
    draw.text((315, 168), "Track your academic performance, subject attendance thresholds, semester grades, and notices.", fill='#e0e7ff', font=font_body)
    
    # Quick KPI cards
    kpis = [
        ("REGISTERED CREDITS", "21 / 21 Cr", "100% Core Load Complete", '#eff6ff', '#1d4ed8'),
        ("CUMULATIVE ATTENDANCE", "88.5%", "✓ Eligible for End Exams", '#f0fdf4', '#15803d'),
        ("CURRENT SGPA", "9.36 / 10.0", "Top 5% in Section CSM-1", '#faf5ff', '#7e22ce'),
        ("UPCOMING EXAMS", "Mid-Term II", "Commencing Nov 16", '#fff7ed', '#c2410c')
    ]
    x_kpi = 285
    for lbl, val, sub, bg, txt in kpis:
        draw.rectangle([x_kpi, 215, x_kpi + 210, 290], fill=bg, outline='#cbd5e1')
        draw.text((x_kpi + 15, 225), lbl, fill='#64748b', font=font_sub)
        draw.text((x_kpi + 15, 242), val, fill=txt, font=font_h2)
        draw.text((x_kpi + 15, 268), sub, fill='#475569', font=font_sub)
        x_kpi += 228
        
    # Section: Attendance Progress Bars
    draw.rectangle([285, 305, w - 25, 470], fill='#ffffff', outline='#e2e8f0')
    draw.text((305, 320), "Subject-wise Attendance Percentages (Mandatory Threshold: 75%)", fill='#0f172a', font=font_h3)
    
    subjects = [
        ("Web Development Fundamentals (26CS101)", "92%", 92, '#10b981'),
        ("Data Structures & Algorithms (26CS102)", "88%", 88, '#10b981'),
        ("Python for Machine Learning (26AI101)", "94%", 94, '#10b981'),
        ("Discrete Mathematical Structures (26BS103)", "82%", 82, '#f59e0b'),
        ("Applied Physics & Optoelectronics (26BS104)", "86%", 86, '#10b981'),
        ("Web Development & UI/UX Lab (26CS105L)", "96%", 96, '#10b981')
    ]
    
    y_sub = 350
    for s_name, pct_str, pct_val, col in subjects:
        draw.text((305, y_sub), s_name, fill='#1e293b', font=font_body)
        draw.text((w - 90, y_sub), pct_str, fill=col, font=font_bold_sm)
        # Bar bg
        draw.rectangle([305, y_sub + 18, w - 50, y_sub + 25], fill='#e2e8f0')
        # Fill
        bar_len = int((w - 50 - 305) * (pct_val / 100))
        draw.rectangle([305, y_sub + 18, 305 + bar_len, y_sub + 25], fill=col)
        y_sub += 36

    # Section: Semester Results Table Preview
    draw.rectangle([285, 485, w - 25, 740], fill='#ffffff', outline='#e2e8f0')
    draw.text((305, 500), "Semester Academic Results & Grade Sheet (SGPA: 9.36 • Outstanding)", fill='#0f172a', font=font_h3)
    
    # Table Header
    draw.rectangle([305, 525, w - 45, 550], fill='#f1f5f9')
    draw.text((315, 532), "CODE", fill='#475569', font=font_bold_sm)
    draw.text((395, 532), "COURSE TITLE", fill='#475569', font=font_bold_sm)
    draw.text((680, 532), "CREDITS", fill='#475569', font=font_bold_sm)
    draw.text((770, 532), "INTERNAL (40)", fill='#475569', font=font_bold_sm)
    draw.text((880, 532), "EXTERNAL (60)", fill='#475569', font=font_bold_sm)
    draw.text((1000, 532), "GRADE", fill='#475569', font=font_bold_sm)
    draw.text((1080, 532), "STATUS", fill='#475569', font=font_bold_sm)
    
    rows = [
        ("26CS101", "Web Development Fundamentals", "3.0", "38", "56", "O (10.0)", "PASS"),
        ("26CS102", "Data Structures & Algorithms", "4.0", "36", "54", "O (10.0)", "PASS"),
        ("26AI101", "Python for Machine Learning", "3.0", "39", "57", "O (10.0)", "PASS"),
        ("26BS103", "Discrete Mathematical Structures", "4.0", "34", "51", "A+ (9.0)", "PASS"),
        ("26BS104", "Applied Physics & Optoelectronics", "3.0", "35", "53", "A+ (9.0)", "PASS"),
        ("26CS105L", "Web Development & UI/UX Lab", "1.5", "40", "58", "O (10.0)", "PASS")
    ]
    y_row = 560
    for code, title, cr, int_m, ext_m, grd, st in rows:
        draw.text((315, y_row), code, fill='#1d4ed8', font=font_mono)
        draw.text((395, y_row), title, fill='#0f172a', font=font_body)
        draw.text((695, y_row), cr, fill='#334155', font=font_body)
        draw.text((800, y_row), int_m, fill='#334155', font=font_body)
        draw.text((910, y_row), ext_m, fill='#334155', font=font_body)
        draw.text((1000, y_row), grd, fill='#15803d', font=font_bold_sm)
        draw.text((1085, y_row), st, fill='#10b981', font=font_bold_sm)
        draw.line([305, y_row + 22, w - 45, y_row + 22], fill='#f1f5f9', width=1)
        y_row += 28

    out_path = os.path.join(SCREENSHOTS_DIR, "academic_dashboard_preview.png")
    img.save(out_path)
    print("Saved:", out_path)

# ==========================================
# 2. E-Learning Platform Preview
# ==========================================
def render_elearning_platform():
    w, h = 1200, 760
    img = Image.new('RGB', (w, h), color='#f8fafc')
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, h, "EduPulse - NRIIT Online Learning Platform", "http://localhost:5500/elearning-platform/")
    
    # Top navbar
    draw.rectangle([0, 71, w, 125], fill='#ffffff', outline='#e2e8f0')
    draw.text((30, 88), "⚡ EduPulse", fill='#4f46e5', font=font_title)
    draw.text((155, 93), "NRIIT E-Learning Hub", fill='#64748b', font=font_sub)
    draw.rectangle([340, 83, 720, 115], fill='#f1f5f9', outline='#cbd5e1')
    draw.text((355, 90), "🔍 Search courses, instructors, tech stack...", fill='#94a3b8', font=font_body)
    draw.rectangle([w - 240, 83, w - 30, 115], fill='#f8fafc', outline='#cbd5e1')
    draw.text((w - 225, 91), "👤 Yaswanth Avirneni (CSM-1)", fill='#1e293b', font=font_bold_sm)
    
    # Hero section with active course progress
    draw.rectangle([0, 126, w, 310], fill='#312e81')
    draw.text((40, 145), "● ACTIVE LEARNING SESSION", fill='#34d399', font=font_bold_sm)
    draw.text((40, 170), "Advance Your Engineering Skills with Hands-on Courses", fill='#ffffff', font=font_title)
    draw.text((40, 205), "Curated curriculum by Dr. RVR NRIIT Faculty and Industry Architects.", fill='#c7d2fe', font=font_body)
    
    # Active course card in hero
    draw.rectangle([40, 235, w - 40, 298], fill='#1e1b4b', outline='#4338ca')
    draw.text((60, 246), "CONTINUE WATCHING: Full-Stack Modern Web Engineering", fill='#ffffff', font=font_h3)
    draw.text((60, 268), "Current Lesson: Module 4: Responsive CSS Flexbox & CSS Grid Mastery", fill='#a5b4fc', font=font_sub)
    draw.text((w - 280, 246), "68% Complete (18/26 Lessons)", fill='#34d399', font=font_bold_sm)
    # Progress bar
    draw.rectangle([60, 285, w - 60, 292], fill='#3730a3')
    draw.rectangle([60, 285, 60 + int((w - 120) * 0.68), 292], fill='#10b981')
    
    # Category filter pills
    cats = ["All Disciplines (6)", "Web Development (2)", "AI & Machine Learning (2)", "Data Structures (1)", "Cloud & DevOps (1)"]
    x_cat = 40
    for i, c in enumerate(cats):
        if i == 0:
            draw.rectangle([x_cat, 325, x_cat + 130, 355], fill='#4f46e5')
            draw.text((x_cat + 14, 333), c, fill='#ffffff', font=font_bold_sm)
            x_cat += 140
        else:
            draw.rectangle([x_cat, 325, x_cat + 155, 355], fill='#ffffff', outline='#cbd5e1')
            draw.text((x_cat + 12, 333), c, fill='#475569', font=font_body)
            x_cat += 165
            
    # Course Cards Grid (3 cards preview)
    courses = [
        ("Full-Stack Web Engineering", "Web Dev • Intermediate", "HTML5, CSS3, DOM & Responsive Grid", "Dr. S. Ramesh, Ph.D. (NRIIT CSE)", "★ 4.9 (1,240 students)", '#1e40af', '#3b82f6'),
        ("Python for Machine Learning", "AI & ML • Beginner", "NumPy, Pandas, Scikit-Learn Models", "Prof. K. Praveen Kumar (AI Head)", "★ 4.95 (2,180 students)", '#6b21a8', '#a855f7'),
        ("Algorithms & Problem Solving", "DSA • Intermediate", "Trees, Graphs, Dynamic Programming", "Dr. V. Nagasri, Ph.D. (Sr. Prof)", "★ 4.88 (1,840 students)", '#065f46', '#10b981')
    ]
    
    x_card = 40
    card_w = 360
    for title, cat, topics, inst, rating, c1, c2 in courses:
        # Card container
        draw.rectangle([x_card, 375, x_card + card_w, 715], fill='#ffffff', outline='#cbd5e1')
        # Thumbnail
        draw.rectangle([x_card, 375, x_card + card_w, 480], fill=c1)
        draw.ellipse([x_card + (card_w // 2) - 20, 405, x_card + (card_w // 2) + 20, 445], fill='#ffffff')
        draw.text((x_card + (card_w // 2) - 6, 415), "▶", fill=c1, font=font_h2)
        draw.text((x_card + card_w - 110, 455), "⏱️ 18h 45m", fill='#ffffff', font=font_sub)
        
        # Details
        draw.text((x_card + 16, 495), cat, fill='#4f46e5', font=font_bold_sm)
        draw.text((x_card + 16, 515), title, fill='#0f172a', font=font_h3)
        draw.text((x_card + 16, 538), topics, fill='#64748b', font=font_sub)
        
        # Objectives box
        draw.rectangle([x_card + 16, 560, x_card + card_w - 16, 615], fill='#f8fafc', outline='#e2e8f0')
        draw.text((x_card + 22, 566), "🎯 Objectives: Component architectures,", fill='#334155', font=font_sub)
        draw.text((x_card + 22, 582), "fluid layout systems, production deployment.", fill='#334155', font=font_sub)
        
        # Instructor & Rating
        draw.text((x_card + 16, 630), inst, fill='#1e293b', font=font_bold_sm)
        draw.text((x_card + 16, 650), rating, fill='#eab308', font=font_bold_sm)
        
        # Button
        draw.rectangle([x_card + 16, 672, x_card + card_w - 16, 702], fill='#4f46e5')
        draw.text((x_card + (card_w // 2) - 40, 680), "Enroll Now", fill='#ffffff', font=font_bold_sm)
        
        x_card += card_w + 30

    out_path = os.path.join(SCREENSHOTS_DIR, "elearning_platform_preview.png")
    img.save(out_path)
    print("Saved:", out_path)

# ==========================================
# 3. Hospital & Healthcare Services Preview
# ==========================================
def render_healthcare_portal():
    w, h = 1200, 760
    img = Image.new('RGB', (w, h), color='#f8fafc')
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, h, "NRIIT Care - Hospital & Healthcare Services", "http://localhost:5500/healthcare-portal/")
    
    # Emergency banner
    draw.rectangle([0, 71, w, 102], fill='#991b1b')
    draw.ellipse([25, 82, 35, 92], fill='#ef4444')
    draw.text((45, 78), "🚑 24/7 EMERGENCY & TRAUMA HELPLINE: Call +91 9640334422 or 1800-NRIIT-CARE | Free Campus Ambulance Support", fill='#ffffff', font=font_bold_sm)
    
    # Main nav
    draw.rectangle([0, 103, w, 158], fill='#ffffff', outline='#e2e8f0')
    draw.text((30, 118), "🏥 NRIIT CARE HOSPITAL", fill='#0369a1', font=font_title)
    draw.text((320, 125), "Super-Speciality Healthcare & Medical Research Center", fill='#64748b', font=font_sub)
    draw.text((w - 420, 122), "Departments    Specialists    Facilities    Visiting Hours", fill='#334155', font=font_bold_sm)
    draw.rectangle([w - 165, 112, w - 25, 148], fill='#0284c7')
    draw.text((w - 150, 122), "Book Appointment", fill='#ffffff', font=font_bold_sm)
    
    # Hero Banner
    draw.rectangle([0, 159, w, 335], fill='#0369a1')
    draw.text((40, 180), "✓ NABH & NABL ACCREDITED CENTER", fill='#6ee7b7', font=font_bold_sm)
    draw.text((40, 205), "Compassionate Healthcare Backed by Modern Medical Science", fill='#ffffff', font=font_title)
    draw.text((40, 240), "24/7 Emergency response, multi-specialty clinical care, advanced diagnostics & outpatient consultations.", fill='#e0f2fe', font=font_body)
    
    # Hero metric boxes
    metrics = [("24/7", "Trauma Care"), ("45+", "Specialist MDs"), ("100%", "ICU Ready"), ("128-Slice", "CT / 3T MRI")]
    x_m = 40
    for m1, m2 in metrics:
        draw.rectangle([x_m, 275, x_m + 160, 320], fill='#0c4a6e', outline='#0284c7')
        draw.text((x_m + 14, 282), m1, fill='#ffffff', font=font_h3)
        draw.text((x_m + 14, 302), m2, fill='#bae6fd', font=font_sub)
        x_m += 175
        
    # Departments showcase
    draw.text((40, 355), "SPECIALIZED CLINICAL DEPARTMENTS", fill='#0284c7', font=font_bold_sm)
    depts = [
        ("❤️ Cardiology", "Cath Lab, Angioplasty, Pacemaker implants", "Lead: Dr. A. K. Varma, MD, DM"),
        ("🧠 Neurology", "Stroke care, Epilepsy, Spine micro-surgery", "Lead: Dr. M. Sujatha, MS, MCh"),
        ("🦴 Orthopedics", "Joint replacement, Trauma fractures, Sports care", "Lead: Dr. K. Rajesh, MS (Ortho)"),
        ("👶 Pediatrics", "Level-III NICU, Child vaccination programs", "Lead: Dr. P. Sravanthi, MD")
    ]
    x_dept = 40
    dept_w = 265
    for d_title, d_desc, d_lead in depts:
        draw.rectangle([x_dept, 380, x_dept + dept_w, 475], fill='#ffffff', outline='#cbd5e1')
        draw.text((x_dept + 14, 395), d_title, fill='#0f172a', font=font_h3)
        draw.text((x_dept + 14, 420), d_desc, fill='#64748b', font=font_sub)
        draw.text((x_dept + 14, 452), d_lead, fill='#0284c7', font=font_bold_sm)
        x_dept += dept_w + 18
        
    # Appointment Booking Form & OPD Token Preview
    draw.text((40, 495), "DOCTOR CONSULTATION APPOINTMENT DESK (ACCESSIBLE FORM)", fill='#0284c7', font=font_bold_sm)
    
    # Form Left Card
    draw.rectangle([40, 520, 680, 735], fill='#ffffff', outline='#cbd5e1')
    draw.text((60, 535), "Patient Appointment Request Form", fill='#0f172a', font=font_h3)
    
    form_fields = [
        ("Patient Name:", "Yaswanth Avirneni (Roll No: 26000918)", 565),
        ("Contact Mobile:", "+91 9640334422 (SMS Token Verified)", 605),
        ("Department:", "Cardiology & Cardiac Sciences", 645),
        ("Consultant Doctor:", "Dr. A. K. Varma, MD, DM (Cardiology)", 685)
    ]
    for lbl, val, y_f in form_fields:
        draw.text((60, y_f), lbl, fill='#475569', font=font_bold_sm)
        draw.rectangle([210, y_f - 4, 650, y_f + 24], fill='#f8fafc', outline='#cbd5e1')
        draw.text((220, y_f + 2), val, fill='#0f172a', font=font_body)
        
    # Token Right Card (Pure CSS :target modal preview)
    draw.rectangle([710, 520, w - 40, 735], fill='#f0fdf4', outline='#86efac')
    draw.text((735, 535), "✓ OPD TOKEN GENERATED", fill='#15803d', font=font_h3)
    draw.rectangle([735, 565, w - 65, 625], fill='#ffffff', outline='#bbf7d0')
    draw.text((750, 575), "CONFIRMATION TOKEN", fill='#64748b', font=font_sub)
    draw.text((750, 595), "NRIIT-MED-2026-0842", fill='#0f172a', font=font_h2)
    
    draw.text((735, 640), "Consultation Slot: Nov 15, 2026 (09:30 AM)", fill='#1e293b', font=font_body)
    draw.text((735, 660), "Location: NRIIT OPD Suite 104, 1st Floor", fill='#475569', font=font_sub)
    draw.text((735, 680), "Patient: Yaswanth Avirneni | Roll No: 26000918", fill='#475569', font=font_sub)
    draw.rectangle([735, 700, w - 65, 725], fill='#059669')
    draw.text((820, 706), "Download PDF Token Receipt", fill='#ffffff', font=font_bold_sm)

    out_path = os.path.join(SCREENSHOTS_DIR, "healthcare_portal_preview.png")
    img.save(out_path)
    print("Saved:", out_path)

if __name__ == "__main__":
    render_academic_dashboard()
    render_elearning_platform()
    render_healthcare_portal()
