from django import forms
from django.contrib.auth.models import User
from calo.models import UserProfile
from django.forms.widgets import RadioSelect

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    TYPE_SELECT = (('female', 'Female'), ('male', 'male'),)
    gender= forms.CharField(widget=forms.RadioSelect(choices=TYPE_SELECT))

    class Meta:
        model = UserProfile
        fields = ('Height', 'Weight', 'gender')