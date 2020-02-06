from flask import Response, request
from src import app

import json


class TaskView:
    
	@app.route('/api/tasks', methods=['GET'])
	def index():
		response = {
			'status': 'success',
			'message': 'Request successful'
		}
		return Response(json.dumps(response), content_type='application/json')	

		