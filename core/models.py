from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(User):
    ...


class ClientQuestion(models.Model):
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_email
