#!/usr/bin/env python
"""
Advanced wrapper for youtube-dl. Makes downloading and converting videos much easier.
"""
import argparse
import filenames
import os
import subprocess
import upgrades
import time


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
    urls = []
    with open(filename, 'r') as f:
        # We'll be pretty liberal in what we take - youtube-dl should do the error checking.
        for line in f:
            line = line.strip()
            if line.startswith('#'):       # It's a comment
                continue
            elif line.startswith('http'):  # This is a start...
                urls.append(line)
    return urls


def download_urls(urls, _format):
    for URL in urls:
        #  os.system('youtube-dl --max-quality --o "%(title)s.%(ext)s" {}'.format(i))

        filename = '%(title)s.%(ext)s'

        if _format == 'any':
            COMMAND = ['youtube-dl', '--restrict-filenames', '--no-playlist', '--o', str(filename), URL]
        if _format == 'mp4':
            COMMAND = ['youtube-dl', '--restrict-filenames', '--no-playlist', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
                       '--o', filename, URL]

        # Extra options
        # '--newline',
        # '--verbose',
        # '-f', 'bestaudio',
        # '--extract-audio',

        p = subprocess.Popen(COMMAND, stdin=subprocess.PIPE)
        p.wait()


def get_video_list():
    return [f for f in os.listdir('.') if f.endswith(VID_EXTENSIONS)]


def extract_audio(filelist, audioformat='mp3'):
    time.sleep(2)
    for f in filelist:
        print('Trying to convert {}'.format(f))
        # Assumes no dots in directory structure, and no dots in middle of video name.
        dot = f.find('.')
        newname = '{}.{}'.format(f[:dot], audioformat)

        cmd = ['ffmpeg', '-n', '-i', f, newname]
        print('newname = {}'.format(newname))
        print('cmd = {}'.format(cmd))
        #  os.system('ffmpeg -i {} {}.{}'.format(f, newname, audioformat))
        p = subprocess.Popen(cmd)
        p.wait()


def ensure_dir(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def cleanup():
    for file in os.listdir('.'):
        if file.endswith('.mp3'):
            for ext in VID_EXTENSIONS:

                # Only delete if the video counterpart exists!
                vid = file.replace('.mp3', ext)

                if os.path.exists(vid):
                    print('Deleting {}'.format(vid))
                    os.remove(vid)


def get_parser():
    parser = argparse.ArgumentParser(
        description="Wrapper for youtube-dl. Defaults to extracting audio from Youtube videos.")

    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Show more explicit info on the video processing.")
    parser.add_argument('-i', '--info', action='store_true',
                        help="Bypass downloading, just show info for each video.")
    parser.add_argument('-l', '--list', type=str,
                        help="Download a pre-made text file of urls.")
    parser.add_argument('-c', '--clean-filenames', action='store_true',
                        help="Trims out junk from the video and audio filenames.")
    parser.add_argument('-f', '--format', type=str, choices=['mp4'], default='any',
                        help="Force the video to the chosen file format.")
    parser.add_argument('-U', '--upgrade', action='store_true',
                        help="Check for the latest version of youtube-dl and install/upgrade, then exit.")
    parser.add_argument('-k', '--keep-vids', action='store_true',
                        help="Keeps the videos that have been converted to audio, the default is to remove them.")
    parser.add_argument('-d', '--dir', action="store", default=os.curdir,
                        help="The directory to download to.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--audio', type=str, choices=['wav', 'mp3'],
                       help="Extract audio from the video(s) to a specific format.")
    group.add_argument('-V', '--video-only', action='store_true',
                       help="Only download videos, do not convert to audio.")
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    if args.upgrade:
        upgrades.youtube_dl()
        exit()

    if args.list:
        urls = parse_user_list(args.list)
    else:
        urls = get_user_picks()

    if args.info:
        print('Video format is {}'.format(args.format))
        if args.verbose:
            for i, u in enumerate(urls):
                print('URL #{:3}: {}'.format(i, u))
    else:
        print('Downloading to {}'.format(args.dir))
        download_urls(urls, _format=args.format)

    vidlist = get_video_list()

    if not args.video_only:
        if args.audio:
            extract_audio(vidlist, args.audio)
        else:
            extract_audio(vidlist)

    if not args.keep_vids:
        cleanup()

    if args.clean_filenames:
        filenames.clean(filenames)
