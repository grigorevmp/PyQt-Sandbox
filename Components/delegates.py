from PyQt5 import QtCore, QtWidgets, QtGui
import sys

from PyQt5.QtWidgets import QWidget


class SpinBoxDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        """
        Create component-editor used for edit position num
        :param parent:
        :param option:
        :param index:
        :return:
        """
        editor = QtWidgets.QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(0)
        editor.setSingleStep(1)
        return editor

    def setEditorData(self, editor: QWidget, index: QtCore.QModelIndex) -> None:
        """
        Set num to component-editor
        :param editor:
        :param index:
        :return:
        """
        value = int(index.model().data(index, QtCore.Qt.EditRole))
        editor.setValue(value)

    def updateEditorGeometry(self, editor: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> None:
        """
        Set editor geometry
        :param editor:
        :param option:
        :param index:
        :return:
        """
        editor.setGeometry(option.rect)

    def setModelData(self, editor: QWidget, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        """
        Set data to model
        :param editor:
        :param model:
        :param index:
        :return:
        """
        value = str(editor.value())
        model.setData(index, value, QtCore.Qt.EditRole)


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTableView()
window.setWindowTitle("Delegator")

sti = QtGui.QStandardItemModel(parent=window)
lst1 = ['Disk', 'Paper', 'Box']
lst2 = ["10", "2", "8"]
for row in range(0, 3):
    item1 = QtGui.QStandardItem(lst1[row])
    item2 = QtGui.QStandardItem(lst2[row])
    sti.appendRow([item1, item2])
sti.setHorizontalHeaderLabels(['Product', 'Num'])
window.setModel(sti)

window.setItemDelegateForColumn(1, SpinBoxDelegate())
window.setColumnWidth(0, 150)
window.resize(300, 150)
window.show()
sys.exit(app.exec_())
