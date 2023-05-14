# PythonOCC 环境配置

[TOC]



## 安装conda

推荐安装miniconda，较为轻量级，下面是下载地址，我们以windows平台为例

```http
# miniconda3 下载地址
https://docs.conda.io/en/latest/miniconda.html
https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

下载得到  Miniconda3-latest-Windows-x86_64.exe  安装即可；

完成后检查虚拟环境目录

```shell
conda config --show
#重点检查 envs_dirs 一栏 是否在用户隐藏文件中  若是则需要修改环境路径
conda config --add envs_dirs newdir # 增加环境路径
conda config --remove envs_dirs newdir  # 删除环境路径
#然后在如下位置找到文件    .condarc
C:\Users\username\.condarc
#在该文件中添加 
envs_dirs:
  - E:\miniconda3\envs #新的环境保存位置
#然后查看路径
conda env list 
```

## 创建PYOCC环境

注意版本推荐7.7.0

```shell
# OCC 7.5.1
conda create --name=pyoccenv python=3.7
source activate pyoccenv
conda install -c conda-forge pythonocc-core=7.5.1
# OCC 7.7.0
conda create --name=pyoccenv python=3.9
activate pyoccenv
conda install -c conda-forge pythonocc-core=7.7.0

#环境配置完成后如有需要可以克隆一个分支环境
conda create -n pyoccenv_pyside --clone pyoccenv

```

完成后 需要安装一个pyside界面或者pyqt 来使用pyocc库的样例代码，这里我们选择安装官方的pyside

```shell
activate pyoccenv_pyside
pip install pyside2 -i https://pypi.douban.com/simple/
```

## 样例代码

首先看pyside是否安装成功，建立文件 pyside_test.py 执行

```python
#pyside_test.py
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QApplication, 
    QLabel
)
# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it
label = QLabel("Hello World")
label.show()
# Enter Qt application main loop
app.exec_()
sys.exit()
```

再看pyocc是否能够运行 建立文件 pyocc_test.py

```python
#pyocc_test.py
#第一个程序，在显示框中显示两个点
from OCC.Display.SimpleGui import init_display
from OCC.Core.gp import gp_Pnt

if __name__ == '__main__':
    display, start_display, add_menu, add_function_to_menu = init_display()
    P0=gp_Pnt(0,0,1)
    P1 =gp_Pnt(0, 30, 20)
    display.DisplayShape(P0)
    display.DisplayShape(P1)
    start_display() 
```

## 编译器

编译器推荐 vscode 或 pycharm   ， vscode配置可能较为麻烦，pycharm功能强大易用，且使用社区版即可，这里使用pycharm；

```http
# pycharm 下载地址
https://www.jetbrains.com/pycharm/download/  
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC
```







































