import unittest
from unittest.mock import patch, mock_open

from django_before.json_settings import make_json_settings_reader
from django_before.exceptions import (
    DjangoBeforeImproperlyConfigured,
    DjangoBeforeNotImplemented
)

REGULAR_SETTINGS_SAMPLE = '''
{
  "KEY1": "VALUE1",
  "KEY2": "VALUE2"
}
'''


MALFORMED_SETTINGS_SAMPLE = '''
{
   WRONG FORMAT
  "KEY1": "VALUE1",
  "KEY2": "VALUE2"
}
'''


NONDICT_SETTINGS_SAMPLE = '''
[{
  "KEY1": "VALUE1",
  "KEY2": "VALUE2"
}]
'''


class TestMakeJsonSettingsReader(unittest.TestCase):

    def test_regular_settings(self):
        with patch('builtins.open', mock_open(read_data=REGULAR_SETTINGS_SAMPLE)) as mock_file:
            settings = make_json_settings_reader('some/path')
            self.assertEqual(settings['KEY1'], 'VALUE1')
            self.assertEqual(settings['KEY2'], 'VALUE2')
            mock_file.assert_called_once_with('some/path')

    def test_malformed_settings(self):
        with patch('builtins.open', mock_open(read_data=MALFORMED_SETTINGS_SAMPLE)) as mock_file:
            self.assertRaises(DjangoBeforeImproperlyConfigured, make_json_settings_reader, 'some/path')
            mock_file.assert_called_once_with('some/path')

    def test_nondict_settings(self):
        with patch('builtins.open', mock_open(read_data=NONDICT_SETTINGS_SAMPLE)) as mock_file:
            self.assertRaises(DjangoBeforeImproperlyConfigured, make_json_settings_reader, 'some/path')
            mock_file.assert_called_once_with('some/path')

    def test_set_value(self):
        def _set_dict_value(d, k, v):
            '''
                Helper to try set value in dict, because it is not allowed via lambda in python
            '''
            d[k] = v

        with patch('builtins.open', mock_open(read_data=REGULAR_SETTINGS_SAMPLE)) as mock_file:
            settings = make_json_settings_reader('some/path')
            self.assertRaises(DjangoBeforeNotImplemented, _set_dict_value, settings, 'KEY1', 'VALUE')
            mock_file.assert_called_once_with('some/path')

    def test_access_absent_key(self):
        with patch('builtins.open', mock_open(read_data=REGULAR_SETTINGS_SAMPLE)) as mock_file:
            settings = make_json_settings_reader('some/path')
            self.assertRaises(DjangoBeforeImproperlyConfigured, lambda: settings['ABSENT_KEY'])
            mock_file.assert_called_once_with('some/path')

    def test_no_file_found(self):
        bad_open = mock_open()
        bad_open.side_effect = IOError('File not found emulation.')
        with patch('builtins.open', bad_open) as mock_file:
            self.assertRaises(DjangoBeforeImproperlyConfigured, make_json_settings_reader, 'some/path')
            mock_file.assert_called_once_with('some/path')
