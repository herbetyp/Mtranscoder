from unittest import TestCase
import os
import sys

from libs.video import Video


class VideoTestExistFile(TestCase):

    video = Video('mp4', os.curdir, 'mkv', os.curdir, '320k', '00:00:00 00:00:00', None)

    def setUp(self):
        os.mknod('teste.mp4')
        os.mknod('teste.mkv')
        os.mknod('teste.srt')

    def test_filter_files(self):
        self.assertEqual(self.video.filter_files(), ['teste.mp4'])

    def test_caption(self):
        self.assertEqual(self.video.caption('teste.srt'), ('-i "teste.srt"',
                                                           '-c:s -map v:0 -map a -map 1:0', 'teste.srt'))

    def tearDown(self):
        try:
            os.remove('teste.mp4')
            os.remove('teste.mkv')
            os.remove('teste.srt')
        except:
            ...


class TestVideoNoExistFile(TestCase):

    video = Video('mp4', os.curdir, 'mkv', os.curdir, '320k', '00:00:00 00:00:00', None)

    def test_filter_file_no_file(self):
        self.assertEqual(self.video.filter_files(), False)

    def test_caption_no_file(self):
        self.assertEqual(self.video.caption('teste.srt'), ('', '', 'teste.srt'))
