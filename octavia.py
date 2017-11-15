#!/usr/bin/env python3
"""
  " Advanced wrapper for youtube-dl. Makes downloading and converting videos much easier.
  """
import argparse
import filenames
import os
import subprocess
import upgrades
import time


VID_EXTENSIONS = tuple(['.mp4', '.mkv', '.webm', '.avi'])


def get_user_picks():
    """ Let the user input links one at a time. Terminate by entering a blank entry. """
    urls = []
    while True:
        currenturl = input('Video URL: ')
        if currenturl:
            urls.append(currenturl)
        else:
            break

    print ('Done with queue entry. Downloading videos:')
    return urls


def parse_user_list(filename):
    """ Read the urls from the file and return as a list. """
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


def download_urls(urls, args):
    """ Performs the actual downloading and formatting of the filenames. """
    for URL in urls:
        if args.channel_name:
            filename = args.dir + '/%(uploader)s_-_%(title)s.%(ext)s'
        else:
            filename = args.dir + '/%(title)s.%(ext)s'

        options = [
            'youtube-dl',
            #'--restrict-filenames',
            '--no-playlist',
            # '-f', "'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'",
            #  '--dump-user-agent',
            #  '--no-part',
            #  '--quiet',
            #  '--no-overwrites',
            #  '--ignore-errors',
            # '--o',
        ]

        # if args.format == 'mp4':
            # options.extend(['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'])

        options.extend(['--o', filename, URL])

        run_cmd(options)


def run_cmd(cmd_list):
    """ Takes a list of commands and arguments to run. Tests if a shell command ran successfully. Returns True if successful,
        and False it it failed or the command doesn't exist.
    """
    try:
        result = subprocess.call(cmd_list)
        if result == 0:
            return True
        else:
            return False
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False


def get_video_list(_dir):
    """ Retrieves a list of all videos in the specified directory. """
    return ['/'.join([_dir, f]) for f in os.listdir(_dir) if f.endswith(VID_EXTENSIONS)]


def extract_audio(filelist, audioformat='mp3'):
    """ Converts each video in the filelist to the specified audio format. """
    time.sleep(2)

    for f in filelist:
        dot = f.rfind('.')  # Look for the dot from the right!
        newname = '{}.{}'.format(f[:dot], audioformat)

        cmd = ['ffmpeg', '-n', '-i', f, newname]
        p = subprocess.Popen(cmd)
        p.wait()


def ensure_dir(_dir):
    """ Makes sure the specified directory exists and creates it if it doesn't. """
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def cleanup(_dir):
    """ Deletes any video files it there is an existing mp3 counterpart. """
    for f in os.listdir(_dir):
        if f.endswith('.mp3'):
            for ext in VID_EXTENSIONS:

                # Only delete if the video counterpart exists!
                vid = _dir + '/' + f.replace('.mp3', ext)

                if os.path.exists(vid):
                    print('Deleting {}/{}'.format(_dir, vid))
                    os.remove(vid)


def get_parser():
    """ Builds and returns the command line argument parser. """
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
    parser.add_argument('-C', '--channel-name', action='store_true',
                        help="Prepend the channel name to the file(s).")
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


def main():
    """ Main entry point. """
    parser = get_parser()
    args = parser.parse_args()

    if args.upgrade:
        upgrades.youtube_dl()
        exit()

    if args.list:
        urls = parse_user_list(args.list)
    else:
        urls = get_user_picks()

    download_urls(urls, args=args)
    vidlist = get_video_list(_dir=args.dir)

    if not args.video_only:
        if args.audio:
            extract_audio(vidlist, args.audio)
        else:
            extract_audio(vidlist)

    if not args.keep_vids:
        cleanup(_dir=args.dir)

    if args.clean_filenames:
        filenames.clean(filenames)


if __name__ == "__main__":
    main()
