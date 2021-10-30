from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    # address = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 20}))
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    # phone_number = forms.IntegerField()
    # dp = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
