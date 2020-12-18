from PyQt5 import QtGui, QtWidgets
import sys

from modules.mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)

# set icon
app.setWindowIcon(QtGui.QIcon(r"images/svd.png"))
window = MainWindow()
window.show()
sys.exit(app.exec_())
