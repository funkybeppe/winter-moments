from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm

# def home(request):
#     return render(request, 'home.html', {})


class Home(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
