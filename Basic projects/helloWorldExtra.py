from PyQt5 import QtWidgets
import sys
import helloWorld


class HelloWorldDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.myWidget = helloWorld.HelloWorldWindow()
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0)

        self.button = QtWidgets.QPushButton("&Edit text")

        self.mainBox = QtWidgets.QVBoxLayout()
        self.mainBox.addWidget(self.myWidget)
        self.mainBox.addWidget(self.button)

        self.setLayout(self.mainBox)

        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText("New text")
        self.button.setDisabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = HelloWorldDialog()
    window.setWindowTitle("Second QT programm")
    window.resize(300, 100)

    window.show()

    sys.exit(app.exec_())
