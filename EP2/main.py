from abc import ABC, abstractmethod

class Person(ABC):
    counter = 0

    def __init__(self, name, lName, phoneNo):
        self.name = name
        self.lName = lName
        self.phoneNo = phoneNo
        Person.counter += 1

    @abstractmethod
    def callUser(self):
        pass


class SimpleUser(Person):
    def callUser(self):
        print("Calling simple user {} {} ".format(self.name, self.lName))


class OperatorUser(Person):
    def __init__(self, name, lName, phoneNo, internalNumber):
        self.internalNumber = internalNumber
        super().__init__(name, lName, phoneNo)

    def callUser(self):
        print("Calling user with internal number {}".format(self.internalNumber))

class AdminUser(Person):
    def callUser(self):
        print("Cannot call admin")


s = SimpleUser("Bahman", "shadmehr", "09388309605")
o = OperatorUser("Zalcademy", "-", "09388309605", 4)
a = AdminUser("Shakiba", "Lotfmohammadi", "09388309605")

users = [s, o, a]

for user in users:
    user.callUser()
