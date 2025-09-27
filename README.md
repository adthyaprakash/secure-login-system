# Secure Login System with RBAC

## Overview
This project is a secure login and registration system built using Flask, PostgreSQL, and JWT authentication.  
It includes role-based access control (RBAC) with separate dashboards for **Admin** and **User** roles.  

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

### User Dashboard
![User Dashboard](src/backend/static/assets/user%20dashboard.png)

### Admin Dashboard
![Admin Dashboard](src/backend/static/assets/admin%20dashboard.png)

---

## Project Structure
