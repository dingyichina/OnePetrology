'''
    用户维护的是自己独有的知识树

    by：丁毅
    2022-02-12
'''
import json
import os
import sys
import uuid

import xlsxwriter
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog

import myservice
from model.KnowledgeNode import KnowledgeNode, KNodeType
from myservice import arango
from ui.ui_knowledgetree_my import Ui_KnowledgeTree4My
from pyecharts import options as opts
from pyecharts.charts import Tree


class TreeItem:

    def __init__(self):
        self.name = ""
        self.children = []
        pass

    def __repr__(self):
        if len(self.children) > 0:
            return (self.name, self.children)
        else:
            return (self.name)


class KnowledgeTree4My(QWidget):
    ui = Ui_KnowledgeTree4My()

    def __init__(self, parent=None):
        super(KnowledgeTree4My, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 添加browser
        self.browser = QWebEngineView()
        Url = 'http://www.baidu.com'
        self.browser.setUrl(QtCore.QUrl(Url))
        self.browser.settings().globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.browser.settings().globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.ui.stackedWidget_2.addWidget(self.browser)

        # 其它关联信号和槽的代码写在此处
        # 绑定信号和槽
        self.ui.btnPreview.clicked.connect(self.preview)
        self.ui.tbtnCopyRoot.clicked.connect(self.copyroot)
        self.ui.btnSaveExcel.clicked.connect(self.save2excel)

    # 从公用的知识树复制到本地来
    def copyroot(self):
        if QMessageBox.question(self, 'Question', 'Copy ROOT Knowledge Tree will override your customized result!\r\n'
                                                  'It will cost several minutes. \r\n\r\n Do you want to continue ?',
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes) == QMessageBox.No:
            return

        # 从root复制所有的知识树节点到当前用户下
        # 首先复制所有根节点，然后复制每个根节点下面的所有子节点
        # 显示等待对话框
        myservice.loading_mask.show()
        myservice.logger.info("Starting Check ROOT Knowledge...")
        knlist = arango.fetchAllKNodeByOwner("ROOT", "ROOT")  # 如果是自己添加的ROOT节点会怎样？ todo
        myservice.logger.info("ROOT Knowledge Tree has {} Nodes".format(knlist.__len__()))
        for knode in knlist:  # 循环检查每一个节点是否已存在，判断依据是名称和所有者
            myservice.logger.info("process node {} ".format(knode.name))
            rtnList = arango.fetchKNodeByNameAndOwner(knode.name, myservice.username.upper())
            if len(rtnList) == 0:
                # 此时需要添加
                myservice.logger.info("add new private node {} ".format(knode.name))
                newKnode = KnowledgeNode()
                # 挨个复制属性值
                newKnode.name = knode.name  # 这个肯定有，不会为空
                newKnode.uuid = uuid.uuid4()
                newKnode.parent = myservice.username.upper()  # 默认根节点是用户名
                newKnode.owner = myservice.username.upper()  # 默认所有者也是用户名的大写（为了好记，都用大写）
                if hasattr(knode, "cn_name"):
                    newKnode.cn_name = knode.cn_name
                if hasattr(knode, "desc"):
                    newKnode.desc = knode.desc
                if hasattr(knode, "type"):
                    newKnode.type = knode.type
                if hasattr(knode, "expr"):
                    newKnode.expr = knode.expr
                if hasattr(knode, "value_type"):
                    newKnode.value_type = knode.value_type
                if hasattr(knode, "rel_entity"):
                    newKnode.rel_entity = knode.rel_entity
                if hasattr(knode, "order"):
                    newKnode.order = knode.order
                # 插入到数据库
                arango.insertKNode(newKnode)
                myservice.logger.info("copy one ROOT Node from public")
                arango.copyChildren(knode.uuid, newKnode.uuid, myservice.username.upper(), update=True)  # 递归复制子节点
            else:
                # 此时已经存在该节点，则应该遍历该节点的子节点
                myservice.logger.info(
                    "{} has exists,root node don't need update,choose first to use ".format(knode.name))
                arango.copyChildren(knode.uuid, rtnList[0].uuid, myservice.username.upper(), update=True)  # 递归复制子节点，并更新

        # 完成之后关闭等待对话框
        myservice.loading_mask.hide()
        pass

    # 填充枚举数据
    def fillEnumData(self, k_node, rootNode):
        kn_list = arango.fetchChildrenKNodeByParent(k_node.uuid)
        for k in kn_list:
            obj = TreeItem()
            obj.name = k.name + "\r\n" + k.cn_name
            rootNode.children.append(obj)
            # 递归调用
            self.fillEnumData(k, obj)

    # 预览选中的知识结点
    def preview(self):

        k_node = self.ui.treeView.getCurKNode()
        if k_node is None:
            # 检查不能为空
            QMessageBox.information(self, 'Infomation', 'Select the Node first please !\r\n', QMessageBox.Yes,
                                    QMessageBox.Yes)
            return
        else:
            # 显示等待对话框
            myservice.loading_mask.show()

            if k_node.type == KNodeType.CLASSIFY.value:
                # 用pyecharts生成树状图，然后浏览

                # class TreeItem(
                #     # 树节点的名称，用来标识每一个节点。
                #     name: Optional[str] = None,
                #     # 节点的值，在 tooltip 中显示。
                #     value: Optional[Numeric] = None,
                #     # 该节点的样式
                #     label_opts: Optional[LabelOpts] = None,
                #     # 子节点，嵌套定义。
                #     children: Optional[Sequence] = None,
                # )
                data = []
                obj = TreeItem()
                obj.name = k_node.name + "\r\n" + k_node.cn_name
                # obj.value = k_node.cn_name

                data.append(obj)
                self.fillEnumData(k_node, obj)
                localfile = os.getcwd() + os.path.sep + "mypreview.html"

                c = (
                    Tree()
                    .add("", json.loads(
                        json.dumps(data, allow_nan=False, default=lambda o: o.__dict__, sort_keys=True, indent=4,
                                   ensure_ascii=False)))
                    .set_global_opts(title_opts=opts.TitleOpts(title=k_node.name))
                    .render(localfile)
                )

                self.browser.setUrl(QUrl.fromLocalFile(localfile))
                self.ui.stackedWidget_2.setCurrentWidget(self.browser)

            else:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.stackPage1)
                arango.getDf(k_node)
                self.ui.tableView.setModel(k_node)
            # 完成之后关闭等待对话框
            myservice.loading_mask.hide()

    # 保存为excel
    def save2excel(self):
        # 导出全部的知识结点作为excel文件存在，需要的时间比较长，首先进行询问
        if QMessageBox.question(self, 'Question', 'Do you want to export all the knowledge Tree ?  \r\nIt will '
                                                  'cost several minutes according your content...\r\n \r\n   Are '
                                                  'you sure to continue?', QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes) == QMessageBox.No:
            return
        try:
            self.to_excel()
        except Exception as e:
            myservice.logger.error(e)
            QMessageBox.warning(self, "Error", e)

    # 输出思维导图，目前默认输入的是excel文件的路径
    def save_to_xmind(self, k_node, filename):  # 同时创建中英文
        import xmind  # 加载包
        xmindfile = filename + "." + k_node.name + ".xmind"
        # 如果已存在，则删除，避免多次导入重复
        if os.path.exists(xmindfile):
            os.remove(xmindfile)

        w = xmind.load(xmindfile)  # 加载，如果不存在，创建新的工作布
        s1 = w.getPrimarySheet()  # 得到第一页
        s1.setTitle(k_node.name)  # 给第一页命名英文名字

        s2 = w.createSheet()  # 得到第二页
        s2.setTitle(k_node.cn_name)  # 第二页中文

        r1 = s1.getRootTopic()  # 创建根节点
        r1.setTitle(k_node.name)  # 给根节点命名

        r2 = s2.getRootTopic()  # 创建根节点
        r2.setTitle(k_node.cn_name)  # 给根节点命名

        self.fillxmind(k_node, r1, r2)
        xmind.save(w)  # 保存文件`

    # 填充思维导图
    def fillxmind(self, k_node, root_en, root_cn):
        kn_list = arango.fetchChildrenKNodeByParent(k_node.uuid)
        if len(kn_list) > 0:
            for kn in kn_list:
                en = root_en.addSubTopic()
                en.setTitle(kn.name)
                cn = root_cn.addSubTopic()
                cn.setTitle(kn.cn_name)
                # 递归填充
                self.fillxmind(kn, en, cn)

    # 把知识树写入Excel文件
    def to_excel(self):
        fileNames, fileType = QFileDialog.getSaveFileName(self, "Save to File", os.getcwd(),
                                                          "Excel Files(*.xlsx)")
        if fileNames is None or fileNames == "":
            return
        else:
            # 利用xlsxwriter 写入excel
            wb = xlsxwriter.Workbook(fileNames)
            knlist = arango.fetchAllKNodeByOwner(owner_uuid=myservice.username.upper(),
                                                 parent=myservice.username.upper())
            for k_node in knlist:
                # 枚举节点应该输出为思维导图
                if k_node.type == KNodeType.CLASSIFY.value:
                    self.save_to_xmind(k_node, fileNames)
                    continue  # 跳过填充excel的过程
                # ENTITY类型，填充当前知识结点
                arango.getDf(k_node)
                sht = wb.add_worksheet(k_node.name)
                bold = wb.add_format({
                    'bold': True,  # 字体加粗
                    'border': 1,  # 单元格边框宽度
                    'align': 'center',
                    'valign': 'vcenter',  # 字体对齐方式
                    'fg_color': '#F4B084',  # 单元格背景颜色
                    'text_wrap': True,  # 是否自动换行
                })
                title = wb.add_format({
                    'bold': True,  # 字体加粗
                    'border': 1,  # 单元格边框宽度
                    'align': 'center',
                    'valign': 'vcenter',  # 字体对齐方式
                    'fg_color': '#FFFF00',  # 单元格背景颜色
                    'text_wrap': True,  # 是否自动换行
                })
                # 应用特点，只需要行合并。首先写入需要合并的
                for i in range(0, k_node.deep_level):
                    colName = "Column{}".format(i)
                    row = k_node.df_t.groupby(colName).groups
                    for r in row:
                        v = row[r]
                        startIndex = min(v)
                        endIndex = max(v)
                        # sht.write(i,startIndex,r)
                        sht.merge_range(i, startIndex, i, endIndex, r, bold)
                # 接着写入具体字段
                for i in range(k_node.deep_level, k_node.deep_level + 2):
                    cols = len(k_node.df.columns)
                    for j in range(0, cols):
                        sht.write(i, j, k_node.df.iloc[i, j], title)
            wb.close()
            QMessageBox.information(self, 'Infomation', 'Knowledge Tree export has done !\r\n', QMessageBox.Yes,
                                    QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = KnowledgeTree4My()
    appWin.show()

    sys.exit(app.exec_())