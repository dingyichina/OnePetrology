'''

    在执行plot之前需要对df中的列进行映射，保证必须存在的列都存在才可以执行plot操作


    author:dingyi
    2022-08-19
'''
import os
import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import QAbstractTableModel, QVariant, QModelIndex, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QStyledItemDelegate, QComboBox, QDialog, QMessageBox, QFileDialog

from ColumnConfigWidget import ColumnConfigWidget, ColumnObj
from ui.ui_dfColumnMapping import Ui_dfColumnMapping


# 自定义的tablemodel
class ColumnMappingModel(QAbstractTableModel):

    def __init__(self, columnList):
        QAbstractTableModel.__init__(self)
        self.columnList = columnList
        self.headers = ["Name ", "Desc ", "Data Column Name"]

    def rowCount(self, parent=None):
        return len(self.columnList)

    def columnCount(self, parnet=None):
        return 3

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                if index.column() == 0:
                    return self.columnList[index.row()].name
                elif index.column() == 1:
                    return self.columnList[index.row()].desc
                elif index.column() == 2:
                    return self.columnList[index.row()].dfColumn
                else:
                    return QVariant()

            elif role == Qt.BackgroundRole:
                if self.columnList[index.row()].dfColumn is None:
                    return QColor("#76b87d")
                elif hasattr(self.columnList[index.row()], "ratio"):
                    if self.columnList[index.row()].ratio > 90:
                        return QColor(Qt.yellow)
                    else:
                        return QColor(Qt.red)
                else:
                    return QColor(Qt.white)
            elif role == Qt.TextAlignmentRole:
                return Qt.AlignCenter

        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[col]
        return None

    # 以下为编辑功能所必须实现的方法
    def setData(self, index, value, role=Qt.EditRole):
        # 编辑后更新模型中的数据 View中编辑后，View会调用这个方法修改Model中的数据
        if index.isValid() and 0 <= index.row() < len(self.columnList) and value:
            col = index.column()
            # print(col)
            if 0 < col < len(self.headers):
                self.beginResetModel()
                # if CONVERTS_FUNS[col]:  # 必要的时候执行数据类型的转换
                #     self.datas[index.row()][col] = CONVERTS_FUNS[col](value)
                # else:
                if value == "None":
                    self.columnList[index.row()].dfColumn = None
                else:
                    self.columnList[index.row()].dfColumn = value
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


# 编辑代理类
class MyComboDelegate(QStyledItemDelegate):

    def __init__(self, dfColumns, parent=None):
        super().__init__(parent)
        self.dfColumns = dfColumns

    def createEditor(self, parent, option, index):
        wdgt = QComboBox(parent)
        wdgt.addItem("None")
        for c in self.dfColumns:
            wdgt.addItem(c)
        return wdgt

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.DisplayRole)
        editor.setCurrentText(str(value))

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText())


