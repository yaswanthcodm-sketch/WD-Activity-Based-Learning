import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = "/Users/yaswanth/.gemini/antigravity/scratch/WD-Activity-Based-Learning"
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
PDF_PATH = os.path.join(BASE_DIR, "Consolidated_Report.pdf")

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
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, total_pages):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#0f2942"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, "Dr. RVR NRI INSTITUTE OF TECHNOLOGY  |  Web Development Activity-Based Learning (ABL)")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawRightString(558, 755, "Student: Yaswanth Avirneni (26000918, CSM-1)")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.75)
            self.line(54, 748, 558, 748)
            
        # Footer
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.75)
        self.line(54, 45, 558, 45)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(54, 32, "Deemed to be University u/s 3 of UGC Act, 1956  •  Department of CSE (AI & ML)")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(558, 32, page_str)
        self.restoreState()

def build_pdf():
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
    univ_head = ParagraphStyle(
        'UnivHead',
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#0f2942'),
        alignment=1
    )
    univ_sub = ParagraphStyle(
        'UnivSub',
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#475569'),
        alignment=1
    )
    doc_title = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1e40af'),
        alignment=1,
        spaceAfter=8
    )
    h1_style = ParagraphStyle(
        'H1Style',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0f2942'),
        spaceBefore=14,
        spaceAfter=6
    )
    h2_style = ParagraphStyle(
        'H2Style',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#1e40af'),
        spaceBefore=10,
        spaceAfter=4
    )
    body = ParagraphStyle(
        'Body',
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=6
    )
    body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#0f172a')
    )
    code_snippet = ParagraphStyle(
        'CodeSnippet',
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#0f172a')
    )

    elements = []

    # ================= COVER / HEADER =================
    elements.append(Paragraph("Dr. RVR NRI INSTITUTE OF TECHNOLOGY", univ_head))
    elements.append(Paragraph("An Institution deemed to be University u/s 3 of UGC Act, 1956", univ_sub))
    elements.append(Paragraph("Sponsored by Sri Durga Malleswari Educational Society", univ_sub))
    elements.append(Paragraph("Pothavarappadu (V), Agiripalli (M), Vijayawada Rural, Eluru District, Andhra Pradesh", univ_sub))
    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1e40af'), spaceAfter=14))
    
    elements.append(Paragraph("Web Development Activity-Based Learning (ABL)", doc_title))
    elements.append(Paragraph("<b>Consolidated Academic Project & Implementation Report (Pure HTML5 & CSS3)</b>", ParagraphStyle('Sub', alignment=1, fontSize=10, textColor=colors.HexColor('#475569'), spaceAfter=14)))

    # Student Info Table
    info_data = [
        [Paragraph("<b>Student Full Name:</b>", body), Paragraph("<b>Yaswanth Avirneni</b>", body_bold), Paragraph("<b>Academic Year:</b>", body), Paragraph("2026–2027 (I B.Tech)", body)],
        [Paragraph("<b>Roll Number:</b>", body), Paragraph("<b>26000918</b>", body_bold), Paragraph("<b>Class Section:</b>", body), Paragraph("<b>CSM - 1</b>", body_bold)],
        [Paragraph("<b>Department / Branch:</b>", body), Paragraph("CSE (Artificial Intelligence & ML)", body), Paragraph("<b>Course & Lab:</b>", body), Paragraph("Web Development (10 Marks)", body)],
        [Paragraph("<b>GitHub Repository:</b>", body), Paragraph("<code>yaswanthcodm-sketch/WD-Activity-Based-Learning</code>", body), Paragraph("<b>Technology Stack:</b>", body), Paragraph("Pure Semantic HTML5 & Responsive CSS3", body)]
    ]
    info_table = Table(info_data, colWidths=[120, 150, 110, 124])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(info_table)
    elements.append(Spacer(1, 14))

    # Abstract / Executive Overview
    elements.append(Paragraph("Executive Overview of Selected Case Studies", h1_style))
    elements.append(Paragraph("In accordance with the Dr. RVR NRI Institute of Technology Web Development curriculum, three distinct, feature-complete case studies have been selected, designed, and developed from the prescribed institutional syllabus. All three web applications strictly adhere to <b>100% Pure Semantic HTML5 and Modern CSS3</b> without external JavaScript libraries, ensuring high performance, pristine accessibility, and responsive fidelity.", body))

    summary_table_data = [
        [Paragraph("<b>S.No</b>", body_bold), Paragraph("<b>Syllabus Title</b>", body_bold), Paragraph("<b>Directory</b>", body_bold), Paragraph("<b>Key Architectural Concepts</b>", body_bold)],
        [Paragraph("01", body), Paragraph("<b>Case 4: Student Academic Dashboard</b>", body), Paragraph("<code>academic-dashboard/</code>", body), Paragraph("Sidebar layout, attendance progress bars, tabular semester grades, KPI metric cards, examination schedule, notice board.", body)],
        [Paragraph("02", body), Paragraph("<b>Case 3: Online Learning Platform Interface</b>", body), Paragraph("<code>elearning-platform/</code>", body), Paragraph("Course discovery catalog, video lesson thumbnails, instructor credentials, learning objectives, pure CSS :target modal enrollment.", body)],
        [Paragraph("03", body), Paragraph("<b>Case 11: Hospital & Healthcare Services</b>", body), Paragraph("<code>healthcare-portal/</code>", body), Paragraph("24/7 trauma emergency bar, multi-specialty clinical departments, doctors OPD timetable, visiting hours matrix, accessible appointment request form.", body)]
    ]
    summary_table = Table(summary_table_data, colWidths=[35, 150, 110, 209])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e40af')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(summary_table)

    elements.append(PageBreak())

    # ================= CASE STUDY 1: STUDENT ACADEMIC DASHBOARD =================
    elements.append(Paragraph("1. Case Study 4: Student Academic Dashboard", h1_style))
    elements.append(Paragraph("<b>Directory:</b> <code>academic-dashboard/</code> | <b>Files:</b> <code>index.html</code>, <code>style.css</code>", h2_style))
    elements.append(Paragraph("<b>Problem Definition & Scope:</b> Design an administrative student dashboard displaying comprehensive profile metadata, subject-wise attendance percentages with eligibility thresholds, semester examination results, upcoming exam timetables, and departmental notices using CSS Flexbox, CSS Grid, custom progress bars, and a modern sidebar layout.", body))

    elements.append(Paragraph("<b>Key Technical Capabilities Implemented:</b>", body_bold))
    elements.append(Paragraph("• <b>Fixed Sidebar Layout:</b> Modern navigation sidebar containing the university badge, student avatar (YA), roll number (26000918), section (CSM-1), and smooth-scroll anchor links.<br/>"
                              "• <b>KPI Metrics Cards:</b> 4 distinct analytical summary boxes showcasing Registered Credits (21 Cr), Attendance (88.5%), SGPA (9.36), and upcoming Mid-Term II alerts.<br/>"
                              "• <b>Dynamic Attendance Progress Bars:</b> CSS progress bars with conditional color fills (safe green vs warning amber) and session statistics for all enrolled subjects.<br/>"
                              "• <b>Structured Semester Grade Table:</b> Responsive tabular data presentation showing course codes, internal (40), external (60), total marks, grade points, and letter grades.<br/>"
                              "• <b>Examination Schedule & Circular Notice Board:</b> Date badge cards for mid-term exams and priority-coded urgent department notifications.", body))

    elements.append(Spacer(1, 6))
    dash_img_path = os.path.join(SCREENSHOTS_DIR, "academic_dashboard_preview.png")
    if os.path.exists(dash_img_path):
        elements.append(Paragraph("<b>Interface Render Screenshot (Academic Dashboard):</b>", body_bold))
        elements.append(Image(dash_img_path, width=504, height=315))
    
    elements.append(PageBreak())

    # ================= CASE STUDY 2: ONLINE LEARNING PLATFORM =================
    elements.append(Paragraph("2. Case Study 3: Online Learning Platform Interface", h1_style))
    elements.append(Paragraph("<b>Directory:</b> <code>elearning-platform/</code> | <b>Files:</b> <code>index.html</code>, <code>style.css</code>", h2_style))
    elements.append(Paragraph("<b>Problem Definition & Scope:</b> Develop a full-featured e-learning web interface containing course disciplines, video lesson thumbnails with playback indicators, verified instructor profiles, structured learning objectives, and responsive enrollment cards with active learning progress indicators.", body))

    elements.append(Paragraph("<b>Key Technical Capabilities Implemented:</b>", body_bold))
    elements.append(Paragraph("• <b>Active Learning Track Hero Card:</b> Real-time session tracker highlighting current lesson progress (68% complete, 18/26 lessons) with progress indicators.<br/>"
                              "• <b>Video Lesson Cards:</b> Rich thumbnail cards with gradient backdrops, play trigger overlays, duration badges (e.g. 18h 45m), and tech-stack chips.<br/>"
                              "• <b>Structured Learning Objectives:</b> Dedicated learning outcomes breakdown for each course (NumPy, Scikit-Learn, PyTorch, Docker, CSS Grid).<br/>"
                              "• <b>Pure CSS Modal Interactivity:</b> Implemented enrollment syllabus popups and enrollment confirmation dialogs using pure CSS <code>:target</code> pseudo-class selectors with zero JavaScript dependency.<br/>"
                              "• <b>Instructor Directory & Star Ratings:</b> Faculty profiles with verified designations, student enrollments, and academic ratings.", body))

    elements.append(Spacer(1, 6))
    elearn_img_path = os.path.join(SCREENSHOTS_DIR, "elearning_platform_preview.png")
    if os.path.exists(elearn_img_path):
        elements.append(Paragraph("<b>Interface Render Screenshot (Online Learning Platform):</b>", body_bold))
        elements.append(Image(elearn_img_path, width=504, height=315))

    elements.append(PageBreak())

    # ================= CASE STUDY 3: HOSPITAL & HEALTHCARE SERVICES =================
    elements.append(Paragraph("3. Case Study 11: Hospital and Healthcare Services Website", h1_style))
    elements.append(Paragraph("<b>Directory:</b> <code>healthcare-portal/</code> | <b>Files:</b> <code>index.html</code>, <code>style.css</code>", h2_style))
    elements.append(Paragraph("<b>Problem Definition & Scope:</b> Create a tertiary hospital web portal presenting clinical departments, specialist physician directories, diagnostic facilities, visiting hours regulations, 24/7 trauma emergency contact details, and an accessible appointment request form.", body))

    elements.append(Paragraph("<b>Key Technical Capabilities Implemented:</b>", body_bold))
    elements.append(Paragraph("• <b>24/7 Emergency Trauma Bar:</b> Urgent red alert header with pulsating status dot and emergency hotline (9640334422 / 1800-NRIIT-CARE).<br/>"
                              "• <b>Clinical Departments Grid:</b> Comprehensive medical department cards (Cardiology, Neurology, Orthopedics, Pediatrics, Pulmonology, Intensive Care).<br/>"
                              "• <b>Doctor Specialist Directory:</b> Detailed consultant physician profiles with credentials, OPD suite numbers, consultation schedules, and availability tags.<br/>"
                              "• <b>Inpatient Visiting Hours Matrix:</b> Structured table displaying ward-specific visiting windows, attendant limits, and visitor pass regulations.<br/>"
                              "• <b>Accessible Appointment Request Form:</b> Semantic HTML form with accessible <code>&lt;label&gt;</code> tags, pattern-matched phone number inputs, required selects, date pickers, priority radios, and pure CSS confirmation receipt.", body))

    elements.append(Spacer(1, 6))
    health_img_path = os.path.join(SCREENSHOTS_DIR, "healthcare_portal_preview.png")
    if os.path.exists(health_img_path):
        elements.append(Paragraph("<b>Interface Render Screenshot (Hospital & Healthcare Services):</b>", body_bold))
        elements.append(Image(health_img_path, width=504, height=315))

    elements.append(PageBreak())

    # ================= EVALUATION & VERIFICATION =================
    elements.append(Paragraph("4. Academic Evaluation Rubric & Faculty Assessment Sheet", h1_style))
    elements.append(Paragraph("Web Development Activity-Based Learning Evaluation (Total: 10 Marks)", body_bold))
    
    rubric_data = [
        [Paragraph("<b>Evaluation Parameter</b>", body_bold), Paragraph("<b>Max Marks</b>", body_bold), Paragraph("<b>Implementation Standard Achieved</b>", body_bold), Paragraph("<b>Awarded</b>", body_bold)],
        [Paragraph("<b>Semantic HTML5 Structure</b>", body), Paragraph("2.5", body), Paragraph("Extensive use of semantic tags (<code>&lt;header&gt;</code>, <code>&lt;aside&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;section&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;table&gt;</code>, <code>&lt;form&gt;</code>).", body), Paragraph("___ / 2.5", body)],
        [Paragraph("<b>CSS3 Styling, Flexbox & Grid</b>", body), Paragraph("2.5", body), Paragraph("Modern CSS custom properties, responsive multi-column layouts, smooth card hover transitions, and progress bar animations.", body), Paragraph("___ / 2.5", body)],
        [Paragraph("<b>Responsive UI & Accessibility</b>", body), Paragraph("2.5", body), Paragraph("Fluid media queries across mobile, tablet, and desktop viewports; accessible form controls and clear visual hierarchy.", body), Paragraph("___ / 2.5", body)],
        [Paragraph("<b>Functional Completeness & Case Coverage</b>", body), Paragraph("2.5", body), Paragraph("Exact alignment with Case Studies 4, 3, and 11 from the Dr. RVR NRIIT curriculum sheet, documentation, and repository.", body), Paragraph("___ / 2.5", body)],
        [Paragraph("<b>Total Score</b>", body_bold), Paragraph("<b>10.0</b>", body_bold), Paragraph("<b>Comprehensive Web Development Activity Submission</b>", body_bold), Paragraph("<b>___ / 10</b>", body_bold)]
    ]
    rubric_table = Table(rubric_data, colWidths=[130, 60, 240, 74])
    rubric_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f2942')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(rubric_table)

    elements.append(Spacer(1, 35))
    
    # Signature Section
    sig_data = [
        [Paragraph("<b>Student Signature:</b><br/><br/>_______________________<br/><b>Yaswanth Avirneni</b><br/>Roll No: 26000918<br/>Section: CSM - 1<br/>CSE (AI & ML), NRIIT", body),
         Paragraph("<b>Evaluator / Faculty Signature:</b><br/><br/>_______________________<br/><b>Faculty of Web Development</b><br/>Department of Computer Science & Engineering<br/>Dr. RVR NRI Institute of Technology", body)]
    ]
    sig_table = Table(sig_data, colWidths=[252, 252])
    sig_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
    ]))
    elements.append(sig_table)

    doc.build(elements, canvasmaker=NumberedCanvas)
    print("PDF Successfully Generated:", PDF_PATH)

if __name__ == "__main__":
    build_pdf()
