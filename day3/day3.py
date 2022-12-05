# Day 3 in Advend of Code :p

import string

def getRepeatedItem(rucksack):
    if "\n" in rucksack:
        rucksack = rucksack[:-1]
    
    length = len(rucksack)
    half = int(length/2)
    # if (length % 2) != 0: # is even?
    #     half += 0.5
    head = rucksack[:half]
    tail = rucksack[half:]

    for letter in head:
        if letter in tail:
            return letter

def getRepeatedItemPriority(rucksack1, rucksack2, rucksack3):
    for letter in rucksack1:
        if letter in rucksack2:
            if letter in rucksack3:
                return letter
    
def getLetterValue(letter):
    try:
        return string.ascii_lowercase.index(letter) + 1
    except:
        return string.ascii_uppercase.index(letter) + 27

def getTotal(rucksacks):
    total = 0
    for rucksack in rucksacks:
        total += getLetterValue(getRepeatedItem(rucksack))
    return total

def getTotalPriorities(rucksacks):
    totalPriorities = 0

    numberOfPacks = int(len(rucksacks) / 3)
    for i in range(numberOfPacks):
        offset = i * 3
        totalPriorities += getLetterValue(getRepeatedItemPriority(rucksacks[offset - 3], rucksacks[offset - 2], rucksacks[offset - 1]))
    return totalPriorities

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        rucksacks = file.readlines()
        print("Total is ", getTotalPriorities(rucksacks))
        