# no is divesible by 5 and 11


# def div(a):
#     if a%5==0 and a%11==0:
#         return "number is divisible by 5 and 11 "
#     else:
#         return "number is not  divisible by 5 and 11"
# n=int(input("enter a number:"))
# print(div(n))



# sum of n no of arguments.

# def add(*args):                        #n no of positional arguments
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(5)
# add(1,2,3,4,5)
# add(1,2,3,4,5,6,7,8)



# def display(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# display(name="supriya")
# display(name="supriya",age=21)





# def even(a):
#     list2=[]
#     for i in a:        
#         if i%2==0:
#             list2.append(i)
#     return list2
# list1=[1,2,34,5,6]
# print(even(list1))





# def prime():
#     isprime=True
#     n=int(input("enter a number:"))
#     for i in range(2,n):
#         if n%i==0:
#             isprime=False
#     if n==1:
#         print("number is not prime not composite.")
#     elif isprime==True:
#         print("number is prime.")
#     else:
#         print("number is not prime.")
# prime()



# def prime(n):
#     isprime=True

#     for i in range(2,n):
#         if n%i==0:
#             isprime=False
#     if n==1:
#         return "number is not prime not composite."
#     elif isprime==True:
#         return "number is prime."
#     else:
#         return "number is not prime."
# n=int(input("enter a number:"))
# print(prime(n))




# def student(**kwargs):
#     for key,val in kwargs.items():
#         print(f"{key}:{val}")
# student(name="supriya")
# student(name="supriya",age=21)





# n=2
# isprime=True
# for i in range(2,n):
#     if n%i==0:
#         isprime=False
#         break
# if n==1:
#     print("Number is not prime nor composite.")
# elif isprime==False:
#     print("Number is not prime")
# else:
#     print("Number is prime")



# for i in range(2,51):
    
#     isprime=True
#     for j in range(2,i):
#         if i%j==0:    
#             isprime=False
#     if isprime==True:
#         print(i)  
             









#  Addition od digits from number.
# n=123
# add=0
# while n>0:
#     rem=n%10
#     add=add+rem
#     n=n//10
# print(add)


# reverse the digits of number.
# n=123
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print(rev)



# Find number is armstrong or not
# n=153
# num=n
# s=0
# while n>0:
#     rem=n%10
#     s=s+(rem**3)
    
#     n=n//10
# if s==num:
#     print("Armstrong number")
# else:
#     print("Not Armstrong")



# str="listen"
# str2="silent"
# s1=sorted(str)
# s2=sorted(str2)
# s11="".join(s1)
# s22="".join(s2)
# if s11==s22:
#     print("String is Anagram")
# else:
#     print("String is not anagram")



# str1="listen"
# str2="silent"
# a=sorted(str1.lower())
# b=sorted(str2.lower())
# a1="".join(a)
# b1="".join(b)
# if a1==b1:
#     print("String is an anagram")
# else:
#     print("not an anagram")


# find largest palindrome from the string
# str1="abcba"
# s=""    
# for i in range(len(str1)):
#     for j in range(i+1,len(str1)):
#         part=str1[i:j+1]
#         if part==part[::-1]:
#             if len(part)>len(s):
#                 s=part
# print(s)
# 
# 
# 
# 
# 
#                                        
