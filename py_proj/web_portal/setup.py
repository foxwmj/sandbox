from conf import *
import os
from subprocess import call


def main():

    cmd = """init:
\tcd %s;
\tvirtualenv --no-site-packages venv;
\tsource %s/venv/bin/activate;
\tinstall -r requirements.txt;
""" % (ROOT_ABS_FOLDER, ROOT_ABS_FOLDER)

    print cmd

    makefile = os.path.join(ROOT_ABS_FOLDER, "Makefile")
    with open(makefile, "w") as mf:
        mf.write(cmd)


    #call([cmd], shell=True)

if __name__ == "__main__":
    main()
