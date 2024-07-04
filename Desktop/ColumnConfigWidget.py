'''
    在进行plot操作时，每列的转换设置参数

    目前主要是None值处理方式

    构造函数输入的数据有要求，比如包含:
       name,desc,type
    默认的空值处理方式为丢弃 drop only

    author :dingyi
    2022-08-19

'''
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from ui.ui_column_config import Ui_ColumnConfig


# 描述一个目标列的对象
class ColumnObj:

    def __init__(self, name, desc, type, use_default, default_value):
        self.name = name
        self.desc = desc
        self.type = type
        self.use_default = use_default
        self.default_value = default_value
        self.dfColumn = None
        pass


# 单行目标列的widget
class ColumnConfigWidget(QWidget):

    def __init__(self, columnobj, parent=None):
        self.ui = Ui_ColumnConfig()
        super(ColumnConfigWidget, self).__init__(parent)
        self.setupUi()
        # 初始化
        self.ui.lblName.setText(columnobj.name)
        self.ui.lblDesc.setText(columnobj.desc)
        self.ui.lblType.setText(columnobj.type)
        self.columnObj = columnobj
        self.ui.ldtDefault.setText(columnobj.default_value)
        if columnobj.use_default:
            self.ui.chkDefault.setChecked(True)
            self.ui.ldtDefault.setVisible(True)

        else:
            self.ui.chkDefault.setChecked(False)
            self.ui.ldtDefault.setVisible(False)

        self.ui.chkDefault.toggled['bool'].connect(self.doChkDefault)
        # 默认隐藏最后一个填充值，因为默认的空值选项是丢弃
        self.ui.ldtNullValue.setVisible(False)

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 设置处理函数
        self.ui.comboNullProcess.currentIndexChanged.connect(self.doComboNull)

    def doComboNull(self, index):
        if index == 0:
            self.ui.ldtNullValue.setVisible(False)
        else:
            self.ui.ldtNullValue.setVisible(True)
            self.ui.ldtNullValue.setFocus()

    def doChkDefault(self, checked):
        if checked:
            self.ui.ldtDefault.setFocus()

    def getColumnObj(self):
        self.columnObj.use_default = self.ui.chkDefault.isChecked()
        if self.ui.chkDefault.isChecked():
            if self.columnObj.type.lower() == "float":
                self.columnObj.default_value = float(self.ui.ldtDefault.text())
            else:
                self.columnObj.default_value = self.ui.ldtDefault.text()
        if self.ui.comboNullProcess.currentIndex() == 1 :
            self.columnObj.fill_null = True
            if self.columnObj.type.lower() == "float":
                self.columnObj.null_value = float(self.ui.ldtNullValue.text())
            else:
                self.columnObj.null_value = self.ui.ldtNullValue.text()
        else:
            self.columnObj.fill_null = False
        return self.columnObj





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    data ={"Name": "Label", "Desc": "点的标签值", "Type": "String","UseDefault":False,"DefaultValue":"O"}
    colobj = ColumnObj(data["Name"], data["Desc"], data["Type"], data["UseDefault"], data["DefaultValue"])
    dfe = ColumnConfigWidget(colobj)
    dfe.show()

    sys.exit(app.exec_())
