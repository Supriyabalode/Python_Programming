#WRITE A PROGRAM TO PRINT NUMBERS FROM 1 TO 10 USING WHILE LOOP.

# i=1
# while i<=10:
#     print(i)
#     i+=1





#WRITE A PROGRAM THAT TAKE NUMBER 100 AS INPUT AND CALCULATE SUM OF ALL INTEGERS FROM 1 TO 100 USING WHILE LOOP.

# i=1
# num=int(input("enter a number:"))
# sum=0
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)






# FACTORIAL OF NUMBER USING WHILE LOOP.

# fact=1
# i=1
# num=int(input("enter a num:"))
# while i<=num:
#     fact*=i
#     i+=1
# print(fact)




#WRITE A PROGRAM THAT USES FOR LOOP TO PRINT EVEN NUMBERS FROM 1 TO 100.


# for i in range(1,101):
#     if i%2==0:
#         print(i)





# PRINT MULTIPLICATION TABLE USING FOR LOOP.

# num=int(input("enter a number:"))
# for i in range(1,11):
#     print(num*i)


#WRITE A PROGRAM THAT USES FOR LOOP TO COUNT HOW MANY TIMES SPECIIC CHARACTER APPEAR IN THE STRING.

# string="supriya balode"
# char=input("enter a character:")
# count=0
# for c in string:
#     if c==char:
#         count+=1
# print(count)



#WRITE A PROGRAM THAT USES FOR LOOP COUNT NO OF VOWELS IN STRING.
# vowels="aeiouAEIOU"
# count=0
# string="supriya balode"
# for  i in string:
#     if i in vowels:
#         count+=1
# print(count)




#WRITE A PROGRAM THAT CALCULATE SUM OF EVEN NUMBERS FROM 1 TO 100.FOR LOOP TO ITERATE THROUGH THE NUMBERS AND 
# WHILE LOOP TO ACCUMULATE THE SUM.









#FIBONACCI SERIES.


# n=int(input("enter a number:"))
# num1=0
# num2=1
# next_num=num2
# count=1
# while count<=n:
#     print(next_num)
#     count+=1
#     next_num=num1+num2
#     num1,num2=num2,next_num





# n=5
# a=0
# b=1
# while a<=n:
#     print(a)
#     a,b=b,a+b





#MULTIPLIACTION MATRIX

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i*j:4}",end="   ")
#     print( )


#CHECK IF A NUMBER IS PRIME OR NOT using while loop.

# n=int(input("enter a number:"))
# isprime=True
# for i in range(2,n):
#     if n%i==0:
#         isprime=False
#         break
# if n==1:
#     print("not prime nor composite.")
# elif isprime==True:
#     print("prime")
# else:
#     print("not prime")




# n=int(input("enter a number:"))
# isprime=True
# i=2
# while i<n//2:
#     if n%i==0:
#         isprime=False
#         break
#     i+=1
# if n==1:
#     print("not prime nor composite.")
# elif isprime==True:
#     print("prime")
# else:
#     print("not prime")


# lst=[]
# n=10
# for j in range(1,n):
#     isprime=True

#     for i in range(2,j):
#         if j%i==0:
#             isprime=False
#             break
#     if j==1:
#         continue
#     elif isprime==True:
#         lst.append(j)
# print(lst)




n=10
for i in range(1,n):
    isPrime=True
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            isPrime=False
            break
    
    if isPrime==True:
        print(i)




# n=int(input("enter a number:"))
# isprime=True
# for i in range(2,n):
    
    
#     if n%i==0:
#         isprime=False
#         break
# if n==1:
#     print("number is not prime nor composite")
# elif isprime==True:
#     print(f"{n} is prime")
# else:
#     print(f"{n} is not prime")






n=50
for i in range(1,n):
    isprime=True
    for j in range(2,i):
        if i%j==0:
            isprime=False
            break
    if isprime==True:
        print(i)
    