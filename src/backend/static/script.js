// script.js

// Handle Login
document.getElementById("loginForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();
  const captchaResponse = grecaptcha.getResponse();

  if (!captchaResponse) {
    alert("Please complete the CAPTCHA.");
    return;
  }

  try {
    const res = await fetch("/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password, captcha: captchaResponse }),
    });

    const data = await res.json();

    if (res.ok) {
      alert(data.message);

      // save session data
      sessionStorage.setItem("token", data.token);
      sessionStorage.setItem("username", data.user.username);
      sessionStorage.setItem("role", data.user.role);

      // redirect based on role
      if (data.user.role === "admin") {
        window.location.href = "/admin_dashboard_page";
      } else {
        window.location.href = "/dashboard_page";
      }
    } else {
      alert(data.error || "Login failed.");
      grecaptcha.reset();
    }
  } catch (err) {
    console.error("Login error:", err);
    alert("Something went wrong.");
    grecaptcha.reset();
  }
});

// Handle Register
document.getElementById("registerForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();
  const confirm_password = document.getElementById("confirm_password").value.trim();
  const role = document.getElementById("role").value;
  const captchaResponse = grecaptcha.getResponse();

  if (!captchaResponse) {
    alert("Please complete the CAPTCHA.");
    return;
  }

  if (password !== confirm_password) {
    alert("Passwords do not match.");
    return;
  }

  try {
    const res = await fetch("/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password, role, captcha: captchaResponse }),
    });

    const data = await res.json();

    if (res.ok) {
      alert(data.message);
      window.location.href = "/";
    } else {
      alert(data.error || "Registration failed.");
      grecaptcha.reset();
    }
  } catch (err) {
    console.error("Register error:", err);
    alert("Something went wrong.");
    grecaptcha.reset();
  }
});
