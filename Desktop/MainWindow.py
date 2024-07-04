'''

主窗口类
   主窗口类采用dockwidget方式，由于dockwidget方式的特殊性，需要进行一些布局设置

   所有的功能组件直接嵌入到dockwidget中来实现

   本文件定义系统中所有的自定义信号
   信号均实例在mainwindows中，各个widget通过两次parent去关联信号


  by：dingyi
     2021-11-29
'''
import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  QMessageBox, QMainWindow, QDialog, QWidget

import myservice
from AboutDlg import AboutDlg
from BrowserWidget import BrowserWidget
from DuplicateCheckWidget import DuplicateCheckWidget
from KnowledgeTree4My import KnowledgeTree4My
from KnowledgeTree4Root import KnowledgeTree4Root
from LoadingMask import LoadingMask
from PdfBatchProcessWidget import PdfBatchProcessWidget
from PdfExtractExcelWidget import PdfExtractExcelWidget
from PdfSubmitWidget import PdfSubmitWidget
from PlotAuto import PlotAuto
from PlotCIPW import PlotCIPW
from PlotFluidInclusion import PlotFluidInclusion
from PlotHarker import PlotHarker
from PlotHarkerClassical import PlotHarkerClassical
from PlotK2OSiO2 import PlotK2OSiO2
from PlotPearce import PlotPearce
from PlotREE import PlotREE
from PlotRaman import PlotRaman
from PlotSaccani import PlotSaccani
from PlotSpatial import PlotSpatial
from PlotTAS import PlotTAS
from PlotTiAlCaMgMnKNaSi import PlotTiAlCaMgMnKNaSi
from PlotTrace import PlotTrace
from PlotZrYSrTi import PlotZrYSrTi
from PrivateDataWidget import PrivateDataWidget
from ProcessExcelWidget import ProcessExcelWidget
from PublicDataWidget import PublicDataWidget

from ui.ui_mainwindow import Ui_MainWindow

from UploadBitstreamWidget import UploadBitstreamWidget

from LoginDlg import LoginDlg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QEvent


