import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Algorithms, Robots, Results
from os import getenv

class TestBase(TestCase):
    def create_app(self):

        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        hashed_pw = bcrypt.generate_password_hash('admin2016')
        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password=hashed_pw)

        # create test non-admin user
        hashed_pw_2 = bcrypt.generate_password_hash('test2016')
        employee = Users(first_name="test", last_name="user", email="test@user.com", password=hashed_pw_2)

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


#First test
class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)

    def test_register_view(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code,200)

    def test_robot_view(self):
        response = self.client.get(url_for('robot'))
        self.assertEqual(response.status_code,200)

    def test_algorithm_view(self):
        response = self.client.get(url_for('algorithm'))
        self.assertEqual(response.status_code,200)

    def test_result_view(self):
        response = self.client.get(url_for('result'))
        self.assertEqual(response.status_code,200)

    def test_login_view(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code,200)

    def test_addrobot_view(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        response = self.client.get(url_for('addRobot'))
        self.assertEqual(response.status_code,200)

    def test_addalgorithm_view(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        response = self.client.get(url_for('addAlgorithm'))
        self.assertEqual(response.status_code,200)

    def test_addresult_view(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        response = self.client.get(url_for('addResult'))
        self.assertEqual(response.status_code,200)

    def test_updaterobot_view(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addRobot'),
            data=dict(
                model_name='Testbot',
                drive_type='Test motor',
                height=42,
                width=42,
                length=42),
            follow_redirects=True)
        response = self.client.get(url_for('updateRobot',robot_id=1))
        self.assertIn(b'Update Robot',response.data)

    def test_updatealgorithm_view(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addAlgorithm'),
            data=dict(
                algorithm_name='Testalgorithm',
                movement_type='Test motor'),
            follow_redirects=True)
        response = self.client.get(url_for('updateAlgorithm',algorithm_id=1))
        self.assertIn(b'Update Algorithm',response.data)

class TestLogin(TestBase):
    def test_login(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        response=self.client.get(url_for('home'))
        self.assertIn(b'Logout',response.data)

    def test_logout(self):
        self.client.get(url_for('logout'))
        response = self.client.get(url_for('home'))
        self.assertIn(b'login',response.data)

class TestRegistration(TestBase):
    def test_register_account(self):
        self.client.post(
            url_for('register'),
            data=dict(
                first_name='Sam',
                last_name='Asquith',
                email='test@test.com',
                password='test',
                confirm_password='test'),
            follow_redirects=True)
        response=self.client.get('login')
        self.assertIn(b'Login',response.data)

class TestAddition(TestBase):
    def test_add_robot(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addRobot'),
            data=dict(
                model_name='Testbot',
                drive_type='Test motor',
                height=42,
                width=42,
                length=42),
            follow_redirects=True)
        response=self.client.get(url_for('robot'))
        self.assertIn(b'Testbot',response.data)

    def test_add_algorithm(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addAlgorithm'),
            data=dict(
                algorithm_name='Testalgorithm',
                movement_type='Test motor'),
            follow_redirects=True)
        response=self.client.get(url_for('algorithm'))
        self.assertIn(b'Testalgorithm',response.data)


    def test_add_result(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addAlgorithm'),
            data=dict(
                algorithm_name='Testalgorithm',
                movement_type='Test motor'),
            follow_redirects=True)
        self.client.post(
            url_for('addRobot'),
            data=dict(
                model_name='Testbot',
                drive_type='Test motor',
                height=42,
                width=42,
                length=42),
            follow_redirects=True)
        self.client.post(
            url_for('addResult'),
            data=dict(
                robot_id=1,
                algorithm_id=1,
                time_taken=42),
            follow_redirects=True)
        response=self.client.get(url_for('result'))
        self.assertIn(b'Testbot',response.data)

class TestDeletion(TestBase):

    def test_delete_robot(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addRobot'),
            data=dict(
                model_name='Testbot',
                drive_type='Test motor',
                height=42,
                width=42,
                length=42),
            follow_redirects=True)
        self.client.get(url_for('deleteRobot',robot_id=1),
            follow_redirects=True)
        response = self.client.get(url_for('robot'))
        self.assertIn(b'No robots here',response.data)


    def test_delete_algorithm(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addAlgorithm'),
            data=dict(
                algorithm_name='Testalgorithm',
                movement_type='Test motor'),
            follow_redirects=True)
        self.client.get(url_for('deleteAlgorithm',algorithm_id=1),
            follow_redirects=True)
        response = self.client.get(url_for('algorithm'))
        self.assertIn(b'No algorithms here',response.data)


class TestUpdate(TestBase):

    def test_update_robot(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addRobot'),
            data=dict(
                model_name='Testbot',
                drive_type='Test motor',
                height=42,
                width=42,
                length=42),
            follow_redirects=True)
        self.client.post(url_for('updateRobot',robot_id=1),
            data=dict(
                model_name='Testbot1',
                drive_type='Test motor',
                height=42,
                width=42,
                length=42),
            follow_redirects=True)
        response = self.client.get(url_for('robot'))
        self.assertIn(b'Testbot1',response.data)

    def test_update_algorithm(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(
            url_for('addAlgorithm'),
            data=dict(
                algorithm_name='Testalgorithm',
                movement_type='Test motor'),
            follow_redirects=True)
        self.client.post(url_for('updateAlgorithm',algorithm_id=1),
            data=dict(
                algorithm_name='Testalgorithm1',
                movement_type='Test motor'),
            follow_redirects=True)
        response = self.client.get(url_for('algorithm'))
        self.assertIn(b'Testalgorithm1',response.data)



            
