"""
    单个提取excel的界面，包括提取参数的设置

"""
import os
import sys

import camelot
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QVariant, Qt, QUrl, QThread
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox

import myservice
from pandasgui.store import PandasGuiDataFrameStore
from pandasgui.widgets.dataframe_explorer import DataFrameExplorer
from ui.ui_pdf_extract_excel import Ui_PdfExtractExcel

class DspaceTreeItem(object):

    def __init__(self, dso, parent=None):
        self.mParent = parent
        self.dso = dso
        self.mChilds = []
        self.mType = self.dso.type
        self.mValue = self.dso.name
        self.refreshChildren()

    def refreshChildren(self):
        self.mChilds.clear()
        # self.kNode._children.clear()
        # 判断类型
        if self.dso.type.lower() == "collection":
            rtnList = myservice.client.getCollectionItems(self.dso.uuid)
            for r in rtnList:
                tnode = DspaceTreeItem(r, self)
                self.appendChild(tnode)
        elif self.dso.type.lower() == "item":
            # 此时需要遍历下面所有的附件
            bundle = myservice.client.getItemBundle(self.dso.uuid,"ORIGINAL")
            bsList = myservice.client.getBitstreams(bundle.getBitstreamsLink())
            for bs in bsList:
                tnode = DspaceTreeItem(bs, self)
                self.appendChild(tnode)

    def appendChild(self, item):
        self.mChilds.append(item)

    def child(self, row: int):
        return self.mChilds[row]

    def parent(self):
        return self.mParent

    def childCount(self):
        return len(self.mChilds)

    def row(self):
        if self.mParent is not None:
            return self.mParent.mChilds.index(self)
        return 0

    def setKey(self, key: str):
        self.mKey = key

    def setValue(self, value: str):
        self.mValue = value

    def setType(self, type):
        self.dso.type = type

    def key(self):
        return self.mKey

    def value(self):
        return self.mValue

    def type(self):
        return self.dso.type


class DspaceTreeModel(QAbstractItemModel):
    def __init__(self, col_uuid, parent=None):
        super().__init__(parent)
        col = myservice.client.getCollectionByUuid(col_uuid)
        self.mRootItem = DspaceTreeItem(col)
        self.mHeaders = ["Name", "type"]



    def data(self, index: QModelIndex, role: int = ...):
        if not index.isValid():
            return QVariant()

        item = index.internalPointer()
        col = index.column()

        if role == Qt.DisplayRole:
            if col == 0:
                return str(item.value())
            elif col == 1:

                return str(item.type())
        if role == Qt.DecorationRole:
            if item.type().lower() == "bitstream":
                  return QtGui.QIcon("./res/PDF.png")
            # if item.type() == KNodeType.PROP.value:
            #     return QtGui.QIcon("./res/prop.png")
            # if item.type() == KNodeType.CLASSIFY.value:
            #     return QtGui.QIcon("./res/classify.png")
            if item.type().lower() == "item":
                return QtGui.QIcon("./res/item.png")

        return QVariant()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:
            return self.mHeaders[section]

        return QVariant()

    def index(self, row: int, column: int, parent: QModelIndex = ...):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.mRootItem
        else:
            parentItem = parent.internalPointer()
        try:
            childItem = parentItem.child(row)
            return self.createIndex(row, column, childItem)
        except IndexError:
            return QModelIndex()

    def parent(self, index: QModelIndex):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.mRootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent: QModelIndex = ...):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.mRootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def columnCount(self, parent: QModelIndex = ...):
        return 2

