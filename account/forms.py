from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from account.models import Account, ProfileImg


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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileImg
        fields = ['avatar']


# class UpdateProfile(forms.ModelForm):
#     # username = forms.CharField(required=True)
#     # email = forms.EmailField(required=True)
#     # wigu = forms.CharField(required=True)
#     # education = forms.CharField(required=True)
#     # language = forms.CharField(required=True)
#     # about = forms.CharField(required=True)
#     # interest = forms.CharField(required=True)
#     # civ = forms.CharField(required=True)
#     # cil = forms.CharField(required=True)
#
#     class Meta:
#         model = Account
#         fields = ('wigu', 'education', 'language', 'about', 'interest', 'cil', 'civ', 'availability')
#
#     # def clean_email(self):
#     #     username = self.cleaned_data.get('username')
#     #     email = self.cleaned_data.get('email')
#     #
#     #     if email and User.objects.filter(email=email).exclude(username=username).count():
#     #         raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
#     #     return email
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.wigu = self.cleaned_data['wigu']
#         print("hello", user.wigu)
#
#         if commit:
#             user.save()
#
#         return user

