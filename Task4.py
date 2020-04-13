#  1

def notdiv5_mult7(input_list):
    input_list = filter(lambda x: x % 5 != 0, input_list)
    input_list = filter(lambda x: x % 7 == 0, input_list)

    return list(input_list)

# 2 

def mult_list(int_square):
    return (int_square ** 2)


def map_list(list_a):
    return list(map(mult_list, list_a))


#  3

def find_upper(stringy):
    return [char for char in stringy if char.isupper() == True]


#  4

Student = ['Smit', 'Jaya', 'Rayyan']
Capital = ['CSE', 'Networking', 'Operating System']


def into_dict(x, y):
    return dict(zip(x, y))


into_dict(Student, Capital)

#  6

input_string = 'Consultadd Training'


def rev_list_gen(inp_string):
    new_string = ''
    for i in range(len(inp_string) - 1, -1, -1):
        new_string = new_string + inp_string[i]
        yield new_string


def rev_string():
    for i in rev_list_gen(input_string):
        print(i)


rev_string()

#  7

def decorator_function(example_function):
    def another_func():
        print('Here is my decorator function.')

        example_function()

        if isinstance(example_function(), str):
            print('The inserted function is a string')

        elif not isinstance(example_function(), str):
            print('The inserted function is not a string')

    return another_func()


def insert_func():
    a = 'I am a string'
    print(a)
    return a




