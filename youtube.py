#!/usr/bin/env python
import argparse
import os
import subprocess
import substitutions
import time
import upgrades

"""
Leeching music from youtube.

youtube-dl
batch-download option
youtube-dl just downloads the file as its native mp3 formt.
ffmpeg: can convert video files from one format to another.

Note: To manually download all a users videos, use:

"""

VID_EXTENSIONS = tuple(['.mp4', '.mkv', '.webm', '.avi'])


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
    """
    Clean out junk from the filename. Uses the substitution dictionary in substitutions. These
    entries are usually meaningless or captalized keywords.
    """
    for file in os.listdir('.'):
        if file.endswith(VID_EXTENSIONS) or file.endswith('.mp3'):
            newname = file
            for k, v in substitutions.SUBS.iteritems():
                newname = newname.replace(k, v)

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


def download_urls(urls, _format):
    for URL in urls:
        #  os.system('youtube-dl --max-quality --o "%(title)s.%(ext)s" {}'.format(i))

        if _format == 'any':
            COMMAND = ['youtube-dl', '--no-playlist', '--o', '%(title)s.%(ext)s', URL]
        if _format == 'mp4':
            COMMAND = ['youtube-dl', '--no-playlist', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
                       '--o', '%(title)s.%(ext)s', URL]

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

    if args.clean_filenames:
        print('Cleaning up filenames')
        clean_filenames()
    exit()

    print('Finished downloading queue. Finding downloaded videos: ')
    downloaded = get_video_list()

    #  print('here are the found files: ')
    #  print('[{}]'.format('\n').join(map(str, downloaded)))

    if format != 'vid':
        extract_audio(downloaded, format)
        cleanup()
