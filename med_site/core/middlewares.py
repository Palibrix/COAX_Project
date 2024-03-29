from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from re import compile


EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/')), compile('admin'),
               # compile("auth/register/")
               ]


def is_exempt_url(request, exempt_urls=None):
    """Check if the request URL is exempted from
    the middleware.
    :param request: request to check
    :param exempt_urls: optional list of exempt urls
    :return:
    """
    if not exempt_urls:
        exempt_urls = EXEMPT_URLS

    path = request.path_info.lstrip('/')
    if any(m.match(path) for m in exempt_urls):
        return True
    return False


class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).
    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, 'user'):
            raise AttributeError("The Login Required middleware requires authentication middleware to be installed. "
                                 "Edit your MIDDLEWARE_CLASSES setting to insert "
                                 "django.contrib.auth.middleware.AuthenticationMiddleware'. If that doesn't work, "
                                 "ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes "
                                 "django.core.context_processors.auth'.")
        if not request.user.is_authenticated:
            if not is_exempt_url(request):
                return HttpResponseRedirect(settings.LOGIN_URL)

        return self.get_response(request)
