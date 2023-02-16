from django.contrib import admin
from .models import Post, Category, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
@admin.register(Category)
@admin.register(Profile)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
