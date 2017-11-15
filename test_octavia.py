"""
  " Tests for octavia.py
  """

import octavia
import os

# Setup - make sure temp test dir exists and is empty.

# Teardown, make sure temp test dir gets cleaned out.


class Args():
    def __init__(self):
        self.channel_name = False
        self.format = 'mp4'
        self.dir = os.curdir + '/testing/'


""" Tests for get_user_picks() """
# This requires user input, how to test?


def test_parse_user_list():
    f = 'testing/1short.txt'
    vids = octavia.parse_user_list(f)
    assert len(vids) == 1
    assert vids[0] == 'https://www.youtube.com/watch?v=lHBytHVEyAE'


""" Tests for download_urls(urls, _format) """


def test_download_url_mkv():
    # This should result in an mkv being downloaded
    args = Args()
    f = args.dir + "When I'm Citizen.mkv"
    url = 'https://www.youtube.com/watch?v=BoaG30dJa7E'
    octavia.download_urls([url], args)
    assert os.path.exists(f)
    os.remove(f)


def test_download_url_mp4():
    # This should result in an mp4 being downloaded (As of 11/15/17)
    args = Args()
    f = args.dir + "Cheese Scepter.mp4"
    url = 'https://www.youtube.com/watch?v=lHBytHVEyAE'
    octavia.download_urls([url], args)
    assert os.path.exists(f)
    os.remove(f)


# 1 valid url, any format

# 1 valid url, mp4 format
# 1 invalid url, 1 valid url - 1 found in temp folder
# list of really short urls, all download

""" Tests for get_video_list() """

# 1 mp4
# 1 mpeg
# 1 mkv
# 1 avi
# 1 of each: mp4, mpeg, mkv, avi

""" Tests for extract_audio(filelist, audioformat) """
# mp4 -> mp3
# mpeg -> mp3
# mkv -> mp3
# avi -> mp3
# mp4 -> wav
# mpeg -> wav
# mkv -> wav
# avi -> wav


""" Tests for ensure_dir(_dir) """
# Test making a directory

""" Tests for cleanup() """
# List of 2 dirty files.
