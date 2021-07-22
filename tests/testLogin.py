import unittest, sys, os

sys.path.append('Mood-Tracker-Project')
from main import app, db, login

class TestLogin(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    ###############
    #### tests ####
    ###############

    def register(self, username, email, password):
        return self.app.post('/createaccount',
                            data=dict(username=username,
                                      email=email,
                                      password=password, 
                                      confirm_password=password),
                            follow_redirects=True)
    def login(self, email, password):
        return self.app.post('/login',
                            data=dict(email=email,
                                      password=password),
                            follow_redirects=True)

    def test_valid_login(self):
        response = self.register('test', 'test@example.com', 'FlaskIsAwesome')
        self.assertEqual(response.status_code, 200)
        login = self.login('test@example.com', 'FlaskIsAwesome')
        self.assertEqual(login.status_code, 200)

if __name__ == "__main__":
    unittest.main()