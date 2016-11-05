#!/usr/bin/env python2

import youtube_dl

with youtube_dl.YoutubeDL({}) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])

def download(url):
    pass
