from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name = 'User')
    nick = models.CharField('Nick', max_length = 255, null = True, blank = True)
    # TODO
    # some other fields


