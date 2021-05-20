p1 = {
    "name": "Bahman",
    "lname": "Shadmehr",
    "phoneNo": "09388309605",
    "role": "simple"
}

p2 = {
    "name": "Zalcademy",
    "lname": "-",
    "phoneNo": "09388309605",
    "internalNumber": 5,
    "role": "operator"
}

p3 = {
    "name": "Shakiba",
    "lname": "Lotf Mohammadi",
    "phoneNo": "09388309605",
    "role": "admin"
}

users = [p1, p2, p3]

p4 = {
    "firstanem": "Ali",
    "last_name": "Shadmehr",
    "phone_number": "54658456"
}
# users.append(p4) # This will cause an error

def callSimpleUser(user):
    print("We are calling {} {} at {}".format(user["name"], user["lname"], user["phoneNo"]))

def callOperator(user):
    print("Calling operator with internal number of {}".format(user["internalNumber"]))

def callUser(user):
    if user["role"] == "simple":
        callSimpleUser(user)
    elif user["role"] == "operator":
        callOperator(user)
    else:
        print("Cannot call this user")

for user in users:
    callUser(user)
