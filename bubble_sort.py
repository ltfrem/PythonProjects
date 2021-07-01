def bubble_sort(values, t): #values = list, t = incrementation
    length = len(values) - 1
    sorted = False
    while not sorted:
        sorted = True
        loop = 0 #Need this otherwise there are one too many iterations
        for i in range(length):
            if values[i] > values[i+1]: #If value on left is greater than on right
                sorted = False
                values[i], values[i+1] = values[i+1], values[i]
                loop += 1
                if loop == 1:
                    t += 1
                    make_print = ', '.join([str(i) for i in values])
                    test = print("Pass " + str(t) + ": " + str(make_print))
    return values, t
numbers = '';
while numbers != 'exit':
    try:
        numbers = input("Enter a comma-separated group of numbers, or Exit to quit: ")
        if numbers.lower() == 'exit':
            print("Goodbye")
            quit()
        elif numbers.lower() != 'exit':
            nums_list = numbers.split(",") #Make numbers into a list
            pass_list = []
            for i in nums_list:
                i = int(i) 
                pass_list.append(i) 
            orig = ', '.join([str(i) for i in pass_list])
            print("Original List: " + str(orig))
            output = bubble_sort(pass_list, 0)
            sorted = ', '.join([str(i) for i in output[0]])
            print("\nOriginal List: " + str(orig))
            print("Sorted List: " + str(sorted))
            print("Number of Passes: " + str(output[1]))
    except ValueError:
        print("Your input is invalid. Please try again.")
        continue