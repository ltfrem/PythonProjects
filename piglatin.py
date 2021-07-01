def consonant(word):
    if word[1] in vowels: 
        pre_letters = word[:1] #Take first character off
        after = word[1:] #This is the word with beginning taken off
        update_word = after + pre_letters + 'ay'
    elif word[2] in vowels: 
        pre_letters = word[:2] #Take first 2 characters off
        after = word[2:] 
        update_word = after + pre_letters + 'ay'
    elif word[3] in vowels: 
        pre_letters = word[:3] #Take first character off
        after = word[3:] 
        update_word = after + pre_letters + 'ay'
    else: #words with no vowels are unchanged
        update_word = word
    return update_word

def vowel(word):
    new_word = word + 'yay'
    return new_word

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
sentence = str(input("Enter a sentence to be converted to Pig Latin: "))
indiv_words = sentence.split() 
new_sentence = [] #Initialize list variable to hold output of functions

#This for loop differentiates between words starting with vowel or consonant
for tester in range(len(indiv_words)): 
    word = indiv_words[tester]
    try:
        if word[0] not in vowels: #If the first letter is not a vowel:
            new_word = consonant(word) 
            new_sentence.append(new_word) 
        elif word[0] in vowels: #If the first letter is a vowel:
            new_word = vowel(word) 
            new_sentence.append(new_word) 
    except IndexError:
        new_sentence.append(word)
print(' '.join(new_sentence)) #Format for printing