# Locals
# lambda x: x**2

# Enclosing Function Locals

name = 'This is a global name!'


def greet():
    name = 'sammy'

    def hello():
        print("hello "+name)

    hello()


greet()
print(name)

# Built-in Functions

# Functions such as len()

# GLOBAL

x = 50


def func():
    global x
    x = 1000


print("before function call, x is: ", x)
func()
print("after function call, x is: ", x)
