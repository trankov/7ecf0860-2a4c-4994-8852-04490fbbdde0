CACHES = {
   'default': {
       'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
                # 'django.core.cache.backends.locmem.LocMemCache',
        # The cache backend to use. The built-in cache backends are:
                # 'django.core.cache.backends.dummy.DummyCache'
                # 'django.core.cache.backends.filebased.FileBasedCache'
                # 'django.core.cache.backends.locmem.LocMemCache'
                # 'django.core.cache.backends.memcached.PyMemcacheCache'
                # 'django.core.cache.backends.memcached.PyLibMCCache'
                # 'django.core.cache.backends.redis.RedisCache'
       'KEY_FUNCTION': None,
       'KEY_PREFIX': '',
       'OPTIONS': {},
       'TIMEOUT': 300,
       'VERSION': 1,
   }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
USER_ONLINE_TIMEOUT = 300
USER_LAST_SCREEN_TIMEOUT = 60 * 60 * 24 * 7
