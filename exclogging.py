# import logging
# try:
#     printf("Hello world!")
# except Exception as argument:
#     logging.exception("Error occured while printing.")



# import logging
# try:
#     a=10
#     b="c"
#     c=a+b
# except Exception as err:
#     f=open("mynew1.txt","a")
    
#     print(str(err))
#     # f.close()
    
#     a=logging.exception("g")
#     f.write(a)
    



# import logging
# logging.basicConfig(filename='app.log',level=logging.ERROR,format='%(asctime)s - %(levelname)s - %(message)s')
# def risky_function():
#     return 10/0
# try:
#     risky_function()
# except Exception as e:
#     logging.error("An exception occured",exc_info=True)



# import logging
# def main():
#     logging.basicConfig(filename="practice.log",format='[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s',filemode='a')
#     logger=logging.getLogger('my_logger')
#     logger.setLevel(logging.DEBUG)
#     logger.debug("Harmless debug message")
#     logger.info("just an information")
#     logger.warning("Its warning")
#     logger.error("Did you try to divide by zero")
#     logger.critical("internet is down")
# if __name__=='__main__':
#     main()



# import logging
# logging.basicConfig(filename='app1.log',level=logging.ERROR,format='%(asctime)s - %(levelname)s - %(message)s')
# def compare_files(file1,file2):
#     try:
#         with open(file1,"r") as f1, open(file2,"r") as f2:
#             content1=f1.read()
#             content2=f2.read()
#             if content1==content2:
#                 print("files are same")
#             else:
#                 print("files are different.")
    
#     except Exception as e:
#         logging.error("an exception is occured:",exc_info=True)

# compare_files("file1.txt","file22.txt")
