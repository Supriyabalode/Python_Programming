# class Student:
#     school_name = "ABC School"  # Class variable

#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name

# s1=Student()
# s1.change_school("XYZ School")

# print(s1.school_name)  # Output: XYZ School









# class School:
#     school_name = "Greenwood High"  # Class variable

#     @classmethod
#     def show_school_name(cls):
#         print("School name is:", cls.school_name)

# # Call the class method
# School.show_school_name()




class Abc: 
    name="supriya"             # class atribute
    def Std(self):
        print(self.name)
   
    @classmethod
    def Student(cls):               #class method
        return cls.name
a=Abc()
print(a.Student())
a.Std()



