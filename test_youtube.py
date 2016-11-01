import youtube

# Setup - make sure temp test dir exists and is empty.

# Teardown, make sure temp test dir gets cleaned out.

"""
Tests for get_user_picks()
"""
# This requires user input, how to test?

"""
Tests for parse_user_list(filename)
"""
# Empty file - empty list
# Just comments - empty list
# Just invalid links - empty list
# 1 valid link
# 2 valid links
# 3 valid links, in mix of invalid lines

"""
Tests for download_urls(urls, _format)
"""
# 1 valid url, any format
# 1 valid url, mp4 format
# 1 invalid url, 1 valid url - 1 found in temp folder
# list of really short urls, all download

"""
Tests for get_video_list()
"""
# 1 mp4
# 1 mpeg
# 1 mkv
# 1 avi
# 1 of each: mp4, mpeg, mkv, avi

"""
Tests for extract_audio(filelist, audioformat)
"""
# mp4 -> mp3
# mpeg -> mp3
# mkv -> mp3
# avi -> mp3
# mp4 -> wav
# mpeg -> wav
# mkv -> wav
# avi -> wav


"""
Tests for ensure_dir(_dir)
"""
# Test making a directory

"""
Tests for cleanup()
"""
# List of 2 dirty files.
