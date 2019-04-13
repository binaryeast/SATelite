import sqlite3

con = sqlite3.connect("real.db")

cursor = con.cursor()
cursor.execute("CREATE TABLE ex(Date text, Stair text, Walk text, Hour integer, id integer)")
cursor.execute("CREATE TABLE daily(Date text, daily text, id integer)")
cursor.execute("CREATE TABLE study(Date text, subject text, quality text, Hour integer, id integer)")


cursor.execute("""INSERT INTO ex VALUES("e", "x", "a", 0, 0)""")
cursor.execute("""INSERT INTO daily VALUES("e", "g", 0)""")
cursor.execute("""INSERT INTO study VALUES("m", "p", "l", 0, 0)""")


con.commit()
con.close()