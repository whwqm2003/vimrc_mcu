# vimrc使用说明

## 介绍
- 个人vimrc配置，主要用来C语言的单片机开发, 优先更新win平台下的gvim环境
- 适用于：
	- c/c++
	- markdown
	- python 
	- 二进制文件(.bin)
- vim版本
gvim8.2 x64, 其他未测试
- 使用平台：
	- win10
	- ubuntu(测试)

## 依赖
- python3.9 64bit
- nodejs >= 10.12
- clangd
- ctags
- cygwin64
- 其他看使用说明。。。

## 使用说明
1. 安装nodejs
- win平台下安装，[下载链接](http://nodejs.cn/download/)
- ubuntu下安装nodejs
```
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y nodejs
```
2. 工作目录配置  
- win平台：配置将打开默认工作目录，按需修改vimrc中的cd命令部分
3.  font目录下的字体手动安装一下
4.  color目录下的配色文件复制到你的VIM对应目录
5.  plugManager目录下的plug.vim复制到你的对应目录，文件已做修改，更改了插件下载源，速度还是很快的。（安装失败的话多尝试几次看看）
6.  vim命令：安装coc LSP服务器
```
:CocInstall coc-clangd
:CocInstall coc-pyright
```
7.  win平台: 下载[clangd](https://clangd.llvm.org/)， 添加bin目录到系统环境变量
8.  vim命令：安装vimspector的c调试器(这个需要从github拉取，可以找不同时间段尝试或者连接手机热点尝试,推荐从镜像站手动下载文件后放到下载目录再执行此命令)
```
:VimspectorInstall --enable-c 
```
9. 安装markdown预览组件
- win平台: 管理员运行powershell：(依赖nodejs)
```
npm -g install instant-markdown-d
```
- ubuntu: 
```
sudo npm -g install instant-markdown-d
```
10. 下载`compile_commands.json`生成工具
win平台: compiledb，powershell：
```shell
pip install compiledb 
```
11. 工具安装
- win平台: 下载[Cygwin64](https://cygwin.com/index.html), 安装gcc、g++、make等工具，安装完成后把bin目录添加到环境变量

12. 编译器安装：
- win平台: 下载[arm-none-eabi-gcc](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)交叉编译器，安装完成后把bin目录添加到环境变量

13. win平台: 解压ctags文件夹下的`ctags58.zip`，拷贝ctags.exe到vim可执行文件目录下

14. win平台: 把keil可执行文件目录添加到环境变量，用于调用keil编译和下载

15. win平台: 把fullscreen目录下的dll文件拷贝到gvim.exe同级目录

## config.py使用说明
### win平台
使用管理员运行即可
### ubuntu
- 配置时（功能1）：先不使用管理员运行，更新普通用户.vimrc，再使用管理员运行，更新管理员.vimrc和其他系统文件。（普通用户报错正常，因为只能移动.vimrc, 无权限移动其他vim组件）
- 上传时（功能2）：如果更改的是管理员的.vimrc，则使用管理员权限运行，如果不使用管理员权限运行则上传普通用户.vimrc。（上传完成后用功能1更新另一个账户的配置文件）

## 一些自定义按键说明(<>内表示同时按，否则为顺序按)

### 移动
- `<C-j>`：插入模式下移光标
- `<C-k>`：插入模式上移光标
- `<C-h>`：插入模式左移光标
- `<C-l>`：插入模式右移光标

### jk<esc映射>
- `jk`: esc

### 工作区恢复
- `<leader><F5>`: 保存工作区
- `<leader><F6>`: 恢复工作区(不恢复文件树插件)

### 功能
- `<F2>`: 生成tags，辅助跳转
- `<F3>`: 文件树
- `<F4>`: Tagbar
- `<Alt-+>`: 终端
- `<leader>be`: buffer列表

#### coc
- `gd`: 跳转到定义
- `gr`: 跳转到引用
- `<leader>rn`: 符号重命名
- `<leader>f`: 格式化选中的代码
- `<leader>qf`: 对当前行使用自动修复
- `<space>a`: 语法检查列表
- `<space>o`: 查找当前文档符号
- `<space>s`: 查找工作区符号
- `<space>e`: 已安装coc扩展列表

#### easymotion
- `<leader><leader>w`:按单词向后跳转
- `<leader><leader>b`:按单词向前跳转
- `<leader><leader>s`:跳转到指定字符

#### 对齐: Tabular
- 对齐指定字符：先选中要操作范围，选中后冒号
```
:Tabularize /{char}
```
#### vim-floaterm
- `<A-=>`: 打开/隐藏终端窗口
- `<A-+>`: 关闭终端窗口，在窗口关闭前使用
#### 翻译
- `<leader>t`: 	在底行翻译
- `<leader>tt`: 弹窗翻译
- `<space><space>`: Ken翻译

### 窗口跳转和调整
- `<C-]>`：使用tags文件跳转
- `<leader>s/d`: 窗口跳转
- `<leader>w/e`：窗口调整
- `<leader>j`：窗口交换
- `<C-f>`：窗口滚动
- `<C-b>`：窗口滚动
- `<C-d>`：窗口滚动
- `<C-u>`：窗口滚动
- `<C-y>`：窗口滚动
- `<C-e>`：窗口滚动
- `<tab>`：切换buffer标签,自动补全时切换选项，加`shift`反向切换

### keil命令
- `<leader>kb`：使用keil编译
- `<leader>kr`: 使用keil重新编译
- `<leader>kd`: 使用keil下载

### 全屏插件
- `<Alt-Enter>`: 全屏
- `<Alt-y`>:全屏减小透明度
- `<Alt-t`>:全屏增加透明度

### 文件类命令
- `<leader>hex`:打开二进制文件(不能用于关闭)

	详细映射查看配置文件

### 帮助
- `K`: 打开帮助

## Debug
调试使用vimspector插件，需要`.vimspector.json` 配置文件
- `<F5>`: 运行/继续
- `<S-F5>`: 停止调试
- `<C-S-F5>`: 复位调试
- `<F6>`: 暂停
- `<F9>`: 添加/取消断点
- `<S-F9>`: 添加函数断点
- `<F10>`: 单步跳过
- `<F11>`: 单步进入
- `<S-F11>`: 单步跳出

## keil编码配置
- 屏蔽printf中文报错, option->c/c++(ac6)->Misc Controls，文本框填入：
```
-Wno-invalid-source-encoding
```

## 其他
- 51使用ctags生成tags文件辅助跳转，其他使用make的工具使用`make compiledb`更新数据库文件
- vimspector插件安装--enable-c时提示权限问题：
```
sudo chown -R  username:username  filename
```
- makefile里面win平台库路径示例：
```c
-I D:/GreenSoft/gcc-arm-none-eabi-5_4-2016q3-20160926-win32/arm-none-eabi/include
```

- wsl下所有光标都一样，单独加入下面配置，可以凑合使用

| 1        | 2      | 3            | 4        | 5          | 6      |
| :----:   | :----: | :----:       | :----:   | :----:     | :----: |
| 闪烁块 █ | 块 █   | 闪烁下划线 ▁ | 下划线 ▁ | 闪烁竖线 ┃ | 竖线 ┃ |

```
" 进入插入模式下的光标形状
let &t_SI.="\e[5 q"
" 进入替换模式下的光标形状
let &t_SR.="\e[3 q"
" 从插入模式或替换模式下退出，进入普通模式后的光标形状
let &t_EI.="\e[1 q"
" 进入vim时，设置普通模式下的光标形状
autocmd VimEnter * silent !echo -ne "\e[1 q"
" 离开vim后，恢复shell模式下的光标形状
autocmd VimLeave * silent !echo -ne "\e[5 q"
```

## 演示
<img src="https://www.z4a.net/images/2022/03/19/Snipaste_2022-03-19_17-21-39.png" alt="Snipaste_2022-03-19_17-21-39.png" border="0" />




















