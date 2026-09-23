# n=25
# for i in range(1,11):
#     print(n*i)



# n=int(input("enter a number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)



# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)


# for i in range(2,101,2):
#     print(i)


# list1=[1,2,3,4,5,6,7,67,8,9]
# odd=[]
# even=[]
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even numbers:",even)
# print("odd numbers:",odd)



# string1="hello world"
# vowel=[]
# consonants=[]
# lst=list(string1)
# for i in lst:
#     if i in "aeiouAEIOU":
#         vowel.append(i)
#     else:
#         consonants.append(i)

# print(vowel)
# print(consonants)



# n=25
# for i in range(1,11):
#     print(n*i)



# string1="hello world"
# char1="o"
# count=0
# lst=list(string1)
# for i in lst:
#     if char1==i:
#         count+=1
# print(count)



# string1="hello world"
# count=0
# for i in string1:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)





# sum=0
# for i in range(2,101,2):
#     sum+=i
# print(sum)


# n=5
# a=0
# b=1
# while a<=n:
#     print(a)
#     a,b=b,a+b


# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i*j:4}",end=" ")
#     print()



# n=int(input("enter a number:"))
# isprime=True
# i=2
# while i<=n:
#     if n%i==0:
#         isprime=False
#     i+=1   
#     break   
# if n==1:
#     print("number is neither composite or prime.")
# elif isprime==True:
#     print("number is prime.")
# else:
#     print("number is not prime.")



# n=10
# while n>=1:
#     print(n)
#     n-=1


# list1=[1,2,3,4,5]
# sum=0
# for i in list1:
#     sum+=i
# print(sum)



# num=123
# count=0
# while num>0:
#     num=num//10
#     count+=1
# print(count)



# num=int(input("enter a number:"))
# reverse=0
# while num>0:
#     rem=num%10
#     reverse=reverse*10+rem
#     num=num//10
# print(reverse)




# num=123
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)




# x=2
# n=3
# i=1
# a=1
# while i<=n:
#     a=a*x
#     i+=1
# print(a)


# list1=[1,2,3,4,5]
# list2=[4,5,6]
# list3=[]
# for i in list1:
#     if i in list2:
#         list3.append(i)
# print(list3)




# a=10
# b=3
# i=1
# c=1
# while i<=b:
#     c=c*a
#     i+=1
# print(c) 



string1="hii hello /?/"
str1=string1.replace(" ","")
vowel=[]
cons=[]
for i in str1:
        if i in "aeiouAEIOU":
            vowel.append(i)
        else:
            cons.append(i)
print(vowel)
print(cons)

