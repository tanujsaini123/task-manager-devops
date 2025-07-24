from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)

# Home Route - View all tasks
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# Add Task Route
@app.route('/add', methods=['POST'])
def add():
    task_content = request.form['content']
    if task_content.strip():  # Prevent empty tasks
        new_task = Task(content=task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

# Toggle Complete/Incomplete
@app.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get_or_404(id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('index'))

# Delete Task
@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# Start the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # ✅ Create the table if it doesn't exist
    app.run(debug=True, host='0.0.0.0')
