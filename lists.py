# list1=[1,12.23,True,23+45j,"python"]
# print(list1)

# print(list1[3])
#          
# list1[2]=10       #replace  value.
# print(list1)


# list1.append(20)       #add element at end of the list.
# print(list1)


# list1.insert(2,"abc")      #insert ele at specific position
# print(list1)


# list1.extend([2,67,89,90])    #insert multiple elements at end of list.
# print(list1)


# list1.pop()      #remove last ele. from list.

# list1.pop(4)       #remove element of specific position.

# list1.remove(2)     #remove specific element 

# del list1      # delete whole list
# list1=[10,23,7,9,90,45,3]
# del list1[3]       #remove element from the specific index.
# print(list1)

# list1.clear()    #delete list.

# list2=[]
# list2=list1.copy()
# print(list2)


# list1.sort()
# print(list1)

# list1.sort(reverse=True)
# print(list1)






# list1=[10,20,30,23,54,45,34]
# print(list1)







#create list of fruits,and append another fruit in list.

# fruits=["apple","banana","mango"]
# fruits.append("guava")
# print(fruits)




#create list of colors and remove third item from list.

# colors=["red","pink","green","yellow","blue"]
# print(colors)
# colors.pop(2)
# print(colors)



#find max and min.

# list1=[10,45,34,67,90,2,1,4]
# print(max(list1))
# print(min(list1))



#replace second number

# list1=[20,34,67,80,22,12]
# list1[1]=10
# print("updated list:",list1)


#insert 100 at second position.

# list2=[10,20,32,43,90,23]
# list2.insert(1,100)
# print(list2)



#concatenate two lists.

# list1=[20,34,67,80,22,12]
# list2=[99,34,67,32]
# print(list1+list2)



#remove duplicate elements.

# list1=[10,20,34,54,67,20,32,32,45,34,45]
# a=set(list1)
# print(a)
# final1=list(a)
# print(final1)






#write a program that takes a value finds its index,if the value is not in list return -1.

# list1=[10,20,30,45,54,65,75]
# value=int(input("enter a element to find index:"))
# if value in list1:
#     print("index:",list1.index(value))
# else:
#     print("-1")   





# list1=[1,23,34,45,65,78,89,0,65,43]
# print(list1[0:5])
# print(list1[5:10])
# print(list1[:6])
# print(list1[6:])
# print(list1[::1])
# print(list1[::2])
# print(list1[2:7:3])
# print(list1[::-1])
# print(list1[-5:-8:-1])

#CREATE A LLIST  AND THEN COPY IT INTO ANOTHER LIST.MODIFY THE COPIED LIST AND PRINT BOTH LIST TO VERIFY
#THEY ARE INDEPENDENT.

# list1=[10,34,45,60,2,1,12]
# print("list1:",list1)
# list2=list1.copy()
# print("list2:",list2)
# list2.append(10) 
# print(list2)
# print(list1)
# list2.clear()
# print(list2)

# WRITE A PYTHON PROGRAM GENERATES ALL SUBSETS (POWER SET) OF A GIVEN LIST OF   ELements.




# a=[2,3,4,9,5]
# a.clear()
# print(a)


# list1=[1,2,3,4,5]
# list2=list1
# list2.append(10)
# print(list1)
# print(list1 is list2)

# list1=[1,2,3]
# list2=list1
# list1.append(10)
# print(list2)








# lst=[2,1,5,9,6,8]
# large=lst[0]
# small=lst[0]

# for i in lst:
#     if i>large:
#         large=i
#     if i<small:
#         small=i
# print("large:",large)
# print("small:",small)


# lst=[2,3,4,5,1,8,6]
# small=lst[0]
# large=lst[0]
# for i in lst:
#     if i<small:
#         small=i
#     if i>large:
#         large=i
# print("small:",small)
# print("large:",large)










lst1=[10,20,30,40,50,50,60,45,78,90,100,15,25,35,45,10,20]
# for i in lst1:
#     if i>=20 and i<=50:
#         print(i)



# count=0
# for i in lst1:
#     if lst1.count(i)>1:
#         count+=1
# print(count)



# num=100
# for i in lst1:
#     if i==num:
#         a=lst1.index(i)

#         lst1.insert(a,1000)
# print(lst1) 


a=10
print(id(a))
a=30
print(id(a))