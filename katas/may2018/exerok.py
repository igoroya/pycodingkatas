'''
Created on 22 May 2018

Reverse the word order in a csv string (with ";" separator),
keeping the letters in proper order in eqach word

(Proper solution)

@author: igoroya
'''


def reorder_char_array(char_array):
    words = char_array.split(';')
    rev_words = ''
    for w in reversed(words):
        rev_words += w
        rev_words += ';'
    rev_words = rev_words[:-1]
    return rev_words


if __name__ == '__main__':
    char_array = "today;is;tuesday"
    rev_text = reorder_char_array(char_array)
    print(rev_text)
