import os
# Production Level Changes
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

#Change session engine to cookie based
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"


#cache optmization
def cache_images_forever(headers, path, url):
    #Force images to be cached forever
    tokens = path.split(".")
    if len(tokens) > 1:
        extension = tokens[-1].lower()
        if extension in ('png', 'jpg', 'jpeg', 'ico', 'gif'):
            headers['Cache-Control'] = 'public, max-age=315360000'    

WHITENOISE_ADD_HEADERS_FUNCTION = cache_images_forever
