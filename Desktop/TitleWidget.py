"""
    自定义标题栏，用来模拟原来的标题栏的动作
    author：dingyi

"""
import sys

from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtWidgets import QWidget, QApplication

from ui.ui_titlewidget import Ui_QTitleWidget


class TitleWidget(QWidget):
    # 自定义信号
    windowMin = pyqtSignal()    # 最小化
    windowMax = pyqtSignal()    # 最大化
    windowClose = pyqtSignal()  # 关闭
    windowMove = pyqtSignal(QPoint)   # 移动

    ui = Ui_QTitleWidget()

    def __init__(self,parent=None):
        super(TitleWidget, self).__init__(parent)
        # 初始化ui
        self.setupUi()
        # 初始化变量
        self.m_bPressed = False

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 处理其它
        self.ui.btnMax.clicked.connect(self.doMax)
        self.ui.btnMin.clicked.connect(self.doMin)
        self.ui.btnClose.clicked.connect(self.doClose)

    def doMax(self):
        self.windowMax.emit()

    def doMin(self):
        self.windowMin.emit()

    def doClose(self):
        self.windowClose.emit()

    # 鼠标按下事件
    def mousePressEvent(self,event):
        # print("Mouse press")
        # 鼠标左键
        if (event.buttons() == Qt.LeftButton):
            self.m_ptPress = event.pos()
            self.m_bPressed = True
            # print("left press")

    # 鼠标移动事件
    def mouseMoveEvent(self,event):
        try:
            if self.m_bPressed:
                p = event.pos() - self.m_ptPress
                self.windowMove.emit(p)
                # print("移动事件：",p)
        except Exception as e:
            print(e)

    # 鼠标释放事件
    def mouseReleaseEvent(self,event):
        self.m_ptPress = False

    # 鼠标双击事件
    def mouseDoubleClickEvent(self,event):
        self.windowMax.emit()

if __name__=='__main__':
    app = QApplication(sys.argv)

    appWin = TitleWidget()
    appWin.showMaximized()
    sys.exit(app.exec_())