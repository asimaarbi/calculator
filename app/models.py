from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True, default='')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class History(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=30)
