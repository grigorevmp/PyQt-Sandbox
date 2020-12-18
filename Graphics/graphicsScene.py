from PyQt5 import QtCore, QtWidgets, QtGui
import sys


def on_clicked():
    print(scene.hasFocus())
    scene.setFocus()
    scene.setFocusItem(rect)
    print(type(scene.focusItem()))
    print(scene.hasFocus())


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

line1 = scene.addLine(50.0, 50.0, 450.0, 50.0,
                      pen=QtGui.QPen(QtCore.Qt.red, 3))
line1.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
line1.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
line1.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable)

line2 = scene.addLine(QtCore.QLineF(50.0, 100.0, 450.0, 100.0),
                      pen=QtGui.QPen(QtCore.Qt.blue, 3))
line2.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
line2.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
line2.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0),
                     pen=QtGui.QPen(QtCore.Qt.blue, 3),
                     brush=QtGui.QBrush(QtCore.Qt.green))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable)

line1.setSelected(True)

view = QtWidgets.QGraphicsView(scene)

button = QtWidgets.QPushButton("Проверить")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())
