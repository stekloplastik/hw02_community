from django.contrib import admin

# Register your models here.
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text','pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug')
    search_fields = ('title', 'description')
    list_filter = ('slug',)
    empty_value_display = '-пусто-'   


admin.site.register(Post, PostAdmin) 
admin.site.register(Group, GroupAdmin)  
  