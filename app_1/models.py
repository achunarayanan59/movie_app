from django.db import models

# Create your models here.
class movie_list(models.Model):
    title=models.TextField(max_length=250,null=False)
    year=models.IntegerField(null=False)
    desc=models.TextField(max_length=250,null=False)
