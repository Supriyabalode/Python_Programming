# list1=[10,34,78,90,45,10,122]

#ADD ELEMENT IN THE LAST POSITION.

#list1.append(90)
# #print(list1)



#ADD ELEMENT AT SPECIFIC POSITION.

# list1.insert(2,5)              
# print(list1)

#DELETE LAST ELEMENT.

# list1.pop()
# print(list1)


#TO REMOVE SPECIFIC ELEMENT.

# list1.remove(78)
# print(list1)



#SORT LIST.

# list1.sort()
# print(list1)




#COUNT.

# print(list1.count(10))



#TO KNOW THE INDEX.

# print(list1.index(10))




# listc=[10,5,89,9,7]
# listc.clear()
# print(listc)



# list3=[17,34,56,34,5,6]
# list2=[10,2,4,3,5]
# list3.extend(list2)
# print(list3)



# import keyword
# print(keyword.kwlist)



#create string of your introduction.
# introduction="my name is supriya dattatraya balode.\tI am from sangamner"
# print(introduction)
# print(type(introduction))

# name="supriya"
# surname="balode"
# print(name+surname)
# print(name+" "+surname)


# student="senior"
# print(student*2)

# str1=str(input("enter a string:"))
# print("first letter:",str1[0])
# print("last letter:",str1[-1])


#print the string in reverse order.

# str1.reverse()
# print(str1)

# rev=str1[::-2]
# print(rev)

#print(str1[0:5])
# str1="hefshine"

# print(str1[-1:-5:-1])
# print(str1[-4:-1])
# print(str1[-1::-1])


#print(str1[2:])




# list1=[12,34,23,45,56,67,90]
# list1.append(10)
# print(list1)

# list1.insert(2,10)
# print(list1)

# list1.pop()
# print(list1)



# list1.remove(90)
# print(list1)

# print(list1.index(10))

# print(len(list1))


# print(list1[::-1])

# list1.reverse()
# print(list1)
# list1.reverse()
# print(list1)

 


#add multiple elements in list.
# a=[90,80,70,60]
# list1.extend(a)
# print(list1)




#COPY LIST INTO ANOTHER LIST.
# mylist=list1.copy()
# print(mylist)

# list2=[6,5,9,50,43,90,20,30]
# print(list2[:3])
# print(list2[-1:-8:-1])
# print(list2[::-1])


# print(list2[0:])

# print(list2[:2])



# list1=[2,4,5,8,9,1,5,9]
# print(list1)
# list1.append(10)
# print(list1)                                                                                
# list1.insert(2,10)
# print(list1)
# list2=[10,20,30]
# list1.extend(list2)
# print(list1)
# list1.pop()
# print(list1)
# list1.remove(10)
# print(list1)





# print("max element:",max(list1))
# print("min element:",min(list1))
# print("length of list:",len(list1))
# print("count:",list1.count(4))
# print("index:",list1.index(1))





# lista=[10,20,45,23,33,67,10,5]
# print(lista[1:])
# print(lista[-1::-1])





# list1=[3,9,6,7,4,2,8]
# list1.sort()
# print(list1)
# print(list1[2])


# print(list1.index(7))
# list1.sort()
# print("sorted list:",list1)




#NESTED LIST.......

# lst=[[1,2,3,4,5],["a","abc","abcd"]]
# print(lst[1][2])






# list1=[1,2,3,4,5,6,7,8,9,10]
# num=int(input("enetr a number:"))
# if num in list1:
#     print(f"{num} is present at position ",list1.index(num))
# else:
#     print("not present")


# list1=[1,2,3,4,5,6,7,8,9]
# count=False
# element=int(input("enter element:"))
# for i in list1:
#     if i==element:
#         count=True
#         break
# if count==True:
#     print(f"{element} is present at position {list1.index(element)}")
# else:
#     print("element is not present")




# lst=[1,2,3,4]
# lst2=lst
# lst2[0]=6
# print(lst)




# list1=[10,20,50,60,70]
# for i in list1:
#     if i>50:
#         print(i)
#         break



# n=int(input("enter a number:"))
# total=0
# while n>0:
#     rem=n%10
#     total+=rem
#     n=n//10
# print(total)

# a="listen"
# lst=[]
# lst1=["silent","lst","netsil"]
# for i in lst1:
#     if sorted(i)==sorted(a):
#         lst.append(i)
# print(lst)


# prime number...

# isprime=True
# for i in range(2,100):
#     for j in range(2,100):
#         if i%j==0:
#             isprime=False
#     if isprime==True:
#         print(i)



lst1=[1,2,3,4,5]
lst1.insert(0,9)
lst1[0]=10
print(lst1)