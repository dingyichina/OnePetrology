"""
    显示一个Dataframe，并允许编辑
    k_node被调用设置之前，必须已经填充好如下属性：
        1， deep_level ，即除了叶子节点之外的深度
        2, leaf_list,  所有叶子节点，即最后的带有表头信息的列表（已经按照order 排完序），每个叶子节点还有要给pth属性，是自己到entity根节点的路径（自下而上）
        3，df, 即 dataframe，用所有叶子节点按照顺序构成的所有的列的column


    作者：丁毅
    2022-01-27

"""
import os
import sys
import xlsxwriter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog

from model.KTableModel import KTableModel
from model.KnowledgeNode import KNodeType
from myservice import arango
from ui.ui_dfview import Ui_DfView


class DfViewWidget(QWidget):


    def __init__(self, parent=None):
        super(DfViewWidget, self).__init__(parent)
        self.ui = Ui_DfView()
        self.setWindowTitle('DataFrame View')
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # 设置右键菜单
        self.ui.tableView.addAction(self.ui.actionSave_Excel)

        self.ui.actionSave_Excel.triggered.connect(self.to_excel)

    # 设置进来的entity节点，必须首先被填充好df数据
    def setModel(self, k_node):
        model = KTableModel(k_node)
        self.ui.tableView.setModel(model)
        self.k_node = k_node
        # 调整表头，合并单元格
        self.merge_cell()

    def merge_cell(self):
        # 应用特点，只需要行或者列合并.
        # if self.k_node.type in {KNodeType.ENTITY.value, KNodeType.DIR.value}:  # 实体和目录 ，行合并
            for i in range(0, self.k_node.deep_level):
                colName = "Column{}".format(i)
                row = self.k_node.df_t.groupby(colName).groups
                for r in row:
                    v = row[r]
                    self.ui.tableView.setSpan(i, min(v), 1, max(v) - min(v) + 1)
        # elif self.k_node.type in {KNodeType.CLASSIFY.value}:  # 分类 ，行合并
        #     for i in range(0, self.k_node.deep_level):
        #         colName = self.k_node.df.columns[i]
        #         row = self.k_node.df.groupby(colName).groups
        #         for r in row:
        #             v = row[r]
        #             self.ui.tableView.setSpan( min(v), i, max(v) - min(v) + 1, 1)

    # 把结构写入Excel文件
    def to_excel(self):
        fileNames, fileType = QFileDialog.getSaveFileName(self, "Save to File", os.getcwd(),
                                                          "Excel Files(*.xlsx)")
        if fileNames is None or fileNames == "":
            return
        else:
            # 利用xlsxwriter 写入excel
            wb = xlsxwriter.Workbook(fileNames)
            sht = wb.add_worksheet(self.k_node.name)
            bold = wb.add_format({
                'bold': True,  # 字体加粗
                'border': 1,  # 单元格边框宽度
                'align': 'center',
                'valign': 'vcenter',  # 字体对齐方式
                'fg_color': '#F4B084',  # 单元格背景颜色
                'text_wrap': True,  # 是否自动换行
            })
            title=wb.add_format({
                'bold': True,  # 字体加粗
                'border': 1,  # 单元格边框宽度
                'align': 'center',
                'valign': 'vcenter',  # 字体对齐方式
                'fg_color': '#FFFF00',  # 单元格背景颜色
                'text_wrap': True,  # 是否自动换行
            })
            # 应用特点，只需要行合并。首先写入需要合并的
            for i in range(0, self.k_node.deep_level):
                colName = "Column{}".format(i)
                row = self.k_node.df_t.groupby(colName).groups
                for r in row:
                    v = row[r]
                    startIndex = min(v)
                    endIndex = max(v)
                    # sht.write(i,startIndex,r)
                    sht.merge_range(i,startIndex,i,endIndex,r,bold)
            # 接着写入具体字段
            for i in range(self.k_node.deep_level,self.k_node.deep_level+2):
                cols=len(self.k_node.df.columns)
                for j in range(0,cols):
                    sht.write(i,j,self.k_node.df.iloc[i,j],title)
            wb.close()

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = DfViewWidget()
    appWin.show()

    # 查找sample，然后把它设置进去
    k_node = arango.fetchKNodeByUUID('3ff8bfd3-fb43-49c9-9bff-b9276593dede')
    arango.getEntityDf(k_node)
    appWin.setModel(k_node)
    sys.exit(app.exec_())
