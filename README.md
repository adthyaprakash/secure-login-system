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
```
## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/adthyaprakash/secure-login-system.git
cd secure-login-system
```

### 2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL Database
Login to PostgreSQL and create a database:

```sql
CREATE DATABASE vaultdb;
```
Create the users table:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    is_active BOOLEAN DEFAULT TRUE,
    failed_attempts INTEGER DEFAULT 0
);
```
### 5. Configure Database in app.py

Update this function with your PostgreSQL credentials:

```python
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="vaultdb",
        user="postgres",
        password="your_password_here"
    )
```
### 6. Run the Application

```bash
python src/backend/app.py
```
The app will run at:
```cpp
http://127.0.0.1:5000/

```