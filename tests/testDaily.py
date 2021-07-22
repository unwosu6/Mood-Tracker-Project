import unittest, sys, os

sys.path.append('Mood-Tracker-Project')
from main import app, db, daily

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

    def daily(self, email, password):
        return self.app.post('/daily',
                             data=dict(email=email,
                                      password=password),
                             follow_redirects=True)

    def test_valid_daily(self):
        daily = self.daily('test@example.com', 'FlaskIsAwesome')
        self.assertEqual(daily.status_code, 200)

if __name__ == "__main__":
    unittest.main()