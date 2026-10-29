/**
 * NRIIT Central E-Library & Academic Bookstore
 * Student: Yaswanth | Roll No: 26000918 | Branch: CSE (CSM1)
 */

// Academic Library Catalog
const libraryBooks = [
  {
    id: "BK01",
    isbn: "978-0131103627",
    title: "The C Programming Language",
    author: "Brian W. Kernighan & Dennis M. Ritchie",
    genre: "cs-core",
    genreLabel: "CS Core",
    edition: "2nd Edition (Prentice Hall)",
    stock: 6,
    shelf: "Rack A-04, Ground Floor",
    coverColor: "linear-gradient(135deg, #1e3a8a, #0369a1)"
  },
  {
    id: "BK02",
    isbn: "978-0262033848",
    title: "Introduction to Algorithms (CLRS)",
    author: "Thomas H. Cormen, Charles E. Leiserson",
    genre: "cs-core",
    genreLabel: "CS Core",
    edition: "4th Edition (MIT Press)",
    stock: 4,
    shelf: "Rack A-12, Ground Floor",
    coverColor: "linear-gradient(135deg, #312e81, #4f46e5)"
  },
  {
    id: "BK03",
    isbn: "978-1491952023",
    title: "JavaScript: The Definitive Guide",
    author: "David Flanagan",
    genre: "web-dev",
    genreLabel: "Web & Full Stack",
    edition: "7th Edition (O'Reilly Media)",
    stock: 7,
    shelf: "Rack B-08, 1st Floor",
    coverColor: "linear-gradient(135deg, #854d0e, #ca8a04)"
  },
  {
    id: "BK04",
    isbn: "978-1492051725",
    title: "Learning Web Design: A Beginner's Guide",
    author: "Jennifer Robbins",
    genre: "web-dev",
    genreLabel: "Web & Full Stack",
    edition: "5th Edition (O'Reilly Media)",
    stock: 3,
    shelf: "Rack B-09, 1st Floor",
    coverColor: "linear-gradient(135deg, #065f46, #0d9488)"
  },
  {
    id: "BK05",
    isbn: "978-0134610993",
    title: "Artificial Intelligence: A Modern Approach",
    author: "Stuart Russell & Peter Norvig",
    genre: "ai-data",
    genreLabel: "AI & Data Science",
    edition: "4th Edition (Pearson)",
    stock: 5,
    shelf: "Rack C-02, 2nd Floor",
    coverColor: "linear-gradient(135deg, #4c1d95, #7c3aed)"
  },
  {
    id: "BK06",
    isbn: "978-1449369415",
    title: "Python Data Science Handbook",
    author: "Jake VanderPlas",
    genre: "ai-data",
    genreLabel: "AI & Data Science",
    edition: "2nd Edition (O'Reilly)",
    stock: 8,
    shelf: "Rack C-07, 2nd Floor",
    coverColor: "linear-gradient(135deg, #1e293b, #334155)"
  },
  {
    id: "BK07",
    isbn: "978-0073383095",
    title: "Discrete Mathematics & Its Applications",
    author: "Kenneth H. Rosen",
    genre: "math",
    genreLabel: "Applied Math",
    edition: "8th Edition (McGraw-Hill)",
    stock: 5,
    shelf: "Rack D-01, 2nd Floor",
    coverColor: "linear-gradient(135deg, #831843, #be185d)"
  },
  {
    id: "BK08",
    isbn: "978-0132350884",
    title: "Clean Code: A Handbook of Agile Craft",
    author: "Robert C. Martin (Uncle Bob)",
    genre: "cs-core",
    genreLabel: "CS Core",
    edition: "1st Edition (Prentice Hall)",
    stock: 2,
    shelf: "Rack A-15, Ground Floor",
    coverColor: "linear-gradient(135deg, #0c4a6e, #0284c7)"
  }
];

// App State
const MAX_BAG_CAPACITY = 3;
let readingBag = [];
let activeLoans = [];
let activeGenre = "all";
let searchKeyword = "";

// DOM Elements
const booksGrid = document.getElementById("booksGrid");
const libSearch = document.getElementById("libSearch");
const categoryChips = document.getElementById("categoryChips");
const bagCount = document.getElementById("bagCount");
const btnOpenBag = document.getElementById("btnOpenBag");
const bagDrawer = document.getElementById("bagDrawer");
const btnCloseBag = document.getElementById("btnCloseBag");
const bagList = document.getElementById("bagList");
const previewDueDate = document.getElementById("previewDueDate");
const btnIssueBooks = document.getElementById("btnIssueBooks");

