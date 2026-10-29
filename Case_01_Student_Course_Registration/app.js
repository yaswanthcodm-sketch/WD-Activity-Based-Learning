/**
 * Dr. RVR NRI Institute of Technology
 * Course Registration Portal - Logic & Interactivity
 * Student: Yaswanth | Roll No: 26000918 | Branch: CSE (CSM1)
 */

// Course catalog dataset
const coursesData = [
  {
    id: "CS301",
    code: "26CS301",
    title: "Data Structures & Algorithms",
    category: "Core",
    credits: 4,
    faculty: "Dr. K. Srinivas Rao",
    schedule: "Mon, Wed, Fri (09:00 - 10:00 AM)",
    room: "CS-Hall 102",
    description: "Core concepts of linear and non-linear data structures, trees, graphs, and algorithmic complexity.",
    tuition: 3000,
    labFee: 500
  },
  {
    id: "CS302",
    code: "26CS302",
    title: "Web Development Technologies",
    category: "Core",
    credits: 3,
    faculty: "Prof. M. Lakshmi",
    schedule: "Tue, Thu (10:15 - 11:45 AM)",
    room: "Lab-3 / Web Center",
    description: "Modern frontend semantics, CSS Grid/Flexbox, DOM manipulation, responsive UI, and client-side logic.",
    tuition: 2500,
    labFee: 1000
  },
  {
    id: "CS303",
    code: "26CS303",
    title: "Discrete Mathematics",
    category: "Core",
    credits: 4,
    faculty: "Dr. P. V. Ramana",
    schedule: "Mon, Wed, Fri (11:00 - 12:00 PM)",
    room: "CS-Hall 201",
    description: "Mathematical logic, sets, relations, combinatorics, graph theory, and recurrence relations.",
    tuition: 3000,
    labFee: 0
  },
  {
    id: "CS304",
    code: "26CS304",
    title: "Artificial Intelligence & ML",
    category: "Elective",
    credits: 3,
    faculty: "Dr. A. Sudhir Babu",
    schedule: "Tue, Thu (01:30 - 03:00 PM)",
    room: "AI Specialization Lab",
    description: "Introduction to intelligent agents, search algorithms, heuristic methods, and predictive modeling.",
    tuition: 3200,
    labFee: 800
  },
  {
    id: "CS305",
    code: "26CS305",
    title: "Python for Data Science",
    category: "Elective",
    credits: 3,
    faculty: "Prof. N. Chaitanya",
    schedule: "Wed, Fri (02:00 - 03:30 PM)",
    room: "Computing Lab 1",
    description: "Data analysis workflows using NumPy, Pandas, visualization libraries, and exploratory data analysis.",
    tuition: 2800,
    labFee: 600
  },
  {
    id: "CS306",
    code: "26CS306",
    title: "Computer Networks & Security",
    category: "Elective",
    credits: 3,
    faculty: "Prof. G. Rajesh",
    schedule: "Mon, Thu (03:00 - 04:30 PM)",
    room: "Networks Lab",
    description: "OSI reference model, TCP/IP protocol suite, subnetting, network layer routing, and crypto basics.",
    tuition: 2800,
    labFee: 700
  },
  {
    id: "CS307",
    code: "26CS307L",
    title: "Data Structures Laboratory",
    category: "Lab",
    credits: 1.5,
    faculty: "Prof. K. Sandhya",
    schedule: "Mon (01:30 - 04:30 PM)",
    room: "Advanced Programming Lab",
    description: "Hands-on implementation of linked lists, stacks, queues, binary trees, sorting, and graph traversals.",
    tuition: 1000,
    labFee: 1500
  },
  {
    id: "CS308",
    code: "26CS308L",
    title: "Web Development Hands-on Lab",
    category: "Lab",
    credits: 1.5,
    faculty: "Prof. M. Lakshmi",
    schedule: "Thu (01:30 - 04:30 PM)",
    room: "Web Development Lab",
    description: "Building responsive websites, practical DOM scripting, asynchronous events, and activity-based projects.",
    tuition: 1000,
    labFee: 1500
  }
];

