print("Hello, world!")

name = input("Name: ")

print("Hello, " + name)

#formatted string

print(f"Hello, {name}")

# Conditions
# Indentations are required
# Had to cast int bc otherwise interpreted as str

n = int(input("Number: "))

if n > 0:
    print("N is positive")
elif n < 0:
    print ("n is negative")
else:
    print("n is not positive")

# Sequences

name = "Harry"

print(name[0]) #first char, "H"

# List = seq of mutable values

names = ["Harry", "Ron", "Hermione"]
print(names)
print(names[0])
# Adds list item
names.append("Draco")
print(names[3])
# Alphabetical automatic sort
names.sort()


# Tuples, like coordinates for ex
# sequence of immutable vals

coordinate = (10.0, 20.0)
# Linked now

# Set = collection of unique vals

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(s)
# Remove things from set
s.remove(2)
print(s)
# Length of sequence (list, sets, tuples, etc.)
print(f"The set has {len(s)} elems.")

# Dict = collection of key-val pairs
# key: val
houses = {"Harry": "Gryf", "Draco": "Slyth"}
print(houses["Harry"])
# add or change val in dict
houses["Hermione"] = "Gryf"
print(houses["Hermione"])

# Loops
for i in range(6):
    print(i)

for name in names:
    print(name)

# Functions
def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")

# Can import functions from other .py files
# from functions (filename) import square (funct)
# can also just say import functions, but would require functions.square
# for funct call

# OOP
# class
class Point():
        #init = function called everytime point is created
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(2, 8)
print(p.x)
print(p.y)

# Class w/ functions

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
for person in names:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")

# Functional programming + decorators (announce in this case)

def announce(f):
    def wrapper():
        print("About to run function...")
        f()
        print("Finished running function")
    return wrapper

@announce
def hello():
    print("Hello, world")

hello()

# Lambda
# dicts inside lists

people = [
    {"name": "Harry", "house": "Gryf"},
    {"name": "Draco", "house": "Slyth"},
    {"name": "Cho", "house": "Raven"}
]


def f(person):
    return person["name"]

# sort using names as key
people.sort(key=f)

print(people)

# Lambda timeeee

people.sort(key=lambda person: person["house"])
print(people)

# Try?

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid Input")
    sys.exit(1)

try:
        result = x / y
        
# if try to divide by 0
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    sys.exit(1)

print(f"{x} / {y} = {result}")