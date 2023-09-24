from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={"class": "password", "placeholder": "create password", "class": "form-control"}), label="Password")
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={"class": "password", "placeholder": "confirm password", "class": "form-control"}), label="Confirm password")

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", 
                            "placeholder": "your username",
                            'hx-post': reverse_lazy("username-validation"),
                            'hx-target': '#usernameError',
                            'hx-trigger': 'keyup[target.value.length > 3]',
                          }),
            "email": forms.TextInput(attrs={"class": "form-control", 
                            "placeholder": "your email",
                            'hx-post': reverse_lazy('email-validation'),
                            'hx-target': '#emailError',
                            'hx-trigger': 'keyup[target.value.length > 3]'
                            }),
        }


class LoginForm(forms.Form):
    username = forms.EmailField(label="E-mail", label_suffix="",
                                widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", label_suffix="",
                               widget=forms.PasswordInput(attrs={"placeholder": "********", "class": "form-control"}))