class DfColumnMappingWidget(QWidget):

    def __init__(self, df, dataList, parent=None):
        self.ui = Ui_dfColumnMapping()
        self.df = df
        if df is None:
            self.dfColumns = None
        else:
            self.dfColumns = df.columns
        super(DfColumnMappingWidget, self).__init__(parent)
        self.setupUi()
        self.columnList = []

        # 初始化
        for data in dataList:
            columnObj = ColumnObj(data["Name"], data["Desc"], data["Type"], data["UseDefault"], data["DefaultValue"])
            self.ui.targetLayout.addWidget(ColumnConfigWidget(columnobj=columnObj, parent=self.ui.targetDataType))
            self.columnList.append(columnObj)
            pass
        #  添加一个空的占位Widget，避免到底不好看
        # self.ui.targetLayout.addWidget(QWidget())

        # 对目标column和df的column进行匹配
        # 直接匹配相等来一遍（忽略了大小写，但没有忽略空格和连接符等）
        for col in self.columnList:
            # 循环遍历是否已经与dfColumns里面的值是否对应上
            col.dfColumn = self.getDfColumn(col.name)
            # print(leaf.dfColumn)

        # 通过计算相似度进行匹配其他的None值，选出一个相似度最高的（阈值设置为90%，只有高于这个才会被选中，其他仍旧设置为None）
        for col in self.columnList:
            if col.dfColumn is None:
                # 尝试用模糊匹配的方式进行匹配  fuzz
                col.dfColumn = self.getDfColumnByRatio(col)

        # 构建model
        model = ColumnMappingModel(self.columnList)
        self.ui.tableView.setModel(model)

        # 设置每一列的宽度，确保美观
        self.ui.tableView.setColumnWidth(0, 220)
        self.ui.tableView.setColumnWidth(1, 320)
        self.ui.tableView.setColumnWidth(2, 320)

        # 设置编辑代理
        delegate = MyComboDelegate(dfColumns=self.dfColumns, parent=self)
        self.ui.tableView.setItemDelegateForColumn(2, delegate)

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 设置处理函数
        self.ui.btnSaveData.clicked.connect(self.doSaveData)
        self.ui.btnDoPlotting.clicked.connect(self.doPlotting)

    # 把数据存到本地，修改后可以再次成图  todo
    def doSaveData(self):
        if not self.getAllColumnObjs():
            return
        if self.makedf():
            # 保存filterDf
            fileNames, fileType = QFileDialog.getSaveFileName(self, "Save to File", os.getcwd(),
                                                              "Excel Files(*.xlsx)")
            if fileNames is None or fileNames == "":
                return
            self.df.to_excel(fileNames, encoding="utf-8", index=None)
            QMessageBox.information(self, 'Tips','File has saved!', QMessageBox.Yes, QMessageBox.Yes)


    def makedf(self):
        # 检查列映射，如果没有选择use default ,则必须有映射；如果既有列映射，也有default，则采用映射
        # 首先把列映射的结果附加到columnObj上面
        for obj in self.columnList:
            if obj.dfColumn is None and obj.use_default == False:
                QMessageBox.information(self, 'Tips',
                                        '{} is not mapping ,and do not have default value. Please modify first.'.format(
                                            obj.name),
                                        QMessageBox.Yes, QMessageBox.Yes)
                return False
        # 所有的要么有了映射列，要么有了default value，此时开始修改df ，直接修改df可能会造成原始df的破坏，要不要重新做一个df?todo
        for obj in self.columnList:
            if obj.name in self.df.columns:
                # 检查null值处理
                if obj.fill_null:
                    self.df.fillna({obj.name, obj.default_value}, inplace=True)
                else:
                    self.df.dropna(subset=[obj.name], inplace=True)
                # 类型校对
                if obj.type == "Float":  # 如果是浮点数，则转换
                    self.df[obj.name] = self.df[obj.name].apply(pd.to_numeric, errors='coerce') #转换失败的填0.fillna(0.0)
                continue  # 掠过进入下一个

            if obj.dfColumn is None:  # 没有匹配，则直接用default
                self.df[obj.name] = obj.default_value
            else:
                # 做转换，把
                self.df[obj.name] = self.df[obj.dfColumn]
                # 把原来的列移除，否则调用geopytool的时候会报错，因为冲名列出现了两次
                self.df.drop(obj.dfColumn,axis=1,inplace = True) # 删除该列
                print('column :',obj.dfColumn," has mapping to",obj.name,",dropped it.")
                # 检查null值处理
                if obj.fill_null:
                    self.df.fillna({obj.name, obj.default_value}, inplace=True)
                else:
                    self.df.dropna(subset=[obj.name], inplace=True)
                # 类型校对
                if obj.type == "Float":  # 如果是浮点数，则转换
                    self.df[obj.name] = self.df[obj.name].astype("float")
        return True

    # 把数据设置好，然后用于成图  todo
    def doPlotting(self):
        if not self.getAllColumnObjs():
            return
        if self.makedf():
            # 替换完了，判断是否dlg状态，如果是，则把dlg给关掉，然后返回df给外面，设置一个标记
            if hasattr(self,"dlg"):
                if self.dlg.isVisible():
                    self.dlg.df = self.df
                    self.dlg.accept()

        pass

    # 忽略大小写匹配
    def getDfColumn(self, name):
        if self.dfColumns is None:
            return None
        for column in self.dfColumns:
            if column.lower() == name.lower():  # 全转为小写进行比较，忽略大小写
                return column
        return None

    # 根据相似度计算最接近的字段
    def getDfColumnByRatio(self, leaf):
        if self.dfColumns is None:
            return None
        from fuzzywuzzy import fuzz
        ratio = 0
        tempColumn = None
        for column in self.dfColumns:
            newRatio = fuzz.token_set_ratio(column.lower().replace("_", ' '),
                                            leaf.name.lower().replace("_", ' '))  # 把连接字符给忽略掉
            if newRatio > ratio:
                ratio = newRatio
                tempColumn = column
        if ratio >= 80:  # 控制阀值，
            leaf.dfColumn = tempColumn
            leaf.ratio = ratio
            return tempColumn
        else:
            return None

    def getAllColumnObjs(self):
        self.columnObjList = []
        num = self.ui.targetLayout.count()
        try:
            for i in range(num):
                c = self.ui.targetLayout.itemAt(i).widget()
                self.columnObjList.append(c.getColumnObj())

        except Exception as ex:
            print(ex)

            QMessageBox.information(self, 'Tips', 'Please check the value first.',
                                    QMessageBox.Yes, QMessageBox.Yes)
            return False
        for c in self.columnObjList:
            print(c.__dict__)
        return True

    # 把自己加入到一个对话框中进行显示
    def showDlg(self):
        dlg = QDialog(self.parent(), flags=Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        dlg.setWindowTitle("Plotting data prepare")
        dlg.resize(1024, 768)
        hl = QtWidgets.QVBoxLayout()
        hl.addWidget(self)
        dlg.setLayout(hl)
        self.dlg = dlg  # 标记一下dlg
        dlg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    df = pd.read_excel("d:/岩石数据库-黄河数据.xlsx", sheet_name="样品基本信息", header=2)

    datalist = [{"Name": "Label", "Desc": "点的标签值", "Type": "String", "UseDefault": True, "DefaultValue": "O"},
                {"Name": "Color", "Desc": "颜色值，red，green等", "Type": "String", "UseDefault": True,
                 "DefaultValue": "red"},
                {"Name": "Marker", "Desc": "分类标签，例如O，*", "Type": "String", "UseDefault": False, "DefaultValue": "O"},
                {"Name": "Size", "Desc": "图标大小，默认10", "Type": "String", "UseDefault": False, "DefaultValue": "O"},
                {"Name": "Width", "Desc": "宽度，默认1", "Type": "String", "UseDefault": False, "DefaultValue": "O"},
                {"Name": "Style", "Desc": "渲染风格，默认-", "Type": "String", "UseDefault": False, "DefaultValue": "O"},
                {"Name": "Alpha", "Desc": "透明度，默认0.6，取值范围0~1", "Type": "Float", "UseDefault": False,
                 "DefaultValue": "O"},
                {"Name": "SiO2", "Desc": "二氧化硅含量", "Type": "Float", "UseDefault": False, "DefaultValue": "O"},
                {"Name": "K2O", "Desc": "氧化钾含量", "Type": "Float", "UseDefault": False, "DefaultValue": "O"},
                {"Name": "Na2O", "Desc": "氧化钠含量", "Type": "Float", "UseDefault": False, "DefaultValue": "O"}]

    dfe = DfColumnMappingWidget(df, datalist)
    dfe.show()

    sys.exit(app.exec_())
