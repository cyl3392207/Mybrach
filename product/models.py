from django.db import models

from users.models import User
from store.models import Store
from collection.models import Collection

class Product(models.Model):
    time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    url = models.URLField(unique=True)
    image = models.ImageField()

    price = models.CharField(max_length=40, blank=True, null=True)
    buy_link = models.URLField(blank=True, null=True)
    store = models.ForeignKey(Store, blank=True, null=True)

class Save(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    collection = models.ForeignKey(Collection)
    product = models.ForeignKey(Product)




