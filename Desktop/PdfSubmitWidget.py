"""
    从本地提交pdf文件到dspace库中

    author: dingyi
    2022-04-02

"""
import os
import sys
import threading
import time
import traceback

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QFileInfo, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QApplication

import myservice
import util
from ui.ui_pdf_submit import Ui_PdfSubmit


class PdfSubmitWidget(QWidget):
    collectionId = "c04dce5a-2f71-4ef9-a872-b55f290511d2"  # 文献集合的UUID，目前写死了，回头在调整  todo
    ui = Ui_PdfSubmit()

    def __init__(self, parent=None, ):
        super(PdfSubmitWidget, self).__init__(parent)
        self.setupUi()
        self.fileName=""

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 初始化浏览器组件
        Url = 'http://8.218.13.217:8080/pdfjs/web/viewer.html'
        self.ui.browser.setUrl(QtCore.QUrl(Url))
        self.ui.browser.page().fullScreenRequested.connect(self.handleFullscreenRequest)
        self.ui.browser.settings().globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        # self.ui.browser.settings().globalSettings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.ui.browser.settings().globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.ui.browser.settings().globalSettings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)


        # 链接功能函数
        self.ui.btnChooseFiles.clicked.connect(self.doChooseFile)
        self.ui.btnSubmit.clicked.connect(self.doSubmit)
    # 选择一个PDF文件
    def doChooseFile(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "Choose Paper or Report", os.getcwd(),
                                                           "PDF Files(*.pdf)")
        if fileName is not None:
            self.ui.txtFilePath.setText(fileName)
            # 读取pdf的元数据信息
            from PyPDF2 import PdfFileReader

            with open(fileName, 'rb') as pdf:
                pdf_toread = PdfFileReader(pdf)
                pdf_info = pdf_toread.getDocumentInfo()
                # 把对应元数据复制到对应位置
                self.ui.txtAuthor.setText(pdf_info.get("/Author",""))
                self.ui.txtTitle.setText(pdf_info.get("/Title", os.path.basename(fileName)[:-4]))
                self.ui.txtProducer.setText(pdf_info.get("/Producer",""))
                self.ui.txtSubject.setText(pdf_info.get("/Subject",""))
                self.ui.txtCreateDate.setText(pdf_info.get("/CreationDate",""))
                self.ui.txtModDate.setText(pdf_info.get("/ModDate",""))
                self.ui.txtCreator.setText(pdf_info.get("/Creator",""))
            # 把文件复制给浏览网页
            #url = QtCore.QUrl.fromUserInput('%s?file=%s' % (QUrl.fromLocalFile(QFileInfo("pdfjs/web/viewer.html").absoluteFilePath()).toString(), QUrl.fromLocalFile(QFileInfo(fileName).absoluteFilePath()).toString()))
            url =  QUrl.fromLocalFile(QFileInfo(fileName).absoluteFilePath())
            self.ui.browser.setUrl(url)
            self.fileName = fileName
            print(url)

    # 提交到dspace中
    def doSubmit(self):
        if self.fileName == "":
            QMessageBox.information(self,"Tips","Please choose pdf file first.",QMessageBox.Yes ,QMessageBox.Yes )
            return

        if self.ui.txtAuthor.text().strip() == "" or self.ui.txtSubject.text().strip() == "":
            if QMessageBox.question(self, 'Tips', 'Not all meta information is filled ,Do you want to submit directly ?', QMessageBox.Yes |QMessageBox.No, QMessageBox.Yes) == QMessageBox.No:
                return
        # 拼装元数据
        # 拼装meta元数据
        data = {
                    "name": self.ui.txtTitle.text(),
                    "metadata": {  # 必须把该集合所需要的必填项的所有元数据都填进去，  todo：
                        "dc.title": [
                            {
                                "value": self.ui.txtTitle.text(),
                                "language": "Zh_CN",
                                "authority": "null",
                                "confidence": -1
                            }
                        ],
                        "dc.contributor.author": [
                            {
                                "value": self.ui.txtAuthor.text(),
                                "language": "Zh_CN",
                                "authority": "null",
                                "confidence": -1
                            }
                        ],
                        "dc.subject": [
                            {
                                "value": self.ui.txtSubject.text(),
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ],
                        "dc.subject.other": [
                            {
                                "value": self.ui.txtKeyWords.text(),
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ],
                        "dc.creator": [
                            {
                                "value": self.ui.txtCreator.text(),
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ],
                        "dc.contributor.other": [
                            {
                                "value": self.ui.txtProducer.text(),
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ],
                        "dc.date.created": [
                            {
                                "value": self.ui.txtCreateDate.text(),
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ],
                        "dc.date": [
                            {
                                "value": self.ui.txtModDate.text(),
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ],
                        "dc.date.submitted": [
                            {
                                "value": time.strftime("%Y-%m-%d",time.localtime(time.time())),
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ],
                        "dc.rights": [
                            {
                                "value": "Upload",
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ],
                        "dspace.entity.type": [
                            {
                                "value": 'Publication',
                                "language": "zh_CN",
                                "authority": 'null',
                                "confidence": -1
                            }
                        ]
                    },
                    "inArchive": "true",
                    "discoverable": "true",
                    "withdrawn": "false",
                    "type": "item"
                }
        newItem = myservice.client.createItemWithJson(self.collectionId, data)
        newBundle = myservice.client.createBundle(newItem.uuid, "ORIGINAL")
        self.bundleuuid = newBundle.uuid;
        self.myThread = threading.Thread(target=self.uploadInThread())
        self.myThread.start()
        pass

        # 线程函数，执行上传
    def uploadInThread(self):
            try:

                myservice.client.createBitstream(self.bundleuuid, util.getFileName(self.fileName), self.fileName, self.showProgress)
            except Exception as e:
                traceback.format_exc()
                myservice.logger.error(self.fileName+" upload failed!\r\n"+traceback.format_exc())

    def showProgress(self, monitor):
            QApplication.processEvents()  # 防止界面被卡死
            progress = round(monitor.bytes_read / monitor.len * 100, 2)
            self.ui.progressBar.setValue(progress)
            # print(progress)
            if progress >= 100:
                self.state = 1
                # 改变上传按钮的图标

            pass
    # 全屏的响应函数
    def handleFullscreenRequest(self, request):
            print("requested")
            if (request.toggleOn()):
                request.accept()
                self.ui.horizontalLayout.removeWidget(self.browser)
                self.browser.setParent(None, QtCore.Qt.Window)
                self.browser.showFullScreen()
            else:
                request.accept()
                self.ui.horizontalLayout.addWidget(self.browser)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = PdfSubmitWidget()
    dfe.show()

    sys.exit(app.exec_())
