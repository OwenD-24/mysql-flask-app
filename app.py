from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

# Initialise Flask application
app = Flask(__name__)

# MySQL Configuration for connecting to the local MySQL server
app.config['MYSQL_HOST'] = '127.0.0.1'  # Local MySQL server address
app.config['MYSQL_PORT'] = 3306  # Default MySQL port
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'mypassword'  # MySQL password
app.config['MYSQL_DB'] = 'collections'  # Database name

# Initialise MySQL connection object
mysql = MySQL(app)

# Home route to display notes, transactions, and payment plans
@app.route('/')
def home():
    cur = mysql.connection.cursor()

    # Fetch all notes from the collector_notes table
    cur.execute("SELECT * FROM collector_notes")
    notes = cur.fetchall()

    # Fetch transactions with specific columns and formatted date/time
    cur.execute("SELECT id, customer_name, amount, DATE_FORMAT(transaction_date, '%Y-%m-%d') AS transaction_date, TIME_FORMAT(transaction_time, '%H:%i:%s') AS transaction_time FROM customer_transactions")
    transactions = cur.fetchall()

    # Fetch all payment plans
    cur.execute("SELECT * FROM payment_plans")
    payment_plans = cur.fetchall()

    cur.close()  # Close the cursor after executing the queries

    # Render home.html template and pass fetched data as variables
    return render_template('home.html', notes=notes, transactions=transactions, payment_plans=payment_plans)

# Route to handle adding a note to the database
@app.route('/add_note', methods=['POST'])
def add_note():
    if request.method == 'POST':
        # Retrieve the note text from the form input
        note = request.form['note']
        
        # Ensure the note is not empty
        if not note:
            return "Note cannot be empty", 400  # Return error if the note is empty
        
        cur = mysql.connection.cursor()

        # Retrieve transaction_id and payment_plan_id from the form
        transaction_id = request.form.get('transaction_id')
        payment_plan_id = request.form.get('payment_plan_id')
        
        # Insert the new note into the collector_notes table
        cur.execute(
            "INSERT INTO collector_notes (note, transaction_id, payment_plan_id) VALUES (%s, %s, %s)", 
            (note, transaction_id, payment_plan_id)
        )
        mysql.connection.commit()  # Commit the changes to the database
        cur.close()  # Close the cursor

        # Redirect to the home page after successfully adding the note
        return redirect(url_for('home'))

# Add a route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Validate credentials (replace this with database logic)
        if email == "admin@example.com" and password == "password123":
            return redirect(url_for('home'))
        else:
            return "Invalid credentials. Please try again.", 401

    return render_template('login.html')

# Run the app in debug mode if executed directly
if __name__ == "__main__":
    app.run(debug=True)

