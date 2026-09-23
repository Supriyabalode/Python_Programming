# mytuple=["apple","banana","cherry"]
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))



# CREATE AN ITERATOR THET RETURN NUMBERS,STARTING WITH 1,AND EACH SEQUENCE WILL INCREASE BY ONE .

# class Mynumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass=Mynumbers()
# myiter=iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# class Mynumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# mynum=Mynumbers()
# myiter=iter(mynum)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



class Myclass:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=Myclass()
myiter=iter(myclass)
print(next(myiter))



