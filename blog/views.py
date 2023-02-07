from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

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
    template_name = 'add_post.html'
    fields = '__all__'
