import os

from .video import Video
from .overwrite_file import file_exists


class Audio(Video):
    def __init__(self, input_midia_format, source_path, output_midia_format,
                 output_path, bitrate, time):
        super().__init__(input_midia_format, source_path,
                         output_midia_format, output_path, bitrate, time)

        if self.input_midia_format == 'mp3' or self.output_midia_format == 'mp3':
            self.codec_audio = '-acodec libmp3lame'
            self.bitrate_audio = bitrate
            self.time = f'-ss {time[0]} -t {time[1]}'

        if self.input_midia_format == 'ogg' or self.output_midia_format == 'ogg':
            self.codec_audio = '-acodec libvorbis'
            self.bitrate_audio = bitrate
            self.time = f'-ss {time[0]} -t {time[1]}'

        if self.input_midia_format == 'flac' or self.output_midia_format == 'flac':
            self.codec_audio = '-c:a flac'
            self.bitrate_audio = bitrate
            self.time = f'-ss {time[0]} -t {time[1]}'

        if self.input_midia_format == 'aac' or self.output_midia_format == 'aac':
            self.codec_audio = '-c:a aac'
            self.bitrate_audio = bitrate + ' -f adts'
            self.time = f'-ss {time[0]} -t {time[1]}'

    def execute(self):
        files = (file for _, _, files in os.walk(self.source_path)
                 for file in files if self.input_midia_format in file and '_NEW' not in file)

        if not list(files):
            print(
                f'\nFiles .{self.input_midia_format} no _NEW not found.')

        for file in files:
            name_file, extension_file = os.path.splitext(file)
            exit_file = (
                f'{self.output_path}/{name_file}_NEW.{self.output_midia_format}'
            )
            if file_exists(name_file, exit_file, self.output_midia_format):
                ...
            else:
                break
            command = (
                f'{self.command_ffmpeg} -i "{self.source_path}/{file}" -vn '
                f'{self.bitrate_audio} {self.codec_audio} {self.time} '
                f'"{exit_file}"'
            )
            print('\nThe operation is being performed...')
            os.system(command)
            print('\nOperation successfully completed :)')
