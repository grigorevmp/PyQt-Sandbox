from PyQt5 import QtWidgets, uic
import sys


class LoaderUi(QtWidgets.QWidget):
    """
    Load ui from file in "resources/sample_3.ui"
    :return:
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        Form, Base = uic.loadUiType("resources/sample_3.ui")
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoaderUi()
    window.show()
    sys.exit(app.exec_())
