from flask import Response, request, jsonify
from src import app, db, debug
from src.api.models.task import Task
from datetime import datetime
import json, os


class TaskView:
    
	@app.route('/api/tasks', methods=['GET'])
	def index():

		response = {'data': []}		
		
		tasks = Task.query.all()						
		
		for task in tasks:
			
			record = {
				'id': task.id,
				'title': task.title,
				'date_begin': task.date_begin.isoformat(),
				'date_until': task.date_until.isoformat(),
				'description': task.description
			}
			
			response['data'].append(record)		

				
		return Response(json.dumps(response), content_type='application/json', status=200)	

	
	@app.route('/api/tasks/add', methods=['POST'])
	def add():
		
		try:
			data = {
				'title': request.json.get('title'),
				'description': request.json.get('description'),
				'date_begin': datetime.strptime(request.json.get('date_begin'), '%Y-%m-%d %H:%M:%S'),
				'date_until': datetime.strptime(request.json.get('date_until'), '%Y-%m-%d %H:%M:%S')
			}
			
			task = Task(data)
						
			db.session.add(task)
			db.session.commit()
			db.session.flush()
			
			response = {
				'status': 'success',
				'message': 'Task added successfully'				
			} 

			return Response(json.dumps(response), content_type='application/json', status=201)	

		except Exception as err:
			db.session.rollback()
			response = {
				'status': 'error', 
				'message': str(err) if debug else 'Something was wrong. Try again later!'
			}
			return Response(json.dumps(response), content_type='application/json', status=422)	
	
	@app.route('/api/tasks/edit/<id>', methods=['PUT'])
	def edit(id):
		
		try:
			task = Task.query.get(id)
			task.title = request.json.get('title'),
			task.description = request.json.get('description'),
			task.date_begin = datetime.strptime(request.json.get('date_begin'), '%Y-%m-%d %H:%M:%S'),
			task.date_until = datetime.strptime(request.json.get('date_until'), '%Y-%m-%d %H:%M:%S')
			
			db.session.commit()
			db.session.flush()
			
			response = {
				'status': 'success',
				'message': 'Task edited successfully'
			}

			return Response(json.dumps(response), content_type='application/json', status=201)
		
		except Exception as err:
			db.session.rollback()
			response = {
				'status': 'error', 
				'message': str(err) if debug else 'Something was wrong. Try again later!'
			}
			return Response(json.dumps(response), content_type='application/json', status=422)
			

	@app.route('/api/tasks/remove/<id>', methods=['DELETE'])
	def remove(id):
		try:
			task = Task.query.get(id)
			
			db.session.delete(task)
			db.session.commit()
			db.session.flush()

			response = {
				'status': 'success',
				'message': 'Task removed successfully'				
			}

			return Response(json.dumps(response), content_type='application/json', status=200)

		except Exception as err:
			db.session.rollback()
			response = {
				'status': 'error', 
				'message': str(err) if debug else 'Something was wrong. Try again later!'
			}
			return Response(json.dumps(response), content_type='application/json', status=400)

	
	@app.route('/api/tasks/show/<id>', methods=['GET'])
	def show(id):
		try:
			task = Task.query.get(id)
			
			response = {
				'data': {
					'id': task.id,
					'title': task.title,
					'description': task.description,
					'date_begin': task.date_begin.isoformat(),
					'date_until': task.date_until.isoformat()
				}
			}
		
			return Response(json.dumps(response), content_type='application/json', status=200)

		except Exception as err:			
			response = {
				'status': 'error', 
				'message': str(err) if debug else 'Something was wrong. Try again later!'				
			}
			return Response(json.dumps(response), content_type='application/json', status=404)		

			
