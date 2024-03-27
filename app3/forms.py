# from django.forms import ModelForm
# from .models import Employee
# from django import forms

# class EmployeeForm(ModelForm):
#     class Meta:
#         model=Employee
#         fields='__all__'

#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.TextInput(attrs={'class':'form-control'}),
#             'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True)
#         }

# from dataclasses import fields
# from pyexpat import model
# from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import Employee
class EmployeeForm(ModelForm):
    user_name=forms.CharField(required=False,label="Name")
    user_email=forms.EmailField(label="Email")
    user_phone=forms.IntegerField(label="Phone No")