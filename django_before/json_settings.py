import json
from .exceptions import DjangoBeforeImproperlyConfigured, DjangoBeforeNotImplemented


def make_json_settings_reader(settings_filename):
    reader = _JSONSettingsReader(settings_filename)
    return reader


class _JSONSettingsReader(object):
    def __init__(self, settings_filename):
        self.settings_filename = settings_filename
        self.settings = self._load_settings(settings_filename)

    def __getitem__(self, setting_name):
        try:
            return self.settings[setting_name]
        except KeyError:
            raise DjangoBeforeImproperlyConfigured('Setting with name "%s" has not found in file "%s".' %
                                                   (setting_name, self.settings_filename))

    def __setitem__(self, *args, **kwargs):
        raise DjangoBeforeNotImplemented('JSONSettingsReader does not allow set up settings values.')

    @staticmethod
    def _load_settings(settings_filename):
        settings = None

        try:
            file = open(settings_filename)
        except IOError:
            raise DjangoBeforeImproperlyConfigured('Failed to open setting\'s file with name "%s".' % settings_filename)
        else:
            with file:
                try:
                    settings = json.load(file)
                except json.JSONDecodeError as e:
                    raise DjangoBeforeImproperlyConfigured('Failed to parse settings file "%s". JSON error: "%s".' %
                                                           (settings_filename, e))

        if not isinstance(settings, dict):
            raise DjangoBeforeImproperlyConfigured('Setting\'s loaded from file with name "%s" are not in dict format.' %
                                                   settings_filename)

        return settings
