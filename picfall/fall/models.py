from django.utils.translation import ugettext as _
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
    name = models.CharField(_('Pic Name'), max_length = 255, default = 'unamed')
    externid = models.IntegerField(_('External ID'), null = True, blank = True)
    externurl = models.CharField(_('External URL'), max_length = 255,
            null = True, blank = True)
    category = models.ForeignKey('Category', verbose_name = _('Category'))
    def get_image_path(instance, filename):
        # FIXME
        """
        define a proper file-renaming function here
        """
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(settings.IMAGE_DIR, filename)
    def get_image(self):
        return self.image.url
    def get_thumbnail_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(settings.THUMBNAIL_DIR, filename)
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return ""
    thumbnail = models.ImageField(_('thumbnail'), null = True, blank = True,
            upload_to = get_thumbnail_path)
    image = models.ImageField(_('Image'), upload_to = get_image_path)
    description = models.TextField(_('Description'), null = True, blank = True)

    uploader = models.ForeignKey(User, verbose_name = _('Uploader'),
            related_name = 'uploader')
    uploadtime = models.DateTimeField(_('Upload at'), default = datetime.now())
    modifier = models.ForeignKey(User, verbose_name = _('Modifier'),
            related_name = 'modifier', null = True, blank = True)
    modifiedtime = models.DateTimeField(_('Last Modified at'),
            null = True, blank = True)

    header = models.BooleanField(_('Pinned on header'), default = False)
    clicked = models.IntegerField(_('Clicked'), default = 0)
    liked = models.IntegerField(_('Liked'), default = 0)
    hated = models.IntegerField(_('Hated'), default = 0)
    commented = models.IntegerField(_('Commented'), default = 0)
    repinned = models.IntegerField(_('Liked'), default = 0)
    # FIXME: enable this once you have completed your ordering manager
    # objects = OrderedPicture()
    def __unicode__(self):
        return self.name

    def create_thumbnail(self):
        # original code for this method came from
        # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

        # If there is no image associated with this.
        # do not create thumbnail
        if not self.image:
            return
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os

        DJANGO_TYPE = self.image.file.content_type

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
        image = Image.open(StringIO(self.image.read()))

        #if image.mode not in ('L', 'RGB'):
        #    image = image.convert('RGB')

        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image.thumbnail(settings.THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

    def save(self):
        # create a thumbnail
        self.create_thumbnail()
        super(Picture, self).save()


    """
    class Meta:
        ordering = ('liked', 'repeinned')
    """

class Category(models.Model):
    name = models.CharField(_('Category Name'), max_length = 255,
            default = 'unamed')
    externid = models.IntegerField(_('External ID'), null = True, blank = True)
    externurl = models.CharField(_('External URL'), max_length = 255,
            null = True, blank = True)
    parent = models.ForeignKey('Category', verbose_name = _('Parent Category'),
            null = True, blank = True)
    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(_('Tag Name'), max_length = 255)
    user = models.ForeignKey(User, verbose_name = _('Added by'))
    freq = models.IntegerField(_('Frequency'), default = 0)
    time = models.DateTimeField(_('Added Time'), default = datetime.now())
    def __unicode__(self):
        return self.name


