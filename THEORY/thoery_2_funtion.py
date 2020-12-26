# function define
def say_hello():
    print("hello")
    print("bye")


say_hello()


def plus(a, b):
    print(a + b)


plus(2, 5)


def minus(a, b=2):
    print(a - b)


minus(2)


def say_hello(name="anonymous"):
    print("hello", name)


say_hello("dhddldid")


# return

def p_plus(a, b):
    print(a + b)


def r_plus(a, b):
    return a + b


p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)  # None, 5

# Keyworded Arguments
result = r_plus(b=30, a=-15)
print(result)


def say_hello(name, age):
    return f"Hello {name} you are {age} years old"


hello = say_hello("dhddl", "30")
print(hello)


def plus(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None



print(plus(12, "10"))
