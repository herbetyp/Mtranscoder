import os
from unittest import TestCase
from unittest.mock import patch

from libs.check_files import files_exists


class TestFileExists(TestCase):

    def setUp(self):
        os.mknod('teste.mp4')

    @patch('builtins.input', lambda _: 'y')
    def test_yes_overwrite(self):

        func = files_exists('teste', os.curdir, 'mp4')
        assert func == True

    @patch('builtins.input', lambda _: 'n')
    def test_not_overwrite(self):

        func = files_exists('teste', os.curdir, 'mp4')
        assert func == False

    def tearDown(self):
        os.remove('teste.mp4')
