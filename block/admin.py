from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('author',)


admin.site.register(Post, PostAdmin)
