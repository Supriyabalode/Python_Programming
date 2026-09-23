#write a program to check string is palindrome or not.

# mystring="aba"
# a=mystring[::-1]
# print(a)
# if mystring==a:
#     print("string is palindrome.")
# else:
#     print("string is not palindrome.")




#write a program to reverse the words in a string.

# mystring="my name is supriya"
# print(mystring)
# a=mystring.split(" ")
# reversed_str=a[::-1]
# final=" ".join(reversed_str)
# print("Reversed words in sentence:",final)




#sort a string alphanumerically.

# mystring="orange,red,white,black,green"
# abc=mystring.split(",")
# print(abc)
# abc.sort()
# print(abc)
# final=",".join(abc)
# print("soted words alphanumericaly:",final)



#swap dot and comma.

# mystring="20.30,40,40"
# a=mystring.maketrans(",.",".,")
# abc=mystring.translate(a)
# print("swaped dot and comma:",abc)



# a='supriya'
# print(a)
# b="hefshine software"
# print(b)
# c='''hefshine software'''
# print(c)



#find occurences of substring.

# mystring="hefshine softwares"
# abc="i"
# occ=mystring.count(abc)
# print("total occurences:",occ)




#count total words in the string.

# mystring="hefshine software"
# a=mystring.split()
# total=len(a)
# print(total)



# check string contain only digit or not.

# str="1"
# a=str.isalnum()
# print(a)



#sort string alphanumerically.

# mystring="supriya balode"
# a=sorted(mystring)
# sorted_string="".join(a)
# print("sorted_string:",sorted_string)



#REPLACE ALL OCCURENCES OF SUBSTRING BY ANOTHER.



# mystring="my name is abc "
# replstr=mystring.replace("abc","supriya")
# print("replaced string:",replstr)



#WAP TO CHECK STRING STARTS WITH AND ENDSWITH PREFIX AND SUFFIX.

# mystring="my name is abc"
# print(mystring.startswith("my") or mystring.endswith("a"))




#REMOVE ALL WHITESPACES.

# str="hefshine software"
# abc=str.replace(" ","")
# print(abc)



#READ A STRING.AND EXCHANGE FIRST AND LAST CHARACTER OF STRING.

# mystring="hefshine software"
# string1=mystring[-1]+mystring[1:-1]+mystring[0]
# print(string1)




#READ A LINE FROM USER.PRINT THREE STRING USING ODD INDEXED CHAR,EVEN AND EVERY THIRD CHAR.

# str2="hefshine software"
# oddno=str2[1::2]
# print("odd indexed char:",oddno)
# even=str2[0::2]
# print("even indexed char:",even)
# third=str2[0::3]
# print("every third char:",third)




#WRITE PROG. TO CHECK IF SUBSTRING EXIST IN GIVEN STRING.
# mystring="hefshine software"
# substr="shine"
# print(substr in mystring)




#wRITE A PROG.TO FIND STRING ANAGRAM OR NOT.

# str1="listen"
# str2="silent"
# a=sorted(str1)
# b=sorted(str2)
# if a==b:
#     print("strings are anagram.")
# else:
#     print("strings are not anagram.")


# mystring="  hello"
# print(mystring.rstrip())
# print("hello")







# a="congratulations"
# b=input("enter a char:")
# vowels="aeiouAEIOU"
# if b in vowels:
#     c=a.count(b) 
#     print(c)



#print middle character of string.

# str2="hefshine software"
# a=len(str2)/2
# b=int(a)
# print(b)
# print(str2[b-1])



list1=["a","b","c"]
a="".join(list1)
print(a)