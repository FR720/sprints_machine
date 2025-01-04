  

# Requirement 1 
from collections import Counter

def count_word_frequencies(file_path):
    """
    Reads a text file and counts the frequency of each word using the Counter class.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            words = text.split()
            word_count = Counter(words)
            return word_count
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."

 

# Requirement 2 
from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'year', 'isbn'])

def create_book(title, author, year, isbn):
    """
    Creates a namedtuple instance for storing book information.
    """
    return Book(title=title, author=author, year=year, isbn=isbn)

 
book1 = create_book("1984", "George Orwell", 1949, "1234567890")
book2 = create_book("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321")
print("Book 1:", book1)
print("Book 2:", book2)

 