# salary=[10000,20000,300000,543333,566777,89000,9000,80000,70000]
# print(salary[4:8])

# list1=[10,20,30,40,50,60,70,10000]
# print(sum(list1)/len(list1))


# dict3={"student1":{"id":1,"name":"supriya","age":21,"course":"data science","fees":35000},
#        "student2":{"id":2,"name":"raj","age":21,"course":"python","fees":30000},
#        "student3":{"id":3,"name":"kiran","age":29,"course":"data science","fees":35000},
#        "student4":{"id":4,"name":"mohan","age":31,"course":"java","fees":45000},
#        "student5":{"id":5,"name":"raj","age":21,"course":"data science","fees":35000}}
# print(dict3)


dict4=[{"id":1,"name":"supriya","age":21,"course":"data science","fees":35000},
{"id":2,"name":"raj","age":21,"course":"python","fees":30000},
{"id":3,"name":"kiran","age":29,"course":"data science","fees":35000},
{"id":4,"name":"mohan","age":31,"course":"java","fees":45000},
{"id":5,"name":"raj","age":21,"course":"data science","fees":35000}]
# print(dict4)


# max=0
# for i in dict4:
#     if i.get("age")>0:
#         max=i.get("age")
# print(max)




# max=0
# for x in dict4:
#     if x.get("age")>max:
#         max=x.get("age")
# print(max)


# min=50
# for x in dict4:
#     if x.get("age")<min:
#         min=x.get("age")
# print(min)




# lst1=[1,2,3,4,5]
# lst2=lst1.copy()
# print(lst2)
# lst2.append(6)
# print(lst1)


# lst1=[[1,2],[3,4]]
# lst2=lst1.copy()
# lst2[0][0]=7
# print(lst1)

# import copy
# lst1=[[1,2],[3,4]]
# lst2=copy.deepcopy(lst1)
# lst2[0][0]=7
# print(lst1)


# lst=[23,45,78,11,89,56,90,78]
# max=0
# for i in lst:
#     if i>max:
#         max=i
# print(max)


# min=lst[0]
# for i in lst:
#     if i<min:
#         min=i
# print("Minimum element:",min)





# str1="abcbd"

# s=str1
# for i in range(len(str1)):
#     for j in range(i+1,len(str1)+1):
#         part=str1[i:j]
#         if part==part[::-1]:
#                 if len(part)<len(s):
#                     s=part
# print(s)





# str1="abab"    
# s=""
# for i in range(len(str1)):         
#     for j in range(i+1,len(str1)+1):
#         part=str1[i:j]
#         if part==part[::-1]:
#             if len(part)>len(s):
#                 s=part
# print(s)


# from functools import reduce
# n=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,n)
# print(result)



from functools import reduce
n=5
result=reduce(lambda a,b:a*b,range(1,n+1))
print(result)
