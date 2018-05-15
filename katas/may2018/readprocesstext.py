'''
Created on 15 May 2018

@author: igoroya
'''


def read_text(file_path):

    my_file = open(file_path, 'r', encoding="utf-8")
    text = my_file.read()
    my_file.close()
    return text

def print_text(text):
    print(text)

def get_lines(text):
    return text.split("\n")


def get_words(text):
    words = []
    lines = get_lines(text)
    for entry in lines:
        for w in entry.split(" "):
            words.append(w)
    return words


def get_letters(text):
    letters = []
    words = get_words(text)
    for w in words:
        for letter in w:
            letters.append(letter)
    return letters


def print_words(words):
    for word in words:
        print(word)


def get_text_stats(text):
    lines = len(get_lines(text))
    words = len(get_words(text))
    letters = len(get_letters(text))
    print('Text Stats')
    print('lines: {}, words: {}, letters: {}'.format(lines, words, letters))


def find_letter_occurences(text):
    letter_set = set(get_letters(text.lower()))
    letter_occurence = dict()
    for letter in letter_set:
        letter_occurence[count_occurrences(text, letter)] = letter
    print(sorted(letter_occurence))
    print('Occurrence of letters')
    print('Letter: times')
    for key in sorted(letter_occurence, reverse=True):
        print("%s: %s" % (letter_occurence[key], key))


def count_occurrences(text, letter):
    return text.count(letter)


if __name__ == '__main__':
    text = read_text('Text')
    get_text_stats(text)
    print()
    find_letter_occurences(text)
