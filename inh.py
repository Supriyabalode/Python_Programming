# HIERARCHICAL INHERITANCE......


# class Student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.marks=marks
#         self.roll=roll   
#     def Display(self):
#         print("name:",self.name)
#         print("roll:",self.roll)
#         print("marks:",self.marks)    
# class Personal(Student):   
    # def __init__(self,name,roll,marks):
    #     super().__init__(name,roll,marks)
# class Result(Student):
#     def __init__(self,name,roll,marks):
        
#         super().__init__(name,roll,marks)
#         super().Display()
#     def Display1(self):
#         print(f"{self.name} has {self.marks} marks")      
# result=Result("supriya",3,67)
# result.Display1()



# HYBRID INHERITENCE...

# class Student:
#     def __init__(self,name,roll,age,marks):
#         self.name=name
#         self.roll=roll
#         self.age=age
#         self.marks=marks
# class Personal_info(Student):
#     def __init__(self,marks):
#         super().__init__(marks)

# class Exam(Student):
    
#     def __init__(self,marks):
#         super().__init__(marks)
# class StudentInfo(Personal_info,Exam):
#     def __init__(self,name,roll,marks,age,):
#         Personal_info.__init__(self,name,roll,age)
#         Exam.__init__(self,marks)
# std=StudentInfo("supriya",34,55,6)
# print(std.marks)



# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age    
# class Personalinfo(Student):
#     def __init__(self,name,marks):
#         super().__init__(name,marks)
#     def Display(self):
#         print("name:",self.name)
# class Exam(Personalinfo):
#     def __init__(self,name,marks,roll):
#         super().__init__(name,marks)
#         self.roll=roll
#     def DisplayResult(self):
#         print("name:",self.name)
#         print("marks:",self.roll)
# e=Exam("supriya",34,3)
# e.DisplayResult()




#

# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# class Personal_info(Student):
#     def __init__(self,name,roll):
#         super().__init__(name,roll)
    
# class Std(Student):
#     def __init__(self,name,roll):
#         super().__init__(name,roll)
# class Exam(Personal_info,Std):
#     def __init__(self,name,roll,age):
#         Std.__init__(self,name,roll)
#         Personal_info.__init__(self,name,roll)
#         self.age=age
#     def Display(self):
#         print("name:",self.name)
# e1=Exam("supriya",21,78)
# e1.Display()




# class Personal_info:
#     def __init__(self):
#         self.name="supriya"
#         self.age=21
# class Result(Personal_info):
#     def __init__(self,marks):
#         super().__init__()
#         self.a=self.name
#         self.marks=marks
    
# result=Result(78)
# print(result.name)
# print(result.marks)
        



#multiple inheritance......

class Personal_info:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Marks(Personal_info):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    def Display(self):
        # self.n=self.name
        print(self.name)
m1=Marks("supriya",21,56)
m1.Display()
