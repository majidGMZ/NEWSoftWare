from django.shortcuts import render
from account.forms import UserCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from pprint import pprint
from django.core.mail import EmailMessage
import smtplib
from account.models import Spaces
from account.models import SpaceRank
from account.models import Comments
from django.shortcuts import redirect
import random
from django.db.models import Sum
import string


class Auth:
    def singup(self):
        if self.method == 'POST':
            form = UserCreationForm(self.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')

                raw_password = form.cleaned_data.get('password')
                digits = "".join([random.choice(string.digits + string.ascii_letters) for i in range(10)])
                email = EmailMessage('Hello', 'http://localhost:8000/panel/verify?link=' + digits,
                                     to=['mahsamovaffag@gmail.com'])  # fill this param

                email.send()
                form.link = digits
                form.save()
                user = authenticate(username=username, password=raw_password)
                # login(self, user)
                # user.save()
                return HttpResponseRedirect('/accounts/login')
        else:
            form = UserCreationForm()

        return render(self, 'account/signup.html', {'form': form})

    def login(self):
        if self.method == 'POST':
            form = LoginForm(self.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(email=cd['user_email'],
                                    password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(self, user)

                        return HttpResponseRedirect('/index')

                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()

            return render(self, 'account/login.html', {'form': form})

    def logout(self):
        logout(self)
        return redirect('/accounts/login')
