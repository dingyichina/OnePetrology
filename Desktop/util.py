
import os,json

# 文件全路径传入之后得到文件大小的描述，转换为KB或者MB或者GB或者字节数
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QAbstractTableModel, Qt, QSize, QRectF, QUrl, QFileInfo, QModelIndex

# 根据载体代码返回载体描述
from PyQt5.QtGui import QPixmap, QWheelEvent, QPainter
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QGraphicsItem, QDialog, QApplication


def getCarrierDesc(carrierCode):
    carrierDict={"11":"纸质","12":"实物","13":"录音带","14":"录像带","15":"幻灯片","16":"硬盘","17":"胶卷/平片","18":"光盘","19":"其他介质"}
    return carrierDict[carrierCode]

# 得到文件大小
def getFileSize(file):
    fsize = os.stat(file).st_size
    if fsize <1024:
        return '{} 字节'.format(fsize)
    elif fsize<1024*1024:
        return '{} KB'.format(round(fsize/1024.0,2))
    elif fsize<1024*1024*1024:
        return '{} MB'.format(round(fsize /1024.0/1024, 2))
    else:
        return '{} GB'.format( round(fsize / 1024.0 / 1024/1024, 2) )


def getFileName(file):
    filepath, filename = os.path.split(file);
    shotname, fileext = os.path.splitext(filename)
    return shotname

# 把配置信息写入配置文件
def writeconfig(obj,file):
    with open("./config/"+file+".json","w") as f:
        json.dump(obj,f,ensure_ascii=False,indent=4)
# 加载配置文件，不需要后缀名.json，只传文件名就可以了。
def loadconfig(file):
    with open("./config/" + file + ".json", "r",encoding='utf-8') as f:
        return json.load(f)


# pandas读取的dataframe
class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

    # 以下为编辑功能所必须实现的方法
    def setData(self, index, value, role=Qt.EditRole):
        # 编辑后更新模型中的数据 View中编辑后，View会调用这个方法修改Model中的数据
        if index.isValid() and 0 <= index.row() < len(self._data) and value:
            col = index.column()
            print(col)
            if 0 < col < len(self.headers):
                self.beginResetModel()
                # if CONVERTS_FUNS[col]:  # 必要的时候执行数据类型的转换
                #     self.datas[index.row()][col] = CONVERTS_FUNS[col](value)
                # else:
                self.datas[index.row()][col] = value
                self.dirty = True
                self.endResetModel()
                return True
        return False

    def flags(self, index):  # 必须实现的接口方法，不实现，则View中数据不可编辑
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(
            QAbstractTableModel.flags(self, index) |
            Qt.ItemIsEditable | Qt.ItemIsSelectable)

    def insertRows(self, position, rows=1, index=QModelIndex()):
        # position 插入位置；rows 插入行数
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        pass  # 对self.datas进行操作
        self.endInsertRows()
        self.dirty = True
        return True

    def removeRows(self, position, rows=1, index=QModelIndex):
        # position 删除位置；rows 删除行数
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        pass  # 对self.datas进行操作
        self.endRemoveRows()
        self.dirty = True
        return True


"""
ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...

ffmpeg -i [输入文件名] [参数选项] -f [格式] [输出文件] 

参数选项： 
(1) -an: 去掉音频 
(2) -vn: 去掉视频 
(3) -acodec: 设定音频的编码器，未设定时则使用与输入流相同的编解码器。音频解复用在一般后面加copy表示拷贝 
(4) -vcodec: 设定视频的编码器，未设定时则使用与输入流相同的编解码器，视频解复用一般后面加copy表示拷贝 
(5) –f: 输出格式（视频转码）
(6) -bf: B帧数目控制 
(7) -g: 关键帧间隔控制(视频跳转需要关键帧)
(8) -s: 设定画面的宽和高，分辨率控制(352*278)
(9) -i:  设定输入流
(10) -ss: 指定开始时间（0:0:05）
(11) -t: 指定持续时间（0:05）
(12) -b: 设定视频流量，默认是200Kbit/s
(13) -aspect: 设定画面的比例
(14) -ar: 设定音频采样率
(15) -ac: 设定声音的Channel数
(16)  -r: 提取图像频率（用于视频截图）
(17) -c:v:  输出视频格式
(18) -c:a:  输出音频格式
(18) -y:  输出时覆盖输出目录已存在的同名文件
"""
# 视频转换函数，采用的是FFMPEG 命令行的方式进行。  duration单位为秒
def  processVideo(inputFile,outputFile,duration=180):

    pass

