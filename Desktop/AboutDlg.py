"""
    关于对话框

"""
from PyQt5.QtWidgets import QDialog

from ui.ui_about_dlg import Ui_AboutDlg


class AboutDlg(QDialog):
    ui = Ui_AboutDlg()

    def __init__(self,parent=None):
        QDialog.__init__(self, parent)
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # self.ui.btnLogin.connect(self.ui.btnLogin.click,self.dologinprocess)