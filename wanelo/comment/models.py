from django.db import models
from users.models import User
from product.models import Product

class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    text = models.TextField(default=u'')