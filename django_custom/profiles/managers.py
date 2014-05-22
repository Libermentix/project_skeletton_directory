__author__ = 'Felix'
import logging

logger = logging.getLogger(__name__)


from django.contrib.auth.models import BaseUserManager


class AppUserManager(BaseUserManager):
    PW_ALLOWED_CHARS = 'abcdefghjkmnpqrstuvwxyz' + \
                       'ABCDEFGHJKLMNPQRSTUVWXYZ' + \
                       '23456789' + \
                       '_+=&^%$#@'

    def create_user(self, email, password=None, *args, **kwargs):
        """
        creates a user, if no password is set, a random passwort is set
        *args, and **kwargs are ignored in case username or other variables
        are passed to that function.

        """
        if not email:
            msg = "user must have an email adress"
            raise ValueError(msg)

        email = AppUserManager.normalize_email(email=email)

        user = self.model(email=email, *args, **kwargs)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password, *args, **kwargs):
        """
        creates a superuser with all admin flags set to true
        """
        user = self.create_user(email=email, password=password, *args, **kwargs)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





