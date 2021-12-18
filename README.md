# vimrc

#### 介绍
个人vimrc配置，主要用来C语言的单片机开发

#### vim版本
gvim8.2 x64
其他未测试

#### 依赖

python3.9
nodejs >= 10.12

#### 使用说明

1.  _vimrc里面有个工作目录切换，需要设置一下
2.  font目录下的字体安装一下
3.  color目录下的配色文件复制到你的对应目录
4.  plugManager目录下的plug.vim复制到你的对应目录，文件已做修改，更改了插件下载源，速度还是很快的
5.  使用自动拷贝脚本时先编辑修改到自己的路径
6.  打开gvim，安装coc LSP服务器
```
:CocInstall coc-clangd
```
7.  program文件夹下是备用程序
	- ctags可以在coc效果不好时使用

#### 其他建议安装
- `compile_commands.json`生成工具compiledb：
```
pip install compiledb 
```
- Cygwin64 安装gcc、g++、make等工具
- arm-none-eabi-gcc交叉编译器
