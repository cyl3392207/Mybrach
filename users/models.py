from django.db import models

class User(models.Model):
    email = models.CharField(max_length=40, unique=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)

    def __unicode__(self):
        return '%s[%s]' % (self.username, self.email)

class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile_image')
    full_name = models.CharField(max_length=40, default=u'')
    location = models.CharField(max_length=140, default=u'')
    website = models.URLField(blank=True, null=True)
    description = models.TextField(default=u'')

    def __unicode__(self):
        return '%s' % self.full_name