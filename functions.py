# Functions
# Code block that can be reused later in the programme

# Creating a function

# def print_something(print_string):
#     print(print_string)
#
# print_something("something")

# Greeting function

# def greeting(name):
#     print(f"Hello my name is " + name)
#
# greeting("Elena")

# Return statement

# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(2, 2))

# Default arguments/parameters

def addition(int1=2, int2=2):
    return int1 + int2

print(addition())
print(addition(7, 3))

# Multiple arguments

def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5)
multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

