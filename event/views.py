from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView, RedirectView
from . import models
from .forms import EventModelForm, CommentModelForm, DiscussionModelForm, CommentDiscussionModelForm
from django.urls import reverse, reverse_lazy
from account.models import Account
from django.utils import timezone

from django.http import request


def EventListView(request):
    event_list = {
        "event_all": models.Events.objects.all()
    }
    return render(request, "event/event_list.html", event_list)


#    context_object_name = 'event_l'
#    model = models.Events


# return events_list
# wecan change this name to  context_object_name= 'eventss'
#

class EventDetailView(DetailView):
    context_object_name = 'event'
    queryset = models.Events.objects.all()
    template_name = 'event/event_detail.html'


class CommentOneEventDetailView(DetailView):
    context_object_name = 'comment_detail_one_event'
    queryset = models.Events.objects.all()
    template_name = 'event/comment_detail_one_event.html'


class EventCreateView(CreateView):
    context_object_name = 'event_create'
    form_class = EventModelForm
    queryset = models.Events.objects.all()
    template_name = 'event/event_create.html'
    success_url = reverse_lazy('event:list_event')

    # success_url = '/'

    def form_valid(self, form):
        account = Account.objects.get(pk=self.request.user.pk)
        form.instance.account = account
        return super().form_valid(form)


class EventUpdateView(UpdateView):
    context_object_name = 'event_create'
    form_class = EventModelForm
    template_name = 'event/event_create.html'
    queryset = models.Events.objects.all()


class HomePageView(TemplateView):
    template_name = 'event/event_home_search.html'


class SearchResultsView(ListView):
    model = models.Events
    template_name = 'mainProject/show_event_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = models.Events.objects.filter(city=query)
        return object_list


class EventDeleteView(DeleteView):
    context_object_name = 'event_delete'
    template_name = 'event/event_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Events, id=id_)

    def get_success_url(self):
        return reverse("event:event_search")


##########################
'''def add_comment_to_post(request, pk):
    event = get_object_or_404(models.Events, pk=pk)

    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.save()
            return redirect('event:detail', pk=event.pk)

    else:
        form = CommentModelForm()
    return render(request, 'event/comment_form.html', {'form': form})


def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.approve()
    return redirect('event:detail', pk=comment.event.pk)'''


