# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_excel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExcelProcess(object):
    def setupUi(self, ExcelProcess):
        ExcelProcess.setObjectName("ExcelProcess")
        ExcelProcess.resize(1234, 604)
        ExcelProcess.setStyleSheet("\n"
"\n"
"/*===================================== Tab =================================*/\n"
"QTabWidget#tabWidget{\n"
"    background:transparent;\n"
"}\n"
"QTabWidget::pane{\n"
"    border-top: 1px solid;\n"
"    border-color: transparent;\n"
"    top:-1px;\n"
"}\n"
"QTabBar::tab {\n"
"    min-width:85px;\n"
"    min-height:16px;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #e2e2e2; \n"
"    font:10px \"Microsoft YaHei\" ;\n"
"}\n"
"QTabBar::tab:selected{\n"
"    min-width:85px;\n"
"    min-height:18px;\n"
"    color: #000;\n"
"    border: 0px solid;\n"
"    background:#00fffb;\n"
"    font:12px \"Microsoft YaHei\" ;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ExcelProcess)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(ExcelProcess)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 25 12pt \"Microsoft YaHei\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnChooseFile = QtWidgets.QPushButton(ExcelProcess)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.btnChooseFile.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnChooseFile.setIcon(icon)
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.horizontalLayout.addWidget(self.btnChooseFile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(ExcelProcess)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 25 12pt \"Microsoft YaHei\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboSheet = QtWidgets.QComboBox(ExcelProcess)
        self.comboSheet.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.comboSheet.setFont(font)
        self.comboSheet.setObjectName("comboSheet")
        self.horizontalLayout.addWidget(self.comboSheet)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(ExcelProcess)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 25 12pt \"Microsoft YaHei\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinHeaderIndex = QtWidgets.QSpinBox(ExcelProcess)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.spinHeaderIndex.setFont(font)
        self.spinHeaderIndex.setObjectName("spinHeaderIndex")
        self.horizontalLayout.addWidget(self.spinHeaderIndex)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnReload = QtWidgets.QPushButton(ExcelProcess)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.btnReload.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon1)
        self.btnReload.setObjectName("btnReload")
        self.horizontalLayout.addWidget(self.btnReload)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(ExcelProcess)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(ExcelProcess)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ExcelProcess)

    def retranslateUi(self, ExcelProcess):
        _translate = QtCore.QCoreApplication.translate
        ExcelProcess.setWindowTitle(_translate("ExcelProcess", "Form"))
        self.label_3.setText(_translate("ExcelProcess", "<html><head/><body><p>Tips:  please double click left tree node to choose excel file. another way is to choose local excel file from disk. And then click reload to read excel.</p><p>操作指南：可以双击左侧的资源库中的excel文件，也可以从本地选择。然后点击Reload按钮去读取数据。</p></body></html>"))
        self.btnChooseFile.setText(_translate("ExcelProcess", "Local file"))
        self.label.setText(_translate("ExcelProcess", "Sheet List:"))
        self.label_2.setText(_translate("ExcelProcess", "Header Index(Zero based):"))
        self.btnReload.setText(_translate("ExcelProcess", "Reload"))