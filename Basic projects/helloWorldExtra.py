from PyQt5 import QtWidgets
import sys
import helloWorld


class HelloWorldDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # get window
        self.myWidget = helloWorld.HelloWorldWindow()
        # and set margins to it
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0)

        # add new button to edit text
        self.button = QtWidgets.QPushButton("&Edit text")

        # create vertical layout and add our widgets
        self.mainBox = QtWidgets.QVBoxLayout()
        self.mainBox.addWidget(self.myWidget)
        self.mainBox.addWidget(self.button)

        # set vertical layout to window
        self.setLayout(self.mainBox)

        # quit button listener
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText("New text")
        self.button.setDisabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # create window
    window = HelloWorldDialog()
    window.setWindowTitle("Second QT programm")
    window.resize(300, 100)

    window.show()

    sys.exit(app.exec_())
