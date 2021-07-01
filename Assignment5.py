#using the keys method for dictionaries and the sort method for lists, write a
#for loop that prints the keys and corresponding values of a dictionary in the
#alphabetical order of the keys
foods = {'a': 'apple', 'c': 'cauliflower', 'g': 'guava', \
            'j': 'jackfruit', 'b': 'berry'}
keys = []
for key in foods.keys():
    keys.append(key)
keys.sort()
for key in keys:
    print(key + ': ' + foods[key])

#as an alternative to the range function, some programmers like to increment a
#counter inside a while loop and stop the while loop when the counter is no longer
#less than the length of the array. rewrite the following code using a while loop
#instead of a for loop
a = [7,12,9,14,15,18,12]
b = [9,14,8,3,15,17,15]
big = []
i = 0
while i < len(a):
    big.append(max(a[i],b[i]))
    i += 1
    
#write a loop that reads each line of a file. it should count the number of
#characters in each line and keep track of the total number of characters read.
#once you have a total of 1,000 or more characters, break the loop (you can use
#a break statement to do this)
import os
f = open(os.path.expanduser("~/Desktop/test_file.txt"))
lines = f.read().split("\n")
char_count = 0
total_char = 0

for line in lines:
    char_count += len(line)
    total_char += char_count
    if total_char >= 1000:
        break
f.close()

#modify the program written in question 3 so that it doesn't count characters on any
#line that begins with a #
import os
f = open(os.path.expanduser("~/Desktop/test_file.txt"))
lines = f.read().split("\n")
char_count = 0
total_char = 0

for line in lines:
    if line.startswith("#"):
        continue
    char_count += len(line)
    total_char += char_count
    if total_char >= 1000:
        break
f.close()