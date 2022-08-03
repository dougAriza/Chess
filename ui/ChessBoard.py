from ui.ChessBoardUI import Ui_MainWindow
from PyQt5 import QtWidgets
import os

class ChessBoard:
    def __init__(self) -> None:
        os.system('pyuic5 UI_Doc\ChessBoard.ui -o ui\ChessBoardUI.py')
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(MainWindow)
        self.settingButtonsAction()
        MainWindow.show()
        sys.exit(app.exec_())
        
    def settingButtonsAction(self):
        for button in self.__ui.BordFrame.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(lambda  state, name = button.objectName(): self.onButton(name))
            
    def onButton(self, name:str):
        button = self.__ui.BordFrame.findChild(QtWidgets.QPushButton, name)
        print(button.objectName())