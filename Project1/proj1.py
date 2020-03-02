# File: proj1.py
# Author: MAHMOOD UL MOHASIN AZIZ
# Description: 
# This text file contains the design for project1
# python code that helps user learn the pronounciation
# of hawaiian phrases by entering them.

# info for getting choices.
ANSWERS = ["y","yes","n","no"]
EXIT = ["n", "no"]
QUESTION = "Do you want to enter another word? "
OPTIONS = "(y/yes/n/no): "

# info about characters.
OKINA = "'"
CONSTANT_W = "w"

VOWELS = ["a", "e", "i", "o", "u"]
VOWELS_HAWAIIAN = ["ah", "eh", "ee", "oh", "oo"]

COMP_VOWELS = ["ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui"]
COMP_VOWELS_HAWAIIAN = ["eye", "eye", "ow", "ow","ay", "eh-oo", "ew", "oy", "ow","ooey"]

CONSONANTS = ["h", "k", "l", "m", "n", "p",CONSTANT_W,OKINA]

# input validation.
INPUT_VALID = VOWELS + CONSONANTS

########################################################
################### HELPER FUNCTIONS ###################

########################################################

# getChoice() prompts and reprompts the user until
#             they select a valid choice
# Parameters: question; a string to be asked
#             options; a list of string options
# Return:     choice; a string chosen by the user

def getChoice(question, options):

# prompting the user and providing options.
    
    askQuest = input(question+options)
    choice = askQuest.lower()

# running loop to get the right input.

    while choice not in ANSWERS:
        print("Enter",OPTIONS[1:11])
        askQuest = input(question+options)
        choice = askQuest.lower() 

# returning the choice.

    return choice

########################################################

# getHawaiianPhrase() prompts and reprompts the user
#                     until they enter a valid a hawaiian
#                     phrase.
# Parameters:         takes no input.
# Return:             returns string of the chosen
#                     hawaiian phrase.
    
def getHawaiianPhrase():

    counter = 1

# runnning the loop until the user enter the correct
# input.

    while counter != 0:
        getString = input("Enter a hawaiian phrase to pronounce: ")
        
        strLower = getString.lower()
        strSplit = strLower.split()
        
        counter  = 0

        # running the loop to check if last letter is a vowel.
        index = 0
        while index < len(strSplit):
            strCheck = strSplit[index][(len(strSplit[index]) - 1)]
            if strCheck not in VOWELS:
                print("The word",strSplit[index],"does not end in a vowel")
                counter += 1
            index += 1

        # running a loop to print the invalid letters.
        count = 0
        while count < len(getString):
            if strLower[count] not in INPUT_VALID and strLower[count] != ' ':
                print("The letter",getString[count],"is not valid")
                counter += 1
            count += 1

    # returning the validated input in lower case.        
    return getString.lower()

#######################################################

# pronounceW() decides how to pronounce the letter 'w',
#              if the string has the letter 'w' in
#              it.
# Parameters:  word; takes in the only string that has
#                    the letter 'w' in it.
#              index; the integer of the index, in a
#                     string where 'w' is at.
# Return:      character; a single character string with
#                         either 'v' or 'w' in it
#                         depending on the pronunciation.

def pronounceW(word,index):

    # checking if the following letter is a vowel
    # to change 'w' to 'v' and return.
    
    if word[index + 1] in VOWELS:
        character = "v"
        return character
    
    else:
        return word[index]

#######################################################

# simpleVowel() decides the pronunciation of a vowel.
# Parameters:   letter; takes a single character string.
# Return:       vowel1; a string, how the vowel is
#                       is pronounced.

    
def simpleVowel(letter): 

    # using loop to check if the input letter is in VOWELS
    # and replacing them with pronounciation and returning
    # as a string.
    
    vowel1 = ""
    index = 0
    while index < len(VOWELS):
        if VOWELS[index] == letter:
            vowel1 = VOWELS_HAWAIIAN[index]
            return vowel1
        index += 1
        
########################################################