class PdfExtractExcelWidget(QWidget):
    ui = Ui_PdfExtractExcel()
    col_uuid = "c04dce5a-2f71-4ef9-a872-b55f290511d2"
    def __init__(self,parent=None):
        super(PdfExtractExcelWidget, self).__init__(parent)
        self.setupUi()
        # 初始化

        self.thread4tree = WorkerThread4Tree(self.col_uuid)
        self.thread4tree.finishSignal.connect(self.doFinishBuild)
        if hasattr(myservice, "main_window"):
            self.thread4tree.statusSignal.connect(myservice.main_window.workerStatus)
        if hasattr(myservice, "loading_mask"):
            self.thread4tree.finishSignal.connect(myservice.loading_mask.hide)
            myservice.loading_mask.show()
        self.thread4tree.start()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 初始化浏览器组件
        Url = 'https://petrology.deep-time.org/pdfjs/web/viewer.html'
        self.ui.browser.setUrl(QtCore.QUrl(Url))
        self.ui.browser.page().fullScreenRequested.connect(self.handleFullscreenRequest)
        self.ui.browser.settings().globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.ui.browser.settings().globalSettings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.ui.browser.settings().globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.ui.browser.settings().globalSettings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls,
                                                                 True)

        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.treeView.doubleClicked.connect(self.treeDoubleClick)
        self.ui.btnExtract.clicked.connect(self.doExtract)
        self.ui.btnChooseFile.clicked.connect(self.doChooseFile)

    def doFinishBuild(self):
        if hasattr(self.thread4tree,"model"):
            self.ui.treeView.setModel(self.thread4tree.model)
            # 调整第一列的宽度
            self.ui.treeView.header().resizeSection(0, 300)
    def doExtract(self):
        # 处理参数，暂缺 todo

        # 检查是否存在文件
        if self.ui.lblFile.text() == "":
            QMessageBox.information(self, "Tips", "Please choose pdf file first.", QMessageBox.Yes, QMessageBox.Yes)
            return
        # 开始处理，启动线程
        self.thread = WorkerThread(self.ui.lblFile.text())
        self.thread.finishSignal.connect(self.doFinishExtract)
        if hasattr(myservice,"main_window"):
            self.thread.statusSignal.connect(myservice.main_window.workerStatus)
        if hasattr(myservice,"loading_mask"):
            self.thread.finishSignal.connect(myservice.loading_mask.hide)
            myservice.loading_mask.show()
        self.thread.start()
        pass

    # 从线程中提取tables
    def doFinishExtract(self,msg):

        # 移除已有的tab页
        # 移除掉已有的tab
        for i in range(self.ui.tabWidget.count() - 1, -1, -1):
            self.ui.tabWidget.removeTab(i)
        self.tables = self.thread.tables

        for tpos in range(0, len(self.tables) - 1):  # 确保从前往后的顺序
            df = self.tables[tpos].df
            tab_name = f"page-{self.tables[tpos].page}-table-{self.tables[tpos].order}"
            pgdfs = PandasGuiDataFrameStore(df, tab_name)
            dfe = DataFrameExplorer(pgdfs)
            self.ui.tabWidget.addTab(dfe, tab_name)


    def doChooseFile(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "Choose Paper or Report", os.getcwd(),
                                                         "PDF Files(*.pdf)")
        if fileName is not None:
            self.ui.lblFile.setText(fileName)
            self.ui.browser.setUrl(QUrl.fromLocalFile(fileName))

        pass

    # 全屏的响应函数
    def handleFullscreenRequest(self, request):
            print("requested")
            if (request.toggleOn()):
                request.accept()
                #self.ui.splitter.removeWidget(self.browser)
                self.ui.browser.setParent(None, QtCore.Qt.Window)
                self.ui.browser.showFullScreen()
            else:
                request.accept()
                self.ui.browser.setParent(self.ui.splitter)
                #self.ui.splitter.addWidget(self.browser)

    def treeDoubleClick(self, index):
            item = index.internalPointer()
            # print(item.dso.__dict__)
            if item.type().lower() == "bitstream":
                #myservice.loading_mask.show()
                self.ui.lblFile.setText(item.dso.getContentLink())
                print(item.dso.getContentLink())
                self.ui.browser.setUrl(QUrl('https://petrology.deep-time.org/pdfjs/web/viewer.html?file='+item.dso.getContentLink()))
                #self.ui.browser.setUrl(QUrl.fromUserInput())
                #myservice.loading_mask.hide()
# 后台线程,避免界面卡顿
class  WorkerThread4Tree(QThread):

    finishSignal = QtCore.pyqtSignal(str)  # 完成信号
    statusSignal = QtCore.pyqtSignal(str)  # 注册过程状态信号

    def __init__(self,col_uuid,parent=None):
        super(WorkerThread4Tree, self).__init__(parent)
        self.col_uuid = col_uuid

        pass
    # 处理提交到db的操作
    def run(self):
        self.statusSignal.emit("building tree model for："+self.col_uuid)
        myservice.logger.info("building tree model for："+self.col_uuid)
        try:
            self.model = DspaceTreeModel(self.col_uuid)
            self.finishSignal.emit("building tree model for："+self.col_uuid)
            myservice.logger.info("building tree model for："+self.col_uuid)
        except Exception as ex:
            import traceback
            msg = traceback.format_exc()
            myservice.logger.critical(msg)
            self.statusSignal.emit("building tree model Error :"+msg)
            self.finishSignal.emit("building tree model Error :"+msg)

class  WorkerThread(QThread):

    finishSignal = QtCore.pyqtSignal(str)  # 完成信号
    statusSignal = QtCore.pyqtSignal(str)  # 注册过程状态信号
    def __init__(self,filePath,parent=None):
        super(WorkerThread, self).__init__(parent)
        self.filePath = filePath
        self.tables = []
        pass
    # 处理提交到db的操作
    def run(self):
        self.statusSignal.emit("Extract start："+self.filePath)
        myservice.logger.info("Extract start："+self.filePath)
        try:
            self.tables = camelot.read_pdf(self.filePath, flavor='lattice',pages="all", encoding='gbk',flag_size=True,strip_text='\n',copy_text=['v'],line_scale=40)

            self.finishSignal.emit("Extract finished:"+self.filePath)
            myservice.logger.info("Extract finished:"+self.filePath)
        except Exception as ex:
            import traceback
            msg = traceback.format_exc()
            myservice.logger.error(msg)
            self.statusSignal.emit("Error :"+msg)
            self.finishSignal.emit("Error :"+msg)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = PdfExtractExcelWidget()
    dfe.show()

    sys.exit(app.exec_())
