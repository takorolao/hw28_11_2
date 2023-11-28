from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class SignedDataObject(models.Model):
    data = models.TextField()
    signature = models.TextField()

    def __str__(self):
        return f"Signed Data: {self.data}"
