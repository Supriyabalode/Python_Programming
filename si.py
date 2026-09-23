#calculate simple interest.

# p=int(input("enter principal amount:"))
# r=int(input("enter rate of interest:"))
# t=int(input("enter time span:"))
# si=p*r*t/100
# print("simple interest:",si)


#calculate compound interest.

# p=int(input("enter principal amount:"))
# r=int(input("enter rate:"))
# t=int(input("enter time"))

# a=p*(1+r/100)
# A=pow(a,t)
# compound_interest=A-p
# print(a)
# print(compound_interest)



# ch=str(input("enter a character"))
# a=ord(ch)
# print(a)

#CREATE list with mixed data type.
# list1=["abc",20,1+2j,True]
# print(list1)
# list1.reverse()
# print("list in reverse:",list1)

# list2=[2,6,4,3,9]
# list2.sort()
# print(list2)
# list2.reverse()

# print(list2)

# #list3
# list3=[2,5,3,8,1,6]
#data=int(input("enter elements:"))
#print("index of element:",list3.index(data))
#print("index of",data,"is",list3.index(data))


# print("sum:",sum(list3))
# print("min ele:",min(list3))
# print("max:",max(list3))
# print("length:",len(list3))



#find the occurence of given element.
# list4=[1,2,6,3,4,3]
# occ=int(input("enter element to count occurence:"))
# print("occurence of",occ,"is",list4.count(occ))

#conditinal statement
#if stmt

#a=int(input("enter no:"))
# if a>5:
#     print("a is greater than 5")
# print("end")

#if-else
# if a>5:
#     print("a is greater than 5")
# else:
#     print("a is not greater than 5")
# print("end of program")


# num1=int(input("enter a num:"))
# if(num1%2==0):
#     print("num is even.")
# else:
#     print("num is odd.")

#accept 2 no. from user and compare them.
# num1=int(input("enter a num1:"))
# num2=int(input("enter a num2:"))
# if(num1>num2):
#     print("num1 is greater than num2.")
# else:
#     print("num2 is greater than num1.")



#accept no from user check it is positive or negative.

# a=int(input("enter no:"))
# if a>0:
#     print("num is positive.")
# elif a<0:
#     print("num is negative.")
# else:
#     print("number is zero.")




#pass statement is used to keep body of if statement blank.

# a=int(input("enter a no:"))
# if a>10:
#     pass

# print("end of main program.")




#accept marks for 3 subject from user.calculate average.
# s1=int(input("enter marks of sub1:"))
# s2=int(input("enter marks of sub2:"))
# s3=int(input("enter marks of sub3:"))
# total=s1+s2+s3
# avg=total/3
# print(avg)
# if(avg>=75):
#     print("grade A")
# elif(avg>=60):
#     print("grade B")
# elif(avg>=45):
#     print("grade C")
# elif(avg>=35):
#     print("grade D")
# elif(avg<35):
#     print("Fail")
# else:
#     print("invalid marks.")




#calculate power

# print(pow(10,2))


# num=int(input("enter a num:"))
# if num>10:
#     None
# print("end of the program.")




# list4=[1,9,7,5,4,6]
# print(list4[-1::-1])



#ACCEPT THE AGE FRON USER AND CHECK WHETHER USER IS ELIGIBLE TO VOTE OR NOT.

# age=int(input("enter your age:"))
# if age>100:
#     print("please enter age below 101")

# elif age>=18:
#     print("you are eligible to vote.")
# elif age<18:
#     print("you are not elible to vote.")
# else:
#     print("Invalid age.")





#SHORT HAND IF.
# age=int(input("enter age:"))
# if age>=18:print("eligible to vote.")


#SHORT HAND IF ELSE.
# age=int(input("enetr age"))
# print("you are elible to vote.") if age>=18 else print("not eligible to vote.")


#TERNARY CONDITIONAL STATEMENT.

# age=int(input("enetr age:"))
# result="you asre eligible to vote" if age>=18 else " you are not eligible"
# print(result)





# NESTED IF.

# age=int(input("enter your age:"))
# if age>=18:
#     if age>=60:
#         print("sinior citizon")
#     else:
#         print("adult.")
# else:
#     print("child")


# marks=int(input("enter marks:"))
# if marks>=35:
#     if marks>100:
#         print("i nvalid amrks.")
#     elif marks>=75:
#         print("distinction.")
#     elif marks>=60:
#         print("first class.")
#     elif marks>=45:
#         print("second class.")
#     else:
#         print("pass.")
# else:
#     print("fail")




#LOGICAL AND.
# marks=int(input("enter marks:"))
# if marks>=35 and marks<45:
#     print("pass")
# elif marks>=45 and marks<60:
#     print("second class.")
# elif marks>=60 and marks<75:
#     print("first class.")
# elif marks>=75 and marks<=100:
#     print("distinction.")
# elif marks>=0 and marks<35:
#     print("fail.")
# else:
#     print("invalid marks")


# num1=int(input("enter a num1:"))
# num2=int(input("enter second no:"))
# num3=int(input("enter third no:"))
# if num1>num2 and num1>num3:
#     print("num1 is greater.")
# elif num2>num1 and num2>num3:
#     print("num2 is greater.")
# elif num3>num1 and num3>num2:
#     print("num3 is greater.")
# else:
#     print("both or all no. are same")




# age=int(input("enter age:"))
# if age>=18:print("you are eligible to vote.")


# age=int(input("enter age"))
# print("you are elible to vote.") if age>=18 else print("you are not eligible.") 


# age=int(input("enter your age:"))
# result="you are eligible to vote." if age>=18 else "you are not eligible."
# print(result)

# age=int(input("enter your age:"))
# if age>=18:
#     if age>65:
#         print("adult")
#     else:
#         print("young")
# else:
#     print("child")





    
# marks1=int(input("enter marks1:"))
# marks2=int(input("enter marks2:"))
# marks3=int(input("enter marks3:"))
# total=marks1+marks2+marks3
# print(total)
# avg=total/3
# print(avg)
# if avg>=35:
#     if avg>100:
#         print("invalid marks.")
#     elif avg>75:
#         print("distinction.")
#     elif avg>=60:
#         print("first class.")
#     elif avg>=45:
#         print("second class.")
#     else:
#         print("pass")
# else:
#     print("Fail.")




# age=10
# name="supriya"
# print(f"my name is {name} and age is { age}")
# print("my name is {0} and age is {1}".format(name,age))

# age=10
# name="supriya"
# print(f"my name is {name} and age is {age}")
# print("my name is {} and age is {}".format(name,age))


print(pow(10,2))






