import os
import tempfile

def mkdirIfNotExsits(absPath):
    if not os.path.isdir(absPath):
        os.makedirs(absPath)

ROOT_ABS_FOLDER = os.path.dirname(os.path.abspath(__file__))

STATIC_FOLDER = "static"
STATIC_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, STATIC_FOLDER)
mkdirIfNotExsits(STATIC_ABS_FOLDER)

COMPOSITED_FOLDER = "composited"
COMPOSITED_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, COMPOSITED_FOLDER)
mkdirIfNotExsits(COMPOSITED_ABS_FOLDER)

FONT_FOLDER = "fonts"
FONT_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, FONT_FOLDER)
mkdirIfNotExsits(FONT_ABS_FOLDER)

UPLOAD_FOLDER = "upload_temp"
UPLOAD_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, UPLOAD_FOLDER)
mkdirIfNotExsits(UPLOAD_ABS_FOLDER)


def makeTempFileName():
    return next(tempfile._get_candidate_names())

