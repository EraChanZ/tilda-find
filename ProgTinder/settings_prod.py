DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'hello',
        'USER': 'hello_django',
        'HOST': 'localhost',
        'PORT': '',
    }
}
