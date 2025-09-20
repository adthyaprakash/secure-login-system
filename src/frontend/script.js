document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.getElementById("registerForm");
  const loginForm = document.getElementById("loginForm");

  if (registerForm) {
    registerForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = registerForm.email.value;
      const password = registerForm.password.value;

      if (!/^[^ ]+@[^ ]+\.[a-z]{2,3}$/.test(email)) {
        alert("Please enter a valid email address");
        return;
      }
      if (password.length < 6) {
        alert("Password must be at least 6 characters");
        return;
      }
      alert("Registration successful!");
    });
  }

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      alert("Login successful!");
    });
  }
});
