import sys
from PyQt5.QtWidgets import *
import sqlite3
import time, datetime


con = sqlite3.connect("real.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM ex ORDER BY id DESC")
pid = cursor.fetchone()[-1]
exid = int(pid)+1

cursor.execute("SELECT * FROM study ORDER BY id DESC")
pid = cursor.fetchone()[-1]
stdid =  int(pid)+1

cursor.execute("SELECT * FROM daily ORDER BY id DESC")
pid = cursor.fetchone()[-1]
did =  int(pid)+1

today = str(datetime.datetime.now())[:10]
dday = datetime.date(2018, 11, 15) - datetime.date.today()
d_day = dday.days
stair = "no"
walk = "no"
exhour = 0

subject = "no"
quality = "bad"
stdhour = 0

diary = "Oh, Lord!"

def change():
    return "OK"

def up(a):
    a+=1
    return  a

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.resize(900,600)

    def setupUI(self):
        #self.setGeometry(800, 400, 600, 150)
        self.setWindowTitle("to-do manager")

        #labels
        day = QLabel("%s" % today, self)
        day.move(10, 20)

        d_daylabel = QLabel("d - %d" %d_day, self)
        d_daylabel.move(10, 50)

        prlabel = QLabel("Diary", self)
        prlabel.move(10, 100)

        stdlabel = QLabel("Study", self)
        stdlabel.move(10, 300)

        exlabel = QLabel("Exercise", self)
        exlabel.move(10, 500)

        #displaying stat
        self.stat = QLabel("Stat" ,self)
        self.stat.move(450, 10)
        self.stat.resize(300,20)

        #diary input
        self.dailyline = QLineEdit("", self)
        self.dailyline.move(550, 100)
        self.dailyline.resize(140,30)
        self.dailyline.returnPressed.connect(self.daily)

        dailybtn = QPushButton("Push", self)
        dailybtn.move(700, 100)
        dailybtn.clicked.connect(self.daily)

        #exercise
        btn1 = QPushButton("Enough?", self)
        btn1.move(700, 500)
        btn1.clicked.connect(self.stairbtn)

        btn2 = QPushButton("Jogging", self)
        btn2.move(700, 550)
        btn2.clicked.connect(self.walkbtn)



        #study
        self.subject = QLineEdit("", self)
        self.subject.move(550, 300)
        self.subject.returnPressed.connect(self.subinput)

        subbtn = QPushButton("subject", self)
        subbtn.move(700, 300)
        subbtn.clicked.connect(self.subinput)

        self.hourbox = QSpinBox(self)
        self.hourbox.move(550, 350)
        self.hourbox.valueChanged.connect(self.studyhours)

        self.qualcheck1 = QRadioButton("good", self)
        self.qualcheck1.move(700, 350)
        self.qualcheck1.clicked.connect(self.stdqual)

        self.qualcheck2 = QRadioButton("so-so", self)
        self.qualcheck2.move(700, 370)
        self.qualcheck2.setChecked(True)
        self.qualcheck2.clicked.connect(self.stdqual)

        self.qualcheck3 = QRadioButton("bad", self)
        self.qualcheck3.move(700, 390)
        self.qualcheck3.clicked.connect(self.stdqual)



        #yesterday
        self.yesbtn = QPushButton("yesterday", self)
        self.yesbtn.move(800, 550)
        self.yesbtn.clicked.connect(self.yesterday)


    def stairbtn(self):
        #QMessageBox.about(self, "message", "clicked")
        global stair
        stair = change()
        print(stair+"stair")
        self.stat.clear()
        self.stat.setText("Enough exercise")
        

    def walkbtn(self):
        #QMessageBox.about(self, "message", "clicked")
        global walk
        walk = change()
        print(walk+"walk")
        self.stat.clear()
        self.stat.setText("Enough jogging")

    
    def subinput(self):
        global subject
        subject = self.subject.text()
        print(subject)
        self.stat.setText("%s study finished" %subject)

    def daily(self):
        global daily
        daily = self.dailyline.text()
        print(daily)
        self.stat.setText("%s" %daily)

    def studyhours(self):
        global stdhour
        stdhour = self.hourbox.value()
        self.stat.setText("I studied %s hours." %stdhour)

    def stdqual(self):
        global quality
        msg = ""
        if self.qualcheck1.isChecked():
            msg = "good"
            self.stat.setText("good")
        elif self.qualcheck2.isChecked():
            msg = "so-so"
            self.stat.setText("so-so")
        else:
            msg = "bad"
            self.stat.setText("bad")
        quality = msg


    def yesterday(self):
        cursor.execute("SELECT * FROM daily ORDER BY id DESC")
        p = str(cursor.fetchone())

        cursor.execute("SELECT * FROM ex ORDER BY id DESC")
        exer = str(cursor.fetchone()[1:])

        cursor.execute("SELECT * FROM study ORDER BY id DESC")
        stu = str(cursor.fetchone()[1:])
        ysmessage = "diary : "+ p + "\nexercise : "+exer+"\nstudy : "+stu
        QMessageBox.about(self,"yesterday stat", "%s" %ysmessage)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWin()
    mywindow.show()     
    app.exec_()
    ex = "\""+today+"\", \""+stair+"\", \""+walk+"\", "+str(exhour)+" ,"+str(exid)
    
    study = "\""+today+"\", \""+subject+"\", \""+quality+"\", "+str(stdhour)+" ,"+str(stdid)
    daily = "\""+today+"\", \""+daily+"\", "+str(did)
    print(ex+study+daily)
    cursor.execute("""INSERT INTO ex VALUES(%s)""" % ex)
    cursor.execute("""INSERT INTO study VALUES(%s)""" % study)
    cursor.execute("""INSERT INTO daily VALUES(%s)""" % daily)
    con.commit()
    con.close()
    print("ok!") 
