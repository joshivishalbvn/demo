import mysql.connector as con 

db=con.connect(host="localhost",user="root",passwd="",database="",port="3306")

print("coonection establised.....")
mycursor=db.cursor()

sql="create database student"

mycursor.execute(sql)

db.commit()

print("database are created.......")