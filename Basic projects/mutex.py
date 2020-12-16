from PyQt5 import QtCore, QtWidgets
import sys


class MyThread(QtCore.QThread):
    x = 10
    mutex = QtCore.QMutex()

    def __init__(self, _id, parent=None):
        super().__init__(parent)
        self.id = _id

    def run(self):
        self.change_x()

    def change_x(self):
        MyThread.mutex.lock()
        print("x =", MyThread.x, "id =", self.id)
        MyThread.x += 5
        self.sleep(2)
        print("x =", MyThread.x, "id =", self.id)
        MyThread.x += 34
        print("x =", MyThread.x, "id =", self.id)
        MyThread.mutex.unlock()


class MyWindow(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setText("Run")

        self.thread1 = MyThread(1)
        self.thread2 = MyThread(2)

        self.clicked.connect(self.on_start)

    def on_start(self):
        if not self.thread1.isRunning(): self.thread1.start()
        if not self.thread2.isRunning(): self.thread2.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # create window
    window = MyWindow()
    window.setWindowTitle("QT Thread")
    window.resize(300, 100)

    window.show()

    sys.exit(app.exec_())
