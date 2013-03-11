from django.db import models

from users.models import User
from store.models import Store
from collection.models import Collection

class PeopleFollow(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    following = models.ForeignKey(User)

class StoreFollow(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    following = models.ForeignKey(Store)

class CollectionFollow(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    following = models.ForeignKey(Collection)

