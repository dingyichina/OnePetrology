# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_duplicate_checking.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DuplicateChecking(object):
    def setupUi(self, DuplicateChecking):
        DuplicateChecking.setObjectName("DuplicateChecking")
        DuplicateChecking.resize(1161, 585)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        DuplicateChecking.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DuplicateChecking)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(DuplicateChecking)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnChooseFile = QtWidgets.QPushButton(DuplicateChecking)
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
        self.label = QtWidgets.QLabel(DuplicateChecking)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboSheet = QtWidgets.QComboBox(DuplicateChecking)
        self.comboSheet.setMinimumSize(QtCore.QSize(160, 0))
        self.comboSheet.setObjectName("comboSheet")
        self.horizontalLayout.addWidget(self.comboSheet)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(DuplicateChecking)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinHeaderIndex = QtWidgets.QSpinBox(DuplicateChecking)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.spinHeaderIndex.setFont(font)
        self.spinHeaderIndex.setObjectName("spinHeaderIndex")
        self.horizontalLayout.addWidget(self.spinHeaderIndex)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnReload = QtWidgets.QPushButton(DuplicateChecking)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(DuplicateChecking)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 937, 155))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.widget_2 = QtWidgets.QWidget(DuplicateChecking)
        self.widget_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnDuplicateOnly = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnDuplicateOnly.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDuplicateOnly.setIcon(icon2)
        self.btnDuplicateOnly.setObjectName("btnDuplicateOnly")
        self.verticalLayout.addWidget(self.btnDuplicateOnly)
        self.btnNoDuplicateView = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnNoDuplicateView.setFont(font)
        self.btnNoDuplicateView.setIcon(icon2)
        self.btnNoDuplicateView.setObjectName("btnNoDuplicateView")
        self.verticalLayout.addWidget(self.btnNoDuplicateView)
        self.btnDuplicateCheck = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnDuplicateCheck.setFont(font)
        self.btnDuplicateCheck.setIcon(icon2)
        self.btnDuplicateCheck.setObjectName("btnDuplicateCheck")
        self.verticalLayout.addWidget(self.btnDuplicateCheck)
        self.btnSaveToExcel = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnSaveToExcel.setFont(font)
        self.btnSaveToExcel.setIcon(icon)
        self.btnSaveToExcel.setObjectName("btnSaveToExcel")
        self.verticalLayout.addWidget(self.btnSaveToExcel)
        spacerItem4 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.dockWidget = QtWidgets.QDockWidget(DuplicateChecking)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.verticalLayout_2.addWidget(self.dockWidget)
        self.verticalLayout_2.setStretch(3, 1)

        self.retranslateUi(DuplicateChecking)
        QtCore.QMetaObject.connectSlotsByName(DuplicateChecking)

    def retranslateUi(self, DuplicateChecking):
        _translate = QtCore.QCoreApplication.translate
        DuplicateChecking.setWindowTitle(_translate("DuplicateChecking", "Form"))
        self.label_3.setText(_translate("DuplicateChecking", "<html><head/><body><p>Tips:The data duplication check function can load Excel for duplication check, or check the query results in the public data and private data functions.</p><p>操作指南：数据查重功能可以加载excel进行查重，或者对public data和private data功能中的查询结果进行查重。</p></body></html>"))
        self.btnChooseFile.setText(_translate("DuplicateChecking", "Local file"))
        self.label.setText(_translate("DuplicateChecking", "Sheet List:"))
        self.label_2.setText(_translate("DuplicateChecking", "Header Index(Zero based):"))
        self.btnReload.setText(_translate("DuplicateChecking", "Reload"))
        self.groupBox.setTitle(_translate("DuplicateChecking", "Filter Fields:"))
        self.btnDuplicateOnly.setToolTip(_translate("DuplicateChecking", "only all duplcate view"))
        self.btnDuplicateOnly.setText(_translate("DuplicateChecking", "All Duplicate View"))
        self.btnNoDuplicateView.setToolTip(_translate("DuplicateChecking", "only distinct data ,without duplicate items"))
        self.btnNoDuplicateView.setText(_translate("DuplicateChecking", "Only No Duplicate"))
        self.btnDuplicateCheck.setToolTip(_translate("DuplicateChecking", "duplicate items only be truncated as one"))
        self.btnDuplicateCheck.setText(_translate("DuplicateChecking", "Duplicate keep first"))
        self.btnSaveToExcel.setText(_translate("DuplicateChecking", "Save to  Excel  file"))