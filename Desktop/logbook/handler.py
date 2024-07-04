import logging

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal


class _Signals(QtCore.QObject):
    """ Custom signals """
    signal_record = pyqtSignal(logging.LogRecord)
    record_context_request = pyqtSignal(QtCore.QPoint, list, QtWidgets.QListWidget)

    def __init__(self):
        QtCore.QObject.__init__(self)


class LogbookHandler(logging.Handler):
    """ A handler that emits qt signals dedicated to our LogBook widget. """

    signals = _Signals()

    def emit(self, record):
        """ Emits a LogRecord object

        Args:
            record (logging.LogRecord): passed record object

        Returns:

        """
        self.signals.signal_record.emit(record)
