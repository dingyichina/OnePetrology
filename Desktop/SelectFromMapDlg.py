import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

from ui.ui_select_from_map_dlg import Ui_dlgMap


class SelectFromMapDlg(QDialog):
    ui = Ui_dlgMap()

    def __init__(self,parent=None):
        QDialog.__init__(self, parent)
        self.setupUi()
        self.polygon = "" # 默认置空

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 复用网站的功能
        Url = 'https://petrology.deep-time.org/search/bylocation.html'
        self.ui.mapWidget.setUrl(QtCore.QUrl(Url))
        self.ui.mapWidget.loadFinished.connect(self.doLoadFinished)

        self.ui.btnOk.clicked.connect(self.doOk)
        self.ui.btnCancel.clicked.connect(self.doCancel)
        # 用js隐藏掉页面的submit按钮



        # self.ui.btnLogin.connect(self.ui.btnLogin.click,self.dologinprocess)
        #self.ui.mapWidget.initBaseMap()
        # 禁掉 其它功能，保留矩形和多边形
        #self.ui.mapWidget.ui.btnIdentify.setEnabled(False)
        #self.ui.mapWidget.ui.btnCircle.setEnabled(False)

    def doLoadFinished(self):
        # 屏蔽掉submit，避免误操作引发跳转
        jsstr = "$('#btnSubmit').css('visibility','hidden');"
        self.ui.mapWidget.page().runJavaScript(jsstr)
    def doOk(self):
        jsstr='$("#queryGeojson").val();'
        self.ui.mapWidget.page().runJavaScript(jsstr,self.js_callback)


    def js_callback(self,rtn):
        if isinstance(rtn,str):
            if len(rtn) >0:
                self.polygon = rtn  # 保存在变量中
                self.accept()
            else:
                # 提醒先选择
                QMessageBox.information(self, 'Information', "Please select the area polygon first ", QMessageBox.Yes)
    def doCancel(self):
        self.reject()
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = SelectFromMapDlg()
    dfe.show()

    sys.exit(app.exec_())
