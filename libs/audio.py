from itertools import count
import os

from .video import Video
from .overwrite_file import files_exists
from .progresss_bar import progressbar


class Audio(Video):
    def __init__(self, input_midia_format, source_path, output_midia_format,
                 output_path, bitrate, time):
        super().__init__(input_midia_format, source_path,
                         output_midia_format, output_path, bitrate, time)

        if self.input_midia_format == 'mp3' or self.output_midia_format == 'mp3':
            self.codec_audio = '-c:a libmp3lame'
            self.bitrate_audio = bitrate
            self.time = time

        if self.input_midia_format == 'ogg' or self.output_midia_format == 'ogg':
            if self.input_midia_format == 'ogg' and self.output_midia_format == 'mp3':
                self.codec_audio == '-c:a libmp3lame'
                self.bitrate_audio = bitrate
                self.time = time
            else:
                self.codec_audio = '-c:a libvorbis'
                self.bitrate_audio = bitrate
                self.time = time

        if self.input_midia_format == 'flac' or self.output_midia_format == 'flac':
            self.codec_audio = '-c:a flac'
            self.bitrate_audio = bitrate
            self.time = time

        if self.input_midia_format == 'aac' or self.output_midia_format == 'aac':
            self.codec_audio = '-c:a aac'
            self.bitrate_audio = bitrate + ' -f adts'
            self.time = time

    def execute_files(self):
        # Multiple files
        files = (file for _, _, files in os.walk(self.source_path)
                 for file in files if self.input_midia_format in file)
        files = tuple(files)
        if files:
            for file in files:
                name_file, extension_file = os.path.splitext(file)

                exit_file = (
                    f'{self.output_path}{name_file}_{self.output_midia_format}.'
                    f'{self.output_midia_format}'
                )
                if files_exists(name_file, exit_file, self.output_midia_format):
                    command = (
                        f'{self.command_ffmpeg} -i "{self.source_path}{file}" -vn '
                        f'{self.bitrate_audio} {self.codec_audio} {self.time} '
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
                f'\nFiles with extension .{self.input_midia_format} not found')

    def execute_file(self):
        # One files
        self.source_path = self.source_path.split('/')

        if files_exists(self.source_path[-1], '/'.join(self.source_path), ''):
            name_file, extension_file = os.path.splitext(self.source_path[-1])

            self.source_path = '/'.join(self.source_path)

            exit_file = (
                f'{self.output_path}/{name_file}_{self.output_midia_format}.'
                f'{self.output_midia_format}').replace('//', '/')

            if files_exists(name_file, exit_file, self.output_midia_format):
                command = (
                    f'{self.command_ffmpeg} -i "{self.source_path}" -vn '
                    f'{self.bitrate_audio} {self.codec_audio} {self.time} '
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
                f'\nThe file {self.source_path[-1]} does not exist in {"/".join(self.source_path[:-1])}')
