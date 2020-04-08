import os

from .overwrite_file import file_exists


class Video:

    def __init__(
            self, input_midia_format, source_path, output_midia_format,
            output_path, bitrate, time):

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
        self.time = f'-ss {time[0]} -t {time[1]}'

    def execute(self):
        files = (file for _, _, files in os.walk(self.source_path)
                 for file in files if self.input_midia_format in file and '_NEW' not in file)

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
                f'{self.output_path}/{name_file}_NEW.{self.output_midia_format}'
            )
            if not file_exists(name_file, exit_file, self.output_midia_format):
                break
            else:
                ...
            command = (
                f'{self.command_ffmpeg} -i "{self.source_path}/{file}" {caption_input} '
                f'{self.codec_video} {self.crf} {self.preset} {self.codec_audio} '
                f'{self.bitrate_audio} {self.time} {caption_map} "{exit_file}" -y'
                f' &> /dev/null'
            )
            print('\nThe operation is being performed...')
            os.system(command)
            print('\nOperation successfully completed :)')
