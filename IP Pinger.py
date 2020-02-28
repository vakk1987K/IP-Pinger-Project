from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QTextEdit, QWidget


class IPPinger(QWidget):
    def __init__(self, parent=None):
        super(IPPinger, self).__init__(parent)

        nameLabel = QLabel("IP Address:")
        self.nameLine = QLineEdit()

        addressLabel = QLabel("Display:")
        self.addressText = QTextEdit()

        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0)
        mainLayout.addWidget(self.addressText, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("IPPinger")


if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    IPPinger = IPPinger()
    IPPinger.show()

    sys.exit(app.exec_())
