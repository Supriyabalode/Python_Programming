# #PRINT NUMBERS FROM 10 TO 1.
# for i in range(10,0,-1):
#     print(i)


#PRINT ODD NUMBERS FROM 1 TO 20.

# for i in range(1,20,2):
#     print(i)


#SEPARATE AND STORE EVEN,ODD ELEMENT TO DIFFERENT LIST.
# list1=[122,3,1,34,54,55,67,87.90,9]
# even=[]
# odd=[]
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even number list:",even)
# print("odd number list:",odd)



#SEPARATE AND STORE VOWELS AND CONSONANTS FROM GIVEN STRING  TO DIFFERENT LIST.
# str="hello welcome to python"
# vowels=[]
# consonants=[]
# for i in str:
#     if i in ['a','e','i','o','u']:       #if i in 'aeiouAEIOU'
#         vowels.append(i)
#     else:
#         consonants.append(i)
# print("vowels list:",vowels)
# print("consonant list:",consonants)



# list1=[1,2,3,4,5]
# sum=0
# for i in list1:
#     sum+=i
# print("sum is:",sum)




# list2=[1,2,3,4,5]
# count=0
# for i in list2:
#     count+=1
# print("count:",count)


#SUM OF DIGITS...

# num=int(input("enter a number"))
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(f"sum of digit of num is :{sum}")






# num=int(input("enter a number:"))
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)




#COUNT NUMBER OF DIGITS IN THE GIVEN NUMBER.
# num=int(input("enter a number:"))
# sum=0
# count=0
# while num>0:
#     num=num//10
#     count+=1
# print("number of digits:",count)





#WRITE A PROGRAM TO THAT TAKES INTEGER  AS INPUT AND USES WHILE LOOP TO REVERSE THE DIGITS OF NUMBER.
# num2=int(input("enter a number:"))
# reverse=0
# while num2>0:
#     rem=num2%10
#     reverse=reverse*10+rem
#     num2=num2//10
# print(reverse)



# str1="hello welcome to python"
# vowels=[]
# consonants=[]
# for i in str1:
#     if i.isalpha():
#         if i in ['a','e','i','o','u']:       #if i in 'aeiouAEIOU'
#             vowels.append(i)
#         else:
#             consonants.append(i)
    
# print("vowels list:",vowels)
# print("consonant list:",consonants)