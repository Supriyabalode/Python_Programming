# class Student:
#     def __init__(self):
#         self.name="Supriya"
#         print(self.name)
# s1=Student()





#  Poymorphism

# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")

# a=Animal()
# a.sound()




# Example (Overriding)
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):     # Inheritance

    def sound(self): 
          # Overriding
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()