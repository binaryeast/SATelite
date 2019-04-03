import sys
import sqlite3
import time, datetime

from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()     

    def setupUI(self):   
        self.showFullScreen()
        self.setWindowTitle("Missionary's Nuke")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()