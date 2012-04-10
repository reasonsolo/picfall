from django.contrib import admin
from picfall.fall.models import Picture, Category

class PictureAdmin(admin.ModelAdmin):
    model = Picture
admin.site.register(Picture, PictureAdmin)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
admin.site.register(Category, CategoryAdmin)
