from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
@admin.register(Category)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
