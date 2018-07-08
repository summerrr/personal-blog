from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag
#让后台显示的更加详细
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)