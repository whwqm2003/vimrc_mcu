##!/usr/bin/python3
import shutil
import os
import sys

#本地vim安装位置，配置文件路径
default_vimrc_win="D:/Program Files/Vim/_vimrc"
default_colorsDir="D:/Program Files/Vim/vim82/colors"
default_plugManagerDir="D:/Program Files/Vim/vim82/autoload"
default_ctagsTo="D:/Program Files/Vim/vim82"
default_fullscreenTo=default_ctagsTo
#本地仓库文件位置
default_vimrcGitee="./vimrc/_vimrc"
default_colors1="./colors/molokai.vim"
default_colors2="./colors/onedark.vim"
default_colors3="./colors/seoul256.vim"
default_plugManagerGitee="./plugManager/plug.vim"
default_ctags="./ctags/ctags.exe"
default_fullscreen="./fullscreen/gvimfullscreen.dll"


def loop_main(key1,platform):
    if(platform == "win32"):
        if not os.path.isfile(default_vimrc_win):
            print("vim安装路径错误")
            return
        if not os.path.isfile(default_vimrcGitee):
            print("本地仓库路径错误")
            return
#    if(platform == "linux"):
#        print("platform is linux")

    if(key1 == "1"):
        if(platform == "win32"):
            fpath1,fname1 = os.path.split(default_vimrc_win)
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

            shutil.copy(default_fullscreen,default_fullscreenTo)
            print("拷贝全屏组件",default_fullscreen,"==>",default_fullscreenTo,"...")

        if(platform == "linux"):
            home_dir = os.environ['HOME']
            shutil.copy(default_vimrcGitee,home_dir)
            os.rename(home_dir+"/_vimrc",home_dir+"/.vimrc")
            print("拷贝.vimrc: ",default_vimrcGitee,"==>",home_dir,"...")
            
            if os.path.isdir("/usr/share/vim/vim81"):
                linux_vim_install_dir = "/usr/share/vim/vim81"
                print("vim install dir:",linux_vim_install_dir)
            elif os.path.isdir("/usr/share/vim/vim82"):
                linux_vim_install_dir = "/usr/share/vim/vim82"
                print("vim install dir:",linux_vim_install_dir)
            else:
                print("can't find vim install dir")
                return

            autoload_dir_plug = linux_vim_install_dir+"/autoload"
            shutil.copy(default_plugManagerGitee,autoload_dir_plug)
            print("拷贝插件管理器(已修改下载源): ",default_plugManagerGitee,"==>",autoload_dir_plug,"...")

            shutil.copy(default_colors1,linux_vim_install_dir+"/colors")
            shutil.copy(default_colors2,linux_vim_install_dir+"/colors")
            shutil.copy(default_colors3,linux_vim_install_dir+"/colors")
            print("拷贝主题: ",default_colors1,"==>",linux_vim_install_dir+"/colors","...")
            print("拷贝主题: ",default_colors2,"==>",linux_vim_install_dir+"/colors","...")
            print("拷贝主题: ",default_colors3,"==>",linux_vim_install_dir+"/colors","...")
    elif(key1 == "2"):
        if(platform == "win32"):
            fpath1,fname1 = os.path.split(default_vimrcGitee)
            shutil.copy(default_vimrc_win,fpath1)
            print("拷贝_vimrc: ",default_vimrc_win,"==>",fpath1,"...")
        if(platform == "linux"):
            home_dir = os.environ['HOME']
            if(os.path.isfile(home_dir+"/.vimrc")):
                fpath1,fname1 = os.path.split(default_vimrcGitee)
                shutil.copy(home_dir+"/.vimrc",fpath1)
                os.remove(default_vimrcGitee)
                os.rename(fpath1+"/.vimrc",fpath1+"/_vimrc")
                print("拷贝.vimrc: ",home_dir,"/.vimrc","==>",fpath1,"...")
            else:
                print("~/.vimrc不存在!!")
            
    # elif(key1 == "3"):
        # print("333")
    else:
        print("exit...")

vim_platform = sys.platform
print("vim配置脚本: 按下数字键选择功能. 适用于: win32/linux.")
print("先手动安装font/VeraMono.ttf字体文件, 本机平台: "+vim_platform)
print("< 1 > 使用默认路径配置vim")
print("< 2 > 从默认路径拷贝配置文件到本地仓库")
# print("3.使用自定义路径配置vim")
print("<其他> 退出")

key1 = input("请按键选择...\n")
loop_main(key1,vim_platform)



