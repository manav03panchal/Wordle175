from Wordle175 import ScrabbleDict
import random

"""
this function gets us a random word from the list of words we deduced from the clean.py and initiated in Wordle175.py
uses the random library
"""
def HiddenWord(aList):
    HiddenWord = random.choice(aList)
    return HiddenWord

"""
now this function is the one where if there are repeating letters in a word, it assign a number to it and generates a new list
some syntax taken from www.stackoverflow.com and kite.com
"""
def CheckRepeat(someList):
    InputList = list(someList.upper())
    UniqueValues = set(InputList)
    for x in UniqueValues:
        number = 0
        for i in range(0,len(InputList)):
            if InputList[i] == x:
                number += 1
                if number >= 2:
                    InputList[i] += str(number)
    
    return InputList

"""
This function tells the program if there are any words repeated by the user
"""
def CheckIfInputRepeat(AllUserInputs):
    for i in range(len(AllUserInputs)):
        if AllUserInputs.count(AllUserInputs[i]) > 1:
            return True

"""
this is the main program which assigns the leters in a word to red, orange or green
and also prints the result.

"""
def RedOrangeGreen(HiddenWord, UserInput, Feedbacks):
    
    HiddenWordList = CheckRepeat(HiddenWord)
    UserInputList = CheckRepeat(UserInput)
    GreenList = []
    for i in range(len(UserInputList)):
        if UserInputList[i] == HiddenWordList[i]:
            GreenList.append(UserInputList[i])
            GreenList.sort()
    
    
    if len(GreenList) == len(HiddenWord):
        return True

    OrangeList = []
    for i in range(len(UserInputList)):
        if UserInputList[i] in HiddenWordList and UserInputList[i] != HiddenWordList[i]:
            OrangeList.append(UserInputList[i])
            OrangeList.sort()
    
    
    RedList = []
    for i in range(len(UserInputList)):
        if UserInputList[i] not in HiddenWordList:
            RedList.append(UserInputList[i])
            RedList.sort()
    
    Feedbacks.append([UserInput.upper(),', '.join(GreenList),', '.join(OrangeList),', '.join(RedList)])
    
    
    for i in range(len(Feedbacks)):
        print("%s Green={%s} - Orange={%s} - Red={%s}" % (Feedbacks[i][0], Feedbacks[i][1], Feedbacks[i][2], Feedbacks[i][3]))
    
    

"""
this function incorporates the upper functions in some way to finally provide the user with a running program.
"""
def gameLogic(HiddenWord, TheDictionary):
    count = 1
    game_running = True
    Feedbacks = []
    AllUserInputs = []
    while game_running:
        UserInput = str(input(f'Attempt {count}: Please enter a five-letter word: ')).lower()
        
        
        if len(UserInput) > len(HiddenWord):
            print(f'{UserInput.upper()} is too long')
        elif len(UserInput) < len(HiddenWord):
            print(f'{UserInput.upper()} is too short')
        elif len(UserInput) == len(HiddenWord) and not TheDictionary.check(UserInput):
            print(f'{UserInput.upper()} is not a recognized word')
        else:
            AllUserInputs.append(UserInput)
            if CheckIfInputRepeat(AllUserInputs):
                print(f'{AllUserInputs[-1].upper()} was already entered')
                AllUserInputs.pop()
                count -=1

            elif RedOrangeGreen(HiddenWord, UserInput, Feedbacks):
                print(f'Found in {count} attempts. Well Done. The Word is {HiddenWord.upper()}')
                game_running = False
            count += 1
        if count == 7:
            print(f'Sorry you lose. The word is {HiddenWord.upper()}')
            game_running = False
     


def main():
    TheDictionary = ScrabbleDict(5, 'scrabble5.txt')
    EnglishDictionary = TheDictionary.get_finalkeys()
    RandomWord = HiddenWord(EnglishDictionary)
    gameLogic(RandomWord, TheDictionary)
    

main()