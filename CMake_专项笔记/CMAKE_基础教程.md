# CMAKE 教程

[TOC]

## 零、GCC命令

对于写好的c语言文件 main.c

### 1.直接生成可执行文件：

```shell
#直接生成可执行文件
gcc main.c -o main 
#多个文件
gcc main.c fun.c -o main 
```

### 2.分步操作：

预处理、编译、汇编、链接

可对多文件名分别处理到 .o 文件 

```shell
#预处理  	结果main.i文件
gcc -E main.c -o main.i

#编译器	编译后文件main.s
gcc -S main.i

#汇编器	继续汇编产生main.o文件
gcc -c main.s 

#链接器 	将main.o文件链接起来 产生main可执行文件
gcc main.o -o main
```



## 一、Makefile

### 1.例子

若工程编译过，仅仅编译修改的文件或头文件引用的所有内容 Makefile

主要缩行必须用TAB

```makefile
main : main.o input.o calcu.o  
	gcc -o main main.o input.o calcu.o 
main.o：main.c
	gcc -c main.c
input.o：input.c
	gcc -c input.c
calcu.o：calcu.c
	gcc -c calcu.c	

clean:
	rm *.o
	rm main
```

### 2.变量和赋值

主要缩行必须用TAB

引用makeflie变量

```makefile
#Makefile变量使用
objects = main.o input.o 
main:$(objects)
	gcc -o main $(objects)
main.o：main.c
	gcc -c main.c
input.o：input.c
	gcc -c input.c
calcu.o：calcu.c
	gcc -c calcu.c	

clean:
	rm *.o
	rm main
```

= 号为类似指针的赋值 变量会接受最后一次赋的值

```makefile
name = zdk
curname = $(name)
name = tre

#name更新后影响了curname的值 故=号类似于传递指针 
#此处打印为 echo curname:tre    @符号为在shell命令行显示执行过程  不加则显示curname:tre
print:
	@echo curname:$(curname)
```

:=为创建一个新对象

```makefile
name = zdk
curname := $(name)
name = tre

#name更新后影响了curname的值 故:=号类似于创建新副本 
#此处打印为 echo curname:zdk    @符号为在shell命令行显示执行过程  不加则显示curname:zdk
print:
	@echo curname:$(curname)
```

?= 检测变量是否赋值  若没有  则赋值  否则不动

+= 对变量追加内容

### 3.模式规则

将c文件编译为o

%类似通配符  

自动化变量

```makefile
 $@ 
 $< 自动匹配依赖
 $^
```

原有文件改写为

```makefile
#Makefile
objects = main.o input.o 
main:$(objects)
	gcc -o main $(objects)
#自动匹配依赖
%.o：%.c
	gcc -c  $< 
	
clean:
	rm *.o
	rm main
```

伪目标，无论当前目录下是否有clean名字的文件 都进行makefile里默认的clean操作

```makefile
.PHONY:clean
```

条件判断

```makefile
【条件判断字】
	【真时执行】
else
	【假时执行】
endif
```

## 二、CMakeLists编写

**每个目录下都会有CMakeLists.txt**



### 0.指定编译器和参数

```cmake
#指定最低版本号
CMAKE_MINIMUM_REQUIRED(VERSION 3.0)   

##########指定编译器#########
#若想指定编译器则需要如下内容    注意必须在CMAKE_MINIMUM_REQUIRED之后指定
#指定C编译器
set (CMAKE_C_COMPILER "/path_to_gcc/gcc")
#指定C++编译器
set (CMAKE_CXX_COMPILER "/path_to_gpp/g++")
#如不指定则使用系统默认编译器

#########添加编译参数#########
#设置编译选项（配置编译器）有如下三种方法
#ADD_COMPILE_OPTIONS方法会递归引用到整个项目中 针对所有编译器
ADD_COMPILE_OPTIONS(-std=c++11 -Wall -Werror -Wstrict-prototypes -Wmissing-prototypes)
#ADD_DEFINITIONS方法会递归引用到整个项目中 针对所有编译器
ADD_DEFINITIONS(-std=c++11 -Wall -Werror -Wstrict-prototypes -Wmissing-prototypes)
#set命令设置CMAKE_C_FLAGS只针对c编译器
SET(CMAKE_C_FLAGS  -Wall -Werror -Wstrict-prototypes -Wmissing-prototypes)
```

  

### 1.单文件单文件demo1

单文件

```cmake
#指定最低版本号
CMAKE_MINIMUM_REQUIRED(VERSION 3.0)   
#项目名称
PROJECT(demo1)	
#添加可执行程序
ADD_EXECUTABLE(demo1 power.cpp)
```

