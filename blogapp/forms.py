from dataclasses import fields
from django.db import models
from django import forms
from blogapp.models import BlogPost,BlogAppUser



class PostCreateForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=('post_title','post_description','slug','post_status','post_image')        


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=BlogAppUser
        fields=('first_name','middle_name','last_name','email','contact','password','profile')

class UserLoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=BlogAppUser
        fields=('email', 'password')

