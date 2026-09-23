# *
# **
# ***

# for i in range(1,5):
#     print("*"*i)





#     *
#    **
#   ***
#  ****
# *****

# n=5
# for i in range(n):
#     print(" "*((n-i)-1),"*"*(i+1))





#   *
#  * *
# * * *

# n=5
# for i in range(n):
#     print(" "*((n-i)-1),"* "*(i+1))





# * * *
#  * *
#   *

# n=5
# for i in range(n):
#     print(" "*i+"* "*(n))
    




#    A
#   ABC
#  ABCDE

# n=3
# alph=65
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(alph+j),end=" ")
#     for j in range(i):
#         print(chr(alph+(i+j+1)),end=" ")
#     print()




# *
# @@
# ***
# @@@@
# *****

# def Pyramid(n):
#     for i in range(1,n+1):
#         if n%2==1:
#             print("*"*i)
#         else:
#             print("@"*i)
# n=int(input("enter a number:"))
# Pyramid(n)





# *
# @@
# ***
# @@@@
# *****


# n=5
# j=2
# for i in range(1,n+1):
#     if i%2==1:
#         print("*"*i)
#     else:
#         print("@"*i)





# *
# @@
# ***
# @@@@
# *****

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if i%2==0:
#             print("*",end="")
#         else:
#             print("@",end="")
#     print()




n=5
for i in range(n):
    print("*"*n)
    

    

