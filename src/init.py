import mainDesign
import inputDesign
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import webbrowser
import subprocess

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainDesign.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.actionForum.triggered.connect(openForum)
    ui.actionAbout.triggered.connect(lambda: print("help"))

    ui.InstallButton.clicked.connect(install_package)
    ui.UpdateButton.clicked.connect(update)
    ui.SearchButton.clicked.connect(search)

    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.size())
    sys.exit(app.exec_())

def openForum():
    webbrowser.open("https://github.com/idur-package/Visual-Idur/discussions")

def install_package():
    os.system("xterm -e 'read install && apt install $install && read'")
def search():
    Dialog = QtWidgets.QDialog()
    ui = inputDesign.Ui_Dialog()
    ui.setupUi(Dialog)

    ui.OkButton.clicked.connect(lambda: search_by_text(ui.TextInput.toPlainText()))
    ui.CloseButton.clicked.connect(lambda: Dialog.close())

    Dialog.show()
    sys.exit(Dialog.exec_())
def search_by_text(text : str):
    os.system("xterm -e 'idur se " + text + " && read'")
def update():
    os.system("xterm -e 'idur update'")



if __name__ == "__main__":
    main()