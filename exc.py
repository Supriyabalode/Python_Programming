#EXCEPTION-  exception is a abnormal condition occurs in program when program is syntatically correct but 
# it gives error during execution.

#EXCEPTION HANDLING- exception handling is a programming technique which allows a program to handle errors
# and continue running


# a=int(input("enter a number:"))
# b=int(input("enter a second number:"))
# c=a/b
# print("division of no:",c)



# num1=input("enter a number:")
# try:
#     num2=int(num1)
#     print(num2)
# except:
#     print("please enter the correct input.")



# a=int(input("enter a number:"))
# b=int(input("enter a second number:"))
# try:
#     c=a/b
#     print(c)
# except:
#     print("please enter second number non zero.")




# try:
#     file1=open("sample2.txt","r")
#     content=file1.read()
#     print(content)
# except FileNotFoundError as e:
#     print(e)



#MULTIPLE EXCEPTION AND SPECIFIC EXCEPTION COMBINED.

# num1=input("enter a number:")
# try:
#     num2=int(num1)
#     num3=10/num2
#     print(num3)
# except ValueError:
#     print("please enter a numeric value.")
# except ZeroDivisionError:
#     print("please enter a non zero value.")



# num1=input("enter a number:")
# try:
#     num2=int(num1)
#     num3=10/num2
#     print(num3)
# except Exception as e:                       
#     print("Exception:",e)
#     print("please enter the correct input.")



# num1=int(input("enter a number:"))
# num2=int(input("enter a numbet:"))
# try:
#     c=num1/num2
#     print("division:",c)
# except Exception as e:
#     print(e)
# else:
#     print("exception successfully.")



# try:
#     f1=open("aaa.txt","r")
# except Exception as e:
#     print(e)
# else:
#     print("executed successfully.........")





# num1=input("enter a number:") 
# num1=int(input("enter a number:"))
# try:
#     num2=int(num1)
#     num3=10/num2
#     print(num3)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print("successfully executed......")





# RAISE STATEMENT -allows the programmer to force a specific exception to occur.


# try:
#     roll=int(input("enter your roll number:"))
#     if roll<=0:
#         raise ValueError()
# except ValueError:
#     print("Value error exception thrown")





# try:
#     age=int(input("enter age:"))
#     if age<=0:
#         raise ValueError()
#     elif age>18:
#         print("eligible to vote..")
#     else:
#         print("not eligible to vote...")
# except ValueError:
#     print("Invalid age ......")




# try:
#     x=int(input("enter a number:"))
#     if not type(x) is int:
#         raise TypeError()
# except TypeError:
#     print("only integers are allowed")
# except ValueError as e:
#     print(e)




# class Error1(Exception):
#     """Base class for other exceptions """
# try:
#     num=int(input("enter a number:"))
#     if num==0:
#         raise Error1
#     elif num<0:
#         raise Error1
# except Error1:
#     print("Input value is less than or equal to 0,try again!")

# except Exception as e:
#     print(e)
# else:
#     print(num)




# try:
#     num=int(input("enter a number:"))
#     if num<0:
#         raise ValueError
#     fact=1
#     for i in range(num,0,-1):
#         fact=fact*i
# except ValueError:
#     print("only integers value accepted...")
# else:
#     print(fact)


# try:
#     a=int(input("enter a number:"))
#     b=int(input("enter a number2:"))
#     c=a/b
# except ZeroDivisionError:
#     print("please enter second number non zero...")
# except ValueError:
#     print("Invalid number:")
# except Exception as e:
#     print(e)
# else:
#     print(c)



# class Error1(Exception):
#     """ """
# try: 
#     age=int(input("enter your age...:"))
#     if age<=0:
#         raise Error1
#     elif age<18:
#         print("not eligible to vote....")
#     else:
#         print("eligible to vote")   
# except ValueError:
#     print("only integers accepted.......")    

# except Error1:
#     print("negative age not acceptable...")
    




# try:
#     age=int(input("enter your age:"))
#     if age<=0:
#         raise ValueError
#     elif age>100:
#         raise ValueError
#     elif age<18:
#         print("not eligible to vote..")
#     else:
#         print("eligible to vote...")
# except ValueError:
#     print("enter valid age...")




# try:
#     age=int(input("enter age:"))
#     if age<0:
#         raise ValueError
#     if age<18:
#         print("not eligile")
#     else:
#         print("eligible")
# except ValueError:
#     print("please enter valid age..........")


# class error(Exception):
#     """     """
# try:
#     age=int(input("enter your age:"))
#     if age<0:
#         raise error
#     elif age>100:
#         raise error
#     elif age<18:
#         print("you are not eligible to vote...")
#     else:
#         print("eligible to vote....")
# except error:
#     print("enter valid age.......")
# except Exception as e:
#     print(e)




# list1=[1,2,3,4,5,6,7]
# try:
#     print(list1[8])
# except IndexError:
#     print("Index out of range...")



# dict1={"name":"supriya","roll":2}
# try:
#     print(dict1.get("age"))
# except Exception as e:
#     print(e)
    




# try:
#     a=10
#     b=0
#     c=a/b
# except ZeroDivisionError as e:
#     print(e)





# find out largest palindrome from the given string...

str1="Ahilyanagar"
l=""
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        part=str1[i:j+1]
        if part==part[::-1]:
            if len(part)>len(l):
                l=part
print("Largest PAlindrome:",l)








