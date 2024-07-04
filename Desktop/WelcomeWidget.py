'''
    显示欢迎页面，暂时做了一个空页面替代，后期可以完善ui文件，或者加载html
    by：dingyi
    2021-11-27
'''
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication,QStyleFactory
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *


from ui.ui_welcome import Ui_Welcome

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings


class WelcomeWidget(QWidget):
    ui=Ui_Welcome()

    def __init__(self, parent=None):
        super(WelcomeWidget, self).__init__( parent)
        self.setupUi()

        self.browser = QWebEngineView()
        Url = 'http://petrology.deep-time.org/'
        self.browser.setUrl(QtCore.QUrl(Url))
        self.browser.page().fullScreenRequested.connect(self.handleFullscreenRequest)
        self.browser.settings().globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.browser.settings().globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        # self.browser.showFullScreen()
        self.ui.horizontalLayout.addWidget(self.browser)
        self.setLayout(self.ui.horizontalLayout)

    def handleFullscreenRequest(self, request):

        print("requested")

        if (request.toggleOn()):
            request.accept()
            self.ui.horizontalLayout.removeWidget(self.browser)
            self.browser.setParent(None, QtCore.Qt.Window)
            self.browser.showFullScreen()
        else:
            request.accept()
            self.ui.horizontalLayout.addWidget(self.browser)
    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = WelcomeWidget()
    dfe.show()

    sys.exit(app.exec_())
