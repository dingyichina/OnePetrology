# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_select_from_map_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgMap(object):
    def setupUi(self, dlgMap):
        dlgMap.setObjectName("dlgMap")
        dlgMap.resize(1098, 762)
        dlgMap.setSizeGripEnabled(True)
        dlgMap.setModal(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dlgMap)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mapWidget = QtWebEngineWidgets.QWebEngineView(dlgMap)
        self.mapWidget.setObjectName("mapWidget")
        self.verticalLayout.addWidget(self.mapWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnOk = QtWidgets.QPushButton(dlgMap)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(dlgMap)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(dlgMap)
        QtCore.QMetaObject.connectSlotsByName(dlgMap)

    def retranslateUi(self, dlgMap):
        _translate = QtCore.QCoreApplication.translate
        dlgMap.setWindowTitle(_translate("dlgMap", "Select from Map"))
        self.btnOk.setText(_translate("dlgMap", "OK "))
        self.btnCancel.setText(_translate("dlgMap", "Cancel"))
from PyQt5 import QtWebEngineWidgets
