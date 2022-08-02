
from email.errors import NonPrintableDefect
import mymodule2
from datetime import datetime

MainModuleChoise = 0


def DisplayCourse():
    sql = "select * from course where isDeleted=%s "
    values=[0]
    table = db.FetchRow(sql,values)
    print(f"{'id':15} {'title':28} {'fees':7} {'duration':14} {'description':30}")
    print("-"*100)
    for row in table:
        output = f"{row['id']} {'':12} {row['title']:28} {row['fees']:4} {'':6}{row['duration']:12} {row['description']:30}"
        print(output)
        print("-"*100)


def DisplayBatch():
    sql = "select * from batch  where isDeleted=%s "
    values= [0]
    table = db.FetchRow(sql,values)
    print(f"{'id':4} {'courseid':8} {'':4}{'start_date':14} {'end_date':14} {'class_time':15} ")
    print("-"*100)
    for row in table:
        output = f"{row['id']}  {row['courseid']:7} {'':5} {row['start_date']:14} {row['end_date']:14} {row['class_time']:15}"
        print(output)
        print('-'*100)


def DisplaySubject(id=None,all=None):
    if all!=None:
        sql = "select * from subject"
        table = db.FetchRow(sql)
        print(f"{'id':4} {'courseid':10}  {'title':11} {'rate':5}")
        print('-'*50)
        for row in table:
            output = f"{row['id']} {row['courseid']:8} {'':5} {row['title']:10} {row['rate']:5}"
            print(output)
            print('-'*50)
    


def DisplayTeacher():
    sql = "select * from teacher  where isDeleted=%s order by name"
    values=[0]
    table = db.FetchRow(sql,values)
    print(f"{'id':4} {'name':11} {'mobile':10} {' ':6} {'email':15}  {'gender'}  {'qualification'}  {' ':3} {'experience'}")
    print('-'*100)
    for row in table:
        output = f"{row['id']} {row['name']:4}  {row['mobile']:10} {' ':5} {row['email']:20} {row['gender']} {' ':7} {row['qualification']:5} {' ':12} {row['experience']}"
        print(output)
        print('-'*100)


def DisplayTeacherId():
    sql = 'select id,name from teacher'
    table = db.FetchRow(sql)
    print(f"{'id'} {' ':4} {'name'}")
    print('-'*20)
    for row in table:
        output = f"{row['id']} {' ':4}{row['name']}"
        print(output)
        print('-'*20)


def DisplaySubjectId():
    sql = 'select id,title from subject'
    table = db.FetchRow(sql)
    print(f"{'id'} {' ':4} {'title'}")
    print('-'*20)
    for row in table:
        output = f"{row['id']} {' ':4}{row['title']}"
        print(output)
        print('-'*20)


def DisplayBatchId():
    sql = 'select id,title from course '  # bhuk sudharvani chhe
    table = db.FetchRow(sql)
    print(f"{'id'} {' ':4} {'title'}")
    print('-'*20)
    for row in table:
        output = f"{row['id']} {' ':4}{row['title']}"
        print(output)
        print('-'*20)


def PayOutModule():
    sql = "select id,teacherid,subjectid,batchid,duration,amount,lecturedate from lecture where lecturedate>=%s and lecturedate<=%s"
    values = [lecturestartdate, lectureenddate]
    table = db.FetchRow(sql, values)
    print(f"{'id'} {'teacherid':10} {'subjectid':10} {'batchid':8} {'duration':8} {' ':3} {'amount':10} {'lecturedate'}")
    print('-'*80)
    for row in table:
        lecturedate = row['lecturedate'].strftime("%d-%m-%Y %H:%M")
        output = f"{row['id']} {' ':4} {row['teacherid']} {' ':8} {row['subjectid']}  {' ':6} {row['batchid']} {' ':6} {row['duration']} {' ':5} {row['amount']}  {' ':4} {lecturedate}"
        print(output)
        print("-"*80)


def TotalAmountModule():
    sql = 'select id,teacherid,subjectid,batchid,duration,amount,lecturedate from lecture'
    table = db.FetchRow(sql)
    print(f"{'id'} {'teacherid':10} {'subjectid':10} {'batchid':8} {'duration':8} {' ':2} {'amount':10} {'lecturedate'}")
    print('-'*80)
    GrandTotal = 0
    for row in table:
        output = f"{row['id']} {' ':4} {row['teacherid']} {' ':8} {row['subjectid']}  {' ':6} {row['batchid']} {' ':6} {row['duration']} {' ':5} {row['amount']}  {' ':4} {row['lecturedate']}"
        print(output)
        print("-"*80)
        GrandTotal = GrandTotal+row['amount']
    print(f"GrandTotal = {GrandTotal:38}")


db = mymodule2.DBOperation("rpi")

