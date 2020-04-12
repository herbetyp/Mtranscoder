from itertools import count
import os

from .overwrite_file import files_exists, file_exist
from .progresss_bar import progressbar


class Video:

    def __init__(
            self, input_midia_format: str, source_path: str, output_midia_format: str,
            output_path: str, bitrate: str, time: str) -> str:

        self.output_midia_format = output_midia_format
        self.input_midia_format = input_midia_format
        self.codec_video = '-c:v libx264'
        self.codec_audio = '-c:a aac'
        self.crf = '-crf 20'
        self.preset = '-preset ultrafast'
        self.bitrate_audio = bitrate
        self.command_ffmpeg = 'ffmpeg'
        self.time = ''
        self.source_path = source_path
        self.output_path = output_path
        self.time = time

        if self.input_midia_format == 'webm' or output_midia_format == 'webm':
            self.codec_video = '-c:v vp9'
            self.codec_audio = '-c:a libvorbis'
        if self.input_midia_format == 'vob' or output_midia_format == 'vob':
            self.codec_audio = '-c:a ac3'

    def execute_files(self):
        # Multiple files
        files = (file for _, _, files in os.walk(self.source_path)
                 for file in files if self.input_midia_format in file)
        files = tuple(files)
        if files:
            for file in files:
                name_file, extension_file = os.path.splitext(file)

                caption_path = name_file + '.srt'

                if os.path.isfile(caption_path):
                    caption_input = f'-i "{caption_path}"'
                    caption_map = '-c:s -map v:0 -map a -map 1:0'
                else:
                    caption_input = ''
                    caption_map = ''

                exit_file = (
                    f'{self.output_path}{name_file}_{self.output_midia_format}.'
                    f'{self.output_midia_format}'
                )
                if files_exists(name_file, exit_file, self.output_midia_format):
                    command = (
                        f'{self.command_ffmpeg} -i "{self.source_path}{file}" {caption_input} '
                        f'{self.codec_video} {self.crf} {self.preset} {self.codec_audio} '
                        f'{self.bitrate_audio} {self.time} {caption_map} "{exit_file}" -y'
                        f' &> /dev/null'
                    )

                    def ffmpeg():
                        if os.system(command):
                            for i in count(1):
                                ...
                        return

                    progressbar(ffmpeg)
                else:
                    exit()
        else:
            print(
                f'\nFiles with extension .{self.input_midia_format} not found')

    def execute_file(self):
        # One files
        self.source_path = self.source_path.split('/')

        if file_exist(self.source_path[-1], '/'.join(self.source_path)):
            name_file, extension_file = os.path.splitext(self.source_path[-1])

            caption_path = name_file + '.srt'

            if os.path.isfile(caption_path):
                caption_input = f'-i "{caption_path}"'
                caption_map = '-c:s -map v:0 -map a -map 1:0'
            else:
                caption_input = ''
                caption_map = ''

            self.source_path = '/'.join(self.source_path)

            exit_file = (
                f'{self.output_path}/{name_file}_{self.output_midia_format}.'
                f'{self.output_midia_format}').replace('//', '/')

            if files_exists(name_file, exit_file, self.output_midia_format):
                command = (
                    f'{self.command_ffmpeg} -i "{self.source_path}" '
                    f'{caption_input} {self.codec_video} {self.crf} {self.preset} '
                    f'{self.codec_audio} {self.bitrate_audio} {self.time} {caption_map} '
                    f'"{exit_file}" -y &> /dev/null'
                )

                def ffmpeg():
                    if os.system(command):
                        for i in count(1):
                            ...
                    return

                progressbar(ffmpeg)
            else:
                exit()
        else:
            print(
                f'\nThe file {self.source_path[-1]} does not exist.')
