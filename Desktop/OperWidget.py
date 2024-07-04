'''
    封装的左侧操作面板

    by dingyi
    2022-01-29
'''
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

import myservice
from ui.ui_oper import Ui_OperPanel


class OperWidget(QWidget):
    ui=Ui_OperPanel()

    def __init__(self,parent=None):
        super(OperWidget, self).__init__(parent)
        self.setWindowTitle("Operate Panel")
        self.setupUi()


    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.tbtnKb.clicked.connect(self.kb4root)
        self.ui.tbtnKbMy.clicked.connect(self.kb4my)
        self.ui.tbtnUpload.clicked.connect(self.upload)
        self.ui.tbtnProcessFile.clicked.connect(self.processFile)
        self.ui.tbtnBrowseFiles.clicked.connect(self.browseFile)
        self.ui.tbtnPublicPaper.clicked.connect(self.publicPaper)
        self.ui.tbtnMyPaper.clicked.connect(self.myPaper)
        self.ui.tbtnPdfOne.clicked.connect(self.pdfOne)
        self.ui.tbtnPdfBatch.clicked.connect(self.pdfBatch)
        self.ui.tbtnPublicData.clicked.connect(self.publicData)
        self.ui.tbtnMyData.clicked.connect(self.myData)
        self.ui.tbtnDataPlot.clicked.connect(self.dataPlot)
        self.ui.tbtnPostGis.clicked.connect(self.postGis)
        self.ui.tbtnGeoPlot.clicked.connect(self.geoPlot)
        self.ui.tbtnMyProfile.clicked.connect(self.myProfile)


    def kb4root(self):
        myservice.main_window._signal_oper_clicked.emit("RootKnowledge", "Root KnowLedge Tree Edit ", "")

    def kb4my(self):
        myservice.main_window._signal_oper_clicked.emit("MyKnowledge", "My KnowLedge Tree Edit ", "")

    def upload(self):
        myservice.main_window._signal_oper_clicked.emit("UploadData", "Upload Data File", "")

    def processFile(self):
        myservice.main_window._signal_oper_clicked.emit("ProcessDataFile", "Process the Uploaded Data Files", "")

    def browseFile(self):
        myservice.main_window._signal_oper_clicked.emit("BrowseDataFile", "Process the Uploaded Data Files", "")

    def publicPaper(self):
        myservice.main_window._signal_oper_clicked.emit("SubmitPaper", "Submit paper or report to Public Files", "")

    def myPaper(self):
        myservice.main_window._signal_oper_clicked.emit("BrowsePaper", "Browse Paper or Reports in repository", "")

    def pdfOne(self):
        myservice.main_window._signal_oper_clicked.emit("Pdf One", "Process pdf files one by one ", "")

    def pdfBatch(self):
        myservice.main_window._signal_oper_clicked.emit("Pdf batch", "Process pdf files batch...", "")

    def publicData(self):
        myservice.main_window._signal_oper_clicked.emit("PublicData", "View the public data......", "")

    def myData(self):
        myservice.main_window._signal_oper_clicked.emit("MyData", "View the my private data......", "")

    def dataPlot(self):
        myservice.main_window._signal_oper_clicked.emit("DataPlot", "View and plot data......", "")

    def postGis(self):
        myservice.main_window._signal_oper_clicked.emit("PostGis", "working with postgis......", "")

    def geoPlot(self):
        myservice.main_window._signal_oper_clicked.emit("GeoPlot", "spacial analyse and plotting...", "")

    def myProfile(self):
        myservice.main_window._signal_oper_clicked.emit("MyProfile", "Edit the user profile......", "")

if __name__=='__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = OperWidget()
    appWin.show()

    sys.exit(app.exec_())
