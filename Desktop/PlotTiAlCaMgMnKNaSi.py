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
from geopytool.FluidInclusion import FluidInclusion
from geopytool.Saccani import Saccani
from geopytool.TiAlCaMgMnKNaSi import TiAlCaMgMnKNaSi
from geopytool.Trace import Trace
from pandasgui.store import PandasGuiDataFrameStore
from pandasgui.widgets.dataframe_explorer import DataFrameExplorer
from ui.ui_plot_tas import Ui_TASPlot


class PlotTiAlCaMgMnKNaSi(QWidget):
    ui = Ui_TASPlot()

    def __init__(self,parent=None):
        super(PlotTiAlCaMgMnKNaSi, self).__init__(parent)
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
        ''' ['TiO2', 'Al2O3', 'CaO','MgO','MnO','K2O','Na2O','SiO2']  '''
        datalist = [{"Name": "Label", "Desc": "点的标签值", "Type": "String","UseDefault":False,"DefaultValue":"a"},
                    {"Name": "Color", "Desc": "颜色值，red，green等", "Type": "String","UseDefault":True,"DefaultValue":"red"},
                    {"Name": "Marker", "Desc": "分类标签，例如O，*", "Type": "String","UseDefault":True,"DefaultValue":"*"},
                    {"Name": "Size", "Desc": "图标大小，默认10", "Type": "Float","UseDefault":True,"DefaultValue":"10"},
                    {"Name": "Width", "Desc": "宽度，默认1", "Type": "Float","UseDefault":True,"DefaultValue":"1"},
                    {"Name": "Style", "Desc": "渲染风格，默认-", "Type": "String","UseDefault":True,"DefaultValue":"-"},
                    {"Name": "Alpha", "Desc": "透明度，默认0.6，取值范围0~1", "Type": "Float","UseDefault":True,"DefaultValue":"0.6"},
                    {"Name": "TiO2", "Desc": "TiO2", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Al2O3", "Desc": "Al2O3", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "CaO", "Desc": "CaO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "MgO", "Desc": "MgO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "MnO", "Desc": "MnO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "K2O", "Desc": "K2O", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Na2O", "Desc": "Na2O", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "SiO2", "Desc": "SiO2", "Type": "Float", "UseDefault": False, "DefaultValue": "0"}]
        w=DfColumnMappingWidget(self.df,datalist,parent=self)
        w.showDlg()
        if hasattr(w,"df"):
            df = w.df.reset_index(drop=True)
            taspop = TiAlCaMgMnKNaSi(df=df,parent=myservice.main_window)

            taspop.Key_Func()
            taspop.setWindowTitle("TiO2-Al2O3-CaO-MgO-MnO-K2O-Na2O-SiO2 major element patterns in basalts")
            taspop.showMaximized()

            # dlg = QDialog(self.parent(), flags=Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
            # dlg.setWindowTitle("TAS Plot")
            # dlg.resize(1024, 768)
            # hl = QtWidgets.QVBoxLayout()
            # hl.addWidget(taspop)
            # dlg.setLayout(hl)
            # dlg.exec()
            #taspop.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = PlotTiAlCaMgMnKNaSi()
    appWin.show()

    sys.exit(app.exec_())