from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ("email", "username", "password1", "password2", 'birthday')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    user_email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('email', 'password')
