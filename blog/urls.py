"""URL's for blog application"""

from django.urls import path, include
from . import views
from .views import (
    index,
    Home,
    PostDetailView,
    AddPostView, UpdatePostView,
    DeletePostView, AddCategoryView,
    CategoryView, CategoryListView,
    LikeView,
    AddCommentView)


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', Home.as_view(), name='home'),
    path('summernote/', include('django_summernote.urls')),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path(
        'post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'
        ),
]
