from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# from app import routes

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime)

@app.route('/', methods=['GET'])
def index():
    todos = Todo.query.all()
    return render_template('index.html'  ,title = 'Flask App', todos = todos )

@app.route('/add/',methods= ['POST'] )
def add():
    data = request.form['task']
    print(data)

    todo = Todo(task=data, date=datetime.now())
    db.session.add(todo)
    db.session.commit()

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)

