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

## 二、CMAKE

每个目录下都会有CMakeLists.txt

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

#将当前目录路径设定为变量DIR_SRCS
AUX_SOURCE_DIRECTORY(./ DIR_SRCS) 
##上述另一种写法 SET(DIR_SRCS ./)

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
#将当前目录路径设定为变量DIR_LIB_SRCS
AUX_SOURCE_DIRECTORY(. DIR_LIB_SRCS)
##上述另一种写法 SET(DIR_LIB_SRCS .)

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

#将当前目录路径设定为变量DIR_SRCS
AUX_SOURCE_DIRECTORY(./ DIR_SRCS)
##上述另一种写法 SET(DIR_SRCS ./)

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

#将当前目录下的所有文件都放入变量DIR_SRCS内
AUX_SOURCE_DIRECTORY(./ DIR_SRCS)

#添加可执行程序
ADD_EXECUTABLE(demo4 ${DIR_SRCS})

#将子目录生成的库链接过来
TARGET_LINK_LIBRARIES(demo4 libmath.a)
```

mylib的 CMakeLists.txt  主要任务：生成库文件

```cmake
#将当前目录下的所有文件都放入变量DIR_LIB_SRCS内
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



### 附

```cmake
#创建工程helloworld
PROJECT (helloworld)

#将源文件作为变量src
SET(src  ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp ) 
	
#添加可执行程序 helloworld工程 为目标
ADD_EXECUTABLE(helloworld   ${src})
```

