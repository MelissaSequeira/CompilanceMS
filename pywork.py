from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///act.db'
app.secret_key = 'your_secret_key'  # Set a secret key for session
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(20), nullable=False)
    risk = db.Column(db.String(20), nullable=False)

# Define Complaint model
class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    issue = db.Column(db.String(200), nullable=False)

# Ensure tables are created within the application context
with app.app_context():
    db.create_all()

# Initialize dictionary to store button statuses
button_statuses = {}

app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for session



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['rusername']
        password = request.form['rpassword']
        email = request.form['remail']

        if not (username and password and email):
            error = 'All fields are required.'
            return render_template('registration.html', error=error)

        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()

        if existing_user or existing_email:
            error = 'Username or email already exists. Please choose a different one.'
            return render_template('registration.html', error=error)
        else:
            new_user = User(username=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['lusername']
        password = request.form['lpassword']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))
@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))


    if request.method == 'POST':
        if 'toggle_button' in request.form:
            task_id = int(request.form['toggle_button'])
            toggle_button_color(task_id)

        # Get data from the form
        activity = request.form.get('activity')  # Use get method to avoid KeyError
        duration = request.form.get('duration')
        risk = request.form.get('risk')

        # Create a new Task instance if activity, duration, and risk are present
        if activity and duration and risk:
            new_task = Task(activity=activity, duration=duration, risk=risk)
            # Add and commit the new task to the database
            db.session.add(new_task)
            db.session.commit()

            # Redirect to the home page to refresh the tasks
            return redirect(url_for('index'))
        # Handle form submission for complaints
        username = session['username']
        topic = request.form['comp-part']
        issue = request.form['comp-reason']
        if username and topic and issue:
            new_complaint = Complaint(username=username, topic=topic, issue=issue)
            db.session.add(new_complaint)
            db.session.commit()

    complaints = Complaint.query.all()
    
    # Fetch all tasks from the database
    act = Task.query.all()
    # Sort tasks based on risk percentage
    sorted_act = sorted(act, key=lambda x: int(x.risk.strip('%')))

    # Calculate data for the bar graph (activities and associated risks)
    activities = [task.activity for task in sorted_act]
    risks = [int(risk.strip('%')) for risk in [task.risk for task in sorted_act]]  # Extract risk values and convert to integers

    # Generate bar graph using Matplotlib
    plt.figure(figsize=(8, 6))
    if risks:  # Check if risks list is not empty
        plt.bar(activities, risks, color='blue')
        plt.xlabel('Activities')
        plt.ylabel('Risks (%)')  # Update y-axis label to indicate percentage
        plt.title('Risks Statistics')
        plt.xticks(rotation=45, ha='right')

    # Set the bottom limit of the y-axis to 0
        plt.ylim(0, max(risks) + 10)  # Add some buffer to the maximum risk value for better visualization

    # Set y-axis tick labels to display percentages
        plt.gca().set_yticklabels(['{:.0f}%'.format(x) for x in plt.gca().get_yticks()])

    # Save the plot to a bytes buffer
        img_bytes = io.BytesIO()
        plt.savefig(img_bytes, format='png')
        img_bytes.seek(0)

    # Encode the image in base64 format
        img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    else:
        img_base64 = None


    # Generate pie chart for button statuses
    plt.figure(figsize=(6, 6))
    done_count = list(button_statuses.values()).count('done')
    undone_count = len(button_statuses) - done_count

    if done_count > 0 or undone_count > 0:
        labels = ['Undone', 'Done']
        sizes = [done_count, undone_count]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Updates')

        # Save the pie chart to a bytes buffer
        pie_img_bytes = io.BytesIO()
        plt.savefig(pie_img_bytes, format='png')
        pie_img_bytes.seek(0)

        # Encode the pie chart in base64 format
        pie_img_base64 = base64.b64encode(pie_img_bytes.getvalue()).decode('utf-8')
    else:
        pie_img_base64 = None

    return render_template('index.html', act=act, img_base64=img_base64, pie_img_base64=pie_img_base64,complaints=complaints)

@app.route('/toggle_button/<int:task_id>', methods=['POST'])
def toggle_button(task_id):
    toggle_button_color(task_id)
    return redirect(url_for('index'))

# Function to toggle button color
def toggle_button_color(task_id):
    session_key = f'button_color_{task_id}'
    if session_key not in session:
        session[session_key] = 'undone'  # Set initial color to undone if not set
    else:
        session[session_key] = 'done' if session[session_key] == 'undone' else 'undone'

    # Update button status dictionary
    button_statuses[task_id] = session[session_key]

@app.route('/remove_task/<int:task_id>', methods=['POST'])
def remove_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    # Remove task from button status dictionary
    button_statuses.pop(task_id, None)
    return redirect(url_for('index'))

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    activity = request.form.get('activity')
    duration = request.form.get('duration')
    risk = request.form.get('risk')

    if activity and duration and risk:
        task.activity = activity
        task.duration = duration
        task.risk = risk

        db.session.commit()

    return redirect(url_for('index'))

@app.route('/remove_complaint/<int:complaint_id>', methods=['POST'])
def remove_complaint(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    db.session.delete(complaint)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
