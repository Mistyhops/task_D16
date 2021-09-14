from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from .models import Reply


@receiver(post_save, sender=Reply)
def notify_reply_author(sender, instance, created, **kwargs):

    if created:
        html_content = render_to_string(
            'email/notify_reply_author_reply_created.html',
            {
                'username': instance.author.username,
                'announcement': instance.announcement,
                'reply': instance,
            }
        )

        msg = EmailMultiAlternatives(
            subject=1,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.author.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    elif instance.is_accepted is True:
        html_content = render_to_string(
            'email/notify_reply_author_reply_accepted.html',
            {
                'username': instance.author.username,
                'announcement': instance.announcement,
                'reply': instance,
            }
        )

        msg = EmailMultiAlternatives(
            subject=1,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.author.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(post_save, sender=Reply)
def notify_announcement_author_reply_created(sender, instance, created, **kwargs):

    if created:
        html_content = render_to_string(
            'email/notify_announcement_author_reply_created.html',
            {
                'username': instance.announcement.author.username,
                'announcement': instance.announcement,
                'reply': instance,
            }
        )

        msg = EmailMultiAlternatives(
            subject=1,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.announcement.author.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
