##!/usr/bin/python3
#
import shutil
import os

#vim配置文件路径
default_vimrc="D:/Program Files/Vim/_vimrc"
default_colorsDir="D:/Program Files/Vim/vim82/colors"
default_plugManagerDir="D:/Program Files/Vim/vim82/autoload"
default_ctagsTo="D:/Program Files/Vim/vim82"
#本地上传仓库文件位置
# default_vimrcGitee="D:/WorkSpace/Gitee/vimrc/vimrc/_vimrc"
# default_colors1="D:/WorkSpace/Gitee/vimrc/colors/molokai.vim"
# default_colors2="D:/WorkSpace/Gitee/vimrc/colors/onedark.vim"
# default_colors3="D:/WorkSpace/Gitee/vimrc/colors/seoul256.vim"
# default_plugManagerGitee="D:/WorkSpace/Gitee/vimrc/plugManager/plug.vim"
default_vimrcGitee="./vimrc/_vimrc"
default_colors1="./colors/molokai.vim"
default_colors2="./colors/onedark.vim"
default_colors3="./colors/seoul256.vim"
default_plugManagerGitee="./plugManager/plug.vim"
default_ctags="./ctags/ctags58/ctags.exe"


def loop_main(key):
    if not os.path.isfile(default_vimrc):
        print("vim安装路径错误")
        return
    if not os.path.isfile(default_vimrcGitee):
        print("本地仓库路径错误")
        return
    if(key1 == "1"):
        fpath1,fname1 = os.path.split(default_vimrc)
        shutil.copy(default_vimrcGitee,fpath1)
        print("拷贝_vimrc: ",default_vimrcGitee,"==>",fpath1,"...")

        shutil.copy(default_colors1,default_colorsDir)
        shutil.copy(default_colors2,default_colorsDir)
        shutil.copy(default_colors3,default_colorsDir)
        print("拷贝主题: ",default_colors1,"==>",default_colorsDir,"...")
        print("拷贝主题: ",default_colors2,"==>",default_colorsDir,"...")
        print("拷贝主题: ",default_colors3,"==>",default_colorsDir,"...")

        shutil.copy(default_plugManagerGitee,default_plugManagerDir)
        print("拷贝插件管理器(已修改下载源): ",default_plugManagerGitee,"==>",default_plugManagerDir,"...")

        shutil.copy(default_ctags,default_ctagsTo)
        print("拷贝ctags",default_ctags,"==>",default_ctagsTo,"...")

    elif(key1 == "2"):
        fpath1,fname1 = os.path.split(default_vimrcGitee)
        shutil.copy(default_vimrc,fpath1)
        print("拷贝_vimrc: ",default_vimrc,"==>",fpath1,"...")
    # elif(key1 == "3"):
        # print("333")
    else:
        print("exit...")

print("--------------------------------------")
print("----按下数字键选择功能----------------")
print("----适用于：win10---------------------")
print("----* 先安装font/VeraMono.ttf字体文件-\n")
print("< 1 >使用默认路径配置vim")
print("< 2 >从默认路径拷贝配置文件到本地仓库")
# print("3.使用自定义路径配置vim")
print("* 其他按键退出")

key1 = input("请按键选择...\n")
loop_main(key1)



