'''

  对plotly  express的pyqt封装，嵌入到一个widget中，用以支撑plotly express在pyqt中的集成

'''
import os
import sys
import tempfile

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QFileDialog
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

class PlotlyWidget(QWebEngineView):

    def __init__(self,fig=None, parent=None):
        super(PlotlyWidget, self).__init__(parent)
        self.page().profile().downloadRequested.connect(self.on_downloadRequested)

        self.settings().globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.settings().setAttribute(self.settings().ShowScrollBars, False)
        self.settings().setAttribute(QWebEngineSettings.WebGLEnabled, True)

        self.temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False)
        self.set_figure(fig)

        self.resize(700, 600)
        self.setWindowTitle("绘图")

    def set_figure(self, fig=None):
            self.temp_file.seek(0)
            if fig is None:
                fig = go.Figure()
            fig.update_xaxes(showspikes=True)
            fig.update_yaxes(showspikes=True)
            html = fig.to_html( config={"responsive": True, 'scrollZoom': True})
            html += "\n<style>body{margin: 0;}" \
                    "\n.plot-container,.main-svg,.svg-container{width:100% !important; height:100% !important;}</style>"

            self.temp_file.write(html)
            self.temp_file.truncate()
            self.temp_file.seek(0)
            self.load(QtCore.QUrl.fromLocalFile(self.temp_file.name))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.temp_file.close()
        os.unlink(self.temp_file.name)
        super().closeEvent(event)

    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(400, 400)

    def on_downloadRequested(self, download):
        dialog = QtWidgets.QFileDialog()
        dialog.setDefaultSuffix(".png")
        path, _ = dialog.getSaveFileName(self, "Save File", os.path.join(os.getcwd(), "newplot.png"), "*.png")
        if path:
            download.setPath(path)
            download.accept()


    def on_downloadRequested(self, download):
        dialog = QFileDialog()
        dialog.setDefaultSuffix(".png")
        path, _ = dialog.getSaveFileName(self, "Save File", os.path.join(os.getcwd(), "newplot.png"), "*.png")
        if path:
            download.setPath(path)
            download.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling | QtCore.Qt.AA_DisableWindowContextHelpButton)  # 去掉问号。
    appWin = PlotlyWidget()
    appWin.show()
    df = pd.read_excel("d:/岩石数据库-黄河数据.xlsx", sheet_name="样品基本信息", header=2)
    df.info()

    fig = px.scatter(df, x="SiO2", y="TiO2",color="Oraginal_Sample_Id",symbol="Oraginal_Sample_Id",title="Plotly图形显示",template="plotly_dark")
    appWin.set_figure(fig)
    sys.exit(app.exec_())

