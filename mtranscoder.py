#!/usr/bin/python3
# -*- coding: utf-8 -*-

from libs.video import Video
from libs.audio import Audio
from libs.args import args

audio = ['mp3', 'ogg', 'aac', 'flac']
video = ['mp4', 'mkv', 'wmv', 'avi']

if args.O == '':
    args.O = args.I
if args.b != '':
    args.b = '-b:a ' + args.b

# Executed from for video
if args.I in video and args.O in video:
    video = Video(args.I, args.i, args.O, args.o, args.b, args.t)
    video.execute()
    exit()

# Executed from for video/audio or audio
elif args.I in audio or args.I in video and args.O in audio:
    audio = Audio(args.I, args.i, args.O, args.o, args.b, args.t)
    audio.execute()
    exit()
