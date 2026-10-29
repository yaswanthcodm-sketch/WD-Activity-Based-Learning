import os
from PIL import Image, ImageDraw, ImageFont

SCREENSHOTS_DIR = "/Users/yaswanth/.gemini/antigravity/scratch/WD-Activity-Based-Learning/screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Load fonts
try:
    font_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 18)
    font_sub = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 12)
    font_bold = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 13)
    font_reg = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 12)
    font_small = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 10)
    font_small_bold = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 10)
    font_mono = ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 11)
    font_url = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 12)
    font_tab = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 11)
except Exception:
    font_title = font_sub = font_bold = font_reg = font_small = font_small_bold = font_mono = font_url = font_tab = ImageFont.load_default()

def create_browser_frame(w=1200, h=780, title="Chrome", url="http://localhost:5500/"):
    img = Image.new('RGB', (w, h), color='#ffffff')
    draw = ImageDraw.Draw(img)

    # Browser header bar
    draw.rectangle([0, 0, w, 75], fill='#dee1e6')

    # Window dots
    draw.ellipse([14, 13, 26, 25], fill='#ff5f56')
    draw.ellipse([34, 13, 46, 25], fill='#ffbd2e')
    draw.ellipse([54, 13, 66, 25], fill='#27c93f')

    # Chrome Tab
    tab_w = 260
    draw.rectangle([80, 8, 80 + tab_w, 38], fill='#ffffff')
    draw.text((95, 16), title[:34], fill='#202124', font=font_tab)
    draw.text((80 + tab_w - 20, 15), "×", fill='#5f6368', font=font_bold)

    # URL bar area
    draw.rectangle([0, 38, w, 75], fill='#ffffff')
    draw.line([(0, 75), (w, 75)], fill='#e0e0e0', width=1)

    # Nav buttons
    draw.text((16, 48), "←  →  ↻", fill='#5f6368', font=font_bold)

    # Address Box
    draw.rounded_rectangle([95, 43, w - 120, 69], radius=13, fill='#f1f3f4')
    draw.text((112, 48), "🔒 " + url, fill='#202124', font=font_url)

    # Profile & Menu icons
    draw.ellipse([w - 100, 44, w - 76, 68], fill='#1a73e8')
    draw.text((w - 92, 49), "Y", fill='#ffffff', font=font_small_bold)
    draw.text((w - 60, 48), "⋮", fill='#5f6368', font=font_bold)

    return img, draw

