from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext as _

from ._install.skeletton.profiles.models import AppUser


class AppUserCreationForm(forms.ModelForm):
    """
    Form for creating a new user.
    """

    password1 = forms.CharField(
        label=_(u'Password'), widget=forms.PasswordInput)

    password2 = forms.CharField(
        label=_(u'Password'), widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = ('email',)


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            msg = _('Passwords do not match')
            raise forms.ValidationError(msg)

        return password2

    def save(self, commit=True):
        user = super(AppUserCreationForm, self).save(commit=False)

        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()

        return user


class AppUserAdminChangeForm(forms.ModelForm):
    """
    Form for modifying an existing user
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = AppUser

    def clean_password(self):
        """
        clean_password always provides the initial value of the password,
        because the user should not be able to override it in the admin.
        """
        return self.initial['password']