# a=int(input("enter a side1:"))
# b=int(input("enter a side2:"))
# c=int(input("enter a side3:"))
# if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
#     print("right angled triangle.")
# else:
#     print("it is not right angled triangle.")




# x=int(input("enter a x coordinate:"))
# y=int(input("enter a y coordinate:"))
# if x>0 and y>0:
#     print("first quadrant.")
# elif x>0 and y<0:
#     print("second quadrant.")
# elif x<0 and y<0:
#     print("third quadrant")
# elif x<0 and y>0:
#     print("fourth quadrant.")
# elif x==0 and y==0:
#     print("central.")
# elif x==0:
#     print("y axis.")
# elif y==0:
#     print("x axis")

    

# x=int(input("enter a x cordinate:"))
# y=int(input("enter a y coordinate:"))
# if x>0:
#     if y>0:
#         print("first quadrant.")
#     elif y<0:
#         print("fourth quadrant.")
#     else:
#         print("point lies on positive x axis.")
# elif x<0:
#     if y>0:
#         print("second quadrant.")
#     elif y<0:
#         print("third quadrant.")
#     else:
#         print("point lies on negative axis.")
# else:
#     if y==0:
#         print("point is at origin.")
#     else:
#         print("point lies on y axis.")



#quadratic equation.

import math
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a==0:
    print("not quadratic equation.")
else:
    d=(b*b)-4*a*c
    if d>0:
        sqrt1=math.sqrt(d)
        x1=(-b+sqrt1)/2*a
        x2=(-b-sqrt1)/2*a
        print(f"two distinct root:{x1},{x2}")
    elif d==0:
        root=-b/(2*a)
        print(f"one repeated root:{root}")
    else:
        print("complex root.")

        









