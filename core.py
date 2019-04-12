import sys
import sqlite3
import time, datetime

from PyQt5 import QtWidgets, QtGui

import nltk


# 전역 함수들 쓸 곳.
mod = sys.modules[__name__]
today = str(datetime.datetime.now())[:10]
left_day = datetime.date(2019, 11, 14) - datetime.date.today()
d_days = left_day.days

#SQL 준비.
con = sqlite3.connect("power supply.db")
cursor = con.cursor()

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

        post = postname.lower()

        # 여기서 DB 읽어서 바로 쏴주는 로직 필요함. 아오 나도 모르겠네

        post1 = self.Cell(Cellname, CellText, fontsize)
        for i in range(1, 8):
            # 이 아랫줄에 DBr읽어서 박는 것!
            # 여기서 읽어올 것.cursor.execute() 
            setattr(mod, "post{}".format(i), self.Cell(Cellname, CellText, fontsize))

        postLayout = QtWidgets.QVBoxLayout()
        postLayout.addWidget(post1)

        for i in range(2, 8):
            strorder = "postLayout.addWidget(post%d)" %i
            exec(strorder)

        postBox.setLayout(postLayout)

        return postBox


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


    def TimeLayout(self):
        TimeBox = QtWidgets.QGroupBox("your times")
        TimeBox.setFont(Basicfont)

        Left_dayLabel = QtWidgets.QLabel("d - %d" %d_days)
        Left_dayLabel.setFont(Basicfont)

        todayLabel = QtWidgets.QLabel("%s" %today)
        todayLabel.setFont(Basicfont)

        T_BoxLayout = QtWidgets.QVBoxLayout()
        T_BoxLayout.addWidget(Left_dayLabel)
        T_BoxLayout.addWidget(todayLabel)

        TimeBox.setLayout(T_BoxLayout)

        return TimeBox

    
    def StatLayout(self):
        StatBox = QtWidgets.QGroupBox()
        StatBox.setFont(Basicfont)

        return StatBox


    def Leftwing(self): # 그리드로 바꿔 줘야 하고 이것저것 추가해야 함.
        LeftBox = QtWidgets.QGridLayout()

        timeLayout = self.TimeLayout()
        statLayout = self.StatLayout()


        return LeftBox 


    def Rightwing(self):
        SaveBtn = QtWidgets.QPushButton()


        RightGrid = QtWidgets.QGridLayout()
        RightGrid.addWidget(SaveBtn, 8, 0, 1, 1)

        return RightGrid
        
# finish GUI! now we must make slots.
    def Save(self):
        pass


    



    def Bootstrap(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    app.exec_()

    #이제 앱 실행 종료되면 해야 될 부분.