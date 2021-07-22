import unittest, sys, os

sys.path.append('Mood-Tracker-Project')
from main import app, db, happy

class UsersTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    ###############
    #### tests ####
    ###############

    def happy(self, email, password):
        return self.app.post('/generate-happy',
                            data=dict(email=email,
                                      password=password, 
                                      confirm_password=password),
                            follow_redirects=True)

    def test_valid_happy(self):
        happy = self.history()
        self.assertEqual(happy.status_code, 200)

    def history(self):
        return self.app.get('/history')
if __name__ == "__main__":
    unittest.main()