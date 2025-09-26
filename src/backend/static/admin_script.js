async function fetchUsers() {
  try {
    const res = await fetch("/admin/get_users");
    const data = await res.json();

    const tbody = document.querySelector("#userTable tbody");
    tbody.innerHTML = "";

    if (!res.ok || !data.users || data.users.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7">No users found</td></tr>`;
      return;
    }

    data.users.forEach(u => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${u[0]}</td>   <!-- id -->
        <td>${u[1]}</td>   <!-- username -->
        <td>${u[2]}</td>   <!-- email -->
        <td>${u[3]}</td>   <!-- role -->
        <td>${u[4] ? "Yes" : "No"}</td> <!-- is_active -->
        <td>${u[5]}</td>   <!-- failed_attempts -->
        <td>
          ${u[3] !== "admin"
            ? `<button class="disable-btn" onclick="toggleUser(${u[0]}, ${u[4]})">
                 ${u[4] ? "Disable" : "Enable"}
               </button>`
            : "Admin"}
        </td>
      `;
      tbody.appendChild(tr);
    });
  } catch (err) {
    console.error("Error fetching users:", err);
    alert("Error loading users");
  }
}

async function toggleUser(userId, isActive) {
  try {
    const res = await fetch("/admin/toggle_user", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, activate: !isActive })
    });

    const data = await res.json();
    alert(data.message || "User updated");
    fetchUsers(); // refresh after update
  } catch (err) {
    console.error("Error toggling user:", err);
    alert("Failed to update user");
  }
}

// Run on page load
document.addEventListener("DOMContentLoaded", fetchUsers);
