from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

from config import Config


load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
import models

@app.route('/')
def index():
    tasks = models.Task.query.all()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()