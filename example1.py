
def count_vowels(string):
    listOfVowels = ['a', 'o', 'e', 'i', 'u']
    count = 0
    for character in string.lower():
        if character in listOfVowels:
            count += 1
    return count

count_vowels('reza hosseini VEDAD')