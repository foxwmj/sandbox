import os
import csv
from fabric.api import run, settings, env, sudo
from fabric.contrib.files import exists


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
    #d = read_machine_spec_file(r"D:\sandbox\99_machine_info_no_version_control\machine_spec_qcould_161123.csv")
    d = read_machine_spec_file(r"D:\00_MJ_CODE\99_machine_info_no_version_control\machine_spec_qcould_161123.csv")
    env.host_string = d["host_string"]
    env.user = d["user"]
    env.key_filename = d["key_filename"]

# Setup 1
def do_setup_machine():
    config_machine()

    sudo("apt-get update")
    sudo("apt list --installed")
    sudo("apt-get install tree")
    sudo("apt-get install python2.7")
    sudo("apt-get install python-pip")
    sudo("apt-get install build-essential cmake")
    sudo("apt-get install python-dev python3-dev")
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

    run("mkdir -m 0700 ~/00_deployment")
    run("mkdir -m 0700 ~/01_sandbox")

def setup_foxconfig():
    config_machine()
    with settings(warn_only=True):
        run(r'[ ! -d ~/foxconfig.git ] && git clone --bare https://github.com/foxwmj/foxconfig.git ~/foxconfig.git')

    G = 'git --git-dir=$HOME/foxconfig.git --work-tree=$HOME '
    run(G + "pull")
    run(G + "status -s -uno") # review changelist
    run(G + "checkout -b original_files")
    run(G + "commit -a -m 'original files'")
    run(G + "checkout master")

    #https://github.com/foxwmj/foxconfig.git

def deploy_proj_A():
    config_machine()
    with settings(warn_only=True):
        work_folder = '~/01_sandbox/99_git_sandbox'
        proj_A_folder = os.path.join(work_folder, 'py_proj/web_portal')
        if not exists(work_folder ,verbose=True):
            run('clone https://github.com/foxwmj/sandbox.git %s' % (work_folder, ))
            with cd(proj_A_folder):
                run('make setup')
        #run(r'[ -d ~/01_sandbox/99_git_sandbox ] && cd ~/01_sandbox/99_git_sandbox && git pull && python ~/01_sandbox/99_git_sandbox/setup.py')







    
