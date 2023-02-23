from dataclasses import fields
from django import forms
from .models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'bio')
        
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')