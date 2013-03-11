from django.db import models
from users.models import User

class Store(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=40)
    url = models.URLField(blank=True, null=True)

