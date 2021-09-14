from django import forms
from ckeditor.widgets import CKEditorWidget

from .services import *
from .models import Category


class AnnouncementForm(forms.ModelForm):
    header = forms.CharField(label='Заголовок')
    text = forms.CharField(label='Текст:', widget=CKEditorWidget)
    category = forms.ModelMultipleChoiceField(label='Категория', queryset=Category.objects.all())

    class Meta:
        model = Announcement
        fields = ['header', 'text', 'category']
