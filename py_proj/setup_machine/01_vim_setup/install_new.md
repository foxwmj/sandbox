# Windows VIM

---

## 前置条件
- 安装好python
- 安装git，curl，方便VIM更新Vundle
	- 安装完之后，公司proxy运行 git config --global http.proxy https://web-proxyhk.oa.com:8080
- 设置Windows不要隐藏文件，方便排查问题


## 安装步骤
- 安装VIM： vim73\install.exe （管理员模式安装）
- 安装字体： fonts\ 所有字体安装
- 注册VIM到右键菜单： 改变install\popup_menu.reg里的路径， 运行install\popup_menu.reg


## 配置VIM 插件
- Vundle地址配置:  修改_vimrc里的runtimepath
	- __注意：Windows下是用 单 \\分割__
```
set rtp+=d:\00_MJ_CODE\01_github_sandbox\py_proj\setup_machine\01_vim_setup\vundle_runtime_new\Vundle.vim
```
- Vundle插件安装地址配置： 修改_vimrc 
	- __注意：Windows下是用 双 \\\\分割__
```
call vundle#begin("d:\\00_MJ_CODE\\01_github_sandbox\\py_proj\\setup_machine\\01_vim_setup\\vundle_runtime_new")
```
- 在VIM里运行
```
:PluginInstall!    - installs plugins; append ! to update or just :PluginUpdate
```

 