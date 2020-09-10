from django import forms
from django.contrib.auth.models import User
from calo.models import UserProfile, Food_qty, Activity
from django.forms.widgets import RadioSelect

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    TYPE_SELECT = (('female', 'Female'), ('male', 'male'),)
    gender = forms.CharField(widget=forms.RadioSelect(choices=TYPE_SELECT))

    class Meta:
        model = UserProfile
        fields = ('Height', 'Weight', 'gender')

class Food_qtyForm(forms.ModelForm):
    food_consume = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your meal details (e.g. 1 apple)'
        }
    ))
    date_added = forms.CharField(widget=forms.DateTimeInput(
        attrs={
        'class':'form-control',
        'type':'datetime-local'
        }
    ))
    class Meta:
        model = Food_qty
        fields = ('food_consume','date_added')


class ActivityForm(forms.ModelForm):
    exercise = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'exercise'
        }
    ))
    date_added = forms.CharField(widget=forms.DateTimeInput(
        attrs={
        'class':'form-control',
        'type':'datetime-local'
        }
    ))
    class Meta:
        model = Activity
        fields = ('exercise','date_added')

