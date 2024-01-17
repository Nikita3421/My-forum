from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'bio', 
                  'geolocation', 
                  'contacts', 
                  'photo')


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ("bio", "geolocation", "contacts")