# *****
# *****
# *****
# *****
# *****

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()




# *
# **
# ***
# ****
# *****

# n=int(input("enter a number:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print( )




#     *
#    **
#   ***
#  ****
# *****

# n=5
# for i in range(n):
#     for j in range((n-i)-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# *****
# ****
# ***
# **
# *

# n=int(input("enter a number:"))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()




# *****
#  ****
#   ***
#    **
#     *

# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()



#    *
#   ***
#  *****

# n=3
# for i in range(n):
#     for j in range((n-i)-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print( )




# *****
#  ***
#   *

# n=3
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range((n-i)-1):
#         print("*",end=" ")
#     print( )





#     *    
#    * *   
#   * * *  
        

# n=3
# for i in range(n):
#     for j in range((n-i)-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         if (i+j)%2==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         print()




#  *****
#   ***
#    *

# n=3
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range((n-i)-1):
#         print("*",end=" ")
#     print( )



# 1
# 1 2
# 1 2 3
# 1 2 3 4

# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()


    

# 1
# 2 2
# 3 3 3
# 4 4 4 4


# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()







# *****
#  ****
#   ***
#    **
#     *

# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print("*",end=" ")
#     print()








#     *  
#    **   
#   ***    
#  ****     
# *****      


# n=5
# for i in range(n):
#     for j in range((n-i-1)):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()





# A
# AB
# ABC
# ABCD


# n=4
# alph=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(alph+j),end=" ")
#     print()




#      *
#     ***
#    *****
#     ***
#      *

# n=3
# m=2
# for i in range(n):
#     for j in range((n-i)-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#         if i>=4:
#             print("")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(m):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(m-i):
#         print("*",end=" ")
#     for j in range((m-i)-1):
#         print("*",end=" ")
#     print() 
# 
#    





    #   *
    #  * *
    # * * * 

# n=3
# for i in range(n):
#     for j in range((n-i)):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("* ",end=" ")
#     print()




#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *  

# n=3
# m=2
# for i in range(n):
#     for j in range((n-i)):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("* ",end=" ")
#     print()
# for i in range(m):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range():
#         print("* ",end=" ")
#     print( )




#     *
#    * *
#   * * *

# n=3
# for i in range(n):
#     print(" "*((n-i)-1),"* "*(i+1))




# * * *
#  * *
#   *

# n=3
# for i in range(n):
#     print(" "*i,"* "*(n-i))





#     *
#    * *
#   * * *
#    * *
#     *

# n=3
# m=2
# for i in range(n):
#     print(" "*((n-i)-1),"* "*(i+1))
# for i in range(m):
#     print(" "*(i+1),"* "*(m-i))


#OR 



# n=int(input("enter a number:"))
# for i in range(n):
#     for j in range((n-i)-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("* ",end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range((n-i)-1):
#         print("* ",end=" ")
#     print()



# A
# BB
# CCC
# DDDD

# n=int(input("enter a number:"))
# asc=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(asc+i),end=" ")
#     print()




# A
# BC
# DEF

# n=int(input("enter a number:"))
# asc=65

# for i in range(n):
#     for j in range(i+1):
#         alphabets=chr(asc)
#         print(alphabets,end=" ")
#         asc+=1    
#     print()
    


# n=int(input("enter a number:"))
# asc=75

# for i in range(n):
#     for j in range(i+1):
#         alphabets=chr(asc)
#         print(alphabets,end=" ")
#         asc+=1    
#     print()



# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i*j:4}",end=" ")
#     print()



# 11111
# 22222
# 33333
# 44444
# 55555

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()



#   *
#  ***
# *****


# n=3
# for i in range(n):
#     for j in range((n-i)-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()









# s="ababc"
# largest=""
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         part=s[i:j]
#         if part==part[::-1]:
#             if len(part)>len(largest):
#                 largest=part
# print(largest)




#    *****
#     ***
#      *


# n=3
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end="")
#     for j in range((n-i)-1):
#         print("*",end="")
#     print()



# *****
# *   *
# *****
# *   *
# *****


n=5
for i in range(n):
    for j in range(n):
        if i%2==0:
            print("*",end="")
        elif i%2!=0 and (j==0 or j==(n-1)):
            print("*",end="")
        else:
            print(" ",end="")
    print()

