from person import person

from person import student

#instantiation and object creation
fullname = input("enter your fullname ")
age = eval(input("enter your age "))
phone_no = input("enter your phone number ")
split_name = fullname.split(" ")
#print(fullname.split(" ")[0])


school = input("enter school name ")
course = input("enter course ")
faculty = input("enter faculty ")
user1 = person(split_name[0],split_name[1],age,phone_no)
print(user1.get_fname())

student1 = student(split_name[0],split_name[1],age,phone_no,school,course,faculty)
print(student1.get_fname())