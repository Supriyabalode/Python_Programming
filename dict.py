# abc={"name":"supriya","age":21,"rollno":21}
# print(abc)
# abc.update({"rollno":2})       #update or modify value
# print(abc)
# abc.pop("name")              #remove specific pair by key.
# print(abc)
# abc.popitem()                #remove last pair.
# print(abc)
# print("age:",abc.get("age"))      #get specific value by key
# abc["phone"]="123"                 #add new key value pair.
# print(abc)
# abc["age"]=10      #modify value
# print(abc)

# print(abc["age"])




#CREATE A DICTIONARY USING DICT()  CONSTRICTOR.

#student=dict(name="supriya",age="21",roll=32)
# print(student)
# print(type(student))
# print(type(student["name"]))

# print(student.get("name"))
# student["name"]="sanchita"
# print(student)
# student.update({"name":"abc"})
# print(student)
# student["subject"]="python"             #add new key value pair.
# print(student)


# del student["roll"]             #Removes  an item by key.
# print(student)

# #student.pop["roll"]              #remove by key.

# student.popitem()                 #remove last item.
# print(student)

# student.clear()           #empties dictionary.
# print(student)






# #ITERATING THROUGH DICTIONARY.

# dict2={"s1":"java","s2":"python","s3":"ML"}

# for keys in dict2:           #print all keys.
#     print("keys are:",keys)



# for values in dict2.values():        # all values.
#     print("values:",values)


# for keys,values in dict2.items():
#     print("keys and values are:",keys,values)








#dict1={"name":"john","age":"25","city":"NewYork"}
# print(dict1["age"])


# dict1["country"]="USA"
# print(dict1)


#remove city.

# del dict1["city"]
# print(dict1)


# if "age" in dict1:
#     print("present.")
# else:
#     print("absent")



# if "gender" in dict1:
# print(dict1.get("gender"))
# else:
#     print("doesnt exist.")







#WRITE A PROGRAM ITERATES THROUGH THE DICTIONARY .PRINT BOTH KEYS AND VALUES.

# dict1={"a":"java","b":"python","c":"AI"}
# for keys,values in dict1.items():
#     print("keys and values:",keys,values)



# merges two dictionaries.

# dict3={"name":"john","age":32}
# dict4={"city":"newyork","country":"USA"}
# dict3.update(dict4)
# print(dict3)




# dict1={"a":"java","b":"python","c":"AI"}
# dict2={}








# WRITE A PROGRAM THAT UPDATES A DICTIONARY PERSON.

# person={"name":"john","age":25}
# new_info={"age":26,"city":"newyork"}
# person.update(new_info)
# print(person)



#WRITE A PROGRAM THAT FIND KEY WITH MAXIMUM VALUE IN DICTIONARY.

# marks={"s1":60,"s2":90,"s3":80}
# a=max(marks,key=marks.get)
# print(a)




#WRITE A PYTHON PROGRAM CREATE A DICTIONARY FROM LIST OF NUMBERS,WHERE THE KEYS ARE NUMBERS AND VALUES ARE SQUARE.
# numbers=[1,2,3,4,5]
# squares={x:x**2 for x in numbers}
# print(squares)


# abc={"a":2,"b":5}
# print(abc["a"])




# person={"name":"john","age":25,"city":"newyork"}
# for keys,values in person.items():
#     print("keys and values are:",keys,values)



# dict1={"name":"john","age":20}
# dict2={"city":"newyork","countrty":"usa"}
# dict1.update(dict2)
# print(dict1)


# numbers=[1,2,3,4,5]
# squares={x:x**2 for x in numbers}
# print(squares)

# numbers=[1,2,3,4,5]
# squares={x:x**2 for x in numbers}
# print(squares)




# age={"a":2,"b":10,"c":8}
# a=max(age,key=age.get)




# #swap key and values.
# age={"a":2,"b":10,"c":8}
# swapped_keys={value:key for key,value in age.items()}
# print(swapped_keys)

# a={value:key for key,value in age.items()}


# age={"a":2,"b":10,"c":8}
# for key,value in age.items():
#     print("key and value:",key,value)



# dict1={"name":"john","age":25}
# dict2={"city":"newyork","country":"USA"}
# dict1.update(dict2)
# print(dict1)


# numbers={1,2,3,4,5}
# squares={x:x**2 for x in numbers}
# print(squares)




# age={"a":2,"b":10,"c":8}
# a=max(age,key=age.get)
# print(a)




# age={"a":2,"b":10,"c":8}
# new_dict={values:keys for keys,values in age.items()}
# print(new_dict)
# print(new_dict[2])



# age={"a":2,"b":10,"c":8}
# swapped_keys={values:keys for keys,values in age.items()}
# print(swapped_keys)


# dict1={"name":"supriya","roll":2}
# for key,val in dict1.items():
#     print(key,":",val)


# dict2={val:key for key,val in dict1.items()}
# print(dict2)



# print({"a":1,"b":2}.keys())
# a={"a":2,"b":3}
# print(a.values())




# Create a dictionary with keys from a tuple
# keys = ('x', 'y', 'z')
# new_dict = dict.fromkeys(keys)

# print(new_dict)


# Create a dictionary with keys from a list
# keys = ['a', 'b', 'c']
# default_value = 0
# new_dict = dict.fromkeys(keys,default_value)

# print(new_dict)




# Create a dictionary with a list as the default value

keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, [])
# new_dict['a'].append(1)
# new_dict['b'].append(2)
print(new_dict)




