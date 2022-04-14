from django.contrib import admin
from .models import Post
# Register your models here.

# 만든 DB 가져와서 어드민 등록
admin.site.register(Post)