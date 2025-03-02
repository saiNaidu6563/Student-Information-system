import mysql.connector as ms
class students:
    def databases(self):
        try:
            con=ms.connect(host="localhost",user="root",passwd="7660919339")
            cur=con.cursor()
            q="create database students"
            cur.execute(q)
            print("database created--verify")
        except ms.DatabaseError as db:
            print("problem in mysql",db)
    def createtab(self):
        self.databases()
        try:
            con=ms.connect(host="localhost",user="root",passwd="7660919339",
                           database="students")
            cur=con.cursor()
            q="create table student(sno int primary key,Name varchar(10) not null,marks decimal(6.2) not null,collegename varchar(10) not null)"
            cur.execute(q)
            print("table is created--verify")
        except ms.DatabaseError as db:
            print("problem in mysql",db)
    def insertdata(self):

        try:
            con=ms.connect(host="localhost",user="root",passwd="7660919339",
                           database="students")
            cur=con.cursor()
            self.sno=int(input("enter a student number:"))
            self.name=input("enter student name:")
            self.marks=float(input("enter student marks:"))
            self.cname=input("enter clg name:")
            q="insert into student values(%d,'%s',%f,'%s')"
            cur.execute(q%(self.sno,self.name,self.marks,self.cname))
            con.commit()
            print("{} is inserted--verify".format(cur.rowcount))
        except ms.DatabaseError as db:
            print("problem in mysql",db)
        except ValueError:
            print("Don't enter alnums,strs and special symbols")




