from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    # En lugar de 'User', usamos settings.AUTH_USER_MODEL
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    theme = models.CharField(max_length=10, default='light')

    def __str__(self):
        return f"Perfil de {self.user}"