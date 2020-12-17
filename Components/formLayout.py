from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QFormLayout")
window.resize(300, 150)
lineEdit = QtWidgets.QLineEdit()
textEdit = QtWidgets.QTextEdit()
button1 = QtWidgets.QPushButton("&Send")
button2 = QtWidgets.QPushButton("&Clear")

hbox = QtWidgets.QHBoxLayout()
# and add our widgets
hbox.addWidget(button1)
hbox.addWidget(button2)

form = QtWidgets.QFormLayout()
form.addRow("&Name:", lineEdit)
form.addRow("&Description:", textEdit)
form.addRow(hbox)
window.setLayout(form)
window.show()
sys.exit(app.exec_())
