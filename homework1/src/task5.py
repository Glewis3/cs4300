def get_favorite_books():
    books = [
        "1984 by George Orwell",
        "Dune by Frank Herbert",
        "The Hobbit by J.R.R. Tolkien",
        "Fahrenheit 451 by Ray Bradbury",
        "Neuromancer by William Gibson"
    ]
    return books

def get_first_three_books(book_list):
    # slice the list from index 0 to 3
    return book_list[:3]

def get_student_database():
    database = {
        "Hannah": 1001,
        "Parker": 1002,
        "Alex": 1003
    }
    return database

def main():
    # print the first three books
    books = get_favorite_books()
    first_three = get_first_three_books(books)
    print(f"First three books: {first_three}")

if __name__ == "__main__":
    main()