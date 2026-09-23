# def greet():              #FUNCTION DEFINITION
#     print("welcome")
# greet()                    # FUNCTION CALL





# def add():
#     a=10
#     b=20
#     c=a+b
#     return c
# ans=add()
# print("addition:",ans)




# def add(a,b):
#     print("a:",a)
#     print("b:",b)
#     c=a+b
#     print("addition:",c)

# add(120,20)


# def even_odd():
#     num=int(input("enter a number:"))
#     if num%2==0:
#         print("number is even")
#     else:
#         print("number is odd")
# even_odd()




# WRITE A FUNCTION COMPARE() TO COMPARE TWO INTEGERS.USE ONLY ARGUMENT.

# def compare(a,b):
#     if a>b:
#         print("a is greater.")
#     elif b>a:
#         print("b is greater.")
#     else:
#         print("both are same.")
# m=int(input("enter a number:"))
# n=int(input("enter a number:"))
# compare(m,n)




# def compare():
#     a=10
#     b=20
#     if a>b:
#         return "a is greater."
#     elif b>a:
#         return "b is greater."
#     else:
#         return "both are same."
# a=compare()
# print(a)



# def sum():
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     addition=a+b
#     return addition
# a=sum()
# print("addition:",a)



# def compare(a,b):
#     if a>b:
#         return "a is greater."
#     elif b>a:
#         return "b is greater."
#     else:
#         return "both are equal."
# m=int(input("enter a number:"))
# n=int(input("enter a number:"))
# compare(m,n)
# print(compare(m,n))



#factorial of number using function.USE RETURN.

# def fact():
#     num=int(input("enter a number:"))
#     fact1=1
#     for i in range(1,num+1):
#         fact1=fact1*i
#     return fact1
# a=fact()
# print(a)



#FACTORIAL OF NUMBER.USE ONLY ARGUMENTS

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print("facrorial of number:",fact)
# m=int(input("enter a number:"))
# factorial(m)






# def fact(n):
#     facto=1
#     for i in range(1,n+1):
#         facto=facto*i
#     return facto
# m=int(input("enter a number:"))
# a=fact(m)
# print("factorial:",a)








# AREA OF CIRCLE using return.
# def area():
#     r=int(input("enter a radius:"))
#     areaa=3.14*r*r
#     return areaa
# print("area of circle:",area())


#area of circle using argument.

# def area(r):
#     ar=3.14*r*r
#     print("area of circle:",ar)
# r=int(input("enter a radius:"))
# area(r)



#AREA OF CIRCLE USING RETURN AND ARGUMENT.

# def area(r):
#     ar=3.14*r*r
#     return ar
# r=int(input("enter a radius:"))
# area(r)
# print(area(r))




# def even():   
#     start=int(input("enter a start value:"))
#     end=int(input("enter a end value:"))
#     list1=[]
#     for i in range(start,end+1,):
#         if i%2==0:
#             return i
# a=even()
# print("even no:",a)




# def even(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)
            
# start=int(input("enter start value:"))
# end=int(input("enter end value:"))
# even(start,end)






# def n():
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     if a>b:
#         return "a is greater."
#     elif b>a:
#         return "b is greater."
#     else:
#         return "both ara are same."
# print(n())




# def sum_of_two(a,b):
#     c=a+b
#     return c
# print("addition:",sum_of_two(5,7))



# def multiply(a,b=2):
#     c=a*b
#     print("multiplication:",c)
# multiply(2,3)            #positional arguments
# multiply(2)
# multiply(b=2,a=3)          #keyword arguments.


# DEFINE A FUNCTION get_sq(num)


# def get_square(num):
#     square=num*num
#     return square

# print(get_square(5))




# def concatanate_str(str1,str2):
#     str3=str1+str2
#     return str3
# print(concatanate_str("hello","world"))




# def pet(animal_type,pet_name):
#     print(f"I have a pet {animal_type} named {pet_name}")
# pet("dog","rover")






# N NO. OF POSITIONAL ARGUMENTS.
# def sum_all(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
        
#     print("sum:",sum)
# sum_all(2)
# sum_all(2,3,4)
# sum_all(1,2,3,4,5,6)           



# def min_max(*nums):
#     a=min(nums)
#     b=max(nums)
#     return a,b
# print(min_max(1,2,3,4,5,6,7))




#n NO. OF KEYWORD ARGS.

# def display(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# display(name="supriya")
# display(name="supriya",age=21)



# def mult(a,b):
#     c=a*b
#     return c
# print(mult(5,10))



# def square(args):
#     square=[]
#     for i in args:
#         sq=i*i
#         square.append(sq)
#     print(square)
# list1=[1,2,3,4,5]
# square(list1)




# def even():
#     list1=[1,2,3,4,5,6]
#     list2=[]
#     for i in list1:
#         if i%2==0:
#             list1.append(i)            
# even()





# def even(lst):
#     list1=[]
#     for i in lst:
#         if i%2==0:
#             list1.append(i)
#     return list1
# a=[1,2,3,4,5,6]
# print(even(a))



# def Abc(name,age):
#     print(f"my name is {name} and age is{age}")
# Abc(name="supriya",age=21)




def Abc(lst):
    a=max(lst)
    b=min(lst)
    return a,b
print(Abc([1,2,3,4,5]))


