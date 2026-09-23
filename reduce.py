# from functools import reduce
# def add(x,y):
#     return x+y
# numbers=[1,2,3,4,5]
# result=reduce(add,numbers)      
# print(result)




# from functools import reduce
# numbers=[1,2,3,4,5]
# result=reduce(lambda x,y:x+y,numbers)
# print(result)



# from functools import reduce
# n=5
# result=reduce(lambda x,y:x*y,range(1,n+1))
# print(result)


from functools import reduce
n=5
result=reduce(lambda x,y:x*y,range(1,n+1))
print(result)

