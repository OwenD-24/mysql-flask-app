from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session management

# MySQL Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mypassword'
app.config['MYSQL_DB'] = 'collections'

mysql = MySQL(app)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Replace this with actual DB validation for email and password
        if email == "admin@example.com" and password == "password123":
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return "Invalid credentials. Please try again.", 401

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

# Home route
@app.route('/')
def home():
    if not session.get('logged_in'):  # Redirect to login if not logged in
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

if __name__ == "__main__":
    app.run(debug=True)



