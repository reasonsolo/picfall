from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
import uuid
import os


class OrderedPicture(models.Manager):
    # TODO
    """
    Model Picture's customised manager, define your own ordering function here.
    """
    def get_query_set(self):
        return super(OrderedPicture, self).get_query_set()

class Picture(models.Model):
    name = models.CharField('Pic Name', max_length = 255, default = 'unamed')
    externid = models.IntegerField('External ID', null = True, blank = True)
    externurl = models.CharField('External URL', max_length = 255,
            null = True, blank = True)
    category = models.ForeignKey('Category', verbose_name = 'Category')
    def get_image_path(instance, filename):
        # FIXME
        """
        define your own file-renaming function here
        """
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid1(), ext)
        return os.path.join(settings.IMAGE_DIR, filename)
    image = models.ImageField('Image', upload_to = get_image_path)
    description = models.TextField('Description', null = True, blank = True)

    uploader = models.ForeignKey(User, verbose_name = 'Uploader',
            related_name = 'uploader')
    uploadtime = models.DateTimeField('Upload at', default = datetime.now())
    modifier = models.ForeignKey(User, verbose_name = 'Modifier',
            related_name = 'modifier', null = True, blank = True)
    modifiedtime = models.DateTimeField('Last Modified at',
            null = True, blank = True)

    liked = models.IntegerField('Liked', default = 0)
    hated = models.IntegerField('Hated', default = 0)
    repinned = models.IntegerField('Liked', default = 0)
    # FIXME: enable this once you have completed your ordering manager
    # objects = OrderedPicture()
    def __unicode__(self):
        return self.name

    """
    class Meta:
        ordering = ('liked', 'repeinned')
    """

class Category(models.Model):
    name = models.CharField('Category Name', max_length = 255,
            default = 'unamed')
    externid = models.IntegerField('External ID', null = True, blank = True)
    externurl = models.CharField('External URL', max_length = 255,
            null = True, blank = True)
    parent = models.ForeignKey('Category', verbose_name = 'Parent Category',
            null = True, blank = True)
    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Tag Name', max_length = 255)
    user = models.ForeignKey(User, verbose_name = 'Added by')
    freq = models.IntegerField('Frequency', default = 0)
    time = models.DateTimeField('Added Time', default = datetime.now())
    def __unicode__(self):
        return self.name


