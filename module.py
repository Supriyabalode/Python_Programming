import Calculator
result=Calculator.Add(12,78)
print("Addition:",result)



import Calculator as cal
result=cal.Add(12,78)
print("addition:",result)



from Calculator import Sub,Add
result=Sub(152,78)
print(result)



from Calculator import *       #import all functions.
result=Sub(152,78)
print("Substraction:",result)




