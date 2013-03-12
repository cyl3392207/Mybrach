#coding=utf-8

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username:
            raise ValueError(u'用户名为空')

        if not email:
            raise ValueError(u'邮箱为空')

        if not password:
            raise ValueError(u'密码为空')

        user = self.model(username=username, email=UserManager.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.activated = True
        user.save()
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=40, verbose_name=u'用户名', unique=True, db_index=True)
    email = models.CharField(max_length=40, verbose_name=u'邮箱', unique=True, db_index=True)
    activated = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __unicode__(self):
        return '%s[%s]' % (self.username, self.email)

    def get_full_name(self):
        return self.__unicode__()

    def get_short_name(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(blank=True, null=True, upload_to='profile_image')
    full_name = models.CharField(max_length=40, default=u'')
    location = models.CharField(max_length=140, default=u'')
    website = models.URLField(blank=True, null=True)
    description = models.TextField(default=u'')

    def __unicode__(self):
        return '%s' % self.full_name

from django.dispatch import receiver
from django.db.models.signals import post_save
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    instance = kwargs['instance']
    created = kwargs['created']
    if created:
        Profile.objects.create(user=instance)
