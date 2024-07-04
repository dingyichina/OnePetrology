"""
    批量提取excel，从一个目录中

    author:dingyi
    2022-04-04
"""
from PyQt5.QtWidgets import QWidget

from ui.ui_pdf_batch_extract import Ui_PdfBatchProcess


class PdfBatchProcessWidget(QWidget):
    ui = Ui_PdfBatchProcess()

    def __init__(self,parent=None):
        super(PdfBatchProcessWidget, self).__init__(parent)
        self.setupUi()
        # 初始化


    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 初始化浏览器组件