import os

from .video import Video
from .check_files import files_exists


class Audio(Video):
    def __init__(self, input_midia_format: str, source_path: str, output_midia_format: str,
                 output_path, bitrate: str, time: str, qrange: int) -> None:
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

    def filter_files(self):
        files = list((files for files in os.listdir(self.source_path)
                      if self.input_midia_format in files.split('.')[-1]))
        if not files:
            return False
        return files[:self.qrange]

    def processing_file(self, files):
        for file in files:
            name_file, _ = os.path.splitext(file)

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
                self.execute(command)
            continue
