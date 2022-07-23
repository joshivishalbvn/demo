import mysql.connector as con 

db=con.connect(host="localhost",user="root",passwd="",database="student",port="3306")

print("coonection establised.....")
mycursor=db.cursor()

sql="create table studendetail(sid int primary key AUTO_INCREMENT ,sname varchar(20),smobileno varchar(10),sweight float(4),sgender int(1))"

mycursor.execute(sql)

db.commit()

print("database are created.......")