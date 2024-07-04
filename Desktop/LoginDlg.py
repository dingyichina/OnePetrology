import os
import pathlib

from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5.QtCore import  Qt

import util,base64
from ui.loginDlg import Ui_loginDlg
from myservice import client

import sys
class LoginDlg(QDialog):
    ui=Ui_loginDlg()
    login=False
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi()

    def  setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        #self.ui.btnLogin.connect(self.ui.btnLogin.click,self.dologinprocess)
        self.movie=QMovie("res/worldmap.gif")
        self.ui.lblWorldMap.setMovie(self.movie)
        self.movie.start()
        # 检查配置文件是否存在，如果存在则读取信息，如果不存在跳过
        if pathlib.Path("config/login.json").exists():
            # 读取文件
            config= util.loadconfig("login")
            if "Remember" in config:
                self.ui.chkRemember.setChecked(config["Remember"])
            if "UserAccount" in config:
                self.ui.txtUser.setText(config["UserAccount"])
            if "Password" in config:
                self.ui.txtPassword.setText(base64.b64decode(config["Password"]).decode("utf-8"))
            # 是否执行自动登录的判断
            if "AutoLogin" in config:
                self.ui.chkAutoLogin.setChecked(config["AutoLogin"])
                if config["AutoLogin"]:
                    self.accept()

        self.ui.chkAutoLogin.stateChanged.connect(self.doAutoLogin)
        self.ui.chkRemember.stateChanged.connect(self.doRemember)

    def doAutoLogin(self):
        if self.ui.chkAutoLogin.isChecked():
            self.ui.chkRemember.setChecked(True)

    def doRemember(self):
        if not self.ui.chkRemember.isChecked():
            self.ui.chkAutoLogin.setChecked(False)

    def accept(self) :  #ui中关联的槽
        user=self.ui.txtUser.text()
        password=self.ui.txtPassword.text()

        #检查是否有自动存储
        if self.ui.chkRemember.isChecked():
            config={}
            config["Remember"]=True
            config["AutoLogin"] =self.ui.chkAutoLogin.isChecked()
            config["UserAccount"]=self.ui.txtUser.text()
            config["Password"] =str(base64.b64encode(self.ui.txtPassword.text().encode("utf-8")),'utf-8')
            util.writeconfig(config,"login")
        else:
            # 不记忆，则删除文件
            if pathlib.Path("config/login.json").exists():
                os.remove("config/login.json")
        try:
            #client.getToken()
            client.login(user,password)
            self.login = True
            self.close()
        except Exception as e:
            QMessageBox.critical(self, '错误', '登陆失败！请检查您的用户名和密码。\r\n'+str(e), QMessageBox.Yes, QMessageBox.Yes)

        pass


if __name__=="__main__":
    app=QApplication(sys.argv)
    dlg=LoginDlg()
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling |Qt.AA_DisableWindowContextHelpButton)#去掉问号，但好像不好使。
    print(dlg.exec())
    if(dlg.login):
        print('call main app')
        dlg.destroy()
    sys.exit(app.exec())


