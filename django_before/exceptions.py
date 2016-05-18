
from django.core.exceptions import ImproperlyConfigured


class DjangoBeforeError(Exception):
    pass


class DjangoBeforeImproperlyConfigured(DjangoBeforeError, ImproperlyConfigured):
    pass


class DjangoBeforeNotImplemented(DjangoBeforeError, NotImplementedError):
    pass


class DjangoBeforeWrongArguments(DjangoBeforeError):
    pass
