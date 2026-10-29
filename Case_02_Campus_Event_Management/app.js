/**
 * TechVyuha '26 - Campus Event Management Portal
 * Student: Yaswanth | Roll No: 26000918 | Branch: CSE (CSM1)
 */

// Dataset of Campus Tech-Fest Events
const festEvents = [
  {
    id: "EV01",
    title: "CodeSprint: 24-Hour National Hackathon",
    category: "hackathon",
    bannerClass: "banner-hackathon",
    prize: "₹ 50,000",
    fee: "₹ 300",
    date: "Nov 14, 2026",
    time: "09:00 AM onwards",
    venue: "Central CSE Lab 3 & 4",
    teamSize: 3,
    description: "Build innovative software solutions tackling Smart Healthcare, AI for Education, or Urban Mobility. Food and high-speed LAN provided.",
    seatsLeft: 8
  },
  {
    id: "EV02",
    title: "WebCraft: Live Frontend UI/UX Challenge",
    category: "coding",
    bannerClass: "banner-coding",
    prize: "₹ 20,000",
    fee: "₹ 150",
    date: "Nov 15, 2026",
    time: "10:30 AM - 01:30 PM",
    venue: "Web Technology Lab (Block A)",
    teamSize: 1,
    description: "Design and implement responsive, accessible, interactive web layouts under strict time constraints using HTML5, CSS3, and JavaScript.",
    seatsLeft: 14
  },
  {
    id: "EV03",
    title: "AlgoMania: Competitive Speed Coding",
    category: "coding",
    bannerClass: "banner-coding",
    prize: "₹ 25,000",
    fee: "₹ 100",
    date: "Nov 15, 2026",
    time: "02:00 PM - 04:30 PM",
    venue: "Online Coding Arena (Lab 1)",
    teamSize: 1,
    description: "Solve algorithmic and mathematical challenges across 3 levels (Easy, Medium, Hard) within 150 minutes on the college HackerRank platform.",
    seatsLeft: 22
  },
  {
    id: "EV04",
    title: "Paper Presentation: Next-Gen Computing",
    category: "paper",
    bannerClass: "banner-paper",
    prize: "₹ 15,000",
    fee: "₹ 200",
    date: "Nov 16, 2026",
    time: "09:30 AM - 01:00 PM",
    venue: "Seminar Hall - Block B",
    teamSize: 2,
    description: "Present research findings in Generative AI, Quantum Computing, IoT Architectures, or Cyber Forensics before industry expert judges.",
    seatsLeft: 11
  },
  {
    id: "EV05",
    title: "Battlegrounds LAN & Cyber E-Sports",
    category: "gaming",
    bannerClass: "banner-gaming",
    prize: "₹ 30,000",
    fee: "₹ 400",
    date: "Nov 16, 2026",
    time: "02:00 PM - 06:00 PM",
    venue: "Auditorium Annex Gaming Hub",
    teamSize: 4,
    description: "Tactical LAN tournament featuring custom squad battles, zero-latency network infrastructure, and live stage shoutcasting.",
    seatsLeft: 6
  },
  {
    id: "EV06",
    title: "RoboRace: Autonomous Obstacle Challenge",
    category: "hackathon",
    bannerClass: "banner-hackathon",
    prize: "₹ 20,000",
    fee: "₹ 250",
    date: "Nov 15, 2026",
    time: "11:00 AM - 03:00 PM",
    venue: "Open Air Amphitheatre",
    teamSize: 3,
    description: "Autonomous or remote-controlled bot racing through steep ramps, water trenches, gravel, and optical line-following turns.",
    seatsLeft: 9
  }
];

// App State
let registeredPasses = [];
let activeCategory = "all";
let searchQuery = "";
let selectedEvent = null;

// DOM Elements
const eventsGrid = document.getElementById("eventsGrid");
const eventSearch = document.getElementById("eventSearch");
const categoryTabs = document.getElementById("categoryTabs");
const passCount = document.getElementById("passCount");

// Registration Modal Elements
const regModal = document.getElementById("regModal");
const regForm = document.getElementById("regForm");
const modalEventTitle = document.getElementById("modalEventTitle");
const modalEventFee = document.getElementById("modalEventFee");
const teamMembersSection = document.getElementById("teamMembersSection");
const teamInputsContainer = document.getElementById("teamInputsContainer");
const teamLimit = document.getElementById("teamLimit");
const btnCloseRegModal = document.getElementById("btnCloseRegModal");

