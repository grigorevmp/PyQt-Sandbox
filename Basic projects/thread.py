from PyQt5 import QtCore, QtWidgets
import sys


class MyThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = False
        self.count = 0

    def run(self):
        self.running = True
        while self.running:
            self.count += 1
            self.signal.emit(f"i = {self.count}")
            self.sleep(1)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QtWidgets.QLabel("Press button to start thread")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)

        self.buttonStart = QtWidgets.QPushButton("Start process")
        self.buttonStop = QtWidgets.QPushButton("Stop process")

        # create vertical layout
        self.vbox = QtWidgets.QVBoxLayout()
        # and add our widgets
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.buttonStart)
        self.vbox.addWidget(self.buttonStop)

        # set vertical layout to window
        self.setLayout(self.vbox)

        self.myThread = MyThread()
        self.buttonStart.clicked.connect(self.on_start)
        self.buttonStop.clicked.connect(self.on_stop)
        self.myThread.signal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_start(self):
        if not self.myThread.isRunning():
            self.myThread.start()

    def on_stop(self):
        self.myThread.running = False

    def on_change(self, s):
        self.label.setText(s)

    def closeEvent(self, event):
        """
        calling on window closing
        :param event: 
        :return:
        """
        self.hide()
        self.myThread.running = False
        self.myThread.wait(5000)
        event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # create window
    window = MyWindow()
    window.setWindowTitle("QT Thread")
    window.resize(300, 100)

    window.show()

    sys.exit(app.exec_())
