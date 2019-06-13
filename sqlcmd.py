import sqlite3


class cmd():
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.con = sqlite3.connect(self.dbfile)
        self.cursor = self.con.cursor()

    def readall(self, table, line):
        self.cursor.execute("""SELECT * FROM %s ORDER BY %s DESC""" %(table, line))
        i = self.cursor.fetchall()
        return i

    def readone(self, table, line):
        self.cursor.execute("""SELECT * FROM %s ORDER BY %s DESC""" %(table, line))
        i = self.cursor.fetchone()
        return i

    def insert(self, table, value):
        self.cursor.execute("""INSERT INTO %s VALUES(%s)""" %table %value)
    
