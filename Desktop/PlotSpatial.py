'''
    空间分布
    复用了ui界面，但重载了plot函数

'''
import os,time
import sys
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QApplication
import pandas as pd
import geopandas as gpd

import myservice
from BrowserDialog import BrowserDialog
from pandasgui.store import PandasGuiDataFrameStore
from pandasgui.widgets.dataframe_explorer import DataFrameExplorer
from ui.ui_plot_tas import Ui_TASPlot


class PlotSpatial(QWidget):
    ui = Ui_TASPlot()

    def __init__(self,parent=None):
        super(PlotSpatial, self).__init__(parent)
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
        longitude = ''
        latitude = ''
        for col in self.df.columns:
            if col.lower().strip() in ['longitude','经度']:
                longitude = col
            if col.lower().strip() in ['latitude', '纬度']:
                latitude = col
        if longitude == '' or latitude == '':
            QMessageBox.information(self, "Tips", "Please check data ,must have longitude and latitude column!")
            return
        #  去除掉空数据data.dropna(axis=0,subset = ["Age", "Sex"])   # 丢弃‘Age’和‘Sex’这两列中有缺失值的行
        self.df.dropna(axis=0,subset = [longitude, latitude],inplace=True)
        gdf = gpd.GeoDataFrame(self.df, geometry=gpd.points_from_xy(self.df[longitude], self.df[latitude]), crs=4326)
        m = gdf.explore(
                color='#40a9ff',
                #tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                attr=' ',
                width='100%',
                tooltip=False, # 关闭鼠标悬浮时的空白tooltip
                marker_type='circle_marker',

                style_kwds={
                    'color': 'red',
                    'fillOpacity': 0.4
                },
                highlight_kwds={
                    'fillColor': 'white',
                    'fillOpacity': 0.6
                },
                marker_kwds={
                    'radius' : 6 # 点的半径，像素数，marker_type配合使用
                   # 'icon': folium.map.Icon(icon='beer', prefix='fa')
                }
               )
        browser =BrowserDialog(myUrl="",parent=self)
        #临时文件名
        filename = time.strftime("Spatial%Y-%m-%d %H_%M_%S.html", time.localtime())
        m.save(filename)
        browser.openHtml( os.path.abspath(filename))
        browser.setWindowTitle("Spatial distribution")

        browser.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = PlotSpatial()
    appWin.show()

    sys.exit(app.exec_())

