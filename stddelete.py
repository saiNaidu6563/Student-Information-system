#program for student delete
import mysql.connector as ms
class delete:
    def delestd(self):
        try:
            con = ms.connect(host="localhost", user="root", passwd="7660919339",
                             database="students")
            cur = con.cursor()
            self.sno=int(input("enter which student record you have delete:"))
            q = "delete from student where %d"
            cur.execute(q%(self.sno))
            print("one record  is deleted--verify")
            con.commit()
        except ms.DatabaseError as db:
            print("problem in mysql", db)
        except ValueError:
            print("Don't enter alnums ,strs and special symbols:")

