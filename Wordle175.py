class ScrabbleDict:
    """
    the __init__ function takes the size and the filename and uses it to generate a dictionary. 
    It returns nothing and uses other methods down in the code to return the value if required
    """
    def __init__(self, size, filename):
        self.size = size
        f = open(filename ,"r")
        flines = f.readlines()
        FirstWord = []
        Definition = []
        for fline in flines:
            FirstWord.append(fline[:size])
            Definition.append(fline.strip())
        self.WordDefDict = {FirstWord[i]: Definition[i] for i in range(len(flines))}
        
        #for i in range(len(self.WordDefDict)):
            #print(FirstWord[i],':', Definition[i])
        self.FinalKeys = list(self.WordDefDict.keys())
        #print(self.FinalKeys)
    """
    returns the dictionary made in the __init__
    """
    def get_dict(self):
        return self.WordDefDict
    
    """
    returns the keys made in the dictionary in the __init__ function.
    """
    def get_finalkeys(self):
        return self.FinalKeys
    """
    function to check if the word is in the keys of the dictionary
    returns True if possible
    """
    def check(self, word):
        if word in self.FinalKeys:
            return True
        
    """
    function gets the length of the dictionary, which is the same as the length of the keys.
    """
    def getSize(self):
        return len(self.WordDefDict)

    """
    function returns a sorted list of words in the dictionary starting with the character letter.
    """
    def getWords(self, letter):
        SortedWords = []
        for i in range(len(self.FinalKeys)):
            if letter in self.FinalKeys[i][0]:
                SortedWords.append(self.FinalKeys[i])
        SortedWords.sort()
        print(SortedWords)

    """
    returns the length of the words stored in the dictionary. 
    This is the value size provided when building the dictionary.
    """
    def getWordSize(self):
        return self.size
    
    """
    The strategy used here is to get a list of all the positions where a '*' is in the template, then use a loop 
    to replace the positions in the keys of the dictionary with the '*'
    then use a simple check loopp to see if the template is the same as the edited keys

    for eg:
        i have template as t**er, here i used count() to get [1,2] as pos for the '*' and named it StarPositions
        then i replace all the [1,2] of all the keys, for eg: taber becomes t**er, which is the same as the template. 
        I then append all of them to a new list for later use
    """
    def getMaskedWords(self, template):
        # some knowledge for using the enumerate function taken from stackoverflow.com
        StarPositions = [i for i, x in enumerate(template) if x == '*']
        MaskedWords = []
        #print(StarPositions)
        for j in range(len(self.FinalKeys)):
            FinalKey = list(self.FinalKeys[j])
            for i in range(len(StarPositions)):
                FinalKey[StarPositions[i]] = '*'
                StringFinalKey = ''.join(str(e) for e in FinalKey)
            MaskedWords.append(StringFinalKey)
        ReturnedWords = []        
        for n in range(len(MaskedWords)):
            if template in MaskedWords[n]:
                ReturnedWords.append(self.FinalKeys[n])
                
        return ReturnedWords, StarPositions
    
    """
    basically returns all the words in the above function
    """
    def getReturnedWords(self, template):
        ReturnedWords, StarPositions = self.getMaskedWords(template)
        return ReturnedWords
    
    """
    it is a simple loop to get all the possible words given a set of letters from the user.
    uses any() function to get the values. some knowledge taken from www.stackoverflow.com
    """
    def getConstrainedWords(self, template, letters):
        ReturnedWords, StarPositions = self.getMaskedWords(template)
        ConstrainedReturnedWords = []
        
        if len(letters) <= len(StarPositions):
            #for letter in letters:
                for j in range(len(ReturnedWords)):
                    for i in range(len(StarPositions)):
                        if all(letter in ReturnedWords[j] for letter in letters):
                            ConstrainedReturnedWords.append(ReturnedWords[j])
        
        ConstrainedReturnedWords = list(set(ConstrainedReturnedWords))
        ConstrainedReturnedWords.sort()
        return ConstrainedReturnedWords

if __name__ == "__main__":
    TheDictionary = ScrabbleDict(5, 'scrabble5.txt')
    EnglishDictionary = TheDictionary.get_finalkeys()
    print(EnglishDictionary)
    
    print(TheDictionary.get_dict())
    
        
        



        




