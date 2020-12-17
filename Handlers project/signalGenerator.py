from PyQt5 import QtCore, QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):

    my_signal = QtCore.pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Signal generator")
        self.resize(300, 100)

        self.button1 = QtWidgets.QPushButton("Touch me")
        self.button2 = QtWidgets.QPushButton("Button 2")

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.button1)
        self.vbox.addWidget(self.button2)

        # set vertical layout to window
        self.setLayout(self.vbox)

        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.my_signal.connect(self.on_my_signal)

    def on_clicked_button1(self):
        print("Button 1 clicked")
        self.button2.clicked[bool].emit(False)
        self.my_signal.emit(10, 2)

    def on_clicked_button2(self):
        print("Button 2 clicked")

    def on_my_signal(self, x, y):
        print("Handler of my_signal custom signal")
        print("x =", x, "y =", y)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # create window
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
