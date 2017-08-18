from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    '''Test whether flask app was setup correctly'''

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Login loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure login works correctly with correct credentials
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b'You are logged in', response.data)

    # Ensure login works correctly with incorrect credentials
    def test_login_page_fail(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='cms123', password='adminxnxnx'),
            follow_redirects=True
        )
        self.assertIn(b'Invalid login credentials, please try again!', response.data)

    # logout page works correctly
    def test_logout_route(self):
        tester = app.test_client(self)
        response = tester.get('/logout',
                              content_type='html/text',
                              follow_redirects=True)
        self.assertIn(b'You are logged out', response.data)

    # Index page requires login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'Unauthorized to access to this page, Please login' in response.data)

    # Welcome page works correctly
    def test_welcome_route(self):
        tester = app.test_client(self)
        response = tester.get('/welcome', content_type='html/text')
        self.assertTrue(b'Welcome to Flask!' in response.data)


if __name__ == '__main__':
    unittest.main()
