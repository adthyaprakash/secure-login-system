from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
from passlib.hash import bcrypt
import jwt
import datetime
import re

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)
app.config['SECRET_KEY'] = '6LeeANQrAAAAANCERRtSdlwa6ODRSy-JuJJT5Ku_'  # ⚠️ replace with strong random key

# ---------- Database Connection ----------
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="vaultdb",
        user="postgres",
        password="root"  # ⚠️ update with your postgres password
    )

# ---------- Routes ----------
@app.route('/')
def login_page():
    return render_template("index.html")

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/dashboard_page')
def dashboard_page():
    role = session.get("role")
    if not role:
        return redirect(url_for("login_page"))
    if role == "admin":
        return redirect(url_for("admin_dashboard_page"))
    return render_template("dashboard.html")

@app.route('/admin_dashboard_page')
def admin_dashboard_page():
    role = session.get("role")
    if role != "admin":
        return redirect(url_for("dashboard_page"))
    return render_template("admin_dashboard.html")

# ---------- Registration ----------
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email format"}), 400
    if not username or not password:
        return jsonify({"error": "Missing fields"}), 400

    hashed_password = bcrypt.hash(password)

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, email, password, role, is_active, failed_attempts) VALUES (%s, %s, %s, %s, TRUE, 0)",
            (username, email, hashed_password, role)
        )
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- Login ----------
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "SELECT id, username, email, password, role, is_active, failed_attempts FROM users WHERE email = %s",
            (email,)
        )
        user = cur.fetchone()

        if not user:
            return jsonify({"error": "Invalid credentials"}), 401
        if not user['is_active']:
            return jsonify({"error": "Account disabled"}), 403

        if bcrypt.verify(password, user['password']):
            cur.execute("UPDATE users SET failed_attempts = 0 WHERE id = %s", (user['id'],))
            conn.commit()

            token = jwt.encode(
                {
                    'user_id': user['id'],
                    'role': user['role'],
                    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=12)
                },
                app.config['SECRET_KEY'],
                algorithm="HS256"
            )

            session['role'] = user['role']
            session['username'] = user['username']

            cur.close()
            conn.close()
            return jsonify({
                "message": "Login successful",
                "user": {
                    "id": user['id'],
                    "username": user['username'],
                    "email": user['email'],
                    "role": user['role']
                },
                "token": token
            }), 200
        else:
            cur.execute("UPDATE users SET failed_attempts = failed_attempts + 1 WHERE id = %s", (user['id'],))
            conn.commit()

            if user['failed_attempts'] + 1 >= 5:
                cur.execute("UPDATE users SET is_active = FALSE WHERE id = %s", (user['id'],))
                conn.commit()

            cur.close()
            conn.close()
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        print("Login error:", e)
        return jsonify({"error": str(e)}), 500

# ---------- Admin: Fetch Users ----------
@app.route('/admin/get_users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, username, email, role, is_active, failed_attempts FROM users")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({"users": users}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- Admin: Toggle User ----------
@app.route('/admin/toggle_user', methods=['POST'])
def toggle_user():
    data = request.json
    user_id = data.get('user_id')
    activate = data.get('activate', True)

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        if activate:
            cur.execute("UPDATE users SET is_active = TRUE, failed_attempts = 0 WHERE id = %s AND role != 'admin'", (user_id,))
        else:
            cur.execute("UPDATE users SET is_active = FALSE WHERE id = %s AND role != 'admin'", (user_id,))

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": f"User {'enabled' if activate else 'disabled'} successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- Main ----------
if __name__ == '__main__':
    try:
        conn = get_db_connection()
        print("✅ Database connected successfully!")
        conn.close()
    except Exception as e:
        print("❌ DB connection failed:", e)

    app.secret_key = app.config['SECRET_KEY']
    app.run(debug=True)
