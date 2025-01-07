# Collections Dashboard

The **Collections Dashboard** is a web application built using Flask and MySQL, designed for managing and displaying collector notes, customer transactions, and payment plans. This application allows collectors to input new notes, view customer transactions, and manage payment plans in a centralised and easy-to-use interface.

## Application Overview

### Features

- **Dashboard**: A central overview of all key metrics, such as notes, transactions, and payment plans.
- **Add Note**: A form to add new notes, linked to a specific customer transaction and associated payment plan.
- **Customer Transactions**: Track the financial transactions made by customers, such as payments and adjustments.
- **Payment Plans**: Manage installment plans that break down customer payments over time.
- **MySQL Database**: Data is stored securely in a MySQL database, with three primary tables: `collector_notes`, `customer_transactions`, and `payment_plans`.

### Technology Stack

- **Flask**: Python web framework used for building the application.
- **MySQL**: Relational database for storing data such as customer transactions and notes.
- **HTML/CSS/JS**: For front-end design and layout of the dashboard and forms.

## Bug Fixes

### 1. **Flask Route Not Returning Correct Template**
   - **Issue**: When attempting to render a template for a specific route, Flask was returning a 404 error.
   - **Fix**: Ensured that the route was correctly defined in `app.py` with proper URL path and that the corresponding template existed in the `templates/` directory.

### 2. **SQLAlchemy Model Not Updating**
   - **Issue**: Changes made to the SQLAlchemy model weren’t being reflected in the database.
   - **Fix**: Ran `flask db migrate` and `flask db upgrade` to ensure the database schema was updated after modifying the models.

### 3. **Template Variables Not Passing to Frontend**
   - **Issue**: Some variables passed from routes were not showing up in the templates.
   - **Fix**: Ensured that the variables were being correctly passed in the `render_template` function and that the variable names in the templates matched those in the route.

### 4. **Form Validation Not Working Properly**
   - **Issue**: The forms were not validating input fields correctly, causing errors during form submission.
   - **Fix**: Implemented proper form validation using Flask-WTF, and ensured that the form fields were being properly bound and validated.

### 5. **CSS and JS Not Loading on Deployment**
   - **Issue**: Static files (CSS, JavaScript) were not being properly served in the production environment on Heroku.
   - **Fix**: Configured `Flask` to serve static files from the correct directory and ensured proper setup for production in the `config.py` file.

### Database Structure

The application uses a MySQL database to store the following tables:

#### `collector_notes`
- **id**: Auto-incremented primary key.
- **note**: Text field for storing the content of the collector's note.
- **transaction_id**: Foreign key that links to a specific customer transaction.
- **payment_plan_id**: Foreign key that links to a specific payment plan.

#### `customer_transactions`
- **id**: Auto-incremented primary key.
- **customer_name**: Name of the customer involved in the transaction.
- **amount**: The transaction amount.
- **date**: The date of the transaction.
- **payment_status**: Status of the transaction (e.g., paid, pending).

#### `payment_plans`
- **id**: Auto-incremented primary key.
- **plan_name**: Name of the payment plan (e.g., "Installment Plan 1").
- **total_amount**: Total amount to be paid under the plan.
- **monthly_payment**: Amount due each month.
- **start_date**: The start date of the payment plan.
- **end_date**: The end date of the payment plan.

### Application Workflow

1. **Add Customer Transaction**: The user can input new transactions for customers, specifying details such as the customer’s name, amount, and payment status.
2. **Link Notes to Transactions and Payment Plans**: Collectors can create notes linked to specific customer transactions and payment plans, providing additional context or updates on the status of a payment or transaction.
3. **View Dashboard**: The dashboard provides an overview of all customer transactions, payment plans, and notes. This allows the user to easily track progress and stay organized.

### Key Routes

