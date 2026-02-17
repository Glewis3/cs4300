import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import task5

def test_books_list():
    books = task5.get_favorite_books()
    
    # it should be a list and have enough items
    assert isinstance(books, list)
    assert len(books) >= 3

def test_books_slicing():
    books = task5.get_favorite_books()
    first_three = task5.get_first_three_books(books)
    
    # slicing should return exactly 3 items
    assert len(first_three) == 3
    
    # the items should match the first three of the original list
    assert first_three == books[0:3]

def test_student_dictionary():
    db = task5.get_student_database()
    
    # it should be a dictionary
    assert isinstance(db, dict)
    
    # check if we can look up a value by key
    assert "Hannah" in db
    assert db["Hannah"] == 1001