import os 
import sys

# Define a function for walking through a folder and collecting file information
def walking(folder):
    pareja = []
    # Use os.walk to traverse the folder recursively
    for root, directories, files in os.walk(folder):
        for file in files:
            # Get the absolute path of each file
            absolute_path = os.path.join(root, file)
            # Get the size of the file using os.path.getsize
            size = os.path.getsize(absolute_path)
            # Append a tuple of (absolute_path, size) to the list
            pareja.append((absolute_path, size))
    
    # Return the list of file information
    return pareja

# Take an argument from the terminal
path = sys.argv[1]
option=sys.argv[2]
# Call the walking function to get all file information in the specified path
all_files = walking(path)
num=0

# Sort the list of all_files based on the second element of each tuple (size),
# The key parameter specifies a function of one argument that is used to extract a comparison 
# key from each tuple.
# Here, we use a lambda function to specify the key as the second element (x[1]) of each tuple.
# The lambda function takes each tuple (x) and returns its second element (size) for comparison.
# The reverse parameter is set to True to sort the list in descending order.
# The resulting sorted list is iterated in the for loop.

# option 1: Display the {input} largest files
if option=='1':
    number=int(input("Write the number of filepaths you want to see: "))
    for abpath, size in sorted(all_files, key=lambda x:x[1],reverse=True):        
        if num>number:
            break    
        print(f"{num}). Size: {size/1000}KB, File: {abpath}")
        num+=1
# option 2: prints only files with size between input and input bytes
elif option=='2':  

    lower_byte= int(input('Lower Byte limit: '))
    max_byte  = int(input('Max Byte limit: '))
    for abpath, size in sorted(all_files, key=lambda x:x[1],reverse=True): 
        if lower_byte<size<max_byte:
            print(f"{num}). Size: {size/1000}KB, File: {abpath}")
        num+=1

# option 3: only files ending in .{formatinput}  
elif option=='3': 
    conteo=0
    format=input('What format do you want to search: ')
    for abpath, size in sorted(all_files, key=lambda x:x[1],reverse=True):         
        lenght=len(format)
        if abpath[-lenght:]==format:
            print(f"{num}). Size: {size/1000}KB, File: {abpath}")
            conteo+=1
        num+=1
    print(f"\nNúmero de archivos encontrados: {conteo}")
else:
    print("Not valid option")


    


