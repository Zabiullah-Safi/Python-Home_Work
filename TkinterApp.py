
# TkinerApp


from tkinter import *
root = Tk()
root.title("Python Homework")
root.geometry("1500x1500")

def Builtin():
    root = Tk()
    root.title("Built_in Funbtion")
    root.geometry("1500x1500")
    l5 = Label(root, text="Built_in Functions\nPython abs()"
"returns absolute value of a number"
"** Python all()"
"returns true when all elements in iterable is true\n"
"** Python any()"
"Checks if any Element of an Iterable is True"
"** Python ascii()"
"Returns String Containing Printable Representation\n"
"** Python bin()"
"converts integer to binary string"
"** Python bool()"
"Converts a Value to Boolean\n"
"** Python bytearray()"
"returns array of given byte size"
"** Python bytes()"
"returns immutable bytes object\n"
"** Python callable()"
"Checks if the Object is Callable"
"** Python chr()"
"Returns a Character (a string) from an Integer\n"
"** Python classmethod()"
"returns class method for given function"
"** Python compile()"
"Returns a Python code object\n"
"** Python complex()"
"Creates a Complex Number"
"** Python delattr()"
"Deletes Attribute From the Object\n"
"** Python dict()"
"Creates a Dictionary"
"** Python dir()"
"Tries to Return Attributes of Object\n"
"** Python divmod()"
"Returns a Tuple of Quotient and Remainder"
"** Python enumerate()"
"Returns an Enumerate Object\n"
"** Python eval()"
"Runs Python Code Within Program"
"** Python exec()"
"Executes Dynamically Created Program\n"
"** Python filter()"
"constructs iterator from elements which are true"
"** Python float()"
"returns floating point number from number, string\n"
"** Python format()"
"returns formatted representation of a value"
"** Python frozenset()"
"returns immutable frozenset object\n"
"** Python getattr()"
"returns value of named attribute of an object"
"** Python globals()"
"returns dictionary of current global symbol table\n"
"** Python hasattr()"
"returns whether object has named attribute"
"** Python hash()"
"returns hash value of an object\n"
"** Python help()"
"Invokes the built-in Help System"
"** Python hex()"
"Converts to Integer to Hexadecimal"
"** Python id()"
"Returns Identify of an Object\n"
"** Python input()"
"reads and returns a line of string"
"** Python int()"
"returns integer from a number or string\n"
"** Python isinstance()"
"Checks if a Object is an Instance of Class"
"** Python issubclass()"
"Checks if a Class is Subclass of another Class\n"
"** Python iter()"
"returns an iterator"
"** Python len()"
"Returns Length of an Object\n"
"** Python list()"
"creates a list in Python"
"** Python locals()"
"Returns dictionary of a current local symbol table\n"
"** Python map()"
"Applies Function and Returns a List "
"** Python max()" 
"returns the largest item\n"
"** Python memoryview()"
"returns memory view of an argument"
"** Python min()"
"returns the smallest value\n"
"** Python next()"
"Retrieves next item from the iterator\n"
"** Python object()"
"creates a featureless object"
"** Python oct()"
"returns the octal representation of an integer\n"
"** Python open()"
"Returns a file object"
"** Python ord()"
"returns an integer of the Unicode character"
"** Python pow()"
"returns the power of a number\n"
"** Python print()"
"Prints the Given Object"
"** Python property()"
"returns the property attribute"
"** Python range()"
"returns a sequence of integers \n"
"** Python repr()"
"returns a printable representation of the object\n"
"** Python reversed()"
"returns the reversed iterator of a sequence"
"** Python round()"
"rounds a number to specified decimals\n"
"** Python set()"
"constructs and returns a set"
"** Python setattr()"
"sets the value of an attribute of an object\n"
"** Python slice()"
"returns a slice object"
"** Python sorted()"
"returns a sorted list from the given iterable\n"
"** Python staticmethod()"
"transforms a method into a static method"
"** Python str()"
"returns the string version of the object     \n"
"** Python sum()"
"Adds items of an Iterable"
"** Python super()"
"Returns a proxy object of the base class\n"
"** Python tuple()"
"Returns a tuple"
"** Python type()"
"Returns the type of the object\n"
"Python vars()"
"Returns the __dict__ attribute"
"** Python zip()"
"Returns an iterator of tuples\n"
"Python __import__()"
"Function called by the import statement", font="family, 13", justify=LEFT)
    l5.pack()


def factorial():
    root = Tk()
    root.geometry("1500x1500")
    root.title("Factorial")
    Label(root, text="Factorial\n\n\n\n\n"
                     "def factorial(n):\n\n"
                         "count = 1\n\n"
                         "  if n < 0:\n\n"
                             "return 'factorial not defined for negative numbers!'\n\n"
                     "elif n == 1 or n == 0:\n\n"
                         "return 1\n\n"
                     "else:\n\n"
                         "for i in range(2, n+1):\n\n"
                              "count *= i\n\n"
                         "retrun count\n\n"
"print(factorial(5))\n", font="family, 15", justify=LEFT).pack()


def fibonacci():
    root = Tk()
    root.geometry("1500x1500")
    root.title("Fibonacci")
    Label(root, text="Fibonacci Sequence\n\n\n\n"
                     "def fibonacci_sequence(n):\n\n"
                     "a, b = 0, 1\n\n"
                     "for i in range(n):\n\n"
                     "print(a)\n\n"
                     "a, b = b, a+b\n\n\n"
                     "fibonacci(10)", font="family, 20", justify=LEFT).pack()

l = Label(root, text="Python Homework", fg="black", font="Algerian, 25")
l.pack()

Label(root, text="1", font="20").pack()
l1 = Label(root, text="First Homework (Factorial)", fg="black", font="Algerian")
l1.pack()
b1 = Button(root, text="Factorial", bd=15, fg="green", bg="black", width=15, font="Algerian", command=factorial)
b1.pack()
Label(root, text="2", font="20").pack()
Label(root, text="Second Homework (Fibonacci)", fg="black", font="Algerian").pack()
b2 = Button(root, text="Fibonacci", bd=15, fg="green", bg="black", width=15, font="Algerian", command=fibonacci)
b2.pack()
Label(root, text="").pack()
Label(root, text="3", font="20").pack()
Label(root, text="Third Homework (Builtin Functions)", fg="black", font="Algerian").pack()
b3 = Button(root, text="Builtin Functions", bd=15, fg="green", bg="black", width=15, font="Algerian", command=Builtin)
b3.pack()
Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="Made by: Zabiullah 'Safi'", font="Algerian").pack()
Label(root, text="Faculty of Computer Science", font="Algerian").pack()
Label(root, text="Software Engineering Department", font="Algerian").pack()

root.mainloop()

