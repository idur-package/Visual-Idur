import mainDesign
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

import webbrowser

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainDesign.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.actionForum.triggered.connect(openForum)
    ui.actionAbout.triggered.connect(lambda: print("help"))
    ui.InstallButton.clicked.connect(install_package)

    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.size())
    sys.exit(app.exec_())

def openForum():
    webbrowser.open("https://github.com/idur-package/Visual-Idur/discussions")

def install_package():
    os.system("xterm -e 'read install && apt install $install && read'")
def search_package():
    pass



if __name__ == "__main__":
    main()