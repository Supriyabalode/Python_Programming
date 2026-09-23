# class Student:
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
#     def display(self):
#         print("name:",self.name)
#         print("city:",self.city)
# class Exam(Student):
#     def __init__(self,name,city,m1,m2,m3):
#         super().__init__(name,city)
#         super().display()
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#         self.avg=(m1+m2+m3)/3
# exam1=Exam("supriya","pune",80,70,60)
# print(exam1.avg)




# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def __init__(self,name,age,student_id):
#         super().__init__(name,age)
#         self.student_id=student_id
# student1=Student("supriya",21,123)
# print("Name:",student1.name)
# print("age:",student1.age)
# print("id:",student1.student_id)





# CALLING PARENT METHOD.........

# class Vehicle:
#     def start(self):
#         print("vehicle starting..")
    
# class Car(Vehicle):
#     def start(self):
#         print("car starting")
#         super().start()              #inherit method from base class...
# car=Car()
# car.start()




#MULTIPLE INHERITANCE
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Employee:
#     def __init__(self,emp_id):
#         self.emp_id=emp_id
# class Manager(Person,Employee):
#     def __init__(self,name,age,emp_id,dept):
#         Person.__init__(self,name,age)
#         Employee.__init__(self,emp_id)
#         self.dept=dept
# manager1=Manager("abc",54,1,"electronics")
# print(manager1.name)




# class Grandparent:
#     def __init__(self,name):
#         self.name=name
# class Parent(Grandparent):
#     def __init__(self,name,occupation):
#         super().__init__(name)
#         self.occupation=occupation
# class Child(Parent):
#     def __init__(self,name,occupation,school):
#         super().__init__(name,occupation)
#         self.school=school
# child=Child("Emily","Teacher","sprinfield high")
# print(child.name,child.occupation,child.school)



# class Grandparent:
#     def __init__(self,name):
#         self.name=name
# class Parent:
#     def __init__(self,occupation):
#         self.occupation=occupation
# class Child(Grandparent,Parent):
#     def __init__(self,name,occupation,school):
#         Grandparent.__init__(self,name)
#         Parent.__init__(self,occupation)
#         self.school=school
# child1=Child("abc","teacher","xyz")
# print("name:",child1.name)
# print("occupation:",child1.occupation)
# print("school:",child1.school)



#MULTILEVEL INHERITANCE..

class Student:
    def __init__(self,name):
        self.name=name
class Address(Student):
    def __init__(self,name,gaon):
        super().__init__(name)
        self.gaon=gaon
class Result(Address):
    def __init__(self,name,gaon,marks):
        super().__init__(name,gaon)
        self.marks=marks
    def Display(self):
        print(self.name)
        print(self.gaon)
        print(self.marks)
result=Result("supriya","khandgaon",70)
result.Display()
student=Student("a")
print(student.name)






#MULTILEVEL INHERITANCE..

# class Grandparent:
#     def __init__(self,gname):
#         self.gname=gname
# class Parent(Grandparent):
#     def __init__(self,pname,gname):
#         super().__init__(gname)
#         self.pname=pname
# class Child(Parent):
#     def __init__(self,gname,pname,name):
#         Parent.__init__(self,pname,gname)
#         self.name=name
# child1=Child("a","b","c")
# print("gname:",child1.gname)
# print("pname:",child1.pname)
# print("name:",child1.name)




# class Student:
#     def __init__(self,name,marks,roll):
#         self.name=name
#         self.marks=marks
#         self.roll=roll
# class Personal_Info(Student):    
#     def __init__(self,name,roll):
#         super().__init__(name,roll)
#     def Display(self):
#         print("name:",self.name)
#         print("roll:",self.roll)
# class Result(Student):
#     def __init__(self,name,marks):
#         super().__init__(name,marks)
#     def Display1(self):
#         print(f"{self.name} has {self.marks} marks")
# Personalinfo=Personal_Info("supriya",2)
# Personalinfo.Display()




# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def Display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#     def DisplayData(self):
#         self.Display()
# class Exam(Student):
#     def __init__(self,name,age,marks):
#         super().__init__(name,age)
#         self.marks=marks
# exam=Exam("supriya",21,67)
# exam.Display()
# std=Student("supriya",21)
# std.DisplayData()
