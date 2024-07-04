'''
    数据查重页面

    author:dingyi
    2022-06-19
'''
import os
import traceback

from PyQt5.QtWidgets import QWidget, QCheckBox, QFileDialog, QMessageBox

import myservice
from pandasgui.widgets.dataframe_viewer import DataFrameViewer
from ui.ui_duplicate_checking import Ui_DuplicateChecking
import pandas as pd


class DuplicateCheckWidget(QWidget):
    ui = Ui_DuplicateChecking()

    def __init__(self, parent=None):
        super(DuplicateCheckWidget, self).__init__(parent)
        self.sourceDf = None
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 去除dockwidget的titlebar
        self.ui.dockWidget.setTitleBarWidget(QWidget())
        # 绑定信号和槽
        self.ui.btnDuplicateCheck.clicked.connect(self.doDuplicateCheck)
        self.ui.btnDuplicateOnly.clicked.connect(self.doDuplicateView)
        # 链接处理函数
        self.ui.btnReload.clicked.connect(self.doReload)
        self.ui.btnChooseFile.clicked.connect(self.doChooseFile)
        self.ui.btnSaveToExcel.clicked.connect(self.doSaveToExcel)
        self.ui.btnNoDuplicateView.clicked.connect(self.doNoDuplicate)

    def doChooseFile(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "Choose Paper or Report", os.getcwd(),
                                                         "Excel Files(*.xls || *.xlsx)")
        if fileName is not None:
            if os.path.isfile(fileName):
                self.setFilePath(fileName)

    def doReload(self):
        try:
            df = pd.read_excel(self.excelFile, self.ui.comboSheet.currentText(), header=self.ui.spinHeaderIndex.value())
            self.setDf(df)

        except Exception as ex:
            myservice.logger.critical(traceback.format_exc())
        pass

    def setFilePath(self, filePath):
        self.filePath = filePath
        self.fillSheetList(filePath)  # 填充sheet 列表
        # 清除掉已有的内容
        # 默认执行一次reload
        self.doReload()

    def fillSheetList(self, filePath):
        # 首先清空
        self.ui.comboSheet.clear()
        # 根据filePath显示sheet列表
        if filePath is not None:
            # 检查是否是有效的路径
            self.excelFile = pd.ExcelFile(filePath)
            for s in self.excelFile.sheet_names:
                self.ui.comboSheet.addItem(s)

    def setDf(self, df):
        if df is None:
            return

        # 清除之前的列
        for i in reversed(range(self.ui.gridLayout.count())):
            widgetToRemove = self.ui.gridLayout.itemAt(i).widget()
            widgetToRemove.setParent(None)
            widgetToRemove.deleteLater()

        # 添加过滤的列
        i = 0
        columnCount = 10
        for column in df.columns:
            chk = QCheckBox()
            chk.setText(column)
            self.ui.gridLayout.addWidget(chk, i / columnCount, i % columnCount,1,1)
            i = i+1

        # 添加df显示
        viewer = DataFrameViewer(df)
        self.sourceDf = df  # 把原始df保留起来
        # 清除之前的过滤结果
        if hasattr(self, "filterDf"):
            delattr(self,"filterDf")
        self.ui.dockWidget.setWidget(viewer)

    # 查重，选择的字段越多越精确
    def doDuplicateCheck(self):
        if self.sourceDf is None:
            return
        subset = []
        # 循环获取需要的列名
        num = self.ui.gridLayout.count()
        for i in range(num):
            c = self.ui.gridLayout.itemAt(i).widget()
            if c.isChecked():
                # 需要过滤的列明增加
                subset.append(c.text())

        print(subset)
        if len(subset) ==0:
            viewer = DataFrameViewer(self.sourceDf)
            self.ui.dockWidget.setWidget(viewer)
            self.filterDf =self.sourceDf
            return  # 没有过滤则不处理
        newdf = self.sourceDf.drop_duplicates(subset=subset,ignore_index=True)
        viewer = DataFrameViewer(newdf)
        self.filterDf = newdf  # 保留过滤结果
        self.ui.dockWidget.setWidget(viewer)


    # 显示没有重复的，即把出现重复的从中去掉
    def doNoDuplicate(self):
        if self.sourceDf is None:
            return
        subset = []
        # 循环获取需要的列名
        num = self.ui.gridLayout.count()
        for i in range(num):
            c = self.ui.gridLayout.itemAt(i).widget()
            if c.isChecked():
                # 需要过滤的列明增加
                subset.append(c.text())

        print(subset)
        if len(subset) == 0:
            df2 = pd.concat(
                [self.sourceDf.drop_duplicates(), self.sourceDf.drop_duplicates(keep=False)]).drop_duplicates(
                keep=False, ignore_index=True)
            self.filterDf = df2
            viewer = DataFrameViewer(df2)
            self.ui.dockWidget.setWidget(viewer)
            return  # 没有过滤则不处理
        newdf = self.sourceDf.drop_duplicates(subset=subset, ignore_index=True,keep=False)  # 去掉重复的
        viewer = DataFrameViewer(newdf)
        self.filterDf = newdf  # 保留过滤结果
        self.ui.dockWidget.setWidget(viewer)

    # 只看重复的，不重复的不要了。
    def doDuplicateView(self):
        if self.sourceDf is None:
            return
        subset = []
        # 循环获取需要的列名
        num = self.ui.gridLayout.count()
        for i in range(num):
            c = self.ui.gridLayout.itemAt(i).widget()
            if c.isChecked():
                # 需要过滤的列明增加
                subset.append(c.text())

        print(subset)
        if len(subset) ==0:
            df2 = pd.concat([self.sourceDf.drop_duplicates(),self.sourceDf.drop_duplicates(keep=False)]).drop_duplicates(keep=False,ignore_index=True)
            self.filterDf = df2
            viewer = DataFrameViewer(df2)
            self.ui.dockWidget.setWidget(viewer)
            return  # 没有过滤则不处理
        newdf = pd.concat([self.sourceDf,self.sourceDf.drop_duplicates(subset=subset,ignore_index=True,keep=False)]).drop_duplicates(keep=False,ignore_index=True)
        viewer = DataFrameViewer(newdf)
        self.filterDf = newdf  # 保留过滤结果
        self.ui.dockWidget.setWidget(viewer)

    # 保存到excel文件
    def doSaveToExcel(self):
        # 保存filterDf
        fileNames, fileType = QFileDialog.getSaveFileName(self, "Save to File", os.getcwd(),
                                                          "Excel Files(*.xlsx)")
        if fileNames is None or fileNames == "":
            return
        if hasattr(self,"filterDf"):
            self.filterDf.to_excel(fileNames,index=None) #encoding="utf-8",
        else:
            self.sourceDf.to_excel(fileNames,  index=None)#encoding="utf-8",
        QMessageBox.information(self,"Tips","Save succeed!")

