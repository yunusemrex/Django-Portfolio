from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on','categories',)
    list_filter = ("status",'categories',)
    search_fields = ['title', 'content','summaries',]
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)


