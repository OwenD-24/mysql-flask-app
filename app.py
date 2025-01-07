from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

# Initialize Flask application
app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'  # Local MySQL server address (localhost)
app.config['MYSQL_PORT'] = 3306  # Default MySQL port
app.config['MYSQL_USER'] = 'flask_user'  # MySQL username (change it to your actual username)
app.config['MYSQL_PASSWORD'] = 'mypassword'  # MySQL password (change it to your actual password)
app.config['MYSQL_DB'] = 'collections'  # Database name (ensure the DB exists in MySQL)

# Initialize MySQL connection
mysql = MySQL(app)

# Home route to display notes, transactions, and payment plans
@app.route('/')
def home():
    cur = mysql.connection.cursor()

    # Fetch data from collector_notes table
    cur.execute("SELECT * FROM collector_notes")
    notes = cur.fetchall()

    # Fetch data from customer_transactions table
    cur.execute("SELECT * FROM customer_transactions")
    transactions = cur.fetchall()

    # Fetch data from payment_plans table
    cur.execute("SELECT * FROM payment_plans")
    payment_plans = cur.fetchall()

    cur.close()  # Close the cursor after executing the queries

    # Render home.html and pass the fetched data to the template
    return render_template('home.html', notes=notes, transactions=transactions, payment_plans=payment_plans)

# Route for adding a note to the database
@app.route('/add_note', methods=['POST'])
def add_note():
    if request.method == 'POST':
        # Retrieve form data
        note = request.form['note']
        
        # Check if the note input is empty
        if not note:
            return "Note cannot be empty", 400  # Return a bad request if the note is empty
        
        cur = mysql.connection.cursor()

        # Get foreign keys for transaction and payment plan from the form
        transaction_id = request.form['transaction_id']
        payment_plan_id = request.form['payment_plan_id']
        
        # Insert note with foreign keys into the database
        cur.execute(
            "INSERT INTO collector_notes (note, transaction_id, payment_plan_id) VALUES (%s, %s, %s)", 
            (note, transaction_id, payment_plan_id)
        )
        mysql.connection.commit()  # Commit the transaction to the database
        cur.close()  # Close the cursor

        # Redirect to the home page after adding the note
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

