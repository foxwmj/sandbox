import os

ROOT_ABS_FOLDER = os.path.abspath(__file__)

STATIC_FOLDER = "static"
STATIC_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, STATIC_FOLDER)

COMPOSITED_FOLDER = os.path.join(STATIC_FOLDER, "composited")
COMPOSITED_ABS_FOLDER = os.path.join(ROOT_ABS_FOLDER, COMPOSITED_FOLDER)


