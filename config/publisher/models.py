from django.db import models

class Publisher(models.Model):
    name = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    