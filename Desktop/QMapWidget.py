'''
   封装的qigis中的qgsMapCanvas类

   author ：丁毅
   20221110
'''
import datetime
import math
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget
from pandas import DataFrame
from qgis._core import QgsCircle, QgsPoint, QgsGeometry, QgsRectangle, QgsPolygon, QgsRasterLayer, QgsVectorLayer, \
    QgsFeature
from qgis.core import QgsWkbTypes, QgsPointXY
from qgis.gui import QgsMapToolZoom, QgsMapToolEmitPoint, QgsRubberBand
from qgis.gui import QgsMapToolPan

from ui.ui_qmap import Ui_QMapWidget
import geopandas as gpd
# 矩形工具
class RectangleMapTool(QgsMapToolEmitPoint):
  def __init__(self, canvas):
    self.canvas = canvas
    QgsMapToolEmitPoint.__init__(self, self.canvas)
    self.rubberBand = QgsRubberBand(self.canvas, QgsWkbTypes.PolygonGeometry)
    self.rubberBand.setColor(QColor(255, 0, 0, 100))
    self.rubberBand.setWidth(1)
    self.reset()

  def reset(self):
    self.startPoint = self.endPoint = None
    self.isEmittingPoint = False
    self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)

  def canvasPressEvent(self, e):
    self.startPoint = self.toMapCoordinates(e.pos())
    self.endPoint = self.startPoint
    self.isEmittingPoint = True
    self.showRect(self.startPoint, self.endPoint)

  def canvasReleaseEvent(self, e):
    self.isEmittingPoint = False
    r = self.rectangle()
    if r is not None:
      print(r.asPolygon())
      print("Rectangle:", r.xMinimum(),
            r.yMinimum(), r.xMaximum(), r.yMaximum()
           )
    self.getPolyCoordList()

  def canvasMoveEvent(self, e):
    if not self.isEmittingPoint:
      return

    self.endPoint = self.toMapCoordinates(e.pos())
    self.showRect(self.startPoint, self.endPoint)

  def showRect(self, startPoint, endPoint):
    self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)
    if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
      return

    point1 = QgsPointXY(startPoint.x(), startPoint.y())
    point2 = QgsPointXY(startPoint.x(), endPoint.y())
    point3 = QgsPointXY(endPoint.x(), endPoint.y())
    point4 = QgsPointXY(endPoint.x(), startPoint.y())

    self.rubberBand.addPoint(point1, False)
    self.rubberBand.addPoint(point2, False)
    self.rubberBand.addPoint(point3, False)
    self.rubberBand.addPoint(point4, True)    # true to update canvas
    self.rubberBand.show()

  def rectangle(self):
    if self.startPoint is None or self.endPoint is None:
      return None
    elif (self.startPoint.x() == self.endPoint.x() or \
          self.startPoint.y() == self.endPoint.y()):
      return None

    return QgsRectangle(self.startPoint, self.endPoint)

  def deactivate(self):
      super(RectangleMapTool, self).deactivate()
      self.deactivated.emit()
      self.reset()

  def getPolyCoordList(self):
      r = self.rectangle()
      if r is None:
         return None
      pts = []
      polystr = r.asPolygon()
      for pstr in polystr.split(","):
          cs = pstr.strip().split(' ')
          pts.append([float(cs[0]),float(cs[1])])
      print("转换为多边形：",pts)
      return pts
# 圆形工具
class CircleMapTool(QgsMapToolEmitPoint):
  def __init__(self, canvas):
    self.canvas = canvas
    QgsMapToolEmitPoint.__init__(self, self.canvas)
    self.rubberBand = QgsRubberBand(self.canvas, QgsWkbTypes.PolygonGeometry)
    self.rubberBand.setColor(QColor(255, 0, 0, 100))
    self.rubberBand.setWidth(1)
    self.reset()

  def reset(self):
    self.startPoint = self.endPoint = None
    self.isEmittingPoint = False
    self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)

  def canvasPressEvent(self, e):
    self.startPoint = self.toMapCoordinates(e.pos())
    self.endPoint = self.startPoint
    self.isEmittingPoint = True
    self.showCircle(self.startPoint, self.endPoint)

  def canvasReleaseEvent(self, e):
    self.isEmittingPoint = False
    r = self.circle()
    if r is not None:
      print(r.toPolygon(36).asJson(4))
      print("Circle:", r.center()," , radius:", r.radius())
    self.getPolyCoordList()
  def canvasMoveEvent(self, e):
    if not self.isEmittingPoint:
      return

    self.endPoint = self.toMapCoordinates(e.pos())
    self.showCircle(self.startPoint, self.endPoint)

  def showCircle(self, startPoint, endPoint):
    self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)
    if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
      return

    point1 = QgsPoint(startPoint.x(), startPoint.y())

    point2 = QgsPoint(endPoint.x(), endPoint.y())

    circle = QgsCircle.fromCenterPoint(point1,point2)
    for p in circle.points():

        self.rubberBand.addPoint(QgsPointXY(p.x(),p.y()), True)    # true to update canvas
    # self.rubberBand.updateCanvas()
    self.rubberBand.show()

  def circle(self):
    if self.startPoint is None or self.endPoint is None:
      return None
    elif (self.startPoint.x() == self.endPoint.x() or \
          self.startPoint.y() == self.endPoint.y()):
      return None
    point1 = QgsPoint(self.startPoint.x(), self.startPoint.y())

    point2 = QgsPoint(self.endPoint.x(), self.endPoint.y())
    return QgsCircle.fromCenterPoint(point1,point2)


  def deactivate(self):
    super(CircleMapTool, self).deactivate()
    self.deactivated.emit()
    self.reset()

  def getPolyCoordList(self):
      r = self.circle()
      if r is None:
         return None
      pts = []
      for p in r.points(36):
          pts.append([p.x(),p.y()])
      print("转换为多边形：", pts)
      return pts

