from django.contrib import admin
from blog.models import BlogPost, BlogComment

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    fields = ['text', 'post_title']
    list_display = ('post_title', 'pub_date')

class BlogCommentAdmin(admin.ModelAdmin):
    fields = ['blogpost', 'comment_title', 'text']
    list_display = ('comment_title', 'pub_date')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)