from django.urls import path, include
from .views import Home, PostDetailView, AddPostView, UpdatePostView
# from . import views


urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name='home'),
    path('summernote/', include('django_summernote.urls')),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
]
