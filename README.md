# vimrc使用说明

## 介绍
- 个人vimrc配置，主要用来C语言的单片机开发
- 适用于：
	- c/c++
	- markdown
	- python 

- vim版本
gvim8.2 x64, 其他未测试

## 依赖

- python3.9
- nodejs >= 10.12
- clangd
- ctags

## 使用说明
1.  配置可以打开默认工作目录，按需修改
2.  font目录下的字体安装一下
3.  color目录下的配色文件复制到你的对应目录
4.  plugManager目录下的plug.vim复制到你的对应目录，文件已做修改，更改了插件下载源，速度还是很快的。（安装失败的话多尝试几次看看）
5.  vim命令：安装coc LSP服务器
```
:CocInstall coc-clangd
:CocInstall coc-pyright
```
6.  下载[clangd](https://clangd.llvm.org/)， 添加bin目录到系统环境变量
7.  vim命令：安装vimspector的c调试器(这个需要从github拉取，没有科学上网大概率会失败，可以找不同时间段尝试或者连接手机热点尝试,或者手动下载文件后放到下载目录再执行此命令)
```
:VimspectorInstall --enable-c 
```
8. powershell命令：安装markdown预览组件
```
npm -g install instant-markdown-d
```
9. 下载`compile_commands.json`生成工具compiledb，powershell命令：
```shell
pip install compiledb 
```
10. 下载[Cygwin64](https://cygwin.com/index.html), 安装gcc、g++、make等工具，安装完成后把bin目录添加到环境变量

11. 下载[arm-none-eabi-gcc](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)交叉编译器，安装完成后把bin目录添加到环境变量

12. 解压ctags文件夹下的`ctags58.zip`，拷贝ctags.exe到vim可执行文件目录下

13. 把keil可执行文件目录添加到环境变量，用于调用keil编译和下载

## 一些自定义按键说明
	详细映射查看配置文件
- leader w/e：窗口调整
- leader s/d: 窗口跳转
- leader kb：使用keil编译
- leader kd: 使用keil下载
- Ctrl+P：markdown预览

## keil编码配置
- 屏蔽printf中文报错, option->c/c++(ac6)->Misc Controls，文本框填入：
```
-Wno-invalid-source-encoding
```

## 其他
- vscode文件夹下面有一个vscode 51的配置，需要安装c/c++插件并配置keil目录。因为sdcc和keil格式不兼容，暂时不使用gvim开发51
- WSL下安装nodejs
```
sudo apt install -y nodejs
//安装失败可以试试下面这个再安装
//curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
```
- vimspector插件安装--enable-c时提示权限问题：
```
sudo chown -R  username:username  filename
```
- makefile中添加win平台库路径示例：
```c
-I D:/GreenSoft/gcc-arm-none-eabi-5_4-2016q3-20160926-win32/arm-none-eabi/include
```

