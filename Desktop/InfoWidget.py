'''
    信息显示
    by ：丁毅
    2022-01-29
'''
from PyQt5.QtWidgets import QWidget

from ui.ui_info import Ui_Info


class InfoWidget(QWidget):
    ui=Ui_Info()

    def __init__(self,parent=None):
        super(InfoWidget,self).__init__(parent)

        self.setWindowTitle("Operate Panel")
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