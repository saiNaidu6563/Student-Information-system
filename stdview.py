#program view students
import mysql.connector as ms
class stdview:
    def view1(self):
        try:
            con = ms.connect(host="localhost", user="root", passwd="7660919339",
                             database="students")
            cur = con.cursor()
            self.sno=int(input("enter which student record you have to view:"))
            q = "select * from student where sno=%d"
            cur.execute(q%(self.sno,))
            result=cur.fetchone()
            if result:
                # If the record is found, print it
                print("Student record found:")
                print(f"SNO: {result[0]}")
                print(f"Name: {result[1]}")
                print(f"Marks: {result[2]}")
                print(f"College Name: {result[3]}")
            else:
                print(f"No record found for SNO {self.sno}")

            con.commit()
        except ms.DatabaseError as db:
            print("problem in mysql", db)
        except ValueError:
            print("Don't enter alnums ,strs and special symbols:")

    def viewall(self):
        try:
            con = ms.connect(host="localhost", user="root", passwd="7660919339",
                             database="students")
            cur = con.cursor()

            q = "select * from student "
            cur.execute(q)
            result = cur.fetchall()
            for record in result:
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            else:
                print("No record found  ")

            con.commit()
        except ms.DatabaseError as db:
            print("problem in mysql", db)
        except ValueError:
            print("Don't enter alnums ,strs and special symbols:")


