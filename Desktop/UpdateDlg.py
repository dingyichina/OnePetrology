import os
import sys
import zipfile

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QDialog, QApplication

import MultiDownloader
import myservice
from ui.ui_update import Ui_updateDlg


class UpdateDlg(QDialog):
    # 下载解压完成后,发送信号，提示退出重启
    updateSuccessSignal = QtCore.pyqtSignal(str)

    ui = Ui_updateDlg()
    curSize  = 0

    def __init__(self,parent=None):
        QDialog.__init__(self, parent)
        self.downloader = MultiDownloader.MultiDownloader()
        self.setupUi()
        # 初始化界面参数
        try:
            # 写死的三个字段

            item = myservice.client.getItem("69bbb230-73a4-4b47-b279-94c2f4f15060")
            self.ui.lblNewVersion.setText(item.metadata['dc.description.version'][0]['value'])
            self.ui.lblCurVersion.setText(str(myservice.__version__))
            self.ui.lblDescprition.setText(item.metadata['dc.description'][0]['value'])
            self.uuid = item.metadata['dc.description.uri'][0]['value']
        except:
            import  traceback
            myservice.logger.error(traceback.format_exc())

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        #链接处理函数
        self.ui.btnStart.clicked.connect(self.doStartUpdate)
        self.ui.btnClose.clicked.connect(self.doClose)
        self.downloader.progressSignal.connect(self.updateProgress)


    def doStartUpdate(self):
        # 采用多线程下载，然后更新界面进度
        # 拼装下载链接
        url = "https://petrology.deep-time.org/server2/api/core/bitstreams/"+self.uuid+"/content"
        file_name = "update.zip"
        self.thread = WorkerThread(self.downloader,url,file_name)
        self.thread.finishSignal.connect(self.doDownloadSuccess)
        self.thread.statusSignal.connect(self.updateStatus)
        self.thread.start()
        self.ui.btnStart.setEnabled(False)
        pass

    def updateStatus(self,msg):
        self.ui.lblProgress.setText(msg)

    def updateProgress(self,chunksize,totalSize):
        self.curSize = self.curSize + chunksize
        self.ui.progressBar.setMaximum(totalSize)
        self.ui.progressBar.setValue(self.curSize)
        self.ui.lblProgress.setText("Current Progress: {} / {}".format(self.curSize,totalSize))


    def doDownloadSuccess(self):
        # 此时解压到temp目录
        self.ui.lblProgress.setText("unzip succeed!")

        # 解压缩之后提示推出程序然后执行更新脚本bat，
        self.close()
        os.system("start DDE-OnePetrology.exe")
        pass

    def doClose(self):
        #
        if hasattr(self,"thread"):
            if self.thread.isRunning():
                self.thread.terminate()
        self.close()
        pass

# 后台下载线程
class  WorkerThread(QThread):

    finishSignal = QtCore.pyqtSignal(str)  # 完成信号
    statusSignal = QtCore.pyqtSignal(str)  # 注册过程状态信号
    def __init__(self,downloader,url,file_name,callback=None,parent=None):
        super(WorkerThread, self).__init__(parent)
        self.downloader=downloader
        self.url = url
        self.file_name = file_name
        self.callback = callback
        pass
    # 处理提交到db的操作
    def run(self):
        myservice.logger.info("start  auto update progress"+self.url)
        try:
            self.downloader.download(self.url, self.file_name)

            myservice.logger.info("auto update download finished:" + self.url)
            zfile = zipfile.ZipFile(self.file_name, "r")
            self.statusSignal.emit("unzip the file ......")
            zfile.extractall(path="../")
            self.finishSignal.emit("auto update download finished:" + self.url)
        except Exception as ex:
            import traceback
            msg = traceback.format_exc()
            myservice.logger.error(msg)
            self.statusSignal.emit("Error :" + msg)
            self.finishSignal.emit("Error :" + msg)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = UpdateDlg()
    dfe.show()

    sys.exit(app.exec_())
