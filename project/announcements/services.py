import datetime

from .models import Announcement, Reply
from accounts.models import CustomUser


def get_current_user(request):
    if request:
        user = request.user
        return user
    else:
        return None


def get_current_user_announcements(request):
    if request is None:
        return Announcement.objects.all()
    else:
        announcement_list = Announcement.objects.filter(author=get_current_user(request))
        reply_list = Reply.objects.filter(announcement__in=announcement_list, is_active=True).values('announcement_id')
        announcements_with_any_reply = Announcement.objects.filter(id__in=reply_list)
        return announcements_with_any_reply


def get_reply_authors_for_current_user_announcements(request):
    if request is None:
        return CustomUser.objects.all()
    else:
        announcement_list = Announcement.objects.filter(author=request.user)
        reply_list = Reply.objects.filter(announcement__in=announcement_list, is_active=True).values('author_id')
        reply_author_list = CustomUser.objects.filter(id__in=reply_list)
        return reply_author_list


def get_announcement_list_for_last_week_for_selected_user(user):
    today_date = datetime.datetime.now()
    start_date = today_date - datetime.timedelta(weeks=1)

    if user.category_set.all():
        announcement_list = Announcement.objects.filter(category__in=user.category_set.all(),
                                                        time__range=(start_date, today_date)).distinct()
        return {
            'announcement_list': announcement_list,
        }
    return None
