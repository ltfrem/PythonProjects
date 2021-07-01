def insertion_sort(nums):
    j = 0 #Initialize variable j to be incremented
    for i in range(1, len(nums)): #start at second item, go through nums list
        possible = nums[i]
        while nums[i-1] > possible and i > 0: #Item on the left is larger, don't allow negative indexing
            j += 1 #Increment j each time a swap occurs
            nums[i], nums[i-1] = nums[i-1], nums[i] #Swap the order
            i = i -1 #Keep going through the list
            swap_num = ', '.join([str(i) for i in nums]) #Formatting for printing
            print("Swap " + str(j) + ": " + str(swap_num))
    return nums

def calculate_mean(values):
    sum = 0 #Initialize variable to hold the total
    mean = 0
    for i in values:
        i = int(i) 
        sum += i 
        mean = sum/len(values) #Divide total by amount of numbers
    return mean

numbers = '' #Initialize numbers variable
while numbers != 'exit': #Keep prompting until user enters 'exit'
    try:
        numbers = input("Enter a comma-separated group of numbers: ")
        if numbers.lower() == 'exit':
            print("Goodbye")
            quit()
        elif numbers.lower() != 'exit':
            nums_list = numbers.split(",") #Make numbers into a list
            pass_list = []
            for i in nums_list:
                i = int(i)
                pass_list.append(i) #Add each integer to pass_list
    except ValueError:
        print("You've entered something that's not a number.")
        continue
    
    orig = ', '.join([str(i) for i in pass_list]) #Format - not a list for printing
    print("Original List: " + str(orig))
    sorted = insertion_sort(pass_list) #Format - not a list for printing
    sorted = ', '.join([str(i) for i in sorted])
    print("Sorted List: " + str(sorted))
    print("Mean Value: " + str(calculate_mean(pass_list)))