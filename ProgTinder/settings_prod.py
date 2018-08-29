DEBUG = True
ALLOWED_HOSTS = ['*']
STATIC_URL = '/static/' 
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'hello',
        'USER': 'hello_django',
        'HOST': 'localhost',
        'PASSWORD': 's6c89q4g',
        'PORT': '',
    }
}
