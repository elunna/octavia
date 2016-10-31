import os
import substitutions
from youtube import TEMPDIR


def clean():
    rm_junk()
    remove_spaces()
    sanitize()
    trim()


def remove_spaces(filelist):
    for f in filelist:
        newname = os.path.basename(f)
        newname = file.replace(' ', '_')
        os.rename(TEMPDIR + file, TEMPDIR + newname)

#  ' .mp4': '.mp4',
#  '_.mp4': '.mp4',
#  '_.mp3': '.mp3',
#  '_.mp3': '.mp3',


def trim(filelist):
    JUNK = (' ', '-', '_')
    for f in filelist:
        basename = os.path.basename(f)
        newname = os.path.splitext(basename)[0]
        while newname.startswith(JUNK):
            newname = file[1:]

        while newname.startswith(JUNK):
            newname = file[:-1]

        os.rename(f, TEMPDIR + newname)


def rm_junk(filelist):
    """
    Clean out junk from the filename. Uses the substitution dictionary in substitutions. These
    entries are usually meaningless or captalized keywords.
    """
    for f in filelist:
        newname = os.path.basename(f)
        for k, v in substitutions.SUBS.iteritems():
            newname = newname.replace(k, v)

        os.rename(f, TEMPDIR + newname)


def sanitize(filelist):
    for f in filelist:
        newname = os.path.basename(f)
        for k, v in substitutions.SANITIZATIONS:
            newname = newname.replace(k, v)
        os.rename(f, TEMPDIR + newname)
