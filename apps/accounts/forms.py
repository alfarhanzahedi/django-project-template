from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from .models import User

# Forms for the new User model.
# Refer to: https://wsvincent.com/django-custom-user-model-tutorial/.

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email',)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            if User.objects.get(email = email).email == email:
                return email
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            if User.objects.get(email = email).email == email:
                return email
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')