from threading import Thread
from itertools import count
from time import sleep
import sys


def progressbar(ffmpeg):
    print('\n')
    thread_ffmpeg = Thread(target=ffmpeg)
    progress = 0
    time = 4
    thread_ffmpeg.start()
    while True:
        for i in count(0):
            sys.stdout.write("\r")
            sys.stdout.flush()
            sys.stdout.write(f'[{progress}%] ')
            sys.stdout.write("█ "*(i+1))
            sys.stdout.flush()
            progress += 2
            sleep(time)
            if progress >= 10 <= 20:
                time = 8
            if progress > 20 <= 30:
                time = 16
            if progress > 30 <= 40:
                time = 32
            if progress > 40 <= 50:
                time = 64
            if progress > 50 <= 60:
                time = 128
            if progress > 60 <= 70:
                time = 128
            if progress > 70 <= 80:
                time = 128
            if progress > 80 <= 90:
                time = 256
            if progress > 90 < 100:
                time = 256
            if not thread_ffmpeg.is_alive():
                progress = 100
                sys.stdout.write("\r")
                sys.stdout.flush()
                sys.stdout.write(f'[{progress}%] ')
                print('\n\n# FINISHED #')
                break
        if not thread_ffmpeg.is_alive():
            break
        continue
