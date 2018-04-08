'''
Created on 8 Apr 2018

Makes the three first letters of each word upper case

@author: igoroya
'''


def make_uppercase(sentence):
    '''
    Sentence is a string
    '''
    words = sentence.split(' ')

    adapted_sentence = ''

    for word in words:
        word_start = word[0:3]
        word_end = word[3:]
        new_word = word_start.upper() + word_end
        adapted_sentence = adapted_sentence + new_word + ' '

    return adapted_sentence


if __name__ == '__main__':
    sentence = 'This is a sentence that you need to process'
    print('Original sentence: ' + sentence)
    new_sentence = make_uppercase(sentence)
    print('Processed sentence: ' + new_sentence)
