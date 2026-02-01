// Data Simulation
const dashboardData = {
    totalApplied: 1240,
    shortlisted: 350,
    pending: 45,
    rejected: 845
};

const applicants = [
    { name: "Rahul Sharma", role: "Frontend Dev", exp: "2 Years", date: "2023-10-25", status: "Shortlisted" },
    { name: "Priya Patel", role: "UI/UX Designer", exp: "Fresher", date: "2023-10-24", status: "Pending" },
    { name: "Amit Singh", role: "Backend Dev", exp: "3 Years", date: "2023-10-24", status: "Rejected" },
    { name: "Sneha Gupta", role: "Frontend Dev", exp: "1 Year", date: "2023-10-23", status: "Shortlisted" },
    { name: "Vikram Malhotra", role: "Data Analyst", exp: "4 Years", date: "2023-10-22", status: "Pending" }
];

// Initialize Dashboard
document.addEventListener('DOMContentLoaded', () => {
    updateKPIs();
    renderCharts();
    populateTable();
});

// Update Top Cards
function updateKPIs() {
    document.getElementById('total-applied').innerText = dashboardData.totalApplied.toLocaleString();
    document.getElementById('total-shortlisted').innerText = dashboardData.shortlisted.toLocaleString();
    document.getElementById('total-pending').innerText = dashboardData.pending.toLocaleString();
}

// Render Charts using Chart.js
function renderCharts() {
    // 1. Line Chart: Application Trends
    const ctxApp = document.getElementById('applicationChart').getContext('2d');
    new Chart(ctxApp, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'New Applications',
                data: [65, 59, 80, 81, 56, 105, 120],
                borderColor: '#4f46e5',
                backgroundColor: 'rgba(79, 70, 229, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // 2. Doughnut Chart: Role Distribution
    const ctxRole = document.getElementById('roleChart').getContext('2d');
    new Chart(ctxRole, {
        type: 'doughnut',
        data: {
            labels: ['Frontend', 'Backend', 'UI/UX', 'QA'],
            datasets: [{
                data: [40, 30, 20, 10],
                backgroundColor: [
                    '#4f46e5',
                    '#10b981',
                    '#f59e0b',
                    '#64748b'
                ]
            }]
        },
        options: {
            responsive: true,
            cutout: '70%',
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
}

// Populate Applicant Table
function populateTable() {
    const tableBody = document.getElementById('applicant-table-body');
    tableBody.innerHTML = '';

    applicants.forEach(applicant => {
        const row = document.createElement('tr');
        
        // Determine status class for styling
        const statusClass = applicant.status.toLowerCase();

        row.innerHTML = `
            <td><strong>${applicant.name}</strong></td>
            <td>${applicant.role}</td>
            <td>${applicant.exp}</td>
            <td>${applicant.date}</td>
            <td><span class="status ${statusClass}">${applicant.status}</span></td>
            <td>
                <button class="action-btn" title="View Profile"><i class="fas fa-eye"></i></button>
                <button class="action-btn" title="Download Resume"><i class="fas fa-download"></i></button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}