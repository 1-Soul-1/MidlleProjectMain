from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100) # поле с ограничением по символам

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(Author,on_delete=models.CASCADE, related_name='books')

    