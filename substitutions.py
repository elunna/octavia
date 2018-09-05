"""
These are junk terms that commonly occur:
Variations: parentheses/brackets, uppercase, lowercase, or Title Style.
And with spaces or underscores

Ex: 'song' can come as:
    [epilepsy warning], [EPILEPSY WARNING], [Epilepsy Warning]
    [epilepsy_warning], [EPILEPSY_WARNING], [Epilepsy_Warning]
    (epilepsy warning), (EPILEPSY WARNING), (Epilepsy Warning)
    (epilepsy_warning), (EPILEPSY_WARNING), (Epilepsy_Warning)

This should cover a LOT of the junk that occurs, and any more specific stuff can be added to
JUNK
"""

KEYWORDS = [
    '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
    '1080P',
    'AMV',
    'Audio',
    'Audio Only',
    'CHIPTUNE 8-BIT',
    'Cover',
    'Cover Art',
    'DRUM AND BASS',
    'DUBSTEP',
    'Drumstep',
    'ELECTRO',
    'EPILEPSY WARNING',
    'EUROBEAT',
    'EXPLICIT',
    'FULL VERSION',
    'Free DL',
    'HARDSTYLE',
    'HD',
    'HOUSE',
    'HQ',
    'HQ+lyrics',
    'LYRICS',
    'LYRICS ON SCREEN',
    'Lyric video',
    'M-V',
    'MV',
    'MUSIC VIDEO',
    'Monstercat Release',
    'new album',
    'Official Audio',
    'Official Full Stream',
    'OFFICIAL MUSIC VIDEO',
    'OFFICIAL VIDEO HQ',
    'OFFICIAL VIDEO',
    'OFFICIAL VIDEOCLIP',
    'OFFICIAL',
    'OST',
    'OUT NOW',
    'PMV',
    'SONG',
    'ULTRA MUSIC',
    'VIDEO VERSION',
    'VIP',
    'WIP',
    'With Lyrics',
]

JUNK = [
    '| MUSIC |',
    '_ Music _ ',
    '| HD',
    ' _ HD',
    'EPILEPSY_WARNING!',
    '+Lyrics',
    'now on iTunes!',
]

SUBS = {
    'MLP: FiM': 'MLP -',
    'MLP -FiM': 'MLP -',
    'My Little Pony - Friendship is Magic': 'MLP',
    'My_little_Pony': 'MLP',
}


SANITIZATIONS = {
    '_': ' ',   # More readable for humans and media libraries
    '(': '[',   # Parentheses aren't linux friendly
    ')': ']',
    '\\': ' ',  # Slashes are not filename friendly
    '/': ' ',   # Slashes are not filename friendly
    ',': '',
    '!': '',
    '&': 'x',   # Use x instead of &
    '..': '.',
}
