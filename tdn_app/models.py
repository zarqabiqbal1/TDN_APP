from django.db import models


class UserModel(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateField(blank=False)

