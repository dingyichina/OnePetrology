import datetime
import os
import sys

import numpy as np
import pandas as pd
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QAbstractTableModel, QVariant, QModelIndex, Qt, QThread
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QStyledItemDelegate, QComboBox, QMessageBox, QCheckBox

import myservice
from model.KnowledgeNode import ValueType
from ui.ui_my_entity import Ui_MyEntityMapping


# 自定义的tablemodel


class EntityMappingModel(QAbstractTableModel):

    def __init__(self, knList):
        QAbstractTableModel.__init__(self)
        self.knList = knList
        self.headers = ["Name ", "CN Name", "Excel header mapping"]

    def rowCount(self, parent=None):
        return len(self.knList)

    def columnCount(self, parnet=None):
        return 3

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                if index.column() == 0:
                    return self.knList[index.row()].name
                elif index.column() == 1:
                    return self.knList[index.row()].cn_name
                elif index.column() == 2:
                    return self.knList[index.row()].dfColumn
                else:
                    return QVariant()

            elif role == Qt.BackgroundRole:
                if self.knList[index.row()].dfColumn is None:
                    return QColor("#76b87d")
                elif hasattr(self.knList[index.row()], "ratio"):
                    if self.knList[index.row()].ratio > 90:
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
        if index.isValid() and 0 <= index.row() < len(self.knList) and value:
            col = index.column()
            # print(col)
            if 0 < col < len(self.headers):
                self.beginResetModel()
                # if CONVERTS_FUNS[col]:  # 必要的时候执行数据类型的转换
                #     self.datas[index.row()][col] = CONVERTS_FUNS[col](value)
                # else:
                if value == "None":
                    self.knList[index.row()].dfColumn = None
                else:
                    self.knList[index.row()].dfColumn = value
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