// Loan Modal Elements
const loanModal = document.getElementById("loanModal");
const receiptTxnId = document.getElementById("receiptTxnId");
const receiptIssueDate = document.getElementById("receiptIssueDate");
const receiptDueDate = document.getElementById("receiptDueDate");
const receiptBooksList = document.getElementById("receiptBooksList");
const btnPrintSlip = document.getElementById("btnPrintSlip");
const btnCloseModal = document.getElementById("btnCloseModal");

// Active Loans Elements
const borrowStatusStrip = document.getElementById("borrowStatusStrip");
const activeLoanCount = document.getElementById("activeLoanCount");
const btnViewLoans = document.getElementById("btnViewLoans");
const activeLoansModal = document.getElementById("activeLoansModal");
const activeLoansContainer = document.getElementById("activeLoansContainer");
const btnCloseLoans = document.getElementById("btnCloseLoans");

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  renderCatalog();
  calculateDueDates();
  setupEventListeners();
});

// Render Books Grid
function renderCatalog() {
  booksGrid.innerHTML = "";

  const filtered = libraryBooks.filter(book => {
    const matchesGenre = (activeGenre === "all" || book.genre === activeGenre);
    const matchesKeyword = book.title.toLowerCase().includes(searchKeyword.toLowerCase()) ||
                           book.author.toLowerCase().includes(searchKeyword.toLowerCase()) ||
                           book.isbn.includes(searchKeyword);
    return matchesGenre && matchesKeyword;
  });

  if (filtered.length === 0) {
    booksGrid.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 3rem; background: #fff; border-radius: 12px;">
        <p style="color: #64748b;">No textbooks found matching your query.</p>
      </div>
    `;
    return;
  }

  filtered.forEach(book => {
    const inBag = readingBag.some(item => item.id === book.id);
    const card = document.createElement("div");
    card.className = "book-card";

    card.innerHTML = `
      <div class="book-cover" style="background: ${book.coverColor};">
        <span class="cover-cat">${book.genreLabel}</span>
        <h4 class="cover-title">${book.title}</h4>
        <span class="cover-isbn">ISBN: ${book.isbn}</span>
      </div>
      <div class="book-details">
        <div class="book-author">${book.author}</div>
        <div class="book-edition">${book.edition}</div>
        <div class="book-location">
          <span>📍 <strong>Location:</strong> ${book.shelf}</span>
        </div>
        <div class="book-card-bottom">
          <span class="stock-tag ${book.stock > 3 ? 'in-stock' : 'low-stock'}">
            ● ${book.stock} Copies in Shelf
          </span>
          <button class="btn ${inBag ? 'btn-secondary' : 'btn-lib-primary'}" onclick="toggleBag('${book.id}')">
            ${inBag ? '✓ In Bag' : '+ Add to Bag'}
          </button>
        </div>
      </div>
    `;
    booksGrid.appendChild(card);
  });
}

// Toggle Book in Reading Bag
window.toggleBag = function(bookId) {
  const book = libraryBooks.find(b => b.id === bookId);
  if (!book) return;

  const existingIndex = readingBag.findIndex(item => item.id === bookId);

  if (existingIndex > -1) {
    readingBag.splice(existingIndex, 1);
  } else {
    if (readingBag.length >= MAX_BAG_CAPACITY) {
      alert(`Borrow limit reached! You can borrow at most ${MAX_BAG_CAPACITY} textbooks simultaneously.`);
      return;
    }
    readingBag.push(book);
  }

  updateBagDrawer();
  renderCatalog();
};

// Update Bag Drawer View
function updateBagDrawer() {
  bagCount.textContent = readingBag.length;

  if (readingBag.length === 0) {
    bagList.innerHTML = `<li class="empty-bag-msg">Your reading bag is empty. Browse textbooks and click "+ Add to Bag".</li>`;
    btnIssueBooks.disabled = true;
  } else {
    bagList.innerHTML = "";
    readingBag.forEach(book => {
      const li = document.createElement("li");
      li.className = "bag-item";
      li.innerHTML = `
        <div class="bag-item-left">
          <span class="bag-item-title">${book.title}</span>
          <span class="bag-item-author">${book.author}</span>
        </div>
        <button class="btn-bag-remove" onclick="toggleBag('${book.id}')" title="Remove from bag">&times;</button>
      `;
      bagList.appendChild(li);
    });
    btnIssueBooks.disabled = false;
  }
}

// Compute standard 14-day return date
function calculateDueDates() {
  const today = new Date();
  const due = new Date();
  due.setDate(today.getDate() + 14);

  const formattedDue = due.toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric"
  });

  previewDueDate.textContent = formattedDue;
}

// Event Listeners Setup
function setupEventListeners() {
  // Search
  libSearch.addEventListener("input", (e) => {
    searchKeyword = e.target.value.trim();
    renderCatalog();
  });

  // Category filter
  categoryChips.querySelectorAll(".chip").forEach(chip => {
    chip.addEventListener("click", () => {
      categoryChips.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      activeGenre = chip.getAttribute("data-genre");
      renderCatalog();
    });
  });

  // Drawer open/close
  btnOpenBag.addEventListener("click", () => bagDrawer.classList.add("active"));
  btnCloseBag.addEventListener("click", () => bagDrawer.classList.remove("active"));

  // Issue books action
  btnIssueBooks.addEventListener("click", () => {
    handleLoanIssuance();
  });

  // Loan confirmation modal actions
  btnCloseModal.addEventListener("click", () => loanModal.classList.remove("active"));
  btnPrintSlip.addEventListener("click", () => window.print());

  // Active loans modal
  btnViewLoans.addEventListener("click", () => {
    renderActiveLoans();
    activeLoansModal.classList.add("active");
  });
  btnCloseLoans.addEventListener("click", () => activeLoansModal.classList.remove("active"));
}

// Handle Loan Checkout
function handleLoanIssuance() {
  const today = new Date();
  const due = new Date();
  due.setDate(today.getDate() + 14);

  const issueDateStr = today.toLocaleDateString("en-IN", { day: "2-digit", month: "short", year: "numeric" });
  const dueDateStr = due.toLocaleDateString("en-IN", { day: "2-digit", month: "short", year: "numeric" });
  const txnId = `NRIIT-LIB-${Math.floor(1000 + Math.random() * 9000)}`;

  // Add to active loans
  readingBag.forEach(b => {
    activeLoans.push({
      id: b.id,
      title: b.title,
      author: b.author,
      isbn: b.isbn,
      shelf: b.shelf,
      issueDate: issueDateStr,
      dueDate: dueDateStr,
      txnId
    });
    b.stock = Math.max(0, b.stock - 1);
  });

  // Render modal receipt
  receiptTxnId.textContent = txnId;
  receiptIssueDate.textContent = issueDateStr;
  receiptDueDate.textContent = dueDateStr;

  receiptBooksList.innerHTML = "";
  readingBag.forEach((b, idx) => {
    const row = document.createElement("div");
    row.className = "receipt-book-row";
    row.innerHTML = `
      <span>${idx + 1}. <strong>${b.title}</strong></span>
      <span style="font-size:0.75rem; color:#64748b;">${b.shelf}</span>
    `;
    receiptBooksList.appendChild(row);
  });

  // Reset bag
  readingBag = [];
  updateBagDrawer();
  bagDrawer.classList.remove("active");
  loanModal.classList.add("active");

  // Update Active Loans Strip
  updateActiveLoansStrip();
  renderCatalog();
}

// Update Active Loans Banner Strip
function updateActiveLoansStrip() {
  if (activeLoans.length > 0) {
    borrowStatusStrip.style.display = "flex";
    activeLoanCount.textContent = activeLoans.length;
  } else {
    borrowStatusStrip.style.display = "none";
  }
}

// Render Active Loans
function renderActiveLoans() {
  activeLoansContainer.innerHTML = "";

  if (activeLoans.length === 0) {
    activeLoansContainer.innerHTML = `<p style="text-align:center; padding:1.5rem; color:#64748b;">No active loans on record.</p>`;
    return;
  }

  activeLoans.forEach((loan, idx) => {
    const item = document.createElement("div");
    item.className = "active-loan-item";
    item.innerHTML = `
      <div>
        <h4 style="font-size:0.95rem; font-weight:700;">${loan.title}</h4>
        <p style="font-size:0.75rem; color:#64748b;">Due Date: <strong style="color:#b91c1c;">${loan.dueDate}</strong> | Txn: ${loan.txnId}</p>
      </div>
      <button class="btn btn-secondary" style="font-size:0.75rem;" onclick="returnBook(${idx})">
        Return Book
      </button>
    `;
    activeLoansContainer.appendChild(item);
  });
}

// Return book action
window.returnBook = function(index) {
  const returned = activeLoans.splice(index, 1)[0];
  const orig = libraryBooks.find(b => b.id === returned.id);
  if (orig) orig.stock += 1;

  updateActiveLoansStrip();
  renderActiveLoans();
  renderCatalog();
};
