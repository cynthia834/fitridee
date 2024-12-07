# bike_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Bicycle, CustomUser


class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields = ['serial_number', 'color', 'image', 'timer', 'amount','time_taken','station','owner']
class CustomUserCreationForm(UserCreationForm):
    fullname = forms.CharField(max_length=100)
    id_no = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    class Meta:
        model = CustomUser
        fields = ['username', 'fullname', 'id_no', 'phone_number', 'password1', 'password2']