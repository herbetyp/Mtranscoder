from itertools import count
import os

from .video import Video
from .check_files import files_exists
from .progresss_bar import progressbar


class Audio(Video):
    def __init__(self, input_midia_format, source_path, output_midia_format,
                 output_path, bitrate, time, qrange):
        super().__init__(input_midia_format, source_path,
                         output_midia_format, output_path, bitrate, time, qrange)

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
        files = set((files for files in os.listdir(self.source_path)[:self.qrange]
                     if self.input_midia_format in files.split('.')[-1]))
        if files:
            for file in files:
                name_file, extension_file = os.path.splitext(file)

                exit_file = (
                    f'{self.output_path}/{name_file}_{self.output_midia_format}.'
                    f'{self.output_midia_format}'
                )
                if files_exists(name_file, exit_file, self.output_midia_format):
                    command = (
                        f'{self.command_ffmpeg} -i "{self.source_path}/{file}" -vn '
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
                    break
        else:
            print(
                f'\nFiles with extension .{self.input_midia_format} in "{self.source_path}"')
