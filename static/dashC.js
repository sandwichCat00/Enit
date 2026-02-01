// KPI values (replace later with backend data)
document.getElementById("total-applied").innerText = "1,240";
document.getElementById("total-shortlisted").innerText = "350";
document.getElementById("total-pending").innerText = "45";

// ===============================
// Application Trends (Line Chart)
// ===============================
const ctx1 = document.getElementById("applicationChart");

new Chart(ctx1, {
  type: "line",
  data: {
    labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    datasets: [{
      data: [65, 58, 80, 82, 55, 105, 120],
      borderColor: "#6366f1",
      backgroundColor: "rgba(99,102,241,0.15)",
      tension: 0.4,
      fill: true,
      pointRadius: 4,
      pointBackgroundColor: "#6366f1"
    }]
  },
  options: {
    plugins: { legend: { display: false } },
    scales: {
      x: { grid: { display: false }, ticks: { color: "#9ca3af" } },
      y: { grid: { color: "rgba(255,255,255,0.05)" }, ticks: { color: "#9ca3af" } }
    }
  }
});

// ===============================
// Role Distribution (Doughnut)
// ===============================
const ctx2 = document.getElementById("roleChart");

new Chart(ctx2, {
  type: "doughnut",
  data: {
    labels: ["Frontend", "Backend", "UI/UX", "QA"],
    datasets: [{
      data: [40, 30, 20, 10],
      backgroundColor: [
        "#6366f1",
        "#10b981",
        "#f59e0b",
        "#9ca3af"
      ],
      borderWidth: 2,
      borderColor: "#020617"
    }]
  },
  options: {
    cutout: "70%",
    plugins: {
      legend: {
        labels: { color: "#9ca3af" }
      }
    }
  }
});

// ===============================
// Sample table data
// ===============================
const tableBody = document.getElementById("applicant-table-body");

const applicants = [
  ["Aarav Patel", "Frontend Dev", "2 Years", "Jan 29", "Shortlisted"],
  ["Sneha Rao", "Backend Dev", "3 Years", "Jan 28", "Pending"],
  ["Rohan Mehta", "UI/UX", "1.5 Years", "Jan 27", "Reviewed"]
];

applicants.forEach(a => {
  const row = `
    <tr>
      <td>${a[0]}</td>
      <td>${a[1]}</td>
      <td>${a[2]}</td>
      <td>${a[3]}</td>
      <td>${a[4]}</td>
      <td><i class="fas fa-ellipsis-h"></i></td>
    </tr>`;
  tableBody.innerHTML += row;
});
