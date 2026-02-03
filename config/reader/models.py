from django.db import models
from django.contrib.auth.models import User

class Reader(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    membership_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    
