# 04_三剑客之awk

[TOC]

## 简介

awk 是强大的文本格式化工具，早期在UNIX系统上开发的，之后移植到了linux上awk是gawk = GNU awk

awk是一门脚本语言 ，有循环判断等

```shell

awk [可选参数]  '模式[动作]'  [文件数据] 

sky92@sky92:~$ awk --help
Usage: awk [POSIX or GNU style options] -f progfile [--] file ...
Usage: awk [POSIX or GNU style options] [--] 'program' file ...
POSIX options:          GNU long options: (standard)
        -f progfile             --file=progfile
        -F fs                   --field-separator=fs
        -v var=val              --assign=var=val
Short options:          GNU long options: (extensions)
        -b                      --characters-as-bytes
        -c                      --traditional
        -C                      --copyright
        -d[file]                --dump-variables[=file]
        -D[file]                --debug[=file]
        -e 'program-text'       --source='program-text'
        -E file                 --exec=file
        -g                      --gen-pot
        -h                      --help
        -i includefile          --include=includefile
        -l library              --load=library
        -L[fatal|invalid]       --lint[=fatal|invalid]
        -M                      --bignum
        -N                      --use-lc-numeric
        -n                      --non-decimal-data
        -o[file]                --pretty-print[=file]
        -O                      --optimize
        -p[file]                --profile[=file]
        -P                      --posix
        -r                      --re-interval
        -S                      --sandbox
        -t                      --lint-old
        -V                      --version

To report bugs, see node `Bugs' in `gawk.info', which is
section `Reporting Problems and Bugs' in the printed version.

gawk is a pattern scanning and processing language.
By default it reads standard input and writes standard output.

Examples:
        gawk '{ sum += $1 }; END { print sum }' file
        gawk -F: '{ print $1 }' /etc/passwd

```



## 建立测试文件

```shell
sky92@sky92:~$ echo good{1..10}  >> /tmp/awktest.txt 
sky92@sky92:~$ echo good{11..20} >> /tmp/awktest.txt
sky92@sky92:~$ echo good{21..30} >> /tmp/awktest.txt
sky92@sky92:~$ cat -n /tmp/awktest.txt
     1  good1 good2 good3 good4 good5 good6 good7 good8 good9 good10
     2  good1 good2 good3 good4 good5 good6 good7 good8 good9 good10
     3  good11 good12 good13 good14 good15 good16 good17 good18 good19 good20
     4  good21 good22 good23 good24 good25 good26 good27 good28 good29 good30

sky92@sky92:~$ cp /tmp/awktest.txt /tmp/awktest2.txt
sky92@sky92:~$ sed 's/\ /#/gp' /tmp/awktest2.txt -i -n
sky92@sky92:~$ cat -n /tmp/awktest2.txt
     1  good1#good2#good3#good4#good5#good6#good7#good8#good9#good10
     2  good1#good2#good3#good4#good5#good6#good7#good8#good9#good10
     3  good11#good12#good13#good14#good15#good16#good17#good18#good19#good20
     4  good21#good22#good23#good24#good25#good26#good27#good28#good29#good30
 
```



## 演示

awk默认以空格为分隔符

下面仅仅打印内容

```shell
#每行取出首个
sky92@sky92:~$ awk '{print $1}' /tmp/awktest.txt
good1
good1
good11
good21

#每行取出第二个
sky92@sky92:~$ awk '{print $2}' /tmp/awktest.txt
good2
good2
good12
good22

#每行取出整行 全部打印出来
sky92@sky92:~$ awk '{print $0}' /tmp/awktest.txt
good1 good2 good3 good4 good5 good6 good7 good8 good9 good10
good1 good2 good3 good4 good5 good6 good7 good8 good9 good10
good11 good12 good13 good14 good15 good16 good17 good18 good19 good20
good21 good22 good23 good24 good25 good26 good27 good28 good29 good30
 
#  $NF 代表最后一列
sky92@sky92:~$ awk '{print $NF}' /tmp/awktest.txt
good10
good10
good20
good30

sky92@sky92:~$ awk '{print $(NF-1)}' /tmp/awktest.txt
good9
good9
good19
good29
 
```

### awk内置变量

| 内置变量 | 解释                     |
| -------- | ------------------------ |
| $n       | 当前行的第n个字段        |
| $0       | 当前行的所有             |
| FS       | 字段分割符 默认为空格    |
| NF       | 一行内分割后的总字段数量 |
| NR       | 当前记录数 行数          |
|          |                          |

### awk参数

