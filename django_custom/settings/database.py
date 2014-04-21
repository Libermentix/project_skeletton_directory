from _install.skeletton.core.utils import get_env_variable

DATABASES = {
    'default': {
        'ENGINE': get_env_variable('DB_ENGINE'), #'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PW'),
        'HOST': get_env_variable('DB_HOST'), #'localhost'
        'PORT': get_env_variable('DB_PORT'), #'', # Set to empty string for default.,
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

