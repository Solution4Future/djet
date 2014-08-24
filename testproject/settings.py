DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

SECRET_KEY = '_'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'tests',
)

STATIC_URL = '/static/'