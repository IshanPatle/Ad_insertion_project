import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import subprocess
import atexit
import ffmpeg
import os


#-------------------------------------------------global values

root = r"C:\Users\admin\PycharmProjects\test2"
input_file = r"\2.mp4"
out_file = r"\out.webm"
out = r"\output_gen_file"
video = ffmpeg_streaming.input(root+input_file)

#-------------------------------------------------video manipulation functions
def convert_mp4():
    command = 'ffmpeg -i ' + input_file + ' ' + out_file
    subprocess.run(command)


def video_to_dash():
    dash = video.dash(Formats.h264())
    dash.auto_generate_representations()
    dash.output(r'C:\Users\admin\PycharmProjects\test2\dash.mpd')

    _144p  = Representation(Size(256, 144), Bitrate(95 * 1024, 64 * 1024))
    _240p  = Representation(Size(426, 240), Bitrate(150 * 1024, 94 * 1024))
    _360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
    _1080p = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))
    _2k    = Representation(Size(2560, 1440), Bitrate(6144 * 1024, 320 * 1024))
    _4k    = Representation(Size(3840, 2160), Bitrate(17408 * 1024, 320 * 1024))

    dash = video.dash(Formats.h264())
    dash.representations(_144p, _240p, _360p, _480p, _720p, _1080p, _2k, _4k)
    dash.output(r'C:\Users\admin\PycharmProjects\test2\dash.mpd')
    atexit.register(print, "Video conversion successfully!")


def video_to_hls():
    _144p = Representation(Size(256, 144), Bitrate(95 * 1024, 64 * 1024))
    _240p = Representation(Size(426, 240), Bitrate(150 * 1024, 94 * 1024))
    _360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
    _1080p = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))

    hls = video.hls(Formats.h264())
    hls.representations(_144p, _240p, _360p, _480p, _720p, _1080p)
    hls.output(root+out+'.m3u8')
    atexit.register(print, "Video conversion successfully!")

#--------------------------------------------------input parameters from user

print('''THIS IS A POC CODE FOR AD-INSERTION
Please enter you preference for video conversion 
Select:
1 - for DASH conversion
2 - for HLS conversion
''')
user_input = int(input("Please enter your preference: "))
if user_input == 1:
    print('You selected video conversion to DASH format. Please wait while the file is being converted...')
    video_to_dash()

if user_input == 2:
    print('You selected video conversion to HLS format. Please wait while the file is being converted...')
    video_to_hls()

