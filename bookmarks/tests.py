"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class ViewTest(TestCase):
	fixtures = ['test_data.json']
	def setUp(self):
		self.client = Client()

	def test_register_page(self):
		data ={'username':'test_user','email':'123@example.com','password1':'pass123','password2':'pas123'}
		response = self.client.post('/register/',data)
		self.assertEqual(response.status_code,302)
	def test_bookmark_save(self):
		response = self.client.login('/save/','lu','1990730')
		self.assertTrue(response)
		data = {'url':'http://hao123.com','title':'Test Url','tags':'test-tag'}
		response = self.client.post('/save/',data)
		self.assertEqual(response.status_code,302)

		response = self.client.get('/user/lu/')
		self.assertTrue("http://hao123.com" in response.content)
		self.assertTrue('Test Url' in response.content)
		self.assertTrue('test-tag' in response.content)