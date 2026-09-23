# while True:                                    #CONTINOUS LOOP.
#     n=int(input("enter a number"))
#     if n%7==0:
#         break
# print("number is found.")



# for i in range(1,20):
#     if i%2==0:
#         continue
#     print(i)



# i=1
# while i<=30:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1




#PRINT PRIME NUMBERS BETWEEN 1 TO 100

# for n in range(1,101):
#     isprime=True
#     for i in range(2,n):
#         if n%i==0:
#             isprime=False
#             continue
#     if n==1:
#         continue
#     elif isprime==True:
#         print(n)
#     else:
#         continue
            


#OR

# for n in range(1,101):
#     isprime=True
#     for i in range(2,n):
#         if n%i==0:
#             isprime=False
#         if n==1:
#             continue
#     if isprime==True:
#         print(n)




#WRITE A PYTHON PROGRAM THAT ITERATES THROUGH A LIST OF INTEGERS AND PRINT ALL POSITIVE NUMBERS ,
# SKIPPING NEGATIVE NUMBER USING continue.



# list1=[-1,3,4,-9,8,-6,5,-10]
# for i in list1:
#     if i<0:
#         continue
#     print(i)



# WRITE A PYTHON PROGRAM THAT USES A WHILE LOOP TO CHECK IF A NUMBER IS DIVISIBLE BY 7.IF IT IS,BREAK LOOP AND PRINT FOUND.
# OTHERWISE KEEP CHECKING UNTIL YOU FIND IT.

# while True:
#     n=int(input("enter a number:"))
#     if n%7==0:
#         print("number is found")
#         break




#WRITE A PYTHON PROGRAM THAT CHECKS IF A NUMBER IS POSITIVE,NEGATIVE OR ZERO.IF A NUMBER IS POSITIVE,DO NOTHING USING PASS.
# FOR NEGATIVE NUMBERS PRINT NEGATIVE AND FOR ZERO PRINT ZERO.

# n=int(input("enter a number:"))
# if n>0:
#     pass
# elif n<0:
#     print("negative")
# else:
#     print("zero.")






#WRITE A PROGRAM THAT ITERATES OVER THE NUMBER FROM 1 TO 100.THE PROGRAM SHOULD PRINT THE FIRST NUMBER THAT IS DIVISIBLE BY 5 AND 7,
# AND THEN BREAK THE LOOP

# for i in range(1,101):
#     if i%5==0 and i%7==0:
#         print(i)
#         break






# WRITE A PYTHON PROGRAM THAT READS A LIST OF NUMBERS EXIST THE LOOP AS SOON AS IT ENCOUNTERS THE FIRST NUMBER GREATER THAN 50.
# PRINT THE NUMBER AND BREAK THE LOOP.

# count=0
# list1=[10,2,3,4,5,67,8,51,67]
# for i in list1:
#     if i>50:
#         print(i)
#         break

        





#SQUARE PATTERN OF STARS.

# n=5
# for i in range(n):
#     for j in range(n):
#         print(f"*",end=" ")
#     print()


