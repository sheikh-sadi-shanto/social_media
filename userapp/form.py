from django import forms
from django.contrib.auth.models import User

class Loginform(forms.Form):
    username=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Registerform(forms.Form):
    username=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    

# class Registerform(forms.ModelForm):
#     password1=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ('username','email','password','password1')


# class Registerform(forms.ModelForm):
#     password1=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ('username','email','password','password1')