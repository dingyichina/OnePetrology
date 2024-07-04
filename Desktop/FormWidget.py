"""
   用于提交口述文字资料
   author：dingyi

   2021-12-05
"""
import datetime
import os, sys,json

import numpy as np
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox, QListView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from service.ScientistService import scientistService
from myservice import client
import util
from ui.ui_form import Ui_Form
import pandas as pd
from util import pandasModel

# 校对载体代码的函数，把默认读取的类型改为str
def correctCode(var):
    if pd.isnull(var):
        return ''
    if isinstance(var,float):
        return str(int(var))
    elif isinstance(var,int):
        return str(var)
    elif isinstance(var, bool):
        return str(var)
    else:
        return str(var)
#  转换datetime为字符串
def convertDatetime(var):
    if isinstance(var,datetime.datetime):
        if var.hour==0 and var.minute==0 and var.second==0:
            return var.strftime("%Y-%m-%d")
        else:
            return var.strftime("%Y-%m-%d %H:%M:%S")
    return var

class FormWidget(QWidget):


    def __init__(self,sheet_name,config_name, parent=None):
        super(FormWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.setupUi()
        self.sheet_name=sheet_name
        self.setWindowTitle(sheet_name)
        self.config = util.loadconfig(config_name)
        self.ui.lblSheet.setText(sheet_name)
        self.ui.lblCollection.setText(sheet_name)
        pass

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        #设置下拉框的选项的高度
        self.ui.combScientist.setStyleSheet("QAbstractItemView::item {height: 22px;}")
        self.ui.combScientist.setView(QListView())
        # 连接信号和槽
        self.ui.btnOpenFile.clicked.connect(self.openExcel)
        self.ui.btnSubmit.clicked.connect(self.doSubmit)
        # 设置科学家下拉列表
        scientists=scientistService.getScientistList()
        for s in scientists:
            self.ui.combScientist.addItem(s.name+"    :"+s.uuid)
        # 设置表格模型

    # 打开excel，并通过pandas
    def openExcel(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取清洗校对后的Excel文件", os.getcwd(),
                                                         "Excel Files(*.xls *.xlsx *.xlsm)")

        if fileName != '':  # 文件不为空
            self.curpath = os.path.dirname(fileName)  # 记录当前目录，传输文件时使用
            try:
                # 用pandas 打开
                self.df = pd.read_excel(fileName, sheet_name=self.sheet_name, header=0)  # 首行是表头，sheet名称是固定死的。
            except Exception as e:
                QMessageBox.critical(self, '错误', '您的excel读取错误。\r\n' + str(e), QMessageBox.Yes, QMessageBox.Yes)
                self.ui.btnSubmit.setEnabled(False)
                return #直接返回
            self.ui.lblFile.setText(fileName)
            # 去掉空行
            self.df.dropna(axis=0, how='all')  # 全部为空则去除
            # 是否滤重 ？
            self.df.drop_duplicates()  # 该操作暂时保留
            model = pandasModel(self.df)
            self.ui.tableView.setModel(model)
            # 处理表头与配置文件之间的对应关系。
            for colname in self.df.columns:
                colname=colname.strip()
                if colname not in self.config.keys():
                    QMessageBox.critical(self, '错误', '您的excel的表头不标准。\r\n' + colname + "\r\n 请修改校对后再重新打开。",
                                         QMessageBox.Yes, QMessageBox.Yes)
                    return  # 直接退出
            # 所有准备已就绪，上传按钮可用
            self.ui.btnSubmit.setEnabled(True)
        else:
            # 清空文件名。是否清空列表？
            self.ui.lblFile.setText('')
            self.ui.btnSubmit.setEnabled(False)


    # 提交数据
    def doSubmit(self):
        #获取科学家的uuid
        scientistUUID=self.ui.combScientist.currentText().split(':')[1]
        scientistName = self.ui.combScientist.currentText().split(':')[0].strip()
        if QMessageBox.question(self,"确认提交信息","您要提交的科学家是：\r\n    "+scientistName+"\r\n\r\n确认继续提交吗？", QMessageBox.Yes| QMessageBox.No, QMessageBox.Yes)!=QMessageBox.Yes:
            return

        # 确保载体代码的列为str类型
        if "载体代码" in self.df.columns:
           self.df["载体代码"] = self.df["载体代码"].apply(correctCode)

        self.ui.btnSubmit.setEnabled(False)
        # 根据dataframe和config拼接创建item的json数据
        for rIndex,row in self.df.iterrows():
            row=row.to_dict()
            item={}
            metadata={}
            for index,col in enumerate (self.df.columns):
                temp = row[col]
                if pd.isnull(temp) or temp=='':  # NaN 或者空字符略过
                    continue

                value = convertDatetime(temp)  # 把datetime转换为字符串
                metadata[self.config[col]]=[]
                # 首先检查是否是需要进行代码转换的列：载体代码   目前仅有一个需要进行转换的代码

                if col=="载体代码":
                    codes=value.replace('，',',')  # 兼容中文逗号，替换为西文逗号
                    for code in codes.split(","):  #默认只处理以逗号分割
                        meta = {
                            "value": util.getCarrierDesc(code),
                            "language": "zh_CN",
                            "authority": "null",
                            "confidence": -1
                        }
                        metadata[self.config[col]].append(meta)
                else:
                    meta={
                            "value":value,
                            "language": "zh_CN",
                            "authority": "null",
                            "confidence": -1
                          }
                    metadata[self.config[col]].append(meta)
                if self.config[col] == "dc.title":
                    item["name"] = row[col]
            # 设置entityType
            metadata["dspace.entity.type"]=[{
                        "value":self.config["dspace.entity.type"],
                        "language": "en",
                        "authority": "null",
                        "confidence": -1
                      }]
            #设置关联科学家
            metadata[self.config["关联科学家"]] = [{
                    "value": scientistUUID,
                    "language": "en",
                    "authority": "null",
                    "confidence": -1
                }]
            metadata["dc.scientist.name"] = [{
                    "value": scientistName,
                    "language": "zh_CN",
                    "authority": "null",
                    "confidence": -1
                }]
            #设置是否支持 IIIF
            metadata["dspace.iiif.enabled"] = [{
                    "value": "true",   # true 打开IIIF 功能， false 关闭
                    "language": "en",
                    "authority": "null",
                    "confidence": -1
                }]

            item["metadata"]=metadata
            item["inArchive"] = "true"
            item["discoverable"] = "true"
            item["withdrawn"] = "false"
            item["type"] = "item"
            # 执行创建item
            # print(json.dumps(item, indent=4, ensure_ascii=False))
            try:

                self.ui.txtUploadFile.setText("------add------" + item["name"])
            except Exception as e:
                print(e)
            rtn=client.createItemWithJson(self.config["collection_uuid"],item)
            #print(json.dumps(rtn.__dict__, indent=4, ensure_ascii=False))
            #根据返回的item执行上传
            # 查找到存储路径对应的值，如果不为空，则进入文件上传
            if isinstance(row[self.config["savepath"]],str):
                savepath = row[self.config["savepath"]]
                if not pd.isnull(savepath):  # 过滤掉nan值
                    if savepath!="":
                       self.doUpload(rtn,savepath)
        # 全部提交完毕 ，更新界面提示 todo：
        QMessageBox.information(self, '提醒', '您的excel的包含的内容已经提交完毕',
                             QMessageBox.Yes, QMessageBox.Yes)
        self.ui.txtUploadFile.setText("*********已经全部提交完成！****************")
        self.ui.progressBar.setValue(100)
    # 针对item上传附件，默认上传到ORIGINAL中
    def doUpload(self,item,savepath):
        print("upload 被调用",savepath)
        # 首先校对传入的savepath是否正确，当前目录必须是 . 开始，不允许出现 /或者\开头，因为这代表根目录
        if savepath.startswith('/') or savepath.startswith('\\'):
            savepath="."+savepath  #加上 .代表当前目录
        # 首先检查savepath是目录还是文件
        filepath=os.path.join(self.curpath,savepath)
        filepath=os.path.abspath(filepath)

        # 判断bundle是否需要创建
        if client.isBundleExists(item.uuid, "ORIGINAL") == False:
            # 不存在首先创建 bundle
            bundle=client.createBundle(item.uuid,"ORIGINAL")
        else:
            bundle=client.getItemBundle(item.uuid,"ORIGINAL")
        # 判断是文件还是目录
        if os.path.exists(filepath):
            if os.path.isdir(filepath):
                # 循环遍历目录下的所有文件，并上传
                for root, dirs, files in os.walk(filepath):
                    for dir in dirs:
                        # 递归调用子目录
                        self.doUpload(item,os.path.join(root, dir))
                    for file in files:
                        tempFilePath = os.path.join(root, file)
                        try:
                            self.ui.txtUploadFile.setText(tempFilePath)
                        except Exception as e:
                            print(e)
                        client.createBitstream(bundle.uuid, file, tempFilePath, self.uploadProgress)
                pass
            else:
                # 执行上传
                self.ui.txtUploadFile.setText(filepath)
                client.createBitstream(bundle.uuid,os.path.basename(filepath),filepath,self.uploadProgress)
                pass

    # 上传进度
    def uploadProgress(self,monitor):
        QApplication.processEvents()  # 防止界面被卡死
        progress = round(monitor.bytes_read / monitor.len * 100, 2)
        self.ui.progressBar.setValue(progress)

        pass
if __name__ == "__main__":
    # 单独测试本widget
    client.login('goaksoft@126.com', 'goaksoft123')
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = FormWidget("1.口述文字资料", "oral")
    appWin.show()

    sys.exit(app.exec_())
