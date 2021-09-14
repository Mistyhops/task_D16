import django_filters
from django import forms

from .services import *


class ReplyFilter(django_filters.FilterSet):

    time = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt',
                                         label='Позже даты',
                                         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    author = django_filters.ModelChoiceFilter(label='Автор',
                                              queryset=get_reply_authors_for_current_user_announcements,
                                              )
    announcement = django_filters.ModelChoiceFilter(label='Объявление',
                                                    queryset=get_current_user_announcements)

    class Meta:
        model = Reply
        fields = ('time', 'author', 'announcement', )

