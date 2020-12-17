from PyQt5 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QStandartItemModel")

tv = QtWidgets.QTreeView(parent=window)
sti = QtGui.QStandardItemModel(parent=window)
rootitem1 = QtGui.QStandardItem('QAbstractItemView')
rootitem2 = QtGui.QStandardItem('Base class')

item1 = QtGui.QStandardItem('QListView')
item2 = QtGui.QStandardItem('List')
rootitem1.appendRow([item1, item2])

item1 = QtGui.QStandardItem('QTableView')
item2 = QtGui.QStandardItem('Table')
rootitem1.appendRow([item1, item2])

item1 = QtGui.QStandardItem('QTreeView')
item2 = QtGui.QStandardItem('Tree')
rootitem1.appendRow([item1, item2])

sti.appendRow([rootitem1, rootitem2])
sti.setHorizontalHeaderLabels(['Class', 'Description'])
tv.setModel(sti)
tv.setColumnWidth(0, 170)
tv.resize(400, 100)

window.show()
sys.exit(app.exec_())
