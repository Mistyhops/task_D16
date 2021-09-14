from django.urls import path

from .views import AnnouncementListView, AnnouncementDetailView, AnnouncementCreateView, \
    AnnouncementEditView, AnnouncementDeleteView, accept_reply, delete_reply, subscribe_category


urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('<int:pk>/edit/', AnnouncementEditView.as_view(), name='announcement_edit'),
    path('<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement_delete'),
    path('reply/<int:pk>/accept', accept_reply, name='accept_reply'),
    path('reply/<int:pk>/delete', delete_reply, name='delete_reply'),
    path('category/<int:category_id>/subscribe/', subscribe_category, name='subscribe'),

]
