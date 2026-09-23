# NTH POWER USING LOOP.
# x=int(input("enter a number:"))
# n=int(input("enter a power:"))
# ans=1
# for i in range(1,n+1):
#     ans=ans*x
# print(f"{n} th power of {x} is:{ans}")




# x=int(input("enter a number:"))
# n=int(input("enter a power:"))
# ans=1
# while n>0:
#     ans=ans*x
#     n-=1
# print("nth power :",ans)


#COMMON ELEMENTS FROM TWO LISTS.

# list1=[1,2,3,4,5,6]
# list2=[1,2,8,9,5,6]
# common=[]
# for i in list1:
#     if i in list2:
#         common.append(i)
# print(common)



#PROGRAM THAT GENERATES AND PRINT FIRST 10 MULTIPLIES OF 5 USING FOR LOOP.
# n=5
# for i in range(1,11):
#     a=n*i
#     print(f"{n}x{i}",n*i)



#REVERSE THE DIGIT OF NO.
# num=int(input("enter a number:"))
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)





#PYRAMID pattern 1

# rows=int(input("enter no of rows:"))
# for i in range(1,rows+1):
#     print(" "*(rows-i)+"*"*(2*i-1))



#pyramid pattern 2
# rows=int(input("enter no of rows:"))
# for i in range(1,rows+1):
#     print(" "*(rows-1)+"*"*(2*i-1))




# num=int(input("enter a number:"))
# n=num
# reverse=0
# while num>0:
#     rem=num%10
#     reverse=reverse*10+rem
#     num=num//10

# if reverse==n:
#     print("palindrome.")
# else:
#     print("not palindrome.")




# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()





# for i in range(6):
#     for j in range(i+1):
#         print("*",end=" ")
#     print( )



# n=int(input("enter a number:"))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print( )



# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()






# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()




# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()



# NTH POWER USING LOOP.

# num=int(input("enter a number:"))
# pow=3
# a=1
# for i in range(1,pow+1):
#     a=a*num
# print(a)




# num=int(input("enter a number:"))
# power=int(input("enter a power:"))
# a=1
# for i in range(1,power+1):
#     a=a*num
# print(a)





# nth power
# n=5
# pow=3
# a=1
# for i in range(1,pow+1):
#     a=a*n
# print(a)


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

    