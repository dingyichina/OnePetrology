# encoding=utf-8
import os
os.environ['HDF5_DISABLE_VERSION_CHECK'] = '2'  # 忽略掉hdf文件版本不一致的问题
from qgis.core import QgsApplication
#QgsApplication.setPrefixPath("D:/QGIS-3.28.15/")
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import  QSplashScreen
from PyQt5.QtCore import Qt
import sys


import myservice
from MainWindow import MainWindow

if __name__ == '__main__':
    try:
        import os

        os.environ[
            "QTWEBENGINE_CHROMIUM_FLAGS"
        ] = "--no-sandbox,--enable-features=NetworkServiceInProcess , --single-process"
        from PyQt5.QtCore import Qt
        from PyQt5.QtGui import QGuiApplication

        ######使用下面的方式一定程度上可以解决界面模糊问题--解决电脑缩放比例问题
        QgsApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        QgsApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QgsApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
        # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        #QgsApplication.setPrefixPath("D:/QGIS 3.34.4/", True); #// 这里必须是true
        qgs = QgsApplication([], True)
        # QgsApplication.setPrefixPath("D:\\QGIS 3.22.12", True)
        print("prefix", QgsApplication.prefixPath())
        qgs.initQgis()
        # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
        splash = QSplashScreen()
        splash.setPixmap(QPixmap('res/splash.png'))
        splash.setFont(QFont("microsoft yahei", 12, QFont.Bold))
        splash.show()
        splash.showMessage('Welcome to Use DDE-OnePetrology ,please wait for loading......',
                           Qt.AlignBottom | Qt.AlignCenter, Qt.green)

        appWin = MainWindow()
        appWin.setWindowFlags(Qt.FramelessWindowHint)
        myservice.logger.info("system starting ...")

        appWin.showMaximized()
        splash.finish(appWin)

        # sys.exit(app.exec_())

        exitCode = qgs.exec()
        qgs.exitQgis()
    except Exception as e:
        myservice.logger.error(e)
