

# 21: Create a FileManager with methods to read from and write to a file.

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, content):
        with open(self.filename, "w") as file:
            file.write(content)
            print("added")

    def read_from_file(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                return content
        except:
            print("no find")
            return none

file = FileManager("aaa.txt")
file.write_to_file("this is a instance")
file.read_from_file()
