#!/usr/bin/env python3.4



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


if len(sys.argv) >=2:
    whattosearch = sys.argv[2]
    wheretosearch = sys.argv[1]
    filesfound = find_the_file(wheretosearch, whattosearch)
    if len(filesfound):
        for each_file in filesfound:
            print ( "This file was located -->", each_file)
    else:
        print (None , "was found. Please try again!")
else:
    print("Please make sure to supply where and what to search for")
