import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import task6

def test_word_count():
    count = task6.count_words("task6_read_me.txt")
    assert count == 127

def test_missing_file():
    # makes sure it handles missing files correctly
    assert task6.count_words("non_existent_file.txt") == 0