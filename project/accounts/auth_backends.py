from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


class AuthByEmail(ModelBackend):
    """
        Let user authenticate with both login or email
    """

    def authenticate(self, request, username=None, password=None, **kwargs):

        user_model = get_user_model()

        try:
            user = user_model.objects.get(email__iexact=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except user_model.DoesNotExist:
            return None
