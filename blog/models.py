"""Models for Blog application"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """Post Model

    Posts can be created by adding a title, an image (optional),
    description and category
    """

    title = models.CharField(max_length=255)
    featured_image = CloudinaryField('image', blank=True, null=True)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        """Adds a space between title and author in admin page"""
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        """Create reverse url for posts"""
        return reverse('post-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    """Creates profile for a new user"""

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    facebook_link = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)
    twitter_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


def create_profile(sender, instance, created, **kwargs):
    """Creates a profile id on user registration"""

    if created:
        profile_user = Profile(user=instance)
        profile_user.save()


"""Saves the changes to database"""
post_save.connect(create_profile, sender=User)


class Comment(models.Model):
    """Model for adding comments,
    the name field is the user username
    """

    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE
        )
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    def __str__(self):
        """Adds a dash between post title and username in admin panel"""

        return '%s - %s' % (self.post.title, self.name)
