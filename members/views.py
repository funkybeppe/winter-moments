"""Views for members application"""

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView, FormView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy
from blog.models import Profile
from .forms import (
    SignUpForm,
    EditProfileForm,
    PasswordChangingForm,
    ProfilePageForm,
)
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
    AuthenticationForm,
)


class LoginView(FormView):
    """FormView for login page, handles user authentication"""

    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_messages(
            self.request, messages.SUCCESS, "Login successfully"
            )
        return response

    def form_invalid(self, form):

        response = super().form_invalid(form)
        messages.add_message(
            self.request, messages.ERROR, "Username or Password invalid. Please try again."
        )
        return response


class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    """PasswordChangeView for password change page"""

    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    """Renders success page"""
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    """CreateView for new user creation"""

    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Success message when form is submitted correctly"""

        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS, "User created successfully"
        )
        return response

    def form_invalid(self, form):
        """Error message when form is submitted incorrectly"""

        response = super().form_invalid(form)
        messages.add_message(
            self.request, messages.ERROR, "Username or Password invalid. Please try again."
        )
        return response


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    """UpdateView for user details editing"""

    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        """Gets the current user"""
        return self.request.user

    def form_valid(self, form):
        """Success message when form is submitted correctly"""
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS, "Settings updated successfully"
            )
        return response


class ProfilePageView(LoginRequiredMixin, DetailView):
    """DetailView to display user profile details in profile page"""

    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        """Gets the username, user id and profile id and returns
        the profile page associated to the user"""

        context = super(ProfilePageView, self).get_context_data(
            *args, **kwargs
            )
        profile_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['profile_user'] = profile_user
        return context


class EditProfilePageView(LoginRequiredMixin, generic.UpdateView):
    """UpdateView for user details editing"""

    """User will be redirected to home page after editing"""

    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Success message when form is submitted correctly"""
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS, "Profile details updated successfully"
        )
        return response


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_profile.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def error_404(request, exception):
    """Page not found error"""
    return render(request, '404.html')


def error_500(request, exception):
    """Internal server error"""
    return render(request, '500.html')


def error_403(request, exception):
    """Forbidden error"""
    return render(request, '403.html')
