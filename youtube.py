#!/usr/bin/env python
import argparse
import filenames
import os
import subprocess
import time
import upgrades
"""
Advanced wrapper for youtube-dl. Makes downloading and converting videos much easier.
"""

VID_EXTENSIONS = tuple(['.mp4', '.mkv', '.webm', '.avi'])
TEMPDIR = './temp_youtube/'


def get_user_picks():
    """
    Let the user input links one at a time. Terminate by entering a blank entry.
    """
    urls = []
    while True:
        currenturl = raw_input('Video URL: ')
        if currenturl:
            urls.append(currenturl)
        else:
            break

    print ('Done with queue entry. Downloading videos:')
    return urls


def parse_user_list(filename):
    """
    Read the urls from the file and return as a list.
    """
    with open(filename, 'r') as f:
        # We'll be pretty liberal in what we take - youtube-dl should do the error checking.
        urls = []
        for line in f:
            line = line.strip()
            if line.startswith('http'):  # This is a start...
                urls.append(line)
        return urls


def download_urls(urls, _format):
    for URL in urls:
        #  os.system('youtube-dl --max-quality --o "%(title)s.%(ext)s" {}'.format(i))

        #  filename = '{}%(title)s.%(ext)s'.format(TEMPDIR),
        filename = TEMPDIR + r'%(title)s.%(ext)s'

        if _format == 'any':
            COMMAND = ['youtube-dl', '--no-playlist', '--o', str(filename), URL]
        if _format == 'mp4':
            COMMAND = ['youtube-dl', '--no-playlist', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
                       '--o', filename, URL]

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
    return [''.join([TEMPDIR, f])
            for f in os.listdir(TEMPDIR)
            if file.endswith(VID_EXTENSIONS)]


def extract_audio(filelist, audioformat):
    print ('Now converting videos: ')
    time.sleep(2)

    for _file in filelist:
        print('Trying to convert {}'.format(_file))
        # Assumes no dots in directory structure, and no dots in middle of video name.
        dot = _file.find('.')
        newname = _file[:dot]
        os.system('ffmpeg -i {} {}.{}'.format(_file, newname, audioformat))


def ensure_dir(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def cleanup():
    print ('Cleaning up filenames in {}: '.format(TEMPDIR))

    for file in os.listdir(TEMPDIR):
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
    parser.add_argument('-c', '--clean-filenames', action='store_true',
                        help="Trims out junk from the video and audio filenames.")
    parser.add_argument('-f', '--format', type=str, choices=['mp4'], default='any',
                        help="Force the video to the chosen file format.")
    parser.add_argument('-U', '--upgrade', action='store_true',
                        help="Check for the latest versions of youtube-dl and ffmpeg, and also install them if not present.")
    args = parser.parse_args()

    if args.upgrade:
        upgrades.youtube_dl()
        upgrades.ffmpeg()
        exit()

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

    if args.list:
        urls = parse_user_list(args.list)
    else:
        urls = get_user_picks()

    if args.info:
        print('Video info ON!')
        print('Video format is {}'.format(args.format))
        if args.verbose:
            for i, u in enumerate(urls):
                print('URL #{:3}: {}'.format(i, u))
    else:
        download_urls(urls, _format=args.format)
        print('Finished downloading queue.')

        if args.audio:
            downloaded = get_video_list()
            extract_audio(downloaded, format)
            cleanup(downloaded)

    if args.clean_filenames:
        print('Cleaning up filenames')
        filenames.clean()
