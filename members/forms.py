from django.contrib.auth.models import User
from django import forms
from blog.models import Profile
from django.contrib.auth.forms import (
                                        UserCreationForm,
                                        UserChangeForm,
                                        PasswordChangeForm
                                    )


class PasswordChangingForm(PasswordChangeForm):
    """Password change form for users.

    Provides old, new password and password confirmation.
    Attributes are added for bootstrap style classes
    """

    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(
        max_length=50, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'})
        )
    new_password2 = forms.CharField(
        max_length=50, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'})
        )

    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password1',
            'new_password2',
        )


class EditProfileForm(UserChangeForm):
    """Edit Profile Settings form.

    Form inherits from the User model.
    """

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    username = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )


class SignUpForm(UserCreationForm):
    """Sign Up form.

    This form will create the user profile, inheriting from User model.
    """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ProfilePageForm(forms.ModelForm):
    """Edit Profile Page form.

    This form inherits from Profile Model Form.
    """
    class Meta:
        model = Profile
        fields = (
            'bio',
            'profile_picture',
            'facebook_link',
            'instagram_link',
            'twitter_link'
            )

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook_link': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.TextInput(attrs={'class': 'form-control'}),
        }
