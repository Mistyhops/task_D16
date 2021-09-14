from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

import secrets
import string
import datetime

from announcements.models import Reply, Announcement
from .models import OneTimeCode

import sys

sys.path.append('..')


def generate_random_code(length):
    choices = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(choices) for i in range(length))
    return random_string


def send_mail_to_confirm_registration(user, code):

    html_content = render_to_string(
        'email/confirm_email_registration.html',
        {
            'user': user,
            'code': code,
        }
    )

    msg = EmailMultiAlternatives(
        subject=1,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def get_current_user_reply_queryset_reverse_by_date(request):
    if request is None:
        return Reply.objects.none()
    else:
        announcement_list = Announcement.objects.filter(author=request.user)
        reply_list = Reply.objects.filter(announcement__in=announcement_list, is_active=True).order_by('-time')
        return reply_list


def get_old_one_time_codes():
    old_codes = OneTimeCode.objects.filter(time__lt=datetime.datetime.now() - datetime.timedelta(hours=24))
    return old_codes
