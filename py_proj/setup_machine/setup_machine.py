import os
import csv
from fabric.api import run, settings, env, sudo, cd
from fabric.contrib.files import exists
from fabric.contrib.console import confirm


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
    sudo("apt-get install exuberant-ctags")
    sudo("apt-get install tmux")
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
    run(G + "status -s -uno") # review changelist
    run(G + "checkout -b original_files")
    run(G + "commit -a -m 'original files'")
    run(G + "checkout master")
    run(G + "pull")

    #https://github.com/foxwmj/foxconfig.git

def install_vim8_build(uninstall=False):
    config_machine()

    if uninstall:
        #uninstall vim80 & install trusted vim74
        with settings(warn_only=True):
            sudo("dpkg -P vim")
            sudo("apt-get install vim vim-common vim-runtime vim-tiny")
    else:
        with settings(warn_only=True):
            sudo("apt-get install libncurses5-dev libgnome2-dev libgnomeui-dev \
                    libgtk2.0-dev libatk1.0-dev libbonoboui2-dev libcairo2-dev \
                    libx11-dev libxpm-dev libxt-dev python-dev python3-dev     \
                    ruby-dev lua5.1 lua5.1-dev git")
            sudo("apt-get install checkinstall")

            run("dpkg -l | grep vim")
            if not confirm("Remove vim vim-common vim-runtime vim-tiny???"):
                return

            sudo("dpkg -P vim vim-common vim-runtime vim-tiny")

            build_folder = "~/01_sandbox/0001_temp_build_vim"
            run("mkdir " + build_folder) 
            run("git clone https://github.com/vim/vim.git " + build_folder)
            with cd(build_folder):
                run("./configure --with-features=huge \
                    --enable-multibyte \
                    --enable-rubyinterp \
                    --enable-pythoninterp \
                    --with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu \
                    --enable-perlinterp \
                    --enable-luainterp \
                    --enable-gui=gtk2 --enable-cscope --prefix=/usr")
                run("make VIMRUNTIMEDIR=/usr/share/vim/vim80")
                sudo("make install")
                sudo("checkinstall")

                sudo("update-alternatives --install /usr/bin/editor editor /usr/bin/vim 1")
                sudo("update-alternatives --set editor /usr/bin/vim")
                sudo("update-alternatives --install /usr/bin/vi vi /usr/bin/vim 1")
                sudo("update-alternatives --set vi /usr/bin/vim")



def deploy_proj_A():
    config_machine()
    with settings(warn_only=True):
        work_folder = '~/01_sandbox/99_git_sandbox'
        proj_A_folder = os.path.join(work_folder, 'py_proj/web_portal')
        if not exists(work_folder ,verbose=True):
            run('git clone https://github.com/foxwmj/sandbox.git %s' % (work_folder, ))
            with cd(proj_A_folder):
                run('make setup')
        #run(r'[ -d ~/01_sandbox/99_git_sandbox ] && cd ~/01_sandbox/99_git_sandbox && git pull && python ~/01_sandbox/99_git_sandbox/setup.py')







    
