import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image as RLImage,
    Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

REPO_DIR = "/Users/yaswanth/.gemini/antigravity/scratch/WD-Activity-Based-Learning"
REPORTS_DIR = os.path.join(REPO_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(REPO_DIR, "screenshots")
os.makedirs(REPORTS_DIR, exist_ok=True)

PDF_PATH = os.path.join(REPORTS_DIR, "WD_ABL_Consolidated_Report.pdf")
ROOT_PDF_PATH = os.path.join(REPO_DIR, "WD_ABL_Consolidated_Report.pdf")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Suppress headers on cover page
        if self._pageNumber > 1:
            # Header
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#0f172a"))
            self.drawString(54, 750, "DR. RVR NRI INSTITUTE OF TECHNOLOGY")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawString(245, 750, "| Web Development Activity-Based Learning (ABL) Assignment")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.75)
            self.line(54, 742, 558, 742)

            # Footer
            self.setStrokeColor(colors.HexColor("#e2e8f0"))
            self.setLineWidth(0.75)
            self.line(54, 45, 558, 45)
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawString(54, 32, "Student: Yaswanth | Roll No: 26000918 | Branch: CSE (CSM1)")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(558, 32, page_text)
        self.restoreState()

def generate_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a'),
        alignment=1, # Center
        spaceAfter=6
    )

    inst_style = ParagraphStyle(
        'InstHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#1e40af'),
        alignment=1,
        spaceAfter=3
    )

    sub_inst = ParagraphStyle(
        'SubInst',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#475569'),
        alignment=1,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#0f172a'),
        backColor=colors.HexColor('#f8fafc'),
        borderColor=colors.HexColor('#e2e8f0'),
        borderWidth=1,
        borderPadding=6,
        spaceAfter=6
    )

    story = []

    # =========================================================================
    # FRONT COVER / HEADER
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("DR. RVR NRI INSTITUTE OF TECHNOLOGY", inst_style))
    story.append(Paragraph("An Institution deemed to be University u/s 3 of UGC Act, 1956<br/>School of Computer Studies • Department of Computer Science & Engineering<br/>Pothavarappadu (V), Agiripalli (M), Vijayawada Rural, Eluru District, AP - 521212", sub_inst))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1e40af'), spaceAfter=15))

    story.append(Paragraph("ACTIVITY-BASED LEARNING (ABL) ASSIGNMENT REPORT", title_style))
    story.append(Paragraph("<b>Course:</b> Web Development Lab (I B.Tech) &nbsp;|&nbsp; <b>Academic Session:</b> 2026-2027", ParagraphStyle('SubSub', parent=body_style, alignment=1, fontSize=10, textColor=colors.HexColor('#475569'))))
    story.append(Paragraph("<b>Circular Ref:</b> Web Development ABL / Dussehra Holidays Assignment (15-10-2026)", ParagraphStyle('SubRef', parent=body_style, alignment=1, fontSize=9, textColor=colors.HexColor('#64748b'), spaceAfter=15)))

    # Student Credentials Card Box
    cred_data = [
        [Paragraph("<b>Student Full Name:</b>", body_style), Paragraph("Yaswanth", body_style), Paragraph("<b>Academic Year / Sem:</b>", body_style), Paragraph("I B.Tech (2026-27)", body_style)],
        [Paragraph("<b>Roll Number:</b>", body_style), Paragraph("<b>26000918</b>", body_style), Paragraph("<b>Branch / Discipline:</b>", body_style), Paragraph("CSE (Computer Science)", body_style)],
        [Paragraph("<b>Class Section:</b>", body_style), Paragraph("<b>CSM1</b>", body_style), Paragraph("<b>Repository Name:</b>", body_style), Paragraph("WD-Activity-Based-Learning", body_style)]
    ]
    cred_table = Table(cred_data, colWidths=[120, 130, 120, 134])
    cred_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(cred_table)
    story.append(Spacer(1, 15))

    # Table of Selected 3 Case Studies
    story.append(Paragraph("Prescribed Case Studies Selection Overview", h2_style))
    summary_data = [
        ["No.", "Case Study Title", "Core Web Technologies", "Folder Location"],
        ["1", "Student Course Registration Portal", "HTML5, CSS3 Grid, DOM State, Credit Meter, Modal Receipt", "Case_01_Student_Course_Registration/"],
        ["2", "Campus Event & Tech-Fest Hub (TechVyuha)", "Event Filtering, Dynamic Forms, Fee & Pass Generation", "Case_02_Campus_Event_Management/"],
        ["3", "Online Book Store & Digital Central Library", "Live Search, Cart/Bag Management, 14-Day Due Dates", "Case_03_Online_Bookstore_and_Library/"]
    ]
    summary_table = Table(summary_data, colWidths=[26, 175, 175, 128])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e40af')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#ffffff')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')])
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 15))

    # Assignment Objectives
    story.append(Paragraph("<b>Assignment Objective & Scope:</b>", h2_style))
    story.append(Paragraph(
        "As communicated in the institutional circular dated 15-10-2026, students are instructed to design and build fully working web applications "
        "covering client-side architecture. Each solution incorporates semantic HTML5, responsive CSS3 layouts, interactive JavaScript DOM manipulations, "
        "form validation, and downloadable/printable confirmation receipts tailored for authentic university academic operations.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # CASE STUDY 1
    # =========================================================================
    story.append(Paragraph("Case Study 1: Student Course Registration Portal", h1_style))
    story.append(Paragraph("<b>Directory:</b> <code>Case_01_Student_Course_Registration/</code> &nbsp;|&nbsp; <b>Primary Files:</b> <code>index.html</code>, <code>style.css</code>, <code>app.js</code>", ParagraphStyle('SubSub2', parent=body_style, fontSize=8, textColor=colors.HexColor('#64748b'))))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#cbd5e1'), spaceAfter=8))

    story.append(Paragraph("<b>1. Problem Statement & Academic Context:</b>", h2_style))
    story.append(Paragraph(
        "In university credit-based academic systems (such as CBCS at Dr. RVR NRIIT), undergraduate students in the School of Computer Studies "
        "must enroll in courses for the upcoming semester while strictly adhering to institutional workload limitations (Minimum 16 credits, "
        "Maximum 24 credits). The goal of this case study is to provide an interactive, intuitive course enrollment portal that calculates real-time "
        "credit points, dynamically assesses tuition/lab dues, verifies prerequisites, and provides a formal semester registration slip.",
        body_style
    ))

    story.append(Paragraph("<b>2. Key Functional & Technical Implementations:</b>", h2_style))
    story.append(Paragraph(
        "• <b>Live Credit Counter & Progress Bar:</b> Dynamic progress calculation with automated alerts preventing enrollment exceeding 24 credits.<br/>"
        "• <b>Category Filtering:</b> Instant client-side filtering between Core Subjects, Professional Electives, and Laboratory Courses.<br/>"
        "• <b>Fee Breakdown Calculation:</b> Real-time computation of tuition fees and laboratory consumables based on selected courses.<br/>"
        "• <b>Official Registration Slip Modal:</b> Generation of a formal digital slip with Roll No: <b>26000918</b>, Student Name: <b>Yaswanth</b>, and Section: <b>CSM1</b> with print capability.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>3. Visual Execution Screenshots:</b>", h2_style))

    # Screenshot 1: Main Portal
    img_cs1_main = os.path.join(SCREENSHOTS_DIR, "case_01_main_portal.png")
    if os.path.exists(img_cs1_main):
        story.append(RLImage(img_cs1_main, width=500, height=270))
        story.append(Paragraph("<i>Figure 1.1: Case Study 1 — Course Catalog, Category Filter & Live Credit Workload Meter</i>", ParagraphStyle('Cap', parent=body_style, alignment=1, fontSize=7.5, textColor=colors.HexColor('#64748b'))))

    story.append(Spacer(1, 6))

    # Screenshot 2: Modal
    img_cs1_modal = os.path.join(SCREENSHOTS_DIR, "case_01_modal_receipt.png")
    if os.path.exists(img_cs1_modal):
        story.append(RLImage(img_cs1_modal, width=460, height=250))
        story.append(Paragraph("<i>Figure 1.2: Case Study 1 — Verified Registration Confirmation Slip Modal Dialog</i>", ParagraphStyle('Cap2', parent=body_style, alignment=1, fontSize=7.5, textColor=colors.HexColor('#64748b'))))

    story.append(PageBreak())

    # =========================================================================
    # CASE STUDY 2
    # =========================================================================
    story.append(Paragraph("Case Study 2: Campus Event & Tech-Fest Hub (TechVyuha '26)", h1_style))
    story.append(Paragraph("<b>Directory:</b> <code>Case_02_Campus_Event_Management/</code> &nbsp;|&nbsp; <b>Primary Files:</b> <code>index.html</code>, <code>style.css</code>, <code>app.js</code>", ParagraphStyle('SubSub3', parent=body_style, fontSize=8, textColor=colors.HexColor('#64748b'))))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#cbd5e1'), spaceAfter=8))

    story.append(Paragraph("<b>1. Problem Statement & Functional Goals:</b>", h2_style))
    story.append(Paragraph(
        "Annual technical symposiums like <i>TechVyuha '26</i> require a high-throughput event discovery and registration platform where students can "
        "explore technical hackathons, speed coding contests, paper presentations, and gaming arenas. The platform must handle dynamic team formation, "
        "track seat availability in real time, collect participant credentials, and issue verified digital event passes with unique pass IDs.",
        body_style
    ))

    story.append(Paragraph("<b>2. Key Technical Implementations:</b>", h2_style))
    story.append(Paragraph(
        "• <b>Live Multi-Attribute Filtering & Search:</b> Instant real-time search by keywords, venues, and category chips.<br/>"
        "• <b>Adaptive Team Member Generation:</b> Dynamically generates team member input rows according to each event's maximum team size.<br/>"
        "• <b>Seat Inventory Management:</b> Updates available slot tallies on successful registration.<br/>"
        "• <b>Digital E-Ticket Pass:</b> Renders an official tech-fest pass with QR-code placeholder, unique pass ID (e.g. <code>NRIIT-TV26-8918</code>), venue timings, and candidate verification badge.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>3. Visual Execution Screenshots:</b>", h2_style))

    img_cs2_main = os.path.join(SCREENSHOTS_DIR, "case_02_techfest_portal.png")
    if os.path.exists(img_cs2_main):
        story.append(RLImage(img_cs2_main, width=500, height=270))
        story.append(Paragraph("<i>Figure 2.1: Case Study 2 — TechVyuha '26 Event Hub with Live Filters and Prize Badges</i>", ParagraphStyle('Cap3', parent=body_style, alignment=1, fontSize=7.5, textColor=colors.HexColor('#64748b'))))

    story.append(Spacer(1, 6))

    img_cs2_pass = os.path.join(SCREENSHOTS_DIR, "case_02_digital_pass.png")
    if os.path.exists(img_cs2_pass):
        story.append(RLImage(img_cs2_pass, width=440, height=255))
        story.append(Paragraph("<i>Figure 2.2: Case Study 2 — Generated Verified Digital Entry Pass with Unique Pass ID & QR</i>", ParagraphStyle('Cap4', parent=body_style, alignment=1, fontSize=7.5, textColor=colors.HexColor('#64748b'))))

    story.append(PageBreak())

    # =========================================================================
    # CASE STUDY 3
    # =========================================================================
    story.append(Paragraph("Case Study 3: Online Book Store & Digital Library Catalog", h1_style))
    story.append(Paragraph("<b>Directory:</b> <code>Case_03_Online_Bookstore_and_Library/</code> &nbsp;|&nbsp; <b>Primary Files:</b> <code>index.html</code>, <code>style.css</code>, <code>app.js</code>", ParagraphStyle('SubSub4', parent=body_style, fontSize=8, textColor=colors.HexColor('#64748b'))))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#cbd5e1'), spaceAfter=8))

    story.append(Paragraph("<b>1. Problem Statement & Library Workflow:</b>", h2_style))
    story.append(Paragraph(
        "Academic institutions maintain extensive inventories of technical reference books across diverse engineering disciplines. "
        "The Dr. RVR NRIIT Central E-Library application enables students to browse textbooks, check physical shelf rack locations, "
        "manage a borrowing cart (Reading Bag) constrained to 3 books, enforce 14-day return due dates, and track active loans.",
        body_style
    ))

    story.append(Paragraph("<b>2. Key Technical Implementations:</b>", h2_style))
    story.append(Paragraph(
        "• <b>Real-time Book Search & Discipline Chips:</b> Search catalog by book title, author, or ISBN.<br/>"
        "• <b>Reading Bag Drawer:</b> Sliding side drawer managing borrowed volumes with capacity validation (Max 3 books).<br/>"
        "• <b>Automated Due Date Calculation:</b> Computes exact 14-day return deadlines and outlines late fee regulations.<br/>"
        "• <b>Circulation Receipt & Active Loan Tracker:</b> Generates library borrowing receipts and allows one-click book returns.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>3. Visual Execution Screenshots:</b>", h2_style))

    img_cs3_main = os.path.join(SCREENSHOTS_DIR, "case_03_library_portal.png")
    if os.path.exists(img_cs3_main):
        story.append(RLImage(img_cs3_main, width=500, height=270))
        story.append(Paragraph("<i>Figure 3.1: Case Study 3 — Central E-Library Catalog with Shelf Locations & Discipline Chips</i>", ParagraphStyle('Cap5', parent=body_style, alignment=1, fontSize=7.5, textColor=colors.HexColor('#64748b'))))

    story.append(Spacer(1, 6))

    img_cs3_slip = os.path.join(SCREENSHOTS_DIR, "case_03_circulation_slip.png")
    if os.path.exists(img_cs3_slip):
        story.append(RLImage(img_cs3_slip, width=440, height=255))
        story.append(Paragraph("<i>Figure 3.2: Case Study 3 — Official 14-Day Library Circulation Receipt Dialog</i>", ParagraphStyle('Cap6', parent=body_style, alignment=1, fontSize=7.5, textColor=colors.HexColor('#64748b'))))

    story.append(PageBreak())

    # =========================================================================
    # REPOSITORY STRUCTURE & SUBMISSION DETAILS
    # =========================================================================
    story.append(Paragraph("Repository Organisation & GitHub Submission Guide", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#cbd5e1'), spaceAfter=10))

    story.append(Paragraph("<b>GitHub Repository Name:</b> <code>WD-Activity-Based-Learning</code>", h2_style))
    story.append(Paragraph(
        "In strict compliance with <b>Instruction #3</b> of the circular, all code, screenshots, and this consolidated report "
        "are organized inside a clean GitHub repository. The folder structure is laid out as follows:",
        body_style
    ))

    tree_text = (
        "WD-Activity-Based-Learning/\n"
        "├── Case_01_Student_Course_Registration/\n"
        "│   ├── index.html        (Semantic layout, filters, course grid, summary & modal slip)\n"
        "│   ├── style.css         (Custom styling, responsive CSS Grid/Flexbox, cards & badges)\n"
        "│   └── app.js            (Dynamic rendering, credit limit validation, fee calculation)\n"
        "├── Case_02_Campus_Event_Management/\n"
        "│   ├── index.html        (Hero banner, event arenas, search bar, registration modal)\n"
        "│   ├── style.css         (Tech-fest aesthetic, event cards, digital pass styling)\n"
        "│   └── app.js            (Filtering, dynamic team fields, unique Pass ID generation)\n"
        "├── Case_03_Online_Bookstore_and_Library/\n"
        "│   ├── index.html        (Textbook catalog, reading bag drawer, circulation receipt)\n"
        "│   ├── style.css         (Academic design, book spine covers, drawer transitions)\n"
        "│   └── app.js            (Catalog search, 3-book limit, 14-day due date computation)\n"
        "├── screenshots/          (High-resolution browser execution screenshots)\n"
        "├── reports/\n"
        "│   └── WD_ABL_Consolidated_Report.pdf  (Official consolidated submission PDF)\n"
        "└── README.md             (Student details, selected case study titles & setup guide)"
    )
    story.append(Paragraph(tree_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))

    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Student Declaration & Verification:</b>", h2_style))
    story.append(Paragraph(
        "I hereby declare that the three case studies presented in this report and uploaded to the GitHub repository "
        "<code>WD-Activity-Based-Learning</code> were designed and developed independently by me as part of the Web Development "
        "Activity-Based Learning (ABL) course assignment during the Dussehra vacation. All code, design structures, and logic "
        "are authentic and ready for live demonstration before the faculty evaluation committee.",
        body_style
    ))

    story.append(Spacer(1, 15))
    sig_data = [
        [Paragraph("<b>Student Signature:</b>", body_style), Paragraph("<b>Faculty / Mentor Evaluation:</b>", body_style)],
        [Paragraph("<i>(Yaswanth)</i><br/>Roll No: <b>26000918</b><br/>Section: <b>CSM1</b> | Branch: <b>CSE</b><br/>Dr. RVR NRI Institute of Technology", body_style),
         Paragraph("Marks Awarded: <b>____ / 10 Marks</b><br/>Signature: _______________________<br/>Date: ___________________________", body_style)]
    ]
    sig_table = Table(sig_data, colWidths=[250, 254])
    sig_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(sig_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Consolidated PDF generated at:", PDF_PATH)

    # Also copy to root for ease of access
    import shutil
    shutil.copyfile(PDF_PATH, ROOT_PDF_PATH)
    print("Copied to root:", ROOT_PDF_PATH)

if __name__ == "__main__":
    generate_pdf()
