import sqlite3
import os 
import sys
#Takes an argument from the terminal
path=sys.argv[1]

def main():
    #Walks ALL directories and files in the path, ALL subfiles ALL subdirectories
    for root, directories, files in os.walk(path):
        for directory in directories:
            absolute_path=os.path.join(root,directory)
            print(f"Dir Path: {absolute_path}")
        for file in files:
            absolute_path=os.path.join(root,file)
            print(f"File Path: {absolute_path}")