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
from geopytool.Trace import Trace
from pandasgui.store import PandasGuiDataFrameStore
from pandasgui.widgets.dataframe_explorer import DataFrameExplorer
from ui.ui_plot_tas import Ui_TASPlot


class PlotTrace(QWidget):
    ui = Ui_TASPlot()

    def __init__(self,parent=None):
        super(PlotTrace, self).__init__(parent)
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
        ''' ['Cs', 'Tl', 'Rb', 'Ba', 'W', 'Th', '', 'Nb', 'Ta', 'K', 'La', 'Ce', 'Pb', 'Pr', 'Mo',
         'Sr', 'P', 'Nd', 'F', 'Sm', 'Zr', 'Hf', 'E', 'Sn', 'Sb', 'Ti', 'Gd', 'Tb', 'Dy',
         'Li',
         'Y', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']  '''
        datalist = [{"Name": "Label", "Desc": "点的标签值", "Type": "String","UseDefault":False,"DefaultValue":"a"},
                    {"Name": "Color", "Desc": "颜色值，red，green等", "Type": "String","UseDefault":True,"DefaultValue":"red"},
                    {"Name": "Marker", "Desc": "分类标签，例如O，*", "Type": "String","UseDefault":True,"DefaultValue":"*"},
                    {"Name": "Size", "Desc": "图标大小，默认10", "Type": "Float","UseDefault":True,"DefaultValue":"10"},
                    {"Name": "Width", "Desc": "宽度，默认1", "Type": "Float","UseDefault":True,"DefaultValue":"1"},
                    {"Name": "Style", "Desc": "渲染风格，默认-", "Type": "String","UseDefault":True,"DefaultValue":"-"},
                    {"Name": "Alpha", "Desc": "透明度，默认0.6，取值范围0~1", "Type": "Float","UseDefault":True,"DefaultValue":"0.6"},
                    {"Name": "Cs", "Desc": "Cs", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "Tl", "Desc": "Tl", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "Rb", "Desc": "Rb", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "Ba", "Desc": "Ba", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "W", "Desc": "W", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Th", "Desc": "Th", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Nb", "Desc": "Nb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ta", "Desc": "Ta", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "K", "Desc": "K", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "La", "Desc": "La", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ce", "Desc": "Ce", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Pb", "Desc": "Pb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Pr", "Desc": "Pr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "Mo", "Desc": "Mo", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Sr", "Desc": "Sr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "P", "Desc": "P", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Nd", "Desc": "Nd", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "F", "Desc": "F", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Sm", "Desc": "Sm", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Zr", "Desc": "Zr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Hf", "Desc": "Hf", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "E", "Desc": "E", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "Sn", "Desc": "Sn", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "Sb", "Desc": "Sb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    #{"Name": "Ti", "Desc": "Ti", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Gd", "Desc": "Gd", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Tb", "Desc": "Tb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Dy", "Desc": "Dy", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Li", "Desc": "Li", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Y", "Desc": "Y", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ho", "Desc": "Ho", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Er", "Desc": "Er", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Tm", "Desc": "Tm", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Yb", "Desc": "Yb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Lu", "Desc": "Lu", "Type": "Float", "UseDefault": False, "DefaultValue": "0"}]
        w=DfColumnMappingWidget(self.df,datalist,parent=self)
        w.showDlg()
        if hasattr(w,"df"):
            df = w.df.reset_index(drop=True)
            #try:
            taspop = Trace(df=df,parent=myservice.main_window)

            taspop.Trace()
            taspop.setWindowTitle("Trace Plot")
            taspop.showMaximized()
            #except Exception as ex:
            #    QMessageBox.critical(self,"Error",ex.__str__())

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
    appWin = PlotTrace()
    appWin.show()

    sys.exit(app.exec_())
