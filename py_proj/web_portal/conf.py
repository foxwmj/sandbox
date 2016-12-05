import os
import tempfile

ROOT_ABS_FOLDER = os.path.dirname(os.path.abspath(__file__))

STATIC_FOLDER = "static"
STATIC_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, STATIC_FOLDER)

COMPOSITED_FOLDER = "composited"
COMPOSITED_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, COMPOSITED_FOLDER)

FONT_FOLDER = "fonts"
FONT_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, FONT_FOLDER)

UPLOAD_FOLDER = "upload_temp"
UPLOAD_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, UPLOAD_FOLDER)


def makeTempFileName():
    return next(tempfile._get_candidate_names())

