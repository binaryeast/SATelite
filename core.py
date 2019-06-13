import sys
import sqlite3
import time, datetime

from PyQt5 import QtWidgets, QtGui

from nltk.tokenize import WhitespaceTokenizer as Wtokenizer
import sqlcmd

# 전역 함수들 쓸 곳.
mod = sys.modules[__name__]
today = str(datetime.datetime.now())[:10]
left_day = datetime.date(2019, 11, 14) - datetime.date.today()
d_days = left_day.days

#SQL 준비.
con = sqlite3.connect("D:/New working space/Programming/SATelite/SATelite/power supply.db")
cursor = con.cursor()
cmdsor = sqlcmd.cmd("D:/New working space/Programming/SATelite/SATelite/power supply.db")


# vars for test.
Cellname = "To-Do"
CellText = "일어나라 빛을 발하라."
fontsize = 18

# font
Basicfont = QtGui.QFont()
Basicfont.setFamily("D2Coding")
Basicfont.setPointSize(fontsize)


# DB 로직 짤 부분.

def fileread(file):
    with open(file, "r") as f:
        plaintext = f.read()
        linetext = f.readlines()

    
def filewrite(file, data):
    with open(file, "w") as f:
        writing = f.write(data)

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        MasterLayout = QtWidgets.QHBoxLayout() # Grid 레이아웃으로 바꿀 것.
        MasterLayout.addLayout(self.Leftwing()) 
        MasterLayout.addLayout(self.MainBoard("완성까지!")) # MainGrid
        MasterLayout.addLayout(self.Rightwing())
        self.setLayout(MasterLayout)

        try:
            cursor.execute("SELECT * FROM date ORDER BY date_id DESC")
            lastday = cursor.fetchone()
            print(lastday)
            if lastday[1] == today:
                print("perfect!")
            else:
                datecommand = "INSERT INTO date VALUES(\""+today+"\")"
                print(datecommand)
                cursor.execute(datecommand)
            print("good!")
        except:
            print("DB error!")

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

        postname = postname.lower()
        # 여기서 세로줄이 칼럼인가? 그거 맞게 긁어오는 걸로 바꿔야 해. 아오 귀찮아.
        # cursor.execute("""SELECT * FROM %s ORDER BY id DESC""" %postname)

        for i in range(1, 8):
            # text = cursor.fetchone()
            setattr(mod, "post{}".format(i), self.Cell(Cellname, CellText, fontsize))

        postLayout = QtWidgets.QVBoxLayout()

        for i in range(1, 8):
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
        self.Notice = QtWidgets.QLabel("Notice : %s" %notice)
        self.Notice.setFont(Basicfont)

        self.Command = QtWidgets.QLineEdit("What?")
        self.Command.setFont(Basicfont)
        self.Command.returnPressed.connect(self.Bootstrap) # 여기에다 함수 넣으면 연결됨     라인 함수

        MainGrid = QtWidgets.QGridLayout()
        MainGrid.addWidget(self.Notice, 0, 0, 2, 1)
        MainGrid.addLayout(self.Board(), 2, 0, 5, 1)
        MainGrid.addWidget(self.Command, 7, 0, 2, 1)
        
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
        StatBox = QtWidgets.QGroupBox("Status")
        StatBox.setFont(Basicfont)

        return StatBox


    def Leftwing(self): # 그리드로 바꿔 줘야 하고 이것저것 추가해야 함.
        LeftBox = QtWidgets.QGridLayout()

        timeLayout = self.TimeLayout()
        statLayout = self.StatLayout()

        LeftBox.addWidget(timeLayout)
        LeftBox.addWidget(statLayout)

        return LeftBox 


    def Rightwing(self):
        SaveBtn = QtWidgets.QPushButton("Save")
        SaveBtn.clicked.connect(self.Save) # 여기도 함수.

        LineBtn = QtWidgets.QPushButton("command")
        LineBtn.clicked.connect(self.Bootstrap)

        RightGrid = QtWidgets.QGridLayout()
        RightGrid.addWidget(SaveBtn, ) 
        RightGrid.addWidget(LineBtn, 7, 0, 1, 1) 

        return RightGrid
        
# finish GUI! now we must make slots.
    def Save(self):
        print("Good to go!")
        pass

    def Bootstrap(self):
        print("Perfect!")
        # 이 아래 깨짐. 확인할것.
        commandline = self.Command.text()
        print(commandline)
        token_list = Wtokenizer().tokenize(commandline)
        for t in token_list:
            print(t)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    app.exec_()

    #이제 앱 실행 종료되면 해야 될 부분.