在不同系统有不同表现

将CMakeLists.txt翻译为当前系统的Makeflie （针对VS编译器会出现一个sln及相关文件）

```shell
cmake ./
```

linux下

```shell
make 
```

win下 直接打开sln操作

### 2.单目录多文件demo2

多文件

```cmake
#指定最低版本号
CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

#项目名称
PROJECT(demo2)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
AUX_SOURCE_DIRECTORY(./ DIR_SRCS)  

#添加可执行程序
ADD_EXECUTABLE(demo2 ${DIR_SRCS})
```

### 3.多目录多文件demo3

多目录多文件目录结构

```shell
.
├── CMakeLists.txt
├── main.cpp
└── mylib
    ├── CMakeLists.txt
    ├── mymath.cpp
    └── mymath.hpp
```

子目录mylib的CMakeLists.txt 

```cmake
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
AUX_SOURCE_DIRECTORY(. DIR_LIB_SRCS) 

#添加静态库 名为libmath.a  静态库文件  linux下为.a   win下为.lib
#STATIC静态库    SHARED动态库  MODULE使用dyld系统有效 否则等同于动态库
ADD_LIBRARY(libmath.a STATIC ${DIR_LIB_SRCS})

#添加动态库 名为libmath.so  动态库文件  linux下为.so   win下为.dll
#STATIC静态库    SHARED动态库  MODULE使用dyld系统有效 否则等同于动态库
ADD_LIBRARY(libmath.so SHARED ${DIR_LIB_SRCS})
```

主程目录的CMakeLists.txt 

```cmake
#指定最低版本号
CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

#项目名称
PROJECT(demo3)

#添加程序的子目录 即考虑子目录下的CMakeLists.txt  若加EXCLUDE_FROM_ALL则为编译过程忽略该目录
ADD_SUBDIRECTORY(./mylib)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
AUX_SOURCE_DIRECTORY(./ DIR_SRCS) 

#添加可执行程序
ADD_EXECUTABLE(demo3 ${DIR_SRCS})

#将子目录生成的库链接过来
TARGET_LINK_LIBRARIES(demo3 libmath.a)
```

### 4.标准工程demo4

目录结构

```
.
├── build
├── CMakeLists.txt
├── mylib
│   ├── CMakeLists.txt
│   ├── mymath.cpp
│   └── mymath.hpp
└── src
    ├── main.cpp
    └── CMakeLists.txt
```

src 的 CMakeLists.txt  主要任务 ：查找头文件  添加主程依赖 引用库文件

```cmake
#向工程添加多个头文件搜索路径 
#PROJECT_SOURCE_DIR 最近的包含PROJECT关键词的CMakeLists.txt所在的路径  
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/mylib)

#指定可执行文件输出路径 EXECUTABLE_OUTPUT_PATH    
#PROJECT_BINARY_DIR是cmake产生二进制文件所在路径  即执行cmake的目录 这里是build目录
#将生成的可执行文件放入固定的成果位置
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
AUX_SOURCE_DIRECTORY(./ DIR_SRCS)

#添加可执行程序
ADD_EXECUTABLE(demo4 ${DIR_SRCS})

#将子目录生成的库链接过来
TARGET_LINK_LIBRARIES(demo4 libmath.a)
```

mylib的 CMakeLists.txt  主要任务：生成库文件

```cmake
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
AUX_SOURCE_DIRECTORY(. DIR_LIB_SRCS)

#指定库文件输出路径 LIBRARY_OUTPUT_PATH    
#PROJECT_BINARY_DIR是cmake产生二进制文件所在路径  即执行cmake的目录 这里是build目录
#将产生的库文件放入固定的成果位置
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)

#添加静态库 名为libmath.a  静态库文件  linux下为.a   win下为.lib
#STATIC静态库    SHARED动态库  MODULE使用dyld系统有效 否则等同于动态库
ADD_LIBRARY(libmath.a STATIC ${DIR_LIB_SRCS})

#添加动态库 名为libmath.so  动态库文件  linux下为.so   win下为.dll
#STATIC静态库    SHARED动态库  MODULE使用dyld系统有效 否则等同于动态库
ADD_LIBRARY(libmath.so SHARED ${DIR_LIB_SRCS})

###############注意这里的ADD_LIBRARY只能存在一个 一份代码的静态库和动态库只能生成一种
```

工程根目录的 CMakeLists.txt  统筹各个子目录

