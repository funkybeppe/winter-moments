"""Views for blog application"""

from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )


class Home(LoginRequiredMixin, ListView):
    """ListView to display a list of posts"""

    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']

    def get_context_data(self, *args, **kwargs):
        """Gets the categories and returns a category menu using their id's"""

        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    """DetailView to see the post in details"""

    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        """Gets the post and returns a category list using their id's"""

        """The post will be included in the category
        the author selected during post creation"""

        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        post = get_object_or_404(Post, id=self.kwargs['pk'])

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    """CreateView to create new posts using PostForm"""

    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        """Success message after post creation"""

        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS, "Post created successfully"
        )
        return response


class AddCommentView(LoginRequiredMixin, CreateView):
    """CreateView to create new comments on posts using CommentForm"""

    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        """Success message after comment submission"""

        form.instance.post_id = self.kwargs['pk']
        messages.add_message(
            self.request, messages.SUCCESS, "Comment added successfully"
        )
        return super().form_valid(form)

    def get_success_url(self):
        """Redirects to the commented post by taking the post primary key"""

        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class AddCategoryView(LoginRequiredMixin, CreateView):
    """CreateView to create new categories for posts"""

    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    """UpdateView to edit a post"""

    model = Post
    template_name = 'update_post.html'
    form_class = EditForm

    def form_valid(self, form):
        """Success message when post is updated"""

        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS, "Post updated successfully"
        )
        return response


class DeletePostView(LoginRequiredMixin, DeleteView):
    """DeleteView for post deletion"""

    """Redirects to home page"""

    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def CategoryListView(request):
    """Gets all the categories added and returns a list"""

    cat_menu_list = Category.objects.all()
    return render(
        request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    """For good practice every category has a dash,
    when rendered the dash is removed"""

    ordering = ['-created_on']
    category_posts = Post.objects.filter(
        category=cats.replace('-', ' '))
    return render(
        request, 'categories.html', {
            'cats': cats.title().replace('-', ' '),
            'category_posts': category_posts
            }
        )


def LikeView(request, pk):
    """Gets the post id, when user likes a post sends
    a request and adds the like"""

    """When the user clicks the like button again the like is removed"""

    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def index(request):
    """Renders index page"""

    return render(request, 'index.html')
