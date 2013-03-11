from django.db import models
from users.models import User
from product.models import Product
from comment.models import Comment

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

class ProductTag(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    tag = models.ForeignKey(Tag)
    from_comment = models.ForeignKey(Comment)

class ProductMention(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='related_productmention_user')
    product = models.ForeignKey(Product)
    mention = models.ForeignKey(User, related_name='related_productmention_mention')
    from_comment = models.ForeignKey(Comment)
