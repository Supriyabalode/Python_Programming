# write a program to print your name.

# print("My name is supriya.")


# a=int(input("enter  a:"))
# b=int(input("enter b:"))
# c=a+b
# print("sum:",c)



#area of circle.

# radius=int(input("enter radius:"))
# area=3.14*radius*radius
# print("area of circle:",area)



#area of rectangle

# length=int(input("enter length:"))
# width=int(input("enter width:"))
# area=length*width
# print("area of rect:",area)



#area of triangle.

# base=int(input("enter base:"))
# height=int(input("enter height"))
# area=0.5*base*height
# print(area)




#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#  Ask user for their salary and year of service and print the net bonus amount. 

# year_of_service=int(input("enter year of services:"))
# salary=int(input("enter your salary:"))
# if year_of_service>5:
#     bonus=(salary/100)*5
#     total=salary+bonus
#     print("salary+bonus:",total)
# else:
#     print("your service is below 5 year.")
#     print("salary:",salary)




# A shop gives a discount of 10% if the cost of purchased quantity is more than $1000. 
# Take appropriate inputs and print total cost for user. 

# products=int(input("enter no of products:"))
# cost=int(input("enter cost:"))
# total_purchased=products*cost
# if total_purchased>1000:
#     print("you are eligible for discount")
#     discount=(total_purchased/100)*10
#     print("discount:",discount)
# else:
#     print("price:",total_purchased)



# A STUDENT WILL NOT BE ALLOWED TO ATTEND THE EXAM.IF HIS ATTENDENCE IS LESS THAN 75%.TAKE INPUT FRON USER.
#NO. OF CLASSES HELD,NO. OF CLASSES ATTENDED AND PRINT THE PERCENTAGE OF CLASS ATTENDED .

classes=int(input("enter no of classes held:"))
attend=int(input("enter no of  classes attended:"))
attendance=attend/classes*100
print("attendence:",attendance,"%")
if attendance>=75:
    print("Eligible to attend the exam.")
else:
    print("not eligible to attend the exam.")


    

