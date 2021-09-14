from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import get_connection, EmailMultiAlternatives
from django.conf import settings

from accounts.models import CustomUser
from .services import get_announcement_list_for_last_week_for_selected_user


@shared_task
def regular_subscribers_email_newsletter():
    connection = get_connection()
    connection.open()
    messages = []

    for user in CustomUser.objects.all():
        if get_announcement_list_for_last_week_for_selected_user(user):

            html_content = render_to_string(
                'email/weekly_email_newsletter.html',
                {
                    'username': user.username,
                    'announcement_list': get_announcement_list_for_last_week_for_selected_user(user)['announcement_list']
                }
            )

            msg = EmailMultiAlternatives(
                subject='',
                body='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
                connection=connection,
            )
            msg.attach_alternative(html_content, 'text/html')
            messages.append(msg)

    connection.send_messages(messages)
    connection.close()
