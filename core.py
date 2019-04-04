import sqlite3
import time, datetime

from PyQt5 import QtWidgets, QtGui


# 전역 함수들 쓸 곳.
today = str(datetime.datetime.now())[:10]
left_day = datetime.date(2019, 11, 14) - datetime.date.today()
d_days = left_day.days

#SQL 준비.

# vars for test.
Cellname = "To-Do"
CellText = "일어나라 빛을 발하라."
fontsize = 20

# font
Basicfont = QtGui.QFont()
Basicfont.setFamily("D2Coding")
Basicfont.setPointSize(fontsize)


# DB 로직 짤 부분.

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        MasterLayout = QtWidgets.QHBoxLayout() # Grid 레이아웃으로 바꿀 것.
        MasterLayout.addLayout(self.Leftwing()) 
        MasterLayout.addLayout(self.MainBoard("완성까지!")) # MainGrid
        MasterLayout.addLayout(self.Rightwing())
        self.setLayout(MasterLayout)

        # 창 설정, 건드릴 것 없음.
        self.setWindowTitle("Missionary's Nuke")
        self.showMaximized()

    # 이 위에 함수들 써 놓고 아래에서 먹어라. 위아래는 상관없나?

    
    def Cell(self, Cellname, CellText, fontsize):
        CellBox = QtWidgets.QGroupBox("%s" %Cellname)
        gene = QtWidgets.QLabel("%s" %CellText)

        CellBox.setFont(Basicfont)
        gene.setFont(Basicfont)

        nucleus = QtWidgets.QVBoxLayout()
        nucleus.addWidget(gene)

        CellBox.setLayout(nucleus)
        return CellBox


    def post(self, postname): # 포스트잇 구현. postname은 groupbox 이름이고 cell은 항목임.
        postBox = QtWidgets.QGroupBox("%s" %postname)
        Basicfont.setPointSize(30)
        postBox.setFont(Basicfont)
        Basicfont.setPointSize(fontsize)

        post1 = self.Cell(Cellname, CellText, fontsize)
        post2 = self.Cell(Cellname, CellText, fontsize)
        post3 = self.Cell(Cellname, CellText, fontsize)
        post4 = self.Cell(Cellname, CellText, fontsize)
        post5 = self.Cell(Cellname, CellText, fontsize)
        post6 = self.Cell(Cellname, CellText, fontsize)
        post7 = self.Cell(Cellname, CellText, fontsize)
        # 7개 기억!

        postLayout = QtWidgets.QVBoxLayout()
        postLayout.addWidget(post1)
        postLayout.addWidget(post2)
        postLayout.addWidget(post3)
        postLayout.addWidget(post4)
        postLayout.addWidget(post5)
        postLayout.addWidget(post6)
        postLayout.addWidget(post7)

        postBox.setLayout(postLayout)

        return postBox

        """
        #Basicfont setting
        Basicfont = QtGui.QFont()
        Basicfont.setFamily("D2Coding")
        Basicfont.setPointSize(20)
        """

    def Board(self):
        coreBox = QtWidgets.QHBoxLayout()
        coreBox.addWidget(self.post("Task"))
        coreBox.addWidget(self.post("test"))
        coreBox.addWidget(self.post("study"))

        return coreBox


    def MainBoard(self, notice):
        Notice = QtWidgets.QLabel("Notice : %s" %notice)
        Notice.setFont(Basicfont)

        Command = QtWidgets.QLineEdit("What?")
        Command.setFont(Basicfont)

        MainGrid = QtWidgets.QGridLayout()
        MainGrid.addWidget(Notice, 0, 0, 2, 1)
        MainGrid.addLayout(self.Board(), 2, 0, 5, 1)
        MainGrid.addWidget(Command, 7, 0, 2, 1)
        #MainGrid.addWidget(self.Board(), 1, 0, 5, 1)
        
        return MainGrid

    
    def Leftwing(self): # 그리드로 바꿔 줘야 하고 이것저것 추가해야 함.
        StatBox = QtWidgets.QGroupBox()

        StatLayout = QtWidgets.QVBoxLayout()

        Left_dayLabel = QtWidgets.QLabel("d - %d" %d_days)
        Left_dayLabel.setFont(Basicfont)

        todayLabel = QtWidgets.QLabel("%s" %today)
        todayLabel.setFont(Basicfont)

        StatLayout.addWidget(Left_dayLabel)
        StatLayout.addWidget(todayLabel)

        return StatLayout


    def Rightwing(self):
        SaveBtn = QtWidgets.QPushButton()


        RightGrid = QtWidgets.QGridLayout()
        RightGrid.addWidget(SaveBtn, 8, 0, 1, 1)

        return RightGrid
        
# finish GUI! now we must make slots.

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    app.exec_()

    #이제 앱 실행 종료되면 해야 될 부분.