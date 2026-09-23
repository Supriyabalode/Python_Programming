# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i*j:4}",end="")
#     print()




#prime number.

# n=int(input("enter a number:"))
# i=2
# isprime=True
# while i<n:
#     if n%i==0:
#         isprime=False
#     i+=1
# if n==1:
#     print("not prime nor composite.")
# elif isprime==True:
#     print("prime number")
# else:
#     print("not prime number.")





#FIBONACCI SERIES.
# n=int(input("enter a number:"))
# a=0
# b=1
# while a<=n:
#     print(a)
#     a,b=b,a+b



#PRINT NUMBERS FROM 10 TO 1.

# for i in range(10,0,-1):
#     print(i)

# i=10
# while i>0:
#     print(i)
#     i-=1


# PRINT ODD NUMBERS FROM 1 TO 10.


# for i in range(1,10,2):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i+=2




#SEPARATE AND STORE ODD AND EVEN NUMBERS.

# list1=[1,2,3,4,5,6,7,8]
# odd=[]
# even=[]
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd:",odd)
# print("even:",even)



#SAPERATE AND STORE VOWEL AND CONSONANTS

# string1="hefshine softwares"
# vowels=[]
# consonants=[]
# for i in string1:
#     if i in "aeiouAEIOU":
#         vowels.append(i)
#     else:
#         consonants.append(i)
# print("vowels:",vowels)
# print("consonants:",consonants)



#SUM OF ELEMENTS OF LIST.

# list1=[1,2,3,4,5]
# sum=0
# for i in list1:
#     sum=sum+i
# print("Addition of elements:",sum)



#SUM OF DIGITS.

# num=int(input("enter a number:"))
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)



# COUNT THE NUMBER OF DIGITS IN GIVEN NUMBER.

# num=int(input("enter a number:"))
# count=0
# while num>0:
#     num=num//10
#     count+=1
# print(count)




#REVERSE THE DIGITS OF NUMBERS

# num1=int(input("enter a number:"))
# reverse=0
# while num1>0:
#     rem=num1%10
#     reverse=reverse*10+rem
#     num1=num1//10
# print(reverse)




# list1=[1,2,3,4,5,6,7]
# for i in list1:
#     print(i)
    



# list2=[1,23,3,2,4,3,6,90]
# for index in range(len(list2)):
#     print(list2[index])


# for index,value in enumerate(list2):
#     print(index,value)



# list3=[9,8,7,6,5,4,45]
# index=0
# while index<len(list3):
#     print(list3[index])
#     index+=1


# dict1={"name":"supriya","age":21}
# for key in dict1:
#     print("keys are:",key)

# for val in dict1.values():
#     print("values are:",val)

# for key,val in dict1.items():
#     print("keys and values:",key,val)



#SUM OF 1 TO N NUMBERS.
# sum=0
# n=int(input("enter a number:"))
# for i in range(n+1):
#     sum=sum+i
# print(sum)


#FACTORIAL.

# num=int(input("enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print("factorial:",fact)



#COUNT HOW MANY TIMES SPECIFIC CHARACTER APPEAR IN THE STRING.
# mystr="hefshine software"
# ch=input("enter a character:")
# count=0
# for i in mystr:
#     if ch==i:
#         count+=1
# print(count)



#NO OF VOWELS IN STRING.
# mystr="hefshine softwares"
# count=0
# for i in mystr:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)





#MULTIPLICATION TABLE.

# n=int(input("enter a numer:"))
# for i in range(1,11):
#     print(f"{n} x {i} :",n*i)



#FIBONACCI SERIES.
# n=int(input("enter a number:"))
# a=0
# b=1

# while a<=n:
#     print(a)
#     a,b=b,a+b



# n=5
# b=1
# for a in range(0,n+1):
#     print(a)
#     a,b=b,a




#MULTIPLICATION MATRIX.


# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i*j:4}",end=" ")
#     print()




#PRIME NUMBER

# num=int(input("enter a number:"))
# isprime=True
# for i in range(2,num):
#     if num%i==0:
#         isprime=False
# if num==1:
#     print("not prime nor composite.")
# elif isprime==True:
#     print("prime number.")
# else:
#     print("not prime number.")




# separate the positive and nagative numbers from list. 
# list1=[1,9,-2,3,-4,5,-5,8,]
# positive=[]
# negative=[]
# for i in list1:
#     if i>0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print("positive no:",positive)
# print("negative no:",negative)



# a=set()
# print(type(a))



# n=int(input("enter a number:"))
# n1=n
# sum=0
# while n>0:
#     rem=n%10
#     sum=sum+(rem**3)
#     n=n//10
# if n1==sum:
#     print("armstrong number..")
# else:
#     print("not armstrong number..")


# sum of digits
# n=1235
# sum=0
# while n>0:
#     rem=n%10
#     sum=sum+rem
#     n=n//10
# print(sum)


#  reverse digits of number
# n=1235
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print(rev)



# armstrong number.....
# n=1235
# sum=0
# while n>0:
#     rem=n%10
#     sum=sum+(rem**3)
#     n=n//10