def add_comment_to_post(request, pk):
    print('olkijuujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', pk)
    event = get_object_or_404(models.Events, pk=pk)
    if request.method == "POST":
        form = CommentModelForm(request.POST)

        if form.is_valid():
            account = request.user
            comment = form.save(commit=False)
            comment.account = account
            comment.event = event

            comment.save()
            return redirect('event:event_detail', pk=event.pk)
    else:
        form = CommentModelForm()
    return render(request, 'event/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.approve()
    return redirect('event:event_detail', pk=comment.event.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.delete()
    return redirect('event:event_detail', pk=comment.event.pk)


########discussion#########
class DiscussionCreateView(CreateView):
    context_object_name = 'discussion_create'
    form_class = DiscussionModelForm
    queryset = models.Events.objects.all()
    template_name = 'discussion/discussion_create.html'

    def form_valid(self, form):
        account = Account.objects.get(pk=self.request.user.pk)
        form.instance.account = account
        return super().form_valid(form)


def DiscussionListView(self, request):
    account = Account.objects.get(pk=self.request.user.pk)
    event_list = {
        "discuttion_all": models.Discussion.objects.filter(city=account.wigu)
    }
    return render(request, "mainProject/home.html", event_list)


class DiscussionDetailView(DetailView):
    context_object_name = 'discussion_detail'
    queryset = models.Discussion.objects.all()
    template_name = 'discussion/discussion_detail.html'


class DiscussionUpdateView(UpdateView):
    context_object_name = 'discussion_create'
    form_class = DiscussionModelForm
    template_name = 'discussion/discussion_create.html'
    queryset = models.Discussion.objects.all()


class DiscussionDeleteView(DeleteView):
    context_object_name = 'discussion_delete'
    template_name = 'discussion/discussion_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Discussion, id=id_)

    def get_success_url(self):
        return reverse("event:discussion_detail_city")


def add_comment_to_discussion(request, pk):
    discussion = get_object_or_404(models.Discussion, pk=pk)
    if request.method == "POST":
        account = request.user
        form = CommentDiscussionModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.discussion = discussion
            comment.account = account
            comment.save()
            return redirect('event:discussion_detail', pk=discussion.pk)
    else:
        form = CommentDiscussionModelForm()
    return render(request, 'discussion/add_comment_to_discussion.html', {'form': form})


@login_required
def comment_discussion_approve(request, pk):
    comment = get_object_or_404(models.CommentDiscussion, pk=pk)
    comment.approve()
    return redirect('event:discussion_detail', pk=comment.discussion.pk)


@login_required
def comment_discussion_remove(request, pk):
    comment = get_object_or_404(models.CommentDiscussion, pk=pk)
    comment.delete()
    return redirect('event:discussion_detail', pk=comment.discussion.pk)


def navbar(request):
    event_list = {
        "event_all": models.Events.objects.all()
    }

    return render(request, "mainProject/event_list.html", event_list)


######member
'''class MemberCreateView(CreateView):
    model = models.MemberEvent
    context_object_name = 'member_create'
    template_name = 'event/member_create.html'
    fields = []

    def get_queryset(self):
        account = self.request.user
        print(self.request.GET.get('eventpk'))
        pk = self.request.GET.get('eventpk')
        memmber = self.model
        memmber.account = account
        memmber.event = models.Events.objects.filter(pk=pk)
        return memmber.save()'''


# def form_valid(self, form):
#     account = Account.objects.get(pk=self.request.user.pk)
#     form.instance.account = account
#     print(self.request.GET.get('eventpk'))
#     event = models.MemberEvent.objects.get(pk=self.request.GET.get('eventpk'))
#     form.instance.account = event
#     return super().form_valid(form)

class Joinevent(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('event:list_event')

    def get(self, *args, **kwargs):
        event = get_object_or_404(models.Events, pk=self.kwargs.get('pk'))
        try:
            models.MemberEvent.objects.create(account=self.request.user, event=event)
        except InterruptedError:
            HttpResponse("<h1> jjjfjfrj</h1>")
        else:
            HttpResponse("<h1> you are noe a member</h1>")

        return super().get(request, *args, **kwargs)


class Events_I_joined(ListView):
    model = models.MemberEvent
    context_object_name = 'myevent'
    template_name = "event/events_I_joined.html"

    def get_queryset(self):
        account = self.request.user
        query = models.MemberEvent.objects.filter(account=account)
        return query


class LeaveEvent(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # return reverse('event:event_search', kwargs={'pk': self.kwargs.get('pk')})
        return reverse('event:list_event')

    def get(self, *args, **kwargs):
        try:
            membership = models.MemberEvent.objects.filter(
                account=self.request.user,
                event__pk=self.kwargs.get('pk')
            ).get()
        except models.MemberEvent.DoesNotExist:
            HttpResponse("<h1> jjjfjfrj</h1>")

        else:
            membership.delete()
            HttpResponse("<h1> delete</h1>")

        return super().get(request, *args, **kwargs)


def index(request):
    account = request.user
    city = account.wigu
    discussion_list = {
        'discussion_list': models.Discussion.objects.filter(city__icontains=city)
    }

    return render(request, "mainProject/home.html", discussion_list)


class SearchDiscussion(ListView):
    model = models.Discussion
    template_name = 'mainProject/home.html'

    def get_queryset(self):
        account = self.request.user
        query = account.wigu
        object_list = models.Discussion.objects.filter(city__icontains=query)
        return object_list


# class showmembers(ListView):
#     model = models.MemberEvent
#     context_object_name = 'members'
#     template_name = 'mainProject/memmbers.html'
#
#     def get_queryset(self):
#         memmbers = models.MemberEvent.objects.filter()

# def showmembers(request,pk):
#     memmbers = {
#         "memmbers": models.MemberEvent.objects.filter(event__id)
#     }
#     return render(request, "event/event_list.html", event_list)

