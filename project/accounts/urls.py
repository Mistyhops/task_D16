from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import BaseRegisterView, UserProfile, confirm_email


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', BaseRegisterView.as_view(), name='signup'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('profile/activate/<code>/', confirm_email, name='activate_profile'),
]