# 多边形工具
class PolygonMapTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.rubberBand = QgsRubberBand(self.canvas, QgsWkbTypes.PolygonGeometry)
        self.rubberBand.setColor(QColor(255, 0, 0, 100))
        self.rubberBand.setWidth(1)
        self.reset()

    def reset(self):
        self.is_start = False  # 开始绘图
        self.is_vertical = False  # 垂直画线
        self.cursor_point = None
        self.points = []
        self.rubberBand.reset(True)

    def canvasPressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.points.append(self.cursor_point)
            self.is_start = True
        elif event.button() == Qt.RightButton:
            self.getPolyCoordList()
            # 右键结束绘制
            if self.is_start:
                self.is_start = False
                self.cursor_point = None
                self.show_polygon()
                self.points = []
            else:
                pass

        else:
            pass

    def canvasMoveEvent(self, event):
        self.cursor_point = event.mapPoint()
        if not self.is_start:
            return
        self.show_polygon()

    def show_polygon(self):
        self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)  # 防止拖影
        first_point = self.points[0]
        last_point = self.points[-1]
        self.rubberBand.addPoint(first_point, False)
        for point in self.points[1:-1]:
            self.rubberBand.addPoint(point, False)
        if self.cursor_point:
            self.rubberBand.addPoint(QgsPointXY(last_point.x(), last_point.y()), False)
        else:
            self.rubberBand.addPoint(QgsPointXY(last_point.x(), last_point.y()), True)
            self.rubberBand.show()
            return
        # 光标所在点
        if self.is_vertical and len(self.points) >= 2:
            countdown_second_point = self.points[-2]
            cursor_point_x = self.cursor_point.x()
            cursor_point_y = self.cursor_point.y()
            diff_x = int(math.fabs(last_point.x() - countdown_second_point.x()))
            diff_y = int(math.fabs(last_point.y() - countdown_second_point.y()))
            # if diff_x > diff_y:
            #     # 最后一条线的x,y差值比较
            #     cursor_point_x = equation(countdown_second_point.x(), countdown_second_point.y(), last_point.x(),
            #                               last_point.y(), self.cursor_point.y(), solve_type='x')
            # else:
            #     cursor_point_y = equation(countdown_second_point.x(), countdown_second_point.y(), last_point.x(),
            #                               last_point.y(), self.cursor_point.x(), solve_type='y')
            _cursor_point = QgsPointXY(cursor_point_x, cursor_point_y)
            self.cursor_point = _cursor_point

        self.rubberBand.addPoint(self.cursor_point, True)
        self.rubberBand.show()

    def deactivate(self):
        super(PolygonMapTool, self).deactivate()
        self.deactivated.emit()
        self.reset()

    def getPolyCoordList(self):
        if self.points is None or len(self.points)<3:
            return None
        pts = []
        for p in self.points:
            pts.append([p.x(), p.y()])
        # 闭合需要加上最后一个
        pts.append([self.points[0].x(),self.points[0].y()])
        print("转换为多边形：",pts)
        return pts

# 查找经度列，返回None则不存在
def getLongitudeColumn(df):
    if df is None:
        return None
    known = {"x",'longitude',"lon","经度","lon."}
    for col in df.columns:
        if col.lower().strip() in known:
            return col
    return None
# 查找纬度列，返回None则不存在
def getLatitudeColumn(df):
    if df is None:
        return None
    known = {"y",'latitude',"lat","纬度","lat."}
    for col in df.columns:
        if col.lower().strip() in known:
            return col
    return None

