"""
    显示所有的公共数据

    author ：丁毅
    2022-04-04

"""
import sys
import time

import pandas as pd
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog

import myservice
from SelectConditionDlg import SelectConditionDlg
from pandasgui.store import PandasGuiDataFrameStore
from pandasgui.widgets.dataframe_explorer import DataFrameExplorer
from ui.ui_public_data import Ui_PublicData


class PublicDataWidget(QWidget):
    ui = Ui_PublicData()

    def __init__(self,parent=None):
        super(PublicDataWidget, self).__init__(parent)
        self.setupUi()
        # 初始化combolist
        self.doRefresh()


    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 连接信号与函数
        self.ui.btnRefresh.clicked.connect(self.doRefresh)
        self.ui.btnFetch.clicked.connect(self.doFetchData)
        self.ui.combDf.currentIndexChanged.connect(self.comboDfChanged)
        self.ui.btnDuplicateCheck.clicked.connect(self.doDuplicateCheck)
        self.ui.btnClear.clicked.connect(self.doClear)
        # 清除数据库中的数据，该操作要慎重，询问三遍
        self.ui.queryFilterWidget.ui.btnCondition.clicked.connect(
            self.doCondtionFilter)  # 这个由于需要参数，所以在这里设置，有点不太好看，***todo***
    def doCondtionFilter(self):
        self.map = SelectConditionDlg(self.ui.comboEntity.currentText(),myservice.username,self)
        print("doCondtionFilter")
        if self.map.exec() == QDialog.Accepted:
            print(self.map.condition)
            self.ui.queryFilterWidget.ui.txtCondition.setText(self.map.condition)
        pass

    def doClear(self):
        kname = self.ui.comboEntity.itemData(self.ui.comboEntity.currentIndex()).name
        for i in range(3):
            if QMessageBox.question(self, 'Question', 'Do you want to clear your public data of ' + kname + ' ?  \r\nIt will '
                                                                                                     'be deleted and can not be retored...\r\n \r\n   Are '
                                                                                                     'you sure to continue?',
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.Yes) == QMessageBox.No:
                return
        # 执行删除，代码暂缺 todo
        sample = {"owner": myservice.username.upper(), "scope": "public"}
        myservice.arango.delete(kname, sample)
        QMessageBox.information(self, "Tips", "Clear public data succeed!")

    def doDuplicateCheck(self):
        # 执行查重
        myservice.main_window._signal_oper_clicked.emit("Duplicate Checking",
                                                        "Check the data and find the duplicate......",
                                                        self.ui.combDf.currentData())


    def comboDfChanged(self):
        if self.ui.combDf.currentData() is None:
            self.ui.btnDuplicateCheck.setEnabled(False)
        else:
            self.ui.btnDuplicateCheck.setEnabled(True)

    def doRefresh(self):
        self.ui.comboEntity.clear()
        # 初始化combolist
        kn_list = myservice.arango.fetchAllEntity()
        for k_node in kn_list:
            self.ui.comboEntity.addItem(k_node.name,k_node)

    # 从界面上获取各个要素，拼装成aql
    def buildAQL(self):
        k_name = self.ui.comboEntity.currentText()
        condition = self.ui.queryFilterWidget.ui.txtCondition.toPlainText()
        polygon = self.ui.queryFilterWidget.ui.txtPolygon.toPlainText()
        # 如何判断polygon 是否是逆时针， 现在新版必须是逆时针才可以正常查询。  todo ****
        totalaql = " for c in {}  filter  c.scope =='{}'  ".format(k_name, 'public')  # 用来查询当前条件下的所有的条数
        if self.ui.chkOnlyMy.isChecked(): # 如果只看自己
            totalaql = totalaql + " && c.owner =='{}' ".format(myservice.username.upper())

        if polygon is None or polygon.strip(' ') == '':
            print("输入空间条件为空，不进行空间检索")
        else:
            # 根据传入的坐标点拼装查询条件
            # 例子数据 (96.328125,48.748945),(91.318359,43.644026),(102.568359,36.173357),(110.742188,43.261206),(102.392578,43.197167),(105.205078,47.457809),(96.328125,48.748945)
            points = polygon.replace('(', '[').replace(')', ']')  # 把小括号转为中括号，以适配AQL语法
            spatial_filter = " FILTER c.Longitude <=180 && c.Longitude >=-180 && c.Latitude <=90 && c.Latitude >=-90  &&  GEO_CONTAINS(GEO_POLYGON([{}]),[c.Longitude,c.Latitude]) ".format(
                points)  # 前部分的条件是为了过滤掉不合法的经纬度
            print(spatial_filter)
            totalaql = totalaql + spatial_filter  # 作为条件拼装在后面 ，多个filter属于and与的关系
        if condition is None or condition.strip(' ') == '':
            print("字段过滤为空，不进行条件判断")
        else:
            # 对传入的条件进行校对和 拼装
            condition_filter = " FILTER {}".format(condition)
            totalaql = totalaql + condition_filter
            # 拼装最后的return c
        totalaql = totalaql + " return c"
        print("拼装aql：", totalaql)
        return totalaql
        pass
    def doFetchData(self):
        # 根据查询参数从数据库中查询数据
        # 从arango中获取数据，拼装为df，然后显示到界面上
        k_node = self.ui.comboEntity.itemData(self.ui.comboEntity.currentIndex())
        self.k_node = k_node
        # 拼装查询条件，字典

        aql = self.buildAQL()

        self.thread = WorkerThread(k_node,aql)
        self.thread.finishSignal.connect(self.doFinishExtract)
        if hasattr(myservice,"main_window"):
            self.thread.statusSignal.connect(myservice.main_window.workerStatus)
        if hasattr(myservice,"loading_mask"):
            self.thread.finishSignal.connect(myservice.loading_mask.hide)
            myservice.loading_mask.show()


        self.thread.start()

    def doFinishExtract(self,msg):

        tab_name = self.k_node.name+":"+time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime(time.time()))
        # 先添加到下拉列表框，供查重使用
        self.ui.combDf.addItem(tab_name, self.thread.df)

        pgdfs = PandasGuiDataFrameStore(self.thread.df, tab_name)
        pgdfs.k_node = self.k_node #  把知识树带进去备用
        dfe = DataFrameExplorer(pgdfs)
        self.ui.tabWidget.addTab(dfe, tab_name)

        pass

