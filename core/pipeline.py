from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
password = settings.SOCIAL_USERS_PASSWORD


def create_or_get_user(backend, details, response, *args, **kwargs):
    email = response['email']
    username = email.split('@')[0]
    profile = response['picture']
    user, created = User.objects.get_or_create(
        email=email,
        username=username,
        profile_pic=profile
    )

    if created:
        user.set_password(password)
        user.save()

    return user