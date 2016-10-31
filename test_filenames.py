import filenames

"""
Tests for clean_filelist(filelist)
"""

"""
Tests for clean
"""


def test_clean_uglyfile1():
    t = '_The Smile_ Song[HD]..mp3'
    expected = 'The Smile Song.mp3'
    assert filenames.clean(t) == expected


def test_clean_uglyfile2():
    t = '_The    Smile,_ Song(OFFICIAL) [HD]..mp3'
    expected = 'The Smile Song.mp3'
    assert filenames.clean(t) == expected


"""
Tests for rm_spaces
"""


def test_rm_spaces_title():
    t = 'The Smile Song'
    expected = 'The_Smile_Song'
    assert filenames.rm_spaces(t) == expected


def test_rm_spaces_filename():
    t = 'The Smile Song.mp3'
    expected = 'The_Smile_Song.mp3'
    assert filenames.rm_spaces(t) == expected


"""
Tests for trim
"""


def test_trim_spaceatstart():
    t = ' The Smile Song'
    expected = 'The Smile Song'
    assert filenames.trim(t) == expected


def test_trim_spaceatend():
    t = 'The Smile Song '
    expected = 'The Smile Song'
    assert filenames.trim(t) == expected


def test_trim_filename_spaceatstart():
    t = ' The Smile Song.mp3'
    expected = 'The Smile Song.mp3'
    assert filenames.trim(t) == expected


def test_trim_filename_spaceatend():
    t = 'The Smile Song .mp3'
    expected = 'The Smile Song.mp3'
    assert filenames.trim(t) == expected


def test_trim_filename_space_afterext():
    t = 'The Smile Song.mp3 '
    expected = 'The Smile Song.mp3'
    assert filenames.trim(t) == expected


def test_trim_filename_ugly():
    t = ' - __ The Smile Song-_  _.mp3'
    expected = 'The Smile Song.mp3'
    assert filenames.trim(t) == expected


"""
Tests for rm_junk
"""


def test_rmjunk_easy():
    t = 'The Smile Song(AMV)'
    t = filenames.sanitize(t)  # Sanitize should be used first
    expected = 'The Smile Song'
    assert filenames.rm_junk(t) == expected


def test_rmjunk_variations():
    t = 'The Smile Song(FULL VERSION)[FULL VERSION]'
    t = filenames.sanitize(t)  # Sanitize should be used first
    expected = 'The Smile Song'
    assert filenames.rm_junk(t) == expected


def test_rmjunk_ugly():
    t = 'The Smile Song(1080p)[HD][FULL VERSION][lyrics](Out Now)'
    t = filenames.sanitize(t)  # Sanitize should be used first
    expected = 'The Smile Song'
    assert filenames.rm_junk(t) == expected


"""
Tests for correct_spacing(filename):
"""


def test_correctspacing_singles():
    t = 'The Smile Song'
    expected = 'The Smile Song'
    assert filenames.correct_spacing(t) == expected


def test_correctspacing_double():
    t = 'The  Smile Song'
    expected = 'The Smile Song'
    assert filenames.correct_spacing(t) == expected


def test_correctspacing_triple():
    t = 'The  Smile   Song'
    expected = 'The Smile Song'
    assert filenames.correct_spacing(t) == expected


"""
Tests for sanitize
"""


def test_sanitize_parens():
    t = '(The Smile Song)'
    expected = '[The Smile Song]'
    assert filenames.sanitize(t) == expected


def test_sanitize_underscores():
    t = 'The_Smile_Song'
    expected = 'The Smile Song'
    assert filenames.sanitize(t) == expected


def test_sanitize_slashes():
    t = r'The/Smile\Song'
    expected = 'The Smile Song'
    assert filenames.sanitize(t) == expected


def test_sanitize_slashes2():
    t = 'The/Smile\\Song'
    expected = 'The Smile Song'
    assert filenames.sanitize(t) == expected


def test_sanitize_exclamation():
    t = 'The Smile Song!'
    expected = 'The Smile Song'
    assert filenames.sanitize(t) == expected


def test_sanitize_ampersand():
    t = 'The Smile Song & Pinkie Pie'
    expected = 'The Smile Song x Pinkie Pie'
    assert filenames.sanitize(t) == expected


def test_sanitize_doubledot():
    t = 'The Smile Song..mp3'
    expected = 'The Smile Song.mp3'
    assert filenames.sanitize(t) == expected


"""
Tests for kw_cases(keyword):
"""


def test_kwcases():
    t = 'The Smile Song'
    expected = ['THE SMILE SONG', 'the smile song', 'The Smile Song']
    assert filenames.kw_cases(t) == expected


"""
Tests for get_keyword_combos(keyword)
"""


def test_kwcombos():
    t = 'The Smile Song'
    expected = [
        '[THE SMILE SONG]', '[the smile song]', '[The Smile Song]',
        '[THE_SMILE_SONG]', '[the_smile_song]', '[The_Smile_Song]',
    ]
    assert filenames.kw_combos(t) == expected
