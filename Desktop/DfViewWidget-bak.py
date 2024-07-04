"""
    显示一个Dataframe，并允许编辑
    k_node被调用设置之前，必须已经填充好如下属性：
        1， deep_level ，即除了叶子节点之外的深度
        2, leaf_list,  所有叶子节点，即最后的带有表头信息的列表（已经按照order 排完序），每个叶子节点还有要给pth属性，是自己到entity根节点的路径（自下而上）
        3，df, 即 dataframe，用所有叶子节点按照顺序构成的所有的列的column

    功能：
        1，用冻结表头方式显示层次结构，显示到叶子节点名称

    经过操作之后，k_node有可能被改变的属性：
        1，左侧增加冻结 frozen_df
        2，

    作者：丁毅
    2022-01-27

"""
import sys

import typing
from PyQt5.QtCore import Qt, QModelIndex, QAbstractTableModel, QVariant
from PyQt5.QtGui import QColor, QResizeEvent
from PyQt5.QtWidgets import QWidget, QApplication, QItemDelegate, QStyle, QStyleOptionViewItem, QTableView, \
    QAbstractItemView, QFrame, QHeaderView

from myservice import arango
from ui.ui_dfview import Ui_DfView
from util import pandasModel


class VerticalHeaderDelegate(QItemDelegate):
    def paint(self, painter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        if option.state & QStyle.State_HasFocus:
            option.state = option.state ^ QStyle.State_HasFocus
        super(VerticalHeaderDelegate, self).paint(painter, option, index)

# 垂直显示冻结表头，默认显示索引号，当有冻结列出现时，重新摆布
class VerticalHeaderModel(QAbstractTableModel):
    def __init__(self, k_node , parent=None):
        super().__init__(parent)
        self.k_node = k_node

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return  100 #self.k_node.df.shape[0]-self.k_node.deep_level

    def columnCount(self, parent: QModelIndex = ...) -> int:
        if hasattr(self.k_node,"frozen_df"):
            self.k_node.frozen_df.shape[1]+1
        else:
            return 1  #默认只有索引列

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            if(index.column()==0):
                return  str(index.row())
            elif hasattr(self.k_node.frozen_df):
                return self.k_node.frozen_df.iloc[index.row(), index.column()]
            else:
                return QVariant()
        elif role == Qt.BackgroundRole:
            return QColor(Qt.green)
        return QVariant()

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return super().flags(index)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return QVariant("Index")
        return QVariant()


class VerticalHeaderView(QTableView):
    def __init__(self, k_node,parent=None):
        super().__init__(parent)
        self.setModel(VerticalHeaderModel(k_node,self))
        self.verticalHeader().setVisible(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置单元格不可编辑
        self.setFocusPolicy(Qt.NoFocus)  # 解决选中虚框问题
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.setFrameShape(QFrame.NoFrame)

        self.setItemDelegate(VerticalHeaderDelegate(self))
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setSelectionMode(QAbstractItemView.SingleSelection)


class HorizontalHeaderModel(QAbstractTableModel):
    def __init__(self, k_node,parent=None):
        super().__init__(parent)
        self.k_node = k_node

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self.k_node.deep_level+1

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self.k_node.df.shape[1]

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            return str(self.k_node.df.iloc[index.row(), index.column()])
        elif role == Qt.BackgroundRole:
            return QColor("#96b8ed")
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return QVariant()

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return super().flags(index)

# 顶端被锁定的表头
class HorizontalHeaderView(QTableView):
    def __init__(self,k_node, parent=None):
        super().__init__(parent)
        self.setModel(HorizontalHeaderModel(k_node,self))
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setFrameShape(QFrame.NoFrame)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置单元格不可编辑
        self.setFocusPolicy(Qt.NoFocus)  # 解决选中虚框问题
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

        # 合并表头待修改  todo
        self.setSpan(0, 0, 2, 1)
        self.setSpan(0, 1, 1, 2)
        self.setSpan(1, 3, 1, 2)




class KTableModel(QAbstractTableModel):

    def __init__(self, k_node):
        QAbstractTableModel.__init__(self)
        self.df = k_node.df
        self.k_node = k_node
        self.deep_level = k_node.deep_level

    def rowCount(self, parent=None):
        return self.df.shape[0]-self.k_node.deep_level-2

    def columnCount(self, parnet=None):
        return self.df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.df.iloc[index.row()-self.deep_level-2, index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.df.columns[col]
        return None

    # 以下为编辑功能所必须实现的方法
    def setData(self, index, value, role=Qt.EditRole):
        # 编辑后更新模型中的数据 View中编辑后，View会调用这个方法修改Model中的数据
        if index.isValid() and 0 <= index.row() < len(self.df) and value:
            col = index.column()
            print(col)
            if 0 < col < len(self.headers):
                self.beginResetModel()
                # if CONVERTS_FUNS[col]:  # 必要的时候执行数据类型的转换
                #     self.datas[index.row()][col] = CONVERTS_FUNS[col](value)
                # else:
                self.datas[index.row()][col] = value
                self.dirty = True
                self.endResetModel()
                return True
        return False

    def flags(self, index):  # 必须实现的接口方法，不实现，则View中数据不可编辑
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(
            QAbstractTableModel.flags(self, index) |
            Qt.ItemIsEditable | Qt.ItemIsSelectable)

    def insertRows(self, position, rows=1, index=QModelIndex()):
        # position 插入位置；rows 插入行数
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        pass  # 对self.datas进行操作
        self.endInsertRows()
        self.dirty = True
        return True

    def removeRows(self, position, rows=1, index=QModelIndex):
        # position 删除位置；rows 删除行数
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        pass  # 对self.datas进行操作
        self.endRemoveRows()
        self.dirty = True
        return True


class DfViewWidget(QWidget):
    ui = Ui_DfView()

    def __init__(self, parent=None):
        super(DfViewWidget, self).__init__(parent)
        self.setWindowTitle('DataFrame View')
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    # 设置进来的entity节点，必须首先被填充好df数据
    def setModel(self, k_node):
        model = KTableModel(k_node)
        self.ui.tableView.setModel(model)

        self.ui.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ui.tableView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        # 1、水平表头
        self.horizontalHeaderView = HorizontalHeaderView(k_node,self.ui.tableView)

        self.ui.tableView.viewport().stackUnder(self.horizontalHeaderView)
        self.ui.tableView.horizontalScrollBar().valueChanged.connect(self.horizontalHeaderView.horizontalScrollBar().setValue)
        self.horizontalHeaderView.horizontalScrollBar().valueChanged.connect(self.ui.tableView.horizontalScrollBar().setValue)

        # 2、垂直表头
        self.verticalHeaderView = VerticalHeaderView(k_node,self.ui.tableView)

        self.ui.tableView.viewport().stackUnder(self.verticalHeaderView)
        self.ui.tableView.verticalScrollBar().valueChanged.connect(self.verticalHeaderView.verticalScrollBar().setValue)
        self.verticalHeaderView.verticalScrollBar().valueChanged.connect(self.ui.tableView.verticalScrollBar().setValue)

        # 3、微调
        headerHeight = 0
        for row in range(self.horizontalHeaderView.model().rowCount()):
            headerHeight += self.verticalHeaderView.rowHeight(row)
        self.ui.tableView.horizontalHeader().setFixedHeight(headerHeight)

        headerWidth = 0
        for row in range(self.verticalHeaderView.model().columnCount()):
            headerWidth += self.verticalHeaderView.columnWidth(row)
        self.ui.tableView.verticalHeader().setFixedWidth(headerWidth)
        self.ui.tableView.horizontalHeader().setFixedHeight(headerHeight)

        self.__updateHorizontalTableGeometry()
        self.__updateVerticalTableGeometry()

        pass

    def __updateVerticalTableGeometry(self):
        x = self.ui.tableView.frameWidth()
        y = self.ui.tableView.frameWidth()
        width = self.ui.tableView.verticalHeader().width()
        height = self.ui.tableView.viewport().height() + self.ui.tableView.horizontalHeader().height()
        self.verticalHeaderView.setGeometry(x, y, width, height)

    def __updateHorizontalTableGeometry(self):
        x = self.ui.tableView.frameWidth() + self.ui.tableView.verticalHeader().width()
        y = self.ui.tableView.frameWidth()
        width = self.ui.tableView.viewport().width()
        height = self.ui.tableView.horizontalHeader().height()
        self.horizontalHeaderView.setGeometry(x, y, width, height)


    def resizeEvent(self, e: QResizeEvent):
        super().resizeEvent(e)
        if hasattr(self,"horizontalHeaderView"):
            self.__updateHorizontalTableGeometry()
        if hasattr(self,"verticalHeaderView"):
            self.__updateVerticalTableGeometry()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = DfViewWidget()
    appWin.show()
    # 查找sample，然后把它设置进去
    k_node = arango.fetchKNodeByUUID('3ff8bfd3-fb43-49c9-9bff-b9276593dede')
    arango.getEntityDf(k_node)
    appWin.setModel(k_node)
    sys.exit(app.exec_())
