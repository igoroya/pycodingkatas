'''
Created on 30 Aug 2018

Gets a sentence and makes uppercase the three first words of that sentence

@author: igoroya
'''


def make_uppercase(word):
    new_word = ""
    if len(word) < 4:
        new_word = word.upper()
    else:
        w = []
        w.append(word[0:3].upper())
        w.append(word[3:])
        new_word = ''.join(w)

    return new_word


def get_words(sentence):
    return sentence.split(" ")


def join_sentence(words):
    sentence = []
    for word in words:
        sentence.append(word)
        sentence.append(" ")
    return ''.join(sentence)[:-1]


def put_sentence_uppercase(sentence):
    words = get_words(sentence)
    formatted_words = [make_uppercase(word) for word in words]
    return join_sentence(formatted_words)


if __name__ == '__main__':
    sentence = "My name is Igor and I am from Bergara. And this is a second sentence."
    print(sentence)
    uppercase_sentence = put_sentence_uppercase(sentence)
    print(uppercase_sentence)
