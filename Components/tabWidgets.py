from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QTabWidget")
window.resize(400, 100)

tab = QtWidgets.QTabWidget()
tab.addTab(QtWidgets.QLabel("1 tab content"), "Tab &1")
tab.addTab(QtWidgets.QLabel("2 tab content"), "Tab &2")
tab.addTab(QtWidgets.QLabel("3 tab content"), "Tab &3")
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
