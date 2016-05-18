import unittest
from django_before.settings_path import make_subpather
from django_before.exceptions import DjangoBeforeImproperlyConfigured


class TestMakeSubpather(unittest.TestCase):

    def test_common_empty(self):
        subpath = make_subpather('/home/notrealuser/notrealproject/notrealpath/somesubpath', 2)
        self.assertEqual(subpath(''), '/home/notrealuser/notrealproject')

    def test_common_subpath(self):
        subpath = make_subpather('/home/notrealuser/notrealproject/notrealpath/somesubpath', 2)
        self.assertEqual(subpath('test'), '/home/notrealuser/notrealproject/test')
        self.assertEqual(subpath('test.jpg'), '/home/notrealuser/notrealproject/test.jpg')

    def test_negative_dirups(self):
        self.assertRaises(DjangoBeforeImproperlyConfigured, make_subpather,
                          '/home/notrealuser/notrealproject/notrealpath/somesubpath', -1)

    def test_zero_dirups(self):
        subpath = make_subpather('/home/notrealuser/notrealproject/notrealpath/somesubpath', 0)
        self.assertEqual(subpath(''), '/home/notrealuser/notrealproject/notrealpath/somesubpath')