// Application State
const MIN_CREDITS = 16;
const MAX_CREDITS = 24;
let enrolledCourseIds = new Set();
let currentFilter = "all";

// DOM Elements
const coursesGrid = document.getElementById("coursesGrid");
const enrolledList = document.getElementById("enrolledList");
const creditValue = document.getElementById("creditValue");
const creditProgressBar = document.getElementById("creditProgressBar");
const creditStatusMsg = document.getElementById("creditStatusMsg");
const selectedCountBadge = document.getElementById("selectedCountBadge");
const tuitionFeeText = document.getElementById("tuitionFeeText");
const labFeeText = document.getElementById("labFeeText");
const totalFeeText = document.getElementById("totalFeeText");
const declarationCheck = document.getElementById("declarationCheck");
const btnSubmitRegistration = document.getElementById("btnSubmitRegistration");
const filterButtons = document.querySelectorAll(".filter-btn");

// Modal Elements
const confirmModal = document.getElementById("confirmModal");
const slipTableBody = document.getElementById("slipTableBody");
const slipTotalCredits = document.getElementById("slipTotalCredits");
const slipDate = document.getElementById("slipDate");
const btnPrintSlip = document.getElementById("btnPrintSlip");
const btnCloseModal = document.getElementById("btnCloseModal");
const toast = document.getElementById("toast");

// Initialize application
document.addEventListener("DOMContentLoaded", () => {
  renderCourses();
  updateSummary();
  setupFilterListeners();
  setupActionListeners();
});

// Render course cards based on active filter
function renderCourses() {
  coursesGrid.innerHTML = "";

  const filtered = coursesData.filter(course => {
    if (currentFilter === "all") return true;
    return course.category.toLowerCase() === currentFilter.toLowerCase();
  });

  filtered.forEach(course => {
    const isEnrolled = enrolledCourseIds.has(course.id);
    const card = document.createElement("div");
    card.className = `course-card ${isEnrolled ? "selected" : ""}`;

    const tagClass = 
      course.category === "Core" ? "tag-core" :
      course.category === "Elective" ? "tag-elective" : "tag-lab";

    card.innerHTML = `
      <div>
        <div class="card-top">
          <span class="course-code">${course.code}</span>
          <span class="category-tag ${tagClass}">${course.category}</span>
        </div>
        <h4>${course.title}</h4>
        <p class="course-desc">${course.description}</p>
        <div class="course-details">
          <span><strong>Faculty:</strong> ${course.faculty}</span>
          <span><strong>Schedule:</strong> ${course.schedule}</span>
          <span><strong>Venue:</strong> ${course.room}</span>
        </div>
      </div>
      <div class="card-footer">
        <span class="credits-badge">${course.credits} Credits</span>
        <button class="btn btn-sm ${isEnrolled ? "btn-danger" : "btn-primary"}" onclick="toggleCourse('${course.id}')">
          ${isEnrolled ? "Remove Course" : "+ Add Course"}
        </button>
      </div>
    `;

    coursesGrid.appendChild(card);
  });
}

// Toggle course enrollment
window.toggleCourse = function(courseId) {
  const course = coursesData.find(c => c.id === courseId);
  if (!course) return;

  if (enrolledCourseIds.has(courseId)) {
    enrolledCourseIds.delete(courseId);
    showToast(`Removed "${course.title}" from selection`);
  } else {
    // Check credit limit before adding
    const currentTotal = calculateTotalCredits();
    if (currentTotal + course.credits > MAX_CREDITS) {
      showToast(`Cannot add! Exceeds maximum limit of ${MAX_CREDITS} credits`, true);
      return;
    }
    enrolledCourseIds.add(courseId);
    showToast(`Added "${course.title}" (${course.credits} Cr)`);
  }

  renderCourses();
  updateSummary();
};

// Calculate total enrolled credits
function calculateTotalCredits() {
  let total = 0;
  enrolledCourseIds.forEach(id => {
    const course = coursesData.find(c => c.id === id);
    if (course) total += course.credits;
  });
  return total;
}

