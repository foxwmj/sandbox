import os
import csv
from fabric.api import run, settings, env, sudo


def read_machine_spec_file(filename):
    '''read CSV file,to get machine spec'''
    reader = csv.reader(open(filename, 'r'))
    d = {}
    for k, v in reader:
        d.setdefault(k, v)
    print d
    return d

def config_machine():
    '''config machine info'''
    d = read_machine_spec_file("D:\sandbox\99_machine_info_no_version_control\machine_spec_qcould_161123.csv")
    env.host_string = d["host_string"]
    env.user = d["user"]
    env.key_filename = d["key_filename"]

# Setup 1
def do_setup_machine():
    config_machine()

    sudo("apt list --installed")
    sudo("apt-get install tree")
    sudo("apt-get install python2.7")
    sudo("apt-get install python-pip")
    sudo("pip install --upgrade pip")

# Setup 2
def setup_python_must_have():
    config_machine()

    sudo("pip install virtualenv")
    sudo("pip install Flask")
    sudo("pip install numpy")
    sudo("pip install pandas")

# Setup 3
def setup_sandbox():
    config_machine()

    sudo("mkdir -m 0700 ~/00_deployment")
    run("mkdir -m 0700 ~/01_sandbox")
    
