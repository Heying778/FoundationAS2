#pre for AS2
#Section 2
#2.1
def isogram_checker(word):
    word = word.lower() # case sensitive
    letters = set()

    for letter in word:
        if letter in letters:
            return False
        else:
            letters.add(letter)
    return "This is Isogram!"



 
print(isogram_checker("Machine"))