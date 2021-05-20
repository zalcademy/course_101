class Person():
    """
    This is a base class for defigning other user classess in our project
    """

    counter = 0

    def __init__(self, userName, userLastName, userPhoneNo):
        self.name = userName
        self.lname = userLastName
        self.phoneNo = userPhoneNo
        Person.counter += 1

    def __str__(self):
        return "User with name -> " + self.name + " " + self.lname

    def speak(self):
        print("Horay, I can speak")

    def sayMyName(self):
        print(self.name + " " + self.lname)



print(Person.counter)


p1 = Person("Bahman", "Shadmehr", "09388309605")

Person.counter = 5

p2 = Person("Shakiba", "Lotf mohammadi", "09388309605")

print(p1.name)
print(p2.lname)

print(Person.counter)
print(p2.counter)

# p1.sayMyName()

# p2.sayMyName()

# print(p1)
