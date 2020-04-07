#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import argparse
import os

from app.video import Video


def args(args):
    parser = argparse.ArgumentParser(description='Mtranscoder')
    parser.add_argument('-fi', action='store', required=True,
                        help='define the format of the input media')
    parser.add_argument('-i', action='store', required=False,
                        default=os.path.realpath(os.curdir),
                        help='define the path of the input media')
    parser.add_argument('-fo', action='store', required=False, default='',
                        help='define the format of the output media')
    parser.add_argument('-o', action='store',
                        default=os.path.realpath(os.curdir), required=False,
                        help='define the path of the output media')
    parser.add_argument('-ba', action='store',
                        default='', required=False,
                        help='define the audio bitrate')
    args = parser.parse_args()
    return args


args = args(sys.argv)

if args.fo == '':
    args.fo = args.fi

video = Video(args.fi, args.i, args.fo, args.o, args.ba)
print(video.__dict__)
video.execut()
