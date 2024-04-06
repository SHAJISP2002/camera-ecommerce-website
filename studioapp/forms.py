from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import Order
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your conform password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['First_name','last_name','email','phone_number','address']
        
        
class Order(forms.Form):
    item_name = forms.CharField(label='Item Name', max_length=100)
    quantity = forms.IntegerField(label='Quantity')
    delivery_address = forms.CharField(label='Delivery Address', max_length=200)