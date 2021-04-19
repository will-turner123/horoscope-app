from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .get_sign import return_sign

# class DateInput():
#     birthday = forms.DateInput(widgets=DateInput)
#     fields = ['birthday']



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # birthday = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserBirthdayForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ['birthday']
