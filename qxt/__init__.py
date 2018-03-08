# -*- coding: utf-8 -*-
"""PyQxt
Qt global shorcut
"""

__version__ = '0.0.1'

from PyQt5 import QtWidgets, QtCore
import keyboard


class HotKey(QtCore.QObject):

    triggered = QtCore.pyqtSignal()
    __mainThreaded = QtCore.pyqtSignal()

    def __init__(self, keySequence='', parent=None):
        super().__init__(parent)
        self._handler = None
        self.__mainThreaded.connect(lambda: self.triggered.emit(), QtCore.Qt.BlockingQueuedConnection)
        self.hook(keySequence)

    def hook(self, keySequence):
        self.unhook()
        self._keySequence = keySequence
        if keySequence:
            self._handler = keyboard.add_hotkey(keySequence, self.__callback)

    def unhook(self):
        if self._handler:
            keyboard.remove_hotkey(self._handler)
            self._handler = None

    def __callback(self):
        app = QtWidgets.QApplication.instance()
        if QtCore.QThread.currentThread() is app.thread():
            self.triggered.emit()
        else:
            self.__mainThreaded.emit()
