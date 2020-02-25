from spellchecker import SpellChecker
import os

spell = SpellChecker()
wordslist = []
fileList = []
total = 0

def check_from_paragraph():
    text = str(input("Enter The Paragraph: "))
    print()
    textList = text.split(' ')
    for word in textList:
        correct = spell.correction(word)
        if word == correct:
            wordslist.append(word)
        elif word != correct:
            print("'{}' Is not spelt correctly. I think you meant '{}' \n".format(word, correct))
            wordslist.append(correct)
    
    print("Corrected output: \n" + ' '.join(wordslist))

def check_from_file():
    file_name = input("Enter The Name of the File: ")    
    file = open(file_name)
    for word in file:
        fileList = word.split(' ')
    file.close()
    for word in fileList:
        correct = spell.correction(word)
        if word == correct:
            wordslist.append(word)
        elif word != correct:
            print("'{}' Is not spelt correctly. I think you meant '{}' \n".format(word, correct))
            wordslist.append(correct)
    print("Corrected output: \n" + ' '.join(wordslist))

def main():
    print("Welcome to the Python Spell Check Program!")
    print()
    print("1. Enter a Paragraph")
    print("2. Check Spelling from a text file.")
    print()
    choice = str(input("Enter Your Choice: "))

    if choice == "1":
        check_from_paragraph()
    
    elif choice == "2":
        check_from_file()

    else:
        print("Wrong Choice Entered, Exiting the Program....")
        exit()

main()