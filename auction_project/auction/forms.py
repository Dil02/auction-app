from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from auction.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required", widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 
                                                                                                  'class': 'wide-input'}))
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter a username', 'class': 'wide-input'}))
    password1 = forms.CharField(label='Password1', max_length=100,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Enter a password', 'class': 'wide-input'}))
    password2 = forms.CharField(label='Password2', max_length=100,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password', 'class': 'wide-input'}))
    # dob = forms.DateField(input_formats='%Y-%m-%d',widget=forms.DateInput(attrs={'type': 'date','pattern':'[0-9]{4}-[0-9]{2}-[0-9]{2}'}))
    dob = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    ) 
    city=forms.CharField(label='city', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter a city', 'class': 'wide-input'}))
                               
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2","dob","city")
        
class AccountAuthenticationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email', 'password')
        
    def clean(self)->None:
        if self.is_valid():
            email1 = self.cleaned_data['email']
            password1 = self.cleaned_data['password']
            if not authenticate(email=email1, password=password1):
                raise forms.ValidationError("Invalid Login")
        
        