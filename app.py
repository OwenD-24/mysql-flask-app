# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

# Initialize Flask application
app = Flask(__name__)

# MySQL Configuration - Set up the database connection parameters
app.config['MYSQL_HOST'] = '127.0.0.1'        # MySQL host, usually '127.0.0.1' for local dev
app.config['MYSQL_PORT'] = 3306               # Default MySQL port is 3306
app.config['MYSQL_USER'] = 'root'             # MySQL username (change as needed)
app.config['MYSQL_PASSWORD'] = 'mypassword'   # MySQL password (change as needed)
app.config['MYSQL_DB'] = 'collections'        # Name of the database to connect to

# Initialize MySQL connection using the Flask app
mysql = MySQL(app)

# Home route to display data - Fetch data from three tables in the database
@app.route('/')
def home():
    # Create a cursor to interact with the database
    cur = mysql.connection.cursor()
    
    # Fetch all notes from the collector_notes table
    cur.execute("SELECT * FROM collector_notes")
    notes = cur.fetchall()  # Retrieve all rows of data

    # Fetch all transactions from the customer_transactions table
    cur.execute("SELECT * FROM customer_transactions")
    transactions = cur.fetchall()  # Retrieve all rows of data

    # Fetch all payment plans from the payment_plans table
    cur.execute("SELECT * FROM payment_plans")
    payment_plans = cur.fetchall()  # Retrieve all rows of data

    # Close the cursor to free up resources
    cur.close()

    # Render the 'home.html' template and pass the fetched data as context
    return render_template('home.html', notes=notes, transactions=transactions, payment_plans=payment_plans)

# Add a new note route - Handles POST requests for adding a new note
@app.route('/add_note', methods=['POST'])
def add_note():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        note = request.form['note']  # Get the 'note' field from the form data

        # Create a new cursor for interacting with the database
        cur = mysql.connection.cursor()
        
        # Insert the new note into the collector_notes table
        cur.execute("INSERT INTO collector_notes(note) VALUES(%s)", [note])
        
        # Commit the transaction to save the data in the database
        mysql.connection.commit()

        # Close the cursor after the query is executed
        cur.close()

        # Redirect to the home route after successful note insertion
        return redirect(url_for('home'))

# Main entry point for running the Flask app
if __name__ == "__main__":
    # Run the Flask app in debug mode (auto-reloads and shows detailed errors)
    app.run(debug=True)
