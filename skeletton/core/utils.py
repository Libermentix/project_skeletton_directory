import random
import string
import os

from django.core.exceptions import ImproperlyConfigured


def generate_unique_id(length=6, chars=string.ascii_uppercase+string.digits):
    '''
    generates an id of length picked out of chosen characters
    see: http://stackoverflow.com/questions/2257441/
    python-random-string-generation-with-upper-case-letters-and-digits
    '''
    return u''.join(random.choice(chars) for _ in range(length))


def get_env_variable(var_name):
    msg = 'Set the %s environment variable'
    try:
        return os.environ[var_name]
    except:
        error_msg = msg % var_name
        raise ImproperlyConfigured(error_msg)