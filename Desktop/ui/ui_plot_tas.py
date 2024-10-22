# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plot_tas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TASPlot(object):
    def setupUi(self, TASPlot):
        TASPlot.setObjectName("TASPlot")
        TASPlot.resize(1199, 704)
        font = QtGui.QFont()
        font.setPointSize(12)
        TASPlot.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(TASPlot)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(TASPlot)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnChooseFile = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.btnChooseFile.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnChooseFile.setIcon(icon)
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.horizontalLayout.addWidget(self.btnChooseFile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 25 14pt \"Microsoft YaHei\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboSheet = QtWidgets.QComboBox(self.groupBox)
        self.comboSheet.setMinimumSize(QtCore.QSize(150, 0))
        self.comboSheet.setStyleSheet("font: 25 14pt \"Microsoft YaHei\";")
        self.comboSheet.setObjectName("comboSheet")
        self.horizontalLayout.addWidget(self.comboSheet)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 25 14pt \"Microsoft YaHei\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinHeaderIndex = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.spinHeaderIndex.setFont(font)
        self.spinHeaderIndex.setStyleSheet("font: 25 14pt \"Microsoft YaHei\";")
        self.spinHeaderIndex.setObjectName("spinHeaderIndex")
        self.horizontalLayout.addWidget(self.spinHeaderIndex)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnReload = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.btnReload.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon1)
        self.btnReload.setObjectName("btnReload")
        self.horizontalLayout.addWidget(self.btnReload)
        spacerItem3 = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btnPlot = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.btnPlot.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/数据查询.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlot.setIcon(icon2)
        self.btnPlot.setObjectName("btnPlot")
        self.horizontalLayout.addWidget(self.btnPlot)
        spacerItem4 = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.groupBox)
        self.scrollArea = QtWidgets.QScrollArea(TASPlot)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1179, 625))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(TASPlot)
        QtCore.QMetaObject.connectSlotsByName(TASPlot)

    def retranslateUi(self, TASPlot):
        _translate = QtCore.QCoreApplication.translate
        TASPlot.setWindowTitle(_translate("TASPlot", "Form"))
        self.btnChooseFile.setText(_translate("TASPlot", "Local file"))
        self.label.setText(_translate("TASPlot", "Sheet List:"))
        self.label_2.setText(_translate("TASPlot", "Header Index(Zero based):"))
        self.btnReload.setText(_translate("TASPlot", "Reload"))
        self.btnPlot.setText(_translate("TASPlot", "Plot"))
