from flask import Response, request, jsonify
from src import app, db
from src.api.models.task import Task
from datetime import datetime
import json, os


class TaskView:
    
	@app.route('/api/tasks', methods=['GET'])
	def index():

		response = {'data': []}		
		
		tasks = Task.query.all()				
		total = session.query(func.count(Task.id))

		if (total > 0):
			for task in tasks:
				
				record = {
					'id': task.id,
					'title': task.title,
					'date_begin': task.date_begin.isoformat(),
					'date_until': task.date_until.isoformat(),
					'description': task.description
				}
				
				response['data'].append(record)		

				
		return Response(json.dumps(response), content_type='application/json', status=201)	

	
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
			
			response = {
				'status': 'success',
				'message': 'Task added successfully',
				'id': task.id
			} 

			return Response(json.dumps(response), content_type='application/json', status=201)	

		except Exception as err:
			
			db.session.rollback()
			response = {'status': 'error', 'message': str(err)}
			
			return Response(json.dumps(response), content_type='application/json', status=422)	
		


			
