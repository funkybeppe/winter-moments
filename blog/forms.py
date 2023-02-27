"""Forms for blog application"""

from django import forms
from .models import Post, Category, Comment
from ckeditor.widgets import CKEditorWidget

"""Creates a category list with categories names for form choices"""
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    """Post form for post creation"""

    class Meta:
        model = Post
        fields = (
            'title',
            'title_tag',
            'author',
            'category',
            'featured_image',
            'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '',
                    'id': 'username-field',
                    'type': 'hidden'}),
            'category': forms.Select(
                choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    """EditForm for post editing"""

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """Comment Form for adding new comments to posts"""

    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
