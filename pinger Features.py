# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PINGER(object):
    def setupUi(self, PINGER):
        PINGER.setObjectName("PINGER")
        PINGER.resize(400, 300)
        self.IP1 = QtWidgets.QToolButton(PINGER)
        self.IP1.setGeometry(QtCore.QRect(0, 130, 141, 21))
        self.IP1.setObjectName("IP1")
        self.IP2 = QtWidgets.QToolButton(PINGER)
        self.IP2.setGeometry(QtCore.QRect(0, 160, 141, 21))
        self.IP2.setObjectName("IP2")
        self.IP3 = QtWidgets.QToolButton(PINGER)
        self.IP3.setGeometry(QtCore.QRect(0, 190, 141, 21))
        self.IP3.setObjectName("IP3")
        self.IP4 = QtWidgets.QToolButton(PINGER)
        self.IP4.setGeometry(QtCore.QRect(0, 220, 141, 21))
        self.IP4.setObjectName("IP4")
        self.IP5 = QtWidgets.QToolButton(PINGER)
        self.IP5.setGeometry(QtCore.QRect(0, 250, 141, 21))
        self.IP5.setObjectName("IP5")
        self.STATUS = QtWidgets.QPushButton(PINGER)
        self.STATUS.setGeometry(QtCore.QRect(160, 100, 71, 21))
        self.STATUS.setObjectName("STATUS")
        self.PASS = QtWidgets.QPushButton(PINGER)
        self.PASS.setGeometry(QtCore.QRect(240, 100, 71, 21))
        self.PASS.setObjectName("PASS")
        self.FAIL = QtWidgets.QPushButton(PINGER)
        self.FAIL.setGeometry(QtCore.QRect(320, 100, 71, 21))
        self.FAIL.setObjectName("FAIL")
        self.QUIT = QtWidgets.QPushButton(PINGER)
        self.QUIT.setGeometry(QtCore.QRect(320, 270, 71, 21))
        self.QUIT.setObjectName("QUIT")
        
        

        self.retranslateUi(PINGER)
        QtCore.QMetaObject.connectSlotsByName(PINGER)

    def retranslateUi(self, PINGER):
        _translate = QtCore.QCoreApplication.translate
        PINGER.setWindowTitle(_translate("PINGER", "Dialog"))
        self.IP1.setText(_translate("PINGER", "..."))
        self.IP2.setText(_translate("PINGER", "..."))
        self.IP3.setText(_translate("PINGER", "..."))
        self.IP4.setText(_translate("PINGER", "..."))
        self.IP5.setText(_translate("PINGER", "..."))
        self.STATUS.setText(_translate("PINGER", "STATUS"))
        self.PASS.setText(_translate("PINGER", "PASS"))
        self.FAIL.setText(_translate("PINGER", "FAIL"))
        self.QUIT.setText(_translate("PINGER", "QUIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PINGER = QtWidgets.QDialog()
    ui = Ui_PINGER()
    ui.setupUi(PINGER)
    PINGER.show()
    sys.exit(app.exec_())
