
'''

    直接树形结构展示KNode知识结点

'''

import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt, QAbstractListModel, QMimeData, \
    QDataStream, QByteArray, QJsonDocument, QVariant, QJsonValue, QJsonParseError
from PyQt5.QtWidgets import QApplication, QFileDialog, QTreeView




# 用KNode构建treeItem
from model.KnowledgeNode import KNodeType, KnowledgeNode,ValueType
from myservice import arango


class KTreeItem(object):

    def __init__(self,knode,parent=None):
        self.mParent = parent
        self.k_node=knode
        self.mChilds = []
        #self.mKey=self.kNode.uuid
        self.mType =self.k_node.type
        self.mValue =self.k_node.name
        self.refreshChildren()

    def refreshChildren(self):
        self.mChilds.clear()
        # self.kNode._children.clear()
        self.k_node._children=arango.fetchChildrenKNodeByParent(parent_uuid=self.k_node.uuid)
        for k in self.k_node._children:
            tnode=KTreeItem(k,self)
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

    def setKey(self, key:str):
        self.mKey = key

    def setValue(self, value:str):
        self. mValue = value

    def setType(self, type:KNodeType):
        self.k_node.type = type

    def setValueType(self,value_type:ValueType):
        self.k_node.value_type = value_type

    def setOrder(self,order):
        self.k_node.order = order

    def key(self):
        return self.mKey

    def value(self):
        return self.mValue

    def type(self):
        return self.k_node.type

    def valueType(self):
        return self.k_node.value_type

    def order(self):
        return self.k_node.order



class KTreeModel(QAbstractItemModel):
    def __init__(self, knode,parent =None):
        super().__init__(parent)
        self.mRootItem = KTreeItem(knode)
        self.mHeaders = ["Name","Type","Value type","Order"]


    def setKNode(self, knode):

        if knode is not None:
            self.beginResetModel()
            self.mRootItem=KTreeItem(knode)
            self.endResetModel()

            return True

        print("初始化加载知识树结点")
        return False

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
            elif col == 2:
                return str(item.valueType())
            elif col ==3:
                return str(item.order())
        if role == Qt.DecorationRole:
            if item.type() == KNodeType.DIR.value:
                return QtGui.QIcon("./res/dir.png")
            if item.type() == KNodeType.PROP.value:
                return QtGui.QIcon("./res/prop.png")
            if item.type() == KNodeType.CLASSIFY.value:
                return QtGui.QIcon("./res/classify.png")
            if item.type() == KNodeType.ENTITY.value:
                return QtGui.QIcon("./res/entity.png")


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

        return self.createIndex(parentItem.row(),0, parentItem)

    def rowCount(self, parent: QModelIndex = ...):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.mRootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def columnCount(self, parent: QModelIndex = ...):
        return 4


if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = QTreeView()
    view.setDragEnabled(True)
    knode=KnowledgeNode()
    knode.name="岩浆岩"
    knode.type=KNodeType.DIR
    knode.uuid = "ROOT"

    model = KTreeModel(knode)
    #model.setKNode(knode)
    view.setModel(model)

    view.show()
    view.resize(520, 435)

    sys.exit(app.exec_())

