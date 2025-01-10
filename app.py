from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Get secret key from .env file
app.secret_key = os.getenv('SECRET_KEY')  # Set the secret key securely from .env

# MySQL Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mypassword'  # Ensure this is the correct password for your MySQL
app.config['MYSQL_DB'] = 'collections'

mysql = MySQL(app)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT id, password_hash, role FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[1], password):
            session['logged_in'] = True
            session['user_id'] = user[0]
            session['user_role'] = user[2]

            if user[2] == 'admin':  # Redirect admin users to admin dashboard
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('home'))  # Redirect regular users to the homepage

        return "Invalid credentials. Please try again.", 401

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('user_role', None)
    return redirect(url_for('login'))

# Home route
@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM collector_notes")
    notes = cur.fetchall()

    cur.execute(
        "SELECT id, customer_name, amount, DATE_FORMAT(transaction_date, '%Y-%m-%d') AS transaction_date, "
        "TIME_FORMAT(transaction_time, '%H:%i:%s') AS transaction_time FROM customer_transactions"
    )
    transactions = cur.fetchall()

    cur.execute("SELECT * FROM payment_plans")
    payment_plans = cur.fetchall()
    cur.close()

    return render_template('home.html', notes=notes, transactions=transactions, payment_plans=payment_plans)

# Admin dashboard
@app.route('/admin')
def admin_dashboard():
    if not session.get('logged_in') or session.get('user_role') != 'admin':
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, email, role, created_at FROM users")
    users = cur.fetchall()
    cur.close()

    return render_template('admin_dashboard.html', users=users)

# Registration route for users (sign up)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'user')  # Default role is 'user'

        hashed_password = generate_password_hash(password)

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (email, password_hash, role) VALUES (%s, %s, %s)",
            (email, hashed_password, role)
        )
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))  # Redirect after successful registration

    return render_template('signup.html')  # Display the registration form

if __name__ == "__main__":
    app.run(debug=True)
