# num=int(input("enter a number:"))
# if num%2==0:
#     print("even number.")
# else:
#     print("odd number")



# num2=int(input("enter a number:"))
# if num2>0:
#     print("positive number.")
# elif num2<0:
#     print("negative number.")
# else:
#     print("number is zero.")



# marks=int(input("enter marks:"))
# if marks>100:
#     print("invalid marks.")
# elif marks>=90:
#     print("grade A")
# elif marks>=80:
#     print("grade B")
# elif marks>=70:
#     print("grade C")
# elif marks>=60:
#     print("pass")
# elif marks<60:
#     print("fail")
# else:
#     print("invalid marks.")



# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# num3=int(input("enter number:"))
# if num1>num2 and num1>num3:
#     print("maximum:",num1)
# elif num2>num1 and num2>num3:
#     print("maxium:",num2)
# elif num3>num1 and num3>num2:
#     print("maxium:",num3)
# else:
#     print("either two or three no.s are same.")


# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# num3=int(input("enter number:"))
# if num1>num2:
#     if num1>num3:
#         print("num1 is greater.")
# elif num2>num3:
#     if num2>num1:
#         print("num2 is greater.")
# elif num3>num1:
#     if num3>num2:
#         print("num3 is greater.")
# else:
#     print("either  2 or 3 numbers are same.")




# year=int(input("enter a year:"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("leap year.")
# else:
#     print("not leap year.")



# num1=float(input("enter a number:"))
# num2=float(input("enter a number:"))
# op=input("enter operator:")
# if op=="+":
#     print("result:",num1+num2)
# elif op=="-":
#     print("result:",num1-num2)
# elif op=="*":
#     print("result:",num1*num2)
# elif op=="/":
#     if num2==0:
#         print("zero division error.")
#     else:
#         print("result:",num1/num2)
# else:
#     print("enter valid operator.")
    




# classes_held=int(input("enter a no of classes held:"))
# classes_attend=int(input("enter no of classes attend:"))
# att=(classes_attend/classes_held)*100
# print(f"attendance:{att}")
# if att>=75:
#     print("Allowed to attend exam.")
# else:
#     print("not allowed to attend exam.")


# year_of_s=int(input("enter your years of services:"))
# salary=int(input("enter your salary."))
# if year_of_s>5:
#     bonus=(salary/100)*5
#     print("you are eligible for bonus.")
#     print("bonus:",bonus)
#     print("Total:",salary+bonus)
# else:
#     print("no bonus.")
#     print("salary:",salary)

    


# side1=float(input("enter the first side:"))
# side2=float(input("enter the first side:"))
# side3=float(input("enter the first side:"))
# if side1==side2==side3:
#     print("equilateral triangle.")
# elif side1==side2 or side2==side3 or side1==side3:
#     print("Isoscales triangle")
# else:
#     print("scalene")


# string1="hiihello"
# b=string1[0]
# c=b+string1[1::].replace(b,"$")
# print(c)


# lst1=[1,2]
# lst2=lst1
# lst2.append(8)
# print(lst1)



# a=10
# print(id(a))
# a+=1
# print(id(a))



# lst1=[1,2]
# a=id(lst1)
# lst1.append(8)
# b=id(lst1)
# print(a==b)

# print(pow(2,3))



# str1="abcabaayhdy"
# s=""
# for i in range(len(str1)):
#     for j in range(i+1,len(str1)+1):
#         part=str1[i:j]
#         if part==part[::-1]:
#             if len(part)>len(s):
#                 s=part


# print(s)


str1="aabaabcaa"
ls=""
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        part=str1[i:j]
        if part==part[::-1]:
            if len(part)>len(ls):
                ls=part
print(ls)

