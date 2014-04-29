__author__ = 'Felix'
import logging
logger = logging.getLogger(__name__)

from django.db import models
from django.utils.translation import gettext as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AppUserManager


class BaseAppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('E-Mail'), max_length=512, unique=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    def __unicode__(self):
        return unicode(self.email)

    class Meta:
        abstract = True


class AppUser(BaseAppUser):
    first_name = models.CharField(
        max_length=1000, verbose_name=_('First name'), null=True, blank=True
    )
    last_name = models.CharField(
        max_length=1000, verbose_name=_('Last name'), null=True, blank=True
    )

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return u'%s %s' % (self.first_name)





