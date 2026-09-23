# file1=open("sample.txt","x")

# file1=open("sample.txt","r")
# content=file1.read()
# print(content)


# file1=open("output.txt","w")
# file1.write("my name is supriya")

# f1=open("sample.txt","r")
# content=f1.read()
# print(content)


# f2=open("sample.txt","a")
# f2.write("\nAppended text")


# f2=open("sample.txt","r+")
# content=f2.read()
# print(content)
# f2.write("\nmy name is Supriya Balode")


# f2=open("sample.txt","w+")
# print(f2.tell())
# f2.write("this is w+ mode")
# f2.seek(0)
# content=f2.read()
# print(content)



# with open("sample.txt","a+") as f1:
#     f1.write("\nAppended text")


# import os
# if os.path.exists("output.txt"):
#     print("file exists.")
# else:
#     print("file doesnt exist.")




# import os
# if os.path.exists("sample.txt"):
#     print("file is exist.")
# else:
#     print("file doesnt exist")



# try:
#     f1=open("xx.txt","r")
# except:
#     print("file doesnt exist")
# else:
#     print("file exist.")



# with open("abc.txt","r") as f1:
#     content=f1.readlines()             # output will display in list format.
#     print(content)


# with open("abc.txt","r") as f1:
#     content=f1.readline()             
#     print(content)






# WRITE A PYTHON PROGRAM THAT OPENS A FILE sample.txt  IN READ MODE AND PRINT CONTENT T0 THE CONSOLE.

# f1=open("sample.txt","r")
# content=f1.read()
# print(content)




# write python program that opens file output.txt in write mode and write the string "hello world"
#  to the file.if file already exist,overrite the content.

# f1=open("output.txt","w")
# f1.write("hello world")




#WRITE A PYTHON THAT OPENS A file log.txt in append mode and adds the string "New entry" to the
# end of the file

# f1=open("log.txt","a")
# f1.write("hello python...")




#WRITE A PYTHON PROGRAM THAT OPENS A FILE data.txt IN READ AND WRITE  MODE,READS THE FIRST LINE,
#AND THEN WRITES "UPDATED CONTENT" TO THE BEGINING OF FILE.

# f1=open("data.txt","r+")
# line1=f1.readline()
# print(line1)

# f1.write("UPDATED CONTENT...")





# WAP THAT OPENS A FILE notes.txt IN r+ MODE.READ THE CONTENT ,REPLACE THE WORD "OLD" WITH "NEW" 
# THEN WRITE THE UPDATED CONTENT BACK TO THE FILE...

# f1=open("notes.txt","x")

# file1=open("notes.txt","r+")
# content=file1.read()
# print(content)
# new_content=content.replace("old","new")
# f1.seek(0)
# file1.write(new_content)





# WRITE A PROGRAM THAT CHECKS IF THE FILE sample.txt EXISTS BEFORE OPENING IT IN READ MODE.
# IF THE FILE DOES NOT EXIST IT SHOULD PRINT "file not found"

# import os
# if os.path.exists("aaa.txt"):
    
#     print("file exists")
# else:
#     print("file does not exits.")




# WRITE A PYTHON PROGRAM THAT OPENS A FILE report.txt WRITE MODE.IF THE FILE ALREADY EXIST,OVERWRITE ITS CONTENTS 
# WITH "REPORT GENERATED SUCCESSFULLY."

# f1=open("report.txt","w")
# f1.write("Report Generated Succcessfully...")




#WRITE A PROGRAM THAT PROMPTS THE USER TO INPUT AND THEN  WRITE A STRING TO THE FILE user_input.txt IN WRITE MODE.
# IF THE FILE ALREADY EXISTS,OVERWRITE IT WITH NEW CONTENT.

# string1=input("enter a string:")
# f1=open("user_input.txt","w")
# f1.write(string1)





# WRITE A PROGRAM THAT TRIES TO OPEN A FILE missing_file.txt IN READ MODE.IF THE FILE DOES NOT EXIST ,
# IT SHOULD PRINT "fILE NOT FOUND" WITHOUT CRASHING THE PROGRAM.

# try:
#     f1=open("missing_file","r")
# except FileNotFoundError:
#     print("file not found")




# WRITE A PYTHON PROGRAM THAT MERGES THE CONTENT OF MULTIPLE TEXT FILES (file1.txt,file2.txt.file3.txt) into
# single text merged txt maintaining the order of file.

# f1=open("file1.txt","r")
# f2=open("file2.txt","r")
# f3=open("file3.txt","r")
# f4=open("file4.txt","w")



# write a program compare content of two files...

# f1=open("file1.txt","r")
# f2=open("file2.txt","r")
# content1=f1.read()
# content2=f2.read()
# if content1==content2:
#     print("files are the same.")
# else:
#     print("files are different.")





file_names=["file1.txt","file2.txt","file3.txt"]
output_file="merged.txt"
with open(output_file,"w") as merged_file:
    for file_name in file_names:
        try:
            with open("file_name","r") as file:
                content=file.read()
                merged_file.write(content)
                merged_file.write("\n")
        except FileNotFoundError:
            print(f"Warning:{file_name} not found.skipping....")
print("files merged successfully:",output_file)