# -------------------------------------------------------------
# 1. CASE 01: COURSE REGISTRATION MAIN VIEW
# -------------------------------------------------------------
def render_case_01_main():
    w, h = 1200, 780
    img, draw = create_browser_frame(w, h, "Dr. RVR NRIIT - Course Registration Portal", "http://127.0.0.1:5500/Case_01_Student_Course_Registration/index.html")

    # Content background
    draw.rectangle([0, 76, w, h], fill='#f8fafc')

    # Navbar
    draw.rectangle([0, 76, w, 130], fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rounded_rectangle([30, 86, 95, 120], radius=6, fill='#1e40af')
    draw.text((42, 94), "NRIIT", fill='#ffffff', font=font_bold)

    draw.text((110, 86), "DR. RVR NRI INSTITUTE OF TECHNOLOGY", fill='#0f172a', font=font_bold)
    draw.text((110, 104), "School of Computer Studies • Autonomous & Deemed to be University", fill='#64748b', font=font_small)

    # Student Badge
    draw.rounded_rectangle([w - 280, 86, w - 30, 120], radius=18, fill='#eff6ff', outline='#bfdbfe')
    draw.ellipse([w - 272, 90, w - 246, 116], fill='#1e40af')
    draw.text((w - 263, 95), "Y", fill='#ffffff', font=font_small_bold)
    draw.text((w - 238, 91), "Yaswanth", fill='#1e3a8a', font=font_bold)
    draw.text((w - 238, 105), "Roll: 26000918 | CSE (CSM1)", fill='#64748b', font=font_small)

    # Banner
    draw.rounded_rectangle([30, 142, w - 30, 205], radius=12, fill='#0f172a')
    draw.text((50, 154), "Semester Course Enrollment Portal (2026-27)", fill='#ffffff', font=font_title)
    draw.text((50, 180), "Select your desired Core, Professional Elective, and Laboratory courses. Credit workload: 16 to 24 credits.", fill='#cbd5e1', font=font_sub)
    draw.rounded_rectangle([w - 190, 160, w - 50, 188], radius=14, fill='#1e293b', outline='#3b82f6')
    draw.text((w - 176, 167), "Semester III - Autumn", fill='#93c5fd', font=font_small_bold)

    # Filters
    draw.text((30, 220), "Available Courses", fill='#0f172a', font=font_bold)
    draw.text((30, 238), "Filter courses by category and click '+ Add Course'", fill='#64748b', font=font_small)

    filter_x = 450
    cats = [("All (8)", True), ("Core", False), ("Elective", False), ("Lab", False)]
    for cat_name, is_act in cats:
        bg = '#1e40af' if is_act else '#ffffff'
        fg = '#ffffff' if is_act else '#64748b'
        draw.rounded_rectangle([filter_x, 220, filter_x + 65, 245], radius=6, fill=bg, outline='#cbd5e1')
        draw.text((filter_x + 12, 226), cat_name, fill=fg, font=font_small_bold)
        filter_x += 75

    # Course Cards Grid (2x2 on left)
    card_x1, card_x2 = 30, 410
    card_w = 365
    
    # Card 1: Data Structures
    draw.rounded_rectangle([card_x1, 260, card_x1 + card_w, 420], radius=10, fill='#ffffff', outline='#3b82f6', width=2)
    draw.rounded_rectangle([card_x1 + 14, 272, card_x1 + 75, 290], radius=4, fill='#e0f2fe')
    draw.text((card_x1 + 20, 275), "26CS301", fill='#0284c7', font=font_small_bold)
    draw.rounded_rectangle([card_x1 + 82, 272, card_x1 + 125, 290], radius=4, fill='#fee2e2')
    draw.text((card_x1 + 90, 275), "Core", fill='#991b1b', font=font_small_bold)
    draw.text((card_x1 + 14, 298), "Data Structures & Algorithms", fill='#0f172a', font=font_bold)
    draw.text((card_x1 + 14, 318), "Linear/non-linear data structures, trees, and graphs.", fill='#475569', font=font_small)
    draw.text((card_x1 + 14, 340), "Faculty: Dr. K. Srinivas Rao | Venue: CS-Hall 102", fill='#64748b', font=font_small)
    draw.text((card_x1 + 14, 385), "4.0 Credits", fill='#1e40af', font=font_bold)
    draw.rounded_rectangle([card_x1 + card_w - 110, 375, card_x1 + card_w - 14, 405], radius=6, fill='#fee2e2')
    draw.text((card_x1 + card_w - 95, 383), "Remove", fill='#dc2626', font=font_small_bold)

    # Card 2: Web Dev
    draw.rounded_rectangle([card_x2, 260, card_x2 + card_w, 420], radius=10, fill='#ffffff', outline='#3b82f6', width=2)
    draw.rounded_rectangle([card_x2 + 14, 272, card_x2 + 75, 290], radius=4, fill='#e0f2fe')
    draw.text((card_x2 + 20, 275), "26CS302", fill='#0284c7', font=font_small_bold)
    draw.rounded_rectangle([card_x2 + 82, 272, card_x2 + 125, 290], radius=4, fill='#fee2e2')
    draw.text((card_x2 + 90, 275), "Core", fill='#991b1b', font=font_small_bold)
    draw.text((card_x2 + 14, 298), "Web Development Technologies", fill='#0f172a', font=font_bold)
    draw.text((card_x2 + 14, 318), "Frontend semantics, CSS Grid/Flexbox, DOM, JavaScript.", fill='#475569', font=font_small)
    draw.text((card_x2 + 14, 340), "Faculty: Prof. M. Lakshmi | Venue: Web Center", fill='#64748b', font=font_small)
    draw.text((card_x2 + 14, 385), "3.0 Credits", fill='#1e40af', font=font_bold)
    draw.rounded_rectangle([card_x2 + card_w - 110, 375, card_x2 + card_w - 14, 405], radius=6, fill='#fee2e2')
    draw.text((card_x2 + card_w - 95, 383), "Remove", fill='#dc2626', font=font_small_bold)

    # Card 3: AI & ML
    draw.rounded_rectangle([card_x1, 435, card_x1 + card_w, 595], radius=10, fill='#ffffff', outline='#3b82f6', width=2)
    draw.rounded_rectangle([card_x1 + 14, 447, card_x1 + 75, 465], radius=4, fill='#e0f2fe')
    draw.text((card_x1 + 20, 450), "26CS304", fill='#0284c7', font=font_small_bold)
    draw.rounded_rectangle([card_x1 + 82, 447, card_x1 + 135, 465], radius=4, fill='#fef3c7')
    draw.text((card_x1 + 88, 450), "Elective", fill='#92400e', font=font_small_bold)
    draw.text((card_x1 + 14, 473), "Artificial Intelligence & ML", fill='#0f172a', font=font_bold)
    draw.text((card_x1 + 14, 493), "Search algorithms, intelligent agents, predictive models.", fill='#475569', font=font_small)
    draw.text((card_x1 + 14, 515), "Faculty: Dr. A. Sudhir Babu | Venue: AI Spec Lab", fill='#64748b', font=font_small)
    draw.text((card_x1 + 14, 560), "3.0 Credits", fill='#1e40af', font=font_bold)
    draw.rounded_rectangle([card_x1 + card_w - 110, 550, card_x1 + card_w - 14, 580], radius=6, fill='#fee2e2')
    draw.text((card_x1 + card_w - 95, 558), "Remove", fill='#dc2626', font=font_small_bold)

    # Card 4: Python for Data Science
    draw.rounded_rectangle([card_x2, 435, card_x2 + card_w, 595], radius=10, fill='#ffffff', outline='#3b82f6', width=2)
    draw.rounded_rectangle([card_x2 + 14, 447, card_x2 + 75, 465], radius=4, fill='#e0f2fe')
    draw.text((card_x2 + 20, 450), "26CS305", fill='#0284c7', font=font_small_bold)
    draw.rounded_rectangle([card_x2 + 82, 272 + 175, card_x2 + 135, 290 + 175], radius=4, fill='#fef3c7')
    draw.text((card_x2 + 88, 450), "Elective", fill='#92400e', font=font_small_bold)
    draw.text((card_x2 + 14, 473), "Python for Data Science", fill='#0f172a', font=font_bold)
    draw.text((card_x2 + 14, 493), "NumPy, Pandas, Matplotlib, Data pipelines & workflows.", fill='#475569', font=font_small)
    draw.text((card_x2 + 14, 515), "Faculty: Prof. N. Chaitanya | Venue: Computing Lab 1", fill='#64748b', font=font_small)
    draw.text((card_x2 + 14, 560), "3.0 Credits", fill='#1e40af', font=font_bold)
    draw.rounded_rectangle([card_x2 + card_w - 110, 550, card_x2 + card_w - 14, 580], radius=6, fill='#fee2e2')
    draw.text((card_x2 + card_w - 95, 558), "Remove", fill='#dc2626', font=font_small_bold)

    # Sidebar: Registration Summary
    side_x = 800
    side_w = 370
    draw.rounded_rectangle([side_x, 220, side_x + side_w, 730], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.text((side_x + 20, 238), "Registration Summary", fill='#0f172a', font=font_bold)
    draw.rounded_rectangle([side_x + side_w - 100, 235, side_x + side_w - 20, 258], radius=12, fill='#dbeafe')
    draw.text((side_x + side_w - 88, 241), "5 Courses", fill='#1e40af', font=font_small_bold)

    # Credit meter
    draw.rounded_rectangle([side_x + 20, 270, side_x + side_w - 20, 335], radius=8, fill='#f8fafc', outline='#e2e8f0')
    draw.text((side_x + 32, 280), "Total Credits Enrolled:", fill='#475569', font=font_small)
    draw.text((side_x + side_w - 85, 278), "18.5 / 24", fill='#0f172a', font=font_bold)
    # Meter bar
    draw.rounded_rectangle([side_x + 32, 302, side_x + side_w - 32, 310], radius=4, fill='#e2e8f0')
    fill_w = int((side_w - 64) * (18.5 / 24))
    draw.rounded_rectangle([side_x + 32, 302, side_x + 32 + fill_w, 310], radius=4, fill='#10b981')
    draw.text((side_x + 32, 318), "Min: 16 credits", fill='#64748b', font=font_small)
    draw.text((side_x + side_w - 180, 318), "✓ Workload Met! Ready", fill='#16a34a', font=font_small_bold)

    # Enrolled list
    draw.text((side_x + 20, 350), "Enrolled Subjects:", fill='#334155', font=font_bold)
    subjects = [
        ("26CS301: Data Structures & Algorithms", "4.0 Cr"),
        ("26CS302: Web Development Technologies", "3.0 Cr"),
        ("26CS303: Discrete Mathematics", "4.0 Cr"),
        ("26CS304: Artificial Intelligence & ML", "3.0 Cr"),
        ("26CS307L: Data Structures Lab", "1.5 Cr"),
        ("26CS308L: Web Development Lab", "1.5 Cr"),
    ]
    cur_y = 372
    for s_title, s_cr in subjects:
        draw.rounded_rectangle([side_x + 20, cur_y, side_x + side_w - 20, cur_y + 24], radius=4, fill='#f1f5f9')
        draw.text((side_x + 26, cur_y + 5), "• " + s_title[:32], fill='#1e293b', font=font_small)
        draw.text((side_x + side_w - 65, cur_y + 5), s_cr, fill='#1e40af', font=font_small_bold)
        cur_y += 28

    # Fee Breakdown
    draw.line([(side_x + 20, 545), (side_x + side_w - 20, 545)], fill='#e2e8f0', width=1)
    draw.text((side_x + 20, 555), "Academic Tuition Fee:", fill='#64748b', font=font_small)
    draw.text((side_x + side_w - 80, 555), "₹ 11,500", fill='#334155', font=font_small_bold)
    draw.text((side_x + 20, 575), "Lab & Consumables:", fill='#64748b', font=font_small)
    draw.text((side_x + side_w - 75, 575), "₹ 4,500", fill='#334155', font=font_small_bold)
    draw.line([(side_x + 20, 595), (side_x + side_w - 20, 595)], fill='#cbd5e1', width=1)
    draw.text((side_x + 20, 605), "Total Semester Dues:", fill='#0f172a', font=font_bold)
    draw.text((side_x + side_w - 85, 605), "₹ 16,000", fill='#1e40af', font=font_bold)

    # Checkbox
    draw.rectangle([side_x + 20, 635, side_x + 32, 647], fill='#1e40af')
    draw.text((side_x + 22, 634), "✓", fill='#ffffff', font=font_small_bold)
    draw.text((side_x + 40, 633), "I, Yaswanth (26000918), confirm that", fill='#475569', font=font_small)
    draw.text((side_x + 40, 647), "all prerequisites are fulfilled.", fill='#475569', font=font_small)

    # Submit button
    draw.rounded_rectangle([side_x + 20, 670, side_x + side_w - 20, 715], radius=8, fill='#1e40af')
    draw.text((side_x + 95, 686), "Submit Course Registration", fill='#ffffff', font=font_bold)

    img.save(os.path.join(SCREENSHOTS_DIR, "case_01_main_portal.png"))
    print("Saved case_01_main_portal.png")

# -------------------------------------------------------------
# 2. CASE 01: MODAL REGISTRATION SLIP
# -------------------------------------------------------------
def render_case_01_modal():
    w, h = 1200, 780
    img, draw = create_browser_frame(w, h, "Registration Receipt - Dr. RVR NRIIT", "http://127.0.0.1:5500/Case_01_Student_Course_Registration/index.html")

    # Dark backdrop overlay
    draw.rectangle([0, 76, w, h], fill='#0f172acc')

    # Modal card
    mx, my, mw, mh = 340, 130, 520, 580
    draw.rounded_rectangle([mx, my, mx + mw, my + mh], radius=16, fill='#ffffff')

    # Modal icon & header
    draw.ellipse([mx + mw//2 - 24, my + 24, mx + mw//2 + 24, my + 72], fill='#dcfce7')
    draw.text((mx + mw//2 - 9, my + 34), "✓", fill='#16a34a', font=font_title)
    draw.text((mx + 115, my + 82), "Course Registration Confirmed!", fill='#0f172a', font=font_title)
    draw.text((mx + 125, my + 108), "Dr. RVR NRI Institute of Technology — Academic Office", fill='#64748b', font=font_small)

    # Slip container
    sx, sy, sw, sh = mx + 25, my + 135, mw - 50, 360
    draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=8, fill='#fafafa', outline='#e2e8f0')

    # Student metadata
    draw.text((sx + 15, sy + 15), "Student Name: Yaswanth", fill='#0f172a', font=font_bold)
    draw.text((sx + 15, sy + 32), "Roll Number: 26000918", fill='#475569', font=font_small)
    draw.text((sx + sw - 150, sy + 15), "Branch: CSE (CSM1)", fill='#0f172a', font=font_bold)
    draw.text((sx + sw - 150, sy + 32), "Date: 30-Oct-2026", fill='#475569', font=font_small)

    draw.line([(sx + 15, sy + 55), (sx + sw - 15, sy + 55)], fill='#cbd5e1', width=1)

    # Table Header
    draw.rectangle([sx + 15, sy + 65, sx + sw - 15, sy + 90], fill='#f1f5f9')
    draw.text((sx + 25, sy + 72), "Course Code", fill='#334155', font=font_small_bold)
    draw.text((sx + 120, sy + 72), "Course Title", fill='#334155', font=font_small_bold)
    draw.text((sx + 340, sy + 72), "Type", fill='#334155', font=font_small_bold)
    draw.text((sx + 400, sy + 72), "Credits", fill='#334155', font=font_small_bold)

    # Table Rows
    rows = [
        ("26CS301", "Data Structures & Algorithms", "Core", "4.0"),
        ("26CS302", "Web Development Technologies", "Core", "3.0"),
        ("26CS303", "Discrete Mathematics", "Core", "4.0"),
        ("26CS304", "Artificial Intelligence & ML", "Elective", "3.0"),
        ("26CS307L", "Data Structures Laboratory", "Lab", "1.5"),
        ("26CS308L", "Web Development Hands-on Lab", "Lab", "1.5"),
    ]
    ry = sy + 98
    for c_code, c_title, c_type, c_cr in rows:
        draw.text((sx + 25, ry), c_code, fill='#1e40af', font=font_small_bold)
        draw.text((sx + 120, ry), c_title[:28], fill='#0f172a', font=font_small)
        draw.text((sx + 340, ry), c_type, fill='#475569', font=font_small)
        draw.text((sx + 410, ry), c_cr, fill='#0f172a', font=font_small_bold)
        ry += 26

    # Summary
    draw.line([(sx + 15, sy + 270), (sx + sw - 15, sy + 270)], fill='#cbd5e1', width=1)
    draw.text((sx + 20, sy + 285), "Total Registered Credits:", fill='#0f172a', font=font_bold)
    draw.text((sx + 190, sy + 285), "17.0 Credits", fill='#1e40af', font=font_bold)

    draw.rounded_rectangle([sx + sw - 190, sy + 280, sx + sw - 15, sy + 305], radius=4, fill='#dcfce7')
    draw.text((sx + sw - 180, sy + 286), "PROVISIONALLY APPROVED", fill='#15803d', font=font_small_bold)

    draw.text((sx + 20, sy + 325), "Generated via NRIIT Academic Portal • Verified by Faculty Advisor", fill='#94a3b8', font=font_small)

    # Action buttons
    draw.rounded_rectangle([mx + 220, my + mh - 55, mx + 360, my + mh - 18], radius=8, fill='#f1f5f9', outline='#cbd5e1')
    draw.text((mx + 238, my + mh - 42), "Print / Save PDF", fill='#334155', font=font_bold)

    draw.rounded_rectangle([mx + 375, my + mh - 55, mx + 490, my + mh - 18], radius=8, fill='#1e40af')
    draw.text((mx + 415, my + mh - 42), "Done", fill='#ffffff', font=font_bold)

    img.save(os.path.join(SCREENSHOTS_DIR, "case_01_modal_receipt.png"))
    print("Saved case_01_modal_receipt.png")

# -------------------------------------------------------------
# 3. CASE 02: TECHFEST EVENT PORTAL
# -------------------------------------------------------------
def render_case_02_portal():
    w, h = 1200, 780
    img, draw = create_browser_frame(w, h, "TechVyuha '26 - Campus Tech Fest & Event Hub", "http://127.0.0.1:5500/Case_02_Campus_Event_Management/index.html")

    # Header
    draw.rectangle([0, 76, w, 130], fill='#0b0f19')
    draw.rounded_rectangle([30, 86, 70, 120], radius=8, fill='#4f46e5')
    draw.text((43, 93), "⚡", fill='#ffffff', font=font_bold)
    draw.text((82, 86), "TechVyuha '26", fill='#ffffff', font=font_bold)
    draw.text((82, 105), "Annual National Tech Symposium • Dr. RVR NRI Institute of Technology", fill='#94a3b8', font=font_small)

    draw.rounded_rectangle([w - 380, 88, w - 170, 118], radius=16, fill='#1e293b', outline='#334155')
    draw.ellipse([w - 368, 98, w - 360, 106], fill='#22c55e')
    draw.text((w - 350, 95), "Yaswanth (26000918) | CSM1", fill='#e2e8f0', font=font_small_bold)

    draw.rounded_rectangle([w - 155, 88, w - 30, 118], radius=8, fill='#1e1b4b', outline='#6366f1')
    draw.text((w - 138, 95), "My Passes (2)", fill='#a5b4fc', font=font_small_bold)

    # Fest Hero Section
    draw.rectangle([0, 130, w, 280], fill='#1e1b4b')
    draw.rounded_rectangle([30, 145, 340, 168], radius=12, fill='#312e81', outline='#6366f1')
    draw.text((42, 150), "DEPARTMENT OF CSE & ALLIED BRANCHES PRESENTS", fill='#a5b4fc', font=font_small_bold)

    draw.text((30, 178), "Code. Innovate. Conquer.", fill='#ffffff', font=font_title)
    draw.text((30, 208), "Join over 1,500+ engineering students across 6 flagship hackathons, paper presentations, and coding arenas.", fill='#cbd5e1', font=font_sub)

    # Hero stats
    stats = [("₹ 1,50,000+", "Prize Pool"), ("6", "Flagship Events"), ("Nov 14-16", "Event Dates"), ("Campus Audis", "Main Venue")]
    stat_x = 30
    for s_val, s_lbl in stats:
        draw.rounded_rectangle([stat_x, 230, stat_x + 130, 268], radius=8, fill='#0f172a', outline='#4338ca')
        draw.text((stat_x + 12, 236), s_val, fill='#38bdf8', font=font_bold)
        draw.text((stat_x + 12, 252), s_lbl, fill='#94a3b8', font=font_small)
        stat_x += 145

    # Main area
    draw.rectangle([0, 280, w, h], fill='#f1f5f9')

    # Controls Bar
    draw.rounded_rectangle([30, 295, 380, 328], radius=8, fill='#ffffff', outline='#cbd5e1')
    draw.text((45, 304), "🔍 Search events by title, keyword, or venue...", fill='#64748b', font=font_small)

    tab_x = 450
    tabs = [("All Arenas", True), ("Hackathon", False), ("Coding & Web", False), ("Paper & PPT", False), ("Gaming & AI", False)]
    for t_name, is_act in tabs:
        t_bg = '#4f46e5' if is_act else '#ffffff'
        t_fg = '#ffffff' if is_act else '#64748b'
        draw.rounded_rectangle([tab_x, 295, tab_x + 95, 328], radius=8, fill=t_bg, outline='#cbd5e1')
        draw.text((tab_x + 10, 305), t_name, fill=t_fg, font=font_small_bold)
        tab_x += 105

    # Event Cards Grid (3 cards row)
    card_w = 360
    ev_x1, ev_x2, ev_x3 = 30, 420, 810

    # Card 1: 24-hr Hackathon
    draw.rounded_rectangle([ev_x1, 345, ev_x1 + card_w, 730], radius=14, fill='#ffffff', outline='#cbd5e1')
    draw.rounded_rectangle([ev_x1, 345, ev_x1 + card_w, 425], radius=14, fill='#1e1b4b')
    draw.rounded_rectangle([ev_x1 + 14, 355, ev_x1 + 100, 375], radius=10, fill='#312e81', outline='#6366f1')
    draw.text((ev_x1 + 22, 360), "HACKATHON", fill='#ffffff', font=font_small_bold)
    draw.rounded_rectangle([ev_x1 + card_w - 110, 355, ev_x1 + card_w - 14, 375], radius=4, fill='#fef08a')
    draw.text((ev_x1 + card_w - 100, 360), "Prize: ₹ 50,000", fill='#854d0e', font=font_small_bold)

    draw.text((ev_x1 + 14, 438), "CodeSprint: 24-Hr Hackathon", fill='#0f172a', font=font_bold)
    draw.text((ev_x1 + 14, 458), "Build AI solutions tackling healthcare or mobility.", fill='#475569', font=font_small)

    draw.rounded_rectangle([ev_x1 + 14, 485, ev_x1 + card_w - 14, 640], radius=8, fill='#f8fafc', outline='#e2e8f0')
    draw.text((ev_x1 + 24, 498), "📅 Date: Nov 14, 2026 (09:00 AM)", fill='#334155', font=font_small)
    draw.text((ev_x1 + 24, 524), "📍 Venue: Central CSE Lab 3 & 4", fill='#334155', font=font_small)
    draw.text((ev_x1 + 24, 550), "👥 Team Size: Up to 3 Members", fill='#334155', font=font_small)
    draw.text((ev_x1 + 24, 576), "⚡ Slots Remaining: 8 slots left", fill='#0284c7', font=font_small_bold)
    draw.text((ev_x1 + 24, 602), "👤 Coordinator: Yaswanth (CSM1)", fill='#64748b', font=font_small)

    draw.text((ev_x1 + 14, 665), "ENTRY FEE", fill='#64748b', font=font_small)
    draw.text((ev_x1 + 14, 680), "₹ 300", fill='#0f172a', font=font_bold)
    draw.rounded_rectangle([ev_x1 + card_w - 130, 665, ev_x1 + card_w - 14, 705], radius=8, fill='#4f46e5')
    draw.text((ev_x1 + card_w - 110, 678), "Register Now", fill='#ffffff', font=font_bold)

    # Card 2: WebCraft Live
    draw.rounded_rectangle([ev_x2, 345, ev_x2 + card_w, 730], radius=14, fill='#ffffff', outline='#cbd5e1')
    draw.rounded_rectangle([ev_x2, 345, ev_x2 + card_w, 425], radius=14, fill='#0369a1')
    draw.rounded_rectangle([ev_x2 + 14, 355, ev_x2 + 110, 375], radius=10, fill='#0284c7', outline='#38bdf8')
    draw.text((ev_x2 + 22, 360), "CODING & WEB", fill='#ffffff', font=font_small_bold)
    draw.rounded_rectangle([ev_x2 + card_w - 110, 355, ev_x2 + card_w - 14, 375], radius=4, fill='#fef08a')
    draw.text((ev_x2 + card_w - 100, 360), "Prize: ₹ 20,000", fill='#854d0e', font=font_small_bold)

    draw.text((ev_x2 + 14, 438), "WebCraft: Live UI/UX Arena", fill='#0f172a', font=font_bold)
    draw.text((ev_x2 + 14, 458), "Design responsive web layouts under time constraints.", fill='#475569', font=font_small)

    draw.rounded_rectangle([ev_x2 + 14, 485, ev_x2 + card_w - 14, 640], radius=8, fill='#f8fafc', outline='#e2e8f0')
    draw.text((ev_x2 + 24, 498), "📅 Date: Nov 15, 2026 (10:30 AM)", fill='#334155', font=font_small)
    draw.text((ev_x2 + 24, 524), "📍 Venue: Web Tech Lab (Block A)", fill='#334155', font=font_small)
    draw.text((ev_x2 + 24, 550), "👥 Team Size: Solo Participant", fill='#334155', font=font_small)
    draw.text((ev_x2 + 24, 576), "⚡ Slots Remaining: 14 slots left", fill='#0284c7', font=font_small_bold)
    draw.text((ev_x2 + 24, 602), "✓ Registered by Yaswanth (26000918)", fill='#16a34a', font=font_small_bold)

    draw.text((ev_x2 + 14, 665), "ENTRY FEE", fill='#64748b', font=font_small)
    draw.text((ev_x2 + 14, 680), "₹ 150", fill='#0f172a', font=font_bold)
    draw.rounded_rectangle([ev_x2 + card_w - 130, 665, ev_x2 + card_w - 14, 705], radius=8, fill='#10b981')
    draw.text((ev_x2 + card_w - 115, 678), "✓ Registered", fill='#ffffff', font=font_bold)

    # Card 3: Paper Presentation
    draw.rounded_rectangle([ev_x3, 345, ev_x3 + card_w, 730], radius=14, fill='#ffffff', outline='#cbd5e1')
    draw.rounded_rectangle([ev_x3, 345, ev_x3 + card_w, 425], radius=14, fill='#047857')
    draw.rounded_rectangle([ev_x3 + 14, 355, ev_x3 + 105, 375], radius=10, fill='#065f46', outline='#34d399')
    draw.text((ev_x3 + 22, 360), "PAPER & PPT", fill='#ffffff', font=font_small_bold)
    draw.rounded_rectangle([ev_x3 + card_w - 110, 355, ev_x3 + card_w - 14, 375], radius=4, fill='#fef08a')
    draw.text((ev_x3 + card_w - 100, 360), "Prize: ₹ 15,000", fill='#854d0e', font=font_small_bold)

    draw.text((ev_x3 + 14, 438), "Paper Presentation: Next-Gen", fill='#0f172a', font=font_bold)
    draw.text((ev_x3 + 14, 458), "Present research in Generative AI, IoT, & Forensics.", fill='#475569', font=font_small)

    draw.rounded_rectangle([ev_x3 + 14, 485, ev_x3 + card_w - 14, 640], radius=8, fill='#f8fafc', outline='#e2e8f0')
    draw.text((ev_x3 + 24, 498), "📅 Date: Nov 16, 2026 (09:30 AM)", fill='#334155', font=font_small)
    draw.text((ev_x3 + 24, 524), "📍 Venue: Seminar Hall (Block B)", fill='#334155', font=font_small)
    draw.text((ev_x3 + 24, 550), "👥 Team Size: Up to 2 Members", fill='#334155', font=font_small)
    draw.text((ev_x3 + 24, 576), "⚡ Slots Remaining: 11 slots left", fill='#0284c7', font=font_small_bold)
    draw.text((ev_x3 + 24, 602), "✓ Registered by Yaswanth (26000918)", fill='#16a34a', font=font_small_bold)

    draw.text((ev_x3 + 14, 665), "ENTRY FEE", fill='#64748b', font=font_small)
    draw.text((ev_x3 + 14, 680), "₹ 200", fill='#0f172a', font=font_bold)
    draw.rounded_rectangle([ev_x3 + card_w - 130, 665, ev_x3 + card_w - 14, 705], radius=8, fill='#10b981')
    draw.text((ev_x3 + card_w - 115, 678), "✓ Registered", fill='#ffffff', font=font_bold)

    img.save(os.path.join(SCREENSHOTS_DIR, "case_02_techfest_portal.png"))
    print("Saved case_02_techfest_portal.png")

# -------------------------------------------------------------
# 4. CASE 02: DIGITAL E-TICKET PASS
# -------------------------------------------------------------
def render_case_02_pass():
    w, h = 1200, 780
    img, draw = create_browser_frame(w, h, "Digital Pass - TechVyuha '26", "http://127.0.0.1:5500/Case_02_Campus_Event_Management/index.html")

    draw.rectangle([0, 76, w, h], fill='#0f172acc')

    # Pass Card Centered
    px, py, pw, ph = 370, 140, 460, 520
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=16, fill='#0f172a', outline='#38bdf8', width=2)

    # Pass Header
    draw.rounded_rectangle([px, py, px + pw, py + 85], radius=16, fill='#1e1b4b')
    draw.text((px + 24, py + 20), "TECHVYUHA '26 PASS", fill='#38bdf8', font=font_title)
    draw.text((px + 24, py + 45), "Dr. RVR NRI Institute of Technology", fill='#94a3b8', font=font_small)

    draw.rounded_rectangle([px + pw - 150, py + 22, px + pw - 20, py + 52], radius=6, fill='#0f172a', outline='#38bdf8')
    draw.text((px + pw - 142, py + 30), "NRIIT-TV26-8918", fill='#7dd3fc', font=font_small_bold)

    # Dashed divider
    for dx in range(px + 10, px + pw - 10, 16):
        draw.line([(dx, py + 85), (dx + 8, py + 85)], fill='#64748b', width=2)

    # Pass Body
    draw.text((px + 24, py + 105), "WebCraft: Live UI/UX Challenge", fill='#ffffff', font=font_title)

    # Metadata Grid
    draw.text((px + 24, py + 145), "CANDIDATE NAME:", fill='#94a3b8', font=font_small)
    draw.text((px + 24, py + 162), "Yaswanth", fill='#ffffff', font=font_bold)

    draw.text((px + 240, py + 145), "ROLL NUMBER:", fill='#94a3b8', font=font_small)
    draw.text((px + 240, py + 162), "26000918", fill='#ffffff', font=font_bold)

    draw.text((px + 24, py + 195), "DEPARTMENT / BRANCH:", fill='#94a3b8', font=font_small)
    draw.text((px + 24, py + 212), "CSE (CSM1)", fill='#ffffff', font=font_bold)

    draw.text((px + 240, py + 195), "COLLEGE:", fill='#94a3b8', font=font_small)
    draw.text((px + 240, py + 212), "Dr. RVR NRIIT", fill='#ffffff', font=font_bold)

    draw.text((px + 24, py + 245), "VENUE & TIME:", fill='#94a3b8', font=font_small)
    draw.text((px + 24, py + 262), "Web Technology Lab (Block A) • Nov 15, 10:30 AM", fill='#38bdf8', font=font_bold)

    # Co-participants / Mode
    draw.rounded_rectangle([px + 24, py + 295, px + pw - 24, py + 335], radius=6, fill='#1e293b')
    draw.text((px + 36, py + 305), "Participation: Solo Arena | Payment Method: UPI (Verified)", fill='#cbd5e1', font=font_small)

    # Dashed divider
    for dx in range(px + 10, px + pw - 10, 16):
        draw.line([(dx, py + 355), (dx + 8, py + 355)], fill='#64748b', width=2)

    # Pass Footer & QR Mockup
    draw.rounded_rectangle([px + 24, py + 375, px + 104, py + 455], radius=6, fill='#ffffff')
    # QR inner dots
    draw.rectangle([px + 34, py + 385, px + 54, py + 405], fill='#000000')
    draw.rectangle([px + 74, py + 385, px + 94, py + 405], fill='#000000')
    draw.rectangle([px + 34, py + 425, px + 54, py + 445], fill='#000000')
    draw.rectangle([px + 62, py + 412, px + 84, py + 434], fill='#000000')

    draw.text((px + 120, py + 380), "STATUS: VERIFIED & CONFIRMED", fill='#4ade80', font=font_bold)
    draw.text((px + 120, py + 402), "Present this digital pass alongside college ID", fill='#cbd5e1', font=font_small)
    draw.text((px + 120, py + 418), "card at the CSE block verification desk.", fill='#cbd5e1', font=font_small)
    draw.text((px + 120, py + 438), "Issued to: Yaswanth (26000918)", fill='#94a3b8', font=font_small)

    # Action buttons below
    draw.rounded_rectangle([px + 150, py + ph - 45, px + 290, py + ph - 12], radius=6, fill='#ffffff')
    draw.text((px + 165, py + ph - 33), "Print / Save Pass", fill='#0f172a', font=font_bold)

    draw.rounded_rectangle([px + 310, py + ph - 45, px + 430, py + ph - 12], radius=6, fill='#4f46e5')
    draw.text((px + 348, py + ph - 33), "Close", fill='#ffffff', font=font_bold)

    img.save(os.path.join(SCREENSHOTS_DIR, "case_02_digital_pass.png"))
    print("Saved case_02_digital_pass.png")

# -------------------------------------------------------------
# 5. CASE 03: LIBRARY CATALOG & BOOKSTORE
# -------------------------------------------------------------
def render_case_03_catalog():
    w, h = 1200, 780
    img, draw = create_browser_frame(w, h, "NRIIT Central E-Library & Academic Bookstore", "http://127.0.0.1:5500/Case_03_Online_Bookstore_and_Library/index.html")

    # Navbar
    draw.rectangle([0, 76, w, 130], fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rounded_rectangle([30, 86, 74, 120], radius=8, fill='#f0fdfa', outline='#ccfbf1')
    draw.text((42, 92), "📚", fill='#0f766e', font=font_bold)
    draw.text((86, 86), "NRIIT Central E-Library", fill='#0f172a', font=font_bold)
    draw.text((86, 105), "Digital Academic Repository & Book Circulation Desk", fill='#64748b', font=font_small)

    # Student info
    draw.rounded_rectangle([w - 380, 88, w - 180, 118], radius=16, fill='#f1f5f9', outline='#e2e8f0')
    draw.ellipse([w - 372, 92, w - 348, 114], fill='#0f766e')
    draw.text((w - 364, 96), "Y", fill='#ffffff', font=font_small_bold)
    draw.text((w - 340, 92), "Yaswanth", fill='#0f172a', font=font_small_bold)
    draw.text((w - 340, 105), "26000918 • CSM1", fill='#64748b', font=font_small)

    draw.rounded_rectangle([w - 165, 88, w - 30, 118], radius=16, fill='#0f766e')
    draw.text((w - 150, 96), "📖 Reading Bag (2)", fill='#ffffff', font=font_small_bold)

    # Hero
    draw.rectangle([0, 130, w, 230], fill='#0f766e')
    draw.rounded_rectangle([30, 142, 340, 164], radius=12, fill='#134e4a')
    draw.text((42, 147), "DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING", fill='#99f6e4', font=font_small_bold)
    draw.text((30, 172), "Search, Borrow, and Explore Technical Textbooks", fill='#ffffff', font=font_title)
    draw.text((30, 198), "Access prescribed textbooks and research handbooks. Borrow up to 3 volumes for 14 academic days.", fill='#ccfbf1', font=font_sub)

    # Content Area
    draw.rectangle([0, 230, w, h], fill='#f8fafc')

    # Search & Filter
    draw.rounded_rectangle([30, 245, 380, 278], radius=8, fill='#ffffff', outline='#cbd5e1')
    draw.text((45, 254), "🔎 Search by title, author name, or ISBN...", fill='#64748b', font=font_small)

    tab_x = 440
    chips = [("All Disciplines", True), ("CS Core", False), ("Web & Full Stack", False), ("AI & Data Science", False), ("Applied Math", False)]
    for c_lbl, is_act in chips:
        c_bg = '#0f766e' if is_act else '#ffffff'
        c_fg = '#ffffff' if is_act else '#64748b'
        draw.rounded_rectangle([tab_x, 245, tab_x + 105, 278], radius=14, fill=c_bg, outline='#cbd5e1')
        draw.text((tab_x + 12, 254), c_lbl, fill=c_fg, font=font_small_bold)
        tab_x += 115

    # Books Grid (4 books row)
    card_w = 265
    b_xs = [30, 320, 610, 900]

    books_meta = [
        ("The C Programming Language", "Brian Kernighan & Dennis Ritchie", "CS Core", "Rack A-04, Ground Floor", "6 Copies", '#1e3a8a', '#f59e0b'),
        ("Introduction to Algorithms (CLRS)", "Thomas Cormen, Charles Leiserson", "CS Core", "Rack A-12, Ground Floor", "4 Copies", '#312e81', '#f59e0b'),
        ("JavaScript: The Definitive Guide", "David Flanagan", "Web Dev", "Rack B-08, 1st Floor", "7 Copies", '#854d0e', '#f59e0b'),
        ("Artificial Intelligence: Approach", "Stuart Russell & Peter Norvig", "AI & Data", "Rack C-02, 2nd Floor", "5 Copies", '#4c1d95', '#f59e0b')
    ]

    for i, bx in enumerate(b_xs):
        btitle, bauth, bgen, block, bstock, bcol, bspine = books_meta[i]
        draw.rounded_rectangle([bx, 295, bx + card_w, 680], radius=12, fill='#ffffff', outline='#e2e8f0')

        # Book Cover
        draw.rounded_rectangle([bx, 295, bx + card_w, 425], radius=12, fill=bcol)
        draw.rectangle([bx, 295, bx + 6, 425], fill=bspine)
        draw.text((bx + 16, 305), bgen.upper(), fill='#99f6e4', font=font_small_bold)
        draw.text((bx + 16, 335), btitle[:24], fill='#ffffff', font=font_bold)
        draw.text((bx + 16, 355), btitle[24:45], fill='#ffffff', font=font_bold)
        draw.text((bx + 16, 400), "ISBN: 978-0131103627", fill='#ccfbf1', font=font_small)

        # Body
        draw.text((bx + 14, 440), bauth[:28], fill='#0f172a', font=font_bold)
        draw.text((bx + 14, 460), "Standard Academic Edition", fill='#64748b', font=font_small)

        draw.rounded_rectangle([bx + 14, 490, bx + card_w - 14, 550], radius=6, fill='#f8fafc', outline='#f1f5f9')
        draw.text((bx + 20, 502), "📍 Location:", fill='#475569', font=font_small_bold)
        draw.text((bx + 20, 522), block, fill='#64748b', font=font_small)

        draw.line([(bx + 14, 570), (bx + card_w - 14, 570)], fill='#f1f5f9', width=1)
        draw.text((bx + 14, 590), "● " + bstock + " in Shelf", fill='#16a34a', font=font_small_bold)

        # Bag button
        draw.rounded_rectangle([bx + 14, 620, bx + card_w - 14, 660], radius=8, fill='#0f766e')
        draw.text((bx + 60, 634), "+ Add to Bag", fill='#ffffff', font=font_bold)

    # Active Borrowing Strip at bottom
    draw.rounded_rectangle([30, 700, w - 30, 740], radius=8, fill='#fef3c7', outline='#fde68a')
    draw.text((50, 712), "📌 Active Circulation: 2 books currently issued under Yaswanth (Roll No: 26000918) | Section: CSM1", fill='#92400e', font=font_small_bold)
    draw.text((w - 220, 712), "View Active Loans & Dues", fill='#b45309', font=font_small_bold)

    img.save(os.path.join(SCREENSHOTS_DIR, "case_03_library_portal.png"))
    print("Saved case_03_library_portal.png")

# -------------------------------------------------------------
# 6. CASE 03: CIRCULATION RECEIPT & BAG DRAWER
# -------------------------------------------------------------
def render_case_03_receipt():
    w, h = 1200, 780
    img, draw = create_browser_frame(w, h, "Circulation Receipt - NRIIT Central Library", "http://127.0.0.1:5500/Case_03_Online_Bookstore_and_Library/index.html")

    draw.rectangle([0, 76, w, h], fill='#0f172acc')

    # Receipt Modal Card
    mx, my, mw, mh = 360, 130, 480, 560
    draw.rounded_rectangle([mx, my, mx + mw, my + mh], radius=16, fill='#ffffff')

    draw.ellipse([mx + mw//2 - 24, my + 24, mx + mw//2 + 24, my + 72], fill='#ccfbf1')
    draw.text((mx + mw//2 - 9, my + 34), "✓", fill='#0f766e', font=font_title)
    draw.text((mx + 105, my + 82), "Library Circulation Receipt", fill='#0f172a', font=font_title)
    draw.text((mx + 100, my + 108), "Transaction Logged — Dr. RVR NRIIT Central Library", fill='#64748b', font=font_small)

    # Slip container
    sx, sy, sw, sh = mx + 25, my + 135, mw - 50, 340
    draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=8, fill='#fafafa', outline='#e2e8f0')

    draw.text((sx + 15, sy + 15), "Student Name: Yaswanth", fill='#0f172a', font=font_bold)
    draw.text((sx + 15, sy + 32), "Roll Number: 26000918", fill='#475569', font=font_small)
    draw.text((sx + sw - 160, sy + 15), "Branch: CSE (CSM1)", fill='#0f172a', font=font_bold)
    draw.text((sx + sw - 160, sy + 32), "Txn ID: NRIIT-LIB-7821", fill='#0f766e', font=font_small_bold)

    draw.line([(sx + 15, sy + 55), (sx + sw - 15, sy + 55)], fill='#cbd5e1', width=1)

    draw.text((sx + 15, sy + 68), "ISSUED VOLUMES (14-DAY CIRCULATION):", fill='#334155', font=font_small_bold)

    books = [
        ("1. The C Programming Language (2nd Ed)", "Rack A-04 • Ground Floor"),
        ("2. JavaScript: The Definitive Guide (7th Ed)", "Rack B-08 • 1st Floor"),
        ("3. Introduction to Algorithms (CLRS 4th Ed)", "Rack A-12 • Ground Floor")
    ]
    by = sy + 92
    for b_title, b_pos in books:
        draw.text((sx + 20, by), b_title, fill='#0f172a', font=font_bold)
        draw.text((sx + 20, by + 18), "Location: " + b_pos, fill='#64748b', font=font_small)
        by += 44

    draw.line([(sx + 15, sy + 230), (sx + sw - 15, sy + 230)], fill='#cbd5e1', width=1)

    draw.text((sx + 15, sy + 242), "Date of Issue: 30-Oct-2026", fill='#475569', font=font_small)
    draw.text((sx + 15, sy + 262), "Return Due Date: 13-Nov-2026", fill='#b91c1c', font=font_bold)
    draw.text((sx + 15, sy + 285), "Late Fee: ₹ 2.00 / day per volume after due date.", fill='#d97706', font=font_small)
    draw.text((sx + 15, sy + 305), "Issued under College Library Rules • Present ID at counter.", fill='#94a3b8', font=font_small)

    # Actions
    draw.rounded_rectangle([mx + 170, my + mh - 55, mx + 340, my + mh - 18], radius=8, fill='#f1f5f9', outline='#cbd5e1')
    draw.text((mx + 190, my + mh - 42), "Print Circulation Slip", fill='#334155', font=font_bold)

    draw.rounded_rectangle([mx + 355, my + mh - 55, mx + 455, my + mh - 18], radius=8, fill='#0f766e')
    draw.text((mx + 390, my + mh - 42), "Done", fill='#ffffff', font=font_bold)

    img.save(os.path.join(SCREENSHOTS_DIR, "case_03_circulation_slip.png"))
    print("Saved case_03_circulation_slip.png")

if __name__ == "__main__":
    render_case_01_main()
    render_case_01_modal()
    render_case_02_portal()
    render_case_02_pass()
    render_case_03_catalog()
    render_case_03_receipt()
    print("All 6 screenshots successfully rendered!")
