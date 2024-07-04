import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

from ui.ui_select_from_map_dlg import Ui_dlgMap


class SelectConditionDlg(QDialog):
    ui = Ui_dlgMap()

    def __init__(self,k_name, owner, parent=None):
        QDialog.__init__(self, parent)

        self.k_name = k_name
        self.owner = owner
        self.condition = "" # 默认置空
        self.setupUi()
        self.setWindowTitle("Set fields filter from web ")



    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 复用网站的功能
        # Url = 'https://petrology.deep-time.org/search/bycondition.html'
        #self.ui.mapWidget.setUrl(QtCore.QUrl(Url))
        self.ui.mapWidget.setHtml(self.buildHtml(),baseUrl=QtCore.QUrl("https://petrology.deep-time.org/"))
        self.ui.mapWidget.loadFinished.connect(self.doLoadFinished)


        self.ui.btnOk.clicked.connect(self.doOk)
        self.ui.btnCancel.clicked.connect(self.doCancel)
        # 用js隐藏掉页面的submit按钮



        # self.ui.btnLogin.connect(self.ui.btnLogin.click,self.dologinprocess)
        #self.ui.mapWidget.initBaseMap()
        # 禁掉 其它功能，保留矩形和多边形
        #self.ui.mapWidget.ui.btnIdentify.setEnabled(False)
        #self.ui.mapWidget.ui.btnCircle.setEnabled(False)
    #


    def buildHtml(self):
        html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>测试页面</title>
            </head>
            <body>
            <script>
      	        sessionStorage.setItem("k_node",'{}');
		        sessionStorage.setItem("owner", '{}' );
		        sessionStorage.setItem("scope", 'private' );
		        window.location.href = "https://petrology.deep-time.org/search/bycondition.html";
			</script>
            </body>
            </html>
        """.format(self.k_name,self.owner)
        # print(html)
        return html
    def doLoadFinished(self):
        jsstr = "$('#btn-get').css('visibility','hidden');"
        self.ui.mapWidget.page().runJavaScript(jsstr)
        pass
    def doOk(self):
        jsstr='getAQL();'
        self.ui.mapWidget.page().runJavaScript(jsstr,self.js_callback)


    def js_callback(self,rtn):
        if isinstance(rtn,str):
            if len(rtn) >0:
                self.condition = rtn  # 保存在变量中
                print(rtn)
                self.accept()
            else:
                # 提醒先选择
                QMessageBox.information(self, 'Information', "Please set the filter  first ", QMessageBox.Yes)
    def doCancel(self):
        self.reject()
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = SelectConditionDlg("Igneous_Rock","geowind@126.com")
    dfe.show()

    sys.exit(app.exec_())
