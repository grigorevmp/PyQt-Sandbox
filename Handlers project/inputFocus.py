from PyQt5 import QtCore, QtWidgets
import sys


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, _id, parent=None):
        super().__init__(parent)
        self.id = _id

    def focusInEvent(self, e):
        print(f"Focus of {self.id} got")
        QtWidgets.QLineEdit.focusInEvent(self, e)

    def focusOutEvent(self, e):
        print(f"Focus of {self.id} lost")


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Focus")
        self.resize(300, 100)

        self.button = QtWidgets.QPushButton("Set focus on 2 filed")
        self.line1 = MyLineEdit(1)
        self.line2 = MyLineEdit(2)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.line2)

        # set vertical layout to window
        self.setLayout(self.vbox)

        self.button.clicked.connect(self.on_clicked)
        QtWidgets.QWidget.setTabOrder(self.line1, self.line2)
        QtWidgets.QWidget.setTabOrder(self.line2, self.button)

    def on_clicked(self):
        self.line2.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # create window
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
