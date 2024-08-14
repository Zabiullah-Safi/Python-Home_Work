
# 16: Create a Library with attributes name and books(a list of Book object). Provide methods
# to add and remove books.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add(self, book):
        return self.books.append(book)

    def remove(self, book):
        return self.books.remove(book)

    def detail(self):
        print(f"{self.name}\n{self.books}")
l = Library("Library")
l.add("1 added")
l.add("2added")
l.detail()
l.remove("1 added")
l.detail()

# fibonacci sequence

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a+b

n = int(input("Enter a number:"))
print(fibonacci(n))
