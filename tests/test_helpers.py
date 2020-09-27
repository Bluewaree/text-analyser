import helpers


def test_text_length_count():
    text = "a b"
    length_with_space, length_without_space = helpers.count_text_length(text)
    assert length_with_space == 3, length_without_space == 2


def test_text_words_count():
    text = "a b"
    text_with_extra_spaces = "    a b     c    "
    assert helpers.count_text_words(text) == 2
    assert helpers.count_text_words(text_with_extra_spaces) == 3

