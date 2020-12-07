from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(ModelForm):
    
	class Meta:
		model = User
		fields = ['username', 'password','email', 'first_name', 'last_name']

class ProfileForm(ModelForm):
    #This form is not working, is a separate form necessary?
	class Meta:
		model = UserProfile
		fields = ['city', 'phone_num']