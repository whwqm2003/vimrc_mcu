#vim配置文件路径
source="D:/Program Files/Vim/_vimrc"
#本地上传仓库文件位置
target="D:/WorkSpace/Gitee/vimrc/vimrc"
echo "$source"
echo "$target"
cp "$source" "$target"

read
