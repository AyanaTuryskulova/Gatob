from django.contrib import admin
from .models import Category, Photo, Comment, News

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(News)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'description', 'likes', 'pdf']  
    list_filter = ['category']
    search_fields = ['title', 'description']