class MainWindow(QMainWindow):
    # 配置文件路径
    configFile = "config/layout.ini"

    # 自定义信号
    signal_tree_double_clicked = pyqtSignal(str, str)  # 自定义左侧树结构的双击信号，  uuid,type,科学家姓名

    # 左侧OperPanel操作栏的按钮信号
    _signal_oper_clicked = pyqtSignal(str, str, object)  # 参数代表含义：第一个代表是什么操作，第二个代表操作描述，第三个留作扩展（用于插件的类的描述，动态加载）

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()  # ui对象，通过ui文件自动编译而来
        self.operWidget = {}
        self.setupUI()
        # 登录，成功了继续，不成功则退出
        dlg = LoginDlg(parent)
        if not dlg.login:
            dlg.exec()
        if (dlg.login):
            print('登录成功')
            myservice.username = dlg.ui.txtUser.text()  # 保存用户名
            myservice.main_window = self
            #myservice.initData()
        else:
            dlg.close()
            sys.exit(0)




        # 恢复布局，与action不同的是没有提示
        if os.path.exists(self.configFile):
            with open(self.configFile, 'rb') as f:
                s = f.read()
                self.restoreState(s)
    # 覆写方法
    def changeEvent(self, event):  # real signature unknown
        if event.type() == QEvent.ActivationChange:
            self.repaint()

        pass
    # 保存布局
    def saveLayout(self):
        with open(self.configFile, 'wb') as f:
            s = self.saveState()
            f.write(s)
        QMessageBox.information(self, "Tips", "Current layout state has saved！you can restore it any time.", QMessageBox.Yes, QMessageBox.Yes)
        pass
    # 恢复布局
    def restoreLayout(self):
        if os.path.exists(self.configFile):
            with open(self.configFile, 'rb') as f:
                s = f.read()
                self.restoreState(s)
                QMessageBox.information(self, "Tips", "Layout state has restored from your save.",
                                        QMessageBox.Yes, QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "Warning", "Cant't find last state file. please save it first.",
                                    QMessageBox.Yes, QMessageBox.Yes)


    def about(self):
        # 显示关于对话框
        aboutDlg = AboutDlg(self)
        aboutDlg.exec()

    def doExit(self):
        if QMessageBox.question(self, "Tips", "Are you sure to quit ?", QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes) == QMessageBox.No:

            return False
        self.close()
        return True

    def doWindowMax(self):
        if self.windowState() ==Qt.WindowMaximized:
            self.setWindowState(Qt.WindowNoState)
        else:
            self.setWindowState(Qt.WindowMaximized)

    def doWindowMin(self):
        self.setWindowState(Qt.WindowMinimized)


    def doClose(self):
        if QMessageBox.question(self, "Tips", "Are you sure to quit ?", QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes) == QMessageBox.No:
            return False
        self.close()
        sys.exit(0)

    def doWindowMove(self,p):
        if self.windowState()!=Qt.WindowMaximized:
            self.move(self.pos()+p)  #根据信号移动窗口

    def setupUI(self):
        # 初始化窗口
        self.ui.setupUi(self)
        # 移除掉dockwidget的title
        self.ui.dockTop.setTitleBarWidget(QWidget())
        # self.ui.dockOper.setTitleBarWidget(QWidget())
        # 连接title的处理函数
        self.ui.title.windowMax.connect(self.doWindowMax)
        self.ui.title.windowMin.connect(self.doWindowMin)
        self.ui.title.windowClose.connect(self.doClose)
        self.ui.title.windowMove.connect(self.doWindowMove)

        # 设置dock的相对位置及显示方式
        self.setTabPosition(Qt.LeftDockWidgetArea, QtWidgets.QTabWidget.TabPosition.West)  # 左边的tab位置在左侧
        # self.tabifyDockWidget(self.ui.dockTraditionalTree,self.ui.dockScientist)  #左侧两个叠加
        self.setTabPosition(Qt.RightDockWidgetArea, QtWidgets.QTabWidget.TabPosition.North)  # 右边的tab位置在上端
        # 调整列表布局，使之重叠
        # self.tabifyDockWidget(self.ui.dockOper, self.ui.dockInfo)
        # self.tabifyDockWidget(self.ui.dockWelcome,self.ui.dockKnowledge)
        # 连接信号
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionSaveState.triggered.connect(self.saveLayout)
        self.ui.actionRestoreState.triggered.connect(self.restoreLayout)
        self.ui.actionExit.triggered.connect(self.doExit)
        self.ui.actionCheck_update.triggered.connect(self.doCheckUpdate)
        # self.installEventFilter(self)

        self._signal_oper_clicked.connect(self.doOper)
        self.ui.tabWidget.tabCloseRequested.connect(self.tabClose)
        # 设置日志窗口
        from logbook import LogbookWidget
        my_logbook_instance = LogbookWidget()
        self.ui.dockInfo.setWidget(my_logbook_instance)
        myservice.logger.addHandler(my_logbook_instance.handler)

        # 设置等待对话框
        loading_mask = LoadingMask(self, 'res/loading.gif')
        myservice.loading_mask = loading_mask
        myservice.loading_mask.hide()

    def doCheckUpdate(self):

        if myservice.checkUpdate():
            # 检查版本的代码暂缺 todo
            if QMessageBox.question(self, "Question", "New Vision has come! \n\n You  need to exit application to update,Do you want to continue?",
                                    QMessageBox.Yes| QMessageBox.No, QMessageBox.Yes) ==QMessageBox.No:
                return
            # 退出自己，并调用起 update.exe
            self.close()
            os.system("start update.exe")
            # # 显示更新对话框
            # dlg = UpdateDlg(self)
            # dlg.show()
        else:

            # 检查版本的代码暂缺 todo
            QMessageBox.information(self, "Tips", "The current version is the latest.",
                                    QMessageBox.Yes, QMessageBox.Yes)

    # 关闭事件覆写，目前不起作用，不知道为啥，todo
    def closeEvent(self, event):
        print("close is calling")

        if QMessageBox.question(self, "Tips", "Are you sure to quit ?", QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes) == QMessageBox.No:
            event.ignore()
            return
        # 接受，退出
        event.accept()
        # 记录state

    # 移除
    def tabClose(self, index):
        # 保留welcome 不允许关闭
        if self.ui.tabWidget.tabText(index) == "Welcome":
            return
        self.ui.tabWidget.removeTab(index)

    # 处理状态栏函数
    def workerStatus(self, msg):
        self.statusBar().showMessage(msg)

    # 显示和隐藏log窗口
    def showLog(self):
        if self.ui.dockInfo.isVisible():
            myservice.logger.info("hide log ui")
            self.ui.dockInfo.setVisible(False)
        else:
            myservice.logger.info("show log ui")
            self.ui.dockInfo.setVisible(True)

    # 处理信号
    def doOper(self, cmd, desc, obj):
        # 显示等待对话框
        myservice.loading_mask.show()

        if cmd == "PublicKnowledge":  # 公用知识树
            # 检测该组件是否已存在，如果已存在则激活，如果不存在，则添加

            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = KnowledgeTree4Root()
                myservice.logger.info("create ROOT KnowledgeTree UI")
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate ROOT KnowledgeTree UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/entity.png'))

        elif cmd == "PrivateKnowledge":  # 自定义知识树

            # 检测该组件是否已存在，如果已存在则激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = KnowledgeTree4My()
                myservice.logger.info("create My KnowledgeTree UI")
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate My KnowledgeTree UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/edit.png'))

        elif cmd == "UploadData":  # 上传文件
            # 检测该组件是否已存在，如果已存在则激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = UploadBitstreamWidget()
                myservice.logger.info("create DataTransRoom UI")
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate DataTransRoom UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/upload.png'))
        elif cmd == "BrowseDataFile":  # 浏览文件
            # 检测该组件是否已存在，如果已存在则激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = BrowserWidget(
                    "https://petrology.deep-time.org/dspace/collections/a6c00453-2942-460a-ae2f-52d601a501bf", self)
                myservice.logger.info("create Browse Data File UI")
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Browse Data File UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/browse.png'))
        elif cmd == "ProcessDataFile":  # 处理excel数据文件
            # 检测该组件是否已存在，如果已存在则激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = ProcessExcelWidget(self)
                myservice.logger.info("create Process Data File UI")
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Process Data File UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/process.png'))
        elif cmd == "SubmitPaper":  # 提交PDF文件
            # 检测该组件是否已存在，如果已存在则激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = PdfSubmitWidget(self)
                myservice.logger.info("create Submit Pdf  File UI")
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("create Submit Pdf  File UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/Public.png'))
        elif cmd == "BrowsePaper":  # 浏览文件
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = BrowserWidget(
                    "https://petrology.deep-time.org/dspace/collections/c04dce5a-2f71-4ef9-a872-b55f290511d2", self)
                myservice.logger.info("create Browse Paper  UI")
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Browse Paper File UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/private.png'))
        elif cmd == "Pdf One":  # 处理单个文件的提取
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = PdfExtractExcelWidget(self)
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate PDF extract table  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/PDF.png'))
        elif cmd == "Pdf batch":  # 批量处理多个文件的提取
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = PdfBatchProcessWidget(self)
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate PDF Batch Process  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/pdf-batch.png'))
        elif cmd == "PublicData":  # 批量处理多个文件的提取
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = PublicDataWidget(self)
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Public Data  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/Public.png'))
        elif cmd == "MyData":  # 批量处理多个文件的提取
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = PrivateDataWidget(self)
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate My Private Data  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/private.png'))
        elif cmd == "Duplicate Checking":  # 查重
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = DuplicateCheckWidget(self)
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate My Private Data  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/filter.png'))
            # 把第三个参数df赋值给界面
            self.operWidget[cmd].setDf(obj)

        elif cmd == "TAS":  # TAS 图解
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotTAS(self)
            else:
                # 此时需要把df设置到TAS中，使之重新绘图 ，代码暂缺
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot TAS  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/xy.png'))
        elif cmd == "Trace":  # Trace 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotTrace(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot Trace  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/spider2.png'))
        elif cmd == "REE":  # REE 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotREE(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot REE  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/spider2.png'))
        elif cmd == "Pearce":  # REE 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotPearce(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot Pearce  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/spider.png'))
        elif cmd == "Harker":  # REE 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotHarker(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot Harker  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/spider.png'))
        elif cmd == "CIPW":  # REE 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotCIPW(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot CIPW  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/calc.png'))
        elif cmd == "Saccani":  # REE 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotSaccani(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot Saccani  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/s.png'))
        elif cmd == "K2OSiO2":  # REE 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotK2OSiO2(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot K2OSiO2  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/xy.png'))
        elif cmd == "Raman":  # Raman Strength 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotRaman(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot Raman Strength  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/r.png'))
        elif cmd == "FluidInclusion":  # Fluid Inclusion 图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotFluidInclusion(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot Fluid Inclusion  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/f.png'))
        elif cmd == "HarkerClassical":  # HarkerClassical图
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotHarkerClassical(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot HarkerClassical   UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/spider.png'))
        elif cmd == "ZrYSrTi":  # ZrYSrTi
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotZrYSrTi(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot ZrYSrTi   UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/xy.png'))
        elif cmd == "TiAlCaMgMnKNaSi":  # ZrYSrTi
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotTiAlCaMgMnKNaSi(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot TiAlCaMgMnKNaSi   UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/xy.png'))
        elif cmd == "Auto":  # ZrYSrTi
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # # 此时需要创建并添加到dict中
                # if obj is None:
                #     # 默认加载一个测试文件，暂时是config中的Wholw.csv
                #     obj = pd.read_csv("config/Whole.csv", engine='python')
                self.operWidget[cmd] = PlotAuto(self)
            else:
                # 此时需要把df设置到Trace中，使之重新绘图 ，代码暂缺todo
                pass
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot Auto  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/geopytool/auto.png'))
        elif cmd == "PlotSpatial":
            # 检测该组件是否已存在，如果已存在则BrowseDataFile激活，如果不存在，则添加
            if self.operWidget.get(cmd) is None:
                # 此时需要创建并添加到dict中
                self.operWidget[cmd] = PlotSpatial(self)
            # 判断此时是否已在tab中
            curIndex = self.ui.tabWidget.indexOf(self.operWidget[cmd])
            if curIndex == -1:
                # 此时不存在，需要添加
                curIndex = self.ui.tabWidget.addTab(self.operWidget[cmd], cmd)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            myservice.logger.info("activate Plot Spatial  UI")
            # 设置tooltip
            self.ui.tabWidget.setTabToolTip(curIndex, desc)
            # 设置Icon
            self.ui.tabWidget.setTabIcon(curIndex, QIcon('res/GIS.png'))



        elif cmd == "DataPlot":  # 批量处理多个文件的提取
            QMessageBox.information(self, 'Tips',
                                    'This function is coming soon...',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes)
        elif cmd == "PostGis":  # 批量处理多个文件的提取
            QMessageBox.information(self, 'Tips',
                                    'This function is coming soon...',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes)
        elif cmd == "GeoPlot":  # 批量处理多个文件的提取
            QMessageBox.information(self, 'Tips',
                                    'This function is coming soon...',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes)
        elif cmd == "MyProfile":  # 批量处理多个文件的提取
            QMessageBox.information(self, 'Tips',
                                    'This function is coming soon...',
                                    QMessageBox.Yes,
                                    QMessageBox.Yes)
        # 隐藏等待对话框
        myservice.loading_mask.hide()
    # 退出询问

    # def resizeEvent(self, event):
    # self.centralWidget().resize(event.size().width() * 0.7, event.size().height())
    #     width1 = int(event.size().width() * 0.1)
    #     width2 = int(event.size().width() * 0.9)
    #     # height1 = int(event.size().height()*0.8)
    #     # height2 = int(event.size().height() * 0.2)
    #     # self.resizeDocks([self.ui.dockOper, self.ui.dockInfo], [height1, height2], Qt.Vertical)
    #     # self.resizeDocks([self.ui.dockInfo, self.ui.dockWelcome], [width1, width2], Qt.Horizontal)
    #     self.resizeDocks([self.ui.dockOper, self.ui.dockWelcome], [width1, width2], Qt.Horizontal)
