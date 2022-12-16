from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from auction.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required", widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter a username'}))
    password1 = forms.CharField(label='Password1', max_length=100,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Enter a password'}))
    password2 = forms.CharField(label='Password2', max_length=100,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
        
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
        
        