from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from auction.models import User


class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(max_length=255, help_text="Please enter your email address", required=True)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
       
    #email form validation 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            raise
        raise forms.ValidationError(f"Email {email} is already in use.")