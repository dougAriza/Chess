from ui.ChessBoardUI import Ui_MainWindow
from PyQt5 import QtWidgets
import os

class ChessBoard:
    def __init__(self) -> None:
        os.system('pyuic5 ui\ChessBoard.ui -o ui\ChessBoardUI.py')
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.settingButtonsAction()
        MainWindow.show()
        sys.exit(app.exec_())

    def settingButtonsAction(self):
        pass