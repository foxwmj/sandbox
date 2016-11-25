PREPARE
    1) SVN 安装命令行
    2) Python
        a) python加入到环境变量



1) vim73\install.exe 管理员模式安装
2）fonts\ 所有字体安装
3) install\install.bat 管理员模式安装
    a) Install Bundels
    b) code_proj SVN :   https://mingjin-sandbox.googlecode.com/svn/branches/projs
4) 加入到环境变量PATH中  
    a) C:\Users\mingjinwu\code_projs\PY_projs
5) 改变popup_menu.reg里的路径， 运行install\popup_menu.reg


6) 安装Git,以便更新Vundle插件
    a) 安装完之后，公司proxy运行 git config --global http.proxy https://web-proxyhk.oa.com:8080

7) 运行:BundleInstall

Bundle Script
=======================
    Vundle安装插件有三种形式，一种是一个从官方移植的Vim Script,只需要在配置中写脚本的名字，比如：
    Bundle 'neocomplcache'
    第二种是指定一个github上的项目名，以作者/项目的形式：
    Bundle 'gmarikundle'
    最后还可以指定一个完整的git repos地址：
    Bundle 'git://git.wincent.com/command-t.git'
    将要安装的插件在配置文件中写好，最后执行：
    :BundleInstall
    就可以一键安装了。安装有问题可以按l键查看log。我在第一次安装时出现了“can't resolve proxy 'null' for https”的报警，调查发现是因为git启用了代理的原因，可以运行cmd：
    git config --global --unset http.proxy

