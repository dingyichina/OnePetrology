'''

    左侧显示来自于dspace 集合的文件列表，右侧显示对应的exceProcessWidget

'''
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QVariant, Qt, QThread
from PyQt5.QtWidgets import QWidget

import myservice
from ui.ui_process_excel import Ui_ProcessExcel


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
            try:
                bundle = myservice.client.getItemBundle(self.dso.uuid,"ORIGINAL")
                bsList = myservice.client.getBitstreams(bundle.getBitstreamsLink())
                for bs in bsList:
                    tnode = DspaceTreeItem(bs, self)
                    self.appendChild(tnode)
            except Exception as  ex:
                print(ex)
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
                  return QtGui.QIcon("./res/excel.png")
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


class ProcessExcelWidget(QWidget):
    ui = Ui_ProcessExcel()
    col_uuid = "a6c00453-2942-460a-ae2f-52d601a501bf"
    def __init__(self, parent=None):
        super(ProcessExcelWidget, self).__init__(parent)
        self.setupUi()
        # 初始化
        # 绑定的集合ID:  a6c00453-2942-460a-ae2f-52d601a501bf
        self.thread = WorkerThread(self.col_uuid)
        self.thread.finishSignal.connect(self.doFinishBuild)
        if hasattr(myservice, "main_window"):
            self.thread.statusSignal.connect(myservice.main_window.workerStatus)
        if hasattr(myservice, "loading_mask"):
            self.thread.finishSignal.connect(myservice.loading_mask.hide)
            myservice.loading_mask.show()
        self.thread.start()

    def doFinishBuild(self):
        self.ui.treeView.setModel(self.thread.model)
        # 调整第一列的宽度
        self.ui.treeView.header().resizeSection(0, 300)

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 链接处理函数
        self.ui.treeView.doubleClicked.connect(self.treeDoubleClick)

    def treeDoubleClick(self,index):
        item = index.internalPointer()
        # print(item.dso.__dict__)
        if item.type().lower() == "bitstream":
            myservice.loading_mask.show()
            self.ui.widget.setFilePath(item.dso.getContentLink())
            myservice.loading_mask.hide()

# 后台线程,避免界面卡顿
class  WorkerThread(QThread):

    finishSignal = QtCore.pyqtSignal(str)  # 完成信号
    statusSignal = QtCore.pyqtSignal(str)  # 注册过程状态信号

    def __init__(self,col_uuid,parent=None):
        super(WorkerThread, self).__init__(parent)
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = ProcessExcelWidget()
    dfe.show()

    sys.exit(app.exec_())
