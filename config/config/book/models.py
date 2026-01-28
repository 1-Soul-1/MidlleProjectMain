from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)
    count_book =models.PositiveIntegerField

    def __str__(self):
        return.self.name


    