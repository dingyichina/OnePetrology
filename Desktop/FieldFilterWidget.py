'''

    字段过滤组件，用于设置字段过滤条件

    外层容器是一个layout

    --- dingyi  20231201
'''
from PyQt5.QtCore import pyqtSignal, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit

from ui.ui_field_fiter import Ui_FieldFilterForm


class FieldFilterWidget(QWidget):


    def __init__(self,parent=None,columns_list=[],numbercolumns_list=[], ):
        super(FieldFilterWidget, self).__init__(parent)
        self.columns_list = columns_list
        self.numbercolumns_list = numbercolumns_list
        self.ui = Ui_FieldFilterForm()
        self.setupUi()
        # 默认不显示delete
        self.ui.btnRemove.setVisible(False)

        pass

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 初始化字段下拉列表
        for f in self.columns_list:
            self.ui.comboField.addItem(f,f)
        # 连接信号和槽
        self.ui.comboField.currentIndexChanged.connect(self.switchOper)
        self.ui.btnAdd.clicked.connect(self.addNew)
        self.ui.btnRemove.clicked.connect(self.removeOne)

        #  可能触发的改变事件
        self.ui.comboField.currentIndexChanged.connect(self.fitlerChangedEvent)
        self.ui.comboOp.currentIndexChanged.connect(self.fitlerChangedEvent)
        self.ui.ldtValue.textChanged.connect(self.fitlerChangedEvent)
        self.ui.comboJoin.currentIndexChanged.connect(self.fitlerChangedEvent)

    # 父窗口触发事件
    def fitlerChangedEvent(self):
        if hasattr(self,"ptr2queryfilter"):
            self.ptr2queryfilter.calcfilter()

    # 根据字段列表切换操作符下拉列表
    def switchOper(self):
        # 得到当前选择
        current_field = self.ui.comboField.currentText()
        # print("当前字段" ,current_field,self.numbercolumns_list)
        self.ui.comboOp.clear()

        if current_field in self.numbercolumns_list:  # 如果是数字
            self.ui.comboOp.addItems(["=",">",">=","<","<="])
            # 此时设定只能输入数字
            reg_ex_1 = QRegExp("[0-9]+.?[0-9]{,10}")  # double
            # reg_ex_2 = QRegExp("[0-9]{1,5}")  # minimum 1 integer number to maxiumu 5 integer number
            # reg_ex_3 = QRegExp("-?\\d{1,3}")  # accept negative number also
            # reg_ex_4 = QRegExp("")
            self.oldvalidator = self.ui.ldtValue.validator()
            self.ui.ldtValue.setValidator(QRegExpValidator(reg_ex_1))
        else:
            self.ui.comboOp.addItems(["contains","=="])   # 这两个需要转译
            if hasattr(self,"oldvalidator") :
                self.ui.ldtValue.setValidator(self.oldvalidator)  # 此时不限制

    # 添加一个新的
    def addNew(self):
        newItem = FieldFilterWidget(self.parent(),self.columns_list,self.numbercolumns_list)
        newItem.ui.btnRemove.setVisible(True)
        # 添加到父容器
        # print(self.parent(), self.parent().layout())
        self.parent().layout().addWidget(newItem)
        if hasattr(self, "ptr2queryfilter"):
            newItem.ptr2queryfilter=self.ptr2queryfilter  #  传递指针


    def removeOne(self):
        # 判断是否最后一个
        self.parent().layout().removeWidget(self)
        self.fitlerChangedEvent()

    def setColumns(self,columns_list,numbercolumns_list):
        self.columns_list = columns_list
        self.numbercolumns_list = numbercolumns_list
        # 刷新
        self.ui.comboField.clear()
        # 初始化字段下拉列表
        for f in self.columns_list:
            self.ui.comboField.addItem(f, f)

    def getFilter(self):
        if self.ui.ldtValue.text().strip() == "":
            #self.ui.ldtValue.focusWidget()
            #QMessageBox.information(self, 'Information', "Please input the value ",  QMessageBox.Yes)
            return ""
        # 得到中间的选项名称
        if self.ui.comboOp.currentText()==-1 :
            #self.ui.comboOp.focusWidget()
            #QMessageBox.information(self, 'Information', "Please select the operator ", QMessageBox.Yes)
            return ""
        if self.ui.comboOp.currentText() =="contains": # 只有包含需要特殊处理，其它的直接引用操作符
            return ' c.`{}` like "%{}%" '.format(self.ui.comboField.currentText(),self.ui.ldtValue.text())+ " "+self.ui.comboJoin.currentText()
        elif self.ui.comboOp.currentText() =="==":
            return ' c.`{}` =="{}" '.format(self.ui.comboField.currentText(),
                                                  self.ui.ldtValue.text()) + " " + self.ui.comboJoin.currentText()
        else:
            return ' c.`{}` {}{}  '.format(self.ui.comboField.currentText(),self.ui.comboOp.currentText(),
                                           self.ui.ldtValue.text()) + " " + self.ui.comboJoin.currentText()

