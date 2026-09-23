# def GenFun():
#     yield 10
#     yield 20
#     yield 30
# g=GenFun()
# print(next(g))
# print(next(g))
# print(next(g))



# def ConvertToGen(anylist):
#     for data in anylist:
#         yield data
# list1=[1,2,3,4,5,6]
# g1=ConvertToGen(list1)
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))


# my_list=[1,3,4,5,6,7]
# list1=[x**1 for x in my_list]
# print(list1)
# a=(x**2 for x in my_list)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# def GenSequence(start,end):
#     counter=start
#     while counter<=end:
#         yield counter
#         counter=counter+1
# g3=GenSequence(100,1000)
# print(next(g3))
# print(next(g3))
# print(next(g3))
# print(next(g3))
# print(next(g3))
# print(next(g3))


# CREATE MULTIPLCATION TABLE USING GENERATOR FUNCTION.READ NUMER FROM USER.


# def genTable(num):
#     for i in range(1,11):
#         yield num*i
# num=int(input("enter a number:"))
# g=genTable(num)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))



# def Num():
#     for i in range(1,11):
#         yield i
# a=Num()
# print(next(a))
# print(next(a))
