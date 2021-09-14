from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .forms import BaseRegisterForm
from .models import CustomUser
from .services import *
from announcements.models import Reply, Announcement, Category
from announcements.filters import ReplyFilter


class BaseRegisterView(CreateView):
    model = CustomUser
    form_class = BaseRegisterForm
    success_url = '/announcements/'
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        code = OneTimeCode(user=user, value=generate_random_code(30))
        code.save()
        send_mail_to_confirm_registration(user=user, code=code)
        return super(BaseRegisterView, self).form_valid(form)


class UserProfile(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'accounts/profile.html'
    paginate_by = 10
    context_object_name = 'replies'

    def get_filter(self):
        return ReplyFilter(self.request.GET, queryset=get_current_user_reply_queryset_reverse_by_date(self.request),
                           request=self.request)

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)

        context['filter'] = self.get_filter()
        context['subscribed_categories'] = Category.objects.filter(subscriber=self.request.user.id)
        context['subscribers_list'] = [i['pk'] for i in self.request.user.category_set.all().values('pk')]

        return context


def confirm_email(request, code):
    if OneTimeCode.objects.filter(value=code).exists():
        user = CustomUser.objects.get(id=OneTimeCode.objects.get(value=code).user.id)
        user.is_active = True
        user.save()
        return redirect('/announcements/')
    else:
        return HttpResponse('Код недействителен.')
