#本地上传仓库文件位置
#vim配置文件路径
source_vimrc="D:/WorkSpace/Gitee/vimrc/vimrc/_vimrc"
target_vimrc="D:/Program Files/Vim"
cp "$source_vimrc" "$target_vimrc"

source_color="D:/WorkSpace/Gitee/vimrc/colors"
target_color="D:/Program Files/Vim/vim82"
cp -r "$source_color" "$target_color"

source_plug="D:/WorkSpace/Gitee/vimrc/plugManager/plug.vim"
target_plug="D:/Program Files/Vim/vim82/autoload"
cp -r "$source_plug" "$target_plug"
