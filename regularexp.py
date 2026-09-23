# import re
# text="hii I am amazing amaz"
# pattern=r"\ba\w*z\b"
# result=re.findall(pattern,text)
# print(result)



# import re
# text="Hello 123"
# pattern=r"\D"
# result=re.findall(pattern,text)
# print(result)



# import re
# text="Hello pyhon 123"
# pattern=r"[a-zA-z]"
# result=re.findall(pattern,text)
# print(result)



# import re
# text="I bought 10 book and pens and total is 200"
# text1="Hello pyhon 123"
# text2="123"
# text3="python"
# pattern=r"^[a-zA-z]+$"
# result=re.findall(pattern,text)
# result1=re.findall(pattern,text1)
# result2=re.findall(pattern,text2)
# result3=re.findall(pattern,text3)
# print(result)
# print(result1)
# print(result2)
# print(result3)



# import re
# text="Hello my  name   is    supriya"
# pattern=r"\s+"
# result=re.sub(pattern," ",text)
# print(result)



# import re
# text="my name  is   supriya"
# pattern=r"\s+"
# result=re.sub(pattern," ",text)
# print(result)





#EXTRACT ALL EMAIL ADDRESSES.
# import re
# text="hello abc@gmail.com   ab@gmail.com"
# pattern=r"[a-zA-z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]{2,4}$"
# result=re.findall(pattern,text)
# print(result)



# CHECK IF A STRING CONTAINS A SPECIFIC WORD.
# import re
# text="I am python developer"
# pattern=r"\bpython\b"
# result=re.findall(pattern,text)
# print(result)




#  MATCH ALL WORDS STARTING WITH A SPECIFIC LETTER.
# import re
# text="I am a python developer"
# pattern=r"\ba\w*\b"
# result=re.findall(pattern,text)
# print(result)




# EXTRACT DATES IN DD-MM-YYYY

# import re
# text=" todays date is 19-03-2025\b"
# pattern=r"\b[0-9]{2}-[0-9]{2}-[0-9]{4}\b"
# result=re.findall(pattern,text)
# print(result)




# import re
# def EmailValidate(email):
#     pattern=r"^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,4}$"
#     return bool(re.match(pattern,email))
# print(EmailValidate("abc@gmail.com"))
# print(EmailValidate("ab@gmail.com"))





# import re
# def Abc(text):
#     pattern=r"\b\d{2}-\d{2}-\d{4}\b"
#     result=re.findall(pattern,text)
#     return result
# print(Abc("Todays date is 19-03-2025"))
# print(Abc("the meeting is scheduled between 23-10-2025 to 29-10-2025"))





# CHECK PALINDROME USING REGREX.

# import re
# def is_palindrome(text):
#     cleaned_text=re.sub(r"[^a-zA-Z0-9]","",text).lower()
#     return cleaned_text==cleaned_text[::-1]
# print(is_palindrome("A man, a plan, a canal: Panama"))


# import re
# def Datef(dates):
#      pattern=r"^\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
#      return 
    