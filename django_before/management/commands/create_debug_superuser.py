from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from optparse import make_option
from ...import exceptions


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--username',
                    action='store',
                    default=None,
                    help='Username for new user'),
        make_option('--password',
                    action='store',
                    default=None,
                    help='User Password'),
        make_option('--email',
                    action='store',
                    default=None,
                    help='User Email Address'),
        )

    def handle(self, username, password, email, *args, **kwargs):
        if not(username and password and email):
            raise exceptions.DjangoBeforeWrongArguments('Invalid arguments username="%s", password="%s", email="%s".' %
                                                        (username, password, email))

        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)

        user.is_superuser = True
        user.email = email
        user.set_password(password)
        user.save()
