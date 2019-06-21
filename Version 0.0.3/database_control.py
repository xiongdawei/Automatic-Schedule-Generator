


import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'cykablyat',
    database = 'classtime',)

mycursor = mydb.cursor()




#mycursor.execute("CREATE TABLE classslot(name VARCHAR(255), age INTEGER(10))")
#mycursor.execute("CREATE TABLE students(name VARCHAR(255), ago INTEGER(10))")
#mycursor.execute("SHOW TABLES")
"""
sqlFormula = "INSERT INTO classslot (name, age) VALUES (%s, %s)"
time1 = ("Math", 22)
mycursor.execute(sqlFormula,time1)
mydb.commit()

time2 = ("English", 23)
sqlFormula = "INSERT INTO classslot (name, age) VALUES (%s, %s)"
mycursor.execute(sqlFormula,time2)
mydb.commit()
"""
sqlFormula_add = "ALTER TABLE classslot ADD place "
sqlFormula_add_teacher = "ALTER TABLE classslot ADD teacher VARCHAR(25)"
sqlFormula_add_serial = "ALTER TABLE classslot ADD serial INT(20)"
sqlFormula_add_timeslot = "ALTER TABLE classslot ADD timeslot VARCHA"
sqlFormula_add_group = "ALTER TABLE classslot ADD group INT(1)"
sqlFormula_add_week = "ALTER TABLE classslot ADD week INT(1)"
sqlFormula_drop_age = "ALTER TABLE classslot DROP COLUMN age "
sqlFormula_add_data = 'INSERT INTO classslot (name,place,teacher,serial,week) VALUES (%s,%s,%s,%s,%s) '


Dataset = []


mycursor.executemany(sqlFormula_add_data,Dataset)
mydb.commit()
mydb.close()






"""
mycursor.execute("SELECT * FROM classslot")
myresult1 = mycursor.fetchall()
myresult2 = mycursor.fetchone()


sql = "SELECT * FROM classslot WHERE age = 22"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
"""
"""
sql_getserial1 = "SELECT * FROM classslot WHERE serial=1"
mycursor.execute(sql_getserial1)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)

sql_getname1 = "SELECT * FROM classslot WHERE name LIKE '%an%'"
mycursor.execute(sql_getname1)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)

sql_delete = "DELETE FROM classslot WHERE name ='cyka blyat WHERE place = 0'"
mycursor.execute(sql_delete)
mydb.commit()

sql_droptable = "DROP TABLE students"
mycursor.execute(sql_droptable)
mydb.commit()
"""

