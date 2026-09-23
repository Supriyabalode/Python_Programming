
# tuple1=("apple","banana","cherry")
# print(tuple1[0])
# print(tuple1[2])

# print("length of tuple:",len(tuple1))




# tupl1=(10,20,45,90,65)
# print("maximum element:",max(tupl1))
# print("minimum element:",min(tupl1))


#write a program that unpack a tuple person=(john,25,eng) inti 3 var name,age,prof and print.

# person=("john",25,"Engineer")
# name,age,profession=person
# print("Name:",name)
# print("Age:",age)
# print("Profession:",profession)




# tuple1=(5,5,5,5,5,5,5,5,5,5)
# print(tuple1)

# tuple2=(5,)
# print(tuple2*10)



#abc=[(1,2),(3,4),(5,6)]        
# tupl1=tuple(abc[0])
# tupl2=abc[1]
# tupl3=abc[2]
# print(tupl1+tupl2+tupl3)

#OR


# a,b,c=abc     #using unpacking.
# d=a+b+c
# print(d)


#write a program to concatenate two tuples.

# tuple1=(1,2,3)
# tuple2=(4,5,6)
# tuple3=tuple1+tuple2
# print(tuple3)



#create a tuple numbers=(10,20,30,40,50.).slice the tuple to extract second to forth element.

# tuple1=(10,20,30,40,50)
# print("second to forth elements:",tuple1[1:4])



#write a program to count how many times the number 2 in the tuple.

# tuple2=(1,2,2,3,2,4)
# print(tuple2.count(2))



#WRITE A PROGRAM ITERATES THROUGH THE DICTIONARY .PRINT BOTH KEYS AND VALUES.

dict1={"a":"java","b":"python","c":"AI"}
for keys,values in dict1.items():
    print("keys and values:",keys,values)

print(dict1.values())

# merges two dictionaries.

# dict3={"name":"john","age":32}
# dict4={"city":"newyork","country":"USA"}
# dict3.update(dict4)
# print(dict3)  




# list1=[1,3,2,6,6,5,4]
# for i in enumerate(list1,1):
#     print(i)




# list1=[(1,2),(3,4),(5,9)]
# a,b,c=list1
# print(a)


# list1=(1,2,3)
# a,b,c=list1
# print(a)


