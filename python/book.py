class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages long."
    


book= Book("One Thousand and One Nights", "Anonymous Authors", 300)


print(book.describe())


