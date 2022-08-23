from operator import le


def freq(inputStr:str) -> str:
    letters = {}
    res = ""
    
    # initializes the keys in dictionary
    for char in inputStr:
        letters[char] = 0
    
    # track letter occurence(s) by iterating through the string
    for char in inputStr:
        letters[char] += 1

    # sort dictionary
    sortedLetters = sorted(letters.items())

    #print key(letter) and value(occurence) of the ictionary
    for value in sortedLetters:
        res += value[0] + str(value[1])

    return res