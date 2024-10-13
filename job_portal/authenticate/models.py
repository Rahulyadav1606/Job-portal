from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class sign_up(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)