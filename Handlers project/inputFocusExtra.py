from PyQt5 import QtCore, QtWidgets, QtGui
import sys


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.id = None

    def event(self, e):
        if e.type() == QtCore.QEvent.Shortcut:
            if self.id == e.shortcutId():
                self.setFocus(QtCore.Qt.ShortcutFocusReason)
                return True
        return QtWidgets.QLineEdit.event(self, e)


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Focus")
        self.resize(300, 100)

        self.label = QtWidgets.QLabel("Se&t focus on field 1")
        self.lineEdit1 = QtWidgets.QLineEdit()
        self.label.setBuddy(self.lineEdit1)
        self.lineEdit2 = MyLineEdit()
        self.lineEdit2.id = self.lineEdit2.grabShortcut(
            QtGui.QKeySequence.mnemonic("&e")
        )
        self.button = QtWidgets.QPushButton("&Remove focus from field 1")

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.lineEdit1)
        self.vbox.addWidget(self.lineEdit2)
        self.vbox.addWidget(self.button)

        # set vertical layout to window
        self.setLayout(self.vbox)

        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.lineEdit1.clearFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # create window
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
