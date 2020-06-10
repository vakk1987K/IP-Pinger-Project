import os
import platform
import sys
import ipaddress
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox, QTextEdit, QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(600, 340))
        self.setWindowTitle("IP Pinger")

        self.nameLabel = QLabel(self)
        self.nameLabel2 = QLabel(self)
        self.nameLabel3 = QLabel(self)
        self.nameLabel.setText('Enter IP Address:')
        self.line = QLineEdit(self)
        self.line.move(110, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
        self.nameLabel2.setText('Select IP Address :')
        self.nameLabel2.move(20, 140)

        self.msgBox = QMessageBox(self)

        pybutton = QPushButton('Start', self)
        pybutton.clicked.connect(self.display)
        pybutton.resize(150, 32)
        pybutton.move(330, 20)
        pybutton.pressed.connect(self.find)

        pybutton2 = QPushButton('Clear', self)
        pybutton2.clicked.connect(self.line.clear)
        pybutton2.resize(150, 35)
        pybutton2.move(330, 70)

        self.combo = QComboBox(self)
        self.combo.addItem("172.17.174.250")
        self.combo.addItem("172.17.174.251")
        self.combo.addItem("172.17.174.252")
        self.combo.addItem("172.17.174.248")
        self.combo.addItem("172.17.174.12")
        self.combo.addItem("172.17.174.13")
        self.combo.addItem("172.17.174.23")
        self.combo.addItem("172.17.174.24")
        self.combo.addItem("172.17.174.100")
        self.combo.addItem("172.17.174.101")
        self.combo.addItem("172.17.174.103")

        self.combo.setGeometry(130, 145, 150, 200)

        self.combo.adjustSize()
        pybutton3 = QPushButton('Connect', self)
        pybutton3.resize(150, 32)
        pybutton3.move(330, 140)
        pybutton3.pressed.connect(self.find)

        self.statusBar()

    def display(self):
        host = ipaddress.ip_address(self.line.text())
        print(host)
        hostname = str(host)
        print(hostname)
        giveFeedback = False
        if platform.system() == "Windows":
            response = os.system("ping " + hostname + " -n 1")
        else:
            response = os.system("ping -c 1 " + hostname)
        isUpBool = 'SYSTEM IS DOWN'
        if response == 0:
            if giveFeedback:
                val = print(hostname, 'is up!')
            isUpBool = 'SYSTEM IS UP'
        else:
            if giveFeedback:
                print(hostname, 'is down!')
        print(isUpBool)
        sender = self.sender()
        self.statusBar().setFont(QFont('Arial', 12))
        self.statusBar().showMessage(hostname + " " + isUpBool)

        return isUpBool

    def find(self):
        host = ipaddress.ip_address(self.combo.currentText())
        print(host)
        hostname = str(host)
        print(hostname)
        giveFeedback = False
        if platform.system() == "Windows":
            response = os.system("ping " + hostname + " -n 1")
        else:
            response = os.system("ping -c 1 " + hostname)
        isUpBool = 'SYSTEM IS DOWN'
        if response == 0:
            if giveFeedback:
                val = print(hostname, 'is up!')
            isUpBool = 'SYSTEM IS UP'
        else:
            if giveFeedback:
                print(hostname, 'is down!')
        sender = self.sender()
        self.statusBar().setStyleSheet("background-color : yellow")
        self.statusBar().setFont(QFont('Arial', 12))
        self.statusBar().showMessage(hostname + " " + isUpBool)

        return isUpBool


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())