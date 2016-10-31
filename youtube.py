#!/usr/bin/env python
"""
Leeching music from youtube.

youtube-dl
batch-download option
youtube-dl just downloads the file as its native mp3 formt.
ffmpeg: can convert video files from one format to another.

Note: To manually download all a users videos, use:

"""

import argparse
import os
import sys
import subprocess
import time

VID_EXTENSIONS = tuple(['.mp4', '.mkv', '.webm'])
DL_FFMPEG = 'http://ffmpeg.gusari.org/statis/32bit/ffmpeg.static.32bit.latest.tar.gz'


def checkprograms():
    print('Checking for youtube-dl and FFMpeg...')
    time.sleep(3)

    os.system("cd /usr/local/bin")
    if not os.path.exists('/usr/local/bin/youtube-dl'):
        print("youtube-dl is not installed. Installing now.")
        time.sleep(3)
        os.system('sudo apt-get install youtube-dl')

        print('youtube-dl has been installed.')
        print('Now update youtube-dl...')
        os.system('sudo /usr/local/bin/youtube-dl -U')

    else:
        print('Checking for update to youtube-dl...')
        os.system('sudo /usr/local/bin/youtube-dl -U')

    if not os.path.exists('/usr/local/bin/ffmpeg'):
        print('FFMpeg is not installed. Installing now.')
        time.sleep(3)
        os.system('sudo wget {} -O /usr/local/bin/ffmpeg.tar.gz'.format(DL_FFMPEG))
        os.system('sudo tar -zxvf /sr/local/bin/*.tar.gz -C /usr/local/bin')
        os.system('sudo chmod a+x /sr/local/bin/ffmpeg')
        os.system('sudo chmod a+x /usr/local/bin/ffprobe')
        os.system('sudo rm ffmpeg.tar.gz')
        print('FFMpeg has been installed.')
    else:
        print('FFMpeg is already installed.')


def dl_userpicks():
    urls = []
    currenturl = '1'

    while currenturl != '':
        currenturl = raw_input('Enter URL (ENTER to begin downloading: ')
        if currenturl == '':
            break
        urls.append(currenturl)

    print ('done with queue entry. Downloading videos from Youtube:')
    time.sleep(2)
    return urls


def dl_userlist():
    urls = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            urls.append(line)
    return urls


def clean_filenames():
    remove_title_garbage()
    remove_spaces_in_filenames()
    clean_title_characters()
    trim_filenames()


def remove_spaces_in_filenames():
    for file in os.listdir('.'):
        if file.endswith(VID_EXTENSIONS):
            newname = file.replace(' ', '_')
            os.rename(file, newname)


def trim_filenames():
    for file in os.listdir('.'):
        if file.endswith(VID_EXTENSIONS):
            newname = file

            if file.startswith(' - ') or file.startswith('_-_'):
                newname = file[3:]
            elif file.startswith(' ') or file.startswith('_'):
                newname = file[1:]

            os.rename(file, newname)


def remove_title_garbage():
    for file in os.listdir('.'):
        if file.endswith(VID_EXTENSIONS) or file.endswith('.mp3'):
            newname = file.replace('[1080p]', '')
            newname = newname.replace('[song]', '')
            newname = newname.replace('(Song)', '')
            newname = newname.replace('[Song]', '')
            newname = newname.replace('(+Lyrics)', '')
            newname = newname.replace('_Lyrics', '')
            newname = newname.replace('MLP: FiM', 'MLP -')
            newname = newname.replace('MLP -FiM', 'MLP -')
            newname = newname.replace('My Little Pony - Friendship is Magic', 'MLP')
            newname = newname.replace('My_little_Pony', 'MLP')
            newname = newname.replace('| Music | ', '')
            newname = newname.replace('_ Music _ ', '')
            newname = newname.replace('| HD', '')
            newname = newname.replace('HD', '')
            newname = newname.replace(' _ HD', '')
            newname = newname.replace('(HQ)', '')
            newname = newname.replace('PMV', '')
            newname = newname.replace('AMV', '')
            newname = newname.replace('OST', '')
            newname = newname.replace('VIP', '')
            newname = newname.replace('M-V', '')
            newname = newname.replace('[WIP]', '')
            newname = newname.replace('[Electro]', '')
            newname = newname.replace('[HOUSE]', '')
            newname = newname.replace('[Dubstep]', '')
            newname = newname.replace('[Now_on_iTunes!]', '')
            newname = newname.replace('[EUROBEAT]', '')
            newname = newname.replace('[Hardstyle]', '')
            newname = newname.replace('[Drum_and_Bass]', '')
            newname = newname.replace('[Explicit]', '')
            newname = newname.replace('FULL VERSION', '')
            newname = newname.replace('full version', '')
            newname = newname.replace('full_version', '')
            newname = newname.replace('(video version)', '')
            newname = newname.replace('(Ultra Music)', '')
            newname = newname.replace('EPILEPSY_WARNING!', '')
            newname = newname.replace('EPILEPSY_WARNING', '')
            newname = newname.replace('[OFFICIAL]', '')
            newname = newname.replace('[OFFICIAL VIDEO]', '')
            newname = newname.replace('(Official_Video)', '')
            newname = newname.replace('(Official Video)', '')
            newname = newname.replace('(Official videoclip)', '')
            newname = newname.replace('(Official Music Video)', '')
            newname = newname.replace('(Official Video HQ)', '')
            newname = newname.replace('(Out Now)', '')
            newname = newname.replace('Music Video', '')
            newname = newname.replace('[Chiptune_8-bit]', '')
            newname = newname.replace('[]', '')

            newname = newname.replace(' .mp4', '.mp4')
            newname = newname.replace('_.mp4', '.mp4')
            newname = newname.replace('_.mp3', '.mp3')
            newname = newname.replace('_.mp3', '.mp3')
            newname = newname.replace('..', '.')
            os.rename(file, newname)


