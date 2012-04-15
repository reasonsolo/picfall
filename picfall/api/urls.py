from django.conf.urls import patterns, include, url
from picfall.api.api import PictureResource, CategoryResource,\
                            UserResource, ProfileResource


picture_resource = PictureResource()
category_resource = CategoryResource()
user_resource = UserResource()
profile_resource = ProfileResource()

urlpatterns = patterns('',
        url(r'', include(picture_resource.urls)),
        url(r'', include(category_resource.urls)),
        url(r'', include(user_resource.urls)),
        url(r'', include(profile_resource.urls)),
)
