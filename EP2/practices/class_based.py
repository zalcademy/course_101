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


class AdminUser(Person):
    def __init__(self, name, lName, phoneNo):
        self.access = 'admin'
        super().__init__(name, lName, phoneNo)

    # def callUser(self):
    #     print('Cannot call admin user')


class OperatorUser(Person):
    def __init__(self, name, lName, phoneNo, internalNo):
        self.internalNo = internalNo
        super().__init__(name, lName, phoneNo)

    def callUser(self):
        print("We are calling operator with internal Id {}".format(self.internalNo))


class SimpleUser(Person):
    def callUser(self):
        print("Calling simple user {} {} ".format(self.name, self.lName))


s = SimpleUser("Bahman", "Shadmehr", "09388309605")
o = OperatorUser("Zalcademy", "-", "09388309605", 2)
a = AdminUser("Shakiba", "Lotf Mohammadi", "09388309605")

users = [s, o, a]

for user in users:
    user.callUser()

print("Total user count: {}".format(Person.counter))
