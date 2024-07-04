'''
     添加KNode 知识体系结点

     author:  dingyi
     2021-12-19
'''


from PyQt5.QtWidgets import QDialog, QMessageBox
from myservice import arango
from ui.ui_knode_widget import Ui_KNodeWidget
class EditKNodeDlg(QDialog):

    def __init__(self, knode,parent=None):
        super(EditKNodeDlg, self).__init__(parent)
        self.ui = Ui_KNodeWidget()
        self.setupUi()
        self.setWindowTitle('Edit KNode')
        if hasattr(knode,"parent"):
            if knode.parent is not None:
                klist=arango.fetchKNodeByUUID(knode.parent)
                if  klist is None:
                    self.ui.lblParentName.setText('DDE-OnePetrology')
                else:
                    self.ui.lblParentName.setText(klist.name)


        self.knode = knode

        # 从对象往界面赋值
        self.updateUi()
        # self.ui.txtCNName.setText(knode.cn_name)
        # self.ui.comboType.setCurrentText(knode.type)

        self.ui.btnAdd.setText("Save")

    def updateUi(self):
        if hasattr(self.knode, "name"):
            self.ui.txtName.setText(self.knode.name)
        if hasattr(self.knode,"cn_name"):
            self.ui.txtCNName.setText(self.knode.cn_name)
        if hasattr(self.knode, "type"):
            self.ui.comboType.setCurrentText(self.knode.type)
        if hasattr(self.knode, "desc"):
            self.ui.txtDescription.setPlainText(self.knode.desc)
        if hasattr(self.knode, "expr"):
            self.ui.txtExpression.setPlainText(self.knode.expr)
        if hasattr(self.knode, "value_type"):
            self.ui.comboValueType.setCurrentText(self.knode.value_type)
        if hasattr(self.knode, "rel_entity"):
            self.ui.txtRelateToEntity.setText(self.knode.rel_entity)
        if hasattr(self.knode, "order"):
            self.ui.txtOrder.setText(self.knode.order)

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.btnAdd.clicked.connect(self.saveKNode)
        self.ui.btnCancel.clicked.connect(self.doClose)

    def saveKNode(self):
        name = self.ui.txtName.text().strip()
        type = self.ui.comboType.currentText().strip()
        cnName = self.ui.txtCNName.text().strip()
        # 是否验重？ todo
        if name == "" or type == "":
            QMessageBox.critical(self, 'Error', 'The value can not be empty,please fill the text。\r\n', QMessageBox.Yes,
                                 QMessageBox.Yes)
            return

        self.knode.name = name
        self.knode.type = type
        self.knode.cn_name = cnName
        self.knode.desc = self.ui.txtDescription.toPlainText()
        self.knode.expr = self.ui.txtExpression.toPlainText()
        self.knode.value_type = self.ui.comboValueType.currentText()
        self.knode.rel_entity = self.ui.txtRelateToEntity.text()
        self.knode.order = self.ui.txtOrder.text()
        self.knode.owner = "ROOT"  # 默认，等用户登录之后应该是用户自己的
        # todo  上述有逻辑判断关系，当为叶子结点时，才需要有valueType；当valueType为 枚举时，才需要关联对象  对象可以设置为下拉选择框

        # 更新该节点
        arango.updateKNode(self.knode)

        # 检查不能为空
        QMessageBox.information(self, 'Infomation', 'update Success,please refresh the tree!\r\n', QMessageBox.Yes,
                             QMessageBox.Yes)
        # self.parent.refreshTree()
        self.destroy()
        pass

    def doClose(self):
        self.destroy()
        pass