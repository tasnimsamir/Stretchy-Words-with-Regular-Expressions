#Done by: Tasnim Samir Mohamed
#Contact:telsa087@uottawa.ca
#Subject code: DTI5125
#Assignment 1

import re

class StretchyWords():
    def __init__(self, words_list = [] , string="" , pattern = r'([a-z])\1{2,100}'):

        self.words_list = words_list

        self.string = string.lower() #all string consist only of lowercase letters

        self.pattern = re.compile(pattern)
        self.constraints()

    def constraints(self):
        #1 put constraints on the length of list of the words , 0 <= len(words) <= 100.
        if (len(self.words_list) > 100):
            self.words_list = self.words_list[0:100] #
        elif (len(self.words_list)<=0):
            print("please fill the list with suggested words..")
            self.words_list = []
        #2  put constraints on the length of characters of the string , 0 <= len(S) <= 100.
        if (len(self.string) > 100):
            self.string = self.string[0:100]
        elif (len(self.string) <= 0):
            print("please enter the string!")
            self.string = []
        #3 put constraints on the length of characters of the words inside words_list , 0 <= len(words[i]) <= 100.
        for i in range(len(self.words_list)):
            self.words_list[i] = self.words_list[i].lower() #all words in words consist only of lowercase letters
            if (len(self.words_list[i]) > 100):
                self.words_list[i] = self.words_list[i][0:100]  #
            elif (len(self.words_list[i]) <= 0):
                print("please fill the list with suggested words..")
                self.words_list[i] = []
    def extract_repeated_chars(self): # extract a list of repeated characters
        repeated_chars = re.findall(self.pattern, self.string)
        return repeated_chars
    def extract_main_word(self): #extract the main word without repeated characters
        self.main_word = re.sub(self.pattern, r'\1', self.string)
        return self.main_word
    def occurence_number(self): #returns the number of occurence of the main word in the words list
        occurence_number = len([i for i in self.words_list if i == self.main_word])
        return occurence_number


#================================================================================================================
#Example
words_list=['hello','hi','helo']
S = 'heeeellooooooooooo'
strtchyWords = StretchyWords(words_list= words_list, string= S, pattern= r'([a-z])\1{2,100}')
main_word = strtchyWords.extract_main_word()
repeated_chars = strtchyWords.extract_repeated_chars()
freq = strtchyWords.occurence_number()
print("Input:")
print("words list = ",words_list)
print("String: ", S)
print("\nOutput:")
print("The main word is:" , main_word)
print("Repeated Characters:  ", repeated_chars)
print("Number of occurence in words list = ", freq)
