'''

    按照关联数据的结构进行展示树形----本应用定制，不是普适性的，切记切记！！！！！！！！！！！

        科学家1***
           collection1
              item
                bundle
                  bitstream
           ....
           collectionn
        科学2家***
            collection1
           ....
           collectionn
        .。。
        科学家n****
    by：dingyi   todo：待编写。现在的代码不对
    2021-11-27
'''

from PyQt5.QtWidgets import QWidget, QApplication,QStyleFactory
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *

import TreeBuilder,json
from myservice import client
from ui.ui_TraditionalTree import Ui_TraditionalTree

class ScientistTreeWidget(QWidget):

    rootCommunityUUID='2b78969e-1ce9-4204-a46b-9f37a64b596b'
    scientistCollectionUUID='3eab38f6-fac7-4f63-9e54-35200dc7583d'

    ui=Ui_TraditionalTree()

    def __init__(self, parent=None):
        super(ScientistTreeWidget, self).__init__( parent)
        self.setupUi()
        self.setWindowTitle('科学家')

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.btnRefresh.clicked.connect(self.refreshTree)  # 刷新树形结构
        # 关联双击事件，主要是刷新选中节点下属的子节点
        self.ui.treeView.doubleClicked.connect(self.treeDoubleClicked)
    #刷新树形结构
    def refreshTree(self):
        print('刷新科学家视图')
        #self.ui.treeview.setModel()
        # 设置表头信息
        model = QStandardItemModel(self)
        model.setHorizontalHeaderLabels(['名称', '类型'])
        collectionList=client.getCollections(self.rootCommunityUUID)  #根节点特藏社区的uuid

        for index, c in enumerate(client.getCollectionItems(self.scientistCollectionUUID)):  # 科学家的集合 ID
            scientist=TreeBuilder.getScientist(c)
            #print(json.dumps(c.__dict__, indent=4, ensure_ascii=False))
            model.appendRow(scientist)
            model.setItem(index,1,TreeBuilder.getTypeItem('科学家'))
            cIndex=0
            for col in collectionList:
                if(col.uuid!=self.scientistCollectionUUID): #不是科学家本身的集合才可以作为子节点
                    collection = TreeBuilder.getCollectionItem(col)
                    collection.setData(c.name, Qt.ItemDataRole.UserRole + 2)  # 把科学家的名字存起来
                    scientist.appendRow(collection)
                    scientist.setChild(cIndex, 1, TreeBuilder.getTypeItem(col.type))
                    cIndex+=1

        self.ui.treeView.setModel(model)
        # 调整第一列的宽度
        self.ui.treeView.header().resizeSection(0, 400)
        # 设置成有虚线连接的方式
        self.ui.treeView.setStyle(QStyleFactory.create('windows'))
        # 完全展开
        self.ui.treeView.expandAll()

        # 显示选中行的信息
        self.ui.treeView.selectionModel().currentChanged.connect(self.onCurrentChanged)

        #关联双击事件，主要是刷新选中节点下属的子节点
        #self.ui.treeView.doubleClicked.connect(self.treeDoubleClicked)

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
        self.parent().parent().statusBar().showMessage(txt)
    #双击树中的某一个节点
    def treeDoubleClicked(self):
        #读取选中节点的数据
        index=self.ui.treeView.currentIndex()
        uuid=index.model().data(index,Qt.ItemDataRole.UserRole)
        type=index.model().data(index,Qt.ItemDataRole.UserRole+1)
        scientistName=index.model().data(index,Qt.ItemDataRole.UserRole+2)

        #只有不是科学家和社区的时候，才可以刷新子树
        if type not in ['科学家']:
            #清除当前的所有子节点，然后根据type调用对应函数进行重新填充
            while index.model().hasChildren(index):
                #print('有子节点')
                #删除所有子节点，并重新获取
                index.model().removeRow(0,index)

            #重新刷新
            TreeBuilder.getChildrenItem(uuid,type,index.model().itemFromIndex(index),scientistName)
        #发射左侧树形结构的双击信号
        self.parent().parent().signal_tree_double_clicked.emit(uuid,type)
        pass