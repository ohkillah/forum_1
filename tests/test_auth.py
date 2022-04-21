from django.http import HttpResponseRedirect  # type: ignore
from django.test import TestCase, Client  # type: ignore

from django.contrib.auth import get_user_model

User = get_user_model()


class TestAuth(TestCase):
    def setUp(self):
        self.user = User(username='forumchanin', email='forum@baki.kz')
        self.admin = User(username='admin', email='admin@baki.kz')
        self.admin.is_staff = True
        self.admin.is_superuser = True
        self.password = 'my_admin'
        self.admin.set_password(self.password)

        self.user.save()
        self.admin.save()

    def test_users_exist(self):
        all_users = User.objects.all()
        users_count = all_users.count()

        self.assertEqual(users_count, 2)

    def test_password(self):
        self.assertTrue(self.admin.check_password(self.password))

    def test_register(self):
        client = Client()
        response = client.post('/register/', {
            'username': 'twentyonepilots',
            'password1': 'rewq4321',
            'password2': 'rewq4321',
            'first_name': 'Tyler',
            'last_name': 'Joseph',
            'email': 'some_test@example.com'
        })
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        client = Client()
        response = client.post('/register/', {
            'username': 'twentyonepilots',
            'password1': 'rewq4321',
            'password2': 'rewq4321',
            'first_name': 'Tyler',
            'last_name': 'Joseph',
            'email': 'some_test@example.com'
        })

        response = client.post('/login/', {
            'email': 'some_test@example.com',
            'password': 'rewq4321'})
        self.assertEqual(response.status_code, 302)
