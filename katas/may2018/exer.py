'''
Created on 22 May 2018


Reverse the word order in a csv string (with ";" separator),
keeping the letters in proper order in each word

(Solution I handed in a code interview)

@author: igoroya
'''


def reorder_char_array(char_array):
    new_array = ''
    temp_string = ''
    words = []

    for c in char_array:
        temp_string = temp_string + c
        if c == ';':
            temp_string = temp_string[:len(temp_string) - 1]
            new_array += temp_string
            words.append(new_array)
            new_array = ''
            temp_string = ''

    new_array += temp_string
    words.append(new_array)
    new_array = ''
    temp_string = ''

   
    n_words = len(words)

    rev_text = ''

    for i in reversed(range(0, n_words)):
        rev_text += words[i]
        rev_text += ';'

    rev_text = rev_text[:len(rev_text) - 1]
    return rev_text


if __name__ == '__main__':
    char_array = "today;is;tuesday"
    print(char_array)
    rev_text = reorder_char_array(char_array)
    print(rev_text)
