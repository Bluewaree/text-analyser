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


def test_text_characters_count():
    text = " a bb ccc dddd zzzzz!"
    data = helpers.count_text_characters(text)

    assert len(data) == 5
    assert data[0]["a"] == 1
    assert data[1]["b"] == 2
    assert data[2]["c"] == 3
    assert data[3]["d"] == 4
    assert data[4]["z"] == 5

