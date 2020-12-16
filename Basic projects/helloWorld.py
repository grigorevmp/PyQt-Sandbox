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

        # create text label
        self.label = QtWidgets.QLabel("Hello, world!")
        # set text alignment to center
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        # & used for alt+c hotkey
        self.btnQuit = QtWidgets.QPushButton("&Close window")

        # create vertical layout
        self.vbox = QtWidgets.QVBoxLayout()
        # and add our widgets
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)

        # set vertical layout to window
        self.setLayout(self.vbox)

        # quit button listener
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # create window
    window = HelloWorldWindow()
    window.setWindowTitle("First QT programm")
    window.resize(300, 70)

    window.show()

    sys.exit(app.exec_())