# complexVowel() decides the pronunciationn of
#                string that has two vowels in it.
# Parameters:    vowels; takes in the string that
#                        has two in it.
# Return:        vowel2; a string, how two vowels
#                        in a string are pronounced.

def complexVowel(vowels):

    # using loop to check if the input letters are in
    # COMP_VOWELS and replacing them with pronounciation
    # and returning them as a string. 

    vowel2 = ""
    index = 0
    while index < len(COMP_VOWELS):
        if COMP_VOWELS[index] == vowels:
            vowel2 = COMP_VOWELS_HAWAIIAN[index]
            return vowel2
        index += 1

########################################################
################### GENERAL FUNCTIONS ##################

########################################################

# pronounce() decides how to pronounce the entire
#             phrase.
# Parameters: phrase; takes a string of multiple words.
# Return:     complete; string with complete phrase's
#                       pronunciation.
        
def pronounce(phrase):

    # using for loop to call the function pronounceWord
    # and send in the word that is needed to translated
    # in hawaiian and return the complete pronounciation
    # as a string.
    
    complete = ""
    words = phrase.split(" ")
    for i in range(len(words)):
        complete += pronounceWord(words[i])
        complete += " "

    # returning the final pronounciation to the main
    # as a string.
    return complete

#######################################################

# pronounceWord() decides how to pronounce a single
#                 word.
# Parameters:     word; takes in a string with no
#                       space.
# Return:         strWord; a string, that has the word's
#                          pronunciation.
            
def pronounceWord(word):

    # initializing empty list and string variables
    # that will be used further in this function.
    
    myList = []
    strWord = ""
    tempStr = ""

    # running while loop to check the letters in both
    # VOWLES and the COMP_VOWELS.
    
    index = 0
    while index < len(word) - 1:
        if word[index] in VOWELS:
            string = word[index] + word[index+1]

            # adding up the index and checking
            # two letters at a time by calling
            # complexVowel().
            if string in COMP_VOWELS:
                callComp = complexVowel(string)
                tempStr += callComp
                myList.append(tempStr)
                tempStr = ""
                index += 1   

            # if not complex then checking single
            # letter by calling simpleVowel().
            else:
                strBack = simpleVowel(word[index])
                tempStr += strBack
                myList.append(tempStr)
                tempStr = ""

        # checking 'w' and its index before calling the
        # function pronounceW().
        elif word[index] == CONSTANT_W and index > 1:
            strBack = pronounceW(word, index) 
            tempStr += strBack

        # if not a vowel then concatentate the
        # letter to the empty string.
        else: 
            tempStr += word[index]
        
        index += 1

    # using if statement to check and replace the end
    # vowel by calling simpleVowel() again.
    
    if index < len(word):
        strBack = simpleVowel(word[index])
        tempStr += strBack
        myList.append(tempStr)

    # using for loop to check if there is OKINA in between
    # and concatenate the hyphen to the pronounciation
    # accordingly.

    for i in range(len(myList)):
        if i < (len(myList)-1) and myList[i+1][0] != OKINA:
            strWord += myList[i] + "-"
        else:
            strWord += myList[i]

    # returning the final pronounciation as a string.
    return strWord

#######################################################
################# MAIN FUNCTION #######################

def main():

    # call getPhrase() to get the valid input. 
    getPhrase = getHawaiianPhrase()

    # call getProunce() once the valid input is
    # entered.
    getPronounce = pronounce(getPhrase)

    # using variable to turn the entered string
    # to uppercase.
    inputUp = getPhrase.upper()

    # printing the final output.
    print("The phrase",inputUp,"is pronounced: ")
    print("\t" + getPronounce) 

    # using while loop to ask the user if they want
    # to enter once again and if yes repeat the process
    # and if not quit.
    while getChoice(QUESTION, OPTIONS) not in EXIT:

        getPhrase = getHawaiianPhrase()
        getPronounce = pronounce(getPhrase)    
        inputUp = getPhrase.upper()
        print("The phrase",inputUp,"is pronounced: ")
        print("\t" + getPronounce) 

main()
