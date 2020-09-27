def count_text_length(text):
    length_with_space = len(text)
    length_without_space = len(text.replace(" ",""))
    return length_with_space, length_without_space
