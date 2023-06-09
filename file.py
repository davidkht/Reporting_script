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
# Call the walking function to get all file information in the specified path
all_files = walking(path)


num=0
# only 1 of the three options must be used. Comment the one not used.
# Sort the list of all_files based on the second element of each tuple (size),
# in descending order (largest to smallest) using the sorted() function.
# The key parameter specifies a function of one argument that is used to extract a comparison key from each tuple.
# Here, we use a lambda function to specify the key as the second element (x[1]) of each tuple.
# The lambda function takes each tuple (x) and returns its second element (size) for comparison.
# The reverse parameter is set to True to sort the list in descending order.
# The resulting sorted list is iterated in the for loop.
for abpath, size in sorted(all_files, key=lambda x:x[1],reverse=True):
    #option 1: prints the 10 largest files
    # if num>10:
    #     break    
    # print(f"File: {abpath}, Size: {size/1000}KB")

    #option 2: prints only files with size between 600 and 1000 bytes
    # if 600<size<2000:
    #     print(f"File: {abpath}, Size: {size/1000}KB")

    #option 3: only files ending in .{format}    
    format='.py'
    lenght=len(format)
    if abpath[-lenght:]==format:
        print(f"File: {abpath}, Size: {size/1000}KB")
    num+=1

    


