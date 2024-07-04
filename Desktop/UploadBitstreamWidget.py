
'''
    实现附件上传功能的widget
    by：dingyi
'''

import os
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import  Qt,pyqtSignal

import myservice
import util
from TableUploadWidget import TableUploadWidget
from ui.ui_UploadBitstream import Ui_UploadBitstream
from myservice import client

class UploadBitstreamWidget(QWidget):
    collectionId = "a6c00453-2942-460a-ae2f-52d601a501bf"  # excel集合的UUID，目前写死了，回头在调整  todo

    ui=Ui_UploadBitstream()

    signal_table_delete = pyqtSignal(str)  # 从文件列表中删除，参数是文件全路径（包括文件名）
    signal_upload = pyqtSignal(str)  # 开始上传，参数是self.bundleId


    def __init__(self, parent=None):
        super(UploadBitstreamWidget, self).__init__(parent)
        self.setupUi()


    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        #设置表格模型
        self.model = QStandardItemModel()
        self.model.setColumnCount(5)
        # 设置表头信息
        self.model.setHorizontalHeaderLabels(['文件名', '文件类型', '全路径', '文件大小', ' 操 作'])
        self.ui.tableFileList.setModel(self.model)
        self.ui.tableFileList.setColumnWidth(0,220)
        self.ui.tableFileList.setColumnWidth(1, 80)
        self.ui.tableFileList.setColumnWidth(2, 520)
        self.ui.tableFileList.setColumnWidth(3, 80)
        self.ui.tableFileList.setColumnWidth(4, 400)

        #关联信号和槽
        # self.parent().signal_tree_double_clicked.connect(self.treeDoublieClicked)  #初始化时只需要一个parent即可关联到主窗口，因为该对象是在mainwindow的构造函数里实例化的
        self.signal_table_delete.connect(self.deleteOne)
        self.ui.btnAddFiles.clicked.connect(self.chooseFiles)
        self.ui.btnClear.clicked.connect(self.clearTable)
        self.ui.btnStartUpload.clicked.connect(self.doUpload)

    def doUpload(self):
        # 首先判断是否已经有buddleId属性，如果没有，则需要创建

        # 根据填充的结果生成item和item下面的bundle，然后往bundle下面传附件
        # 检查title是否已填写
        if self.ui.txtTitle.text()=="":
            QMessageBox.information(self, 'Tips', 'Please fill title first.', QMessageBox.Yes, QMessageBox.Yes)
            return
        # 拼装meta元数据
        data = {
            "name": self.ui.txtTitle.text(),
            "metadata": {  # 必须把该集合所需要的必填项的所有元数据都填进去，  todo：
                "dc.contributor.author": [
                    {
                        "value": myservice.username,
                        "language": "Zh_CN",
                        "authority": "null",
                        "confidence": -1
                    }
                ],
                "dc.subject": [
                    {
                        "value": self.ui.txtKeyWords.text(),
                        "language": "zh_CN",
                        "authority": 'null',
                        "confidence": -1
                    }
                ],
                "dc.source": [
                    {
                        "value": self.ui.txtSource.text(),
                        "language": "zh_CN",
                        "authority": 'null',
                        "confidence": -1
                    }
                ],
                "dc.coverage.spatial": [
                    {
                        "value": self.ui.txtSpatialInfo.text(),
                        "language": "zh_CN",
                        "authority": 'null',
                        "confidence": -1
                    }
                ],
                "dc.title": [
                    {
                        "value": self.ui.txtTitle.text(),
                        "language": "zh_CN",
                        "authority": 'null',
                        "confidence": -1
                    }
                ],
                "dc.rights": [
                    {
                        "value": "Upload",
                        "language": "zh_CN",
                        "authority": 'null',
                        "confidence": -1
                    }
                ],
                "dspace.entity.type": [
                    {
                        "value": 'Publication',
                        "language": "zh_CN",
                        "authority": 'null',
                        "confidence": -1
                    }
                ]
            },
            "inArchive": "true",
            "discoverable": "true",
            "withdrawn": "false",
            "type": "item"
        }
        newItem = myservice.client.createItemWithJson(self.collectionId,data)
        newBundle = myservice.client.createBundle(newItem.uuid,"ORIGINAL")

        self.signal_upload.emit(newBundle.uuid)

    # 从table中删除一个指定的选项
    def deleteOne(self,file):
        selected=self.model.findItems(file, Qt.MatchExactly | Qt.MatchRecursive, column=2)
        for item in selected:
            self.model.removeRow(self.model.indexFromItem(item).row())

    def clearTable(self):
        self.model.clear()
        self.model.setColumnCount(5);
        self.ui.txtTitle.setText("")
        self.ui.txtSource.setText("")
        self.ui.txtKeyWords.setText("")
        self.ui.txtSpatialInfo.setText("")
        # 设置表头信息
        self.model.setHorizontalHeaderLabels(['文件名', '文件类型', '全路径', '文件大小', ' 操 作'])
        self.ui.tableFileList.setColumnWidth(0, 220)
        self.ui.tableFileList.setColumnWidth(1, 80)
        self.ui.tableFileList.setColumnWidth(2, 520)
        self.ui.tableFileList.setColumnWidth(3, 80)
        self.ui.tableFileList.setColumnWidth(4, 400)
        self.ui.btnStartUpload.setEnabled(False)
        self.ui.btnClear.setEnabled(False)

    def treeDoublieClicked(self,uuid,type):
        #判断type是否时bundle，只有bundle才可以开始上传附件
        if(type=='bundle'):
            self.ui.btnAddFiles.setEnabled(True)  #允许添加
            self.ui.btnStartUpload.setEnabled(True)  #允许上传
            # 根据uuid查找到bundle对象
            self.bundleuuid=uuid
            bundle=client.getBundle(uuid)
            item=client.getItemByUrl(bundle.getItemLink())
            self.ui.lblBundleName.setText(bundle.name);
            self.ui.lblItemName.setText(item.name);
            # 关联到指定科学家的代码暂空  todo：

            pass

        else:
            self.ui.btnAddFiles.setEnabled(False)
            self.ui.btnStartUpload.setEnabled(False)
            self.ui.lblBundleName.setText('');
            self.ui.lblItemName.setText('');
            pass

    def chooseFiles(self):
        fileNames, fileType = QFileDialog.getOpenFileNames(self, "选取要上传的文件", os.getcwd(),"Excel Files(*.xls || *.xlsx)")
        # 根据返回的fileName的列表做进一步处理
        self.buiildModel(fileNames)
        print(self.model.rowCount())
        if self.model.rowCount() >0:
            self.ui.btnStartUpload.setEnabled(True)
            self.ui.btnClear.setEnabled(True)
        else:
            self.ui.btnStartUpload.setEnabled(False)
            self.ui.btnClear.setEnabled(False)



    # 添加文件
    def buiildModel(self,fileNames):
        # 需要判断一下是否已经在列表中，即第二次选择的话，不再添加
        rowCount=self.model.rowCount()
        index=0
        for file in fileNames:
            if len(self.model.findItems(file,Qt.MatchExactly|Qt.MatchRecursive,column=2))>0:  # 搜索第3列看文件是否已经在里面
                continue  #已存在，跳过
            filepath,filename=os.path.split(file);
            shotname,fileext=os.path.splitext(filename)
            col1 = QStandardItem(shotname)
            col1.setEditable(False)
            #col1.setEnabled(True)
            # 设置用户数据
            self.model.setItem(rowCount+index,0,col1)

            col2=QStandardItem(fileext)
            col2.setEditable(False)
            self.model.setItem(rowCount+index,1,col2)

            col3= QStandardItem(file)  # 完全路径
            col3.setEditable(False)
            self.model.setItem(rowCount+index, 2,col3)

            col4=QStandardItem(util.getFileSize(file))
            col4.setEditable(False)
            self.model.setItem(rowCount+index, 3, col4)

            self.ui.tableFileList.setIndexWidget(self.model.index(rowCount+index,4),TableUploadWidget(file,parent=self))
            # 设置行高，以便显示完全
            self.ui.tableFileList.setRowHeight(rowCount+index,45)
            index += 1