```cmake
#指定最低版本号
CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

#项目名称
PROJECT(demo4)

#添加程序的子目录mylib 考虑子目录下的CMakeLists.txt 若加EXCLUDE_FROM_ALL则为编译过程忽略该目录
ADD_SUBDIRECTORY(./mylib)

#添加程序的子目录src   考虑子目录下的CMakeLists.txt
ADD_SUBDIRECTORY(./src) 
```

### 5.标准工程demo5

文件夹结构

```SHELL
.
├── CMakeLists.txt
├── myapp
│   ├── CMakeLists.txt
│   └── main.cpp
├── mydll
│   ├── CMakeLists.txt
│   ├── myprint.cpp
│   └── myprint.hpp
└── mylib
    ├── CMakeLists.txt
    ├── mymath.cpp
    └── mymath.hpp 
```

windows中的注意事项

```c++
//这里的需要生成dll文件的工程代码务必注意一点 
//在windows中  所有的类和函数前都要加上  __declspec(dllexport) 前缀  此前缀可以用宏定义来简化写法
//这样才能调用封装在动态链接库中的函数
//==================================myprint.hpp======================================
#define MY_LIB_API __declspec(dllexport) 
#include<iostream>
#include<string>
inline
void MY_LIB_API myprint(std::string str1, double count);
```

./mydll/CMakeLists.txt  动态库代码   主要任务：生成动态库文件

```cmake
##########################  ./mydll/CMakeLists.txt    #############################
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
AUX_SOURCE_DIRECTORY(. DIR_LIB_SRCS)  

#指定库文件输出路径 LIBRARY_OUTPUT_PATH    
#PROJECT_BINARY_DIR是cmake产生二进制文件所在路径  即执行cmake的目录 这里是build目录
#将产生的库文件放入固定的成果位置
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/dll)
 
#添加动态库 名为libmath.so  动态库文件  linux下为.so   win下为.dll
#STATIC静态库    SHARED动态库  MODULE使用dyld系统有效 否则等同于动态库
ADD_LIBRARY(myprint SHARED ${DIR_LIB_SRCS})
```

./mylib/CMakeLists.txt  静态库代码  主要任务：生成静态库文件

```cmake
##########################  ./mylib/CMakeLists.txt    #############################
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
AUX_SOURCE_DIRECTORY(. DIR_LIB_SRCS) 
 
#指定库文件输出路径 LIBRARY_OUTPUT_PATH    
#PROJECT_BINARY_DIR是cmake产生二进制文件所在路径  即执行cmake的目录 这里是build目录
#将产生的库文件放入固定的成果位置
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)

#添加静态库 名为libmath.a  静态库文件  linux下为.a   win下为.lib
#STATIC静态库    SHARED动态库  MODULE使用dyld系统有效 否则等同于动态库
ADD_LIBRARY(mymath STATIC ${DIR_LIB_SRCS})
  
```

./myapp/CMakeLists.txt   主程的 CMakeLists.txt     主要任务 ：查找头文件  添加主程依赖 引用库文件

```cmake
##########################  ./myapp/CMakeLists.txt    #############################
#向工程添加多个头文件搜索路径  PROJECT_SOURCE_DIR 项目根目录路径  
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/mylib)
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/mydll)

#指定可执行文件输出路径 EXECUTABLE_OUTPUT_PATH    
#PROJECT_BINARY_DIR是cmake产生二进制文件所在路径  即执行cmake的目录 这里是build目录
#将生成的可执行文件放入固定的成果位置
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

#将当前目录下的所有文件都放入变量DIR_SRCS内
AUX_SOURCE_DIRECTORY(./ DIR_SRCS)

#添加可执行程序
ADD_EXECUTABLE(demo5 ${DIR_SRCS})

#将子目录生成的库链接过来
TARGET_LINK_LIBRARIES(demo5 mymath)
TARGET_LINK_LIBRARIES(demo5 myprint) 
```

./CMakeLists.txt     工程根目录的 CMakeLists.txt  统筹各个子目录

```cmake
##########################  ./CMakeLists.txt    #############################

#指定最低版本号
CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

# 设置C/C++标准
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

#项目名称
PROJECT(demo5)

#添加程序的子目录mylib   若加EXCLUDE_FROM_ALL则为编译过程忽略该目录
ADD_SUBDIRECTORY(./mylib)
#添加程序的子目录mydll 且将上面所得到的myprint.lib以及myprint.dll复制并放到bin文件夹中
ADD_SUBDIRECTORY(./mydll bin)

#添加程序的子目录src
ADD_SUBDIRECTORY(./myapp) 
```



### 附

```cmake
#创建工程helloworld
PROJECT (helloworld)

#将源文件作为变量src
SET(src  ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp ) 
	
#添加可执行程序 helloworld工程 为目标
ADD_EXECUTABLE(helloworld   ${src})
```