// Update Right-Hand Summary Panel
function updateSummary() {
  const totalCredits = calculateTotalCredits();
  const count = enrolledCourseIds.size;

  selectedCountBadge.textContent = `${count} Course${count === 1 ? "" : "s"}`;
  creditValue.textContent = `${totalCredits} / ${MAX_CREDITS}`;

  // Progress Bar
  const pct = Math.min(100, Math.round((totalCredits / MAX_CREDITS) * 100));
  creditProgressBar.style.width = `${pct}%`;

  // Status message
  if (totalCredits < MIN_CREDITS) {
    const needed = (MIN_CREDITS - totalCredits).toFixed(1).replace(".0", "");
    creditStatusMsg.className = "status-warning";
    creditStatusMsg.textContent = `Need ${needed} more credits to meet minimum`;
  } else if (totalCredits <= MAX_CREDITS) {
    creditStatusMsg.className = "status-valid";
    creditStatusMsg.textContent = "Credit requirement met! Ready to register";
  } else {
    creditStatusMsg.className = "status-error";
    creditStatusMsg.textContent = "Credit limit exceeded!";
  }

  // Enrolled list items
  if (count === 0) {
    enrolledList.innerHTML = `<li class="empty-state">No courses added yet. Please select courses from the left panel.</li>`;
  } else {
    enrolledList.innerHTML = "";
    enrolledCourseIds.forEach(id => {
      const course = coursesData.find(c => c.id === id);
      const li = document.createElement("li");
      li.className = "enrolled-item";
      li.innerHTML = `
        <div class="item-left" title="${course.title}">
          <span>•</span>
          <span><strong>${course.code}</strong>: ${course.title}</span>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="item-credits">${course.credits} Cr</span>
          <button class="btn-remove" onclick="toggleCourse('${course.id}')" title="Remove course">&times;</button>
        </div>
      `;
      enrolledList.appendChild(li);
    });
  }

  // Fee calculation
  let tuition = 0;
  let lab = 0;
  enrolledCourseIds.forEach(id => {
    const c = coursesData.find(item => item.id === id);
    if (c) {
      tuition += c.tuition;
      lab += c.labFee;
    }
  });

  tuitionFeeText.textContent = `₹ ${tuition.toLocaleString('en-IN')}`;
  labFeeText.textContent = `₹ ${lab.toLocaleString('en-IN')}`;
  totalFeeText.textContent = `₹ ${(tuition + lab).toLocaleString('en-IN')}`;

  // Validate Submit button
  const isValid = (totalCredits >= MIN_CREDITS && totalCredits <= MAX_CREDITS && declarationCheck.checked);
  btnSubmitRegistration.disabled = !isValid;
}

// Category filter button listeners
function setupFilterListeners() {
  filterButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      filterButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentFilter = btn.getAttribute("data-category");
      renderCourses();
    });
  });
}

// Form and Modal Actions
function setupActionListeners() {
  declarationCheck.addEventListener("change", () => {
    updateSummary();
  });

  btnSubmitRegistration.addEventListener("click", () => {
    openConfirmationModal();
  });

  btnCloseModal.addEventListener("click", () => {
    confirmModal.classList.remove("active");
  });

  btnPrintSlip.addEventListener("click", () => {
    window.print();
  });
}

// Populate and Open Registration Confirmation Slip Modal
function openConfirmationModal() {
  slipTableBody.innerHTML = "";
  const now = new Date();
  slipDate.textContent = now.toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric"
  });

  enrolledCourseIds.forEach(id => {
    const c = coursesData.find(item => item.id === id);
    const row = document.createElement("tr");
    row.innerHTML = `
      <td><strong>${c.code}</strong></td>
      <td>${c.title}</td>
      <td>${c.category}</td>
      <td><strong>${c.credits}</strong></td>
    `;
    slipTableBody.appendChild(row);
  });

  slipTotalCredits.textContent = calculateTotalCredits();
  confirmModal.classList.add("active");
}

// Show Toast feedback
function showToast(message, isError = false) {
  toast.textContent = message;
  toast.style.backgroundColor = isError ? "#b91c1c" : "#0f172a";
  toast.classList.add("show");
  setTimeout(() => {
    toast.classList.remove("show");
  }, 2600);
}
