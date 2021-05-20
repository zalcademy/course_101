import math
from lib.greetings import sayHello

import time
import datetime

# Hello World Project: 
# name = input()
# print("Hello " + name)

# Variables:
a = 25 # int
print(a)

b = 3.14 # float

c = "Zalcademy" # String

d = True # Boolean
e = False # Boolean

presentUsers = 31
presentUsers = presentUsers - 1
print(presentUsers)

f = b + a
print(f)

g = [1, 5, 8, 10, "zal", 45, "zal"]
print(g[4])

g.append("Bahman")
g.remove(10)
print(g)

print(g.count("zal"))

h = "bahman" in g
print(h)

i = [5, 2, 8, 10, 45, 123456]
i.sort()
print(i)

g.extend(i)

print("-----------------")
print(i)
print(g)

print(len(g))

g[12] = 45654654

print(1)
k = (1, 2, 3)
print(k)
# k[2] = 654456

l = set()
l.add(1)
l.add(2)
l.add(3)
l.add(2)
print(l)

l2 = set([1, 2, 3, 4, 4, 4, 4])
print(l2)

d1 = {"bahman": "09388309605", "Shakiba": "21546884684"}
d1["bahman"] = None
print(d1["bahman"])

print(type(d1))
print(type(l2))

a2 = int("15")
print(type(a2))

# Assignment operators:
# =, =+, =-, =/, =*
# 
# Arithmetic Operators:
# +, -, /, *
#
# Logical operators:
# >, <, >=, <=, ==, and, not
# True and True
# True and False
# True or True
# True or False
# False or False
print((5 == 5 and not 5 < 10))

x = 0
x += 1
x += 1
x += 4
x += 1

if x < 5:
    print("Allow the next person to enter")
elif x < 10 and x >= 5:
    print("Capacity is half full")
else:
    print("Full capacity")

print("Program finished")

counter = 0
while counter < 4:
    print(counter)
    counter += 1

print("-------------------")

for item in g:
    print(item * 2)

for item in range(10):
    if item == 2:
        continue
    if item == 6:
        break
    print(item)

def greeting(name, lastname):
    print("Hello " + name + " " + lastname)
    return name + " " + lastname

res = greeting("Bahman", "shadmehr")
greeting("Shakiba", "Lotf mohammadi")

print(res)

def customSum(a, b):
    a *= 2
    b *= 2
    return a + b

res = customSum(2, 2)
print(res)

print(math.ceil(3.97))

sayHello()

for i in range(5):
    time.sleep(0.5)
    print(i)

print(time.time())
print(datetime.datetime.now())
print(datetime.date.today())

classes = {
    "1": False,
    "2": False,
    "10": False,
}

userOption = input()
toReserveClass = input()
classId = input()
