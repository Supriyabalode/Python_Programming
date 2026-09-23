# WE CAN STORE A FUNCTION IN VARIABLE...
# def fun1():
#     print("welcome to python")
# fun1()
# f1=fun1
# f1()





# WE CAN PASS FUNCTION AS A PARAMETER...
# def fun1():
#     print("function1 is called!!")
# def fun2(f1):
#     print("function 2 is called !!")
#     f1()
# fun2(fun1)




# def withdrawcash():
#     print("cash withdrawn successfully...")
# withdrawcash()
# def ATM(func):
#     def insidefn():
#         print("enter pin")
#         func()
#         print("print receipt")
#     return insidefn
# withdraw=ATM(withdrawcash)
# withdraw()




#  DECORATOR  USING ANNOTATION.....


def ATM(func):
    def insidefn():
        print("enter pin")
        func()
        print("print receipt")
    return insidefn
@ATM
def withdrawcash():
    print("cash withdrawn successfully...")
withdrawcash()




# def intro(func):
#     def wrapper(*args,**kwargs):
#         print("hii")
#         func(*args,**kwargs)
#         print("welcome to hefshine softwares...")
#     return wrapper
# @intro
# def sample(*args,**kwargs):
#     for data in args:
#         print(data)`1                     
#     for name,value in kwargs.items():
#         print(name,value)
# sample(10,20,name="abc",education="btech")




# import datetime
# def Scheduletask(func):
#     def wrapper():
#         hour1=datetime.datetime.now().hour
#         if hour1>=10 and hour1<=18:
#             func()
#             print(hour1)
#         else:
#             print("Time is over..")
#     return wrapper
# @Scheduletask
# def Runtask():
#     print("task running")
# Runtask()



# def ATM(func):
#     def insidefn():
#         print("enter a pin:")
#         func()
#         print("print reciept")
#     return insidefn
# @ATM
# def Withdraw():
#     print("cash withdrawn successfully........")
# Withdraw()





# def Add(func):
#     def insidefn(a,b):
#         print("a:",a)
#         func(a,b)
#         print("b",b)
#     return insidefn
# @Add
# def Sum(a,b):
#     print("addition:",a+b)
# Sum(2,3)




# def dec(func):
#     def insidefn(*args,**kwargs):
#         func(*args,**kwargs)
#         print("dictionary created successfully")
#     return insidefn
# @dec
# def dict1(*args,**kwargs):
#     for data in args:
#         print(data)
#     for key,value in kwargs.items():
#         print(key,value)
# dict1(1,2,3,name="supriya",age=21)




# PASSWORD VALIDATION.......

# import re
# def CheckEmail(data):
#     if re.search('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', data):
#         return True
#     else:
#         return False
# def ValidateCustomer(func):
#     def wrapper(customer):
#         if len(customer.Name)<=30 and CheckEmail(customer.Email):
#             func(customer)
#         else:
#             print("Not Saved - Validation Error")
#     return wrapper

# class Customer():
#     Name = None
#     Email = None
    
# cust = Customer()
# cust.Name = 'Deepak'
# cust.Email = 'deepak@gmail.com'

# @ValidateCustomer
# def SaveCustomer(customer):
#     print('Saved Data: Name:',customer.Name, 'Email:',customer.Email)
# SaveCustomer(cust)




def dec1(Abc):
    def wrapper():
        Abc()
        print("Hello")
    return wrapper

@dec1
def Ab():
    print("Hii")
Ab()