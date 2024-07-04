'''
     查询条件组件，用于组合空间查询和条件查询的组件

     ----   dingyi
     20231201
'''
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog

import myservice
from FieldFilterWidget import FieldFilterWidget
from SelectFromMapDlg import SelectFromMapDlg
from model.KnowledgeNode import ValueType
from ui.ui_query_filter import Ui_QueryFilterForm


class QueryFilterWidget(QWidget):


    def __init__(self, k_node_name, parent=None):
        super(QueryFilterWidget, self).__init__(parent)
        self.k_node = k_node_name
        self.ui = Ui_QueryFilterForm()
        self.setupUi()

        pass

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 初始化字段下拉列表
        # 连接信号和槽
        self.ui.btnMap.clicked.connect(self.select_from_map)
        self.ui.btnClearPolygon.clicked.connect(self.clearPolygon)
        self.ui.btnClearCondition.clicked.connect(self.clearCondition)
    def clearCondition(self):
        self.ui.txtCondition.setText("")
    def clearPolygon(self):
        self.ui.txtPolygon.setText("")
    def select_from_map(self):
        self.map = SelectFromMapDlg(self)
        if self.map.exec() == QDialog.Accepted:
            print(self.map.polygon)
            self.ui.txtPolygon.setText(self.map.polygon)
        pass
    # 设置知识树节点，根据这个节点去查询所有的字段
    def set_k_node(self,k_node_name):
        # 结合当前登录用户的名称去查询
        result =  myservice.getleaflist(k_node_name,myservice.username)  #
        self.columns_list=[]
        self.numbercolumns_list=[]
        for r in result:
            self.columns_list.append(r.name)
            if r.value_type == ValueType.FLOAT.value:
                self.numbercolumns_list.append(r.name)

        # 用这个去刷所有的字段列表
        # 遍历所有的字段列表widget
        wl = self.ui.scrollAreaWidgetContents.children()
        for w in wl:
           if isinstance(w, FieldFilterWidget):
             w.setColumns(self.columns_list,self.numbercolumns_list)
             w.ptr2queryfilter = self
    # 得到拼装好的条件
    def get_field_filter(self):
        wl = self.ui.scrollAreaWidgetContents.children()
        filter =""
        for w in wl:
            if isinstance(w, FieldFilterWidget):
               filter = filter+w.getFilter()
        # 需要把最后一个join条件切掉
        # print("filter:",filter)
        if filter.strip()=="":
            return filter  # 此时没有设置，则直接返回
        filter = filter[:filter.strip().rfind(" ")]
        return filter

    def calcfilter(self):
        self.ui.txtFilter.setText(self.get_field_filter())
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = QueryFilterWidget("Igneous_Rock")
    dfe.set_k_node("Igneous_Rock")
    dfe.show()

    sys.exit(app.exec_())




