from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class MyUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)
    phone = forms.CharField(max_length=20, required=True)
    address = forms.CharField(max_length=255, required=True)
    zipcode = forms.CharField(max_length=255, required=True)
    place = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username',  'email', 'phone', 'first_name', 'last_name', 'password1', 'password2', 'address', 'zipcode', 'place']

class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',  'email', 'phone', 'first_name', 'last_name', 'address', 'zipcode', 'place')



class ProfileForm(forms.ModelForm):
    
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)
    phone = forms.CharField(max_length=20, required=True)
    address = forms.CharField(max_length=255, required=True)
    zipcode = forms.CharField(max_length=255, required=True)
    place = forms.CharField(max_length=255, required=True)
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'zipcode', 'place', 'image')
        exclude = ['user']


