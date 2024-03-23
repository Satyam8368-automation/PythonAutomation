class Parent:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def dis(self):
        print(self.fname,self.lname)

class child(Parent):
     pass

obj=Parent("SAT","AGNI")
obj.dis()
obj1=child("RAT","ATAYY")
obj1.dis()
