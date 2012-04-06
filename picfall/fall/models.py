from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from datetime import datetime
import uuid
import os

class Pictrue(models.Model):
    name = models.CharField('Pic Name', max_length = 255, default = 'unamed')
    externid = models.IntegerField('External ID', null = True, blank = True)
    category = models.ForeignKey('Category', verbose_name = 'Category')
    def get_image_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid1(), ext)
        return os.path.join(settings.IMAGE_DIR, filename)
    image = models.ImageField('Image', upload_to = get_image_path)
    description = models.TextField('Description')

    uploader = models.ForeignKey(User, verbose_name = 'Uploader',
            related_name = 'uploader')
    uploadtime = models.DateTimeField('Upload at', default = datetime.now())
    modifier = models.ForeignKey(User, verbose_name = 'Modifier',
            related_name = 'modifier')
    modifiedtime = models.DateTimeField('Last Modified at',
            null = True, blank = True)




class Category(models.Model):
    name = models.CharField('Category Name', max_length = 255,
            default = 'unamed')
    externid = models.IntegerField('External ID', null = True, blank = True)
    parent = models.ForeignKey('Category', verbose_name = 'Parent Category')