# 地图主widget
class QMapWidget(QWidget):

    def __init__(self,parent=None):
        super(QMapWidget, self).__init__(parent)
        self.maptool = None
        self.ui = Ui_QMapWidget()
        self.setupUi()

        self.layers = []  # 缓存所有图层

        # 设置参数
        self.ui.mapCanvas.setCanvasColor(QColor.fromRgb(255, 255, 255))
        self.ui.mapCanvas.enableAntiAliasing(True)
        # 初始化所有的地图工具
        self.maptool = None
        self.rectangleTool = RectangleMapTool(self.ui.mapCanvas)
        self.circleTool = CircleMapTool(self.ui.mapCanvas)
        self.polygonTool = PolygonMapTool(self.ui.mapCanvas)
        # 初始化图层名称
        # self.layerpath = "temp/vlayer{}.shp".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        self.layerpath = "temp.shp"

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        # 链接函数
        self.ui.btnMove.clicked.connect(self.doMove)
        self.ui.btnWhole.clicked.connect(self.doWholeMap)
        self.ui.btnZoomIn.clicked.connect(self.doZoomIn)
        self.ui.btnZoomOut.clicked.connect(self.doZoomOut)
        self.ui.mapCanvas.xyCoordinates.connect(self.show_lonlat)

        self.ui.btnPolygon.clicked.connect(self.doPolygon)
        self.ui.btnRectangle.clicked.connect(self.doRectangle)
        self.ui.btnCircle.clicked.connect(self.doCircle)


    def doCircle(self):
        self.maptool = self.circleTool
        self.ui.mapCanvas.setMapTool(self.maptool)

    def doRectangle(self):
        self.maptool = self.rectangleTool
        self.ui.mapCanvas.setMapTool(self.maptool)

    def doPolygon(self):
        self.maptool = self.polygonTool
        self.ui.mapCanvas.setMapTool(self.maptool)

    def doWholeMap(self):
        self.ui.mapCanvas.setExtent(self.ui.mapCanvas.layers()[-1].extent())
        self.ui.mapCanvas.refresh()
        pass

    def doZoomIn(self):
        self.maptool = QgsMapToolZoom(self.ui.mapCanvas, False)
        self.ui.mapCanvas.setMapTool(self.maptool)


    def doZoomOut(self):
        self.maptool = QgsMapToolZoom(self.ui.mapCanvas, True)
        self.ui.mapCanvas.setMapTool(self.maptool)
        pass

    def doMove(self):
        self.maptool = QgsMapToolPan(self.ui.mapCanvas)
        self.ui.mapCanvas.setMapTool(self.maptool)

    def show_lonlat(self, point):
        x = point.x()
        y = point.y()
        self.ui.lblStatus.setText(f'比例尺:{self.ui.mapCanvas.scale()} \t经度:{x},纬度:{y} ')
    def setLayers(self,layers):
        self.ui.mapCanvas.setLayers(layers)

    def setExtent(self,extent):
        self.ui.mapCanvas.setExtent(extent)
        self.ui.mapCanvas.refreshAllLayers()

    # 初始化底图
    def initBaseMap(self):
        urlWithParams = 'crs=EPSG:4326&dpiMode=7&format=image/png&layers=dde:world2022&styles=&tileMatrixSet=EPSG:4326&url=https://petrology.deep-time.org/geoserver/gwc/service/wmts'
        rlayer = QgsRasterLayer(urlWithParams, 'DDE岩浆岩图2022', 'wms')
        self.layers.append(rlayer)
        self.setLayers(self.layers)
        self.doWholeMap()

    # 加入dataframe
    def setDf(self,df:DataFrame):
        # 检查是否存在代表坐标的列，xy，经纬度，longitude/latitude ,lon,lat等
        if df is None :
            return
        x = getLongitudeColumn(df)
        y = getLatitudeColumn(df)
        if x is None or y is None:
            return
        # # 此时存在经纬度的列，需要根据这两个列创建一个矢量图层
        # gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[x], df[y])
        #                        , crs="EPSG:4326")
        # # 先写入shp文件，然后加载这个图层
        # # 此时好像没必要生成完整的图层，最好是能够动态生成图层 todo
        # gdf.to_file(self.layerpath)
        # vlayer = QgsVectorLayer(self.layerpath,"temp-points","ogr")

        vlayer = QgsVectorLayer("Point?crs=EPSG:4326&field=index:int",
                               'temp-point', "memory")
        # 遍历df
        for index,row in df.iterrows():
            f = QgsFeature(vlayer.fields())
            f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(row[x], row[y])))
            f.setValid(True)
            f.setAttributes([index])
            vlayer.dataProvider().addFeatures([f])
        self.layers.insert(0,vlayer)
        self.setLayers(self.layers)
        pass



if __name__ == "__main__":
    # Supply path to qgis install location
    #QgsApplication.setPrefixPath("D:\\QGIS 3.22.12", True)




    pass

