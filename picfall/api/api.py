# from django.utils.translation import ugettext as _
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from picfall.fall.models import Picture, Category
from picfall.account.models import UserProfile
from picfall.interact.models import Comment


class PictureResource(ModelResource):
    class Meta:
        queryset = Picture.objects.all()
        resource_name = 'picture'
        exclude = []

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class ProfileResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'profile'

class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
