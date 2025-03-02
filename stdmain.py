from stdmenu import student
from stdadd import *
from stddelete import *
from stdupdate import *
from stdview import *
from stdsearch import *
def stdmain():
        while(True):
            try:
                a=student()
                a.studmenu()
                ch=int(input("enter you are choice:"))
                match(ch):
                    case 1:
                        s = students()
                        s.insertdata()

                    case 2:
                        s = delete()
                        s.delestd()

                    case 3:
                        s = update()
                        s.stdupdate()

                    case 4:
                        s=stdview()
                        s.view1()
                    case 5:
                        s=stdview()
                        s.viewall()
                    case 6:
                        s = search()
                        s.search()
                    case 7:
                        print("thanks for using this program")
                        break
            except ValueError:
                print("Don't enter alnums ,strs and special symbols")


#mainprogramt

stdmain()