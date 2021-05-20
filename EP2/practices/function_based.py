# User creation
user1 = {
    "name": "Bahman",
    "lname": "Shadmehr",
    "phoneNo": "09388309605",
    "access": "simple"
}

user2 = {
    "name": "Shakiba",
    "lname": "Lotf Mohammadi",
    "phoneNo": "2",
    "access": "admin"
}

user3 = {
    "name": "Zalcademy",
    "lname": "-",
    "phoneNo": "1231242134235",
    "access": "operator",
    "employementId": 2
}

users = [user1, user2, user3]

# wrong defenition of a user, this will cause an error
user4 = {
    "first_name": "Wrong",
    "last_name": "User",
    "phone_number": "1231242134235",
    "access": "simple"
}
# users.append(user4) # This line will cause an error

# Calling admin
def callAdmin(user):
    if user['access'] != 'admin':
        return
    print("@@@")
    print("We are calling admin with interanl number of {}\n".format(user['phoneNo']))

# def calling SimpleUser
def callSimpleUser(user):
    print("...")
    print("We are calling user {} {}\n".format(user["name"], user["lname"]))

# Calling users
def callUser(user):
    if user['access'] == 'admin':
        callAdmin(user)
    elif user['access'] == 'operator':
        pass
    else:
        callSimpleUser(user)

for u in users:
    callUser(u)
