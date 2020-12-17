import sys, time

from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):

    my_signal = QtCore.pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Simple timer")
        self.resize(200, 100)
        self.label = QtWidgets.QLabel("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)

        self.button1 = QtWidgets.QPushButton("Start")
        self.button2 = QtWidgets.QPushButton("Stop")
        self.button2.setEnabled(False)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button1)
        self.vbox.addWidget(self.button2)

        # set vertical layout to window
        self.setLayout(self.vbox)

        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)

        # time
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timeout)

    def on_clicked_button1(self):
        self.timer.start(1000)
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)

    def on_clicked_button2(self):
        self.timer.stop()
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)

    def on_timeout(self):
        self.label.setText(time.strftime("%H:%M:%S"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # create window
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
