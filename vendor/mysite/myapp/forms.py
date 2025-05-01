from django import forms
from .models import Product
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','description','price','file']

class UserRegistrationForm(forms.ModelForm):
    password1=forms.CharField(label="Password",max_length=100,widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password" ,max_length=100,widget=forms.PasswordInput)

    class Meta:
        
        model=User 
        fields=['username','email','first_name','last_name']
    def check_password(self):
        if self.cleaned_data['password1']!=self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords fields do not match')
        return self.cleaned_data['password2']