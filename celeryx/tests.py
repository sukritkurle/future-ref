import uuid
from test_celery.db_connect import connection
from pymysql import escape_string as thwart


class CreateNewTest:
	def __init__(self, name, email, test_schedule):
		self.test_name = name
		self.owner_email = email
		self.frequency = test_schedule

		uid = uuid.uuid1()
		self.test_id = str(uid)
		self.last_run = "new"

	def update_database(self):
		"""
		Update test database with an entry of the new test.
		"""
		c, conn = connection()

		c.execute("""INSERT INTO tests (test_id, test_name, owner_email,
			frequency, last_run) VALUES (%s, %s, %s, %s, %s)""",
			(thwart(self.test_id), thwart(self.test_name),
			thwart(self.owner_email), thwart(self.frequency),
			thwart(self.last_run)))

		conn.commit()
		c.close()
		conn.close()

test = CreateNewTest('Demo Test', 'user@email.com', 'hourly')
test.update_database()
