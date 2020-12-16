from PyQt5 import QtCore, QtGui, QtWidgets
import time, sys


class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Close screen")
        self.clicked.connect(QtWidgets.qApp.quit)

    def load_data(self, sp):
        for i in range(1, 11):
            time.sleep(2)
            sp.showMessage(f"Loading data... {i * 10}%",
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
            QtWidgets.qApp.processEvents()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("../resources/splashscreen.jpg"))

    splash.showMessage(f"Loading data... 0%",
                       QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    splash.show()
    QtWidgets.qApp.processEvents()
    # create window
    window = MyWindow()
    window.setWindowTitle("QT Splash")
    window.resize(300, 30)
    window.load_data(splash)
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
