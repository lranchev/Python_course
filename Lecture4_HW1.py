# Напишете програма, която търси за файлове във Вашата файлова система. Програмата трябва да получава
# два параметъра при извикването - къде да търси, и какво да търси. Примерно извикване на програмата:
# python3  find.py  /home/user/Downloads  me.jpg
#!/usr/bin/python3.4
import os
import sys


def find_the_file (wheretosearch: str, whattosearch: str) -> list:
    result = []
    wheretosearch = os.path.abspath(wheretosearch)
    targetofsearch = os.path.join(wheretosearch, whattosearch)
    for dirpath, dirname, files in os.walk(wheretosearch):
        for file in files:
            file_absolute_path = os.path.join(dirpath, file)
            if file_absolute_path.find(whattosearch) != -1:
               result.append(file_absolute_path)
    return result


whattosearch = input("Please provide file to search for: " )
wheretosearch = input("Please provide directory where to search: ")


filesfound = find_the_file( wheretosearch, whattosearch)
print ()
if len(filesfound):
    for each_file in filesfound:
        print ( "This file was located -->", each_file)
else:
    print (None , "was found. Please try again!")