class ImageViewer(QGraphicsView):
    """ 图片查看器 """

    def __init__(self, pixmap,parent=None):
        super(ImageViewer,self).__init__(parent=parent)
        self.zoomInTimes = 0
        self.maxZoomInTimes = 42

        # 创建场景
        self.graphicsScene = QGraphicsScene()

        # 图片
        self.pixmap = pixmap
        self.pixmapItem = QGraphicsPixmapItem(self.pixmap)
        self.displayedImageSize = QSize(0, 0)

        # 初始化小部件
        self.__initWidget()

    def __initWidget(self):
        """ 初始化小部件 """
        self.resize(1200, 900)

        # 隐藏滚动条
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 以鼠标所在位置为锚点进行缩放
        self.setTransformationAnchor(self.AnchorUnderMouse)

        # 平滑缩放
        self.pixmapItem.setTransformationMode(Qt.SmoothTransformation)
        self.setRenderHints(QPainter.Antialiasing |
                            QPainter.SmoothPixmapTransform)

        # 设置场景
        self.graphicsScene.addItem(self.pixmapItem)
        self.setScene(self.graphicsScene)

    def wheelEvent(self, e: QWheelEvent):
        """ 滚动鼠标滚轮缩放图片 """
        if e.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def resizeEvent(self, e):
        """ 缩放图片 """
        super().resizeEvent(e)

        if self.zoomInTimes > 0:
            return

        # 调整图片大小
        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size()*ratio
        if ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)
        else:
            self.resetTransform()

    def setImage(self, imagePath: str):
        """ 设置显示的图片 """
        self.resetTransform()

        # 刷新图片
        self.pixmap = QPixmap(imagePath)
        self.pixmapItem.setPixmap(self.pixmap)

        # 调整图片大小
        self.setSceneRect(QRectF(self.pixmap.rect()))
        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size()*ratio
        if ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)

    def resetTransform(self):
        """ 重置变换 """
        super().resetTransform()
        self.zoomInTimes = 0
        self.__setDragEnabled(False)

    def __isEnableDrag(self):
        """ 根据图片的尺寸决定是否启动拖拽功能 """
        v = self.verticalScrollBar().maximum() > 0
        h = self.horizontalScrollBar().maximum() > 0
        return v or h

    def __setDragEnabled(self, isEnabled: bool):
        """ 设置拖拽是否启动 """
        self.setDragMode(
            self.ScrollHandDrag if isEnabled else self.NoDrag)

    def __getScaleRatio(self):
        """ 获取显示的图像和原始图像的缩放比例 """
        if self.pixmap.isNull():
            return 1

        pw = self.pixmap.width()
        ph = self.pixmap.height()
        rw = min(1, self.width()/pw)
        rh = min(1, self.height()/ph)
        return min(rw, rh)

    def fitInView(self, item: QGraphicsItem, mode=Qt.KeepAspectRatio):
        """ 缩放场景使其适应窗口大小 """
        super().fitInView(item, mode)
        self.displayedImageSize = self.__getScaleRatio()*self.pixmap.size()
        self.zoomInTimes = 0

    def zoomIn(self, viewAnchor=QGraphicsView.AnchorUnderMouse):
        """ 放大图像 """
        if self.zoomInTimes == self.maxZoomInTimes:
            return

        self.setTransformationAnchor(viewAnchor)

        self.zoomInTimes += 1
        self.scale(1.1, 1.1)
        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.setTransformationAnchor(self.AnchorUnderMouse)

    def zoomOut(self, viewAnchor=QGraphicsView.AnchorUnderMouse):
        """ 缩小图像 """
        if self.zoomInTimes == 0 and not self.__isEnableDrag():
            return

        self.setTransformationAnchor(viewAnchor)

        self.zoomInTimes -= 1

        # 原始图像的大小
        pw = self.pixmap.width()
        ph = self.pixmap.height()

        # 实际显示的图像宽度
        w = self.displayedImageSize.width()*1.1**self.zoomInTimes
        h = self.displayedImageSize.height()*1.1**self.zoomInTimes

        if pw > self.width() or ph > self.height():
            # 在窗口尺寸小于原始图像时禁止继续缩小图像比窗口还小
            if w <= self.width() and h <= self.height():
                self.fitInView(self.pixmapItem)
            else:
                self.scale(1/1.1, 1/1.1)
        else:
            # 在窗口尺寸大于图像时不允许缩小的比原始图像小
            if w <= pw:
                self.resetTransform()
            else:
                self.scale(1/1.1, 1/1.1)

        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.setTransformationAnchor(self.AnchorUnderMouse)
    # 把自己加入到一个对话框中进行显示
    def showDlg(self):
        dlg=QDialog(self.parent(),flags=Qt.Dialog|Qt.WindowMaximizeButtonHint|Qt.WindowCloseButtonHint)
        dlg.setWindowTitle("查看图像")
        dlg.resize(800,600)
        hl= QtWidgets.QVBoxLayout()
        hl.addWidget(self)
        dlg.setLayout(hl)
        dlg.show()

# 转换int到excel 的A开头的字符串
def column_to_name(colnum):
    if type(colnum) is not int:
        return colnum

    str = ''

    while (not (colnum // 26 == 0 and colnum % 26 == 0)):

        temp = 25

        if (colnum % 26 == 0):
            str += chr(temp + 65)
        else:
            str += chr(colnum % 26 - 1 + 65)

        colnum //= 26
        # print(str)
    # 倒序输出拼写的字符串
    return str[::-1]

class pdfReaderQWebView(QWebEngineView):

    def __init__(self, parent=None):
        super(pdfReaderQWebView,self).__init__(parent)
        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)

    def setFile(self, filename):
        Url = QUrl(filename)
        self.setUrl(QtCore.QUrl(Url))



if __name__ =="__main__":
    app = QApplication(sys.argv)

    gui = pdfReaderQWebView()

    gui.setFile("http://8.218.13.217:8080/pdfjs/web/viewer.html")

    gui.showMaximized()

    sys.exit(app.exec_())



    #print("------------test -------------")
    #print(loadconfig('oral'))
    """obj={
        "档号+室编件号": "dc.identifier.FN",
        "题名": "dc.tile",
        "创建者": "dc.contributor",
        "创建时间": "dc.date.created",
        "创建地点": "dc.contributor.location",
        "受访人/主要人物": "dc.contributor.interviewees",
        "采访人": "dc.contributor.interviewer",
        "内容摘要": "dc.description.abstract",
        "载体代码": "dcterms.format.medium",
        "存储路径": "dc.description.storagePath",
        "字数": "dc.description.wordCount",
        "语种": "dc.language.iso",
        "提供者": "dc.description.provider",
        "提供时间": "dc.date.provided",
        "备注": "dc.description.comment",
        "关联科学家":"relation.isScientistOfOralDocument",
        "dspace.entity.type":"OralDocument"
        }
    writeconfig(obj,"oral")  """
