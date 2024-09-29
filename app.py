from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import url_for
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

from config import Config


load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
import models
from forms import TaskForm

@app.route('/')
def index():
    tasks = models.Task.query.all()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)

    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_task():
    user_input = request.get_json()

    form = TaskForm(data=user_input)

    if form.validate():
        task = models.Task(title=form.title.data)

        db.session.add(task)
        db.session.commit()

        return jsonify(task)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()