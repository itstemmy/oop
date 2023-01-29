class person:
    first_name = ""
    last_name =""
    age = 0
    phone_no = ""

    def __init__(self, fname,lname,age,phone_no) :
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.phone_no = phone_no


    def set_fname(self,fname):
        self.first_name = fname

        

    def get_fname(self):
         return self.first_name
    def get_lname(self):
        return self.last_name
    def get_age(self):
         return self.age
    def get_phone(self):
        return self.phone_no


# to inherit a class
# name the new class and call the name of the parent class to get a child class e.g

class student(person):

    school = "" 
    course = "" 
    faculty = "" 


    def __init__(self, fname, lname, age, phone_no, school, course, faculty):
        super().__init__(fname, lname, age, phone_no)
        self.school = school
        self.course = course
        self.faculty = faculty














