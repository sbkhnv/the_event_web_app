from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "placeholder": 'Username', 'required': True,
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "placeholder": 'Password', 'required': True,
    }))


class Registration(forms.ModelForm):
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'required': True,
               'placeholder': 'Confirm Password', 'name': "cpassword"}))

    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password")
        widgets = {
            'username': forms.TextInput(
                attrs={'required': True,
                       'placeholder': 'Username', 'name': "username"}),
            'email': forms.EmailInput(
                attrs={'required': True,
                        'placeholder': 'Email', 'name': "email"}),
            'password': forms.PasswordInput(
                attrs={'required': True,
                       'placeholder': 'Password', 'name': "password"}),
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil emas !")
        return self.cleaned_data['confirm_password']
