


# def addition(*args):
#     sum=0
#     for i in args:

#         sum=sum+i
#     return sum
# print(addition(1,2,3,4))
# print(addition(1,2))



# def mul(a):
#     mult=1
#     for i in a:
#         mult=mult*i
#     return mult
# list1=[1,3,2,4,5]
# print(mul(list1))



# def even(lst):
#     list2=[]
#     for i in lst:
#         if i%2==0:
#             list2.append(i)
#     return list2
# list1=[1,2,3,4,56,7,8]
# print(even(list(list1)))




# def abc(**kwargs):
#     for key,val in kwargs.items():
#         print(f"{key}:{val}")
# abc(name="supriya",age=21)
# abc(roll=2)






a=[1,2,3,4]
# b=map(lambda x:x**2,a)
# print(b)

b=filter(lambda x:x%2==0,a)
print(list(b))


a=[1,2,3,4,5]
b=sorted(a=lambda x:x)
print(b)







