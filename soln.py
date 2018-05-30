# Enter your code here. Read input from STDIN. Print output to STDOUT


# https://upload.wikimedia.org/wikipedia/commons/d/da/KB_United_States.svg

# saw
# as
# because bob is bumbling, he forgets about repeated letters
# so you don't have worry about finding words with repeated letters such as  - "weed"

# Rows
# 10
# 9
# 7

# Generate Randoms keys and compares them against standard QWERTY
# Count words
# words vector
# count words in vector that can be spelled with adjacent keys
# take one set of adacent keys, and see how many words can be made from it

import random

words = ["a", "ad", "saw", "zoo"]  # all the words in the english language
original_keyboard = [list('qwertyuiop'), list('asdfghjkl'), list('zxcvbnm')]




def count_words(keySet, words):
    count = 0
    for word in words:
        hold = True
        for letter in list(word):
           if letter not in keySet:
               hold = False
               break
        if hold:
            count +=1
            
    return count
    
# test each keySet with count_words

def keySet(keyboard):
    ## Returns list of adjacent keys from random spot
    
    # Random Row
    row = int(random.randrange(3)) #0-2
    
    letterCol = int(random.randrange(len(keyboard[row])))
    
    keys = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 1 and j == 1:
                continue            ## prevents "c" from being adjacent to "s"
            if i == -1 and j == -1:
                continue            ## prevents "q" from being adjecent to "s"
            if (row + i >= 0) and (letterCol + j >= 0):
                try:
                    keys.append(keyboard[row + i][letterCol + j])
                
                except IndexError:
                    pass
    print(keyboard[row][letterCol])           
    print(keys)
    return keys
    
def keySet_letter(keyboard, letter):
    ## Returns list of adjacent keys from random spot
    
    # Random Row
    row = letter[0]
    
    letterCol = letter[1]
    
    keys = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 1 and j == 1:
                continue            ## prevents "c" from being adjacent to "s"
            if i == -1 and j == -1:
                continue            ## prevents "q" from being adjecent to "s"
            if (row + i >= 0) and (letterCol + j >= 0):
                try:
                    keys.append(keyboard[row + i][letterCol + j])
                
                except IndexError:
                    pass
    print(keyboard[row][letterCol])           
    print(keys)
    return keys
    
def generate_keyboard():
    ## Returns random keyBoard
    return 
    
print(count_words(keySet(original_keyboard), words))