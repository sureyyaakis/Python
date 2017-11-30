#Sureyya Betul Akis
#Assingment 4

global lines
global words
global longest_word_found
global max_len
global line_number

def main():
    global lines
    global words
    lines = [line.rstrip('\n') for line in open('file1.txt', 'r')]
    words = []
    for line in lines:
        words += line.split()

    longest_word()
    length_word()
    lineNumber()
    print("The longest word:", longest_word_found,", The length of word:", max_len , ", The line number of the longest word:", line_number)
    secondFile()

def longest_word():
    global words
    global longest_word_found
    longest_word_found = max(words, key=len)

def length_word():
    global words
    global longest_word_found
    global max_len
    max_len = len(longest_word_found)

def lineNumber():
    global words
    global longest_word_found
    global line_number
    for num, line in enumerate(words, 1):
        if longest_word_found in line:
            line_number = num

def secondFile():
    global words
    global longest_word_found
    file2 = open('file2.txt', 'w')

    for num, word in enumerate(words, 1):
        if word == longest_word_found:
            rest = ' '.join(words[num-1:])
    file2.write(rest)
    file2.close()

main()