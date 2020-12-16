from PyQt5 import QtCore, QtWidgets
import sys


class HelloWorldWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """
        Run window with "Hello world" text
        Button to Edit text
        :return:
        """
        super().__init__(parent)

        self.label = QtWidgets.QLabel("Hello, world!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        # & used for alt+c hotkey
        self.btnQuit = QtWidgets.QPushButton("&Close window")

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)

        self.setLayout(self.vbox)

        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = HelloWorldWindow()
    window.setWindowTitle("First QT programm")
    window.resize(300, 70)

    window.show()

    sys.exit(app.exec_())
