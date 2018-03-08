import sys
from PyQt5 import QtWidgets

from qxt import HotKey


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        self.editor = QtWidgets.QLineEdit(self)
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.hk = HotKey('ctrl+alt+z', self)
        self.hk.triggered.connect(self.callback)

    def callback(self):
        print('hotkey callback')
        self.editor.setText('HOTKEY')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    app.exec_()
