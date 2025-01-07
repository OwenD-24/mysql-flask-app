from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'collections'

mysql = MySQL(app)

@app.route('/test_db')
def test_db():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    tables = cur.fetchall()
    cur.close()
    return str(tables)
