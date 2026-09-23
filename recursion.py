
# FACTORIAL OF NUMBER USING RECURSION.
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=5
# print(factorial(n))



#FIBONACCI SERIES USING RECURSION.

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# num=int(input("enter a number:"))
# print(fibonacci(num))



# SUM OF ELEMENTS OF LIST USING RECURSION.

# def sum_of_list(lst):
#     if len(lst)==0:
#         return 0
#     else:
#         return lst[0]+sum_of_list(lst[1:])
# list1=[1,2,3,4,5]    
# print(sum_of_list(list1))




#CHECK STRING IS PALINDROME OR NOT

# def palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0]==s[-1]:
#         return palindrome(s[1:-1])
#     else:
#         return False
# s="racecar"
# print(palindrome(s))





# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))




# def palindrome(str1):
#     if len(str1)<=1:
#         return "palindrome"
#     if str1[0]==str1[-1]:
#         return palindrome(str1[1:1])
# print(palindrome("racecar"))





# def fact(n):
#     if n<=1:
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(5))



# def adds(lst):
#     if len(lst)==0:
#         return 0
#     else:
#         return lst[0]+adds(lst[1:])
# list1=[]
# print(adds(list1))




n=5
from functools import reduce
print(reduce(lambda a,b:a*b,range(1,n+1)))




