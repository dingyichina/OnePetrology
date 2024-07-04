import threading

import pandas as pd

import util
from ui.ui_uploadTableWidget import Ui_TableUploadWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import  QApplication
from myservice import client
from pandasgui import show



class TableUploadWidget(QWidget):

    state=0   #当前状态：  0：待上传   1：上传中    2：已上传完成  3：暂停   4 :出错了

    def __init__(self,filePath,parent=None):
        #print('构造函数被调用',self)
        super(TableUploadWidget,self).__init__(parent)
        self.ui = Ui_TableUploadWidget()  #放在构造函数里可以让界面单独实例化，放在外面属于静态变量
        self.setupUi()
        self.file = filePath  #文件全路径

        #关联到父窗口的 开始上传按钮
        if parent !=None :
            parent.signal_upload.connect(self.doUpload)
            # self.bundleuuid = parent.bundleuuid

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        #关联信号和槽
        self.ui.btnDelete.clicked.connect(self.deleteOne)
        self.ui.btnUpload.clicked.connect(self.btnProcess)
        self.ui.btnPreview.clicked.connect(self.preview)
        self.ui.btnUpload.setVisible(False)

    # 处理按钮
    def btnProcess(self):
        if self.state==0:
            if self.bundleuuid!=None:
                self.doUpload(self.bundleuuid)
            else:
                QMessageBox.warning(self, '错误', '请选择树形结构的bundle节点双击之后再执行本操作。' , QMessageBox.Yes, QMessageBox.Yes)
        elif self.state==1:
            if self.myThread.is_alive():
                self.myThread._stop()
                # 恢复图标
                self.ui.btnUpload.setIcon(QIcon('./res/upload.png'))
        elif self.state==2:
            self.ui.btnUpload.setIcon(QIcon('./res/ok.png'))
        elif self.state==3:
            self.ui.btnUpload.setIcon(QIcon('./res/pause.png'))
        elif self.state == 4:
            self.ui.btnUpload.setIcon(QIcon('./res/error.png'))
    # 预览excel文件
    def preview(self):
        try:
            df=pd.read_excel(self.file)
            show(df)
        except Exception as ex:
            print(ex)

    # 删除自己
    def deleteOne(self):
        self.parent().parent().parent().parent().parent().signal_table_delete.emit(self.file)

    #执行上传
    def doUpload(self,bundleuuid):
        if self.state==0: #当前可以上传
            print('执行上传', self)
            self.bundleuuid=bundleuuid;
            self.myThread=threading.Thread(target=self.uploadInThread())
            self.myThread.start()

        pass
    # 线程函数，执行上传
    def uploadInThread(self):
        try:
            self.ui.btnUpload.setIcon(QIcon('./res/stop.png'))
            client.createBitstream(self.bundleuuid, util.getFileName(self.file), self.file, self.showProgress)
        except Exception as e:
            self.state=4
            self.ui.btnUpload.setIcon(QIcon('./res/error.png'))

    def showProgress(self,monitor):
        QApplication.processEvents() #防止界面被卡死
        progress=round(monitor.bytes_read / monitor.len * 100, 2)
        self.ui.progressBar.setValue(progress)
        #print(progress)
        if progress>=100:
            self.state=1
            #改变上传按钮的图标
            self.ui.btnUpload.setIcon(QIcon('./res/ok.png'))
        pass