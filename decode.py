#First part: need to convert letters to morse code
morse_dict = { 'A':'.-', 'B':'-...', 
               'C':'-.-.', 'D':'-..', 'E':'.', 
               'F':'..-.', 'G':'--.', 'H':'....', 
               'I':'..', 'J':'.---', 'K':'-.-', 
               'L':'.-..', 'M':'--', 'N':'-.', 
               'O':'---', 'P':'.--.', 'Q':'--.-', 
               'R':'.-.', 'S':'...', 'T':'-', 
               'U':'..-', 'V':'...-', 'W':'.--', 
               'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ':' ' } #Equate letters to morse code value
string = input("Enter a word or phrase to convert into Morse code: ")
def letter_list(word): #Break the input apart into individual letters
    word = word.upper() #Capitalize user's input so it can match in morse_dict
    letters = [] #Initialize letters list
    for letter in word: #Break apart the input into individual characters
        letters.append(letter) #Append each letter to the letters list
    return letters
ll = letter_list(string) # ll variable holds the list of letters in the input string after letter_list function has been invoked
def convert(text): 
    output = "" #Initialize output variable where converted text will go as an empty string
    for item in text: #Take every letter of the string and...
        output = morse_dict[item] #Assign output the value of a letter converted to a morse value
        break #Only do one letter at a time
    return output
#Second part: configure blinking    
import RPi.GPIO as GPIO #Import module to control GPIO ports
import time #Import time module
GPIO.setmode(GPIO.BOARD) #Invoke setmode method of GPIO, declare which pin numbering mode to be used
GPIO.setup(11,GPIO.OUT) #Configure pin 11 as the output channel    
def dot(): #Declare dot function
    print('.')
    GPIO.output(11, True) #Pin 11 light on
    time.sleep(0.2) # 0.2 second LED on for a dot
    GPIO.output(11, False) #Turn light off for 0.1 sec
    time.sleep(0.1) #Brief sleep before processing next morse value
def dash():
    print('-')
    GPIO.output(11, True) #Pin 11 light on
    time.sleep(0.5) # 0.5 seconds LED on for a dash
    GPIO.output(11, False) #Turn light off for 0.1 sec
    time.sleep(0.1) #Brief sleep before processing next morse value
def space():
    print(' ')
    GPIO.output(11, False) #Light off
    time.sleep(1) #1 sec off for a space
    GPIO.output(11, False) #Turn light off for 0.1 sec
    time.sleep(0.1) #Brief sleep before processing next morse value
for letter in ll: #For every letter in the ll variable
    print(letter)
    morse = convert(letter) #Invoke convert function to change a letter to a morse value
    for i in morse: #For every . or - in a letter, do one of these
        if i == '.':
            dot() 
        elif i == '-':
            dash() 
        elif i == ' ':
            space() 
    GPIO.output(11, False) #After each for loop execution...
    time.sleep(1.5) #Light off for 1.5 sec between each letter