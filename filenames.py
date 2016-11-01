import os
import substitutions
from youtube import TEMPDIR


def cleanlist(filelist):
    """
    Thoroughly cleans a list of filenames.
    """
    for f in filelist:
        newname = clean(f)
        os.rename(f)


def clean(filename):
    """
    We sanitize characters in the filename, remove junk characters from the beginning and end,
    and remove common junk that appears in Youtube video titles(there's a lot.)
    """
    # Just process the basename of the file.
    newname = os.path.basename(filename)
    #  newname = rm_spaces()
    newname = sanitize(newname)
    newname = trim(newname)
    newname = rm_junk(newname)
    newname = correct_spacing(newname)
    return newname


def rm_spaces(filename):
    """
    Replaces all spaces with underscores in a filename.
    """
    return filename.replace(' ', '_')


def correct_spacing(filename):
    newname, ext = os.path.splitext(filename)
    newname = ' '.join(newname.split())
    return ''.join([newname.strip(), ext.strip()])


def trim(filename):
    """
    Trims junk characters from the beginning and of a filename.
    This removes the file extension if present, and reattaches when the filename is returned.
    """
    JUNK = (' ', '-', '_')
    newname, ext = os.path.splitext(filename)
    while newname.startswith(JUNK):
        newname = newname[1:]

    while newname.endswith(JUNK):
        newname = newname[:-1]

    return newname + ext.strip()


def rm_junk(filename):
    """
    Takes a base filename (or string) and removes YouTube junk that commonly appears in titles.
    Uses the KEYWORDS list in substitutions to generate common variations that can appear.
    """
    for k in substitutions.KEYWORDS:
        for c in kw_combos(k):
            filename = filename.replace(c, '')
    return filename


def sanitize(filename):
    """
    Takes a base filename (or string) and removes potentially harmful or disruptive characters.
    """
    for k, v in substitutions.SANITIZATIONS.items():
        filename = filename.replace(k, v)
    return filename


def kw_cases(keyword):
    """
    Returns 3 variations on a passed keyword string: uppercase, lowercase, and Title Case.
    """
    return [keyword.upper(), keyword.lower(), keyword.title()]


def kw_combos(keyword):
    """
    Generate common variations on junk keywords that can appear.
    Uses different cases for the inner portion.
    We only need to check brackets since the sanitization should convert all () to [].
    """
    cases = kw_cases(keyword)
    underlined = [rm_spaces(c) for c in cases]
    cases.extend(underlined)

    # Make bracket variations
    return ['[' + c + ']' for c in cases]
