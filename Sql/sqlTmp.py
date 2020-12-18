from PyQt5 import QtCore, QtWidgets, QtSql
import sys


def addRecord():
    """
    Add empty row
    :return:
    """
    stm.insertRow(stm.rowCount())


def delRecord():
    """
    Delete row
    Then again read data to a model
    :return:
    """
    stm.removeRow(tv.currentIndex().row())
    stm.select()


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSqlTableModel")

con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()

if 'good' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("create table good(id integer primary autoincrement,"
               "goodname text,"
               "goodcount integer,"
               "catname, integer)")

query = QtSql.QSqlQuery()
query.prepare("insert into good values(null, :goodname, :goodcount, :catname)")
query.bindValue(':goodname', 'Disk')
query.bindValue(':goodcount', 4)
query.bindValue(':catname', 'Disk')
query.exec_()
con.close()

# create model
# stm = QtSql.QSqlRelationalTableModel(parent=window)
stm = QtSql.QSqlTableModel(parent=window)
stm.setTable('good')
stm.setSort(1, QtCore.Qt.AscendingOrder)


# set relationship
#stm.setRelation(3, QtSql.QSqlRelation('category', 'id', 'catname'))

stm.select()

# set header name
stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Num')
stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Category')

# set table to our model
tv = QtWidgets.QTableView()
tv.setModel(stm)

# hide first column and set width
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 60)
tv.setColumnWidth(3, 150)

# Button to add record
btnAdd = QtWidgets.QPushButton("&Add record")
btnAdd.clicked.connect(addRecord)

# Button to delete record
btnDel = QtWidgets.QPushButton("&Delete record")
btnDel.clicked.connect(delRecord)

# Add items to box layout
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tv)
vbox.addWidget(btnAdd)
vbox.addWidget(btnDel)

window.setLayout(vbox)

window.resize(420, 250)
window.show()
sys.exit(app.exec_())
