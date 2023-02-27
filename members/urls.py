"""URLs for registration and profile editing"""

from django.urls import path, include
from . import views
from .views import (
    UserRegisterView,
    UserEditView,
    PasswordsChangeView,
    ProfilePageView,
    EditProfilePageView,
    CreateProfilePageView,
    LoginView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create_profile'),
]
