"""Admin for blog application"""

from django.contrib import admin
from .models import Post, Category, Profile, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
@admin.register(Category)
@admin.register(Profile)
@admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):
    """Summernote imported for future use"""

    """Blog Models are added to admin panel"""

    summernote_fields = ('content',)
