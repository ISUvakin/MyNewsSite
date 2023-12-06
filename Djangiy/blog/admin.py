from . import models
from django.contrib import admin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'publish', 'status', 'image',)
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)