// Ticket Pass Modal Elements
const ticketModal = document.getElementById("ticketModal");
const ticketPassId = document.getElementById("ticketPassId");
const ticketEventName = document.getElementById("ticketEventName");
const ticketCandidate = document.getElementById("ticketCandidate");
const ticketRoll = document.getElementById("ticketRoll");
const ticketBranch = document.getElementById("ticketBranch");
const ticketVenue = document.getElementById("ticketVenue");
const ticketTeamInfo = document.getElementById("ticketTeamInfo");
const btnPrintTicket = document.getElementById("btnPrintTicket");
const btnCloseTicket = document.getElementById("btnCloseTicket");

// My Passes Modal Elements
const myPassesModal = document.getElementById("myPassesModal");
const btnMyRegistrations = document.getElementById("btnMyRegistrations");
const btnCloseMyPasses = document.getElementById("btnCloseMyPasses");
const myPassesContainer = document.getElementById("myPassesContainer");

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  renderEvents();
  setupEventListeners();
});

// Render Event Cards
function renderEvents() {
  eventsGrid.innerHTML = "";

  const filtered = festEvents.filter(ev => {
    const matchesCat = (activeCategory === "all" || ev.category === activeCategory);
    const matchesSearch = ev.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          ev.venue.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          ev.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCat && matchesSearch;
  });

  if (filtered.length === 0) {
    eventsGrid.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 3rem; background:#fff; border-radius:12px;">
        <p style="color:#64748b; font-size:1rem;">No events match your current filter.</p>
      </div>
    `;
    return;
  }

  filtered.forEach(ev => {
    const isAlreadyRegistered = registeredPasses.some(p => p.eventId === ev.id);
    const card = document.createElement("div");
    card.className = "event-card";

    card.innerHTML = `
      <div class="card-banner ${ev.bannerClass}">
        <span class="card-category-badge">${ev.category}</span>
        <span class="card-prize-badge">Prize: ${ev.prize}</span>
      </div>
      <div class="card-body">
        <h3>${ev.title}</h3>
        <p class="event-desc">${ev.description}</p>
        <div class="event-meta-list">
          <div class="meta-row">📅 <strong>Date:</strong> ${ev.date} (${ev.time})</div>
          <div class="meta-row">📍 <strong>Venue:</strong> ${ev.venue}</div>
          <div class="meta-row">👥 <strong>Team Size:</strong> ${ev.teamSize === 1 ? 'Solo Participant' : 'Up to ' + ev.teamSize + ' Members'}</div>
          <div class="meta-row">⚡ <strong>Availability:</strong> ${ev.seatsLeft} slots left</div>
        </div>
        <div class="card-bottom">
          <div class="fee-display">
            <span>Entry Fee</span>
            <strong>${ev.fee}</strong>
          </div>
          <button class="btn btn-primary-fest" onclick="openRegistrationModal('${ev.id}')" ${isAlreadyRegistered ? "disabled" : ""}>
            ${isAlreadyRegistered ? "✓ Registered" : "Register Now"}
          </button>
        </div>
      </div>
    `;
    eventsGrid.appendChild(card);
  });
}

// Open Registration Form Modal
window.openRegistrationModal = function(eventId) {
  selectedEvent = festEvents.find(e => e.id === eventId);
  if (!selectedEvent) return;

  modalEventTitle.textContent = selectedEvent.title;
  modalEventFee.textContent = selectedEvent.fee;
  document.getElementById("selectedEventId").value = eventId;

  // Handle Team member inputs
  if (selectedEvent.teamSize > 1) {
    teamMembersSection.style.display = "block";
    teamLimit.textContent = selectedEvent.teamSize;
    teamInputsContainer.innerHTML = "";
    
    for (let i = 2; i <= selectedEvent.teamSize; i++) {
      const row = document.createElement("div");
      row.style.marginBottom = "8px";
      row.innerHTML = `
        <input type="text" class="team-member-input" placeholder="Team Member #${i} Full Name & Roll No" style="width: 100%; padding: 7px 10px; border:1px solid #cbd5e1; border-radius:6px; font-size:0.8rem;" />
      `;
      teamInputsContainer.appendChild(row);
    }
  } else {
    teamMembersSection.style.display = "none";
    teamInputsContainer.innerHTML = "";
  }

  regModal.classList.add("active");
};

// Setup Listeners
function setupEventListeners() {
  // Category tabs
  categoryTabs.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      categoryTabs.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeCategory = btn.getAttribute("data-cat");
      renderEvents();
    });
  });

  // Search input
  eventSearch.addEventListener("input", (e) => {
    searchQuery = e.target.value.trim();
    renderEvents();
  });

  // Close modals
  btnCloseRegModal.addEventListener("click", () => regModal.classList.remove("active"));
  btnCloseTicket.addEventListener("click", () => ticketModal.classList.remove("active"));
  btnPrintTicket.addEventListener("click", () => window.print());

  // My passes drawer
  btnMyRegistrations.addEventListener("click", () => {
    renderMyPasses();
    myPassesModal.classList.add("active");
  });
  btnCloseMyPasses.addEventListener("click", () => myPassesModal.classList.remove("active"));

  // Form Submit
  regForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleFormSubmit();
  });
}

// Handle Form Submission & Generate Pass
function handleFormSubmit() {
  const name = document.getElementById("studentName").value;
  const roll = document.getElementById("studentRoll").value;
  const branch = document.getElementById("studentBranch").value;
  const payMethod = document.querySelector('input[name="payMethod"]:checked').value;

  // Collect team members
  const teamInputs = document.querySelectorAll(".team-member-input");
  const members = [];
  teamInputs.forEach(inp => {
    if (inp.value.trim()) members.push(inp.value.trim());
  });

  // Generate unique pass ID
  const randomSuffix = Math.floor(1000 + Math.random() * 9000);
  const passId = `NRIIT-TV26-${randomSuffix}`;

  const newPass = {
    passId,
    eventId: selectedEvent.id,
    eventTitle: selectedEvent.title,
    venue: selectedEvent.venue,
    date: `${selectedEvent.date} (${selectedEvent.time})`,
    name,
    roll,
    branch,
    payMethod,
    members
  };

  registeredPasses.push(newPass);
  selectedEvent.seatsLeft = Math.max(0, selectedEvent.seatsLeft - 1);

  // Close Reg modal, Update Header Counter & Open Ticket Modal
  regModal.classList.remove("active");
  passCount.textContent = registeredPasses.length;
  renderEvents();
  showTicketModal(newPass);
}

// Display Generated Digital Pass
function showTicketModal(pass) {
  ticketPassId.textContent = pass.passId;
  ticketEventName.textContent = pass.eventTitle;
  ticketCandidate.textContent = pass.name;
  ticketRoll.textContent = pass.roll;
  ticketBranch.textContent = pass.branch;
  ticketVenue.textContent = `${pass.venue} • ${pass.date}`;

  if (pass.members.length > 0) {
    ticketTeamInfo.style.display = "block";
    ticketTeamInfo.innerHTML = `<strong>Co-Participants:</strong> ${pass.members.join(", ")}`;
  } else {
    ticketTeamInfo.style.display = "none";
  }

  ticketModal.classList.add("active");
}

// Render "My Passes" View
function renderMyPasses() {
  if (registeredPasses.length === 0) {
    myPassesContainer.innerHTML = `
      <p style="text-align:center; padding: 2rem; color:#64748b;">You haven't registered for any events yet.</p>
    `;
    return;
  }

  myPassesContainer.innerHTML = "";
  registeredPasses.forEach(pass => {
    const item = document.createElement("div");
    item.className = "registered-pass-item";
    item.innerHTML = `
      <div>
        <h4>${pass.eventTitle}</h4>
        <p>Pass ID: <strong>${pass.passId}</strong> | ${pass.venue}</p>
        <p style="font-size:0.72rem; color:#475569; margin-top:2px;">Reg Name: ${pass.name} (${pass.roll})</p>
      </div>
      <button class="btn btn-outline" style="color:#0f172a; border-color:#cbd5e1; font-size:0.75rem;" onclick="viewExistingTicket('${pass.passId}')">
        View Pass
      </button>
    `;
    myPassesContainer.appendChild(item);
  });
}

// View existing ticket from list
window.viewExistingTicket = function(passId) {
  const pass = registeredPasses.find(p => p.passId === passId);
  if (pass) {
    myPassesModal.classList.remove("active");
    showTicketModal(pass);
  }
};
