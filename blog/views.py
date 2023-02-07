from django.shortcuts import render
from django.views.generic import ListView, DetailView


# def home(request):
#     return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'
