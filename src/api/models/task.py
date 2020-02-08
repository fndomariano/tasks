from src import db

class Task(db.Model):

	__tablename__ = 'task'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(150), nullable=False)
	description = db.Column(db.Text, nullable=False)
	date_begin = db.Column(db.DateTime, nullable=False)
	date_until = db.Column(db.DateTime, nullable=False)

	def __init__(self, data):
		self.title = data['title']
		self.description = data['description']
		self.date_begin = data['date_begin']
		self.date_until = data['date_until']
		
	def __repr__(self):
		return '<Task %r>' %self.title