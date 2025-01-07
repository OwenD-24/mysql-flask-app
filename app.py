from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

# Initialize Flask application
app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'flask_user'  # Change to your MySQL username
app.config['MYSQL_PASSWORD'] = 'mypassword'  # Change to your MySQL password
app.config['MYSQL_DB'] = 'collections'

# Initialize MySQL connection
mysql = MySQL(app)

@app.route('/')
def home():
    # Create cursor to interact with the database
    cur = mysql.connection.cursor()

    # Fetch data from collector_notes
    cur.execute("SELECT * FROM collector_notes")
    notes = cur.fetchall()

    # Fetch data from customer_transactions
    cur.execute("SELECT * FROM customer_transactions")
    transactions = cur.fetchall()

    # Fetch data from payment_plans
    cur.execute("SELECT * FROM payment_plans")
    payment_plans = cur.fetchall()

    cur.close()

    # Render home.html and pass data
    return render_template('home.html', notes=notes, transactions=transactions, payment_plans=payment_plans)

@app.route('/add_note', methods=['POST'])
def add_note():
    if request.method == 'POST':
        note = request.form['note']
        
        # Simple form validation: Ensure that the note is not empty
        if not note:
            return "Note cannot be empty", 400
        
        cur = mysql.connection.cursor()
        
        # Example Foreign Key insertion (assuming 'transaction_id' is passed)
        transaction_id = request.form['transaction_id']  # Assuming transaction_id is passed with the note
        payment_plan_id = request.form['payment_plan_id']  # Assuming payment_plan_id is passed with the note

        # Inserting note with foreign keys
        cur.execute(
            "INSERT INTO collector_notes (note, transaction_id, payment_plan_id) VALUES (%s, %s, %s)", 
            [note, transaction_id, payment_plan_id]
        )
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
