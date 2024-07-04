from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QDialog

from ui.ui_browser import Ui_Browser
from PyQt5 import QtCore

class BrowserDialog(QDialog):
    ui=Ui_Browser()

    def __init__(self, myUrl, parent=None):
        super(BrowserDialog, self).__init__( parent)
        self.setupUi()

        self.browser = QWebEngineView()
        Url = myUrl
        self.browser.setUrl(QtCore.QUrl(Url))
        self.browser.page().fullScreenRequested.connect(self.handleFullscreenRequest)
        self.browser.settings().globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.browser.settings().globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        #self.browser.showFullScreen()
        self.ui.horizontalLayout.addWidget(self.browser)
        self.setLayout(self.ui.horizontalLayout)

        self.setWindowFlags(Qt.Dialog | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(1024,768)

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

    def setHtml(self,html):
        self.browser.setHtml(html)

    def openHtml(self,file):
        self.browser.load(QtCore.QUrl.fromLocalFile(file))