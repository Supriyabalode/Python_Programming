# for i in range(1,11):
#     print(i)


# i=1
# while i<=100:
#     print(i)
#     i+=1



# list=[10,20,30,40,50,60]
# for i in list:
#      print(i) 


# mylist=[10,20,30,45,40,50,60]
# index=0
# while index<len(mylist):
#     print(mylist[index])
#     index+=1


# list1=[10,20,30,40,50,60]
# for i in range(0,len(list1)):
#     print(list1[i])


# list2=[10,20,30,40,50,60]
# for i,val in enumerate(list2):
#     print(i,val)



# tup1=(10,20,30,45)
# i=0
# while i<len(tup1):
#     print(tup1[i])
#     i+=1


# tup1=(10,20,30,45)
# for i in range(0,len(tup1),1):
#     print(tup1[i])
    



# str1="hefshine"
# i=0
# for i in range(len(str1)):
#     print(str1[i])



# str2="hefshine"
# i=0
# while i<len(str2):
#     print(str2[i])
#     i+=1



# set1={10,20,30,40}

# for i in set1:
#     print(i)


# while i in set1:
#     print(i)



# dict1={1:"a",2:"b",3:"c"}

# for key,val in dict1.items():
#     print(key,val)

    


# dict1={1:"a",2:"b",3:"c"}













# fruits=["Apple","banana","Apple","banana","guava"]
# dict1={}
# for fruit in fruits:
#     dict1[fruit]=fruits.count(fruit)
# print(dict1)



# s="ababc"
# largest=""
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         part=s[i:j]
#         if part==part[::-1]:
#             if len(part)>len(largest):
#                 largest=part
# print(largest)



# s="abacaca"
# longest=""
# for i in range(len(s)):                           
                                                   
#     for j in range(i+1,len(s)+1):
#         part=s[i:j]
#         if part==part[::-1]:
#             if len(part)>len(longest):
#                 longest=part
# print("Largest palindrome:",longest)




n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)



n=5
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)
