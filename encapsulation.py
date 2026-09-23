# class Car:
#     def __init__(self,brand):
#         self.brand=brand                          #public attribute.......
#     def get_brand(self):
#         return self.brand
# car=Car("toyota")
# print(car.brand)
# print(car.get_brand())



class Person:
    def __init__(self,age):
        self._age=age
    def get_age(self):
        return self._age
class Student(Person):
    def __init__(self,name,age):
        super().__init__(age)
        self.name=name
    def display_info(self):
        return f"student {self.name} is {self._age} years"
std=Student("supriya",21)
person=Person(21)
print(person.get_age())
print(std.display_info())




# class Account:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#         else:
#             print("deposit amount must positive")
#     def get_balance(self):
#         return self.__balance        
# acc=Account(2000)
# acc.deposit(500)
# print(f"current balance: {acc.get_balance()}")




# class Student:
#     def __init__(self,age):
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         if age>=0:
#             self.__age=age
#         else:
#             print("age cannot be negative")
# std=Student(21)
# print(f"students age:{std.get_age()}")

