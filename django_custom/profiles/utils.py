from django.contrib.auth import get_user_model

def get_user(**kwargs):
    return get_user_model().objects.get(**kwargs)