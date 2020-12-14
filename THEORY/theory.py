# 1.0 Data Types of Python
a_string = "like this" # str
a_number = 3 # int
a_float = 3.12 # float
a_boolean = False #bool
a_none = None #NoneType

print(type(a_boolean))

# 1.1 Lists in Python
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]  # list
print(type(days))

print("Mon" in days)  # True
print(days[1])  # Tue

# list is mutable sequence
print(days)
days.append("Sat")
print(days)
days.reverse()
print(days)

print(len(days))  # 5

# 1.2 Tuples and Dictionary
days_tuple = ("Mon", "Tue", "Wed", "Thur", "Fri")  # tuple is immuytable
print(type(days_tuple))
print(days_tuple)

# variable to dictionary
name = "dldid"
age = 30
korean = True
fav_food = ["pork cutlet", "pork belly"]

# set dictionary
dldid = {
    "name": "dldid",
    "age": 30,
    "korean": True,
    "fav_food": {"pork cutlet", "pork belly"}
}

print(dldid["name"]) # get item from a dictionary
dldid["handsome"] = True
print(dldid)
