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

	def test_invalid_index(self):		
		response = self.client.get('http://localhost:5000/api/tasks')
		self.assertEqual(200, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual([], response.json.get('data'))		

	def test_post(self):

		task = {
			'title': 'Test Title',
			'date_begin': '02/02/2020 08:00:00',
			'date_until': '02/02/2020 18:00:00',
			'description': 'Lorem Ipsum'
		}

		response = self.client.post('http://localhost:5000/api/tasks/add', json=task)
		
		self.assertEqual(201, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual(True, "id" in response.json)
		self.assertEqual('success', response.json.get('status'))

	def test_invalid_post(self):

		task = {
			'title': 'Test Title',
			'date_begin': '',
			'date_until': '',
			'description': ''
		}

		response = self.client.post('http://localhost:5000/api/tasks/add', json=task)

		self.assertEqual(422, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual(True, "status" in response.json)
		self.assertEqual('error', response.json.get('status'))

	def test_show(self):		
		response = self.client.get('http://localhost:5000/api/tasks/show/8')
		self.assertEqual(200, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual(True, 'data' in response.json)

	def test_invalid_show(self):
		response = self.client.get('http://localhost:5000/api/tasks/show/9999')
		self.assertEqual(404, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual('error', response.json.get('status'))

	def test_remove(self):
		response = self.client.delete('http://localhost:5000/api/tasks/remove/5')
		self.assertEqual(200, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual('success', response.json.get('status'))
	
	def test_invalid_remove(self):
		response = self.client.delete('http://localhost:5000/api/tasks/remove/9999')
		self.assertEqual(400, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual('error', response.json.get('status'))