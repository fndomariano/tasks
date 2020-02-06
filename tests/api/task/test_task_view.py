from src import app

import json
import unittest

class TaskView(unittest.TestCase):

	def setUp(self):
		self.client = app.test_client()
		
	def test_index(self):
		response = self.client.get('http://localhost:5000/api/tasks')
		self.assertEqual(200, response.status_code)
		self.assertIn('application/json', response.content_type)