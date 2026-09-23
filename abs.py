# from abc import ABC , abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def color(self):
#         pass
#     @abstractmethod
#     def price(self):
#         pass
# class Thar(Car):
#     def color(self):
#         return "black"
#     def price(self):
#         return "1400000"
# thar1=Thar()
# print(thar1.color())




# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def name(self):
#         pass
#     @abstractmethod
#     def color(self):
#         pass
#     def name(self):
#         return "Abc"
#     def color(self):
#         return "white"

# animal1=Animal()
# print(animal1.name())
# print(animal1.color())







# WRITE A PYTHON PROGRAM WITH ABSTRACT CLASS VEHICLE HAS WO ABSTRACT MAETHOD START AND STOP.
# CREATE A SUBCLASS CAR WHICH IMPLEMENTS BOTH METHODS

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start():
#         pass
#     def stop():
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("car started.....")
#     def stop(self):
#         print("car stopped....")
# car=Car()
# car.start()
# car.stop()



# WAP WITH AN ABSTRACT CLASS SHAPE WITH AN ABSTRACT METHOD DRAW(),WHICH ACCCEPT ARGUMENT FOR COLOR AND SIZE.
# IMPLEMENT THIS METHOD IN SUBCLASS CIRCLE.


# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def draw(self,color,size):
#         pass
# class Circle(Shape):
#     def draw(self,color,size):
#         print(color)
#         print(size)
# circle=Circle()
# circle.draw("red",3)







#  WRITE A PYTHON PROGRAM WITH ABSTRACT CLASS VEHICLE HAS TWO ABSTRACT MAETHOD START AND STOP.
# CREATE A SUBCLASS CAR WHICH IMPLEMENTS BOTH METHODS

# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("vehicle started......")
#     def stop(self):
#         print("vehicle stopped.......")
# car=Car()
# car.start()
# car.stop()




# WAP WITH AN ABSTRACT CLASS SHAPE WITH AN ABSTRACT METHOD DRAW(),WHICH ACCCEPT ARGUMENT FOR COLOR AND SIZE.
# IMPLEMENT THIS METHOD IN SUBCLASS CIRCLE.


# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def draw(self,color,size):
#         pass
# class Circle(Shape):
#     def draw(self,color,size):
#         self.color=color
#         self.size=size
        
# circle=Circle()
# circle.draw("red",5)
# print(circle.color)
