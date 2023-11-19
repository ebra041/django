from django.forms import ModelForm
from django import forms
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['fname', 'sname', 'password']
        widgets = {
            'password':forms.PasswordInput(),
        }