from django.contrib import admin
from .models import Contact, Category, HappyClients, Post, Tag, Team


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')
    filter_horizontal = ('tags',)
    search_fields = ('title', 'category')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_viewed')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email', 'phone',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(HappyClients)
admin.site.register(Tag)
admin.site.register(Team)
admin.site.register(Contact, ContactAdmin)
