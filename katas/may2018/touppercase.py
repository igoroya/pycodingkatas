'''
Created on 9 May 2018

@author: igoroya
'''


def capitalize_letters(sentence, letters_in_word):
        '''
        Converts the first N letters of each word of a sentence to upper case

        Input parameters:
        sentence - original sentence
        letters_in_word - the number of 1st letters in each word

        Return parameters:
        The reformatted sentence
        '''
        newSentence = ''
        for word in sentence.split(sep=' '):
            first = word[:letters_in_word].upper()
            last = word[letters_in_word:].lower()
            new_word = first + last
            newSentence += new_word
            newSentence += ' '
        return newSentence


if __name__ == '__main__':
    sentence = input('Please add your sentence\n')
    capilatized_sentence = capitalize_letters(sentence, 3)
    print(capilatized_sentence)
