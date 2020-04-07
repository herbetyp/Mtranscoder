import os
import fnmatch
from time import sleep


class Video:

    def __init__(
        self, source_midia_format, source_path,
        destination_midia_format, destination_path, bitrate
    ):
        self.destination_midia_format = destination_midia_format
        self.source_midia_format = source_midia_format
        self.codec_video = '-c:v libx264'
        self.codec_audio = '-c:a aac'
        self.crf = '-crf 20'
        self.preset = '-preset ultrafast'
        self.bitrate_audio = bitrate
        self.command_ffmpeg = 'ffmpeg'
        self.time = ''
        self.source_path = source_path
        self.destination_path = destination_path

    def execut(self):
        files = (file for _, _, files in os.walk(self.source_path)
                 for file in files if self.source_midia_format in file)
        for file in files:
            name_file, extension_file = os.path.splitext(file)

            caption_path = name_file + '.srt'

            if os.path.isfile(caption_path):
                caption_input = f'-i "{caption_path}"'
                caption_map = '-c:s -map v:0 -map a -map 1:0'
            else:
                caption_input = ''
                caption_map = ''

            if '_NEW' in name_file:
                print(f'o arquivo "{file}" já EXISTE.')
                break

            exit_file = (
                f'{self.destination_path}/{name_file}_NEW.{self.destination_midia_format}'
            )

            command = (
                f'{self.command_ffmpeg} -i "{self.source_path}/{file}" {caption_input} '
                f'{self.codec_video} {self.crf} {self.preset} {self.codec_audio} '
                f'{self.bitrate_audio} {self.time} {caption_map} "{exit_file}" -y'
                f' &> /dev/null '
            )
            print('A operação está sendo executada...')
            os.system(command)
            print('\nOperação finalizada com sucesso :)')
