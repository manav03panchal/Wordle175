from Wordle175.Wordle175 import ScrabbleDict
"""
gets the statistics as required in task 5. uses simple list manipulation to get the answer
"""
def statistics(aList):
    theWordsasString = str(''.join(aList))
    theWordsasString = sorted(theWordsasString)
    theWordsasString = ''.join(theWordsasString)
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    LetterOccurrences = []
    for i in range(len(alphabet)):
        LetterOccurrences.append(theWordsasString.count(alphabet[i]))
    
    LetterOccurrencesPercent = [(i/len(theWordsasString))*100 for i in LetterOccurrences]
    
    for i in range(len(alphabet)):
        print(f'{alphabet[i].upper()}:{"{:>6}".format(LetterOccurrences[i])}{"{:>6}".format(round(LetterOccurrencesPercent[i],2))}%  {"{:<10}".format("*"*(round(LetterOccurrencesPercent[i])))}') 
        
"""
using all the functions in the main.py. this program first displays the statistics mentioned above, and then asks
the user for a template and a letter, based on which the words are returned.
"""
def main():
    SomeStuff = ScrabbleDict(5, 'scrabble5.txt')
    AllKeys = SomeStuff.get_finalkeys()
    statistics(AllKeys)
    template = str(input('Enter your template here: ')) 
    letters = list(str(input('Enter your letters here: ')))
    SomeStuff.getMaskedWords(template)
    print('Here are all the words possible in your template:')
    print('')
    MaskedWords = SomeStuff.getReturnedWords(template)
    print(*MaskedWords, sep = "\n")
    print('')
    print('Here are all the words possible with the letters you have entered:')
    print('')
    ConstrainedWords = SomeStuff.getConstrainedWords(template, letters)
    print(*ConstrainedWords, sep="\n")


main()