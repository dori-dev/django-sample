from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AccountTest(TestCase):
    def _status_code(self, url: str) -> int:
        response = self.client.get(url)
        return response.status_code

    # test pages url name content
    def test_register_url_name_content(self):
        self.assertEqual(reverse('accounts:register'), '/accounts/register/')

    def test_login_url_name_content(self):
        self.assertEqual(reverse('accounts:login'), '/accounts/login/')

    def test_logout_url_name_content(self):
        self.assertEqual(reverse('accounts:logout'), '/accounts/logout/')

    # test pages status code
    def test_register_page_status_code(self):
        self.assertEqual(self._status_code(reverse('accounts:register')), 200)

    def test_login_page_status_code(self):
        self.assertEqual(self._status_code(reverse('accounts:login')), 200)

    def test_logout_page_status_code(self):
        self.assertEqual(self._status_code(reverse('accounts:logout')), 302)

    # test pages template
    def test_register_page_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('accounts:register')),
            "accounts/register.html")

    def test_login_page_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('accounts:login')),
            "accounts/login.html")

    # test forms
    def test_register_form(self):
        self.client.post(
            reverse('accounts:register'),
            {
                'first_name': 'mohammad',
                'last_name': 'dori',
                'username': 'dori.dev',
                'email': 'mr.dori.dev@gmail.com',
                'password': '1234',
            })
        user: User = User.objects.first()
        self.assertEqual(user.username, 'dori.dev')
        self.assertEqual(user.first_name, 'mohammad')
        self.assertEqual(user.last_name, 'dori')
        self.assertEqual(user.email, 'mr.dori.dev@gmail.com')
