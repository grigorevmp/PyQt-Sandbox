from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QToolBox")
window.resize(200, 100)

toolbox = QtWidgets.QToolBox()
toolbox.addItem(QtWidgets.QLabel("1 tab content"), "Tab &1")
toolbox.addItem(QtWidgets.QLabel("2 tab content"), "Tab &2")
toolbox.addItem(QtWidgets.QLabel("3 tab content"), "Tab &3")
toolbox.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolbox)

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
