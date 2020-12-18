from PyQt5 import QtCore, QtWidgets, QtPrintSupport


class PreviewDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("Предварительный просмотр")
        self.resize(600, 400)
        vBox = QtWidgets.QVBoxLayout()
        hBox1 = QtWidgets.QHBoxLayout()
        btnZoomIn = QtWidgets.QPushButton("&+")
        btnZoomIn.setFocusPolicy(QtCore.Qt.NoFocus)
        hBox1.addWidget(btnZoomIn, alignment=QtCore.Qt.AlignLeft)
        btnZoomOut = QtWidgets.QPushButton("&-")
        btnZoomOut.setFocusPolicy(QtCore.Qt.NoFocus)
        hBox1.addWidget(btnZoomOut, alignment=QtCore.Qt.AlignLeft)
        btnZoomReset = QtWidgets.QPushButton("&Сброс")
        btnZoomReset.setFocusPolicy(QtCore.Qt.NoFocus)
        btnZoomReset.clicked.connect(self.zoomReset)
        hBox1.addWidget(btnZoomReset, alignment=QtCore.Qt.AlignLeft)
        hBox1.addStretch()
        vBox.addLayout(hBox1)
        hBox2 = QtWidgets.QHBoxLayout()
        self.ppw = QtPrintSupport.QPrintPreviewWidget(parent.printer)
        self.ppw.paintRequested.connect(parent.sudoku.print)
        hBox2.addWidget(self.ppw)
        btnZoomIn.clicked.connect(self.ppw.zoomIn)
        btnZoomOut.clicked.connect(self.ppw.zoomOut)
        box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Close, QtCore.Qt.Vertical)
        btnClose = box.button(QtWidgets.QDialogButtonBox.Close)
        btnClose.setText("&Закрыть")
        btnClose.setFixedSize(96, 64)
        btnClose.clicked.connect(self.accept)
        hBox2.addWidget(box,
                        alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        vBox.addLayout(hBox2)
        self.setLayout(vBox)
        self.zoomReset()

    def zoomReset(self):
        self.ppw.setZoomFactor(1)
