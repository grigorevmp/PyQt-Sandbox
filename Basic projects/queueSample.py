from PyQt5 import QtCore, QtWidgets
import sys
import queue


class MyThread(QtCore.QThread):
    task_done = QtCore.pyqtSignal(int, int, name='taskDone')

    def __init__(self, _id, _queue, parent=None):
        super().__init__(parent)
        self.id = _id
        self.queue = _queue

    def run(self):
        while True:
            task = self.queue.get()
            self.sleep(5)
            self.task_done.emit(task, self.id)
            self.queue.task_done()


class MyWindow(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setText("Give tasks")
        self.queue = queue.Queue()
        self.threads = []
        for i in range(1, 3):
            thread = MyThread(i, self.queue)
            self.threads.append(thread)
            thread.taskDone.connect(self.on_task_done, QtCore.Qt.QueuedConnection)
            thread.start()
        self.clicked.connect(self.on_add_task)

    def on_add_task(self):
        for i in range(0, 11):
            self.queue.put(i)

    def on_task_done(self, data, _id):
        print(data, "- id =", _id)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # create window
    window = MyWindow()
    window.setWindowTitle("QT Queue")
    window.resize(300, 30)

    window.show()

    sys.exit(app.exec_())
