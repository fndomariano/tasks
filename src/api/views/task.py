from flask import Response, request
from src import app, db
from src.api.models.task import Task
from datetime import datetime
import json, os


class TaskView:
    
	@app.route('/api/tasks', methods=['GET'])
	def index():
		response = {
			'status': 'success',
			'message': 'Request successful',			
		}
		
		return Response(json.dumps(response), content_type='application/json')	

	
	@app.route('/api/tasks/add', methods=['POST'])
	def add():
		
		try:
			data = {
				'title': request.json.get('title'),
				'description': request.json.get('description'),
				'date_begin': datetime.strptime(request.json.get('date_begin'), '%d/%m/%Y %H:%M:%S'),
				'date_until': datetime.strptime(request.json.get('date_until'), '%d/%m/%Y %H:%M:%S')
			}
			
			task = Task(data)
						
			db.session.add(task)
			db.session.commit()
			db.session.flush()
			
			return Response(json.dumps({'id': task.id}), content_type='application/json', status=201)	

		except Exception as err:
			
			db.session.rollback()
			response = {'status': 'error', 'message': str(err)}
			
			return Response(json.dumps(response), content_type='application/json', status=422)	
		


			
