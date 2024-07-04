'''
    把CEF 作为浏览器嵌入

'''


# 浏览器内容窗口
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from cefpython3 import cefpython as cef
import sys

class CefBrowser(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.browser = None
        super().__init__(parent)
        self.installEventFilter(self)  #把自己注册为事件监听器

    def create_browser(self, window_info, url):
        self.browser = cef.CreateBrowserSync(window_info, url=url)

    def embedBrowser(self, url):
        self.url=url
        window_info = cef.WindowInfo()
        # void window_info.SetAsChild(int parentWindowHandle, list windowRect), windowRect~[left,top,right,bottom]
        window_info.SetAsChild(int(self.winId()), [0, 0, self.width(), self.height()])
        cef.PostTask(cef.TID_UI, self.create_browser, window_info, url)

    def eventFilter(self, watched, event):
        if event==QEvent.Resize:
            window_info = cef.WindowInfo()
            window_info.SetAsChild(int(self.winId()), [0, 0, self.width(), self.height()])
            cef.PostTask(cef.TID_UI, self.create_browser, window_info,self.url)
            pass
        return False
# Qt主窗口
class BrowserWindow:
    def setUI(self, MainWindow):
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("cefpython3-PyQt5")

        # URL输入框、查询按钮、浏览器控件
        self.le_search = QtWidgets.QLineEdit()
        self.le_search.setPlaceholderText("输入网址...")
        self.btn_search = QtWidgets.QPushButton()
        self.btn_search.setText("查询")
        self.browser_widget = CefBrowser()

        # 设置布局方式：栅栏式
        self.main_layout = QtWidgets.QGridLayout(MainWindow)
        self.main_layout.addWidget(self.le_search, 0, 0, 1, 1)
        self.main_layout.addWidget(self.btn_search, 0, 1, 1, 1)
        self.main_layout.addWidget(self.browser_widget, 1, 0, 8, 2)

        # 信号和槽函数
        self.signal_slots()

    def signal_slots(self):
        # 绑定`查询`按钮的点击事件
        self.btn_search.clicked.connect(self.slot_load_url)

    def slot_load_url(self):
        """获取输入框的URL，判断是否已存在browser对象，如果存在则LoadUrl否则开始创建浏览器"""
        if self.le_search.text():
            if self.browser_widget.browser:
                self.browser_widget.browser.LoadUrl(self.le_search.text())
            else:
                self.browser_widget.embedBrowser(self.le_search.text())

    def show(self):
        """创建和显示应用窗口，循环监听处理"""
        app = QtWidgets.QApplication([])
        widget = QtWidgets.QWidget()
        main_window = BrowserWindow()
        main_window.setUI(widget)
        widget.show()
        app.exec_()


if __name__ == "__main__":
    sys.excepthook = cef.ExceptHook
    # bool cef.Initialize(settings={...},switches={...})
    settings = {
        "debug": False,  # 调试模式
        "log_severity": cef.LOGSEVERITY_INFO,  # 日志的输出级别
        "log_file": "debug.log",  # 设置日志文件
        "user_agent": "test ",
        "multi_threaded_message_loop": True
    }
    switches = {
        "enable-media-stream": "",  # 取消获取媒体流（如音频、视频数据），必须以空字符串代表否！
        "proxy-server": "socks5://127.0.0.1:8888",  # 设置代理
        "disable-gpu": "",  # 设置渲染方式CPU or GPU
    }
    cef.Initialize(settings=settings)
    BrowserWindow().show()
    cef.Shutdown()