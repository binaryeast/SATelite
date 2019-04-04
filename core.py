import sqlite3
import time, datetime

from PyQt5 import QtWidgets, QtGui


# 전역 함수들 쓸 곳.
today = str(datetime.datetime.now())[:10]
left_day = datetime.date(2019, 11, 14) - datetime.date.today()
d_days = left_day.days


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        coreBox = QtWidgets.QHBoxLayout()
        coreBox.addWidget(self.post_it("Task"))
        coreBox.addWidget(self.post_it("test"))
        coreBox.addWidget(self.post_it("study"))

        dateWin = QtWidgets.QVBoxLayout()
        dateWin.addWidget(self.post_it("Date"))

        layout = QtWidgets.QHBoxLayout()
        layout.addLayout(coreBox)
        layout.addLayout(dateWin)


        self.setLayout(layout)

        self.setWindowTitle("Missionary's Nuke")
        self.showMaximized()
        #self.resize(480, 320)

    # def postit(self, postname):

    # 이 위에 함수들 써 놓고 아래에서 먹어라. 위아래는 상관없나?
    def post_it(self, postname): # 포스트잇 구현. postname은 groupbox 이름이고 cell은 항목임.
        groupBox = QtWidgets.QGroupBox("%s" %postname)

        cell1 = QtWidgets.QLabel("go!")
        cell2 = QtWidgets.QLabel("go!")
        cell3 = QtWidgets.QLabel("go!")

        #font setting
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(20)
        cell1.setFont(font)
        cell2.setFont(font)
        cell3.setFont(font)


        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(cell1)
        vbox.addWidget(cell2)
        vbox.addWidget(cell3)
        #vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    app.exec_()

    #이제 앱 실행 종료되면 해야 될 부분.