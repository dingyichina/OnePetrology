# encoding=UTF-8
'''
    Excel预览及处理入库
    传入的是Excel的文件路径（或者来自于dspace的附件链接）
'''
import os.path
import sys
import traceback
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog

import myservice
from MyEntityMappingWidget import MyEntityMappingWidget
from pandasgui.store import PandasGuiDataFrameStore
from pandasgui.widgets.dataframe_explorer import DataFrameExplorer
from ui.ui_excel import Ui_ExcelProcess

import pandas as pd


class ExcelProcessWidget(QWidget):
    ui = Ui_ExcelProcess()

    def __init__(self, parent=None,filePath=None):
        super(ExcelProcessWidget, self).__init__(parent)
        self.setupUi()
        self.excelFile = None
        self.filePath = filePath
        if filePath is not None:
            self.fillSheetList(filePath)   # 填充sheet 列表

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 链接处理函数
        self.ui.btnReload.clicked.connect(self.doReload)
        self.ui.btnChooseFile.clicked.connect(self.doChooseFile)

    def doChooseFile(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "Choose Excel file", os.getcwd(),
                                                         "Excel Files(*.xls || *.xlsx)")
        if fileName is not None:
            self.setFilePath(fileName)

    def doReload(self):
        try:
            df = pd.read_excel(self.excelFile,self.ui.comboSheet.currentText(),header= self.ui.spinHeaderIndex.value())
            pgdfs = PandasGuiDataFrameStore(df,self.ui.comboSheet.currentText())
            # 移除掉已有的tab
            for i in range(self.ui.tabWidget.count()-1,-1,-1):
                self.ui.tabWidget.removeTab(i)
            dfe=DataFrameExplorer(pgdfs)
            self.ui.tabWidget.addTab(dfe,self.ui.comboSheet.currentText())
            # 添加自定义知识树对应的实体ENTITY及对应的字段
            entityWidget = MyEntityMappingWidget(df)
            entityWidget.filePath = self.filePath
            self.ui.tabWidget.addTab(entityWidget,"Mapping to DB")

        except Exception as ex:
            myservice.logger.critical(traceback.format_exc())
        pass

    def setFilePath(self,filePath):
        self.filePath = filePath
        self.fillSheetList(filePath)  # 填充sheet 列表
        # 清除掉已有的内容
        # 移除掉已有的tab
        for i in range(self.ui.tabWidget.count() - 1, -1, -1):
            self.ui.tabWidget.removeTab(i)
        # 默认执行一次reload
        self.doReload()

    def fillSheetList(self,filePath):
        # 首先清空
        self.ui.comboSheet.clear()
        # 根据filePath显示sheet列表
        if filePath is not None:
            # 检查是否是有效的路径
            self.excelFile = pd.ExcelFile(filePath)
            for s in self.excelFile.sheet_names:
                self.ui.comboSheet.addItem(s)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = ExcelProcessWidget(filePath="http://8.218.13.217:8080/server/api/core/bitstreams/32bf0f87-e798-4b11-bf65-5a3310bd8010/content")
    dfe.show()

    sys.exit(app.exec_())
