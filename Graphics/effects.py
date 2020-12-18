from PyQt5 import QtCore, QtWidgets, QtGui
import sys


def on_clicked():
    view.setFocus()
    effect.setEnabled(not effect.isEnabled())
    effect.setBlurRadius(30)


def on_enabled_changed(status):
    print("on_enabled_changed", status)


def on_radius_changed(radius):
    print("on_radius_changed", radius)


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsBlurEffect")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0),
                     pen=QtGui.QPen(QtCore.Qt.darkGreen, 1),
                     brush=QtGui.QBrush(QtCore.Qt.darkGreen))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable)

effect = QtWidgets.QGraphicsBlurEffect()
effect.setBlurRadius(10)
effect.enabledChanged["bool"].connect(on_enabled_changed)
effect.blurRadiusChanged["qreal"].connect(on_radius_changed)
rect.setGraphicsEffect(effect)

view = QtWidgets.QGraphicsView(scene)

button = QtWidgets.QPushButton("Переключить статус и изменить параметры")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())
