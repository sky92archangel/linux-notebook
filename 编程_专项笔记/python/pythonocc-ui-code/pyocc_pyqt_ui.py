from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QMainWindow
# from PyQt5.QtUiTools import QUiLoader
from PyQt5 import uic
from PyQt5.QtCore import QFile

from OCC.Display.backend import load_backend
load_backend("qt-pyqt5")
from OCC.Display import qtDisplay

# from pyocc_ui_demo import ShowShape

class Stats(QDialog):

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义
        # qfile_stats = QFile("./window_demo.ui")
        # qfile_stats.open(QFile.ReadOnly)
        # qfile_stats.close()
        # self.ui = QUiLoader().load(qfile_stats)

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi('./window_demo.ui')

        self.ui.button.clicked.connect(self.displayBOX)

        self.canvas = qtDisplay.qtViewer3d(self)
        self.ui.hLayout.addWidget(self.canvas)
        self.canvas.resize(300, 300)
        self.canvas.InitDriver()
        self.display = self.canvas._display

    def displayBOX(self):
        a_box = BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape()
        self.ais_box = self.display.DisplayShape(a_box)[0]
        self.display.FitAll()


app = QApplication([])
stats = Stats()
stats.ui.show()
# ShowShape()
app.exec_()