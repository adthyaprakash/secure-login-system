# Secure Login System with RBAC

## Overview
This project is a secure login and registration system built using Flask, PostgreSQL, and JWT authentication.  
It includes **Role-Based Access Control (RBAC)** with separate dashboards for Admin and User roles.  
Security features include input validation, CAPTCHA, and account lockout after failed login attempts.

---

## Features
- User registration with hashed passwords (`bcrypt`)
- User login with JWT session management
- **Role-Based Access Control (RBAC):**
  - Admins can view and manage users
  - Users have access to a personal dashboard
- Account lockout after repeated failed logins
- Google reCAPTCHA to prevent brute-force attacks
- Glassmorphic styled frontend with HTML, CSS, and JavaScript

---

## Screenshots

### Login Page
![Login Page](src/backend/static/assets/login%20page.png)

### Register Page
![Register Page](src/backend/static/assets/register.png)

### User Dashboard
![User Dashboard](src/backend/static/assets/user%20dashboard.png)

### Admin Dashboard
![Admin Dashboard](src/backend/static/assets/admindashboard.png)

### About Page
![About Page](src/backend/static/assets/about%20page.png)

### reCAPTCHA
![reCAPTCHA](src/backend/static/assets/captcha.png)

### Database Schema
![Database](src/backend/static/assets/db.png)

---

## Project Structure
```bash
secure-login-system/
│── src/
│   ├── backend/
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── templates/
│   │   │   ├── index.html
│   │   │   ├── register.html
│   │   │   ├── dashboard.html
│   │   │   └── admin_dashboard.html
│   │   ├── static/
│   │   │   ├── style.css
│   │   │   ├── script.js
│   │   │   └── admin_script.js
│── requirements.txt
│── README.md