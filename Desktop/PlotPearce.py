'''
    TAS 图解
    左侧是数据，右侧是图，采用dockwidget方式，可以浮动放大

'''
import os
import sys
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QApplication, QDialog
import  pandas as pd

import myservice
from DfColumnMappingWidget import DfColumnMappingWidget
from MyEntityMappingWidget import MyEntityMappingWidget
from geopytool.Pearce import Pearce
from geopytool.TAS import TAS
from pandasgui.store import PandasGuiDataFrameStore
from pandasgui.widgets.dataframe_explorer import DataFrameExplorer
from ui.ui_plot_tas import Ui_TASPlot


class PlotPearce(QWidget):
    ui = Ui_TASPlot()

    def __init__(self,parent=None):
        super(PlotPearce, self).__init__(parent)
        self.setupUi()
        self.df = None



    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 连接信号与函数
        # 链接处理函数
        self.ui.btnReload.clicked.connect(self.doReload)
        self.ui.btnChooseFile.clicked.connect(self.doChooseFile)
        self.ui.btnPlot.clicked.connect(self.doPlot)

    def doChooseFile(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "Choose Excel File", os.getcwd(),
                                                         "Excel Files(*.xls || *.xlsx)")
        if fileName != '':  # 只有选中了才需要执行
            self.setFilePath(fileName)

    def doReload(self):
        try:
            df = pd.read_excel(self.excelFile, self.ui.comboSheet.currentText(), header=self.ui.spinHeaderIndex.value())
            self.df = df # 保留对象
            pgdfs = PandasGuiDataFrameStore(df, self.ui.comboSheet.currentText())
            dfe = DataFrameExplorer(pgdfs)
            self.ui.scrollArea.setWidget(dfe)
        except Exception as ex:
            myservice.logger.critical(traceback.format_exc())
        pass



    def setFilePath(self,filePath):
            self.filePath = filePath
            self.fillSheetList(filePath)  # 填充sheet 列表
            # 清除掉已有的内容

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

    def doPlot(self):
        if self.df is None:
            # 提醒先打开文件或者从其他地方获取数据
            QMessageBox.information(self, "Tips", "Please open file FIRST!")
            return
        # 校验是否包含必须有的字段  todo，暂缺
        # 做校验，把每个列的类型做校验，如果不对，则转换类型，转换失败的数据则丢掉
        datalist = [{"Name": "Label", "Desc": "点的标签值", "Type": "String","UseDefault":False,"DefaultValue":"a"},
                    {"Name": "Color", "Desc": "颜色值，red，green等", "Type": "String","UseDefault":True,"DefaultValue":"red"},
                    {"Name": "Marker", "Desc": "分类标签，例如O，*", "Type": "String","UseDefault":True,"DefaultValue":"*"},
                    {"Name": "Size", "Desc": "图标大小，默认10", "Type": "Float","UseDefault":True,"DefaultValue":"10"},
                    {"Name": "Width", "Desc": "宽度，默认1", "Type": "Float","UseDefault":True,"DefaultValue":"1"},
                    {"Name": "Style", "Desc": "渲染风格，默认-", "Type": "String","UseDefault":True,"DefaultValue":"-"},
                    {"Name": "Alpha", "Desc": "透明度，默认0.6，取值范围0~1", "Type": "Float","UseDefault":True,"DefaultValue":"0.6"},
                    {"Name": "Y", "Desc": "Y", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Yb", "Desc": "Yb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Nb", "Desc": "Nb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Rb", "Desc": "Rb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ta", "Desc": "Ta", "Type": "Float", "UseDefault": False, "DefaultValue": "0"}]
        w=DfColumnMappingWidget(self.df,datalist,parent=self)
        w.showDlg()
        if hasattr(w,"df"):
            df = w.df.reset_index(drop=True)
            taspop = Pearce(df=df, parent=myservice.main_window)

            taspop.Pearce()
            taspop.setWindowTitle("Pearce Plot")
            taspop.showMaximized()
            #taspop.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = PlotPearce()
    appWin.show()

    sys.exit(app.exec_())
