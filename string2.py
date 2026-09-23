#mystring=" hefshine software"
# print(mystring.count("e"))

#print(mystring.replace("ine","abc"))

# print(mystring.endswith("are") and mystring.startswith("hef"))

# print(mystring.strip())

# print(len(mystring))
# print(mystring.isalnum())
# abc=sorted(mystring)
# sorted_string="".join(abc)
# print(sorted_string)



# abc="xyz"
# a=(abc[::-1])
# print(a)
# if a==abc:
#     print("string is palindtrome.")
# else:
#     print("string is not palindrome.")


#write a python code to reverse the words in a sentence.

# string2="hefshine softwares"
# a=string2.split(" ")
# print(a)
# rev_str=a[::-1]
# final_str=" ".join(rev_str)
# print(final_str)

#read a string.exchange first and last character of a string.

# string3="hefshine softwares"
# print(string3[-1]+string3[1:-1]+string3[0])



#remove all whitespaces from string.
# a=string3.replace(" ","")
# print(a)



#ACCEPT COMMA SEPARETED SEQUENCE OF WORDS AS INPUT AND PRINT THE WORDS IN SORTED FORM(ALPHANUMERICALLY) 
# string4="orange,red,white,black,green"
# abc=string4.split(",")
# print(abc)
# abc.sort()
# print(",".join(abc))



#WRITE A PROGRAM TO SWAP COMMA AND DOT IN A STRING.


# str="47,89,56.3"
# abc=str.maketrans(".,",",.")
# str1=str.translate(abc)
# print(str1)



#READ A LINE FROM USER.PRINT THREE STRINGS USING ODD INDEXED CHARACTERS,EVEN INDEXED CHARACTERS AND EVERY THIRD CHARACTEER.

# str1=input("enter a string:")
# print("odd:",str1[1::2])
# print("even indexed characters:",str1[0::2])
# print("every third character:",str1[0::3])




#write a python program to check if a substring exist in a given string.

# mystring="hefshine software"
# substr="hef"
# if substr in mystring:
#     print("substring exist in string.")
# else:
#     print("not exist")


#write a python program to check if two strings are anagrams(contain the same characters in a different order.)

# str1="listen"
# str2="silent"
# a=sorted(str1)
# b=sorted(str2)
# if a==b:
#     print("given strings are anagram")
# else:
#     print("not anagram.")

#print(float('10.8'))



#A COMPANY DECIDED TO GIVE BONUS OF 5% TO EMPLOYEE IF HIS YEAR OF SERVICE IS MORE THAN 5 YEARS.ASK USER FOR SALARY.


# salary=int(input("enter your salary"))
# service=int(input("enter your year of service:"))
# if service>5:
#     bonus=(salary*0.5)
#     print("bonus:",bonus)
# else:
#     print("your service is less than 5 year.")


# no_of_products=int(input("enter no of product: "))
# cost=int(input("enter cost:"))
# purchased=no_of_products*cost
# if purchased>1000:
#     discount=purchased*0.10
#     print("total:",discount+purchased)
# else:
#     print(purchased)




#write a program to accept age of three person from user and find youngest and older person .

    

# person1=int(input("enter a age:"))
# person2=int(input("enter age:"))
# person3=int(input("enter age:"))
# if person1>person2 and person1>person3:
#     print("person1 is older.")

#     if person2<person3:
#         print("person2 is younger.")
#     else:
#         print("person3 is younger.")
# elif person2>person1 and person2>person3:
#     print("person2 is older.")
#     if person1<person3:
#         print("person1 is younger.")
#     else:
#         print("person3 is younger.")
# else:
#     print("person3 is older.")
#     if person1<person2:
#         print("person1 is younger.")
#     else:
#         print("person2 is younger.")
        


#print(10>5<2)



# mystring="abc"
# abc=mystring.split()
# print(abc)


# str1="hefshine sofware"
# a=str1.split(" ")
# reversed_str=a[::-1]
# abc=" ".join(reversed_str)
# print(abc)





# mystring="hefshine Software"
# a=mystring.split(" ")
# b=a[::-1]
# final=" ".join(b)
# print(final)




# mystr="hefshine,software"
# a=mystr.split()
# b=a[::-1]
# c="".join(b)
# print(c)




# str1="hefshine"
# b=list(str1)
# b.sort()
# c="".join(b)
# print(c)



# print(list("hello"))



#FIND LONGEST PALINDROME IN STRING.












# import re
# string1="hii hello /?/"
# cleaned=re.sub(r'[^\w\s]','',string1)
# str1=cleaned.replace(" ","")
# vowel=[]
# cons=[]
# for i in str1:
#         if i in "aeiouAEIOU":
#             vowel.append(i)
#         else:
#             cons.append(i)
# print(vowel)
# print(cons)





# str1="hello world /9)"
# vowel=[]
# cons=[]
# for i in str1:
#     if i.isalpha():
#         if i in "aeiouAEIOU":
#             vowel.append(i)
#         else:
#             cons.append(i)
# print(vowel)
# print(cons)        



str1="Hefshine Softwares"
l1=str1.split()
l2=l1[::-1]
final=" ".join(l2)
# print(final)


# print(list(str1))

print(sorted(str1.lower()))





