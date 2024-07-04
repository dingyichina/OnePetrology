'''

   本类用来展示知识体系的树形结构
   author :dingyi

   2021-12-19

'''
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QStyleFactory, QMessageBox
from PyQt5.QtCore import *

import myservice
from KNodeEditDlg import EditKNodeDlg
from model.KTreeModel import KTreeModel
from model.KnowledgeNode import KnowledgeNode, KNodeType
from ui.ui_KTree import Ui_KTree
import sys
from KNodeAddDlg import AddKNodeDlg
from myservice import arango


class KTreeWidget(QWidget):

    def __init__(self, parent=None):
        super(KTreeWidget, self).__init__(parent)
        self.ui = Ui_KTree()
        self.setWindowTitle('Knowledge Tree')
        self.setupUi()
        self.parent = parent
        # 初始化构建树
        self.refreshTree()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.btnRefresh.clicked.connect(self.refreshTree)  # 刷新树形结构
        self.ui.btnAdd.clicked.connect(self.addTreeNode)  # 添加子节点
        self.ui.btnModify.clicked.connect(self.editTreeNode)
        self.ui.btnDelete.clicked.connect(self.deleteNode)

        # 设置右键菜单
        self.ui.treeView.addAction(self.ui.actionRefresh)
        self.ui.treeView.addAction(self.ui.actionAdd)
        self.ui.treeView.addAction(self.ui.actionEdit)
        self.ui.treeView.addAction(self.ui.actionDelete)

        self.ui.actionAdd.triggered.connect(self.addTreeNode)
        self.ui.actionEdit.triggered.connect(self.editTreeNode)
        self.ui.actionRefresh.triggered.connect(self.refreshCurNode)
        self.ui.actionDelete.triggered.connect(self.deleteNode)

        # 关联双击事件，主要是刷新选中节点下属的子节点
        # self.ui.treeView.doubleClicked.connect(self.treeDoubleClicked)

    # 添加子节点
    def addTreeNode(self):
        # 首先检查tree的选择是否为空
        index = self.ui.treeView.currentIndex()
        kNode = self.knode
        if index.internalPointer() == None:
            if QMessageBox.question(self, 'Question', 'Are you want to create a root Node?\r\n',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.No:
                return
        else:
            kNode = index.internalPointer().k_node
        # type = index.model().data(index, Qt.ItemDataRole.UserRole + 1)
        # name=index.model().data(index, Qt.ItemDataRole.UserRole + 2)
        if kNode.type in ["Float", "String"]:
            QMessageBox.information(self, 'Tips',
                                    'Can not add below the leaf Node。\r\n you can create the directory node first!',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes)
            return
        # 展开添加子节点的ui
        dlg = AddKNodeDlg(kNode, self,isROOT=True)
        dlg.show()
        # 从dlg中获取Knode，添加到对应的位置

    def editTreeNode(self):
        # 首先检查tree的选择是否为空
        # 首先检查tree的选择是否为空
        index = self.ui.treeView.currentIndex()
        self.curNode = self.knode
        if index.internalPointer() == None:
            QMessageBox.critical(self, 'ERROR', 'please select the  node first。\r\n', QMessageBox.Yes,
                                 QMessageBox.Yes)
            return
        else:
            self.curNode = index.internalPointer().k_node
        dlg = EditKNodeDlg(self.curNode, self)
        dlg.show()

    # 得到当前选中的知识结点
    def getCurKNode(self):
        index = self.ui.treeView.currentIndex()
        if index is None:
            return None
        else:
            if index.internalPointer() == None:
                return None
            else:
                return index.internalPointer().k_node

    # 删除节点
    def deleteNode(self):
        index = self.ui.treeView.currentIndex()
        if index is None:
            return
        else:
            if index.internalPointer() == None:
                return
            else:
                # 删除操作不可恢复，需要反复提示
                if QMessageBox.question(self, 'Question',
                                        'Delete can not be restored. Are you sure to delete  Node 《 ' + index.internalPointer().k_node.name + " 》 ?\r\n",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.No:
                    return

                index.model().beginResetModel()
                parent = index.parent()
                arango.deleteKNode(index.internalPointer().k_node)
                if parent.internalPointer() is None:
                    self.refreshTree()
                else:
                    parent.internalPointer().refreshChildren()
                index.model().endResetModel()
                self.ui.treeView.setCurrentIndex(parent)
                self.ui.treeView.expand(parent)

    # 只刷新当前选中的节点的下属节点
    def refreshCurNode(self):
        index = self.ui.treeView.currentIndex()
        index.model().beginResetModel()
        index.internalPointer().refreshChildren()
        index.model().endResetModel()
        self.ui.treeView.setCurrentIndex(index)
        self.ui.treeView.expand(index)

    # 刷新知识体系结点树
    def refreshTree(self):
        # 设置表头信息
        # model = QStandardItemModel(self)
        # model.setHorizontalHeaderLabels(['Name', 'Type'])
        # 首先获取ktree的根节点名称

        self.knode = KnowledgeNode()  # 不知为何，不能显示根节点，暂时不予理会，回头在处理 todo
        self.knode.name = "DDE-OnePetrology"
        self.knode.type = KNodeType.DIR
        self.knode.uuid = "ROOT"
        self.thread = WorkerThread(self.knode)
        self.thread.finishSignal.connect(self.doFinishBuild)
        if hasattr(myservice, "main_window"):
            self.thread.statusSignal.connect(myservice.main_window.workerStatus)
        if hasattr(myservice, "loading_mask"):
            self.thread.finishSignal.connect(myservice.loading_mask.hide)
            myservice.loading_mask.show()
        self.thread.start()


    def doFinishBuild(self,msg):
        self.ui.treeView.setModel(self.thread.model)
        # 调整第一列的宽度
        self.ui.treeView.header().resizeSection(0, 330)
        # 设置成有虚线连接的方式
        self.ui.treeView.setStyle(QStyleFactory.create('windows'))
        # 完全展开
        self.ui.treeView.expandAll()

        # 显示选中行的信息
        self.ui.treeView.selectionModel().currentChanged.connect(self.onCurrentChanged)
        pass

    # 树形节点选中更新状态栏
    def onCurrentChanged(self, current, previous):
        txt = '父级:[{}] '.format(str(current.parent().data()))
        txt += '当前选中:[(行{},列{})] '.format(current.row(), current.column())

        name = ''
        info = ''
        if current.column() == 0:
            name = str(current.data())
            info = str(current.sibling(current.row(), 1).data())
        else:
            name = str(current.sibling(current.row(), 0).data())
            info = str(current.data())
        txt += '名称:[{}]  类型:[{}]'.format(name, info)
        try:
            self.ui.lblStatus.setText(txt)
            self.parent.parent().statusBar().showMessage(txt)
        except Exception as e:
            print(e)

# 后台线程,避免界面卡顿
class  WorkerThread(QThread):

    finishSignal = QtCore.pyqtSignal(str)  # 完成信号
    statusSignal = QtCore.pyqtSignal(str)  # 注册过程状态信号

    def __init__(self,knode,parent=None):
        super(WorkerThread, self).__init__(parent)
        self.knode = knode

        pass
    # 处理提交到db的操作
    def run(self):
        self.statusSignal.emit("ROOT Knowledge Tree building start from："+self.knode.name)
        myservice.logger.info("ROOT Knowledge Tree building start from："+self.knode.name)
        try:
            knodelist = arango.fetchChildrenKNodeByParent(parent_uuid=self.knode.uuid)  # 默认目前已经可以取完全
            for k in knodelist:
                self.knode._children.append(k)
            self.model = KTreeModel(self.knode)
            self.finishSignal.emit("ROOT Knowledge Tree building  finished:"+self.knode.name)
            myservice.logger.info("ROOT Knowledge Tree building  finished:"+self.knode.name)
        except Exception as ex:
            import traceback
            msg = traceback.format_exc()
            myservice.logger.error(msg)
            self.statusSignal.emit("ROOT Knowledge Tree building Error :"+msg)
            self.finishSignal.emit("ROOT Knowledge Tree building Error :"+msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = KTreeWidget()
    appWin.show()

    sys.exit(app.exec_())
