#1. Write a simple Rectangle class. It should do the following:
#-Accepts length and width as parameters when creating a new instance
#-Has a perimeter method that returns the perimeter of the rectangle
#-Has an area method that returns the area of the rectangle
#-Don't worry about coordinates or negative values, etc.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter
    def area(self):
        area = self.length * self.width
        return area

#2. Using the UserList module, create a class called Ulist, and override
#the __add__, append, and extend methods so that duplicate values will not
#be added to the list by any of these operations.
from collections import UserList
class UList(UserList):
    def __init__(self, item):
        UserList.__init__(self)
        self.data = item
    def __add__(self, new_val):
        for value in new_val:
            if value in self.data:
                print(str(value) + " is already in the list")
            else:
                self.data += [value]
        return self.data
    def append(self, new_val):
        for value in new_val:
            if value in self.data:
                print(str(value) + " is already in the list")
            else:
                self.data.append(value)
        return self.data
    def extend(self, new_val):
        add_list = [] #new list to hold items to extend
        for value in new_val:
            if value in self.data:
                print(str(value) + " is already in the list")
            else:
                add_list.append(value)
        self.data.extend(add_list) #extend new items to original list
        return self.data    
