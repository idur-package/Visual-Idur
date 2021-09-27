import design
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = design.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.InstallButton.clicked.connect(install_package)

    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.size())
    sys.exit(app.exec_())

def install_package():
    os.system("xterm -e 'read install && apt install $install && read'")


if __name__ == "__main__":
    main()