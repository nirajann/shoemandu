from django import forms
from django.contrib.auth import get_user_model
from django.db.models import fields
from .models import *



class customer(forms.ModelForm):
    class Meta:
        model = signupascustomer
        fields = ("__all__")
