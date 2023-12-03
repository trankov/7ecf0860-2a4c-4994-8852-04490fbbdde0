DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': False,
        'AUTOCOMMIT': True,
        'CONN_MAX_AGE': None,  # Use 0 to close database connections at the end
                            # of each request and None for unlimited
                            # persistent connections.
        'DISABLE_SERVER_SIDE_CURSORS': False, # This is a PostgreSQL-specific setting
        'ENGINE': 'django.db.backends.postgresql',
                # 'django.db.backends.mysql'
                # 'django.db.backends.sqlite3'
                # 'django.db.backends.oracle'
        'HOST': "localhost",
        'NAME': "nepo",
        'PASSWORD': "ofalizard",
        'USER': "trankov",
        'PORT': 5432,
        # 'OPTIONS': {},
        # 'TEST': {},
        'TIME_ZONE': None,

    }
}
DATABASE_ROUTERS = ()
DEFAULT_INDEX_TABLESPACE = ''
DEFAULT_TABLESPACE = ''
