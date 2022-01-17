# vimrc

#### 介绍
个人vimrc配置，主要用来C语言的单片机开发

#### vim版本
gvim8.2 x64
其他未测试

#### 依赖

- python3.9
- nodejs >= 10.12
- clangd

#### 使用说明
1.  _vimrc里面有个工作目录切换，需要设置一下
2.  font目录下的字体安装一下
3.  color目录下的配色文件复制到你的对应目录
4.  plugManager目录下的plug.vim复制到你的对应目录，文件已做修改，更改了插件下载源，速度还是很快的
5.  使用自动拷贝脚本时先编辑修改到自己的路径
6.  安装coc LSP服务器
```
:CocInstall coc-clangd
```
7.  下载`clangd`, 添加bin目录到系统环境变量
8.  安装vimspector的c调试器(这个需要从github拉取，没有科学上网大概率会失败，可以找不同时间段尝试或者连接手机热点尝试)
```
:VimspectorInstall --enable-c 
```
9. 安装markdown预览组件
```
npm -g install instant-markdown-d
```

#### 其他 
- program文件夹下是备用程序
	- ctags可以在coc效果不好时使用
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

#### 一些自定义按键说明
	详细映射查看配置文件
- leader w/e：窗口调整
- leader s/d: 窗口跳转
- leader kb：使用keil编译
- leader kd: 使用keil下载
- Ctrl+P：markdown预览
#### 其他安装
- `compile_commands.json`生成工具compiledb：
```
pip install compiledb 
```
- Cygwin64 安装gcc、g++、make等工具
- arm-none-eabi-gcc交叉编译器


