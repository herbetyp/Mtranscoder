from unittest import TestCase
import os

from libs.audio import Audio


class AudioTest(TestCase):

    audio = Audio('mkv', os.curdir, 'mp3', os.curdir, '320k', '00:00:00 00:00:00', None)

    def setUp(self):
        os.mknod('teste.mp4')
        os.mknod('teste.mkv')

    def test_filter_files(self):
        self.assertEqual(self.audio.filter_files(), ['teste.mkv'])

    def tearDown(self):
        os.remove('teste.mp4')
        os.remove('teste.mkv')
