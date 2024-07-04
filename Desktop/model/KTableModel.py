'''
    用于显示已经通过知识树构建好的entity对象

    知识树对应的tablemodel，修改于pandastablemodel

    作者：丁毅
    2022-01-27
'''
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex, QVariant
from PyQt5.QtGui import QColor


class KTableModel(QAbstractTableModel):

    def __init__(self, k_node):
        QAbstractTableModel.__init__(self)
        self.df = k_node.df
        self.deep_level = k_node.deep_level
        self.k_node = k_node

    def rowCount(self, parent=None):
        return self.df.shape[0]

    def columnCount(self, parnet=None):
        return self.df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                v=self.df.iloc[index.row(), index.column()]
                if v is None:
                    return QVariant()
                else:
                    return str(v)
            elif role == Qt.BackgroundRole:
                if index.row()<self.k_node.deep_level:
                    return QColor("#76b87d")
                elif index.row()<self.k_node.deep_level+2:
                    return QColor(Qt.yellow)
                else:
                    return QColor(Qt.white)
            elif role == Qt.TextAlignmentRole:
                return Qt.AlignCenter
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