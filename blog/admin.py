from django.contrib import admin
from .models import Post, Comment
#added comment so I can recommit

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)