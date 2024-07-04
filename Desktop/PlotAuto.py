'''
    TAS 图解
    左侧是数据，右侧是图，采用dockwidget方式，可以浮动放大

'''
import os
import sys
import traceback

import matplotlib
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QApplication, QDialog
import  pandas as pd

import myservice
from DfColumnMappingWidget import DfColumnMappingWidget
from MyEntityMappingWidget import MyEntityMappingWidget
from geopytool.CIPW import CIPW
from geopytool.Harker import Harker
from geopytool.Pearce import Pearce
from geopytool.REE import REE
from geopytool.TAS import TAS
from geopytool.Trace import Trace
from pandasgui.store import PandasGuiDataFrameStore
from pandasgui.widgets.dataframe_explorer import DataFrameExplorer
from ui.ui_plot_tas import Ui_TASPlot


class PlotAuto(QWidget):
    ui = Ui_TASPlot()

    def __init__(self,parent=None):
        super(PlotAuto, self).__init__(parent)
        self.setupUi()
        self.df = None
        self.Standard = {}  # Standard is initialized as a blank Dict



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
        ''' ['SiO2', 'TiO2',    'Al2O3', 'Fe2O3',   'FeO', 'MnO','MgO','CaO','Na2O',
                 'K2O',  'P2O5',    'CO2',    'SO3',    'S',
                 'F',    'Cl', 'Sr', 'Ba',   'Ni','Cr',   'Zr']
                 
                 {"Name": "CO2", "Desc": "CO2", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "SO3", "Desc": "SO3", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Mo", "Desc": "Mo", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "S", "Desc": "S", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "F", "Desc": "F", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Cl", "Desc": "Cl", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                 '''
        datalist = [{"Name": "Label", "Desc": "点的标签值", "Type": "String","UseDefault":False,"DefaultValue":"a"},
                    {"Name": "Color", "Desc": "颜色值，red，green等", "Type": "String","UseDefault":True,"DefaultValue":"red"},
                    {"Name": "Marker", "Desc": "分类标签，例如O，*", "Type": "String","UseDefault":True,"DefaultValue":"*"},
                    {"Name": "Size", "Desc": "图标大小，默认10", "Type": "Float","UseDefault":True,"DefaultValue":"10"},
                    {"Name": "Width", "Desc": "宽度，默认1", "Type": "Float","UseDefault":True,"DefaultValue":"1"},
                    {"Name": "Style", "Desc": "渲染风格，默认-", "Type": "String","UseDefault":True,"DefaultValue":"-"},
                    {"Name": "Alpha", "Desc": "透明度，默认0.6，取值范围0~1", "Type": "Float","UseDefault":True,"DefaultValue":"0.6"},
                    {"Name": "SiO2", "Desc": "SiO2", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "TiO2", "Desc": "TiO2", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "Al2O3", "Desc": "Al2O3", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "Fe2O3", "Desc": "Fe2O3", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "FeO", "Desc": "FeO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "MnO", "Desc": "MnO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "MgO", "Desc": "MgO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "CaO", "Desc": "CaO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Na2O", "Desc": "Na2O", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "K2O", "Desc": "K2O", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "P2O5", "Desc": "P2O5", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},

                    {"Name": "Sr", "Desc": "Sr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ba", "Desc": "Ba", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ni", "Desc": "Ni", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Cr", "Desc": "Cr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Zr", "Desc": "Zr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"}]
        '''[{"Name": "Label", "Desc": "点的标签值", "Type": "String","UseDefault":False,"DefaultValue":"a"},
                    {"Name": "Color", "Desc": "颜色值，red，green等", "Type": "String","UseDefault":True,"DefaultValue":"red"},
                    {"Name": "Marker", "Desc": "分类标签，例如O，*", "Type": "String","UseDefault":True,"DefaultValue":"*"},
                    {"Name": "Size", "Desc": "图标大小，默认10", "Type": "Float","UseDefault":True,"DefaultValue":"10"},
                    {"Name": "Width", "Desc": "宽度，默认1", "Type": "Float","UseDefault":True,"DefaultValue":"1"},
                    {"Name": "Style", "Desc": "渲染风格，默认-", "Type": "String","UseDefault":True,"DefaultValue":"-"},
                    {"Name": "Alpha", "Desc": "透明度，默认0.6，取值范围0~1", "Type": "Float","UseDefault":True,"DefaultValue":"0.6"},
                    {"Name": "SiO2", "Desc": "SiO2", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "TiO2", "Desc": "TiO2", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "Al2O3", "Desc": "Al2O3", "Type": "Float","UseDefault":False,"DefaultValue":"0"},
                    {"Name": "Fe2O3", "Desc": "Fe2O3", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "FeO", "Desc": "FeO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "MnO", "Desc": "MnO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "MgO", "Desc": "MgO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "CaO", "Desc": "CaO", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Na2O", "Desc": "Na2O", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "K2O", "Desc": "K2O", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "P2O5", "Desc": "P2O5", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Cs", "Desc": "Cs", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Tl", "Desc": "Tl", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Rb", "Desc": "Rb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ba", "Desc": "Ba", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "W", "Desc": "W", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Th", "Desc": "Th", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Nb", "Desc": "Nb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ta", "Desc": "Ta", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "K", "Desc": "K", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "La", "Desc": "La", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ce", "Desc": "Ce", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Pb", "Desc": "Pb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Pr", "Desc": "Pr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Mo", "Desc": "Mo", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Sr", "Desc": "Sr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "P", "Desc": "P", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Nd", "Desc": "Nd", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "F", "Desc": "F", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Sm", "Desc": "Sm", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Zr", "Desc": "Zr", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Hf", "Desc": "Hf", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "E", "Desc": "E", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Sn", "Desc": "Sn", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Sb", "Desc": "Sb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ti", "Desc": "Ti", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Gd", "Desc": "Gd", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Tb", "Desc": "Tb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Dy", "Desc": "Dy", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Li", "Desc": "Li", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Y", "Desc": "Y", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Ho", "Desc": "Ho", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Er", "Desc": "Er", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Tm", "Desc": "Tm", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Yb", "Desc": "Yb", "Type": "Float", "UseDefault": False, "DefaultValue": "0"},
                    {"Name": "Lu", "Desc": "Lu", "Type": "Float", "UseDefault": False, "DefaultValue": "0"}]'''
        w=DfColumnMappingWidget(self.df,datalist,parent=self)
        w.showDlg()
        if hasattr(w,"df"):
            df = w.df.reset_index(drop=True)
            TotalResult = []
            AutoResult = 0
            FileOutput, ok1 = QFileDialog.getSaveFileName(self,
                                                          '文件保存',
                                                          'C:/',
                                                          'PDF Files (*.pdf)')  # 数据文件保存输出
            if (FileOutput != ''):

                AutoResult = pd.DataFrame()

                pdf = matplotlib.backends.backend_pdf.PdfPages(FileOutput)

                cipwsilent = CIPW(df=df)
                cipwsilent.CIPW()
                cipwsilent.QAPFsilent()
                # TotalResult.append(cipwsilent.OutPutFig)
                pdf.savefig(cipwsilent.OutPutFig)

                # AutoResult = pd.concat([cipwsilent.OutPutData, AutoResult], axis=1)

                tassilent = TAS(df=df)

                tassilent.TAS()
                tassilent.GetResult()
                # TotalResult.append(tassilent.OutPutFig)

                pdf.savefig(tassilent.OutPutFig)

                AutoResult = pd.concat([tassilent.OutPutData, AutoResult], axis=1)

                reesilent = REE(df=df, Standard=self.Standard)

                if (reesilent.Check() == True):
                    reesilent.REE()
                    reesilent.GetResult()
                    # TotalResult.append(reesilent.OutPutFig)

                    pdf.savefig(reesilent.OutPutFig)

                    AutoResult = pd.concat([reesilent.OutPutData, AutoResult], axis=1)

                tracesilent = Trace(df=df, Standard=self.Standard)

                if (tracesilent.Check() == True):
                    tracesilent.Trace()
                    tracesilent.GetResult()
                    TotalResult.append(tracesilent.OutPutFig)

                    pdf.savefig(tracesilent.OutPutFig)

                harkersilent = Harker(df=df)

                harkersilent.Harker()
                harkersilent.GetResult()
                TotalResult.append(harkersilent.OutPutFig)

                pdf.savefig(harkersilent.OutPutFig)

                pearcesilent = Pearce(df=df)

                pearcesilent.Pearce()
                pearcesilent.GetResult()
                TotalResult.append(pearcesilent.OutPutFig)

                pdf.savefig(pearcesilent.OutPutFig)

                AutoResult = AutoResult.T.groupby(level=0).first().T

                pdf.close()

                AutoResult = AutoResult.set_index('Label')

                AutoResult = AutoResult.drop_duplicates()

                print(AutoResult.shape, cipwsilent.newdf3.shape)

                try:
                    AutoResult = pd.concat([cipwsilent.newdf3, AutoResult], axis=1)
                except(ValueError):
                    pass

                if ('pdf' in FileOutput):
                    FileOutput = FileOutput[0:-4]

                AutoResult.to_csv(FileOutput + '-chemical-info.csv', sep=',', encoding='utf-8')
                cipwsilent.newdf.to_csv(FileOutput + '-cipw-mole.csv', sep=',', encoding='utf-8')
                cipwsilent.newdf1.to_csv(FileOutput + '-cipw-mass.csv', sep=',', encoding='utf-8')
                cipwsilent.newdf2.to_csv(FileOutput + '-cipw-volume.csv', sep=',', encoding='utf-8')
                cipwsilent.newdf3.to_csv(FileOutput + '-cipw-index.csv', sep=',', encoding='utf-8')



            else:
                pass


if __name__=='__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = PlotAuto()
    appWin.show()

    sys.exit(app.exec_())
