from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re

class SignUpForm(UserCreationForm):
    
    username = forms.CharField(
        max_length=10,
        label="Phone number",
    )

    password1 = forms.CharField(
        max_length=10,
        widget = forms.PasswordInput,
        help_text = "Your password shoud be at least 8 characters.",
    )

    password2 = forms.CharField(
        max_length=10,
        widget = forms.PasswordInput,
        help_text = "Confirm Password",
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


    def is_ten_digit_number(self, string):
        pattern = r'^\d{10}$'
    
        match = re.match(pattern, string)
    
        return match is not None

    def clean_username(self):
        data = self.cleaned_data["username"]
        if not self.is_ten_digit_number(data):
            raise ValidationError("Enter a valid phone number!")
        return data

    """def clean_password1(self):
        data = self.cleaned_data["password1"]
        if len(data) < 8:
            raise ValidationError("Password should be at least 8 characters")
        return data

    def clean_password2(self):
        p1 = self.cleaned_data["password2"]
        p2 = self.cleaned_data["password1"]

        if p1 != p2:
            raise ValidationError("Passwords do not match!")

        return p1"""
