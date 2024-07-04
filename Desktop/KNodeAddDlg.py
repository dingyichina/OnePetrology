'''
     添加KNode 知识体系结点

     author:  dingyi
     2021-12-19
'''


from PyQt5.QtWidgets import QDialog, QApplication,QStyleFactory,QMessageBox

import uuid

import myservice
from model.KnowledgeNode import KnowledgeNode, ValueType, KNodeType
from myservice import arango
from ui.ui_knode_widget import Ui_KNodeWidget

class AddKNodeDlg(QDialog):


    def __init__(self,knode, parent=None,isROOT=False):
        super(AddKNodeDlg, self).__init__(parent)
        self.ui = Ui_KNodeWidget()
        self.setupUi()
        self.setWindowTitle('Add KNode')
        self.ui.lblParentName.setText(knode.name)
        self.parentNode = knode
        self.parent = parent
        self.isROOT=isROOT

   #
    # def __init__(self,parentuuid,parentName, parent=None):
    #     super(AddKNodeDlg, self).__init__(parent)
    #     self.ui = Ui_KNodeWidget()
    #     self.setupUi()
    #     self.setWindowTitle('Add KNode')
    #     self.ui.lblParentName.setText(parentName)
    #     self.parentuuid=parentuuid
    #     self.parent=parent
    #     for k in KNodeType:
    #         self.ui.comboType.addItem(k)  # todo 可以加上图标
    #     for v in ValueType:
    #         self.ui.comboValueType.addItem(v)  # todo 可以加上图标 QIcon


    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.btnAdd.clicked.connect(self.addKNode)
        self.ui.btnCancel.clicked.connect(self.doClose)

    def addKNode(self):
        # 检查不能为空

        name = self.ui.txtName.text().strip()
        type = self.ui.comboType.currentText().strip()
        cnName = self.ui.txtCNName.text().strip()
        # 是否验重？ todo
        if name == "" or type == "":
            QMessageBox.critical(self, 'Error', 'The value can not be empty,please fill the text。\r\n', QMessageBox.Yes, QMessageBox.Yes)
            return
        kNode = KnowledgeNode()
        kNode.uuid = uuid.uuid4()
        kNode.name = name
        kNode.type = type
        kNode.cn_name = cnName
        kNode.desc = self.ui.txtDescription.toPlainText()
        kNode.expr = self.ui.txtExpression.toPlainText()
        kNode.value_type = self.ui.comboValueType.currentText()
        kNode.rel_entity = self.ui.txtRelateToEntity.text()
        kNode.order = self.ui.txtOrder.text()
        if self.isROOT:
            kNode.owner = "ROOT"  # 默认，等用户登录之后应该是用户自己的
        else:
            kNode.owner = myservice.username.upper()
        # todo  上述有逻辑判断关系，当为叶子结点时，才需要有valueType；当valueType为 枚举时，才需要关联对象  对象可以设置为下拉选择框

        # 保存方法，一直找Parent，找到根节点之后就可以save了。

        kNode.parent = self.parentNode.uuid

        arango.insertKNode(kNode)

        QMessageBox.information(self, 'Infomation', 'Add Success,please refresh the tree!\r\n', QMessageBox.Yes,
                             QMessageBox.Yes)

        self.destroy()
        pass

    def doClose(self):
        self.destroy()
        pass