- **`/`**: The home page that displays the dashboard with all transactions, payment plans, and notes.
- **`/add_note`**: Route for adding a new collector note linked to a transaction and payment plan.
- **`/add_transaction`**: Route for adding a new customer transaction.
- **`/add_payment_plan`**: Route for adding a new payment plan.

### Setting Up the Project

#### Prerequisites

- **Python**: The application is built using Python 3.x. Make sure Python is installed on your machine.
- **MySQL**: The application uses MySQL as the database. You must have MySQL installed and running on your local machine.
- **Flask**: Flask is required to run the application. You can install it using `pip`.

## Future Features

### 1. **User Authentication and Authorization**
   - Implement user registration, login, and logout functionality.
   - Add role-based access control (e.g., admin, collector) to manage permissions for different types of users.

### 2. **Email Notifications**
   - Integrate email notifications for important events such as payment plan updates, overdue payments, and newly added notes.
   - Users can subscribe to get notified when their payment status changes.

### 3. **PDF Export for Transaction Reports**
   - Add functionality to generate PDF reports of customer transactions, notes, and payment plans.
   - Allow users to download these reports for offline viewing or printing.

### 4. **Advanced Search and Filters**
   - Provide advanced search options to filter transactions and notes based on various parameters (e.g., customer name, transaction date, payment status).
   - Enable pagination for better navigation when there are large amounts of data.

### 5. **Charts and Analytics Dashboard**
   - Implement data visualization features using charts and graphs to provide insights on transaction history, payment plan progress, and note frequency.
   - Create a summary dashboard with charts showing metrics like total payments, outstanding balances, and overdue payments.


## Credits & Acknowledgments

### Coding Resources for Flask App Development

1. **Flask Documentation** - [Flask Documentation](https://flask.palletsprojects.com/)
   - Official Flask documentation that provided extensive help on setting up routes, templates, and configuring the app.
   
2. **Flask Mega-Tutorial** - [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
   - A comprehensive tutorial that guided the structure of the app, including models, templates, and databases.

3. **Flask Tutorial by Corey Schafer** - [YouTube Tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA)
   - Corey Schafer's video series on Flask provided clear explanations and practical examples for building web apps.

4. **Real Python Flask Tutorials** - [Real Python Flask](https://realpython.com/tutorials/flask/)
   - A series of in-depth tutorials on Flask from Real Python, covering essential concepts like Flask forms, authentication, and deployment.

5. **SQLAlchemy Documentation** - [SQLAlchemy Docs](https://www.sqlalchemy.org/)
   - SQLAlchemy was used as the ORM for handling the database interactions, and the documentation helped with setup and usage.

---

### ChatGPT Credits

1. **OpenAI ChatGPT** - [ChatGPT](https://openai.com/)
   - This app integrates the OpenAI GPT-3 model via the OpenAI API. GPT-3 powers the chatbot, and its capabilities in natural language understanding, text generation, and conversation were instrumental in providing conversational features to the app.
   
2. **OpenAI API Documentation** - [OpenAI API Docs](https://platform.openai.com/docs/)
   - Official documentation for using the OpenAI API. It provides crucial information on making API calls, configuring request parameters, and handling responses.

3. **OpenAI GitHub Repository** - [OpenAI GitHub](https://github.com/openai)
   - The official GitHub repositories from OpenAI provided code examples and insights into the implementation of the API and model integration.

---

### Additional Acknowledgments

- **Stack Overflow** - [Stack Overflow](https://stackoverflow.com/)
   - For providing community-driven solutions to common issues faced during Flask app development.

- **GitHub Repositories & Open Source Projects** - Various GitHub repositories helped in solving coding problems and provided reusable code snippets.

- **TutorialsPoint** - [TutorialsPoint](https://www.tutorialspoint.com/)
   - For additional learning materials on Python, Flask, HTML, and CSS that were useful throughout the app development.

---

### Special Thanks

- A big thank you to the open-source community and various developers who contribute tutorials, resources, and code to help beginners and professionals alike build applications.

