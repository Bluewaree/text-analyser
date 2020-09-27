from helpers import count_text_length

def test_text_length_count():
    text = "a b"
    length_with_space, length_without_space = count_text_length(text)
    assert length_with_space == 3, length_without_space == 2
