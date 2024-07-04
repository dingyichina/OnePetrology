'''

    按照传统的树形结构进行显示，不参与自定义实体的关联
          Community
              sub community
                  collection
              collection
                  item
                     bundle
                        bitstream
    by：dingyi
    2021-11-27
'''
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QStyleFactory
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *

import TreeBuilder
from myservice import client
from ui.ui_TraditionalTree import Ui_TraditionalTree


class TraditionalTreeWidget(QWidget):
    ui = Ui_TraditionalTree()

    def __init__(self, parent=None):
        super(TraditionalTreeWidget, self).__init__(parent)
        self.setWindowTitle('经典树')
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.btnRefresh.clicked.connect(self.refreshTree)  # 刷新树形结构
        # 关联双击事件，主要是刷新选中节点下属的子节点
        self.ui.treeView.doubleClicked.connect(self.treeDoubleClicked)

    # 刷新树形结构
    def refreshTree(self):
        print('刷新列表结构')
        # self.ui.treeview.setModel()
        # 设置表头信息
        model = QStandardItemModel(self)
        model.setHorizontalHeaderLabels(['名称', '类型'])

        for index, c in enumerate(client.getCommunities()):
            community = TreeBuilder.getCommunityItem(c)
            model.appendRow(community)
            model.setItem(index, 1, TreeBuilder.getTypeItem(c.type))
            # print('社区：', c.name)
            for sindex, s in enumerate(client.getSubCommunities(c.getSubCommunitiesLink())):
                subCommunity = TreeBuilder.getCommunityItem(s)
                community.appendRow(subCommunity)
                community.setChild(sindex, 1, TreeBuilder.getTypeItem(s.type))
                # print('  子社区:', s.name)
            for colIndx, col in enumerate(client.getCollectionsByUrl(c.getCollectionsLink())):
                collection = TreeBuilder.getCollectionItem(col)
                community.appendRow(collection)
                community.setChild(colIndx, 1, TreeBuilder.getTypeItem(col.type))
                ''' #默认不展开到item级别，需要双击collection才可以看到子节点。避免因为数据过多导致卡死。
                for itemIndex,i in  enumerate(client.getCollectionItems(col.uuid)):
                    item=TreeBuilder.getItemItem(i)
                    collection.appendRow(item)
                    collection.setChild(itemIndex,1,TreeBuilder.getTypeItem(i.type))
                    #print('      条目:', i.name)
                '''
        self.ui.treeView.setModel(model)
        # 调整第一列的宽度
        self.ui.treeView.header().resizeSection(0, 400)
        # 设置成有虚线连接的方式
        self.ui.treeView.setStyle(QStyleFactory.create('windows'))
        # 完全展开
        self.ui.treeView.expandAll()

        # 显示选中行的信息
        self.ui.treeView.selectionModel().currentChanged.connect(self.onCurrentChanged)

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
        self.statusBar().showMessage(txt)

    # 双击树中的某一个节点
    def treeDoubleClicked(self):
        # 读取选中节点的数据
        index = self.ui.treeView.currentIndex()
        uuid = index.model().data(index, Qt.ItemDataRole.UserRole)
        type = index.model().data(index, Qt.ItemDataRole.UserRole + 1)

        # 清除当前的所有子节点，然后根据type调用对应函数进行重新填充
        while index.model().hasChildren(index):
            # print('有子节点')
            # 删除所有子节点，并重新获取
            index.model().removeRow(0, index)

        # 重新刷新
        TreeBuilder.getChildrenItem(uuid, type, index.model().itemFromIndex(index))
        # 发射左侧树形结构的双击信号
        self.parent().parent().signal_tree_double_clicked.emit(uuid, type)
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
            self.parent().parent().statusBar().showMessage(txt)  # 注意此处需要通过两次parent获取到mainwindow
        except:
            print()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = TraditionalTreeWidget()
    dfe.show()

    sys.exit(app.exec_())