while True:
    print("1) Course Management")
    print("2) Batch Management")
    print("3) Subject Management")
    print("4) Teacher Management")
    print("5) Lecture Management")
    print("6) Payout Management")
    print("0) Exit")
    MainModuleChoise = int(input())

    
    if MainModuleChoise == 1:
        while True:
            print("1) Insert New Course")
            print("2) Update Current Course")
            print("3) Delete Course")
            print("4) Select Course")
            print("0) Back To Main Menu")
            CourseModuleChoise = int(input())
            if CourseModuleChoise == 1:
                title = input("Enter New Course Name")
                fees = int(input("Enter New Course Fees"))
                duration = int(input("Enter New Course Duration In Months"))
                description = input("Enter New Course Description")
                sql = "insert into course (title,fees,duration,description) values(%s,%s,%s,%s)"
                Values = [title, fees, duration, description]
                db.RunQuery(sql, Values)
                print("New Course Added")
            elif CourseModuleChoise == 2:
                DisplayCourse()
                courseid = int(input("Enter Id To Update Course"))
                title = input("Enter Update Course Name")
                fees = int(input("Enter Update Course Fees"))
                duration = int(input("Enter Update Course Duration In Months"))
                description = input("Enter Update Course Description")
                sql = "update course set title=%s,fees=%s,duration=%s,description=%s where id=%s"
                Values = [title, fees, duration, description, courseid]
                db.RunQuery(sql, Values)
                print("Course Updated")
            elif CourseModuleChoise == 3:
                DisplayCourse()
                id=int(input("Enter Course Id To Delete Course"))
                sql="update course set isDeleted=%s where id=%s"
                values=[1,id]
                db.RunQuery(sql,values)
                print("Course Deleted")
            elif CourseModuleChoise == 4:
                DisplayCourse()
            elif CourseModuleChoise == 0:
                break
            else:
                print("invalid Choise")

    elif MainModuleChoise == 2:
            while True:
                print("1) Insert New Batch")
                print("2) Update Current Batch")
                print("3) Delete Batch")
                print("4) Select Batch")
                print("0) Back To Main Menu")
                BatchModuleChoise = int(input())

                if BatchModuleChoise == 1:
                    DisplayCourse()
                    courseid = int(input("Enter Course Id To Add Course In Batch"))
                    sql = "select id from course where id=%s"
                    values = [courseid]
                    table = db.FetchRow(sql, values)
                    start_date = input("Enter Starting Date (dd-mm-yy)")
                    end_date = input("Enter Ending Date (dd-mm-yy)")
                    class_time = input("Enter Class Time (--to--)")
                    if len(table) > 0:
                        price = table[0]['id']
                        sql = "insert into batch (courseid, start_date,end_date,class_time) values (%s,%s,%s,%s)"
                        values = [courseid, start_date, end_date, class_time]
                        db.RunQuery(sql, values)
                        print("Batch Added")
                    else:
                        print("invalid course id")

                elif BatchModuleChoise == 2:  
                    DisplayBatch()
                    batchid = int(input("Enter batch ID To Update"))
                    DisplayCourse()
                    courseid=int(input("Enter Course Id"))
                    start_date = input("Enter Starting Date (dd-mm-yy)")
                    end_date = input("Enter Ending Date (dd-mm-yy)")
                    class_time = input("Enter Class Time (--to--)")
                    sql='update batch set courseid=%s,start_date=%s,end_date=%s,class_time=%s where id=%s'
                    values=[courseid,start_date,end_date,class_time,batchid]
                    db.RunQuery(sql,values)
                    print("Batch Updated ")

                elif BatchModuleChoise == 3:
                    DisplayBatch()
                    id = int(input("Enter batch ID To Delete"))
                    sql = "update batch set isDeleted=%s where id=%s"
                    values = [1,id]
                    db.RunQuery(sql, values)
                    print("Batch Deleted")
                elif BatchModuleChoise == 4:
                    DisplayBatch()
                elif BatchModuleChoise == 0:
                    break
                else:
                    print("Invalid Choise")

    elif MainModuleChoise == 3:
            while True:
                print("1) Insert New Subject")
                print("2) Update Current Subject")
                print("3) Delete Subject")
                print("4) Select Subject")
                print("0) Back To Main Menu")
                SubjectModuleChoise = int(input())

                if SubjectModuleChoise == 1:
                    DisplayCourse()
                    courseid = int(input("Enter Batch Id To Insert Subject In It"))
                    title = input("Enter Subject Name")
                    rate = int(input("Enter Subject Fees"))
                    sql = "insert into subject (courseid,title,rate) values(%s,%s,%s)"
                    values = [courseid, title, rate]
                    db.RunQuery(sql, values)
                    print("Subject Added")

                elif SubjectModuleChoise == 2:
                    DisplaySubject()
                    id = int(input("Enter Id To Update Subject"))
                    title = input("Enter New Name")
                    rate = int(input("Enter New Fees"))
                    sql = "update subject set title=%s,rate=%s where id=%s"
                    values = [title, rate, id]
                    db.RunQuery(sql, values)
                    print("Updated...")

                elif SubjectModuleChoise == 3:
                    DisplaySubject()
                    id = int(input("Enter id To Delete Subject"))
                    sql = "update subject set isDeleted=%s where id=%s"
                    values = [1, id]
                    db.RunQuery(sql, values)
                    print("Subject Deleted")

                elif SubjectModuleChoise == 4:
                    DisplaySubject()

                elif SubjectModuleChoise == 0:
                    break

                else:
                    print("Invalid Choise")

    
    elif MainModuleChoise == 4:
            while True:
                print("1) Insert New Teacher")
                print("2) Update Current Teacher")
                print("3) Delete Teacher")
                print("4) Select Teacher")
                print("0) Back To Main Menu")
                TeacherModuleChoise = int(input())

                if TeacherModuleChoise == 1:
                    name = input("Enter Teacher Name")
                    mobile = int(input("Enter Mobile Number"))
                    email = input("Enter E-mail")
                    gender = input("Enter Gender M or F")
                    qualification = input("Enter Qualification")
                    experience = int(input("Enter Experience in year"))
                    sql = "insert into teacher (name,mobile,email,gender,qualification,experience) values(%s,%s,%s,%s,%s,%s)"
                    values = [name, mobile, email,
                            gender, qualification, experience]
                    db.RunQuery(sql, values)
                    print("New Teacher Added..")
                elif TeacherModuleChoise == 2:
                    DisplayTeacher()
                    id = int(input("Enter Id To Update Teacher"))
                    name = input("Enter New Teacher Name")
                    mobile = int(input("Enter Mobile Number"))
                    email = input("Enter E-mail")
                    gender = input("Enter Gender M or F")
                    qualification = input("Enter Qualification")
                    experience = int(input("Enter Experience in year"))
                    sql = "update teacher set name=%s,mobile=%s,email=%s,gender=%s,qualification=%s,experience=%s where id=%s"
                    values = [name, mobile, email, gender,qualification, experience, id]
                    db.RunQuery(sql, values)
                    print("Teacher Updated")
                elif TeacherModuleChoise == 3:
                    DisplayTeacher()
                    id = int(input("Enter Id To Delete Teacher"))
                    sql = "update teacher set isDeleted=%s where id=%s"
                    values = [1, id]
                    db.RunQuery(sql, values)
                    print("Teacher Deleted")
                elif TeacherModuleChoise == 4:
                    DisplayTeacher()
                elif TeacherModuleChoise == 0:
                    break
                else:
                    print("invalid Choise")

    elif MainModuleChoise == 5:
            while True:
                print("1) Insert New Lecture")
                print("2) Select Lecture")
                print("0) Back To Main Menu")
                LectureModuleChoise = int(input())

                if LectureModuleChoise == 1:
                    DisplayTeacherId()
                    teacherid = int(input("Select Teacher By Entering Id"))
                    DisplaySubjectId()
                    subjectid = int(input("Enter Subject Id"))
                    DisplayBatchId()
                    batchid = int(input("Enterr Batch Id"))
                    duration = int(input("Enter Duration In Minutes"))
                    fees = int(input("Enter Amount Of Teacher Per Hour"))
                    rate = fees/60
                    amount = int(rate*duration)
                    sql = 'insert into lecture (teacherid,subjectid,batchid,duration,amount) values(%s,%s,%s,%s,%s)'
                    values = [teacherid, subjectid, batchid, duration, amount]
                    db.RunQuery(sql, values)
                    print("Lecture Detail Added")

                elif LectureModuleChoise == 2:
                    DisplayTeacherId()
                    
                elif LectureModuleChoise == 0:
                    break
                else:
                    print("Invalid Choise")

    elif MainModuleChoise == 6:
            while True:
                print("1) Generate batch wise lecture detail between given date ")
                print("2) Generate batch wise lecture detail with total amount")
                print("0) Exit To Main Menu")
                PayOutModuleChoise = int(input())

                if PayOutModuleChoise == 1:
                    print("Enter Start Date")
                    day = int(input("Enter Day"))
                    month = int(input("Enter Month"))
                    year = int(input("Enter Year"))
                    lecturestartdate = datetime(year, month, day)
                    print("Enter End Date")
                    day = int(input("Enter Day"))
                    month = int(input("Enter Month"))
                    year = int(input("Enter Year"))
                    lectureenddate = datetime(year, month, day)
                    PayOutModule()

                elif PayOutModuleChoise == 2:
                    TotalAmountModule()
                elif PayOutModuleChoise == 0:
                    break
                else:
                    print("Invalid Choise")

    elif MainModuleChoise == 0:
        print("Good Bye")
        break

    else:
        print("Invalid Choise")
