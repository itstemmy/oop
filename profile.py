# python is an object oriented programming language. almost everything in python is an object,
# with its properties and methods.
# A class--- is like object constructor or a blue print for creating object
# a class is like a remote which has different functions which is called method.
# class profile:
#     any variable declared inside a class is called property and any function declared inside
#     a class is called method.
# all classes have a function called __init__() (constructor function) which is always executed
# when the class is been initiated.
# uses of constructor function ---
# 1. assign value to object properties or other operation that are necessary.
class profile:
    name = ""
    age = 0
    gender =""
    nationality =""
    school =""

    def __init__(self,name,age,gender,nationality,school):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.school = school
    def output(self):
        name = self.name
        age = self.age
        gender = self.gender
        nationality = self.nationality
        school = self.school
        print(f'my name is {name}, i am {age} years old, i am from {nationality}')


student1 = profile("Maryam",16,"female","Ghana","Lautech")
student2 = profile("Emmanuel",20,"male","Congo","Landmark")
#print("My name is "+student1.name+" i am "+str(student1.age)+" i am from "+student1.nationality)
#print("my name is +student2")
student1.output()
student2.output()
 


