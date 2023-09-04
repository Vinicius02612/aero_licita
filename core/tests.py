# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse

# from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
from django.test import TestCase


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.login_url = reverse("core:login")
        self.homepage_url = reverse("core:homepage")
        self.adminpage_url = reverse("core:adminpage")
        self.signin_url = reverse("core:signin")
        self.user_data = {
            "username": "test",
            "password": "123mud@R",
        }
        # Cria um usuário válido para testar o login
        self.user = User.objects.create_user(
            username=self.user_data["username"],
            password=self.user_data["password"],
        )

    def test_valid_login_adminpage(self):
        # Define o usuário como staff (admin)
        self.user.is_staff = True
        self.user.save()

        # Cria uma requisição POST com os dados de login válidos
        response = self.client.post(self.login_url, data=self.user_data)

        # Verifica se a resposta redireciona para a página correta
        self.assertRedirects(response, self.adminpage_url)

        # Verifica se o usuário está logado corretamente
        self.assertTrue("_auth_user_id" in self.client.session)

    def test_valid_login_homepage(self):
        # Cria uma requisição POST com os dados de login válidos
        response = self.client.post(self.login_url, data=self.user_data)

        # Verifica se a resposta redireciona para a página correta
        self.assertRedirects(response, self.homepage_url)

        # Verifica se o usuário está logado corretamente
        self.assertTrue("_auth_user_id" in self.client.session)

    def test_invalid_login(self):
        # Simula dados de login inválidos (senha incorreta)
        invalid_data = self.user_data.copy()
        invalid_data["password"] = "wrong_password"

        # Cria uma requisição POST com dados de login inválidos
        response = self.client.post(self.login_url, data=invalid_data)

        # Verifica se a resposta redireciona para a página correta
        self.assertRedirects(response, self.signin_url)

        # Verifica se a mensagem de erro está na sessão de mensagens
        messages = [str(msg) for msg in get_messages(response.wsgi_request)]
        self.assertIn("Invalid username or password", messages)
