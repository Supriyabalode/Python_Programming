# LIST COMPREHENSION- list comprehension offers a shorter syntax when you want to create a new list based
# on the values of an existing list.




# list1=[12,23,45,56,67,84,90,32]
# list2=[]
# for i in list1:
#     a=i*3
#     list2.append(a)
# print(list2)


#OR

# list1=[12,23,45,56,67,84,90,32]
# list2=[i*3 for i in list1]                             #LIST COMPREHENSION...
# print(list2)





#STORE NUMBERS GREATER THAN 30 IN DIFFERENTLIST USING LIST COMPREHENSION..

# list1=[12,23,34,54,21,45,10]
# list2=[i for i in list1 if i>30]
# print(list2)


#DISPLAY ODD NO USING LIST COMPREHENSION...

# list1=[12,23,34,54,21,45,10]
# list2=[i for i in list1 if i%2!=0]        
# print(list2)



# list1=[1,2,3,5,6,7]
# list2=[2,3,4,5,6]
# list3=[i*j for i in list1 for j in list2]
# print(list3)


# set1={1,2,3,4}
# set1.discard(5)
# print(set1)




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
#     print(" "*((n-i)-1),"* "*i)



# n=5
# for i in range(n):
#     print(" "*i+"* "*(n-i))



