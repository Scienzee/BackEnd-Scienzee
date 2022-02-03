import email
from django.db import models

class Dev(models.Model):
    name = models.CharField("Name", max_length = 194, null=True, blank=True)
    email = models.EmailField("E-mail",max_length=194, unique=True)

    def __str__(self):
        return f'{self.name} -- {self.email}'
    
    class Meta:
        verbose_name = "Dev"
        verbose_name_plural="Devs"
        ordering = ['email']
        app_label = 'dev'