| 参数 | 解释                      |
| ---- | ------------------------- |
| -F   | 指定分割字段符            |
| -v   | 定义或修改一个awk内部变量 |
| -f   | 从脚本文件中读取awk命令   |

### 基本用法

```shell
sky92@sky92:~$ awk '{print $1 $2 $4}' /tmp/awktest.txt
good1good2good4
good1good2good4
good11good12good14
good21good22good24

sky92@sky92:~$ awk '{print $1,$2,$4}' /tmp/awktest.txt
good1 good2 good4
good1 good2 good4
good11 good12 good14
good21 good22 good24

sky92@sky92:~$ awk '{print $3,$1,$2}' /tmp/awktest.txt
good3 good1 good2
good3 good1 good2
good13 good11 good12
good23 good21 good22

# awk需要在外层使用单引号， 内层才能用双引号
sky92@sky92:~$ awk '{print "第三列："$3,"第一列："$1}' /tmp/awktest.txt
第三列：good3 第一列：good1
第三列：good3 第一列：good1
第三列：good13 第一列：good11
第三列：good23 第一列：good21

sky92@sky92:~$ awk 'NR==3' /tmp/awktest.txt
good11 good12 good13 good14 good15 good16 good17 good18 good19 good20

sky92@sky92:~$ awk 'NR==2,NR==4' /tmp/awktest.txt
good1 good2 good3 good4 good5 good6 good7 good8 good9 good10
good11 good12 good13 good14 good15 good16 good17 good18 good19 good20
good21 good22 good23 good24 good25 good26 good27 good28 good29 good30

sky92@sky92:~$ awk 'NR==3{print $0}' /tmp/awktest.txt
good11 good12 good13 good14 good15 good16 good17 good18 good19 good20
sky92@sky92:~$ awk 'NR==3{print $1}' /tmp/awktest.txt
good11
sky92@sky92:~$ awk 'NR==3{print $2}' /tmp/awktest.txt
good12
sky92@sky92:~$ awk 'NR==2,NR==4{print $2}' /tmp/awktest.txt
good2
good12
good22

sky92@sky92:~$ awk '{print NR,$0}' /tmp/awktest.txt
1 good1 good2 good3 good4 good5 good6 good7 good8 good9 good10
2 good1 good2 good3 good4 good5 good6 good7 good8 good9 good10
3 good11 good12 good13 good14 good15 good16 good17 good18 good19 good20
4 good21 good22 good23 good24 good25 good26 good27 good28 good29 good30

sky92@sky92:~$ awk 'NR==2,NR==4{print NR,$0}' /tmp/awktest.txt
2 good1 good2 good3 good4 good5 good6 good7 good8 good9 good10
3 good11 good12 good13 good14 good15 good16 good17 good18 good19 good20
4 good21 good22 good23 good24 good25 good26 good27 good28 good29 good30

sky92@sky92:~$ awk 'NR==2,NR==4{print NR,$2,$(NF-1),$(NF-2)}' /tmp/awktest.txt
2 good2 good9 good8
3 good12 good19 good18
4 good22 good29 good28


```

## 分隔符问题

输入分隔符FS      输出分隔符OFS  

```shell

sky92@sky92:~$ awk 'NR==2{print $0}' /tmp/awktest2.txt                         good1#good2#good3#good4#good5#good6#good7#good8#good9#good10 
sky92@sky92:~$ awk -F '#' 'NR==2{print $1}' /tmp/awktest2.txt
good1
sky92@sky92:~$ awk -v FS='#' 'NR==2{print $1}' /tmp/awktest2.txt
good1

# 输入分隔符FS设定为#  输出分隔符OFS设定为|  
sky92@sky92:~$ awk -v FS='#' -v OFS='|' 'NR==2{print $1,$3}' /tmp/awktest2.txt
good1|good3
# 输入分隔符FS设定为#  输出分隔符OFS设定为---  
sky92@sky92:~$ awk -v FS='#' -v OFS='---' 'NR==2{print $1,$3}' /tmp/awktest2.txt
good1---good3


```



### 实战

```shell
sky92@sky92:~$ ifconfig docker0
docker0   Link encap:以太网  硬件地址 02:42:4f:17:cd:6e
          inet 地址:172.17.0.1  广播:172.17.255.255  掩码:255.255.0.0
          inet6 地址: fe80::42:4fff:fe17:cd6e/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:19563516 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:17424630 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:0
          接收字节:12109989039 (12.1 GB)  发送字节:4126438365 (4.1 GB)

sky92@sky92:~$ ifconfig docker0 | awk 'NR==2{print $2}'
地址:172.17.0.1




```







