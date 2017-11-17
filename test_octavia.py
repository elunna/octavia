"""
  " Tests for octavia.py
  """

import octavia
import os
import shutil

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
    args = Args()
    args.format = 'mkv'
    f = args.dir + "When I'm Citizen.mkv"
    url = 'https://www.youtube.com/watch?v=BoaG30dJa7E'
    octavia.download_urls([url], args)
    assert os.path.exists(f)
    os.remove(f)


def test_download_url_mp4():
    args = Args()
    f = args.dir + "Cheese Scepter.mp4"
    url = 'https://www.youtube.com/watch?v=lHBytHVEyAE'
    octavia.download_urls([url], args)
    assert os.path.exists(f)
    os.remove(f)


def test_download_url_channel_name():
    args = Args()
    args.channel_name = True
    f = args.dir + "Unanimous Delivers_-_Cheese Scepter.mp4"
    url = 'https://www.youtube.com/watch?v=lHBytHVEyAE'
    octavia.download_urls([url], args)
    assert os.path.exists(f)
    os.remove(f)


""" Tests for run_cmd(cmd_list) """


def test_runcmdsuccess_touch():
    testfile = 'tempfile.xxx'
    result = octavia.run_cmd(['touch', testfile])
    assert result is True
    os.remove(testfile)  # Cleanup the file


def test_runcmdsuccess_touch_invalid_arg():
    result = octavia.run_cmd(['touch', '-xxx'])
    assert result is False


def test_runcmdsuccess_invalid_cmd_returneFalse():
    result = octavia.run_cmd(['twilicane'])
    assert result is False


""" Tests for get_video_list() """


def test_get_video_list():
    _dir = 'testing/vids'
    result = octavia.get_video_list(_dir)

    assert sorted(result) == [
        _dir + '/Cheese Scepter.mp4',
        _dir + "/When I'm Citizen.mkv"
    ]


""" Tests for extract_audio(filelist, audioformat) """
# todo
# mpeg -> mp3
# avi -> mp3
# mpeg -> wav
# avi -> wav


def test_extract_audio_mp4tomp3():
    f = 'testing/vids/Cheese Scepter.mp4'
    audio = f[:-3] + 'mp3'
    octavia.extract_audio([f], audioformat='mp3')
    assert os.path.exists(audio)
    os.remove(audio)


def test_extract_audio_mp4towav():
    f = 'testing/vids/Cheese Scepter.mp4'
    audio = f[:-3] + 'wav'
    octavia.extract_audio([f], audioformat='wav')
    assert os.path.exists(audio)
    os.remove(audio)


def test_extract_audio_mkvtomp3():
    f = "testing/vids/When I'm Citizen.mkv"
    audio = f[:-3] + 'mp3'
    octavia.extract_audio([f], audioformat='mp3')
    assert os.path.exists(audio)
    os.remove(audio)


def test_extract_audio_mkvtowav():
    f = "testing/vids/When I'm Citizen.mkv"
    audio = f[:-3] + 'wav'
    octavia.extract_audio([f], audioformat='wav')
    assert os.path.exists(audio)
    os.remove(audio)


""" Tests for ensure_dir(_dir) """


def test_ensuredir_exists():
    testdir = 'some_random_directory_xxx1234'
    octavia.ensure_dir(testdir)
    assert os.path.isdir(testdir)

    if os.path.isdir(testdir):
        shutil.rmtree(testdir)


""" Tests for cleanup() """


def test_cleanup():
    _dir = 'testing/'
    f1 = _dir + 'test.mp4'
    f2 = _dir + 'test.mp3'
    open(f1, 'a').close()
    open(f2, 'a').close()
    assert os.path.exists(f1)
    assert os.path.exists(f2)
    octavia.cleanup(_dir)
    assert not os.path.exists(f1)
    os.remove(f2)
