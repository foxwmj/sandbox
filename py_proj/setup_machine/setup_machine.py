import os
import csv
from fabric.api import run, settings, env


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

def do_setup_machine():
    config_machine()
    run('ls -A')
    #run('dir')
