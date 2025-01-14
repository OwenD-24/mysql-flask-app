from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from datetime import datetime
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
app.config['MYSQL_PASSWORD'] = 'MAINPassword25'  # Ensure this is the correct password for your MySQL
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

            if user[2] == 'admin':
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('home'))  # Redirect regular users to the homepage

        return "Invalid credentials. Please try again.", 401

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('user_role', None)
    return redirect(url_for('login'))  # Make sure this points to 'login'


# Home route
@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    
    # Fetch all notes
    cur.execute("SELECT * FROM collector_notes")
    notes = cur.fetchall()

    # Fetch transaction details along with associated payment plans
    cur.execute(
        "SELECT c.id, c.customer_name, c.amount, DATE_FORMAT(c.transaction_date, '%Y-%m-%d') AS transaction_date, "
        "TIME_FORMAT(c.transaction_time, '%H:%i:%s') AS transaction_time, p.plan_name "
        "FROM customer_transactions c LEFT JOIN payment_plans p ON c.payment_plan_id = p.id"
    )
    transactions = cur.fetchall()

    # Fetch all payment plans
    cur.execute("SELECT * FROM payment_plans")
    payment_plans = cur.fetchall()

    cur.close()

    # Render the home page with notes, transactions, and payment plans
    return render_template('home.html', notes=notes, transactions=transactions, payment_plans=payment_plans)

# Note Route
@app.route('/add_note', methods=['POST'])
def add_note():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    note = request.form['note']
    customer_name = request.form['customer_name']
    amount = request.form['amount']
    transaction_date = request.form['transaction_date']
    transaction_time = request.form['transaction_time']
    payment_plan_id = request.form['payment_plan_id']
    
    # Create new transaction
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO customer_transactions (customer_name, amount, transaction_date, transaction_time, payment_plan_id) "
        "VALUES (%s, %s, %s, %s, %s)",
        (customer_name, amount, transaction_date, transaction_time, payment_plan_id)
    )
    mysql.connection.commit()
    
    # Get the transaction ID of the newly created transaction
    cur.execute("SELECT LAST_INSERT_ID()")
    transaction_id = cur.fetchone()[0]

    # Create new collector note
    cur.execute(
        "INSERT INTO collector_notes (note, transaction_id, payment_plan_id) VALUES (%s, %s, %s)",
        (note, transaction_id, payment_plan_id)
    )
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('home'))

@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()

    # Fetch the note and related transaction
    cur.execute(
        "SELECT n.id, n.note, t.id, t.customer_name, t.amount, t.transaction_date, t.transaction_time, t.payment_plan_id "
        "FROM collector_notes n "
        "JOIN customer_transactions t ON n.transaction_id = t.id "
        "WHERE n.id = %s", (note_id,)
    )
    note_data = cur.fetchone()

    # Fetch all payment plans for the dropdown
    cur.execute("SELECT id, plan_name FROM payment_plans")
    payment_plans = cur.fetchall()

    if request.method == 'POST':
        updated_note = request.form['note']
        updated_customer_name = request.form['customer_name']
        updated_amount = request.form['amount']
        updated_transaction_date = request.form['transaction_date']
        updated_transaction_time = request.form['transaction_time']
        updated_payment_plan_id = request.form.get('payment_plan_id')  # Use get() to avoid KeyError

        if not updated_payment_plan_id:
            return "Payment plan is required", 400  # Return an error if no payment plan was selected

        # Update the customer transaction
        cur.execute(
            "UPDATE customer_transactions SET customer_name = %s, amount = %s, transaction_date = %s, "
            "transaction_time = %s, payment_plan_id = %s WHERE id = %s",
            (updated_customer_name, updated_amount, updated_transaction_date, updated_transaction_time, updated_payment_plan_id, note_data[2])
        )

        # Update the collector note
        cur.execute(
            "UPDATE collector_notes SET note = %s WHERE id = %s",
            (updated_note, note_id)
        )

        mysql.connection.commit()
        cur.close()

        return redirect(url_for('home'))

    # Pre-populate the form with current values
    return render_template('edit_note.html', note_data=note_data, payment_plans=payment_plans)

@app.route('/delete_note/<int:note_id>', methods=['GET'])
def delete_note(note_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()

    # Fetch the associated transaction ID
    cur.execute("SELECT transaction_id FROM collector_notes WHERE id = %s", (note_id,))
    transaction_id = cur.fetchone()

    if transaction_id:
        # Delete the note
        cur.execute("DELETE FROM collector_notes WHERE id = %s", (note_id,))

        # Optionally, delete the associated transaction
        cur.execute("DELETE FROM customer_transactions WHERE id = %s", (transaction_id[0],))

        mysql.connection.commit()

    cur.close()
    return redirect(url_for('home'))

@app.route('/delete_transaction/<int:transaction_id>', methods=['GET'])
def delete_transaction(transaction_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()

    # Delete associated notes for this transaction first (if you want to delete them as well)
    cur.execute("DELETE FROM collector_notes WHERE transaction_id = %s", (transaction_id,))

    # Now delete the transaction
    cur.execute("DELETE FROM customer_transactions WHERE id = %s", (transaction_id,))

    mysql.connection.commit()
    cur.close()

    return redirect(url_for('home'))

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

    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)

