from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

from config import Config

load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()