a, b, c = 6, 6.5, "assignment1"
print(type(a), type(b), type(c))

b = 6 + 6j
print(type(b))

a, b = 1, 2
z = a, b
z = b, a

a, b = b, a
print(a, b)

x = input('enter your age')
print(x)

x = eval(input('enter a number between 1-10')) + eval(input('enter a number between 1-10'))
z = x + 30
print(z)

a = 25
print(type(a))

firstName = 'gayathri'
first_name = 'gayathri'
FIRSTNAME = 'gayathri'

# Declare a variable and initialize it
f = 0
print(f)

# re-declaring the variable works
f = "abc"
print(f)

# ERROR: variables of different types cannot be combined
# print ("string type " + 123)
print("string type " + str(123))


# Global vs. local variables in functions
def someFunction():
    # global f
    f = "def"
    print(f)


someFunction()
print(f)

del f
print(f)

#
# Example file for variables
#

# Declare a variable and initialize it
v = 12
# print(v)

# # re-declaring the variable works
v = 11
print(v)

# # ERROR: variables of different types cannot be combined
v = "vinay"
i = "29"
print(v + i)
# Global vs. local variables in functions
# global x
x = 1


def pra():
    global x
    x = 11
    print(x)


pra()

print(x)


def main():
    print("hello world")


if __name__ == "__main__":
    main()

f = 0
print(f)

f = "123"
print(f)

print("happy new year " + str(2020))

v = 28


def air():
    global v
    v = 'mvk'
    print(v)


air()
del v

v = 2285858
print(v)


def prac():
    print("i am practicing python")


prac()
print(prac())
print(prac)
