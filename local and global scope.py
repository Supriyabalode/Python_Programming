# a=10             # global variable
# def Abc():
#     a=20
#              # local
# print(a)


# a=20
# def fun1():
#     a=10
#     print(a)             # it check first for local variable ,if there no local var then only checks for global var
# fun1()

# a=20
# def fun1():
#     print(a)
# fun1()


# def fun2():
#     a=20
#     def fun3():
#         print(a)
# fun2()                        # no output.....



# def fun2():
#     a=20
#     def fun3():
#         print(a)
#     fun3()
# fun2()


# a=20
# def fun1():
#     a=15
#     print(a)
# print(a)
# fun1()



# a=10
# def fun1():
#     a=11
#     def fun2():
#         print(a)
#     fun2()                  
# fun1()



# def display():
#     def show():
#         print("hello")
# show()              # it will give error because show function has local scope.



# def display():
#     def show():
#         print("hello")
#     show()
# display()




# a,b=10,20
# def fun1():
   
#     if b>a:
#         c=a+b   
# print(c)                               # NameError : name c is not defined..
