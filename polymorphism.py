# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
# circle=Circle(5)
# print("circle area:",circle.area())
# rect=Rectangle(2,4)
# print("area of rectangle:",rect.area())




#WAP THAT DEMOSTRATES POLYMORPHISM IN FUNCTION ARGUMENTS. CREATE A FUNCTION greet() 
# THAT ACCEPT DIFFERENT OBJECTS AND CALL THE greet() METHOD ON THEM,REGARDLESS OF THE OBJECT TYPE.

class Dog:
    def greet(self):
        return "woof,hello"
class Cat:
    def greet(self):
        return "meow,hello"
def greet(animal):
    print(animal.greet())
dog=Dog()
cat=Cat()

greet(dog)
greet(cat)





# class Greeter:
#     def greet(self,name="Guest",age=None):
#         if age:
#             return f"Hello {name}, you are {age} years old!"
#         return f"hello {name}"
# greeter=Greeter()
# print(greeter.greet())
# print(greeter.greet("JOhn"))
# print(greeter.greet("John",34))



# class Shape:
#     def area():
#         pass
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*self.r**2
# class Rect(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         return self.l*self.b
# circle=Circle(5)
# print(circle.area())
# rect=Rect(4,2)
# print("area of reactangle:",rect.area())






#  duck typing............

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()  # Works as long as the object has a 'speak' method



make_sound(Dog())  # Bark
make_sound(Cat())  # Meow
