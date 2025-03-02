#program for update student
import mysql.connector as ms
class update:
    def stdupdate(self):
        try:
            con = ms.connect(host="localhost", user="root", passwd="7660919339",
                             database="students")
            cur = con.cursor()
            self.sno = int(input("enter which student record you have delete:"))
            self.name = input("enter new student name:")
            self.marks = float(input("enter new student marks:"))

            q = "update student set name='%s',marks=%f where sno= %d"
            cur.execute(q % (self.name,self.marks,self.sno))
            print("one record  is updated--verify")
            con.commit()
        except ms.DatabaseError as db:
            print("problem in mysql", db)
        except ValueError:
            print("Don't enter alnums ,strs and special symbols:")


