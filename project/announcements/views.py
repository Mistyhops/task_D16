from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AnnouncementForm
from .services import *
from .models import Reply, Category


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    ordering = '-time'
    context_object_name = 'announcements'


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcement_detail.html'

    def post(self, request, *args, **kwargs):
        announcement_id = self.kwargs.get('pk')
        reply = Reply(author=request.user, text=request.POST['text'],
                      announcement=Announcement.objects.get(pk=announcement_id))
        reply.save()
        return super(AnnouncementDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnnouncementDetailView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['subscribers_list'] = [i['pk'] for i in self.request.user.category_set.all().values('pk')]

        return context


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    template_name = 'announcements/announcement_create.html'
    form_class = AnnouncementForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnnouncementCreateView, self).form_valid(form)


class AnnouncementEditView(LoginRequiredMixin, UpdateView):
    template_name = 'announcements/announcement_create.html'
    form_class = AnnouncementForm

    def get_object(self, **kwargs):
        announcement_id = self.kwargs.get('pk')
        return Announcement.objects.get(id=announcement_id)

    def post(self, request, *args, **kwargs):
        if self.get_object(**kwargs).author == self.request.user:
            return super(AnnouncementEditView, self).post(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.WARNING, 'Only author can edit announcement')
            return super(AnnouncementEditView, self).get(request, *args, **kwargs)


class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'announcements/announcement_delete.html'
    queryset = Announcement.objects.all()
    success_url = '/announcements/'

    def get_object(self, **kwargs):
        announcement_id = self.kwargs.get('pk')
        return Announcement.objects.get(id=announcement_id)

    def post(self, request, *args, **kwargs):
        if self.get_object(**kwargs).author == self.request.user:
            return super(AnnouncementDeleteView, self).delete(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.WARNING, 'Only author can delete announcement')
            return super(AnnouncementDeleteView, self).get(request, *args, **kwargs)


def accept_reply(request, pk):
    reply = Reply.objects.get(id=pk)
    if reply.is_accepted:
        reply.is_accepted = False
    else:
        reply.is_accepted = True
    reply.save()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_reply(request, pk):
    reply = Reply.objects.get(id=pk)
    reply.is_active = False
    reply.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def subscribe_category(request, category_id):
    user = request.user
    category = Category.objects.get(id=category_id)
    if category.subscriber.filter(username=user).exists():
        category.subscriber.remove(user)
    else:
        category.subscriber.add(user)
    return redirect(request.GET['from'])
