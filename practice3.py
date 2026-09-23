# prime no between 1 to 100 in reverse order

# for i in range(100,1,-1):
#     isprime=True
#     for j in range (2,i):
#         if i%j==0:
#             isprime=False
#     if isprime==True:
#         print(i)


# lst1=[12,234,35,47,678,789,80,6,456,564,57,67]
# avg=sum(lst1)/len(lst1)
# count=0
# for i in lst1:
#     if i>avg:
#         count=count+1
# print("count of values which is more than average:",count)




# lst1=[34,56,78,87,89,23,66,67]
# Group1=0
# Group2=0
# Group3=0
# for i in lst1:
#     if i<=100 and i>=71:
#         Group1+=1
#     elif i<=70 and i>=51:
#         Group2+=1
#     elif i<=50 and i>=0:
#         Group3+=1
# print("Count of 0-50:",Group3)
# print("Count of 51-70:",Group2)
# print("Count of 71-100:",Group1)


 

# list1=[12,[23,34],[1,2,3,4],[2,2,2,2]]



# Descriptors

# __get__  to retrieve or print value or object
# __set__  to set value to object
#  __del__    to delete value of object


# class Person:
#     def getAge(self):
#         print("Getter is called......")
#         return self._age
#     def setAge(self,age):
#         print("Setter is called.......")
#         self._age=age
#     def delAge(self):
#         print("Deleter is called.......")
#         del self._age
#     age=property(getAge,setAge,delAge)
# p=Person()
# p.age=35
# print(p.age)
# del p.age

    
class Person:
    def getAge(self):
        print("Getter is called......")
        return self._age
    def setAge(self,age):
        if age<100 and age>0:
            print("Setter is called.......")
            self._age=age
    def delAge(self):
        print("Deleter is called.......")
        del self._age
    age=property(getAge,setAge,delAge)
p=Person()
p.age=35
print(p.age)



