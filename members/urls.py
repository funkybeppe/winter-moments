from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
]
