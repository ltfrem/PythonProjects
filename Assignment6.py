#1. write a function that accepts the name of a file and returns a tuple
#containing the number of lines, words, and characters that are in the file.
#(hint: use the split function of the string module to help you count the
#words in the file).
def file_count(filepath):
    file = open(filepath)
    lines = file.read().split("\n")
    line_count = len(lines)
    word_count = 0
    char_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
        char_count += len(line)
    tup1 = (line_count,)
    tup2 = (word_count,)
    tup3 = (char_count,)
    result = tup1 + tup2 + tup3
    return result

#2. write a function that accepts an arbitrary number of lists and returns a
#single list with exactly one occurrence of each element that appears in any
#of the input lists.
def list_filter(*lists):
    new_list = []
    for item in lists: #combine lists
        new_list.extend(item)
    output = []
    for item in new_list:
        if item in output:
            continue
        else:
            output.append(item)
    return output

#3. use the map function to add a constant to each element of a list. perform the
#same operation using a list comprehension (for example, the list (1,20,300,400) and
#constant 8, will result in: 9, 28, 308, 408)
my_list = [1, 20, 300, 400]
#map function:
def octo(num):
    return num + 8
answer = list(map(octo, my_list))
#list comprehension:
[x + 8 for x in my_list]

#4. write a function that will take a variable number of lists. each list can contain
#any number of words. this function should return a dictionary where the words are
#the keys and the values are the total count of each word in all the lists
def make_dict(*lists):
    new_list = []
    for item in lists: #combine lists
        new_list.extend(item)
    new_dict = {}
    for item in new_list:
        value = new_list.count(item)
        new_dict[item] = value
    return new_dict

#5. (optional) write a function that combines several dictionaries by creating a new
#dictionary with all the keys of the original ones. if a key appears in more than one
#input dictionary, the value corresponding to that key in the new dictionary should
#be a list containing all the values encountered in the input dictionaries that
#correspond to that key