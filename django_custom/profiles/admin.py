__author__ = 'Felix'
import logging

logger = logging.getLogger(__name__)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ._install.skeletton.profiles.forms import AppUserCreationForm, AppUserAdminChangeForm
from ._install.skeletton.profiles.models import AppUser


class AppUserAdmin(UserAdmin):
    """
    Admin class to customize the way the admin looks for creating, viewing and
    changing a user.

    """
    add_form = AppUserCreationForm
    form = AppUserAdminChangeForm

    list_display = ('email', 'is_staff', 'is_admin', 'is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)

    search_fields = ('email',)

    ordering = ('email',)

    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields':
                             ('is_active',
                              'is_staff',
                              'is_superuser',
                              'groups',
                              'user_permissions',)
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)
        }),
    )


admin.site.register(AppUser, AppUserAdmin)

