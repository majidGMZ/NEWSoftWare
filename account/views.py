from django.shortcuts import render
from account.forms import UserCreationForm, LoginForm
from django.contrib.auth import login, authenticate
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


# class Site:
#     def SpacesList(self):
#         spaces = Spaces.objects.all()
#         return render(self, 'Spaces.html', {'spaces': spaces})
#
#     def Space(self):
#         space = Spaces.objects.filter(id=self.GET['id'])
#         comments = Comments.objects.filter(space_id=self.GET['id'])
#         rank = SpaceRank.objects.filter(space_id=self.GET['id']).aggregate(Sum('rank'))
#         mrank = rank['rank__sum']
#         if mrank is None:
#             mrank = 0
#         return render(self, 'SingleSpace.html', {'space': space[0], 'comments': comments, 'rank': mrank})


class Auth:
    def singup(self):
        if self.method == 'POST':
            form = UserCreationForm(self.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                #login(self, user)
                digits = "".join([random.choice(string.digits + string.letters) for i in range(10)])
                email = EmailMessage('Hello', 'http://localhost:8000/panel/verify?link=' + digits,
                                     to=['']) # fill this param
                email.send()
                self.user.link = digits
                self.user.save()
                return HttpResponseRedirect('/accounts/login')
        else:
            form = UserCreationForm()
        return render(self, 'signup.html', {'form': form})

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
                        return HttpResponseRedirect('/panel')
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()
            return render(self, 'login.html', {'form': form})


# class Panel:
    # @login_required(login_url='/signin')
    # def home(self):
    #     addresses = Spaces.objects.filter(user_id=self.user.id)  # values_list('address', flat=True)
    #     return render(self, 'panel.html', {'addresses': addresses})
    #
    # @login_required(login_url='/signin')
    # def verify(self):
    #     if self.user.link == self.GET['link']:
    #         self.user.is_verified = True
    #         self.user.save()
    #         return HttpResponse('ok')
    #     else:
    #         return HttpResponse('failed')
    #
    # @login_required(login_url='/signin')
    # def submit_comment(self):
    #     if self.method == 'POST':
    #         comment = Comments()
    #         comment.user_id = self.user.id
    #         comment.comment = self.POST['comment']
    #         comment.space_id = self.GET['space_id']
    #         comment.save()
    #         return HttpResponseRedirect('/space?id=' + self.GET['space_id'])
    #
    # @login_required(login_url='/signin')
    # def like(self):
    #     tmp = SpaceRank.objects.filter(space_id=self.GET['space_id']).filter(user_id=self.user.id)
    #     if tmp.count() == 0:
    #         s = SpaceRank()
    #         s.space_id = self.GET['space_id']
    #         s.user_id = self.user.id
    #         s.rank = 1
    #         s.save()
    #     else:
    #         s = tmp[0]
    #         s.rank = 1
    #         s.save()
    #     return HttpResponseRedirect('/space?id=' + self.GET['space_id'])
    #
    # @login_required(login_url='/signin')
    # def dislike(self):
    #     tmp = SpaceRank.objects.filter(space_id=self.GET['space_id']).filter(user_id=self.user.id)
    #     if tmp.count() == 0:
    #         s = SpaceRank()
    #         s.space_id = self.GET['space_id']
    #         s.user_id = self.user.id
    #         s.rank = -1
    #         s.save()
    #     else:
    #         s = tmp[0]
    #         s.rank = -1
    #         s.save()
    #     return HttpResponseRedirect('/space?id=' + self.GET['space_id'])
    #
    # @login_required(login_url='/signin')
    # def profile(self):
    #     if self.method == 'POST':
    #         user = self.user
    #         user.availability = self.POST["availability"]
    #         user.wigu = self.POST["wigu"]
    #         user.education = self.POST["education"]
    #         user.language = self.POST["language"]
    #         user.about = self.POST["about"]
    #         user.interest = self.POST["interest"]
    #         user.civ = self.POST["civ"]
    #         user.cil = self.POST["cil"]
    #         user.save()
    #         return render(self, 'profile.html', {'user': user})
    #     else:
    #         pprint(self.user)
    #         pprint("---------------------")
    #         # return HttpResponse(self.user)
    #         # addresses = Spaces.objects.filter(user_id=self.user.id) #values_list('address', flat=True)
    #         return render(self, 'profile.html', {'user': self.user})
    #
    # @login_required(login_url='/signin')
    # def delete_item(self):
    #     t = Spaces.objects.get(id=self.POST["id"])
    #     t.price = self.POST["price"]
    #     t.address = self.POST["address"]
    #     t.save()
    #     return redirect('/panel')
    #
    # @login_required(login_url='/signin')
    # def submit_item(self):
    #     # pprint(self.user.username)
    #     # self.user.username = "test11"
    #     # self.user.save()
    #
    #     # s = Spaces()
    #     # s.address = "address1"
    #     # s.price = 4236
    #     # s.user_id = self.user.id
    #     # s.save()
    #     #
    #     # s = Spaces()
    #     # s.address = "address2"
    #     # s.price = 4695
    #     # s.user_id = self.user.id
    #     # s.save()
    #     #
    #     # s = Spaces()
    #     # s.address = "address3"
    #     # s.price = 4125
    #     # s.user_id = self.user.id
    #     # s.save()
    #     #
    #     s = Spaces()
    #     s.address = self.POST["address"]
    #     s.price = self.POST["price"]
    #     s.user_id = self.user.id
    #     s.save()
    #     # r = Spaces.objects.filter(user_id=self.user.id).values_list('address', flat=True)
    #     # pprint(r[0])
    #     return redirect('/panel')
