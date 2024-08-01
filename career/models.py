from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pswd = models.CharField(max_length=100)
    # gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name