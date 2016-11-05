import os
import ytem

"""
Tests for download(url)
"""


def test_download_youtubevid():
    url = 'https://www.youtube.com/watch?v=m0efX3B51dU'
    title = 'Your facekau.mp4'
    ytem.download(url)
    assert os.path.exists(title)
