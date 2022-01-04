from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=100000)
    date = models.DateField()
