"""
    自定义标题栏，用来模拟原来的标题栏的动作
    author：dingyi

"""
import datetime
import sys

from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

import myservice
from ui.ui_mytoolbar import Ui_MyToolBar


class MyToolBarWidget(QWidget):
    # 自定义信号
    # 左侧OperPanel操作栏的按钮信号
    _signal_oper_clicked = pyqtSignal(str, str, str, str, str)  # 参数代表含义：第一个代表是什么操作，第二个代表操作描述，第三个留作扩展（用于插件的类的描述，动态加载）

    ui = Ui_MyToolBar()

    def __init__(self,parent=None):
        super(MyToolBarWidget, self).__init__(parent)
        # 初始化ui
        self.setupUi()
        # 初始化变量
        self.m_bPressed = False

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 按钮处理函数
        self.ui.btnPublicKnowledge.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("PublicKnowledge", "Public KnowLedge Tree Edit ", ""))
        self.ui.btnPrivateKnowledge.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("PrivateKnowledge", "Private KnowLedge Tree Edit ", ""))
        self.ui.btnUploadPaper.clicked.connect(lambda : myservice.main_window._signal_oper_clicked.emit("SubmitPaper", "Submit paper or report to Public Files", ""))
        self.ui.btnBrowsePaper.clicked.connect (lambda :myservice.main_window._signal_oper_clicked.emit("BrowsePaper", "Browse Paper or Reports in repository", ""))
        self.ui.btnExtractTable.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("Pdf One", "Process pdf files one by one ", ""))
        self.ui.btnExtractBatch.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("Pdf batch", "Process pdf files batch...", ""))
        self.ui.btnUploadExcel.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("UploadData", "Upload Data File", ""))
        self.ui.btnBrowseExcel.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("BrowseDataFile", "Process the Uploaded Data Files", ""))
        self.ui.btnImportData.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("ProcessDataFile", "Process the Uploaded Data Files", ""))
        self.ui.btnPublicData.clicked.connect(lambda : myservice.main_window._signal_oper_clicked.emit("PublicData", "View the public data......", ""))
        self.ui.btnPrivateData.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("MyData", "View the my private data......", ""))

        self.ui.btnDuplicateCheck.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("Duplicate Checking", "Check the data and find the duplicate......", None))
        self.ui.btnPlotTAS.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("TAS", "TAS (total alkali–silica) diagram Volcanic/Intrusive (Wilson et al. 1989)", None))
        self.ui.btnPlotTrace.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("Trace", "Trace ---Reference: Sun, S. S., and Mcdonough, W. F., 1989, UCC_Rudnick & Gao2003", None))
        self.ui.btnPlotREE.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("REE", "REE ---Reference: Sun, S. S., and Mcdonough, W. F., 1989, UCC_Rudnick & Gao2003", None))
        self.ui.btnPlotPearce.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("Pearce",
                                                                                                   "Pearce ---Pearce diagram (after Julian A. Pearce et al., 1984).",
                                                                                                   None))
        self.ui.btnPlotHarker.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("Harker",
                                                                                                   "Harker ---Harker diagram",
                                                                                                   None))
        self.ui.btnPlotCIPW.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("CIPW",
                                                                                                      "CIPW Norm Result",
                                                                                                      None))
        self.ui.btnPlotSaccani.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("Saccani",
                                                                                                      "Emilio Saccani Plot doi.org/10.1016/j.gsf.2014.03.006.",
                                                                                                      None))
        self.ui.btnPlotK2OSiO2.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("K2OSiO2",
                                                                                                       "K2O-SiO2diagram'",
                                                                                                       None))
        self.ui.btnPlotRamanStrength.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("Raman",
                                                                                                       "Raman  Strength diagram",
                                                                                                       None))
        self.ui.btnPlotFluidInclusion.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("FluidInclusion",
                                                                                                       "Fluid Inclusion  Plot",
                                                                                                       None))
        self.ui.btnPlotHarkerClassical.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("HarkerClassical",
                                                                                                       "Classical Harker diagram",
                                                                                                       None))
        self.ui.btnPlotZrYSrTi.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("ZrYSrTi",
                                                                                                       "Zr, Ti, Y and Sr analyses of oceanic basalts",
                                                                                                       None))
        self.ui.btnPlotTiAlCaMgMnKNaSi.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("TiAlCaMgMnKNaSi",
                                                                                                       "TiO2-Al2O3-CaO-MgO-MnO-K2O-Na2O-SiO2 major element patterns in basalts",
                                                                                                       None))
        self.ui.btnPlotAuto.clicked.connect(lambda: myservice.main_window._signal_oper_clicked.emit("Auto",
                                                                                                       "CIPW-QAPF-TAS-Harker-Pearce-REE-Trace plots",
                                                                                                       None))
        self.ui.btnPlotDensityHeatmap.clicked.connect(lambda :QMessageBox.information(self, 'Tips',
                                    'This function is coming soon...',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes))

        self.ui.btnPostGis.clicked.connect(lambda :QMessageBox.information(self, 'Tips',
                                    'This function is coming soon...',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes))
        self.ui.btnGeoPlot.clicked.connect(lambda :QMessageBox.information(self, 'Tips',
                                    'This function is coming soon...',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes))
        # profile，弹框修改
        self.ui.btnProfile.clicked.connect(lambda :QMessageBox.information(self, 'Tips',
                                    'This function is coming soon...',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes))
        self.ui.btnSaveLayout.clicked.connect(lambda :myservice.main_window.saveLayout())
        self.ui.btnRestoreLayout.clicked.connect(lambda :myservice.main_window.restoreLayout())
        self.ui.btnLog.clicked.connect( lambda:myservice.main_window.showLog())
        self.ui.btnCheckUpdate.clicked.connect(lambda :myservice.main_window.doCheckUpdate())
        self.ui.btnAbout.clicked.connect(lambda :myservice.main_window.about())
        self.ui.btnExit.clicked.connect(lambda :myservice.main_window.doExit())
         # 处理当前默认的窗口
        self.ui.tabWidget.currentChanged.connect(self.tabchange)

        #plot按钮
        self.ui.btnPlotSpatial.clicked.connect(lambda :myservice.main_window._signal_oper_clicked.emit("PlotSpatial", "View  data space distribution......", ""))


        # 初始化timer，更新时钟
        self.timer=QTimer()
        self.timer.timeout.connect(self.doRefreshTime)
        self.timer.start(1000) #每秒刷新

    def tabchange(self):
        tabName=self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())
        if tabName=="预算决算":
            pass

    def doRefreshTime(self):
        curr_time = datetime.datetime.now()
        strTime = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
        self.ui.lblTime.setText("Current：" + strTime)



if __name__=='__main__':
    app = QApplication(sys.argv)

    appWin = MyToolBarWidget()
    appWin.showMaximized()
    sys.exit(app.exec_())