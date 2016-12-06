from conf import *
import os
from subprocess import call


def main():
    cmd = """
        cd %s;
        virtualenv --no-site-packages venv;
        source venv/bin/activate;
        pip install -r requirements.txt;


    """ % (ROOT_ABS_FOLDER,)
    call([cmd], shell=True)
    pass

if __name__ == "__main__":
    main()