## 三、CMAKE命令

### 1.cmake基础命令

```shell

#假设已经完成了所有的CMakeLists.txt的编写

#进入项目根目录 建立build文件夹 
$ mkdir build
#进入build
$ cd build
# 开始构建
$ cmake ..
# 开始构建
cmake --build .
#此时在 build文件夹内就出现了结果  当然结果文件结构会根据CMakeLists.txt内的设置有改变
```

 

### 1.cmake命令行指定编译器

```shell
#可以直接输入，可以看到当前版本支持的编译器
$ cmake -G
CMake Error: No generator specified for -G

Generators
* Visual Studio 17 2022        = Generates Visual Studio 2022 project files.
                                 Use -A option to specify architecture.
  Visual Studio 16 2019        = Generates Visual Studio 2019 project files.
                                 Use -A option to specify architecture.
  Visual Studio 15 2017 [arch] = Generates Visual Studio 2017 project files.
                                 Optional [arch] can be "Win64" or "ARM".
  Visual Studio 14 2015 [arch] = Generates Visual Studio 2015 project files.
                                 Optional [arch] can be "Win64" or "ARM".
  Visual Studio 12 2013 [arch] = Generates Visual Studio 2013 project files.
                                 Optional [arch] can be "Win64" or "ARM".
  Visual Studio 11 2012 [arch] = Generates Visual Studio 2012 project files.
                                 Optional [arch] can be "Win64" or "ARM".
  Visual Studio 10 2010 [arch] = Deprecated.  Generates Visual Studio 2010
                                 project files.  Optional [arch] can be
                                 "Win64" or "IA64".
  Visual Studio 9 2008 [arch]  = Generates Visual Studio 2008 project files.
                                 Optional [arch] can be "Win64" or "IA64".
  Borland Makefiles            = Generates Borland makefiles.
  NMake Makefiles              = Generates NMake makefiles.
  NMake Makefiles JOM          = Generates JOM makefiles.
  MSYS Makefiles               = Generates MSYS makefiles.
  MinGW Makefiles              = Generates a make file for use with
                                 mingw32-make.
  Green Hills MULTI            = Generates Green Hills MULTI files
                                 (experimental, work-in-progress).
  Unix Makefiles               = Generates standard UNIX makefiles.
  Ninja                        = Generates build.ninja files.
  Ninja Multi-Config           = Generates build-<Config>.ninja files.
  Watcom WMake                 = Generates Watcom WMake makefiles.
  CodeBlocks - MinGW Makefiles = Generates CodeBlocks project files.
  CodeBlocks - NMake Makefiles = Generates CodeBlocks project files.
  CodeBlocks - NMake Makefiles JOM
                               = Generates CodeBlocks project files.
  CodeBlocks - Ninja           = Generates CodeBlocks project files.
  CodeBlocks - Unix Makefiles  = Generates CodeBlocks project files.
  CodeLite - MinGW Makefiles   = Generates CodeLite project files.
  CodeLite - NMake Makefiles   = Generates CodeLite project files.
  CodeLite - Ninja             = Generates CodeLite project files.
  CodeLite - Unix Makefiles    = Generates CodeLite project files.
  Eclipse CDT4 - NMake Makefiles
                               = Generates Eclipse CDT 4.0 project files.
  Eclipse CDT4 - MinGW Makefiles
                               = Generates Eclipse CDT 4.0 project files.
  Eclipse CDT4 - Ninja         = Generates Eclipse CDT 4.0 project files.
  Eclipse CDT4 - Unix Makefiles= Generates Eclipse CDT 4.0 project files.
  Kate - MinGW Makefiles       = Generates Kate project files.
  Kate - NMake Makefiles       = Generates Kate project files.
  Kate - Ninja                 = Generates Kate project files.
  Kate - Unix Makefiles        = Generates Kate project files.
  Sublime Text 2 - MinGW Makefiles
                               = Generates Sublime Text 2 project files.
  Sublime Text 2 - NMake Makefiles
                               = Generates Sublime Text 2 project files.
  Sublime Text 2 - Ninja       = Generates Sublime Text 2 project files.
  Sublime Text 2 - Unix Makefiles
                               = Generates Sublime Text 2 project files.

# Visual Studio 编译器
$ cmake -S . -B build -G "Visual Studio 17 2022"

#windows下nmake支持
cmake -S . -B build -G "NMake Makefiles"

#Ninja  安卓和鸿蒙方案
cmake -S . -B build -G Ninja

#windows下g++ MinGW支持
cmake -S . -B build -G "MinGW Makefiles"
```

 
