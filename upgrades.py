import errno
import os

FFMPEG_DL = 'http://ffmpeg.gusari.org/statis/32bit/ffmpeg.static.32bit.latest.tar.gz'
FFMPEG_DOWNLOAD = 'http://www.ffmpeg.org/download.html'
FFMPEG_RELEASES = 'http://www.ffmpeg.org/download.html#releases'
FFMPEG_GIT = 'https://github.com/FFmpeg/FFmpeg'
FFMPEG_PATH = '/opt/ffmpeg/bin/ffmpeg'
#  FFMPEG_PATH = '/usr/bin/ffmpeg'
#  FFMPEG_PATH = '/usr/local/bin/ffmpeg'
YOUTUBE_DL_PATH = '/usr/local/bin/youtube-dl'


def try_cmd(cmd):
    try:
        os.system(cmd)
    except IOError as e:
        if e[0] == errno.EPERM:
            print("You need root permissions to do this, laterz!")
            exit(1)


def youtube_dl():
    if not os.path.exists(YOUTUBE_DL_PATH):
        print("youtube-dl is not installed. Installing now.")
        try_cmd('sudo apt-get install youtube-dl')

    # Update youtube-dl
    print('Checking for update to youtube-dl...')
    try_cmd('sudo /usr/local/bin/youtube-dl -U')

    print('youtube-dl version:')
    try_cmd('youtube-dl --version')


def ffmpeg():
    print('ffmpeg version:')
    try_cmd('ffmpeg -version')

    if not os.path.exists(FFMPEG_PATH):
        print('FFMpeg is not installed. ')
        print('You should fix that...')
        #  print('Installing ffmpeg...')
        #  os.system('sudo wget {} -O /usr/local/bin/ffmpeg.tar.gz'.format(FFMPEG_DL))
    else:
        print('FFMpeg is already installed.')
