from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Library,on_delete=models.CASCADE,related_name='books')

    