def even(n):
    if n%2==0:
        return "number is even"
    else:
        return "number is odd"
    






def factorial(n):
    
    for i in range(n,0,-1):
        fact=1
        fact=fact*i
        return fact



n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
  