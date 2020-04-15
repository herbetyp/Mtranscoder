import argparse
import os
import sys


# Defines arguments and parameters passed via cli
def args(args: list) -> dict:
    parser = argparse.ArgumentParser(description='Mtranscoder')

    parser.add_argument('-I', action='store', required=True, default='',
                        choices=['mp4', 'mkv', 'wmv', 'avi', 'flv', 'mov', 'webm',
                                 'wma', 'vob', 'mp3', 'ogg', 'flac', 'aac', '3gp'],
                        help='- source media format')

    parser.add_argument('-i', action='store', required=True,
                        default=os.path.realpath(os.curdir),
                        help='- source media path')

    parser.add_argument('-O', action='store', required=False, default='',
                        choices=['mp4', 'mkv', 'wmv', 'avi', 'flv', 'mov', 'webm',
                                 'wma', 'vob', 'mp3', 'ogg', 'flac', 'aac', '3gp'],
                        help='- output media format')

    parser.add_argument('-o', action='store', required=False,
                        default='',
                        help='- output media path')

    parser.add_argument('-b', action='store', default='', required=False,
                        help='- audio bitrate')

    parser.add_argument('-t', action='store', required=False, nargs=2,
                        default='', help='- media time')

    parser.add_argument('-r', action='store', required=False, default=9999,
                        type=int, help='- defined a range for the files')

    args = parser.parse_args()
    return args


args = args(sys.argv)
