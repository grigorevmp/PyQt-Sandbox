from PyQt5 import QtWidgets, uic
import sys
from resources import ui_sample_3


class LoaderUi(QtWidgets.QWidget, ui_sample_3.Ui_myForm):
    """
    Load py from file in "resources/ui_sample_3.py"
    :return:
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoaderUi()
    window.show()
    sys.exit(app.exec_())
