# -*- coding: utf-8 -*

from PyQt5.Qt import *
import time


class LoadingMask(QMainWindow):
    def __init__(self, parent, gif=None, tip=None, min=0):
        """
        gif优先级高于 tip，两者同时赋值优先使用 gif
        :param parent:
        :param gif:
        :param tip:
        :param min:
        """
        super(LoadingMask, self).__init__(parent)

        self.min = min
        self.show_time = 0

        parent.installEventFilter(self)

        self.label = QLabel()

        if not tip is None:
            self.label.setText(tip)
            font = QFont('Microsoft YaHei', 10, QFont.Normal)
            font_metrics = QFontMetrics(font)
            self.label.setFont(font)
            self.label.setFixedSize(font_metrics.width(tip, len(tip)) + 10, font_metrics.height() + 5)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet(
                'QLabel{background-color: rgba(0,0,0,70%);border-radius: 4px; color: black; padding: 5px;}')

        if not gif is None:
            self.label.setStyleSheet(
                'QLabel{background-color: rgba(0,0,0,70%);border-radius: 4px; color: black; padding: 5px;}')
            self.movie = QMovie(gif)
            self.label.setMovie(self.movie)
            self.label.setAttribute(Qt.WA_TranslucentBackground)
            self.label.setFixedSize(QSize(329, 318))
            self.label.setScaledContents(True)
            self.movie.start()

        layout = QHBoxLayout()
        widget = QWidget()
        widget.setObjectName('background')
        # widget.setAttribute(Qt.WA_TranslucentBackground)
        widget.setStyleSheet('QWidget#background{background-color: rgba(255, 255, 255, 40%);}')
        widget.setLayout(layout)
        layout.addWidget(self.label)

        self.setCentralWidget(widget)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.hide()

    def eventFilter(self, widget, event):
        events = {QMoveEvent, QResizeEvent, QPaintEvent}
        if widget == self.parent():
            if type(event) == QCloseEvent:
                self.close()
                return True
            elif type(event) in events:
                self.moveWithParent()
                return True
        return super(LoadingMask, self).eventFilter(widget, event)

    def moveWithParent(self):
        if self.parent().isVisible():
            self.move(self.parent().geometry().x(), self.parent().geometry().y())
            self.setFixedSize(QSize(self.parent().geometry().width(), self.parent().geometry().height()))

    def show(self):
        super(LoadingMask, self).show()
        self.show_time = time.time()
        self.moveWithParent()

    def close(self):
        # 显示时间不够最小显示时间 设置Timer延时删除
        if (time.time() - self.show_time) * 1000 < self.min:
            QTimer().singleShot((time.time() - self.show_time) * 1000 + 10, self.close)
        else:
            super(LoadingMask, self).hide()
            super(LoadingMask, self).deleteLater()

    @staticmethod
    def showToast(window, tip='加载中...', duration=500, appended_task=None):
        mask = LoadingMask(window, tip=tip)
        mask.show()

        def task():
            mask.deleteLater()
            if callable(appended_task):
                appended_task()

        # 一段时间后移除组件
        QTimer().singleShot(duration, task)


if __name__ == '__main__':
    # import PySide2
    import sys

    # import os
    #
    # # 添加环境变量
    # plugin_path = os.path.join(os.path.dirname(PySide2.__file__), 'plugins', 'platforms')
    # os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setFixedSize(500, 500)
    widget.setStyleSheet('QWidget{background-color:black;}')

    button = QPushButton('button')
    layout = QHBoxLayout()
    layout.addWidget(button)
    widget.setLayout(layout)

    loading_mask = LoadingMask(widget, 'res/loading.gif')
    widget.show()
    loading_mask.show()

    # QTimer().singleShot(1000, lambda: loading_mask.hide())

    sys.exit(app.exec_())
