from PyQt5 import QtWidgets, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSplitter")
window.resize(500, 200)

# Create Horizontal splitter
splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

# Labels in splitter
label1 = QtWidgets.QLabel("Component 1 content")
label2 = QtWidgets.QLabel("Component 2 content")

# Set frame style
label1.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)

# Add widgets to splitter
splitter1.addWidget(label1)
splitter1.addWidget(label2)

# Same, but Vertical splitter
splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)

label3 = QtWidgets.QLabel("Component 3 content")
label4 = QtWidgets.QLabel("Component 4 content")

label3.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
label4.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)

splitter2.addWidget(label3)
splitter2.addWidget(label4)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(splitter1)
vbox.addWidget(splitter2)

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
