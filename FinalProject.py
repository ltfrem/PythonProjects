#Pick one or the other:
#1. A file with a name like picture.jpg is said to have an extension of 'jpg'; i.e.
#the extension of a file is the part of the file after the final period in its name.
#Write a program that takes as an argument the name of a directory (folder) and then
#finds the extension of each file. Then, for each extension found, it prints the
#number of files with that extension and the minimum, average, and maximum size for
#files with that extension in the selected directory.
import os
try:
    answer = 0
    while answer == 0:
        usr_input = input("Enter the directory/folder you want to look in: ")
        if os.path.exists(usr_input):
            answer = 1
            files = os.listdir(usr_input)
        else:
            print("Please enter a valid directory.")
except:
    pass
    
def split_ext(files):
    exts = [] #new list to hold files by extension
    for file in files:
        filename, file_ext = os.path.splitext(file) #split file extension off
        new_ext = [file_ext.lower()]
        exts.extend(new_ext)
    return exts #return list of extensions
ext_result = split_ext(files)

def unique_list(file_list): #creates list of all unique extensions
    unique = []
    for i in file_list:
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique
unique_exts = unique_list(ext_result)

def count_exts(ext_list): #get number of files with each extension
    ext_count = []
    count_dict = {}
    for item in ext_result:
        count_dict[item] = ext_result.count(item)
    return count_dict #return dictionary of count by extension
item_count = count_exts(ext_result) #call function based on output of other function
        
def file_size(directory, files): #get sizes of all files
    size_dict = {}
    for root, directory, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file) #get full filepath
            filesize = os.path.getsize(path)
            size_dict[file.lower()] = filesize
    return size_dict #return dictionary of files and their size
files_dict = file_size(usr_input, files)

def sort_values(file_dictionary, file_exts):
    values_dict = {}
    for i in file_exts:
        result = [v for k, v in file_dictionary.items() if i in k]
        values_dict[i] = result
    return values_dict
sorted_vals = sort_values(files_dict, unique_exts)

def get_average(list_of_values):
    count = len(list_of_values)
    total = 0
    for item in list_of_values:
        total += item
    avg = total / count
    return avg

def get_minimum(list_of_values):
    minimum = min(list_of_values)
    return minimum

def get_maximum(list_of_values):
    maximum = max(list_of_values)
    return maximum

print("In the directory " + (str(usr_input)) + ", there are:")
for k, v in item_count.items():
    print("Number of files with extension " + str(k) + ": " + str(v))
for k, v in sorted_vals.items():
    print("Average " + str(k) + " file size: " + str(get_average(v)))
    print("Minimum " + str(k) + " file size: " + str(get_minimum(v)))
    print("Maximum " + str(k) + " file size: " + str(get_maximum(v)))