# 实体映射类
class MyEntityMappingWidget(QWidget):
    # 默认需要选中的字段
    defaultList = {'longitude', 'latitude', 'sampleno'}  # 为了比较方便，默认全写小写
    def __init__(self, df=None, parent=None):
        super(MyEntityMappingWidget, self).__init__(parent)
        self.ui = Ui_MyEntityMapping()
        self.df = df
        if df is None:
            self.dfColumns = None
        else:
            self.dfColumns = df.columns
        self.setupUi()
        self.parent = parent

        # 初始化下拉列表
        knlist = myservice.arango.fetchAllEntity(owner=myservice.username.upper())
        for k in knlist:
            self.ui.comboMyEntity.addItem(k.name, k)

        # filter fields 相关按钮
        self.ui.btnRestoreDefaultFilter.clicked.connect(self.restoreDefault)
        self.ui.btnSelectAllFilterFields.clicked.connect(self.selectAll)
        self.ui.btnReverseFilterFieldsCheck.clicked.connect(self.reverseSelect)

    # 恢复为默认的选项
    def restoreDefault(self):
        num = self.ui.gridLayout.count()
        for i in range(num):
            c = self.ui.gridLayout.itemAt(i).widget()
            if c.text().lower() in self.defaultList :
                c.setChecked(True)
            else:
                c.setChecked(False)

    # 选中全部
    def selectAll(self):
        num = self.ui.gridLayout.count()
        for i in range(num):
            c = self.ui.gridLayout.itemAt(i).widget()
            c.setChecked(True)
    # 反选
    def reverseSelect(self):
        num = self.ui.gridLayout.count()
        for i in range(num):
            c = self.ui.gridLayout.itemAt(i).widget()
            c.setChecked(not c.isChecked())


    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.btnRefresh.clicked.connect(self.doRefresh)
        self.ui.btnSave2DB.clicked.connect(self.doSave2DB)

    def doRefresh(self):
        k_node = self.ui.comboMyEntity.itemData(self.ui.comboMyEntity.currentIndex())
        leaf_list = []
        myservice.arango.getLeafList4Entity(k_node, leaf_list)
        # 直接匹配相等来一遍（忽略了大小写，但没有忽略空格和连接符等）
        for leaf in leaf_list:
            # 循环遍历是否已经与dfColumns里面的值是否对应上
            leaf.dfColumn = self.getDfColumn(leaf.name)
            # print(leaf.dfColumn)
        # 通过计算相似度进行匹配其他的None值，选出一个相似度最高的（阈值设置为90%，只有高于这个才会被选中，其他仍旧设置为None）

        for leaf in leaf_list:
            if leaf.dfColumn is None:
                # 尝试用模糊匹配的方式进行匹配  fuzz
                leaf.dfColumn = self.getDfColumnByRatio(leaf)

        self.leaf_list = leaf_list
        # 构建model
        model = EntityMappingModel(leaf_list)
        self.ui.tableView.setModel(model)
        # 设置编辑代理
        delegate = MyComboDelegate(dfColumns=self.dfColumns, parent=self)
        self.ui.tableView.setItemDelegateForColumn(2, delegate)

        # 刷新过滤字段
        self.refreshFilterFields()

        pass

    # 刷新过滤的字段，用来查重
    def refreshFilterFields(self):
        if self.df is None:
            return
        # 清除之前的列
        for i in reversed(range(self.ui.gridLayout.count())):
            widgetToRemove = self.ui.gridLayout.itemAt(i).widget()
            widgetToRemove.setParent(None)
            widgetToRemove.deleteLater()

        # 添加过滤的列
        i = 0
        columnCount = 3
        for leaf in self.leaf_list:
            chk = QCheckBox()
            chk.setText(leaf.name)
            self.ui.gridLayout.addWidget(chk, i / columnCount, i % columnCount, 1, 1)
            if leaf.name.lower() in self.defaultList:
                chk.setChecked(True)
            i = i + 1

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

    # 保存到数据库中
    def doSave2DB(self):
        # 首先检查已经对应的字段
        if not hasattr(self, "leaf_list"):
            QMessageBox.information(self, 'Tips', 'Please press Refresh button and match the field first.',
                                    QMessageBox.Yes, QMessageBox.Yes)
            return
        # 检查匹配到的列是否有重复字段，如果有，则提醒
        matched_leaf_list = []
        matched_columns = []
        matched_leaf_columns = []  #
        for leaf in self.leaf_list:
            if leaf.dfColumn is not None:
                matched_leaf_list.append(leaf)
                matched_columns.append(leaf.dfColumn)
                matched_leaf_columns.append(leaf.name)
        # 如果有的字段出现了多次，则提醒
        repeat_columns = {}
        for c in matched_columns:
            if matched_columns.count(c) > 1:
                repeat_columns[c] = matched_columns.count(c)
        if len(repeat_columns) > 0:
            if QMessageBox.question(self, 'Question', 'Some columns has used more than one time. \r\n' + str(
                    repeat_columns) + "\r\n   Do you want to continue ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.No:
                return
        # 检查是否有没有映射的字段，如果有，则提醒
        missed_column_list = [item for item in self.dfColumns.values.tolist() if item not in set(matched_columns)]
        if len(missed_column_list) > 0:
            if QMessageBox.question(self, 'Question', 'Some column has missed match field. \r\n' + ' ,'.join(
                    missed_column_list) + "\r\n If continue, some data will missed to DB.\r\n\r\n  Do you want to continue ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.No:
                return
        filterFields = []
        # 获取用来查重的字段
        num = self.ui.gridLayout.count()
        for i in range(num):
            c = self.ui.gridLayout.itemAt(i).widget()
            if c.isChecked():
                # 需要过滤的列明增加
                filterFields.append(c.text())

        print(filterFields)
        if len(filterFields) == 0:
            if QMessageBox.question(self, 'Question', "you didn't  choose filter field.\r\n   This will lead to data "
                                                      "duplication. It is recommended that you choose before "
                                                      "continuing.  \r\n "
                                                      + "\r\n Do you insist on continuing ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.No:
                return
        # 检查是否所有的filter Field 都已经呗映射了，如果没有则提示
        # 转换小写

        for field in filterFields:
            if field not in matched_leaf_columns:
                QMessageBox.information(self, 'Tips', 'Filter Field: ' + field + '  is not matched. please match it '
                                                                                 'first.',
                                        QMessageBox.Yes, QMessageBox.Yes)
                return
        # 把config条件转化为选项值
        import_config = 0
        if self.ui.radioMerge.isChecked():
            import_config = 1
        elif self.ui.radioOverride.isChecked():
            import_config = 2
        elif self.ui.radioPick.isChecked():
            import_config = 3

        # 此时可以去读取dataframe的数据去入库了，根据所匹配到的字段。
        # 检查是否存在对应的collection，如果没有则创建
        col_name = self.ui.comboMyEntity.currentText()

        # 用线程提交数据
        if self.ui.radioPrivate.isChecked():
            scope = "private"
        else:
            scope = "public"
        self.thread = WorkerThread(col_name, matched_leaf_list, self.df, self.filePath, scope, filterFields,
                                   import_config)
        self.thread.statusSignal.connect(myservice.main_window.workerStatus)
        self.thread.finishSignal.connect(myservice.loading_mask.hide)
        self.thread.finishSignal.connect(self.dofinished)
        myservice.loading_mask.show()
        self.thread.start()
        pass

    def dofinished(self, msg, fileName):
        QMessageBox.information(self, 'Result', msg, QMessageBox.Yes, QMessageBox.Yes)
        # 直接打开file ，暂缺  todo
        os.system(os.path.abspath(fileName)) # 用操作系统软件打开文件

# 列中剔除非法字符s和 - — > <
def correctValue(x):
    if (isinstance(x, str)):
        if x == '-':
            return np.nan
        elif x == 's':
            return np.nan
        elif x == '—':
            return np.nan
        elif '<' in x:
            return x.replace('<', '')
        elif '>' in x:
            return x.replace('>', '')

    return x


class WorkerThread(QThread):
    statusSignal = QtCore.pyqtSignal(str)  # 注册过程状态信号
    finishSignal = QtCore.pyqtSignal(str, str)  # 完成信号，第一个是消息字符串，第二个是文件路径

    def __init__(self, col_name, matched_leaf_list, df, filePath, scope, filter_fields, import_config, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.matched_leaf_list = matched_leaf_list
        self.dfColumns = []
        for leaf in self.matched_leaf_list:
            self.dfColumns.append(leaf.dfColumn)
        self.col_name = col_name
        self.df = df
        self.filePath = filePath
        self.scope = scope
        self.filter_fields = filter_fields
        self.import_config = import_config
        pass

    # 处理提交到db的操作
    def run(self):
        skipnum = 0
        addnum = 0

        print("实体名称：", self.col_name)
        col = myservice.arango.getCollection(self.col_name)

        has_skipped = []  # 因为重复被忽略掉的
        has_import = []  # 成功导入的
        has_merged = []  # 成功更新的，输出的是更新之后的结果
        has_delete = []  # 被删除的，当delete and use mine时会出现这个
        dupliacate = []  # 多条重复被挑出来的
        confilict = []  # 被更新的，原来的+自己的+合并之后的
        has_overwrite = []  # 已经覆盖的

        # 通过iloc遍历df的每一行
        for i in range(0, len(self.df)):
            doc = {}
            for leaf in self.matched_leaf_list:
                value = self.df.iloc[i][leaf.dfColumn]
                # 剔除非法字符
                value = correctValue(value)
                # 为空则略过
                if pd.isna(value):
                    continue
                # 校对取值的类型  ，目前没有考虑枚举类型的转换，以及关联类型的取值，待下一步 完善  todo
                try:
                    if leaf.value_type == ValueType.FLOAT.value:
                        value = float(value)

                    elif leaf.value_type == ValueType.STRING.value:
                        value = str(value)
                    else:  # 默认当作字符串
                        value = str(value)
                    doc[leaf.name] = value  # 此时需要根据leaf的type进行类型转换与校验
                except Exception as ex:
                    myservice.logger.error("非法值存在{}行 {}".format(i, leaf.dfColumn))
                    continue  # 非法值当作空值处理

            # 如果没选过滤字段或者选择了全部过滤字段，则默认检查全记录，否则按照config选项进行检查
            if len(self.filter_fields) == 0 or len(self.filter_fields) == len(self.matched_leaf_list):
                myservice.logger.info(" use all fileds to filter.")
                if myservice.arango.isExists(col, doc):
                    # 出发信号
                    self.statusSignal.emit(" data has exists，skipped : " + str(doc))
                    myservice.logger.info(" data has exists，skipped : " + str(doc))
                    skipnum = skipnum + 1
                    has_skipped.append(doc)  # 添加到skipped
                    continue  # 继续下一个
                else:
                    # 全字段不存在，应该添加
                    # 此处需要附加有关信息，例如所有者owner，创建时间等 todo
                    doc["owner"] = myservice.username.upper()
                    doc["scope"] = self.scope  # 默认是私有的
                    doc["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    doc["import from"] = self.filePath  # 描述数据的来源  todo
                    # 写入数据库
                    myservice.logger.info("add data: " + str(doc))
                    myservice.arango.insert(col, doc)
                    # 出发信号
                    self.statusSignal.emit("insert data :" + str(doc))
                    has_import.append(doc)  # 添加到已导入
                    addnum = addnum + 1
            else:  # 此时选择了filter fields 且不是全选
                #  根据所选择的filter fields进行查重
                example = {}
                for field in self.filter_fields:  #  这里的doc，需要用mapping的字段，这里直接用field是不行的，需要修改*****todo****
                    try:
                        example[field] = doc[field]
                    except Exception as ex:
                        print(ex)
                        self.statusSignal.emit("出异常了 :" + str(ex))
                #此时需要添加上owner，用于过滤只属于自己的数据
                example["owner"] = myservice.username.upper()
                rtnRows = col.fetchByExample(example, batchSize=500)
                if len(rtnRows) == 0:  # 没有找到重复的，则添加整行
                    # 此处需要附加有关信息，例如所有者owner，创建时间等 todo
                    doc["owner"] = myservice.username.upper()
                    doc["scope"] = self.scope  # 默认是私有的
                    doc["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    doc["import from"] = self.filePath  # 描述数据的来源  todo
                    # 写入数据库
                    myservice.logger.info("add data: " + str(doc))
                    myservice.arango.insert(col, doc)
                    # 出发信号
                    self.statusSignal.emit("insert data :" + str(doc))
                    has_import.append(doc)  # 添加到已导入
                    addnum = addnum + 1
                    continue  # 继续添加下一行
                elif len(rtnRows) == 1:  # 找到了一行，此时需要用doc中有值的去更新db中没有值的字段。如果有冲突，则输出
                    old_doc = rtnRows[0].getStore()
                    if self.import_config == 1:  # merge，把冲突的行给输出到excel中
                        # 循环遍历doc中的key，然后去检查更新rtnRows[0]中的对应字段
                        hasconflict = False
                        merged = False

                        for k in doc.keys():
                            if k in rtnRows[0].getStore().keys():
                                if doc[k] != rtnRows[0].getStore()[k]:
                                    # rtnRows[0][k] = doc[k]  # 字段赋值  # 此时不做修改，选项2才可以修改
                                    hasconflict = True
                            else:
                                rtnRows[0][k] = doc[k]  # 新增一个字段值
                                merged = True
                                hasconflict = True
                        if hasconflict:
                            # 执行更新指令，并记录日志
                            rtnRows[0].save()  # 直接执行save命令
                            myservice.logger.info("update data: " + str(rtnRows[0].getStore()))
                            # 出发信号
                            self.statusSignal.emit("update data :" + str(rtnRows[0].getStore()))
                            # 先放原来的，再放自己的，然后再放merge之后的
                            if merged:
                                has_merged.append(old_doc)
                                has_merged.append(doc)
                                has_merged.append(rtnRows[0].getStore())
                            else:
                                confilict.append(old_doc)
                                confilict.append(doc)
                                confilict.append(rtnRows[0].getStore())

                        else:
                            #  重复，不需要更新，记录一下
                            has_skipped.append(doc)
                            self.statusSignal.emit(" data has exists，skipped : " + str(doc))
                            myservice.logger.info(" data has exists，skipped : " + str(doc))

                    elif self.import_config == 2:  # 此时是需要delete  and use mine ，先删除找到的，然后用自己的去插入
                        #  删除，并插入新的
                        # has_delete.append(rtnRows[0].getStore())  # 添加到已删除
                        # 此时需要检查数据库中是否存在doc中不存在的字段，反向补充回来到doc中
                        hasconflict = False
                        merged = False
                        for k in doc.keys():
                            if k in rtnRows[0].getStore().keys():
                                if doc[k] != rtnRows[0].getStore()[k]:
                                     rtnRows[0][k] = doc[k]  # 字段赋值
                                     hasconflict = False
                            else:
                                rtnRows[0][k] = doc[k]  # 新增一个字段值
                                merged = True
                                hasconflict = True
                        if hasconflict:
                            # 执行更新指令，并记录日志
                            rtnRows[0].save()  # 直接执行save命令
                            myservice.logger.info("update data: " + str(rtnRows[0].getStore()))
                            # 出发信号
                            self.statusSignal.emit("update data :" + str(rtnRows[0].getStore()))
                            # 先放原来的，再放自己的，然后再放merge之后的
                            if merged:
                                has_merged.append(old_doc)
                                has_merged.append(doc)
                                has_merged.append(rtnRows[0].getStore())
                            else:
                                confilict.append(old_doc)
                                confilict.append(doc)
                                confilict.append(rtnRows[0].getStore())

                        else:
                            #  重复，不需要更新，记录一下
                            has_skipped.append(doc)
                            self.statusSignal.emit(" data has exists，skipped : " + str(doc))
                            myservice.logger.info(" data has exists，skipped : " + str(doc))
                        # rtnRows[0].delete()
                        # myservice.logger.info("delete data: " + str(rtnRows[0].getStore()))
                        # self.statusSignal.emit("delete data :" + str(rtnRows[0].getStore()))
                        # # 此处需要附加有关信息，例如所有者owner，创建时间等 todo
                        # doc["owner"] = myservice.username.upper()
                        # doc["scope"] = self.scope  # 默认是私有的
                        # doc["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        # doc["import from"] = self.filePath  # 描述数据的来源  todo
                        # # 写入数据库
                        # myservice.logger.info("add data: " + str(doc))
                        # myservice.arango.insert(col, doc)
                        # # 出发信号
                        # self.statusSignal.emit("insert data :" + str(doc))
                        # has_overwrite.append(doc)  # 添加到已覆盖
                        # addnum = addnum + 1

                        continue  # 继续添加下一行
                    elif self.import_config == 3:  # 此时是skip and pick out to file，需要把所有重复的给输出，并不做插入
                        dupliacate.append(rtnRows[0].getStore())  # 只是把找到的结果和数据一同添加到重复里面，输出让用户选择
                        dupliacate.append(doc)
                        # 出发信号
                        self.statusSignal.emit("find duplicate data :" + str(doc))
                        myservice.logger.info("find duplicate data : " + str(doc))
                elif len(rtnRows) > 1:  # 找到了多行，此时只执行输出，不做字段层面更新
                    if self.import_config == 1:  # merge，把冲突的行给输出到excel中
                        for row in rtnRows:  # 只是添加到重复中
                            dupliacate.append(row.getStore())
                        dupliacate.append(doc)  # 自身数据也添加到重复中
                        # 出发信号
                        self.statusSignal.emit("find duplicate data :" + str(doc))
                        myservice.logger.info("find duplicate data : " + str(doc))
                        pass
                    elif self.import_config == 2:  # 此时是需要delete  and use mine ，先删除找到的，然后用自己的去插入
                        for row in rtnRows:  # 循环删除旧的
                            has_delete.append(row.getStore())  # 添加到已删除
                            row.delete()
                            myservice.logger.info("delete data: " + str(row))
                            self.statusSignal.emit("delete data :" + str(row))
                        # 此处需要附加有关信息，例如所有者owner，创建时间等 todo
                        doc["owner"] = myservice.username.upper()
                        doc["scope"] = self.scope  # 默认是私有的
                        doc["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        doc["import from"] = self.filePath  # 描述数据的来源  todo
                        # 写入数据库
                        myservice.logger.info("add data: " + str(doc))
                        myservice.arango.insert(col, doc)
                        # 出发信号
                        self.statusSignal.emit("insert data :" + str(doc))
                        has_import.append(doc)  # 添加到已导入
                        addnum = addnum + 1
                        pass
                    elif self.import_config == 3:  # 此时是skip and pick out to file，需要把所有重复的给输出，并不做插入
                        for row in rtnRows:
                            dupliacate.append(row.getStore())
                        dupliacate.append(doc)
                        # 出发信号
                        self.statusSignal.emit("find duplicate data :" + str(doc))
                        myservice.logger.info("find duplicate data : " + str(doc))
                        pass

        # 处理完毕后输出excel
        # 拼装文件名
        output_dir = "import"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # 目录不存在则创建

        filename = output_dir + "/import" + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + ".xlsx"
        writer = pd.ExcelWriter(filename, mode='w', engine='openpyxl')
        try:
            if len(has_skipped) > 0:
                df = pd.DataFrame(has_skipped)
                df.to_excel(writer, "has skipped")
        except Exception as ex:
            myservice.logger.error("输出skipped列表出错")
            pass
        try:
            if len(has_import) > 0:
                df = pd.DataFrame(has_import)
                df.to_excel(writer, "has imported")
        except Exception as ex:
            myservice.logger.error("输出import列表出错")
            pass
        try:
            if len(has_merged) > 0:
                df = pd.DataFrame(has_merged)
                df.to_excel(writer, "has merged")
        except Exception as ex:
            myservice.logger.error("输出 update 列表出错")
            pass
        try:
            if len(has_delete) > 0:
                df = pd.DataFrame(has_delete)
                df.to_excel(writer, "has deleted")
        except Exception as ex:
            myservice.logger.error("输出delete列表出错")
            pass
        try:
            if len(dupliacate) > 0:
                df = pd.DataFrame(dupliacate)
                df.to_excel(writer, "nulti-dupliacate")
        except Exception as ex:
            myservice.logger.error("输出dupliacated列表出错")
            pass
        try:
            if len(confilict) > 0:
                df = pd.DataFrame(confilict)
                df.to_excel(writer, "Confilicts")
        except Exception as ex:
            myservice.logger.error("输出Confilict列表出错")
            pass
        try:
            if len(has_overwrite) > 0:
                df = pd.DataFrame(has_overwrite)
                df.to_excel(writer, "has overwrite")
        except Exception as ex:
            myservice.logger.error("输出has_overwrite列表出错")
            pass
        writer.save()
        writer.close()
        # 执行完毕发射完成信号
        self.finishSignal.emit("finished----- please check the result in file : {}   ".format(filename), filename)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = MyEntityMappingWidget()
    dfe.show()

    sys.exit(app.exec_())
