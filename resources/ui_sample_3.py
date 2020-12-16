# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample_3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myForm(object):
    def setupUi(self, myForm):
        myForm.setObjectName("myForm")
        myForm.resize(300, 70)
        self.horizontalLayout = QtWidgets.QHBoxLayout(myForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(myForm)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.btnQuit = QtWidgets.QPushButton(myForm)
        self.btnQuit.setObjectName("btnQuit")
        self.verticalLayout_2.addWidget(self.btnQuit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(myForm)
        QtCore.QMetaObject.connectSlotsByName(myForm)

    def retranslateUi(self, myForm):
        _translate = QtCore.QCoreApplication.translate
        myForm.setWindowTitle(_translate("myForm", "Form"))
        self.label.setText(_translate("myForm", "TextLabel"))
        self.btnQuit.setText(_translate("myForm", "PushButton"))

