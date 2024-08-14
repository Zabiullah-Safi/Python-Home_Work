
# -------------------------------------------------------------------------------------
class person:
    name = "ahmad"
    age = 19

print("the name of the person is:", person.name)
print("the age of the person is:", person.age)

--------------------------------------------------------------------------------------
class person:
    name = "ahmad"
    def greet(self, name):
        self.name = name
        return f"Hello {person.name} how are you"

print(person().greet(person()))
-----------------------------------------------------------------------------------------
class Car:
    make = "canada"
    year = 2024
    model = "Range Rover"
    def detail(self):
        return f"This car made in {Car.make} in {Car.year} and the model of this car is {Car.model}"

print(Car().detail())
-------------------------------------------------------------------------------------------
class Circle:
    def __int__(self, radius):
        self.radius = radius
        return (3.14 * (radius ** 2))


print(Circle().__int__(10))

---------------------------------------------------------------------------------------------
class Rectangle:
    def area(self, width, length):
        self.length = length
        self.width = width
        return self.length * self.width

print(Rectangle().area(9, 4))
---------------------------------------------****---------------------------------------------------
class Animal:
    def speak(self):
        return "the all animal of speak"
    def Dog(speak):
        return "the dog of sound is wak wak wak"


    def Cat(speak):
        return "the cat of sound is meow meow meow"

print(Animal().speak())
print(Animal().Dog())
print(Animal().Cat())
-------------------------------------------------****-----------------------------------------------------
class Shape:
    def area(self):
        return "the area of the shapes"

class Square(Shape):
    def area(self):
        return "the area of the square"

class Triangle(Shape):
    def area(self):
        return "the area of the triangle"

print(Shape().area())
print(Square().area())
print(Triangle().area())

--------------------------------------------------****-----------------------------------------------------

class Employee:
    name = "ahmad"
    salary = 40000

class Manager(Employee):
    department = "management"
print(Employee().name)
print(Employee().salary)
print(Manager().department)

----------------------------------------------------------------------------------------------------------

class Vehicle:
    def drive(self):
        return "you can drive the all of vehicle"

class Bike(Vehicle):
    def drive(self):
        return "you can drive the bike"

class Truck:
    def drive(self):
        return "you can drive the truck"

print(Vehicle().drive())
print(Bike().drive())
print(Truck().drive())

------------------------------------------------------------------------------------------------------------

class Bird:
    def fly(self):
        return "all of the birds can fly!"


class Eagle:
    def fly(self):
        return "Eagles can fly!"


class Penguin:
    def fly(self):
        return "penguin can not fly!"


print(Bird().fly())
print(Eagle().fly())
print(Penguin().fly())



----------------------------------------------------------------------------------------------------------------

class Book:
    title = "kabul"
    author = "ahmad"
    page = 500

    def get(self):
        return self.title, self.page, self.author

    def setter(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page


print(Book().get())
print(Book().setter("kabul", "ahmad", 500))

-------------------------------------------------------------------------------------------------------



class Ticket:
    def __int__(self, movie_name, seat_number, price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price

    def display_ticket(self):
        print(f"film: {self.movie_name}\nseat_number: {self.seat_number}\nprice: {self.price}")

    def apply_discount(self, discount_percentage):
        discount_amount = (self.price * discount_percentage) / 100
        self.price -= discount_amount
        print(f"apply discount {discount_percentage}%: new price is {self.price}$ ")


ticket = Ticket()
ticket.display_ticket()
ticket.apply_discount(10)
ticket.display_ticket()


-----------------------------------------------------------------------------------



class Bank_Account:
    Account_number = 2020
    Account = 40000

    def account(self):
        self.Account = Bank_Account.Account
        self.Account_number = Bank_Account.Account_number

    def deposit(self, deposit):
        self.Account += deposit

    def withdraw(self, withdraw):
        self.Account -= withdraw

    def check(self):
        return self.Account


Bank = Bank_Account()
print(Bank.check())
(Bank.account())
(Bank.deposit(90))
(Bank.withdraw(100))
print(Bank.check())


-----------------------------------------------------------------------------


class Team:
    def __init__(self):
        self.member = []

    def add(self, name):
        self.member.append(name)
        print(f"{name} added to the team!")

    def remove(self, name):
        if name in self.member:
            self.member.remove(name)
            print(f"{name} removed the from the team!")

        else:
            print(f"{name} is not in the team!")

    def show_member(self):
        print("current members:", {self.member})


team = Team()
team.add("ali")
team.add("zabiullah")
team.show_member()
team.remove("zabiullah")
team.show_member()

------------------------------------------------------------------------------

from tkinter import *
from tkinter import tkinter
class CounterApp(Tk):
    def __init__(self):
        super(CounterApp, self)
        self.minseze(500, 600)
        self.counter = 0
        self.button()

    def decrement(self):
        if self.counter >= 1:
            self.counter -= 1
            self.Label.config(text=f"the number is {str(self.counter)}"
        elif self.counter < 1:
            self.button.config(state="disable")





class WeatherApp:
    self.root = root
    self.root.title("WeatherApp")
    self.city = tk.Label(root, text="city")
    self.city.pack()
    self.city2 = tk.Entry(root)
    self.city.pack()
    self.get = tk.Button(root, text="click")
    self.get.pack()
    self.info = tk.Label(root, text="")
    sefl.info.pack()

    def get(self):
        city = self.city_entry.get().strip()
        if city:
            temp = random.randint(-10, 40)
            condition = random.choice(["sunny", "rainy", "cloudy"])
            self.weather_info.config(text="weather message")
            else:
                messagebox.showwarning("input Error", "pleace enter city name")

if __name__ == "__main__"
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
    












