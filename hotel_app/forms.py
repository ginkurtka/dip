from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

Guest = get_user_model()

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Guest
        fields = ("name", "age", "phone", "email")

'''
from django import forms
from .models import Guest

class Guest(models.Model):
    name = forms.CharField(max_length=20, required= True)
    age = forms.IntegerField(default=20, required= True)
    phone = forms.CharField(max_length=20, required= True)
    email = forms.EmailField()
    
class Meta:
    model = Guest
'''