# class Parent:
#     def greet(self):
#         print("this is parent class...")
# class Child:
#     def greet(self):
#         print("this is child class")
# obj=Child()
# obj.greet()



# class Parent:
#     def greet(self):                #default constructor..........
           
#         self.name="supriya"
#         print(self.name)
# parent=Parent()
# parent.greet()
# print(parent.name)





# class Dog:
#     species="Canine"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# dog1=Dog("Buddy",4)
# dog2=Dog("charlie",5)

# print(dog1.species)
# print(dog1.name)
# print(dog2.name)
# #modify instance variables
# dog1.name="max"
# print(dog1.name)

# #modify class variable.
# Dog.species="feline"
# print(dog1.species)
# print(dog2.species)





# class Student:
    
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
# stud=Student("supriya","pune")
# print(stud.name)




# class Student:
#     def getData(self,name,city):
#         self.name=name
#         self.city=city
#     def display(self):
#         print("name:",self.name)
#         print("city:",self.city)
# s1=Student()
# s1.getData("Raj","Pune")
# s1.display()
# class Exam(Student):
#     pass
# e1=Exam()
# e1.getData("Ram","Mumbai")
# e1.display()




# class Animal:
#     def sound(self):
#         print("parent class")
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# d1=Dog()
# d1.sound()



# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# stud=Student("supriya",2)
# print(stud.name)
# stud2=Student("balode",5)
# print(stud2.roll)






# class Student:
#     def getData(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def Display(self):
#         print("NAme:",self.name)
#         print("marks:",self.marks)
# obj=Student()
# obj.getData("supriya",68)
# obj.Display()




# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def display(self):
#         print(self.name)
#         print(self.roll)
# class Exam(Student):
#     def __init__(self,name,roll,marks):
#         super().__init__(name,roll)
#         self.marks=marks
# obj=Exam("supriya",4,89)
# print(obj.name)
# obj1=Student()





# class Student:
#     def Data(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def display(self):
#         print("name:",self.name)
#         print("roll:",self.roll)
# class Exam(Student):
#     pass
# obj=Exam()
# obj.Data("supriya",4)
# obj.display()



# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# class Exam(Student):
    
#     def __init__(self,name,roll,marks):
#         super().__init__(name,roll)
#         self.marks=marks

# obj=Exam("supriya",5)
# print(obj.name)





# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# class Exam(Student):
    
#     def __init__(self,name,roll,marks):
#         super().__init__(name,roll)
#         self.marks=marks
# obj=Exam("supriya",4,77)
# print(obj.name)



# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# obj=Person("supriya",21)
# print(obj.name)
# print(obj.age)




# class Car:
#     def __init__(self,make,model):
#         self.make=make                  #instance attribute..
#         self.model=model
#     def display_info(self):
#         print("Make:",self.make)
#         print("model:",self.model)
# obj=Car("toyota","Innova")
# obj.display_info()




# class Book:
#     def __init__(self,title="Unknown",author="Unknown"):       #default values...
#         self.title=title
#         self.author=author
# book1=Book()
# print(book1.title)
# print(book1.author)
# book2=Book("python","abc")
# print(book2.title)
# print(book2.author)





# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#         self.area=self.calculate_area()
#     def calculate_area(self):
#         return self.width*self.height
# Rect1=Rectangle(2,4)
# print(Rect1.area)




# class Person:
#     def __init__(self):
#         print("parent class is created")

#     def __del__(self):
#         print("parent class deleted")
  
# person=Person() 
# del person
# class Student:
#     def __init__(self):
#         print("class is created")
#     def __del__(self):
#         print("class is deleted..")
# std=Student()
# del std




# class Std:
#     def __init__(self,name):
#         self.name=name
#         print(f"{self.name}")
#     def __del__(self):
#         print(f"class is deleted..{self.name}")
   
# std1=Std("supriya")
# del std1




# WRITE A PYTHON PROGRAM TAHT DEFINES A CAR CLASS WITH TWO CONSTRUCTORS ONE FOR SETTING MAKE AND MODEL,
# AND ANOTHER FOR SETTING MAKE,MODEL AND YEAR.

# class Car:
#     def __init__(self,make,model,year=None):
#         self.make=make
#         self.model=model
#         if year is not None:
#             self.year=year
#         else:
#             self.year="Not specified"
    
#     def Display(self):
#         print("make:",self.make)
#         print("model:",self.model)
#         print("year:",self.year)
        
# car=Car("toyoto","Innova")
# car.Display()
# car1=Car("toyoto1","Innova2",2020)




class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
    def Display(self):
        print(self.name)
        print(self.age)
        print(self.roll)
class Exam(Student):
    def marks(self,name,age,roll):
        super().__init__(name,age,roll)
        self.marks=79
std=Exam("supriya",21,56)
std.Display()
print(std.name)
