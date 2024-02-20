from django.contrib import admin

# Register your models here.
from .models import Actualite, Post
from django_summernote.admin import SummernoteModelAdmin

#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'image', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    summernote_fields = ('body',)

admin.site.register(Post, PostAdmin)

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')