from django.db import models
from users.models import User

class Collection(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40)
