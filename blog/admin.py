from django.contrib import admin
from .models import Post

# add post to our admin site page
admin.site.register(Post)