import re

FIRST_ASCII_LETTER = 97


def count_text_length(text):
    length_with_space = len(text)
    length_without_space = len(text.replace(" ",""))
    return length_with_space, length_without_space


def count_text_words(text):
    text_without_extra_spaces = re.sub(" {2,} ", " ", text).strip()
    wordCount = 0
    if len(text_without_extra_spaces)>0:
        wordCount = len(text_without_extra_spaces.split(" "))
    return wordCount


def count_text_characters(text):
    letters_count = [0] * 26
    for letter in text:
        if letter.isalpha():
            letters_count[ord(letter) - FIRST_ASCII_LETTER] += 1

    letters_count_data = []
    for i in range(26):
        if letters_count[i] > 0:
            letters_count_data.append({chr(i+FIRST_ASCII_LETTER): letters_count[i] })

    return letters_count_data

