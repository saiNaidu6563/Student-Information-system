#program searching student
import mysql.connector as ms
class search:
    def search(self):

            try:
                con = ms.connect(host="localhost", user="root", passwd="7660919339",
                                 database="students")
                cur = con.cursor()
                self.sno=int(input("enter which student record you have to view:"))
                q = "select * from student where sno=%d"
                cur.execute(q%(self.sno,))
                result=cur.fetchone()
                res="Not found"
                for val in result:
                     if result[0]==self.sno:
                         res = "Found"

                if res=="Not found":
                    print("\t{} Employee Number  does not Exist".format(self.sno))
                else:
                    print("\t{} Employee Number  Exist".format(self.sno))

                con.commit()
            except ms.DatabaseError as db:
                print("problem in mysql", db)
            except ValueError:
                print("Don't enter alnums ,strs and special symbols:")

