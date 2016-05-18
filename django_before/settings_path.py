import os

from .exceptions import DjangoBeforeImproperlyConfigured


def make_subpather(relative_file, dirs_up_count):
    root_dir = _RootDir(relative_file, dirs_up_count)
    return root_dir


class _RootDir(object):
    def __init__(self, relative_file, dirs_up_count):
        self.root_dir = self._dirup(relative_file, dirs_up_count)

    @staticmethod
    def _dirup(relative_file, dirs_up_count):
        if dirs_up_count < 0:
            raise DjangoBeforeImproperlyConfigured('Given negative count of dirs to up: %d', dirs_up_count)

        path = relative_file
        for _ in range(dirs_up_count):
            path = os.path.abspath(os.path.dirname(path))

        return path

    def __call__(self, entry):
        return os.path.abspath(os.path.join(self.root_dir, entry))
