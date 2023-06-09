import sqlite3
import os 
import sys

def walking(folder):
    totalfiles=0
    for root, directories, files in os.walk(folder):

        # for directory in directories:
        #     absolute_path=os.path.join(root,directory)
        #     print(f"Dir Path: {absolute_path}")
        for file in files:
            absolute_path=os.path.join(root,file)
            size= os.path.getsize(absolute_path)
            print(f"File Path: {absolute_path}\nSize: {size/1000}KB")
            totalfiles += 1
    print(totalfiles)


    
#Takes an argument from the terminal
path=sys.argv[1]
walking(path)