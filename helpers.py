import re


def count_text_length(text):
    length_with_space = len(text)
    length_without_space = len(text.replace(" ",""))
    return length_with_space, length_without_space


def count_text_words(text):
    text_without_extra_spaces = re.sub(" {2,} ", " ", text).strip()
    return len(text_without_extra_spaces.split(" "))

