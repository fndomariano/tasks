from src import app, db
from src.api.models.task import Task
from faker import Faker

import json
import unittest

class TaskView(unittest.TestCase):

	def setUp(self):
		self.client = app.test_client()
		self.faker = Faker()
		self.base_url = 'http://localhost:5000/api/tasks' 
		self.task = {
			'title': self.faker.sentence(),
			'date_begin': self.faker.date() + ' 08:00:00',
			'date_until': self.faker.date() + ' 18:00:00',
			'description': self.faker.text()
		}		
		
	def test_index(self):
		response = self.client.get(self.base_url)
		self.assertEqual(200, response.status_code)
		self.assertIn('application/json', response.content_type)

	def test_post(self):
		response = self.client.post(self.base_url + '/add', json=self.task)		
		self.assertEqual(201, response.status_code)
		self.assertIn('application/json', response.content_type)		
		self.assertEqual('success', response.json.get('status'))

	def test_invalid_post(self):
		task = self.task
		del task['date_until']

		response = self.client.post(self.base_url + '/add', json=task)

		self.assertEqual(422, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual(True, "status" in response.json)
		self.assertEqual('error', response.json.get('status'))

	def test_show(self):	
		task = Task(self.task)
		db.session.add(task)
		db.session.commit()

		response = self.client.get(self.base_url + '/show/' + str(task.id))
		self.assertEqual(200, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual(True, 'data' in response.json)

	def test_invalid_show(self):
		response = self.client.get(self.base_url + '/show/0')
		self.assertEqual(404, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual('error', response.json.get('status'))

	def test_remove(self):
		task = Task(self.task)
		db.session.add(task)
		db.session.commit()

		response = self.client.delete(self.base_url + '/remove/' + str(task.id))
		self.assertEqual(200, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual('success', response.json.get('status'))
	
	def test_invalid_remove(self):
		response = self.client.delete(self.base_url + '/remove/0')
		self.assertEqual(400, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual('error', response.json.get('status'))

	def test_put(self):
		task = Task(self.task)		
		db.session.add(task)
		db.session.commit()		
		
		new_data = {
			'title': self.faker.sentence(),
			'date_begin': self.faker.date() + ' 08:00:00',
			'date_until': self.faker.date() + ' 18:00:00',
			'description': self.faker.text()
		}

		response = self.client.put(self.base_url + '/edit/' + str(task.id), json=new_data)
		
		self.assertEqual(201, response.status_code)
		self.assertIn('application/json', response.content_type)		
		self.assertEqual('success', response.json.get('status'))

	def test_invalid_put(self):
		response = self.client.put(self.base_url + '/edit/0', json=self.task)
		self.assertEqual(422, response.status_code)
		self.assertIn('application/json', response.content_type)
		self.assertEqual(True, "status" in response.json)
		self.assertEqual('error', response.json.get('status'))
