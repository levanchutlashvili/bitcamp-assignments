from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("ghtrk") == "ghtrk"

def test_shorten_only_vowels():
    assert shorten("aeiouAEIOU") == ""
def test_shorten_mixed():
    assert shorten("hello world") == "hll wrld"

def test_shorten_single_vowels():
    assert shorten("a") == ""
    assert shorten("e") == ""
    assert shorten("i") == ""
    assert shorten("o") == ""
    assert shorten("u") == ""

def test_shorten_empty():
    assert shorten("") == ""