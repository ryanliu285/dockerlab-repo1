from string_functions import *

def main():
    phrase = input('Enter a text phrase: ')
    vowel_count = get_vowel_count(phrase)
    letter_count = get_letter_count(phrase)

    print('"{0:s}" contains {1:d} vowels'.format(phrase, vowel_count))
    print('"{0:s}" contains the following letter counts:'.format(phrase))
    for item in letter_count:
        print('{0:d} occurrence(s) of {1:s}'.format(letter_count[item], item))

main()