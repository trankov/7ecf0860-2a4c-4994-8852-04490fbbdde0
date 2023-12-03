ADMINS = (
    ("Aleksei Trankov", "trankov@yandex.ru"),
)
# A list of all the people who get code error notifications.
# When DEBUG=False and AdminEmailHandler is configured in LOGGING
# (done by default), Django emails these people the details of exceptions
# raised in the request/response cycle.
# Each item in the list should be a tuple of (Full name, email address).
# Example:
# [('John', 'john@example.com'), ('Mary', 'mary@example.com')]

DEFAULT_FROM_EMAIL = "emailsecrets.login"
SERVER_EMAIL =" emailsecrets.login"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = ""
# Default: Not defined
# The directory used by the file email backend to store output files.
EMAIL_HOST = "emailsecrets.smtp_server"
EMAIL_HOST_PASSWORD = "emailsecrets.password"
EMAIL_HOST_USER = "emailsecrets.login"
EMAIL_PORT = "emailsecrets.port"
EMAIL_SUBJECT_PREFIX = "Непоседы: "
EMAIL_TIMEOUT = 5
EMAIL_USE_LOCALTIME = False
MANAGERS = []
EMAIL_USE_TLS = True
# Whether to use a TLS (secure) connection when talking to the SMTP server.
# This is used for explicit TLS connections, generally on port 587.
# If you are experiencing hanging connections,
# see the implicit TLS setting EMAIL_USE_SSL.
EMAIL_USE_SSL = not EMAIL_USE_TLS
# Whether to use an implicit TLS (secure) connection when talking
# to the SMTP server. In most email documentation this type of TLS connection
# is referred to as SSL. It is generally used on port 465.
# If you are experiencing problems, see the explicit TLS setting EMAIL_USE_TLS.
#
# Note that EMAIL_USE_TLS/EMAIL_USE_SSL are mutually exclusive, so only
# set one of those settings to True.
EMAIL_SSL_CERTFILE = None
# If EMAIL_USE_SSL or EMAIL_USE_TLS is True, you can optionally specify the path
# to a PEM-formatted certificate chain file to use for the SSL connection.
EMAIL_SSL_KEYFILE = None
# If EMAIL_USE_SSL or EMAIL_USE_TLS is True, you can optionally specify the path
# to a PEM-formatted private key file to use for the SSL connection.
#
# Note that setting EMAIL_SSL_CERTFILE and EMAIL_SSL_KEYFILE doesn’t result
# in any certificate checking. They’re passed to the underlying SSL connection.
# Please refer to the documentation of Python’s ssl.wrap_socket() function
# for details on how the certificate chain file and private key file are handled.
