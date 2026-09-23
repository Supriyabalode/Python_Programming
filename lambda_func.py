# IN PYTHON WE CAN USE LAMBDA FUNCTION TO CREATE SMALL,ANONYMOUS FUNCTIONS THAT ARE USEFULL FOR SHORT TASKS.
# LAMBDA FUNCTION TAKE ANY NO OF ARGUMENTS ,BUT CAN ONLY HAVE ONE EXPRESSION.

#map-map function applies a function to each item in an iterable.
#filter-used to filter out the elements based on conditions.



# product=lambda x,y:x*y
# result=product(5,10)
# print(result)




# list1=[1,2,3,4]
# a=map(lambda x:x**2,list1)
# print(list(a))



# list2=[1,2,3,4,5,6]
# even=filter(lambda x:x%2==0,list2)
# print(list(even))



# list1=[(1,3),(2,2),(3,1)]
# a=sorted(list1,key=lambda x:x[1])
# print(a)



# list2=[1,2,3,4,5,6]
# a=map(lambda x:x,list2)
# print(list(a))


# list2=[(11,3),(2,32),(4,45),(6,9)]
# a=sorted(list2,key=lambda x:x[1])  
# print(a)




# multiplication=lambda x,y:x*y
# print(multiplication(1,3))



# list1=[1,2,3,4,5,6]
# even=filter(lambda x:x%2==0,list1)
# print(list(even))


# list1=[1,2,9,4,5]
# a=sorted(list1,key=lambda x:x)
# print(a)


# product=lambda x,y:x*y
# print(product(2,3))


# product=lambda x,y:x+y
# result=product(1,2)
# print(result)

# list1=[1,2,3,4,5,6]
# even=filter(lambda x:x%2==0,list1)
# print(list(even))


# list1=[1,2,3,4,5,6,7,8]
# result=map(lambda x:x**2,list1)
# print(list(result))


# list1=[(1,2),(3,1),(7,6)]
# a=sorted(list1,key=lambda x:x[1])
# print(a)



# sorting list of tuples..
# list1=[(2,"one"),(5,"two"),(3,"Three")]
# sorted_data=sorted(list1,key=lambda x:x[0])
# print(sorted_data)





# prime number
# n=int(input("Enter a number:"))
# isprime=True
# for i in range(2,n):
   
#     if n%i==0:
#         isprime=False
#         break
# if n==1:
#     print("Number is neither composite nor prime.")
# elif isprime==True:
#     print("number is prime")
# else:
#     print("Not prime")

#         


n=int(input("Enter a number:"))
isprime=True
for i in range(2,n+1):
    for j in range(2,i):
   
        if i%j==0:
            isprime=False
            break

    if isprime==True:
        print(i)
