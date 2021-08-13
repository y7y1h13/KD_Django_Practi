from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created', 'updated']
    list_filter = ['author', 'created', 'updated']


admin.site.register(Post, PostAdmin)
