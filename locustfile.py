from locust import HttpLocust, TaskSet, task
from locust import ResponseError
import json


class UserBehavior(TaskSet):

	def __init__(self, parent):
		super(UserBehavior, self).__init__(parent)
		self.token = ""
		self.headers = {}

	def on_start(self):
		# The on_start method is called
		# when a simulated user starts
		# executing that TaskSet class
		self.token = self.login()
		self.headers = {'Authorization': 'Bearer {}'.format(self.token)}
		self.login()

	def login(self):
		# admin login and retrieving it's access token
		response = self.client.post("/login/",
									data = {'username': 'admin',
										'password': 'ZYT5nsg3565!'})
		
		return json.loads(response._content)['access']



class WebsiteUser(HttpLocust):
	# The task_set attribute should point
	# to a TaskSet class which defines
	# the behaviour of the user
	task_set = UserBehavior
	min_wait = 5000
	max_wait = 9000

