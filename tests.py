import unittest
from flask_testing import TestCase
from flask_login import current_user

from project import app, db
from project.models import User, BlogPost

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "admin@admin.com", "admin"))
        db.session.add(
            BlogPost("Test post", "This is a test. Only a test.", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class FlaskTestCase(BaseTestCase):
    '''Test whether flask app was setup correctly'''

    def test_index(self):
        # tester = app.test_client(self)
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Index page requires login
    def test_main_route_requires_login(self):
        # tester = app.test_client(self)
        response = self.client.get('/', follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)

    # Welcome page works correctly
    def test_welcome_route(self):
        # tester = app.test_client(self)
        response = self.client.get('/welcome', content_type='html/text')
        self.assertTrue(b'Welcome to Flask!' in response.data)

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'This is a test. Only a test.', response.data)


class UsersViewTests(BaseTestCase):

    # Login loads correctly
    def test_login_page_loads(self):
        # tester = app.test_client(self)
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure login works correctly with correct credentials
    def test_login_page(self):
        # tester = app.test_client(self)
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username='admin', password='admin'),
                follow_redirects=True
            )
            self.assertIn(b'You are logged in', response.data)
            self.assertTrue(current_user.name == 'admin')
            self.assertTrue(current_user.is_active)

    # Ensure login works correctly with incorrect credentials
    def test_login_page_fail(self):
        # tester = app.test_client(self)
        response = self.client.post(
            '/login',
            data=dict(username='cms123', password='adminxnxnx'),
            follow_redirects=True
        )
        self.assertIn(b'Invalid login credentials, please try again!', response.data)

    # logout page works correctly
    def test_logout_route(self):
        # tester = app.test_client(self)
        with self.client:
            response = self.client.get('/logout',
                                       content_type='html/text',
                                       follow_redirects=True)
            self.assertIn(b'You are logged out', response.data)
            self.assertFalse(current_user.is_active)

    # Ensure register works correctly with correct credentials
    def test_user_register(self):
        # tester = app.test_client(self)
        with self.client:
            response = self.client.post(
                '/register/',
                data=dict(username='johndoe', email='john@doe.com',
                          password='john123', confirm='john123'),
                follow_redirects=True
            )
            self.assertIn(b'Welcome to Flask!', response.data)
            self.assertTrue(current_user.name == 'johndoe')
            self.assertTrue(current_user.is_active)


if __name__ == '__main__':
    unittest.main()