def clean_title_characters():
    for file in os.listdir('.'):
        if file.endswith(VID_EXTENSIONS):
            newname = file.replace('(', '[')
            newname = newname.replace(')', ']')
            newname = newname.replace('\'', '')
            newname = newname.replace(',', '')
            newname = newname.replace('!', '')
            newname = newname.replace('&', 'x')
            os.rename(file, newname)


def download_urls(urls):
    for URL in urls:
        #  os.system('youtube-dl --max-quality --o "%(title)s.%(ext)s" {}'.format(i))

        COMMAND = [
            'youtube-dl',
            '--no-playlist',
            '--o', '%(title)s.%(ext)s',
            URL]

        # Extra options
        # '--newline',
        # '--verbose',
        # '-f', 'bestaudio',
        # '--extract-audio',
        # '--o', '\"%(title)s.%(ext)s\"',
        # '--max-quality',

        # only get the best audio: -f bestaudio
        p = subprocess.Popen(COMMAND, stdin=subprocess.PIPE)
        p.wait()


def get_video_list():
    downloaded = []

    for file in os.listdir('.'):
        if file.endswith(VID_EXTENSIONS):
            downloaded.append(file)
    return downloaded


def extract_audio(filelist, audioformat):
    print ('Now converting videos: ')
    time.sleep(2)

    for _file in filelist:
        print('Trying to convert {}'.format(_file))
        dot = _file.find('.')
        newname = _file[:dot]
        #  os.system('ffmpeg -i {} {}.mp3'.format(x, x))
        #  fname = x.replace(' ', '')
        os.system('ffmpeg -i {} {}.{}'.format(_file, newname, audioformat))


def cleanup():
    print ('Finished converting. Cleaning up: ')
    time.sleep(3)

    for file in os.listdir('.'):
        if file.endswith('.mp3'):
            for ext in VID_EXTENSIONS:
                # Only delete if the video counterpart exists!
                vid = file.replace('.mp3', ext)
                if os.path.exists(vid):
                    #  os.system('rm ' + file)
                    os.remove(vid)  # This is better.


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Wrapper for youtube-dl to streamline extraction of videos and music.")

    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Show more explicit info on program activity.")
    parser.add_argument('-i', '--info', action='store_true',
                        help="Bypass downloading, just show info for each video.")
    parser.add_argument('-l', '--list', type=str,
                        help="Download a pre-made text file of urls.")
    parser.add_argument('-a', '--audio', type=str, choices=['wav', 'mp3'],
                        help="Extract the audio from the video(s)")
    args = parser.parse_args()

    if args.verbose:
        print('Verbose mode ON!')

    if args.info:
        print('Video info ON!')

    if args.audio:
        print('Extracting audio to {}'.format(args.audio))
    else:
        print('Just downloading videos.')

    if args.list:
        print('User passed in list-file {}'.format(args.list))
        if os.path.exists(args.list):
            print('File exists!')
        else:
            print('File {} does not exist!')
            exit()

    exit()
    if args.list == 'userlist':
        urls = dl_userlist()
    else:
        urls = dl_userpicks()

    download_urls(urls)

    clean_filenames()

    print('Finished downloading queue. Finding downloaded videos: ')
    downloaded = get_video_list()

    #  print('here are the found files: ')
    #  print('[{}]'.format('\n').join(map(str, downloaded)))

    if format != 'vid':
        extract_audio(downloaded, format)
        cleanup()
