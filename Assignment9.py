#Using os.walk, write a script that will print the filenames of zero length files.
#It should also print the count of zero length files.
import os
current = os.getcwd() #get current directory, or set equal to specified directory
count = 0
for root, dirs, files in os.walk(current):
    for filename in files:
        path = os.path.join(root, filename) #get full filepath
        filesize = os.path.getsize(path)
        if filesize == 0:
            print(filename + " is a zero length file.")
            count += 1
print("There are " + str(count) + " zero length files in this directory.")
    
#Write a script that will list and count all of the images in a given HTML web
#page/file. You can assume that: Each image file is enclosed with the tag <img
#and end with >, The HTML page/file is syntactically correct.
import urllib.request
import re

def get_images(url):
    images = re.compile('<img.*?/>', re.I)
    page = urllib.request.urlopen(url)
    image_count = 0
    while True:
        line = str(page.readline())
        result = images.findall(line)
        if result:
            image_count += 1
            print("Image number " + str(image_count) + ": " + str(result))

#get_images('https://www.npr.org/') #testing the function