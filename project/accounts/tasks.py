from celery import shared_task

from .services import get_old_one_time_codes


@shared_task
def delete_old_codes():
    if get_old_one_time_codes():
        get_old_one_time_codes().delete()
