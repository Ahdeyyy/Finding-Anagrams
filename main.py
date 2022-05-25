# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def remove_whitespace(word):
    stripped_word = ""
    for letter in word:
        if letter != " ":
            stripped_word += letter

    return stripped_word

def find_anagram(word, anagram):
    # [assignment] Add your code here

    #remove whitespaces from anagram and word 
    stripped_word = remove_whitespace(word.lower())
    stripped_anagram = remove_whitespace(anagram.lower())

    if len(stripped_anagram) != len(stripped_word):
        return False

    #checks if all letters in the word and anagram appear the same times in both of them
    for letter in word:
        if stripped_word.count(letter) != stripped_anagram.count(letter):
            return False
    
    return True

#test cases
print(find_anagram("liSteN dim","silent mid"), " --> True")
print(find_anagram("listen dim","silent mid"), " --> True")
print(find_anagram("stool","tools") , " --> True")
print(find_anagram("secure","rescue"), " --> True")
print(find_anagram("Eleven plus two","Twelve plus one")," --> True")
print(find_anagram("zuri training","ingressive for good"), "--> False")
print(find_anagram("hello", "check"),"--> False")
print(find_anagram("below", "elbow")," --> True")