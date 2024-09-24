from app import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(140))
    date = db.Column(db.DateTime(), default=datetime.now())
    completed = db.Column(db.Boolean(), default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self):
        return f'<Task id: {self.id} - {self.title}'
    