class  WorkerThread(QThread):

    finishSignal = QtCore.pyqtSignal(str)  # 完成信号
    statusSignal = QtCore.pyqtSignal(str)  # 注册过程状态信号
    def __init__(self,k_node,aql,parent=None):
        super(WorkerThread, self).__init__(parent)
        self.k_node = k_node
        self.aql = aql
        pass
    # 处理提交到db的操作
    def run(self):
        self.statusSignal.emit("Query Public Start:"+self.k_node.name)
        myservice.logger.info("Query Public Start:"+self.k_node.name)
        try:
            # col = myservice.arango.getCollection(self.k_node.name)
            doc_list = myservice.arango.getByAQL(self.aql)
            self.df = pd.DataFrame(doc_list)
            # 去除掉arangodb 的默认列，不在ui上显示，公共的默认不需要显示scope
            self.df.drop(columns=["_id", "_rev", "owner"], axis="columns", inplace=True)
            self.df.set_index("_key",inplace=True)   # 把key当作index
            # 此时还需要按照知识树的顺序对列进行排序  todo ******重要*********
            myservice.arango.getDf(self.k_node)
            ktreeColumns = []
            # 接着写入具体字段
            for i in range(self.k_node.deep_level + 1, self.k_node.deep_level + 2):
                cols = len(self.k_node.df.columns)
                for j in range(0, cols):
                    if self.k_node.df.iloc[i, j] not in ktreeColumns:
                        ktreeColumns.append(self.k_node.df.iloc[i, j])
            # print("知识树的顺序:",ktreeColumns)
            # 对self.df按照知识树顺序对列顺序进行排序
            dbColumns = self.df.columns
            # 首先把知识树中不存在的列添加最后
            for col in dbColumns:
                if col in ktreeColumns:
                    continue
                else:
                    ktreeColumns.append(col)
            # 然后移除掉知识树列 不在df中存在的
            temp = ktreeColumns.copy()  # 复制一个用于循环，否则remove之后会导致指针错位导致问题
            for col in temp:
                if col not in dbColumns:
                    ktreeColumns.remove(col)
            # print("df columns",self.df.columns)
            # print("调整后的顺序",ktreeColumns)
            self.df = self.df[ktreeColumns]
            # 按照知识树列排序结束

            self.statusSignal.emit("Query Public Finished:" + self.k_node.name)
            myservice.logger.info("Query Public Finished:" + self.k_node.name)
            self.finishSignal.emit("Query Public Finished:" + self.k_node.name)
        except Exception as ex:
            import traceback
            msg = traceback.format_exc()
            myservice.logger.error(msg)
            self.statusSignal.emit("Error :" + msg)
            self.finishSignal.emit("Error :" + msg)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create and show widget
    dfe = PublicDataWidget()
    dfe.show()

    sys.exit(app.exec_())
