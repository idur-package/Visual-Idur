import mainDesign
import inputDesign
import messageDesign
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import webbrowser

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainDesign.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.actionForum.triggered.connect(openForum)
    ui.actionAbout.triggered.connect(messagewindow)

    ui.InstallButton.clicked.connect(lambda: textwindow("install"))
    ui.UpdateButton.clicked.connect(update)
    ui.SearchButton.clicked.connect(lambda: textwindow("search"))
    ui.ShowButton.clicked.connect(lambda: textwindow("show"))
    ui.RemoveButton.clicked.connect(lambda: textwindow("remove"))

    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.size())
    sys.exit(app.exec_())

def openForum():
    webbrowser.open("https://github.com/idur-package/Visual-Idur/discussions")

def messagewindow():
    Dialog = QtWidgets.QDialog()
    ui = messageDesign.Ui_Dialog()
    ui.setupUi(Dialog)

    ui.OkButton.clicked.connect(lambda: Dialog.close())

    Dialog.show()

def textwindow(mission : str):
    Dialog = QtWidgets.QDialog()
    ui = inputDesign.Ui_Dialog()
    ui.setupUi(Dialog)

    ui.OkButton.clicked.connect(lambda: mission_by_text(ui.TextInput.toPlainText(), mission))

    ui.CloseButton.clicked.connect(lambda: Dialog.close())

    Dialog.show()

def mission_by_text(text, mission):
    os.system("xterm -e 'idur " + mission + " " + text + " && echo && read -p \"enter to continue\" '")
def update():
    os.system("xterm -e 'idur update'")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print("v0.1")
            sys.exit()
    main()

